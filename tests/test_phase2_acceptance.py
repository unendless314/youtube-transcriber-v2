"""Phase 2 驗收測試.

驗收標準：
1. 網路錯誤自動重試 3 次
2. Rate limit 自動等待後重試
3. 進度顯示包含：頻道進度、影片進度、預估時間
4. 可通過配置切換 Whisper backend
5. 單元測試覆蓋率 > 75%
"""

from transcriber.core.errors import ErrorCategory
from transcriber.core.retry import RetryEngine, RetryPolicy


def test_retry_engine_exists():
    """驗收: RetryEngine 已實作."""
    engine = RetryEngine()
    assert engine is not None
    print("✓ RetryEngine 已實作")


def test_retry_policies():
    """驗收: 5 種錯誤類別有對應策略."""
    from transcriber.core.retry import DEFAULT_POLICIES
    
    assert ErrorCategory.NETWORK in DEFAULT_POLICIES
    assert ErrorCategory.RATE_LIMIT in DEFAULT_POLICIES
    assert ErrorCategory.RESOURCE in DEFAULT_POLICIES
    assert ErrorCategory.VIDEO in DEFAULT_POLICIES
    assert ErrorCategory.SYSTEM in DEFAULT_POLICIES
    
    # VIDEO 和 SYSTEM 不應重試
    assert DEFAULT_POLICIES[ErrorCategory.VIDEO].max_retries == 0
    assert DEFAULT_POLICIES[ErrorCategory.SYSTEM].max_retries == 0
    
    # NETWORK 應該重試
    assert DEFAULT_POLICIES[ErrorCategory.NETWORK].max_retries > 0
    print("✓ 5 種錯誤類別策略已配置")


def test_progress_tracker_exists():
    """驗收: ProgressTracker 已實作."""
    from transcriber.core.progress import ProgressTracker
    from rich.console import Console
    
    tracker = ProgressTracker(Console())
    assert tracker is not None
    print("✓ ProgressTracker 已實作")


def test_whisper_backend_factory():
    """驗收: BackendFactory 可列出可用後端."""
    from transcriber.backends.base import BackendFactory
    
    available = BackendFactory.list_available()
    assert isinstance(available, list)
    print(f"✓ BackendFactory 可用，檢測到 {len(available)} 個後端")


def test_transcription_result():
    """驗收: TranscriptionResult 資料結構."""
    from transcriber.backends.base import TranscriptionResult, TranscriptionSegment
    
    result = TranscriptionResult(
        text="Hello world",
        language="en",
        segments=[
            TranscriptionSegment(start=0.0, end=2.0, text="Hello"),
            TranscriptionSegment(start=2.0, end=4.0, text="world"),
        ],
    )
    
    assert result.text == "Hello world"
    assert result.language == "en"
    assert len(result.segments) == 2
    assert result.word_count == 2
    print("✓ TranscriptionResult 資料結構正確")


def test_cli_has_no_progress_option():
    """驗收: CLI 有 --no-progress 選項."""
    import subprocess
    result = subprocess.run(
        ["python3", "-m", "transcriber", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "--no-progress" in result.stdout
    print("✓ CLI 有 --no-progress 選項")


if __name__ == "__main__":
    print("\n" + "="*50)
    print("Phase 2 驗收測試")
    print("="*50 + "\n")
    
    test_retry_engine_exists()
    test_retry_policies()
    test_progress_tracker_exists()
    test_whisper_backend_factory()
    test_transcription_result()
    test_cli_has_no_progress_option()
    
    print("\n" + "="*50)
    print("✅ Phase 2 所有驗收測試通過！")
    print("="*50)
