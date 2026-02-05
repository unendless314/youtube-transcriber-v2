# 資料庫 Schema 設計

> **版本**: 2.0  
> **狀態**: 📝 設計階段  
> **最後更新**: 2026-02-05

---

## 1. 設計原則

### 核心考量
1. **斷電安全**：SQLite 原子寫入，不會產生損壞檔案
2. **自動清理**：只保留最近資料，控制檔案大小
3. **簡單查詢**：核心操作只需 O(log n) 索引查詢
4. **單線程**：不需要並發控制，簡化設計

### 資料保留策略
| 狀態 | 保留時間 | 說明 |
|------|----------|------|
| `success` | 30 天 | 成功的影片記錄，避免短期內重複處理 |
| `failed` | 7 天 | 失敗記錄，7 天後可重試 |
| `skipped` | 7 天 | 跳過記錄，通常不會再變化 |
| `pending`/`processing` | 不清除 | 未完成的不應被清除 |

- **清理時機**：每次插入新記錄後自動觸發
- **總數限制**：只清理 `failed` 和 `skipped`，保留最近 100 筆

---

## 2. Schema 定義

### 2.1 核心表結構

```sql
-- ============================================================================
-- 影片處理記錄表
-- ============================================================================
-- 這是唯一的核心表，記錄所有處理過的影片
-- 設計目標：簡單、快速查詢、自動清理

CREATE TABLE processed_videos (
    -- 主鍵
    video_id TEXT PRIMARY KEY,
    
    -- 影片資訊（去正規化，減少查詢）
    channel_name TEXT NOT NULL,
    title TEXT,
    published_at DATE,
    duration_seconds INTEGER,
    
    -- 處理狀態
    status TEXT NOT NULL DEFAULT 'pending',
    -- 狀態值: pending, processing, success, failed, skipped
    
    -- 錯誤資訊（僅 failed 時使用）
    error_type TEXT,  -- network, transcription, disk, permanent_skip, ...
    error_message TEXT,
    
    -- 重試追蹤
    attempts INTEGER DEFAULT 0,
    max_attempts INTEGER DEFAULT 3,
    
    -- 輸出資訊（僅 success 時使用）
    output_path TEXT,
    word_count INTEGER,
    
    -- 處理時間統計
    processing_started_at TIMESTAMP,
    processing_completed_at TIMESTAMP,
    processing_time_seconds REAL,
    
    -- 審計欄位
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- 索引
-- ============================================================================
-- 核心查詢：檢查影片是否已處理
CREATE INDEX idx_video_id 
    ON processed_videos(video_id);

-- 核心查詢：獲取某頻道的待處理影片
CREATE INDEX idx_channel_status 
    ON processed_videos(channel_name, status);

-- 清理舊資料：按時間排序
CREATE INDEX idx_created_at 
    ON processed_videos(created_at DESC);

-- 統計查詢：按狀態分組
CREATE INDEX idx_status 
    ON processed_videos(status);

-- ============================================================================
-- 觸發器：自動更新時間戳
-- ============================================================================
CREATE TRIGGER update_video_timestamp 
AFTER UPDATE ON processed_videos
FOR EACH ROW
BEGIN
    UPDATE processed_videos 
    SET updated_at = CURRENT_TIMESTAMP 
    WHERE video_id = NEW.video_id;
END;

-- ============================================================================
-- 觸發器：自動清理舊資料
-- ============================================================================
-- 每次插入新記錄後，根據狀態和時間清理
CREATE TRIGGER cleanup_old_videos
AFTER INSERT ON processed_videos
FOR EACH ROW
BEGIN
    -- 清理失敗記錄（7天）
    DELETE FROM processed_videos 
    WHERE status = 'failed' 
    AND created_at < datetime('now', '-7 days');
    
    -- 清理跳過記錄（7天）
    DELETE FROM processed_videos 
    WHERE status = 'skipped' 
    AND created_at < datetime('now', '-7 days');
    
    -- 清理成功記錄（30天）
    DELETE FROM processed_videos 
    WHERE status = 'success' 
    AND created_at < datetime('now', '-30 days');
    
    -- 總數限制（只清理 failed 和 skipped）
    DELETE FROM processed_videos 
    WHERE status IN ('failed', 'skipped')
    AND video_id IN (
        SELECT video_id 
        FROM processed_videos 
        WHERE status IN ('failed', 'skipped')
        ORDER BY created_at DESC 
        LIMIT -1 OFFSET 100
    );
END;
```

### 2.2 可選：頻道統計表

