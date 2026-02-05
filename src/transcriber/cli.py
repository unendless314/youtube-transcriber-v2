"""CLI 入口."""

import sys
from pathlib import Path

import click
import structlog

from transcriber.config.manager import ConfigManager
from transcriber.core.state import StateManager
from transcriber.pipeline.context import ProcessingContext
from transcriber.pipeline.orchestrator import create_default_pipeline
from transcriber import __version__

# 配置結構化日誌
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.dev.ConsoleRenderer(),
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger(__name__)


def extract_video_id(url: str) -> str:
    """從 YouTube URL 提取影片 ID.
    
    Args:
        url: YouTube URL
        
    Returns:
        影片 ID
    """
    # 支援格式：
    # - https://www.youtube.com/watch?v=VIDEO_ID
    # - https://youtu.be/VIDEO_ID
    # - https://www.youtube.com/shorts/VIDEO_ID
    
    import re
    
    # youtu.be 格式
    if "youtu.be/" in url:
        match = re.search(r'youtu\.be/([^?&]+)', url)
        if match:
            return match.group(1)
    
    # watch?v= 格式
    match = re.search(r'[?&]v=([^?&]+)', url)
    if match:
        return match.group(1)
    
    # shorts 格式
    match = re.search(r'/shorts/([^?&]+)', url)
    if match:
        return match.group(1)
    
    # 無法解析，使用 URL 雜湊
    import hashlib
    return hashlib.md5(url.encode()).hexdigest()[:11]


def get_channel_videos(channel_config: dict, max_videos: int, cookies_file: Path | None) -> list[dict]:
    """取得頻道的影片列表.
    
    Args:
        channel_config: 頻道配置
        max_videos: 最大影片數
        cookies_file: cookies 檔案路徑
        
    Returns:
        影片資訊列表
    """
    import yt_dlp
    
    url = channel_config["url"]
    
    # 建構 yt-dlp 選項
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": True,  # 只取得列表，不下載
        "playlistend": max_videos,
    }
    
    if cookies_file:
        ydl_opts["cookiefile"] = str(cookies_file)
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # 提取頻道資訊
            info = ydl.extract_info(url, download=False)
            
            if not info or "entries" not in info:
                logger.warning("no_videos_found", channel=channel_config["name"], url=url)
                return []
            
            videos = []
            for entry in info["entries"]:
                if not entry:
                    continue
                
                video_id = entry.get("id") or extract_video_id(entry.get("url", ""))
                video_url = entry.get("url") or f"https://www.youtube.com/watch?v={video_id}"
                
                videos.append({
                    "video_id": video_id,
                    "title": entry.get("title", "Unknown"),
                    "url": video_url,
                })
            
            return videos
            
    except Exception as e:
        logger.error("failed_to_fetch_channel", channel=channel_config["name"], error=str(e))
        return []


@click.command()
@click.option(
    "--config", "-c",
    type=click.Path(exists=True, path_type=Path),
    required=True,
    help="配置文件路徑 (YAML 格式)",
)
@click.option(
    "--output", "-o",
    type=click.Path(path_type=Path),
    help="輸出目錄（覆寫配置）",
)
@click.option(
    "--state-db",
    type=click.Path(path_type=Path),
    help="狀態資料庫路徑（預設：{output}/.transcriber.db）",
)
@click.option(
    "--dry-run", "-n",
    is_flag=True,
    help="測試模式：只檢查不實際下載/轉錄",
)
@click.option(
    "--verbose", "-v",
    is_flag=True,
    help="詳細輸出",
)
@click.option(
    "--init-config",
    type=click.Path(path_type=Path),
    help="建立範例配置文件並退出",
)
@click.version_option(version=__version__, prog_name="youtube-transcriber")
def main(
    config: Path | None,
    output: Path | None,
    state_db: Path | None,
    dry_run: bool,
    verbose: bool,
    init_config: Path | None,
) -> None:
    """YouTube Transcriber - 自動轉錄 YouTube 頻道影片."""
    
    # 初始化配置文件
    if init_config:
        ConfigManager.create_sample_config(init_config)
        click.echo(f"範例配置已建立: {init_config}")
        sys.exit(0)
    
    # 檢查必要參數
    if not config:
        click.echo("錯誤: 必須指定 --config", err=True)
        sys.exit(1)
    
    # 設定日誌級別
    if verbose:
        import logging
        logging.getLogger().setLevel(logging.DEBUG)
    
    logger.info("youtube_transcriber_started", version=__version__, dry_run=dry_run)
    
    # 載入配置
    try:
        config_manager = ConfigManager(config)
        app_config = config_manager.load()
    except FileNotFoundError as e:
        click.echo(f"錯誤: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"配置錯誤: {e}", err=True)
        sys.exit(1)
    
    # 覆寫輸出目錄
    if output:
        app_config.output.base_dir = output
    
    # 確保輸出目錄存在
    app_config.output.base_dir.mkdir(parents=True, exist_ok=True)
    app_config.output.temp_dir.mkdir(parents=True, exist_ok=True)
    
    # 設定狀態資料庫路徑
    if not state_db:
        state_db = app_config.output.base_dir / ".transcriber.db"
    
    # 初始化狀態管理器
    with StateManager(state_db) as state_manager:
        # 清理舊記錄
        deleted = state_manager.cleanup()
        if deleted > 0:
            logger.info("cleaned_old_records", count=deleted)
        
        # 建立 Pipeline
        pipeline = create_default_pipeline(app_config, state_manager)
        
        # 處理每個頻道
        total_processed = 0
        total_skipped = 0
        total_failed = 0
        
        for channel in app_config.channels:
            logger.info(
                "processing_channel",
                name=channel.name,
                url=channel.url,
            )
            
            # 取得影片列表
            channel_dict = {
                "name": channel.name,
                "url": channel.url,
                "language": channel.language,
                "max_duration": channel.max_duration,
            }
            
            videos = get_channel_videos(
                channel_dict,
                app_config.global_config.max_videos_check,
                app_config.global_config.cookies_file,
            )
            
            if not videos:
                logger.warning("no_videos_found", channel=channel.name)
                continue
            
            click.echo(f"\n頻道: {channel.name} - 找到 {len(videos)} 部影片")
            
            # 處理每部影片
            for i, video in enumerate(videos, 1):
                video_id = video["video_id"]
                title = video["title"]
                url = video["url"]
                
                # 檢查是否已處理
                if state_manager.is_processed(video_id):
                    click.echo(f"  [{i}/{len(videos)}] ⏭️  已處理: {title[:50]}...")
                    total_skipped += 1
                    continue
                
                click.echo(f"  [{i}/{len(videos)}] 處理: {title[:50]}...")
                
                if dry_run:
                    click.echo(f"    📝 測試模式，跳過處理")
                    total_skipped += 1
                    continue
                
                # 建立處理上下文
                context = ProcessingContext(
                    video_id=video_id,
                    channel_name=channel.name,
                    title=title,
                    url=url,
                )
                
                # 執行 Pipeline
                try:
                    pipeline.process(context)
                    total_processed += 1
                    click.echo(f"    ✅ 完成: {context.output_path}")
                except Exception as e:
                    total_failed += 1
                    click.echo(f"    ❌ 失敗: {e}")
                    # 繼續處理下一部影片
                    continue
        
        # 輸出摘要
        click.echo("\n" + "="*50)
        click.echo("處理摘要:")
        click.echo(f"  成功: {total_processed}")
        click.echo(f"  跳過: {total_skipped}")
        click.echo(f"  失敗: {total_failed}")
    
    logger.info("youtube_transcriber_finished")


if __name__ == "__main__":
    main()
