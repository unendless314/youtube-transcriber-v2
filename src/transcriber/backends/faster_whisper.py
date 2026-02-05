"""faster-whisper 後端實作（預留，Phase 3 實作）."""

from pathlib import Path

from transcriber.backends.base import TranscriptionResult, WhisperBackend
from transcriber.core.errors import ErrorCategory, TranscribeError


class FasterWhisperBackend(WhisperBackend):
    """faster-whisper 後端 - 使用 CTranslate2，速度更快."""
    
    def __init__(self, model: str, language: str | None = None) -> None:
        super().__init__(model, language)
        self._model = None
    
    @property
    def name(self) -> str:
        return "faster-whisper"
    
    def load(self) -> None:
        """載入模型."""
        try:
            from faster_whisper import WhisperModel
            
            # TODO: 實作 faster-whisper 載入
            raise NotImplementedError(
                "faster-whisper 後端尚未實作，請使用 openai 後端"
            )
            
        except ImportError:
            raise TranscribeError(
                "未安裝 faster-whisper，請執行：pip install faster-whisper",
                category=ErrorCategory.SYSTEM,
            )
    
    def transcribe(self, audio_path: Path) -> TranscriptionResult:
        """轉錄音訊."""
        raise NotImplementedError("faster-whisper 後端尚未實作")