```sql
-- ============================================================================
-- 頻道統計表（可選，加速統計查詢）
-- ============================================================================
-- 這個表是反正規化的快取，用於快速獲取頻道統計
-- 可由 processed_videos 表的資料計算得出

CREATE TABLE channel_stats (
    channel_name TEXT PRIMARY KEY,
    
    -- 計數
    total_videos INTEGER DEFAULT 0,
    success_count INTEGER DEFAULT 0,
    failed_count INTEGER DEFAULT 0,
    skipped_count INTEGER DEFAULT 0,
    pending_count INTEGER DEFAULT 0,
    
    -- 時間追蹤
    last_processed_at TIMESTAMP,
    last_success_at TIMESTAMP,
    
    -- 更新時間
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 觸發器：當影片狀態改變時更新統計
CREATE TRIGGER update_stats_on_video_change
AFTER UPDATE OF status ON processed_videos
FOR EACH ROW
BEGIN
    INSERT OR REPLACE INTO channel_stats (
        channel_name,
        total_videos,
        success_count,
        failed_count,
        skipped_count,
        pending_count,
        last_processed_at,
        last_success_at
    )
    SELECT 
        channel_name,
        COUNT(*),
        SUM(CASE WHEN status = 'success' THEN 1 ELSE 0 END),
        SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END),
        SUM(CASE WHEN status = 'skipped' THEN 1 ELSE 0 END),
        SUM(CASE WHEN status = 'pending' THEN 1 ELSE 0 END),
        MAX(processing_completed_at),
        MAX(CASE WHEN status = 'success' THEN processing_completed_at END)
    FROM processed_videos
    WHERE channel_name = NEW.channel_name;
END;
```

---

## 3. Python 實作

### 3.1 StateManager 類別

