"""Pipeline Stage 實作."""

import re
import shutil
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

import structlog
import yt_dlp

from transcriber.config.models import Config
from transcriber.core.errors import DownloadError, ErrorCategory, TranscribeError
from transcriber.core.state import StateManager, VideoStatus
from transcriber.pipeline.context import ProcessingContext

logger = structlog.get_logger(__name__)


class Stage(ABC):
    """Pipeline Stage 基礎類別."""
    
    def __init__(self, config: Config, state_manager: StateManager) -> None:
        self.config = config
        self.state = state_manager
        self.logger = structlog.get_logger(__name__, stage=self.name)
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Stage 名稱."""
        ...
    
    @abstractmethod
    def execute(self, context: ProcessingContext) -> ProcessingContext:
        """執行 Stage.
        
        Args:
            context: 處理上下文
            
        Returns:
            更新後的上下文
            
        Raises:
            TranscriberError: 處理失敗
        """
        ...
    
    def should_skip(self, context: ProcessingContext) -> bool:
        """判斷是否應該跳過此 Stage.
        
        Args:
            context: 處理上下文
            
        Returns:
            是否應該跳過
        """
        return False


class DownloadStage(Stage):
    """下載 Stage - 使用 yt-dlp 下載音訊."""
    
    @property
    def name(self) -> str:
        return "download"
    
    def should_skip(self, context: ProcessingContext) -> bool:
        """若已下載則跳過."""
        video_state = self.state.get_state(context.video_id)
        if video_state and video_state.status in (VideoStatus.DOWNLOADED, VideoStatus.COMPLETED):
            # 檢查檔案是否存在
            if context.audio_path and context.audio_path.exists():
                self.logger.info("skip_download", reason="already_downloaded", video_id=context.video_id)
                return True
        return False
    
    def execute(self, context: ProcessingContext) -> ProcessingContext:
        """下載影片音訊."""
        self.logger.info("downloading", video_id=context.video_id, title=context.title)
        self.state.mark_status(context.video_id, VideoStatus.DOWNLOADING)
        
        # 設定輸出目錄
        temp_dir = self.config.output.temp_dir
        temp_dir.mkdir(parents=True, exist_ok=True)
        
        # 設定 yt-dlp 選項
        ydl_opts = self._build_ydl_opts(context, temp_dir)
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                # 先取得影片資訊以檢查時長
                info = ydl.extract_info(context.url, download=False)
                
                if info is None:
                    raise DownloadError(
                        f"無法取得影片資訊: {context.url}",
                        category=ErrorCategory.VIDEO,
                    )
                
                duration = info.get("duration", 0)
                context.duration = duration
                context.published_at = info.get("upload_date", "")
                
                # 檢查時長限制
                max_duration = self._get_max_duration(context.channel_name)
                if duration > max_duration * 60:
                    raise DownloadError(
                        f"影片長度 {duration//60} 分鐘超過限制 {max_duration} 分鐘",
                        category=ErrorCategory.VIDEO,
                    )
                
                # 執行下載
                ydl.download([context.url])
                
                # 找出下載的檔案
                output_path = temp_dir / f"{context.video_id}.mp3"
                if not output_path.exists():
                    # yt-dlp 可能使用不同命名，搜尋檔案
                    output_path = self._find_downloaded_file(temp_dir, context.video_id)
                
                if output_path and output_path.exists():
                    context.audio_path = output_path
                    self.state.mark_status(context.video_id, VideoStatus.DOWNLOADED)
                    self.logger.info("download_complete", video_id=context.video_id, path=str(output_path))
                else:
                    raise DownloadError(
                        "下載完成但找不到輸出檔案",
                        category=ErrorCategory.SYSTEM,
                    )
                
        except yt_dlp.utils.DownloadError as e:
            error_str = str(e).lower()
            
            # 判斷錯誤類型
            if any(kw in error_str for kw in ["private", "unavailable", "removed", "members only"]):
                category = ErrorCategory.VIDEO
            elif any(kw in error_str for kw in ["network", "timeout", "connection"]):
                category = ErrorCategory.NETWORK
            else:
                category = ErrorCategory.UNKNOWN
            
            raise DownloadError(f"yt-dlp 錯誤: {e}", category=category) from e
        
        return context
    
    def _build_ydl_opts(self, context: ProcessingContext, temp_dir: Path) -> dict[str, Any]:
        """建構 yt-dlp 選項."""
        opts: dict[str, Any] = {
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "outtmpl": str(temp_dir / f"{context.video_id}.%(ext)s"),
            "quiet": True,
            "no_warnings": True,
        }
        
        # 加入 cookies
        if self.config.global_config.cookies_file:
            opts["cookiefile"] = str(self.config.global_config.cookies_file)
        
        return opts
    
    def _get_max_duration(self, channel_name: str) -> int:
        """取得頻道的最大時長限制."""
        # 先找頻道特定設定
        for ch in self.config.channels:
            if ch.name == channel_name and ch.max_duration is not None:
                return ch.max_duration
        # 使用全域設定
        return self.config.global_config.max_duration
    
    def _find_downloaded_file(self, temp_dir: Path, video_id: str) -> Path | None:
        """搜尋已下載的檔案."""
        for ext in [".mp3", ".m4a", ".webm", ".opus"]:
            path = temp_dir / f"{video_id}{ext}"
            if path.exists():
                return path
        # 搜尋任何包含 video_id 的檔案
        for f in temp_dir.iterdir():
            if video_id in f.name and f.is_file():
                return f
        return None


class TranscribeStage(Stage):
    """轉錄 Stage - 使用 Whisper 轉錄音訊."""
    
    def __init__(self, config: Config, state_manager: StateManager, backend = None) -> None:
        super().__init__(config, state_manager)
        self._backend = backend
        self._backend_instance = None
    
    @property
    def name(self) -> str:
        return "transcribe"
    
    def should_skip(self, context: ProcessingContext) -> bool:
        """若已完成轉錄則跳過."""
        video_state = self.state.get_state(context.video_id)
        if video_state and video_state.status == VideoStatus.COMPLETED:
            self.logger.info("skip_transcribe", reason="already_completed", video_id=context.video_id)
            return True
        return False
    
    def _get_backend(self):
        """取得或創建 Whisper 後端."""
        if self._backend_instance is None:
            from transcriber.backends.base import BackendFactory
            
            language = self._get_language()
            language = None if language == "auto" else language
            
            self._backend_instance = BackendFactory.create(
                backend=self.config.whisper.backend,
                model=self.config.whisper.model,
                language=language,
            )
            self._backend_instance.load()
        
        return self._backend_instance
    
    def execute(self, context: ProcessingContext) -> ProcessingContext:
        """轉錄音訊."""
        if not context.audio_path or not context.audio_path.exists():
            raise TranscribeError(
                "音訊檔案不存在，請先執行 DownloadStage",
                category=ErrorCategory.SYSTEM,
            )
        
        self.logger.info(
            "transcribing",
            video_id=context.video_id,
            backend=self.config.whisper.backend,
            model=self.config.whisper.model,
        )
        self.state.mark_status(context.video_id, VideoStatus.TRANSCRIBING)
        
        # 使用後端進行轉錄
        backend = self._get_backend()
        result = backend.transcribe(context.audio_path)
        
        # 儲存結果
        context.transcript = result.text
        context.transcript_segments = [
            {
                "start": seg.start,
                "end": seg.end,
                "text": seg.text,
            }
            for seg in result.segments
        ]
        
        self.logger.info(
            "transcribe_complete",
            video_id=context.video_id,
            word_count=result.word_count,
            segment_count=len(result.segments),
            language=result.language,
        )
        
        return context
    
    def _get_language(self) -> str:
        """取得頻道的語言設定."""
        # 先找頻道特定設定
        for ch in self.config.channels:
            if ch.name == ch.name and ch.language is not None:
                return ch.language
        # 使用全域設定
        return self.config.whisper.language


class SaveStage(Stage):
    """儲存 Stage - 將轉錄結果儲存為 Markdown."""
    
    @property
    def name(self) -> str:
        return "save"
    
    def execute(self, context: ProcessingContext) -> ProcessingContext:
        """儲存轉錄結果."""
        if not context.transcript:
            raise TranscribeError(
                "沒有轉錄結果可儲存",
                category=ErrorCategory.SYSTEM,
            )
        
        # 建構輸出路徑
        output_path = self._build_output_path(context)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        self.logger.info("saving", video_id=context.video_id, path=str(output_path))
        
        # 生成 Markdown 內容
        content = self._generate_markdown(context)
        
        # 寫入檔案
        output_path.write_text(content, encoding="utf-8")
        context.output_path = output_path
        
        self.logger.info("save_complete", video_id=context.video_id, path=str(output_path))
        return context
    
    def _build_output_path(self, context: ProcessingContext) -> Path:
        """建構輸出檔案路徑."""
        base_dir = self.config.output.base_dir
        channel_name = self._sanitize_filename(context.channel_name)
        
        # 從 published_at 提取年月 (格式: YYYYMMDD 或 YYYY-MM-DD)
        year_month = "unknown"
        if context.published_at:
            if len(context.published_at) >= 6:
                year_month = f"{context.published_at[:4]}-{context.published_at[4:6]}"
            elif "-" in context.published_at:
                parts = context.published_at.split("-")
                if len(parts) >= 2:
                    year_month = f"{parts[0]}-{parts[1]}"
        
        # 檔案名稱
        title_slug = self._sanitize_filename(context.title)[:50]  # 限制長度
        filename = f"{context.published_at or 'unknown'}_{context.video_id}_{title_slug}.md"
        
        return base_dir / channel_name / year_month / filename
    
    def _sanitize_filename(self, name: str) -> str:
        """清理檔案名稱中的非法字元."""
        # 移除或替換非法字元
        name = re.sub(r'[<>:"/\\|?*]', "_", name)
        name = re.sub(r'\s+', "_", name)
        return name.strip("._")
    
    def _generate_markdown(self, context: ProcessingContext) -> str:
        """生成 Markdown 內容."""
        # 計算字數
        word_count = len(context.transcript)
        
        # 格式化時長
        duration_str = self._format_duration(context.duration)
        
        # Front matter
        lines = [
            "---",
            f'channel: "{context.channel_name}"',
            f'video_id: "{context.video_id}"',
            f'title: "{context.title}"',
            f'published_at: "{context.published_at or "unknown"}"',
            f'duration: "{duration_str}"',
            f'word_count: {word_count}',
            "---",
            "",
            f"# {context.title}",
            "",
        ]
        
        # 加入時間戳記
        for segment in context.transcript_segments:
            start = segment.get("start", 0)
            text = segment.get("text", "").strip()
            if text:
                lines.append(f"[{self._format_timestamp(start)}] {text}")
        
        # 若沒有 segments，使用完整文字
        if not context.transcript_segments:
            lines.append(context.transcript)
        
        return "\n".join(lines)
    
    def _format_duration(self, seconds: int) -> str:
        """格式化時長為 HH:MM:SS."""
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        if hours > 0:
            return f"{hours}:{minutes:02d}:{secs:02d}"
        return f"{minutes}:{secs:02d}"
    
    def _format_timestamp(self, seconds: float) -> str:
        """格式化時間戳為 MM:SS."""
        mins = int(seconds) // 60
        secs = int(seconds) % 60
        return f"{mins:02d}:{secs:02d}"


class CleanupStage(Stage):
    """清理 Stage - 刪除暫存檔案."""
    
    @property
    def name(self) -> str:
        return "cleanup"
    
    def execute(self, context: ProcessingContext) -> ProcessingContext:
        """清理暫存檔案."""
        if context.audio_path and context.audio_path.exists():
            self.logger.info("cleaning_up", path=str(context.audio_path))
            try:
                context.audio_path.unlink()
                self.logger.debug("file_removed", path=str(context.audio_path))
            except OSError as e:
                self.logger.warning("cleanup_failed", path=str(context.audio_path), error=str(e))
        
        return context
