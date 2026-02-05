# 錯誤處理與重試策略

> **版本**: 2.0  
> **狀態**: 📝 設計階段  
> **最後更新**: 2026-02-05

---

## 1. 設計目標

### 核心問題
V1 的錯誤處理過於簡單（只有 RETRYABLE/PERMANENT），無法應對複雜場景：
- 網路超時 → 應該立即重試
- Rate limit (429) → 應該等待 5 分鐘再重試
- 記憶體不足 → 應該換小模型重試
- 影片刪除 → 應該永久跳過
- 磁碟滿了 → 應該終止程式

### 設計原則
1. **細緻分類**：5 級錯誤分類，對應不同處理策略
2. **自動恢復**：無需人工介入，智能決定重試或放棄
3. **清晰可見**：用戶知道發生什麼、為什麼、怎麼辦
4. **錯誤隔離**：單點失敗不影響整體流程

---

## 2. 錯誤分類體系

### 2.1 ErrorCategory 定義

```python
from enum import Enum, auto

class ErrorCategory(Enum):
    """
    錯誤類別，決定處理策略。
    """
    
    # 立即重試（網路抖動等）
    RETRYABLE_IMMEDIATE = "retry_immediate"
    
    # 延遲重試（Rate limit, 429）
    RETRYABLE_DELAYED = "retry_delayed"
    
    # 替代方案重試（換策略）
    RETRYABLE_FALLBACK = "retry_fallback"
    
    # 永久跳過（影片問題）
    PERMANENT_SKIP = "permanent_skip"
    
    # 致命錯誤（系統問題）
    PERMANENT_FATAL = "permanent_fatal"
```

### 2.2 錯誤分類對照表

| 錯誤類型 | Category | 重試次數 | 退避策略 | 具體範例 |
|---------|----------|---------|----------|----------|
| 網路斷線 | RETRYABLE_IMMEDIATE | 3 | fixed 5s | `ConnectionError`, `TimeoutError` |
| DNS 解析失敗 | RETRYABLE_IMMEDIATE | 3 | fixed 5s | 暫時性 DNS 問題 |
| Rate limit 429 | RETRYABLE_DELAYED | 5 | exponential 5min | YouTube 限制請求 |
| 服務不可用 503 | RETRYABLE_DELAYED | 3 | exponential 1min | YouTube 維護 |
| Whisper OOM | RETRYABLE_FALLBACK | 2 | fixed 0s | 記憶體不足，換小模型 |
| 模型載入失敗 | RETRYABLE_FALLBACK | 1 | fixed 0s | 換其他 backend |
| 影片不存在 404 | PERMANENT_SKIP | 0 | - | 影片已刪除 |
| 版權限制 403 | PERMANENT_SKIP | 0 | - | 地區限制、會員專屬 |
| 私人影片 | PERMANENT_SKIP | 0 | - | `Video unavailable` |
| 磁碟空間不足 | PERMANENT_FATAL | 0 | - | `OSError: No space left` |
| 權限拒絕 | PERMANENT_FATAL | 0 | - | 無法寫入輸出目錄 |
| Whisper 模型損壞 | PERMANENT_FATAL | 0 | - | 模型檔案缺失 |

---

## 3. ErrorInfo 資料結構

```python
from dataclasses import dataclass
from typing import Optional, Dict, Any
from datetime import datetime

@dataclass
class ErrorInfo:
    """
    標準化的錯誤資訊。
    
    用於：
    - Stage 間傳遞錯誤
    - 寫入 SQLite 錯誤記錄
    - 顯示給用戶
    - 日誌記錄
    """
    # 分類（決定處理策略）
    category: ErrorCategory
    
    # 基本資訊
    message: str
    video_id: Optional[str] = None
    channel: Optional[str] = None
    stage: Optional[str] = None
    
    # 原始錯誤資訊
    exception_type: Optional[str] = None
    exception_message: Optional[str] = None
    
    # 額外上下文
    details: Optional[Dict[str, Any]] = None
    
    # 時間戳
    timestamp: datetime = field(default_factory=datetime.now)
    
    # 用戶提示（可選）
    user_hint: Optional[str] = None
    
    @property
    def is_retryable(self) -> bool:
        """是否可重試"""
        return self.category in (
            ErrorCategory.RETRYABLE_IMMEDIATE,
            ErrorCategory.RETRYABLE_DELAYED,
            ErrorCategory.RETRYABLE_FALLBACK
        )
    
    @property
    def is_fatal(self) -> bool:
        """是否致命（需要終止程式）"""
        return self.category == ErrorCategory.PERMANENT_FATAL
```