```python
import sqlite3
from pathlib import Path
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import Optional, List
from enum import Enum
import logging

logger = logging.getLogger(__name__)


class VideoStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SUCCESS = "success"
    FAILED = "failed"
    SKIPPED = "skipped"


@dataclass
class VideoRecord:
    """影片記錄資料類別"""
    video_id: str
    channel_name: str
    title: Optional[str]
    status: VideoStatus
    error_type: Optional[str] = None
    error_message: Optional[str] = None
    attempts: int = 0
    output_path: Optional[Path] = None
    word_count: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class ProcessingResult:
    """
    影片處理結果。
    
    由 Pipeline 產出，傳遞給 StateManager 記錄狀態。
    """
    success: bool
    video_id: str
    output_path: Optional[Path] = None
    word_count: Optional[int] = None
    processing_time_seconds: Optional[float] = None
    error: Optional["ErrorInfo"] = None


class StateManager:
    """
    基於 SQLite 的狀態管理器。
    
    特性：
    - 斷電安全（SQLite 原子提交）
    - 自動清理舊資料（7天或100筆）
    - 單線程設計（無需鎖）
    """
    
    # SQL Schema
    SCHEMA = """
    CREATE TABLE IF NOT EXISTS processed_videos (
        video_id TEXT PRIMARY KEY,
        channel_name TEXT NOT NULL,
        title TEXT,
        published_at DATE,
        duration_seconds INTEGER,
        status TEXT NOT NULL DEFAULT 'pending',
        error_type TEXT,
        error_message TEXT,
        attempts INTEGER DEFAULT 0,
        max_attempts INTEGER DEFAULT 3,
        output_path TEXT,
        word_count INTEGER,
        processing_started_at TIMESTAMP,
        processing_completed_at TIMESTAMP,
        processing_time_seconds REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
    CREATE INDEX IF NOT EXISTS idx_video_id 
        ON processed_videos(video_id);
    CREATE INDEX IF NOT EXISTS idx_channel_status 
        ON processed_videos(channel_name, status);
    CREATE INDEX IF NOT EXISTS idx_created_at 
        ON processed_videos(created_at DESC);
    CREATE INDEX IF NOT EXISTS idx_status 
        ON processed_videos(status);
    
    CREATE TRIGGER IF NOT EXISTS update_video_timestamp 
    AFTER UPDATE ON processed_videos
    FOR EACH ROW
    BEGIN
        UPDATE processed_videos 
        SET updated_at = CURRENT_TIMESTAMP 
        WHERE video_id = NEW.video_id;
    END;
    
    CREATE TRIGGER IF NOT EXISTS cleanup_old_videos
    AFTER INSERT ON processed_videos
    FOR EACH ROW
    BEGIN
        -- 清理失敗記錄（7天）
        DELETE FROM processed_videos 
        WHERE status = 'failed' 
        AND created_at < datetime('now', '-7 days');
        
        -- 清理跳過記錄（7天）
        DELETE FROM processed_videos 
        WHERE status = 'skipped' 
        AND created_at < datetime('now', '-7 days');
        
        -- 清理成功記錄（30天）
        DELETE FROM processed_videos 
        WHERE status = 'success' 
        AND created_at < datetime('now', '-30 days');
        
        -- 總數限制（只清理 failed 和 skipped）
        DELETE FROM processed_videos 
        WHERE status IN ('failed', 'skipped')
        AND video_id IN (
            SELECT video_id 
            FROM processed_videos 
            WHERE status IN ('failed', 'skipped')
            ORDER BY created_at DESC 
            LIMIT -1 OFFSET 100
        );
    END;
    """
    
    def __init__(self, db_path: Path):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_database()
    
    def _init_database(self) -> None:
        """初始化資料庫"""
        with sqlite3.connect(self.db_path) as conn:
            conn.executescript(self.SCHEMA)
            logger.debug("Database initialized", db_path=str(self.db_path))
    
    def _get_connection(self) -> sqlite3.Connection:
        """獲取資料庫連接"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    # ========================================================================
    # 核心查詢操作
    # ========================================================================
    
    def is_processed(self, video_id: str) -> bool:
        """檢查影片是否已處理（成功或跳過）"""
        with self._get_connection() as conn:
            row = conn.execute(
                """
                SELECT status FROM processed_videos 
                WHERE video_id = ?
                """,
                (video_id,)
            ).fetchone()
            
            if not row:
                return False
            
            return row["status"] in (VideoStatus.SUCCESS.value, VideoStatus.SKIPPED.value)
    
    def get_video_status(self, video_id: str) -> Optional[VideoStatus]:
        """獲取影片狀態"""
        with self._get_connection() as conn:
            row = conn.execute(
                "SELECT status FROM processed_videos WHERE video_id = ?",
                (video_id,)
            ).fetchone()
            
            return VideoStatus(row["status"]) if row else None
    
    def get_pending_videos(self, channel: Optional[str] = None) -> List[VideoRecord]:
        """
        獲取待處理影片列表。
        
        包含：
        - status = 'pending'
        - status = 'failed' 且 attempts < max_attempts
        """
        with self._get_connection() as conn:
            query = """
                SELECT * FROM processed_videos
                WHERE (
                    status = 'pending'
                    OR (
                        status = 'failed'
                        AND attempts < max_attempts
                    )
                )
            """
            params = []
            
            if channel:
                query += " AND channel_name = ?"
                params.append(channel)
            
            query += " ORDER BY created_at ASC"
            
            rows = conn.execute(query, params).fetchall()
            return [self._row_to_record(row) for row in rows]
    
    # ========================================================================
    # 狀態更新操作
    # ========================================================================
    
    def mark_pending(self, video: "VideoInfo") -> None:
        """標記影片為待處理（插入新記錄）"""
        with self._get_connection() as conn:
            conn.execute(
                """
                INSERT OR IGNORE INTO processed_videos (
                    video_id, channel_name, title, published_at, 
                    duration_seconds, status
                ) VALUES (?, ?, ?, ?, ?, 'pending')
                """,
                (
                    video.video_id,
                    video.channel,
                    video.title,
                    video.published_at.date().isoformat() if video.published_at else None,
                    video.duration_seconds
                )
            )
            logger.debug("Marked pending", video_id=video.video_id)
    
    def mark_processing(self, video_id: str) -> None:
        """標記影片為處理中"""
        with self._get_connection() as conn:
            conn.execute(
                """
                UPDATE processed_videos 
                SET status = 'processing',
                    processing_started_at = CURRENT_TIMESTAMP,
                    attempts = attempts + 1
                WHERE video_id = ?
                """,
                (video_id,)
            )
            logger.debug("Marked processing", video_id=video_id)
    
    def mark_completed(self, result: ProcessingResult) -> None:
        """
        標記影片為處理成功。
        
        Args:
            result: ProcessingResult 物件，包含處理結果資訊
        """
        with self._get_connection() as conn:
            conn.execute(
                """
                UPDATE processed_videos 
                SET status = 'success',
                    output_path = ?,
                    word_count = ?,
                    processing_completed_at = CURRENT_TIMESTAMP,
                    processing_time_seconds = ?
                WHERE video_id = ?
                """,
                (
                    str(result.output_path) if result.output_path else None,
                    result.word_count,
                    result.processing_time_seconds,
                    result.video_id
                )
            )
            logger.info(
                "Marked completed",
                video_id=result.video_id,
                word_count=result.word_count
            )
    
    def mark_failed(self, video_id: str, error: "ErrorInfo") -> None:
        """
        標記影片為處理失敗。
        
        Args:
            video_id: 影片 ID
            error: ErrorInfo 物件，包含錯誤資訊
        """
        # 根據錯誤類別決定狀態
        status = 'skipped' if error.category == ErrorCategory.PERMANENT_SKIP else 'failed'
        
        with self._get_connection() as conn:
            conn.execute(
                """
                UPDATE processed_videos 
                SET status = ?,
                    error_type = ?,
                    error_message = ?,
                    processing_completed_at = CURRENT_TIMESTAMP
                WHERE video_id = ?
                """,
                (status, error.category.value, error.message, video_id)
            )
            logger.warning(
                "Marked failed",
                video_id=video_id,
                error_type=error.category.value,
                status=status
            )
    
    def mark_skipped(self, video_id: str, reason: str) -> None:
        """標記影片為跳過"""
        with self._get_connection() as conn:
            conn.execute(
                """
                UPDATE processed_videos 
                SET status = 'skipped',
                    error_message = ?,
                    processing_completed_at = CURRENT_TIMESTAMP
                WHERE video_id = ?
                """,
                (reason, video_id)
            )
            logger.info("Marked skipped", video_id=video_id, reason=reason)
    
    # ========================================================================
    # 統計操作
    # ========================================================================
    
    def get_channel_stats(self, channel: str) -> dict:
        """獲取頻道統計"""
        with self._get_connection() as conn:
            row = conn.execute(
                """
                SELECT 
                    COUNT(*) as total,
                    SUM(CASE WHEN status = 'success' THEN 1 ELSE 0 END) as success,
                    SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END) as failed,
                    SUM(CASE WHEN status = 'skipped' THEN 1 ELSE 0 END) as skipped,
                    SUM(CASE WHEN status = 'pending' THEN 1 ELSE 0 END) as pending
                FROM processed_videos
                WHERE channel_name = ?
                """,
                (channel,)
            ).fetchone()
            
            return {
                "channel": channel,
                "total": row["total"] or 0,
                "success": row["success"] or 0,
                "failed": row["failed"] or 0,
                "skipped": row["skipped"] or 0,
                "pending": row["pending"] or 0
            }
    
    def get_overall_stats(self) -> dict:
        """獲取整體統計"""
        with self._get_connection() as conn:
            row = conn.execute(
                """
                SELECT 
                    COUNT(DISTINCT channel_name) as channels,
                    COUNT(*) as total,
                    SUM(CASE WHEN status = 'success' THEN 1 ELSE 0 END) as success,
                    SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END) as failed,
                    SUM(CASE WHEN status = 'skipped' THEN 1 ELSE 0 END) as skipped
                FROM processed_videos
                """
            ).fetchone()
            
            return dict(row)
    
    # ========================================================================
    # 維護操作
    # ========================================================================
    
    def cleanup(
        self,
        success_days: int = 30,
        failed_days: int = 7,
        max_failed_skipped: int = 100
    ) -> int:
        """
        手動清理舊資料（通常由觸發器自動處理）。
        
        Args:
            success_days: 成功記錄保留天數（預設 30 天）
            failed_days: 失敗/跳過記錄保留天數（預設 7 天）
            max_failed_skipped: 失敗/跳過記錄最大數量
        
        Returns:
            刪除的記錄數
        """
        with self._get_connection() as conn:
            total = 0
            
            # 清理成功記錄（超過 success_days）
            cursor = conn.execute(
                """
                DELETE FROM processed_videos 
                WHERE status = 'success'
                AND created_at < datetime('now', '-' || ? || ' days')
                """,
                (success_days,)
            )
            deleted_success = cursor.rowcount
            total += deleted_success
            
            # 清理失敗記錄（超過 failed_days）
            cursor = conn.execute(
                """
                DELETE FROM processed_videos 
                WHERE status = 'failed'
                AND created_at < datetime('now', '-' || ? || ' days')
                """,
                (failed_days,)
            )
            deleted_failed = cursor.rowcount
            total += deleted_failed
            
            # 清理跳過記錄（超過 failed_days）
            cursor = conn.execute(
                """
                DELETE FROM processed_videos 
                WHERE status = 'skipped'
                AND created_at < datetime('now', '-' || ? || ' days')
                """,
                (failed_days,)
            )
            deleted_skipped = cursor.rowcount
            total += deleted_skipped
            
            # 總數限制（只清理 failed 和 skipped）
            cursor = conn.execute(
                """
                DELETE FROM processed_videos 
                WHERE status IN ('failed', 'skipped')
                AND video_id IN (
                    SELECT video_id 
                    FROM processed_videos 
                    WHERE status IN ('failed', 'skipped')
                    ORDER BY created_at DESC 
                    LIMIT -1 OFFSET ?
                )
                """,
                (max_failed_skipped,)
            )
            deleted_by_count = cursor.rowcount
            total += deleted_by_count
            
            if total > 0:
                logger.info(
                    "Cleaned up old records",
                    total=total,
                    success=deleted_success,
                    failed=deleted_failed,
                    skipped=deleted_skipped,
                    by_count=deleted_by_count
                )
            return total
    
    def get_database_size(self) -> int:
        """獲取資料庫檔案大小（位元組）"""
        return self.db_path.stat().st_size if self.db_path.exists() else 0
    
    def reset(self) -> None:
        """重置資料庫（刪除所有資料）"""
        with self._get_connection() as conn:
            conn.execute("DELETE FROM processed_videos")
        logger.warning("Database reset", db_path=str(self.db_path))
    
    # ========================================================================
    # 輔助方法
    # ========================================================================
    
    def _row_to_record(self, row: sqlite3.Row) -> VideoRecord:
        """將資料庫 row 轉換為 VideoRecord"""
        return VideoRecord(
            video_id=row["video_id"],
            channel_name=row["channel_name"],
            title=row["title"],
            status=VideoStatus(row["status"]),
            error_type=row["error_type"],
            error_message=row["error_message"],
            attempts=row["attempts"],
            output_path=Path(row["output_path"]) if row["output_path"] else None,
            word_count=row["word_count"],
            created_at=datetime.fromisoformat(row["created_at"]) if row["created_at"] else None,
            updated_at=datetime.fromisoformat(row["updated_at"]) if row["updated_at"] else None
        )
```

