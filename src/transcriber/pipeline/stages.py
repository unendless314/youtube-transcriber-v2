"""Pipeline Stage 實作 - 改為呼叫系統 CLI 工具."""

import json
import random
import re
import subprocess
import time
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

import structlog

from transcriber.config.models import Config
from transcriber.core.errors import DownloadError, ErrorCategory, TranscribeError, TranscriberError
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
        """執行 Stage."""
        ...
    
    def should_skip(self, context: ProcessingContext) -> bool:
        """判斷是否應該跳過此 Stage."""
        return False


class DownloadStage(Stage):
    """下載 Stage - 使用系統安裝的 yt-dlp 執行檔."""
    
    @property
    def name(self) -> str:
        return "download"
    
    def should_skip(self, context: ProcessingContext) -> bool:
        """若已下載則跳過."""
        video_state = self.state.get_state(context.video_id)
        if video_state and video_state.status in (VideoStatus.DOWNLOADED, VideoStatus.COMPLETED):
            if context.audio_path and context.audio_path.exists():
                self.logger.info("skip_download", reason="already_downloaded", video_id=context.video_id)
                return True
        return False
    
    def _show_delay_progress(self, delay: float, video_id: str, channel_name: str) -> None:
        """顯示延遲等待進度，讓 AI Agent 知道程序正常運作中.
        
        注意：這個函數會直接輸出到 stdout，不與 Rich Progress 競爭。
        輸出格式設計為適合 AI Agent 解析。
        """
        delay_int = int(delay)
        
        # 使用 print 而非 Rich Console，避免被 Progress 條覆蓋
        # 格式：[RATE_LIMIT] 等待 XX 秒 | 頻道名稱 | video_id
        print(
            f"\n[RATE_LIMIT] 等待 {delay_int} 秒避免 YouTube 反爬蟲 | "
            f"頻道: {channel_name} | video: {video_id}",
            flush=True
        )
        
        # 每 15 秒輸出一個進度點
        elapsed = 0
        while elapsed < delay_int:
            sleep_time = min(15, delay_int - elapsed)
            time.sleep(sleep_time)
            elapsed += sleep_time
            remaining = delay_int - elapsed
            if remaining > 0:
                print(f"  ...還剩 {remaining} 秒", flush=True)
        
        print(f"  ✓ 等待完成，開始下載 {video_id}\n", flush=True)
    
    def execute(self, context: ProcessingContext) -> ProcessingContext:
        """下載影片音訊."""
        self.logger.info("downloading_via_cli", video_id=context.video_id, title=context.title)
        self.state.mark_status(context.video_id, VideoStatus.DOWNLOADING)
        
        # ===== 智慧延遲：避免觸發 YouTube 反爬蟲 =====
        # 只在「真的要下載」時延遲（已下載的影片會被 should_skip 跳過）
        delay = random.uniform(30, 90)  # 30-90 秒隨機延遲
        self.logger.info("rate_limit_delay", seconds=round(delay, 1), video_id=context.video_id)
        self._show_delay_progress(delay, context.video_id, context.channel_name)
        # ============================================
        
        temp_dir = self.config.output.temp_dir
        temp_dir.mkdir(parents=True, exist_ok=True)
        
        # 使用你系統中的 yt-dlp 執行檔 (通常在 /opt/homebrew/bin/yt-dlp)
        yt_dlp_bin = "yt-dlp" 
        
        try:
            # 1. 取得影片資訊
            info_cmd = [yt_dlp_bin, "--dump-json", context.url]
            if self.config.global_config.cookies_file:
                info_cmd.extend(["--cookiefile", str(self.config.global_config.cookies_file)])
            
            # 加入瀏覽器 cookies（如果設定）
            if self.config.global_config.cookies_from_browser:
                info_cmd.extend(["--cookies-from-browser", self.config.global_config.cookies_from_browser])
            
            self.logger.debug("fetching_video_info", command=" ".join(info_cmd))
            info_result = subprocess.run(info_cmd, capture_output=True, text=True, check=True)
            info = json.loads(info_result.stdout)
            
            duration = info.get("duration", 0)
            context.duration = duration
            context.published_at = self._format_upload_date(info.get("upload_date", ""))
            
            # 2. 檢查時長限制
            max_duration = self._get_max_duration(context.channel_name)
            if duration > max_duration * 60:
                raise DownloadError(
                    f"影片長度 {duration//60} 分鐘超過限制 {max_duration} 分鐘",
                    category=ErrorCategory.VIDEO,
                )
            
            # 3. 執行下載
            output_tmpl = str(temp_dir / f"{context.video_id}.%(ext)s")
            download_cmd = [
                yt_dlp_bin,
                "-x",  # extract audio
                "--audio-format", "mp3",
                "--audio-quality", "192K",
                "-o", output_tmpl,
                context.url
            ]
            if self.config.global_config.cookies_file:
                download_cmd.extend(["--cookiefile", str(self.config.global_config.cookies_file)])
            elif self.config.global_config.cookies_from_browser:
                download_cmd.extend(["--cookies-from-browser", self.config.global_config.cookies_from_browser])
            
            self.logger.info("starting_download_process", video_id=context.video_id)
            subprocess.run(download_cmd, capture_output=True, check=True)
            
            # 4. 確認輸出檔案
            output_path = temp_dir / f"{context.video_id}.mp3"
            if output_path.exists():
                context.audio_path = output_path
                self.state.mark_status(context.video_id, VideoStatus.DOWNLOADED)
                self.logger.info("download_complete", video_id=context.video_id, path=str(output_path))
            else:
                raise DownloadError("下載完成但找不到輸出檔案", category=ErrorCategory.SYSTEM)
                
        except subprocess.CalledProcessError as e:
            error_msg = e.stderr if e.stderr else str(e)
            self.logger.error("yt_dlp_cli_error", error=error_msg)
            
            # 檢查是否為會員專屬影片（預期無法處理，標記為 SKIPPED）
            error_lower = error_msg.lower()
            if any(kw in error_lower for kw in ["members only", "members-only", "channel's members", "membership"]):
                self.logger.info("members_only_video_detected", video_id=context.video_id)
                self.state.mark_skipped(context.video_id, reason="members_only")
                raise DownloadError(
                    "會員專屬影片，已標記為跳過",
                    category=ErrorCategory.VIDEO
                )
            
            # 解析錯誤類型，恢復精確的錯誤分類
            category = self._classify_ytdlp_error(error_msg)
            raise DownloadError(f"yt-dlp 執行失敗: {error_msg}", category=category)
        except TranscriberError:
            # 已經正確分類的錯誤（如時長過長），直接向上拋出不再重新包裝
            raise
        except Exception as e:
            self.logger.error("download_unexpected_error", error=str(e))
            raise DownloadError(f"下載過程發生未知錯誤: {e}", category=ErrorCategory.UNKNOWN)
        
        return context
    
    def _get_max_duration(self, channel_name: str) -> int:
        for ch in self.config.channels:
            if ch.name == channel_name and ch.max_duration is not None:
                return ch.max_duration
        return self.config.global_config.max_duration
    
    def _format_upload_date(self, upload_date: str) -> str:
        """將 yt-dlp 的 upload_date (YYYYMMDD) 轉換為 ISO 8601 格式 (YYYY-MM-DD)."""
        if not upload_date or len(upload_date) != 8:
            return upload_date
        try:
            year = upload_date[:4]
            month = upload_date[4:6]
            day = upload_date[6:8]
            return f"{year}-{month}-{day}"
        except (IndexError, ValueError):
            return upload_date
    
    def _classify_ytdlp_error(self, error_msg: str) -> ErrorCategory:
        """根據 yt-dlp 錯誤訊息分類錯誤類型."""
        error_lower = error_msg.lower()
        
        # YouTube 反爬蟲 / 需要登入
        bot_keywords = [
            "sign in to confirm you're not a bot",
            "sign in to confirm",
            "not a bot",
            "unable to extract uploader id"
        ]
        if any(kw in error_lower for kw in bot_keywords):
            return ErrorCategory.VIDEO  # 歸類為影片問題，但實際需要 cookies
        
        # 影片相關錯誤
        video_keywords = [
            "private", "unavailable", "removed", "members only",
            "video unavailable", "content unavailable", "deleted",
            "copyright", "blocked", "age-restricted", "age restricted",
            "not available", "does not exist", "couldn't find",
            "unable to extract", "unsupported url", "premieres in",
            "upcoming", "live stream"
        ]
        if any(kw in error_lower for kw in video_keywords):
            return ErrorCategory.VIDEO
        
        # 網路相關錯誤
        network_keywords = [
            "network", "timeout", "connection", "resolve", "dns",
            "temporary failure", "ssl", "certificate", "handshake",
            "too many requests", "rate limit", "429", "403", "502", "503",
            "unable to download", "fragment"
        ]
        if any(kw in error_lower for kw in network_keywords):
            return ErrorCategory.NETWORK
        
        return ErrorCategory.UNKNOWN