---

## 4. ErrorClassifier 錯誤分類器

### 4.1 核心類別

```python
import re
from typing import Optional

class ErrorClassifier:
    """
    錯誤分類器。
    
    使用多層級規則：
    1. 例外類型匹配
    2. 錯誤訊息模式匹配
    3. HTTP 狀態碼匹配
    4. 預設分類
    """
    
    # 例外類型 → Category 映射
    TYPE_MAP = {
        ConnectionError: ErrorCategory.RETRYABLE_IMMEDIATE,
        TimeoutError: ErrorCategory.RETRYABLE_IMMEDIATE,
        
        PermissionError: ErrorCategory.PERMANENT_FATAL,
        FileNotFoundError: ErrorCategory.PERMANENT_FATAL,
    }
    
    # 錯誤訊息模式 → Category 映射
    MESSAGE_PATTERNS = [
        # Rate limit
        (r'HTTP.*429', ErrorCategory.RETRYABLE_DELAYED),
        (r'rate.?limit', ErrorCategory.RETRYABLE_DELAYED, re.IGNORECASE),
        (r'too many requests', ErrorCategory.RETRYABLE_DELAYED, re.IGNORECASE),
        
        # 服務不可用
        (r'HTTP.*503', ErrorCategory.RETRYABLE_DELAYED),
        (r'HTTP.*502', ErrorCategory.RETRYABLE_DELAYED),
        (r'HTTP.*504', ErrorCategory.RETRYABLE_DELAYED),
        (r'service unavailable', ErrorCategory.RETRYABLE_DELAYED, re.IGNORECASE),
        
        # 影片不存在
        (r'HTTP.*404', ErrorCategory.PERMANENT_SKIP),
        (r'video.*not found', ErrorCategory.PERMANENT_SKIP, re.IGNORECASE),
        (r'video.*unavailable', ErrorCategory.PERMANENT_SKIP, re.IGNORECASE),
        (r'video.*removed', ErrorCategory.PERMANENT_SKIP, re.IGNORECASE),
        
        # 版權/權限
        (r'HTTP.*403', ErrorCategory.PERMANENT_SKIP),
        (r'copyright', ErrorCategory.PERMANENT_SKIP, re.IGNORECASE),
        (r'blocked', ErrorCategory.PERMANENT_SKIP, re.IGNORECASE),
        (r'private video', ErrorCategory.PERMANENT_SKIP, re.IGNORECASE),
        (r'members only', ErrorCategory.PERMANENT_SKIP, re.IGNORECASE),
        
        # 記憶體問題
        (r'out of memory|oom', ErrorCategory.RETRYABLE_FALLBACK, re.IGNORECASE),
        (r'cannot allocate memory', ErrorCategory.RETRYABLE_FALLBACK, re.IGNORECASE),
        (r'cuda out of memory', ErrorCategory.RETRYABLE_FALLBACK, re.IGNORECASE),
        
        # 磁碟問題
        (r'no space left', ErrorCategory.PERMANENT_FATAL, re.IGNORECASE),
        (r'disk full', ErrorCategory.PERMANENT_FATAL, re.IGNORECASE),
        (r'ENOSPC', ErrorCategory.PERMANENT_FATAL),
        
        # 模型問題
        (r'model.*not found', ErrorCategory.PERMANENT_FATAL, re.IGNORECASE),
        (r'invalid model', ErrorCategory.PERMANENT_FATAL, re.IGNORECASE),
    ]
    
    @classmethod
    def classify(
        cls,
        exception: Exception,
        video_id: Optional[str] = None,
        channel: Optional[str] = None,
        stage: Optional[str] = None
    ) -> ErrorInfo:
        """
        分類錯誤。
        
        返回 ErrorInfo，包含分類結果和處理建議。
        """
        exc_type = type(exception).__name__
        exc_message = str(exception)
        
        # 1. 檢查例外類型
        category = cls._classify_by_type(exception)
        
        # 2. 檢查錯誤訊息
        if category is None:
            category = cls._classify_by_message(exc_message)
        
        # 3. 檢查 HTTP 狀態碼（如果是 HTTPError）
        if category is None:
            category = cls._classify_by_http_status(exception)
        
        # 4. 預設分類
        if category is None:
            category = ErrorCategory.PERMANENT_FATAL
        
        # 生成用戶提示
        user_hint = cls._generate_user_hint(category, exc_message)
        
        return ErrorInfo(
            category=category,
            message=cls._extract_clean_message(exception),
            video_id=video_id,
            channel=channel,
            stage=stage,
            exception_type=exc_type,
            exception_message=exc_message,
            details=cls._extract_details(exception),
            user_hint=user_hint
        )
    
    @classmethod
    def _classify_by_type(cls, exc: Exception) -> Optional[ErrorCategory]:
        """基於例外類型分類"""
        for exc_type, category in cls.TYPE_MAP.items():
            if isinstance(exc, exc_type):
                return category
        return None
    
    @classmethod
    def _classify_by_message(cls, message: str) -> Optional[ErrorCategory]:
        """基於錯誤訊息分類"""
        message_lower = message.lower()
        
        for pattern_info in cls.MESSAGE_PATTERNS:
            pattern = pattern_info[0]
            category = pattern_info[1]
            flags = pattern_info[2] if len(pattern_info) > 2 else 0
            
            if re.search(pattern, message, flags):
                return category
        
        return None
    
    @classmethod
    def _classify_by_http_status(cls, exc: Exception) -> Optional[ErrorCategory]:
        """基於 HTTP 狀態碼分類"""
        # 檢查是否有 status_code 屬性
        status_code = getattr(exc, 'status_code', None) or getattr(exc, 'code', None)
        
        if status_code == 429:
            return ErrorCategory.RETRYABLE_DELAYED
        elif status_code in (502, 503, 504):
            return ErrorCategory.RETRYABLE_DELAYED
        elif status_code == 404:
            return ErrorCategory.PERMANENT_SKIP
        elif status_code == 403:
            return ErrorCategory.PERMANENT_SKIP
        
        return None
    
    @classmethod
    def _generate_user_hint(cls, category: ErrorCategory, message: str) -> str:
        """生成用戶提示"""
        hints = {
            ErrorCategory.RETRYABLE_IMMEDIATE: 
                "網路問題，將自動重試",
            ErrorCategory.RETRYABLE_DELAYED: 
                "服務暫時不可用，將在幾分鐘後自動重試",
            ErrorCategory.RETRYABLE_FALLBACK: 
                "資源不足，將嘗試替代方案",
            ErrorCategory.PERMANENT_SKIP: 
                "此影片無法處理（可能已刪除或有限制），將自動跳過",
            ErrorCategory.PERMANENT_FATAL: 
                "系統錯誤，請檢查磁碟空間和權限後重試",
        }
        return hints.get(category, "未知錯誤")
    
    @classmethod
    def _extract_clean_message(cls, exc: Exception) -> str:
        """提取乾淨的錯誤訊息（移除堆疊追蹤等）"""
        message = str(exc)
        # 移除常見的冗餘前綴
        prefixes = [
            "ERROR:",
            "Error:",
            "Failed to",
        ]
        for prefix in prefixes:
            if message.startswith(prefix):
                message = message[len(prefix):].strip()
        return message
    
    @classmethod
    def _extract_details(cls, exc: Exception) -> Dict[str, Any]:
        """提取詳細資訊"""
        import traceback
        
        details = {
            "exception_module": type(exc).__module__,
        }
        
        # 提取 HTTP 相關資訊
        if hasattr(exc, 'status_code'):
            details['http_status'] = exc.status_code
        if hasattr(exc, 'url'):
            details['url'] = exc.url
        
        # 提取 OSError 錯誤碼
        if isinstance(exc, OSError) and exc.errno:
            details['os_errno'] = exc.errno
        
        return details
```

