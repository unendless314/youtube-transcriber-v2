"""重試機制測試."""

import time
from unittest.mock import MagicMock

import pytest

from transcriber.core.errors import ErrorCategory, TranscriberError
from transcriber.core.retry import RetryEngine, RetryPolicy


class TestRetryPolicy:
    """測試重試策略."""
    
    def test_default_values(self):
        """測試預設值."""
        policy = RetryPolicy()
        assert policy.max_retries == 3
        assert policy.base_delay == 1.0
        assert policy.max_delay == 60.0
        assert policy.exponential_base == 2.0
        assert policy.jitter is True
    
    def test_custom_values(self):
        """測試自定義值."""
        policy = RetryPolicy(
            max_retries=5,
            base_delay=2.0,
            max_delay=300.0,
        )
        assert policy.max_retries == 5
        assert policy.base_delay == 2.0
        assert policy.max_delay == 300.0


class TestRetryEngine:
    """測試重試引擎."""
    
    def test_success_no_retry(self):
        """測試成功時不重試."""
        engine = RetryEngine()
        operation = MagicMock(return_value="success")
        
        result = engine.execute(operation, "test_op")
        
        assert result == "success"
        assert operation.call_count == 1
    
    def test_retry_on_network_error(self):
        """測試網路錯誤時重試."""
        engine = RetryEngine()
        operation = MagicMock(side_effect=[
            TranscriberError("timeout", ErrorCategory.NETWORK),
            TranscriberError("timeout", ErrorCategory.NETWORK),
            "success"
        ])
        
        result = engine.execute(operation, "test_op")
        
        assert result == "success"
        assert operation.call_count == 3
    
    def test_no_retry_on_video_error(self):
        """測試影片錯誤時不重試."""
        engine = RetryEngine()
        operation = MagicMock(side_effect=
            TranscriberError("private", ErrorCategory.VIDEO)
        )
        
        with pytest.raises(TranscriberError) as exc_info:
            engine.execute(operation, "test_op")
        
        assert exc_info.value.category == ErrorCategory.VIDEO
        assert operation.call_count == 1  # 不重試
    
    def test_exhausted_retries(self):
        """測試重試耗盡."""
        policies = {
            ErrorCategory.NETWORK: RetryPolicy(max_retries=2, base_delay=0.01)
        }
        engine = RetryEngine(policies)
        operation = MagicMock(side_effect=
            TranscriberError("timeout", ErrorCategory.NETWORK)
        )
        
        with pytest.raises(TranscriberError):
            engine.execute(operation, "test_op")
        
        # 初始嘗試 + 2 次重試
        assert operation.call_count == 3
    
    def test_calculate_delay_with_jitter(self):
        """測試抖動延遲計算."""
        engine = RetryEngine()
        policy = RetryPolicy(base_delay=1.0, exponential_base=2.0, jitter=True)
        
        # 第 1 次重試：約 1-2 秒
        delay1 = engine._calculate_delay(1, policy)
        assert 0.5 <= delay1 <= 2.0
        
        # 第 2 次重試：約 2-4 秒
        delay2 = engine._calculate_delay(2, policy)
        assert 1.0 <= delay2 <= 4.0
    
    def test_calculate_delay_respects_max(self):
        """測試延遲不超過最大值."""
        engine = RetryEngine()
        policy = RetryPolicy(base_delay=10.0, max_delay=15.0, exponential_base=2.0, jitter=False)
        
        delay = engine._calculate_delay(10, policy)  # 第 10 次重試
        assert delay <= 15.0
    
    def test_should_retry(self):
        """測試是否應該重試."""
        engine = RetryEngine()
        
        assert engine.should_retry(TranscriberError("", ErrorCategory.NETWORK))
        assert engine.should_retry(TranscriberError("", ErrorCategory.RATE_LIMIT))
        assert not engine.should_retry(TranscriberError("", ErrorCategory.VIDEO))
        assert not engine.should_retry(TranscriberError("", ErrorCategory.SYSTEM))