---

## 4. 使用範例

### 4.1 基本使用

```python
from pathlib import Path

# 初始化
state = StateManager(Path("state.db"))

# 標記待處理
video = VideoInfo(video_id="abc123", channel="Test", title="Test Video", ...)
state.mark_pending(video)

# 標記處理中
state.mark_processing("abc123")

# 標記完成
from transcriber.core.state import ProcessingResult

result = ProcessingResult(
    success=True,
    video_id="abc123",
    output_path=Path("output/test/video.md"),
    word_count=1500,
    processing_time_seconds=120.5
)
state.mark_completed(result)

# 檢查是否已處理
if state.is_processed("abc123"):
    print("Already processed, skip")
```

### 4.2 查詢待處理

```python
# 獲取所有待處理
pending = state.get_pending_videos()
for video in pending:
    print(f"{video.video_id}: {video.title}")

# 獲取某頻道的待處理
pending_for_channel = state.get_pending_videos(channel="老高與小茉")
```

### 4.3 統計資訊

```python
# 頻道統計
stats = state.get_channel_stats("老高與小茉")
print(f"Total: {stats['total']}, Success: {stats['success']}")

# 整體統計
overall = state.get_overall_stats()
print(f"Total videos: {overall['total']}")

# 資料庫大小
size_mb = state.get_database_size() / 1024 / 1024
print(f"Database size: {size_mb:.2f} MB")
```