---

## 5. RetryEngine 重試引擎

### 5.1 RetryPolicy 配置

```python
from dataclasses import dataclass
from typing import Optional, Callable

@dataclass
class RetryPolicy:
    """
    重試策略配置。
    """
    category: ErrorCategory
    max_attempts: int
    backoff_strategy: str  # fixed, linear, exponential
    backoff_base_seconds: int
    backoff_max_seconds: int = 3600  # 最大延遲 1 小時
    
    # 可選的 fallback 動作
    fallback_action: Optional[Callable] = None
    
    def calculate_delay(self, attempt: int) -> int:
        """
        計算重試延遲（秒）。
        
        Args:
            attempt: 當前重試次數（0-indexed）
        
        Returns:
            延遲秒數
        """
        if self.backoff_strategy == "fixed":
            delay = self.backoff_base_seconds
        elif self.backoff_strategy == "linear":
            delay = self.backoff_base_seconds * (attempt + 1)
        else:  # exponential
            delay = self.backoff_base_seconds * (2 ** attempt)
        
        return min(delay, self.backoff_max_seconds)
    
    def should_retry(self, attempt: int, error: ErrorInfo) -> bool:
        """是否應該繼續重試"""
        if error.category in (ErrorCategory.PERMANENT_SKIP, ErrorCategory.PERMANENT_FATAL):
            return False
        return attempt < self.max_attempts


# 預設策略
DEFAULT_RETRY_POLICIES = {
    ErrorCategory.RETRYABLE_IMMEDIATE: RetryPolicy(
        category=ErrorCategory.RETRYABLE_IMMEDIATE,
        max_attempts=3,
        backoff_strategy="fixed",
        backoff_base_seconds=5
    ),
    
    ErrorCategory.RETRYABLE_DELAYED: RetryPolicy(
        category=ErrorCategory.RETRYABLE_DELAYED,
        max_attempts=5,
        backoff_strategy="exponential",
        backoff_base_seconds=300,  # 5 分鐘
        backoff_max_seconds=3600   # 最大 1 小時
    ),
    
    ErrorCategory.RETRYABLE_FALLBACK: RetryPolicy(
        category=ErrorCategory.RETRYABLE_FALLBACK,
        max_attempts=2,
        backoff_strategy="fixed",
        backoff_base_seconds=0  # 立即執行 fallback
    ),
    
    ErrorCategory.PERMANENT_SKIP: RetryPolicy(
        category=ErrorCategory.PERMANENT_SKIP,
        max_attempts=0
    ),
    
    ErrorCategory.PERMANENT_FATAL: RetryPolicy(
        category=ErrorCategory.PERMANENT_FATAL,
        max_attempts=0
    ),
}
```

