"""錯誤處理整合測試."""

import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from transcriber.config.models import Config
from transcriber.core.errors import (
    DownloadError,
    ErrorCategory,
    TranscribeError,
    TranscriberError,
)
from transcriber.core.retry import RetryEngine, RetryPolicy
from transcriber.core.state import StateManager, VideoStatus
from transcriber.pipeline.context import ProcessingContext
from transcriber.pipeline.stages import DownloadStage, TranscribeStage


class TestErrorHandlingIntegration:
    """錯誤處理整合測試."""
    
    @pytest.fixture
    def setup(self):
        """提供測試環境."""
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            
            config = Config(
                output={"base_dir": tmp_path / "output", "temp_dir": tmp_path / "temp"},
                channels=[{"name": "Test", "url": "https://youtube.com/@test"}],
            )
            
            db_path = tmp_path / "test.db"
            state_manager = StateManager(db_path)
            
            yield config, state_manager, tmp_path
            
            state_manager.close()
    
    def test_network_error_retry_then_success(self, setup):
        """測試網路錯誤重試後成功."""
        config, state_manager, tmp_path = setup
        
        # 建立重試引擎（快速重試）
        policies = {
            ErrorCategory.NETWORK: RetryPolicy(max_retries=3, base_delay=0.01)
        }
        engine = RetryEngine(policies)
        
        # 模擬操作：前 2 次失敗，第 3 次成功
        call_count = [0]
        def operation():
            call_count[0] += 1
            if call_count[0] < 3:
                raise TranscriberError("timeout", ErrorCategory.NETWORK)
            return "success"
        
        result = engine.execute(operation, "test_op")
        
        assert result == "success"
        assert call_count[0] == 3  # 初始 + 2 次重試
    
    def test_video_error_no_retry(self, setup):
        """測試影片錯誤不重試."""
        config, state_manager, tmp_path = setup
        
        engine = RetryEngine()
        
        call_count = [0]
        def operation():
            call_count[0] += 1
            raise TranscriberError("private video", ErrorCategory.VIDEO)
        
        with pytest.raises(TranscriberError) as exc_info:
            engine.execute(operation, "test_op")
        
        assert exc_info.value.category == ErrorCategory.VIDEO
        assert call_count[0] == 1  # 不重試
    
    def test_error_state_recorded(self, setup):
        """測試錯誤狀態被記錄."""
        config, state_manager, tmp_path = setup
        
        # 標記影片並模擬失敗
        state_manager.mark_pending("vid1", "Test", "Video 1")
        state_manager.mark_status(
            "vid1",
            VideoStatus.FAILED,
            error_message="Download failed",
            error_category="NETWORK",
        )
        
        # 驗證錯誤被記錄
        state = state_manager.get_state("vid1")
        assert state.status == VideoStatus.FAILED
        assert state.error_message == "Download failed"
        assert state.error_category == "NETWORK"
        assert state.retry_count == 1
    
    def test_retry_count_tracking(self, setup):
        """測試重試次數追蹤."""
        config, state_manager, tmp_path = setup
        
        state_manager.mark_pending("vid1", "Test", "Video 1")
        
        # 多次標記為失敗
        for _ in range(3):
            state_manager.mark_status("vid1", VideoStatus.FAILED)
        
        state = state_manager.get_state("vid1")
        assert state.retry_count == 3
    
    def test_transient_error_recovery(self, setup):
        """測試暫時性錯誤恢復."""
        config, state_manager, tmp_path = setup
        
        # 第 1 次：網路錯誤
        state_manager.mark_pending("vid1", "Test", "Video 1")
        state_manager.mark_status("vid1", VideoStatus.FAILED, "timeout", "NETWORK")
        
        # 重試：成功
        state_manager.mark_status("vid1", VideoStatus.DOWNLOADING)
        state_manager.mark_status("vid1", VideoStatus.DOWNLOADED)
        state_manager.mark_completed("vid1")
        
        # 驗證最終狀態
        assert state_manager.is_processed("vid1")
        state = state_manager.get_state("vid1")
        assert state.status == VideoStatus.COMPLETED
        assert state.error_message is None  # 錯誤被清除
