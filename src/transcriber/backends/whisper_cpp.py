"""whisper.cpp 後端實作（預留，Phase 3 實作）."""

from pathlib import Path

from transcriber.backends.base import TranscriptionResult, WhisperBackend
from transcriber.core.errors import ErrorCategory, TranscribeError


class WhisperCppBackend(WhisperBackend):
    """whisper.cpp 後端 - 使用 C++ 實作，效能更好."""
    
    def __init__(self, model: str, language: str | None = None) -> None:
        super().__init__(model, language)
        self._model = None
    
    @property
    def name(self) -> str:
        return "whisper.cpp"
    
    def load(self) -> None:
        """載入模型."""
        try:
            import whisper_cpp
            
            # TODO: 實作 whisper.cpp 載入
            # 需要先下載對應的 ggml 模型檔案
            raise NotImplementedError(
                "whisper.cpp 後端尚未實作，請使用 openai 後端"
            )
            
        except ImportError:
            raise TranscribeError(
                "未安裝 whisper-cpp-python，請執行：pip install whisper-cpp-python",
                category=ErrorCategory.SYSTEM,
            )
    
    def transcribe(self, audio_path: Path) -> TranscriptionResult:
        """轉錄音訊."""
        raise NotImplementedError("whisper.cpp 後端尚未實作")