---

## 5. 性能考量

### 5.1 預期資料量

| 場景 | 記錄數 | 資料庫大小 |
|------|--------|-----------|
| 每日使用（5 部影片） | ~35 筆 | ~100 KB |
| 一週累積 | ~100 筆（上限） | ~300 KB |
| 極端情況（單日 50 部） | ~100 筆 | ~300 KB |

### 5.2 查詢性能

```sql
-- 檢查是否已處理（核心操作）
SELECT status FROM processed_videos WHERE video_id = ?;
-- 使用 idx_video_id，O(log n)

-- 獲取待處理影片
SELECT * FROM processed_videos WHERE channel_name = ? AND status = 'pending';
-- 使用 idx_channel_status，O(log n + m)，m 為結果數
```

預期性能：
- `is_processed()`: < 1ms
- `get_pending_videos()`: < 10ms
- `mark_*()`: < 5ms

### 5.3 清理策略

自動清理由觸發器處理，每次插入後：
1. 清理 `failed` 和 `skipped` 記錄（超過 7 天）
2. 清理 `success` 記錄（超過 30 天）
3. 如果 `failed`/`skipped` 超過 100 筆，刪除最舊的

**為什麼這樣設計？**
- `success` 保留 30 天：避免用戶短期內重複處理（如休假回來）
- `failed`/`skipped` 保留 7 天：足夠時間診斷問題
- 100 筆限制：控制資料庫大小，但保留足夠診斷資訊

---

**最後更新**: 2026-02-05  
**文件狀態**: 📝 設計階段