### 5.2 RetryEngine 實作

```python
import time
import logging
from typing import Callable, TypeVar, Generic

logger = logging.getLogger(__name__)
T = TypeVar('T')

class RetryResult(Generic[T]):
    """重試執行結果"""
    def __init__(
        self,
        success: bool,
        value: Optional[T] = None,
        error: Optional[ErrorInfo] = None,
        attempts: int = 0
    ):
        self.success = success
        self.value = value
        self.error = error
        self.attempts = attempts

class RetryEngine:
    """
    智能重試引擎。
    
    特性：
    - 根據錯誤類型自動選擇重試策略
    - 支援 fallback 動作
    - 詳細的日誌記錄
    - 全局最大重試次數保護（防止無限循環）
    """
    
    # 全局最大重試次數（安全上限）
    MAX_TOTAL_ATTEMPTS = 10
    
    def __init__(
        self,
        state_manager: "StateManager",
        policies: Optional[Dict[ErrorCategory, RetryPolicy]] = None
    ):
        self.state_manager = state_manager
        self.policies = policies or DEFAULT_RETRY_POLICIES
    
    def execute(
        self,
        operation: Callable[[], T],
        video_id: str,
        channel: str,
        stage: str
    ) -> RetryResult[T]:
        """
        執行操作並自動重試。
        
        Args:
            operation: 要執行的操作
            video_id: 影片 ID（用於日誌和狀態更新）
            channel: 頻道名稱
            stage: Stage 名稱
        
        Returns:
            RetryResult，包含執行結果或錯誤
        
        Raises:
            RetryExhaustedError: 超過最大重試次數
        """
        attempt = 0
        last_error = None
        
        while True:
            # 安全檢查：全局最大重試次數
            if attempt >= self.MAX_TOTAL_ATTEMPTS:
                logger.error(
                    "Max total attempts exceeded",
                    video_id=video_id,
                    stage=stage,
                    max_attempts=self.MAX_TOTAL_ATTEMPTS
                )
                return RetryResult(
                    success=False,
                    error=ErrorInfo(
                        category=ErrorCategory.PERMANENT_FATAL,
                        message=f"Exceeded max total attempts ({self.MAX_TOTAL_ATTEMPTS})"
                    ),
                    attempts=attempt
                )
            try:
                # 執行操作
                value = operation()
                
                logger.info(
                    "Operation succeeded",
                    video_id=video_id,
                    stage=stage,
                    attempts=attempt + 1
                )
                
                return RetryResult(
                    success=True,
                    value=value,
                    attempts=attempt + 1
                )
            
            except Exception as e:
                # 分類錯誤
                error = ErrorClassifier.classify(
                    e,
                    video_id=video_id,
                    channel=channel,
                    stage=stage
                )
                last_error = error
                
                # 獲取重試策略
                policy = self.policies.get(error.category)
                
                if not policy or not policy.should_retry(attempt, error):
                    # 不再重試
                    logger.error(
                        "Giving up after retries",
                        video_id=video_id,
                        stage=stage,
                        attempts=attempt + 1,
                        error_category=error.category.value,
                        error_message=error.message
                    )
                    
                    return RetryResult(
                        success=False,
                        error=error,
                        attempts=attempt + 1
                    )
                
                # 執行 fallback（第一次失敗時）
                if policy.fallback_action and attempt == 0:
                    try:
                        logger.info(
                            "Executing fallback action",
                            video_id=video_id,
                            stage=stage
                        )
                        policy.fallback_action()
                    except Exception as fallback_error:
                        logger.warning(
                            "Fallback failed",
                            video_id=video_id,
                            error=str(fallback_error)
                        )
                
                # 計算延遲
                delay = policy.calculate_delay(attempt)
                
                logger.info(
                    "Retry scheduled",
                    video_id=video_id,
                    stage=stage,
                    attempt=attempt + 1,
                    max_attempts=policy.max_attempts,
                    delay_seconds=delay,
                    error_category=error.category.value
                )
                
                # 等待（如果延遲 > 0）
                if delay > 0:
                    time.sleep(delay)
                
                attempt += 1
                last_error = error
```