class TranscribeStage(Stage):
    """轉錄 Stage - 使用 Whisper 轉錄音訊."""
    
    def __init__(self, config: Config, state_manager: StateManager, backend = None) -> None:
        super().__init__(config, state_manager)
        self._forced_backend = backend
        self._backends: dict[tuple[str, str | None], Any] = {}
    
    @property
    def name(self) -> str:
        return "transcribe"
    
    def should_skip(self, context: ProcessingContext) -> bool:
        video_state = self.state.get_state(context.video_id)
        if video_state and video_state.status == VideoStatus.COMPLETED:
            self.logger.info("skip_transcribe", reason="already_completed", video_id=context.video_id)
            return True
        return False
    
    def _get_backend(self, language: str | None):
        if self._forced_backend:
            return self._forced_backend
            
        model = self.config.whisper.model
        key = (model, language)
        
        if key not in self._backends:
            from transcriber.backends.base import BackendFactory
            backend_lang = None if language == "auto" else language
            backend = BackendFactory.create(
                backend=self.config.whisper.backend,
                model=model,
                language=backend_lang,
                cpp_bin=self.config.whisper.cpp_bin,
                model_path=self.config.whisper.model_path,
            )
            backend.load()
            self._backends[key] = backend
        return self._backends[key]
    
    def execute(self, context: ProcessingContext) -> ProcessingContext:
        if not context.audio_path or not context.audio_path.exists():
            raise TranscribeError("音訊檔案不存在", category=ErrorCategory.SYSTEM)
        
        # 輸出轉錄開始提示（讓 AI Agent 知道進入轉錄階段）
        print(
            f"\n[TRANSCRIBE] 開始轉錄 | "
            f"頻道: {context.channel_name} | "
            f"backend: {self.config.whisper.backend} | "
            f"video: {context.video_id}",
            flush=True
        )
        
        self.logger.info(
            "transcribing",
            video_id=context.video_id,
            backend=self.config.whisper.backend,
            model=self.config.whisper.model,
        )
        self.state.mark_status(context.video_id, VideoStatus.TRANSCRIBING)
        
        language = self._get_language(context.channel_name)
        backend = self._get_backend(language)
        result = backend.transcribe(context.audio_path)
        
        context.transcript = result.text
        context.transcript_segments = [{"start": seg.start, "end": seg.end, "text": seg.text} for seg in result.segments]
        
        # 輸出轉錄完成提示
        print(
            f"  ✓ 轉錄完成 | 字數: {result.word_count} | 片段: {len(result.segments)} | "
            f"語言: {result.language}\n",
            flush=True
        )
        
        self.logger.info(
            "transcribe_complete",
            video_id=context.video_id,
            word_count=result.word_count,
            segment_count=len(result.segments),
            language=result.language,
        )
        return context
    
    def _get_language(self, channel_name: str) -> str:
        for ch in self.config.channels:
            if ch.name == channel_name and ch.language is not None:
                return ch.language
        return self.config.whisper.language


