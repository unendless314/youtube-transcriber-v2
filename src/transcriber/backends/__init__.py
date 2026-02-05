"""Whisper Backend 模組."""

from .base import (
    BackendFactory,
    TranscriptionResult,
    TranscriptionSegment,
    WhisperBackend,
)

__all__ = [
    "BackendFactory",
    "TranscriptionResult",
    "TranscriptionSegment",
    "WhisperBackend",
]
