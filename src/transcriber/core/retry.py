"""智能重試機制."""

import random
import time
from dataclasses import dataclass
from typing import Callable

import structlog

from transcriber.core.errors import ErrorCategory, TranscriberError

logger = structlog.get_logger(__name__)


@dataclass(frozen=True)
class RetryPolicy:
    """重試策略配置."""
    
    max_retries: int = 3
    base_delay: float = 1.0  # 基礎延遲（秒）
    max_delay: float = 60.0  # 最大延遲（秒）
    exponential_base: float = 2.0  # 指數退避基數
    jitter: bool = True  # 是否加入隨機抖動


# 預設重試策略
DEFAULT_POLICIES: dict[ErrorCategory, RetryPolicy] = {
    ErrorCategory.NETWORK: RetryPolicy(
        max_retries=3,
        base_delay=1.0,
        max_delay=30.0,
    ),
    ErrorCategory.RATE_LIMIT: RetryPolicy(
        max_retries=5,
        base_delay=5.0,
        max_delay=300.0,  # 最多等 5 分鐘
    ),
    ErrorCategory.RESOURCE: RetryPolicy(
        max_retries=2,
        base_delay=3.0,
        max_delay=10.0,
    ),
    # VIDEO 和 SYSTEM 錯誤不重試
    ErrorCategory.VIDEO: RetryPolicy(max_retries=0),
    ErrorCategory.SYSTEM: RetryPolicy(max_retries=0),
    ErrorCategory.UNKNOWN: RetryPolicy(max_retries=1),
}


class RetryEngine:
    """重試引擎 - 執行帶重試機制的操作."""
    
    def __init__(self, policies: dict[ErrorCategory, RetryPolicy] | None = None) -> None:
        """初始化重試引擎.
        
        Args:
            policies: 自定義重試策略，若為 None 使用預設策略
        """
        self.policies = policies or DEFAULT_POLICIES
        self.logger = structlog.get_logger(__name__)
    
    def execute(
        self,
        operation: Callable,
        operation_name: str,
        context: dict | None = None,
    ) -> any:
        """執行操作並在失敗時重試.
        
        Args:
            operation: 要執行的操作函數
            operation_name: 操作名稱（用於日誌）
            context: 額外上下文資訊
            
        Returns:
            操作結果
            
        Raises:
            TranscriberError: 達到最大重試次數後仍失敗
        """
        ctx = context or {}
        last_error: TranscriberError | None = None
        
        # 先嘗試執行一次，取得錯誤分類
        try:
            return operation()
        except TranscriberError as e:
            last_error = e
            category = e.category
        except Exception as e:
            from transcriber.core.errors import ErrorClassifier
            category = ErrorClassifier.classify(e)
            last_error = TranscriberError(str(e), category)
        
        # 取得該錯誤類型的重試策略
        policy = self.policies.get(category, RetryPolicy(max_retries=0))
        
        if policy.max_retries == 0:
            self.logger.debug(
                "no_retry_for_error",
                operation=operation_name,
                category=category.name,
            )
            raise last_error
        
        # 執行重試
        for attempt in range(1, policy.max_retries + 1):
            delay = self._calculate_delay(attempt, policy)
            
            self.logger.info(
                "retrying_operation",
                operation=operation_name,
                attempt=attempt,
                max_retries=policy.max_retries,
                category=category.name,
                delay=delay,
                **ctx
            )
            
            time.sleep(delay)
            
            try:
                result = operation()
                self.logger.info(
                    "retry_succeeded",
                    operation=operation_name,
                    attempt=attempt,
                    **ctx
                )
                return result
                
            except TranscriberError as e:
                last_error = e
                # 如果錯誤類型改變，可能需要調整策略
                if e.category != category:
                    new_policy = self.policies.get(e.category, RetryPolicy(max_retries=0))
                    if attempt >= new_policy.max_retries:
                        break
                    category = e.category
                        
            except Exception as e:
                from transcriber.core.errors import ErrorClassifier
                new_category = ErrorClassifier.classify(e)
                last_error = TranscriberError(str(e), new_category)
                if new_category != category:
                    if attempt >= self.policies.get(new_category, RetryPolicy(max_retries=0)).max_retries:
                        break
                    category = new_category
        
        # 重試耗盡
        self.logger.error(
            "retry_exhausted",
            operation=operation_name,
            max_retries=policy.max_retries,
            category=category.name,
            error=str(last_error),
            **ctx
        )
        raise last_error
    
    def _calculate_delay(self, attempt: int, policy: RetryPolicy) -> float:
        """計算重試延遲時間（指數退避 + 抖動）."""
        # 指數退避：base_delay * (exponential_base ^ (attempt - 1))
        delay = policy.base_delay * (policy.exponential_base ** (attempt - 1))
        delay = min(delay, policy.max_delay)
        
        # 加入抖動避免雷群
        if policy.jitter:
            # 隨機因子：0.5 ~ 1.5
            jitter_factor = 0.5 + random.random()
            delay *= jitter_factor
        
        return delay
    
    def should_retry(self, error: TranscriberError) -> bool:
        """判斷該錯誤是否應該重試.
        
        Args:
            error: 錯誤物件
            
        Returns:
            是否應該重試
        """
        policy = self.policies.get(error.category, RetryPolicy(max_retries=0))
        return policy.max_retries > 0


class StageRetryWrapper:
    """Stage 重試包裝器 - 為 Stage 添加重試能力."""
    
    def __init__(self, stage: "Stage", retry_engine: RetryEngine | None = None) -> None:
        """初始化包裝器.
        
        Args:
            stage: 要包裝的 Stage
            retry_engine: 重試引擎，若為 None 使用預設
        """
        self.stage = stage
        self.retry_engine = retry_engine or RetryEngine()
    
    @property
    def name(self) -> str:
        return self.stage.name
    
    def should_skip(self, context: "ProcessingContext") -> bool:
        return self.stage.should_skip(context)
    
    def execute(self, context: "ProcessingContext") -> "ProcessingContext":
        """執行 Stage，失敗時重試."""
        operation = lambda: self.stage.execute(context)
        
        return self.retry_engine.execute(
            operation,
            operation_name=f"stage_{self.stage.name}",
            context={
                "video_id": context.video_id,
                "channel": context.channel_name,
            }
        )
