"""Whisper Backend 基礎介面."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol


@dataclass(frozen=True)
class TranscriptionSegment:
    """轉錄片段."""
    start: float  # 開始時間（秒）
    end: float    # 結束時間（秒）
    text: str     # 轉錄文字


@dataclass(frozen=True)
class TranscriptionResult:
    """轉錄結果."""
    text: str                           # 完整文字
    language: str                       # 偵測到的語言
    segments: list[TranscriptionSegment]  # 時間戳記片段
    
    @property
    def word_count(self) -> int:
        """估算字數."""
        return len(self.text.split())


class WhisperBackend(ABC):
    """Whisper 後端抽象基礎類別."""
    
    def __init__(self, model: str, language: str | None = None) -> None:
        """初始化後端.
        
        Args:
            model: 模型名稱（如 "tiny", "base", "small"）
            language: 語言代碼，若為 None 則自動偵測
        """
        self.model_name = model
        self.language = language
        self._is_loaded = False
    
    @property
    @abstractmethod
    def name(self) -> str:
        """後端名稱."""
        ...
    
    @property
    def is_loaded(self) -> bool:
        """模型是否已載入."""
        return self._is_loaded
    
    @abstractmethod
    def load(self) -> None:
        """載入模型.
        
        Raises:
            TranscribeError: 載入失敗
        """
        ...
    
    @abstractmethod
    def transcribe(self, audio_path: Path) -> TranscriptionResult:
        """轉錄音訊檔案.
        
        Args:
            audio_path: 音訊檔案路徑
            
        Returns:
            轉錄結果
            
        Raises:
            TranscribeError: 轉錄失敗
        """
        ...
    
    def unload(self) -> None:
        """卸載模型釋放資源."""
        self._is_loaded = False


class BackendFactory:
    """後端工廠 - 創建適當的 Whisper 後端."""
    
    @staticmethod
    def create(
        backend: str,
        model: str,
        language: str | None = None,
    ) -> WhisperBackend:
        """創建 Whisper 後端.
        
        Args:
            backend: 後端類型（"openai", "cpp", "faster-whisper"）
            model: 模型名稱
            language: 語言代碼
            
        Returns:
            WhisperBackend 實例
            
        Raises:
            ValueError: 不支援的後端類型
            ImportError: 缺少必要的依賴
        """
        if backend == "openai":
            from transcriber.backends.openai_whisper import OpenAIWhisperBackend
            return OpenAIWhisperBackend(model, language)
        
        elif backend == "cpp":
            from transcriber.backends.whisper_cpp import WhisperCppBackend
            return WhisperCppBackend(model, language)
        
        elif backend == "faster-whisper":
            from transcriber.backends.faster_whisper import FasterWhisperBackend
            return FasterWhisperBackend(model, language)
        
        else:
            raise ValueError(f"不支援的 Whisper 後端: {backend}")
    
    @staticmethod
    def list_available() -> list[str]:
        """列出可用的後端.
        
        Returns:
            可用後端名稱列表
        """
        available = []
        
        # 檢查 openai-whisper
        try:
            import whisper
            available.append("openai")
        except ImportError:
            pass
        
        # 檢查 whisper.cpp
        try:
            import whisper_cpp
            available.append("cpp")
        except ImportError:
            pass
        
        # 檢查 faster-whisper
        try:
            from faster_whisper import WhisperModel
            available.append("faster-whisper")
        except ImportError:
            pass
        
        return available