class SaveStage(Stage):
    """儲存 Stage - 將轉錄結果儲存為 Markdown."""
    
    @property
    def name(self) -> str:
        return "save"
    
    def execute(self, context: ProcessingContext) -> ProcessingContext:
        if not context.transcript:
            raise TranscribeError("沒有轉錄結果可儲存", category=ErrorCategory.SYSTEM)
        
        output_path = self._build_output_path(context)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        self.logger.info("saving_transcript", video_id=context.video_id, path=str(output_path))
        
        content = self._generate_markdown(context)
        output_path.write_text(content, encoding="utf-8")
        context.output_path = output_path
        
        self.logger.info("save_complete", video_id=context.video_id, path=str(output_path))
        return context
    
    def _build_output_path(self, context: ProcessingContext) -> Path:
        base_dir = self.config.output.base_dir
        channel_name = self._sanitize_filename(context.channel_name)
        year_month = "unknown"
        if context.published_at:
            # 支持 ISO 格式 (YYYY-MM-DD) 和舊格式 (YYYYMMDD)
            if len(context.published_at) >= 10 and context.published_at[4] == '-':
                # ISO 格式: 2026-02-05
                year_month = context.published_at[:7]
            elif len(context.published_at) >= 6:
                # 舊格式: 20260205
                year_month = f"{context.published_at[:4]}-{context.published_at[4:6]}"
        
        title_slug = self._sanitize_filename(context.title)[:50]
        filename = f"{context.published_at or 'unknown'}_{context.video_id}_{title_slug}.md"
        return base_dir / channel_name / year_month / filename
    
    def _sanitize_filename(self, name: str) -> str:
        name = re.sub(r'[<>:"/\\|?*]', "_", name)
        name = re.sub(r'\s+', "_", name)
        return name.strip("._")
    
    def _generate_markdown(self, context: ProcessingContext) -> str:
        word_count = len(context.transcript)
        duration_str = self._format_duration(context.duration)
        lines = [
            "---",
            f'channel: "{context.channel_name}"',
            f'video_id: "{context.video_id}"',
            f"title: '{context.title.replace(chr(39), chr(39)*2)}'",
            f'published_at: "{context.published_at or "unknown"}"',
            f'duration: "{duration_str}"',
            f'word_count: {word_count}',
            "---",
            "",
            f"# {context.title}",
            "",
        ]
        for segment in context.transcript_segments:
            start = segment.get("start", 0)
            text = segment.get("text", "").strip()
            if text:
                lines.append(f"[{self._format_timestamp(start)}] {text}")
        if not context.transcript_segments:
            lines.append(context.transcript)
        return "\n".join(lines)
    
    def _format_duration(self, seconds: int) -> str:
        hours, remainder = divmod(seconds, 3600)
        minutes, secs = divmod(remainder, 60)
        return f"{hours}:{minutes:02d}:{secs:02d}" if hours > 0 else f"{minutes}:{secs:02d}"
    
    def _format_timestamp(self, seconds: float) -> str:
        mins, secs = divmod(int(seconds), 60)
        return f"{mins:02d}:{secs:02d}"


class CleanupStage(Stage):
    """清理 Stage - 刪除暫存檔案."""
    
    @property
    def name(self) -> str:
        return "cleanup"
    
    def execute(self, context: ProcessingContext) -> ProcessingContext:
        if context.audio_path and context.audio_path.exists():
            self.logger.debug("cleaning_up_temp_file", path=str(context.audio_path))
            try:
                context.audio_path.unlink()
                self.logger.debug("temp_file_removed", path=str(context.audio_path))
            except OSError as e:
                self.logger.warning("cleanup_failed", path=str(context.audio_path), error=str(e))
        return context