---

## 6. 錯誤處理流程圖

```
┌─────────────────────────────────────────────────────────────────────┐
│                        執行 Stage                                    │
└───────────────────────────┬─────────────────────────────────────────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
    ┌─────────────────┐         ┌─────────────────┐
    │     成功        │         │      失敗       │
    └────────┬────────┘         └────────┬────────┘
             │                           │
             │                           ▼
             │                  ┌─────────────────┐
             │                  │ ErrorClassifier │
             │                  └────────┬────────┘
             │                           │
             │              ┌────────────┼────────────┐
             │              │            │            │
             │              ▼            ▼            ▼
             │    ┌───────────┐  ┌───────────┐  ┌───────────┐
             │    │ RETRYABLE │  │   SKIP    │  │   FATAL   │
             │    │           │  │           │  │           │
             │    │ Immediate │  │           │  │           │
             │    │ Delayed   │  │           │  │           │
             │    │ Fallback  │  │           │  │           │
             │    └─────┬─────┘  └─────┬─────┘  └─────┬─────┘
             │          │              │              │
             │          ▼              │              │
             │    ┌──────────┐         │              │
             │    │ 重試？   │         │              │
             │    │ (< max)  │         │              │
             │    └────┬─────┘         │              │
             │         │               │              │
             │    是 /   \ 否          │              │
             │        /     \          │              │
             │       ▼       ▼         ▼              ▼
             │   ┌──────┐  ┌────────┐ ┌────────┐  ┌────────┐
             │   │等待  │  │標記    │ │標記    │  │終止    │
             │   │延遲  │  │Failed  │ │Skipped │  │程式    │
             │   └──┬───┘  └────┬───┘ └───┬────┘  └────┬───┘
             │      │           │         │            │
             └──────┼───────────┴─────────┴────────────┘
                    │
                    ▼
         ┌────────────────────┐
         │  從失敗處繼續執行  │
         │  (檢查點恢復)      │
         └────────────────────┘
```

