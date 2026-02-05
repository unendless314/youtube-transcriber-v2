"""錯誤分類與定義."""

from enum import Enum, auto
from typing import Any


class ErrorCategory(Enum):
    """錯誤分類，用於決定重試策略."""
    
    NETWORK = auto()       # 網路問題，立即重試
    RATE_LIMIT = auto()    # 請求頻率限制，延遲重試
    RESOURCE = auto()      # 資源不足（記憶體、磁碟），換小模型或清理
    VIDEO = auto()         # 影片問題（不存在、版權、私人），永久跳過
    SYSTEM = auto()        # 系統問題，終止程式
    UNKNOWN = auto()       # 未知錯誤，保守處理


class TranscriberError(Exception):
    """基礎錯誤類別."""
    
    def __init__(
        self,
        message: str,
        category: ErrorCategory = ErrorCategory.UNKNOWN,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.category = category
        self.details = details or {}


class ConfigError(TranscriberError):
    """配置錯誤."""
    
    def __init__(self, message: str, details: dict[str, Any] | None = None) -> None:
        super().__init__(message, ErrorCategory.SYSTEM, details)


class DownloadError(TranscriberError):
    """下載錯誤."""
    
    def __init__(
        self,
        message: str,
        category: ErrorCategory = ErrorCategory.NETWORK,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message, category, details)


class TranscribeError(TranscriberError):
    """轉錄錯誤."""
    
    def __init__(
        self,
        message: str,
        category: ErrorCategory = ErrorCategory.RESOURCE,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message, category, details)


class StateError(TranscriberError):
    """狀態管理錯誤."""
    
    def __init__(self, message: str, details: dict[str, Any] | None = None) -> None:
        super().__init__(message, ErrorCategory.SYSTEM, details)


class ErrorClassifier:
    """錯誤分類器，將異常轉換為錯誤分類."""
    
    # 關鍵字對應的錯誤分類
    _KEYWORDS: dict[ErrorCategory, list[str]] = {
        ErrorCategory.NETWORK: [
            "network",
            "connection",
            "timeout",
            "unreachable",
            "reset",
            "refused",
            "temporary failure",
            "ssl",
            "certificate",
        ],
        ErrorCategory.RATE_LIMIT: [
            "rate limit",
            "too many requests",
            "429",
            "slow down",
            "throttle",
        ],
        ErrorCategory.RESOURCE: [
            "memory",
            "disk full",
            "no space",
            "resource",
            "cuda out of memory",
            "gpu",
        ],
        ErrorCategory.VIDEO: [
            "not available",
            "private",
            "removed",
            "copyright",
            "age restricted",
            "members only",
            "login required",
            "video unavailable",
            "premiere",
            "upcoming",
            "live stream",
        ],
        ErrorCategory.SYSTEM: [
            "permission denied",
            "file not found",
            "database",
            "corrupt",
        ],
    }
    
    @classmethod
    def classify(cls, error: Exception) -> ErrorCategory:
        """將異常分類為錯誤類別.
        
        Args:
            error: 異常物件
            
        Returns:
            錯誤分類
        """
        # 如果是已知的 TranscriberError，直接使用其分類
        if isinstance(error, TranscriberError):
            return error.category
        
        # 根據錯誤訊息內容分類
        error_str = str(error).lower()
        error_type = type(error).__name__.lower()
        
        for category, keywords in cls._KEYWORDS.items():
            for keyword in keywords:
                if keyword in error_str or keyword in error_type:
                    return category
        
        return ErrorCategory.UNKNOWN
    
    @classmethod
    def should_retry(cls, category: ErrorCategory) -> bool:
        """判斷該錯誤是否應該重試.
        
        Args:
            category: 錯誤分類
            
        Returns:
            是否應該重試
        """
        return category in {
            ErrorCategory.NETWORK,
            ErrorCategory.RATE_LIMIT,
            ErrorCategory.RESOURCE,
        }
    
    @classmethod
    def should_skip(cls, category: ErrorCategory) -> bool:
        """判斷該錯誤是否應該跳過該影片.
        
        Args:
            category: 錯誤分類
            
        Returns:
            是否應該跳過
        """
        return category == ErrorCategory.VIDEO
    
    @classmethod
    def should_abort(cls, category: ErrorCategory) -> bool:
        """判斷該錯誤是否應該終止程式.
        
        Args:
            category: 錯誤分類
            
        Returns:
            是否應該終止
        """
        return category == ErrorCategory.SYSTEM
