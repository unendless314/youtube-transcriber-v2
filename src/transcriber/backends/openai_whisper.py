"""OpenAI Whisper 後端實作."""

from pathlib import Path

import structlog

from transcriber.backends.base import (
    TranscriptionResult,
    TranscriptionSegment,
    WhisperBackend,
)
from transcriber.core.errors import ErrorCategory, TranscribeError

logger = structlog.get_logger(__name__)


class OpenAIWhisperBackend(WhisperBackend):
    """OpenAI Whisper 官方實作後端."""
    
    def __init__(self, model: str, language: str | None = None) -> None:
        super().__init__(model, language)
        self._model = None
        self.logger = structlog.get_logger(__name__, backend="openai", model=model)
    
    @property
    def name(self) -> str:
        return "openai-whisper"
    
    def load(self) -> None:
        """載入 Whisper 模型."""
        if self._is_loaded:
            return
        
        try:
            import whisper
            
            self.logger.info("loading_model", model=self.model_name)
            self._model = whisper.load_model(self.model_name)
            self._is_loaded = True
            self.logger.info("model_loaded")
            
        except Exception as e:
            error_msg = f"無法載入 Whisper 模型 '{self.model_name}': {e}"
            self.logger.error("load_failed", error=str(e))
            raise TranscribeError(
                error_msg,
                category=ErrorCategory.SYSTEM,
            ) from e
    
    def transcribe(self, audio_path: Path) -> TranscriptionResult:
        """轉錄音訊."""
        if not self._is_loaded:
            self.load()
        
        if self._model is None:
            raise TranscribeError(
                "模型未載入",
                category=ErrorCategory.SYSTEM,
            )
        
        self.logger.debug("transcribing", path=str(audio_path))
        
        try:
            # 執行轉錄
            result = self._model.transcribe(
                str(audio_path),
                language=self.language,
                verbose=False,
            )
            
            # 轉換結果格式
            segments = [
                TranscriptionSegment(
                    start=seg.get("start", 0.0),
                    end=seg.get("end", 0.0),
                    text=seg.get("text", "").strip(),
                )
                for seg in result.get("segments", [])
            ]
            
            # 偵測到的語言
            detected_language = result.get("language", self.language or "unknown")
            
            transcription = TranscriptionResult(
                text=result.get("text", "").strip(),
                language=detected_language,
                segments=segments,
            )
            
            self.logger.info(
                "transcribe_complete",
                language=detected_language,
                segments=len(segments),
                word_count=transcription.word_count,
            )
            
            return transcription
            
        except Exception as e:
            error_str = str(e).lower()
            
            # 判斷錯誤類型
            if any(kw in error_str for kw in ["cuda", "gpu", "out of memory"]):
                category = ErrorCategory.RESOURCE
            elif "file" in error_str or "not found" in error_str:
                category = ErrorCategory.SYSTEM
            else:
                category = ErrorCategory.UNKNOWN
            
            self.logger.error("transcribe_failed", error=str(e), category=category.name)
            raise TranscribeError(
                f"轉錄失敗: {e}",
                category=category,
            ) from e
    
    def unload(self) -> None:
        """卸載模型."""
        if self._model is not None:
            import torch
            # 釋放 GPU 記憶體
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            self._model = None
            self._is_loaded = False
            self.logger.debug("model_unloaded")