---

## 7. 用戶顯示格式

### 7.1 CLI 錯誤顯示

```python
class ErrorDisplay:
    """格式化錯誤資訊供 CLI 顯示"""
    
    EMOJI = {
        ErrorCategory.RETRYABLE_IMMEDIATE: "🔄",
        ErrorCategory.RETRYABLE_DELAYED: "⏳",
        ErrorCategory.RETRYABLE_FALLBACK: "🔀",
        ErrorCategory.PERMANENT_SKIP: "⊘",
        ErrorCategory.PERMANENT_FATAL: "❌",
    }
    
    @classmethod
    def format(cls, error: ErrorInfo, attempt: int = 0, max_attempts: int = 0) -> str:
        """格式化錯誤訊息"""
        emoji = cls.EMOJI.get(error.category, "⚠️")
        
        lines = [
            f"{emoji} [{error.stage}] {error.message}",
        ]
        
        # 重試資訊
        if error.category in (
            ErrorCategory.RETRYABLE_IMMEDIATE,
            ErrorCategory.RETRYABLE_DELAYED
        ):
            if attempt < max_attempts:
                lines.append(f"   將自動重試 ({attempt + 1}/{max_attempts})")
            else:
                lines.append(f"   重試次數已達上限，標記為失敗")
        
        # 用戶提示
        if error.user_hint:
            lines.append(f"   💡 {error.user_hint}")
        
        return "\n".join(lines)
```

### 7.2 顯示範例

```
# 網路問題（自動重試）
🔄 [download] Connection timeout
   將自動重試 (1/3)
   💡 網路問題，將自動重試

# Rate limit（延遲重試）
⏳ [download] HTTP 429: Too Many Requests
   將在 5 分鐘後自動重試 (2/5)
   💡 服務暫時不可用，將在幾分鐘後自動重試

# 影片刪除（跳過）
⊘ [download] Video unavailable (404)
   標記為跳過
   💡 此影片無法處理（可能已刪除或有限制），將自動跳過

# 磁碟滿了（致命錯誤）
❌ [save] No space left on device
   終止程式
   💡 系統錯誤，請檢查磁碟空間和權限後重試
```

---

## 8. 測試策略

### 8.1 錯誤分類測試

```python
def test_classify_network_error():
    exc = ConnectionError("Network unreachable")
    error = ErrorClassifier.classify(exc, video_id="test")
    
    assert error.category == ErrorCategory.RETRYABLE_IMMEDIATE
    assert error.is_retryable

def test_classify_rate_limit():
    exc = HTTPError("HTTP 429: Too Many Requests")
    error = ErrorClassifier.classify(exc, video_id="test")
    
    assert error.category == ErrorCategory.RETRYABLE_DELAYED

def test_classify_video_not_found():
    exc = Exception("Video unavailable (404)")
    error = ErrorClassifier.classify(exc, video_id="test")
    
    assert error.category == ErrorCategory.PERMANENT_SKIP
    assert not error.is_retryable

def test_classify_disk_full():
    exc = OSError(28, "No space left on device")
    error = ErrorClassifier.classify(exc, video_id="test")
    
    assert error.category == ErrorCategory.PERMANENT_FATAL
    assert error.is_fatal
```

### 8.2 重試引擎測試

```python
def test_retry_success_on_second_attempt():
    call_count = 0
    
    def flaky_operation():
        nonlocal call_count
        call_count += 1
        if call_count < 2:
            raise ConnectionError("First attempt fails")
        return "success"
    
    engine = RetryEngine(MockStateManager())
    result = engine.execute(
        flaky_operation,
        video_id="test",
        channel="test",
        stage="test"
    )
    
    assert result.success
    assert result.attempts == 2

def test_retry_gives_up_after_max_attempts():
    def always_fails():
        raise ConnectionError("Always fails")
    
    engine = RetryEngine(MockStateManager())
    result = engine.execute(
        always_fails,
        video_id="test",
        channel="test",
        stage="test"
    )
    
    assert not result.success
    assert result.attempts == 3  # DEFAULT_RETRY_POLICIES 設定
```

---

**最後更新**: 2026-02-05  
**文件狀態**: 📝 設計階段
