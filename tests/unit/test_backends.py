"""Whisper Backend 測試."""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from transcriber.backends.base import (
    BackendFactory,
    TranscriptionResult,
    TranscriptionSegment,
)
from transcriber.core.errors import ErrorCategory, TranscribeError


class TestTranscriptionSegment:
    """測試轉錄片段."""
    
    def test_creation(self):
        """測試創建."""
        seg = TranscriptionSegment(start=0.0, end=5.0, text="Hello")
        assert seg.start == 0.0
        assert seg.end == 5.0
        assert seg.text == "Hello"


class TestTranscriptionResult:
    """測試轉錄結果."""
    
    def test_creation(self):
        """測試創建."""
        result = TranscriptionResult(
            text="Hello world",
            language="en",
            segments=[],
        )
        assert result.text == "Hello world"
        assert result.language == "en"
    
    def test_word_count(self):
        """測試字數計算."""
        result = TranscriptionResult(
            text="Hello world foo bar",
            language="en",
            segments=[],
        )
        assert result.word_count == 4


class TestBackendFactory:
    """測試後端工廠."""
    
    def test_create_openai_backend(self):
        """測試創建 OpenAI 後端."""
        # 需要 mock import
        with patch("transcriber.backends.openai_whisper.OpenAIWhisperBackend") as mock_backend:
            instance = MagicMock()
            mock_backend.return_value = instance
            
            backend = BackendFactory.create("openai", "tiny", "zh")
            
            mock_backend.assert_called_once_with("tiny", "zh")
    
    def test_create_invalid_backend(self):
        """測試創建無效後端."""
        with pytest.raises(ValueError) as exc_info:
            BackendFactory.create("invalid", "tiny")
        
        assert "invalid" in str(exc_info.value).lower()
    
    def test_list_available_returns_list(self):
        """測試列出可用後端返回列表."""
        # 這個測試只是確認函數能執行並返回列表
        # 實際結果取決於環境中安裝了哪些套件
        available = BackendFactory.list_available()
        assert isinstance(available, list)
