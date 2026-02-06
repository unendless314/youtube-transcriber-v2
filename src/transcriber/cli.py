"""CLI 入口 - 已改為使用 yt-dlp CLI 掃描頻道."""

import json
import subprocess
import sys
from pathlib import Path

import click
import structlog
from rich.console import Console

from transcriber import __version__
from transcriber.config.manager import ConfigManager
from transcriber.core.progress import ProgressTracker
from transcriber.core.retry import RetryEngine, StageRetryWrapper
from transcriber.core.state import StateManager
from transcriber.pipeline.context import ProcessingContext
from transcriber.pipeline.orchestrator import Pipeline
from transcriber.pipeline.stages import (
    CleanupStage,
    DownloadStage,
    SaveStage,
    TranscribeStage,
)

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
    """從 YouTube URL 提取影片 ID."""
    import re
    
    if "youtu.be/" in url:
        match = re.search(r'youtu\.be/([^?&]+)', url)
        if match:
            return match.group(1)
    
    match = re.search(r'[?&]v=([^?&]+)', url)
    if match:
        return match.group(1)
    
    match = re.search(r'/shorts/([^?&]+)', url)
    if match:
        return match.group(1)
    
    import hashlib
    return hashlib.md5(url.encode()).hexdigest()[:11]


def _check_output_exists(output_dir: Path, video_id: str) -> bool:
    """檢查輸出目錄中是否已存在該 video_id 的 Markdown 檔案.
    
    這是防止數據庫遺失時重複處理的雙重保險機制。
    檔案命名格式: {date}_{video_id}_{title}.md
    
    Args:
        output_dir: 輸出根目錄
        video_id: YouTube 影片 ID
        
    Returns:
        是否找到匹配的輸出檔案
    """
    if not output_dir.exists():
        return False
    
    # 遞迴搜尋所有 .md 檔案，檢查檔名是否包含 video_id
    for md_file in output_dir.rglob("*.md"):
        if video_id in md_file.name:
            return True
    
    return False


def get_channel_videos(
    channel_config: dict,
    max_videos: int,
    cookies_file: Path | None,
    cookies_from_browser: str | None = None,
) -> list[dict]:
    """取得頻道的影片列表 (透過 yt-dlp CLI)."""
    url = channel_config["url"]
    
    # 準備 yt-dlp 指令
    cmd = [
        "yt-dlp",
        "--quiet",
        "--no-warnings",
        "--flat-playlist",
        "--dump-json",
        "--playlist-end", str(max_videos),
        url
    ]
    
    if cookies_file:
        cmd.extend(["--cookiefile", str(cookies_file)])
    elif cookies_from_browser:
        cmd.extend(["--cookies-from-browser", cookies_from_browser])
    
    try:
        # 執行並獲取 JSON 輸出
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # yt-dlp 在 dump-json 時，如果是播放清單/頻道，會每行輸出一個 entry 的 JSON
        videos = []
        for line in result.stdout.strip().split('\n'):
            if not line:
                continue
            entry = json.loads(line)
            
            video_id = entry.get("id") or extract_video_id(entry.get("url", ""))
            video_url = entry.get("url") or f"https://www.youtube.com/watch?v={video_id}"
            
            videos.append({
                "video_id": video_id,
                "title": entry.get("title", "Unknown"),
                "url": video_url,
            })
        
        return videos
            
    except subprocess.CalledProcessError as e:
        logger.error("failed_to_fetch_channel_cli", channel=channel_config["name"], error=e.stderr)
        return []
    except Exception as e:
        logger.error("failed_to_fetch_channel_unexpected", channel=channel_config["name"], error=str(e))
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
    "--no-progress",
    is_flag=True,
    help="停用進度顯示",
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
    no_progress: bool,
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
    
    # 創建控制台
    console = Console()
    
    # 創建進度追蹤器
    progress = ProgressTracker(console)
    if no_progress:
        progress.disable()
    
    # 初始化狀態管理器
    with StateManager(state_db) as state_manager:
        # 清理舊記錄
        deleted = state_manager.cleanup()
        if deleted > 0:
            logger.info("cleaned_old_records", count=deleted)
        
        # 建立重試引擎
        retry_engine = RetryEngine()
        
        # 建立 Pipeline（帶重試）
        pipeline = Pipeline(app_config, state_manager)
        pipeline.add_stage(StageRetryWrapper(DownloadStage(app_config, state_manager), retry_engine))
        pipeline.add_stage(StageRetryWrapper(TranscribeStage(app_config, state_manager), retry_engine))
        pipeline.add_stage(SaveStage(app_config, state_manager))
        pipeline.add_stage(CleanupStage(app_config, state_manager))
        
        # 收集所有頻道的影片資訊
        channel_videos = []
        all_channels_info = []
        
        for channel in app_config.channels:
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
                app_config.global_config.cookies_from_browser,
            )
            
            if videos:
                channel_videos.append((channel, videos))
                all_channels_info.append((channel.name, len(videos)))
        
        if not channel_videos:
            console.print("[yellow]沒有找到可處理的影片[/yellow]")
            sys.exit(0)
        
        # 使用進度追蹤器
        with progress:
            # 開始追蹤頻道
            progress.start_channels(all_channels_info)
            
            # 處理每個頻道
            for channel, videos in channel_videos:
                progress.start_channel(channel.name)
                
                logger.info("processing_channel", name=channel.name, video_count=len(videos))
                
                # 處理每部影片
                for i, video in enumerate(videos, 1):
                    video_id = video["video_id"]
                    title = video["title"]
                    url = video["url"]
                    
                    # 更新進度 - 當前處理
                    progress.update_video(title, "processing")
                    
                    # 檢查是否已處理（數據庫狀態）
                    if state_manager.is_processed(video_id):
                        progress.update_video(title, "skipped")
                        logger.info("video_already_processed_db", video_id=video_id)
                        continue
                    
                    # 檢查輸出檔案是否已存在（防止數據庫遺失導致重複處理）
                    output_dir = app_config.output.base_dir
                    if _check_output_exists(output_dir, video_id):
                        progress.update_video(title, "skipped")
                        logger.info("video_already_processed_file", video_id=video_id, output_dir=str(output_dir))
                        # 標記為已完成，避免下次再檢查
                        state_manager.mark_completed(video_id, "")
                        continue
                    
                    if dry_run:
                        progress.update_video(title, "skipped")
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
                        progress.update_video(title, "completed")
                        logger.info("video_processed", video_id=video_id)
                    except Exception as e:
                        progress.update_video(title, "failed")
                        logger.error("video_failed", video_id=video_id, error=str(e))
                        # 繼續處理下一部影片
                        continue
        
        # 列印摘要（如果啟用了進度顯示）
        if not no_progress:
            progress.print_summary()
    
    logger.info("youtube_transcriber_finished")


if __name__ == "__main__":
    main()