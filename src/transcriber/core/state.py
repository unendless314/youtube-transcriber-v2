"""SQLite 狀態管理 - 實現斷點續傳核心功能."""

import json
import sqlite3
import time
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
from typing import Any

import structlog

logger = structlog.get_logger(__name__)


class VideoStatus(str, Enum):
    """影片處理狀態."""
    
    PENDING = "pending"           # 等待處理
    DOWNLOADING = "downloading"   # 下載中
    DOWNLOADED = "downloaded"     # 已下載
    TRANSCRIBING = "transcribing" # 轉錄中
    COMPLETED = "completed"       # 已完成
    FAILED = "failed"             # 處理失敗
    SKIPPED = "skipped"           # 已跳過


@dataclass(frozen=True)
class VideoState:
    """影片處理狀態記錄."""
    
    video_id: str
    channel_name: str
    title: str
    status: VideoStatus
    error_message: str | None = None
    error_category: str | None = None
    retry_count: int = 0
    created_at: float = 0.0
    updated_at: float = 0.0
    metadata: dict[str, Any] | None = None


class StateManager:
    """管理影片處理狀態的 SQLite 資料庫.
    
    核心功能：
    1. 記錄每部影片的處理狀態
    2. 支援斷點續傳（中斷後查詢已完成項目）
    3. 自動清理舊記錄
    4. 事務保證資料完整性
    """
    
    def __init__(self, db_path: Path, max_records: int = 10000, max_age_days: int = 30) -> None:
        """初始化狀態管理器.
        
        Args:
            db_path: SQLite 資料庫路徑
            max_records: 最大保留記錄數（預設 10000，約可保留 3 個月每日 100 部的量）
            max_age_days: 最大保留天數（預設 30 天）
        """
        self.db_path = db_path.resolve()
        self.max_records = max_records
        self.max_age_days = max_age_days
        self._connection: sqlite3.Connection | None = None
        
        # 確保目錄存在
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 初始化資料庫
        self._init_db()
    
    def _init_db(self) -> None:
        """初始化資料庫結構."""
        with self._get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS video_states (
                    video_id TEXT PRIMARY KEY,
                    channel_name TEXT NOT NULL,
                    title TEXT NOT NULL,
                    status TEXT NOT NULL,
                    error_message TEXT,
                    error_category TEXT,
                    retry_count INTEGER DEFAULT 0,
                    created_at REAL NOT NULL,
                    updated_at REAL NOT NULL,
                    metadata TEXT  -- JSON string
                )
            """)
            
            # 建立索引加速查詢
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_channel_status 
                ON video_states(channel_name, status)
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_updated 
                ON video_states(updated_at)
            """)
            
            conn.commit()
            logger.info("database_initialized", db_path=str(self.db_path))
    
    def _get_connection(self) -> sqlite3.Connection:
        """取得資料庫連線."""
        if self._connection is None:
            self._connection = sqlite3.connect(
                self.db_path,
                timeout=30.0,
                isolation_level=None,  # 手動控制事務
            )
            # 啟用 WAL 模式提升並發效能
            self._connection.execute("PRAGMA journal_mode=WAL")
            # 同步模式設為 NORMAL，平衡效能與安全
            self._connection.execute("PRAGMA synchronous=NORMAL")
            # 設定 busy timeout
            self._connection.execute("PRAGMA busy_timeout=5000")
        return self._connection
    
    def close(self) -> None:
        """關閉資料庫連線."""
        if self._connection:
            self._connection.close()
            self._connection = None
            logger.debug("database_closed")
    
    def __enter__(self) -> "StateManager":
        return self
    
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.close()
    
    def is_processed(self, video_id: str) -> bool:
        """檢查影片是否已完成處理.
        
        Args:
            video_id: YouTube 影片 ID
            
        Returns:
            是否已完成（completed 或 skipped）
        """
        with self._get_connection() as conn:
            cursor = conn.execute(
                """
                SELECT status FROM video_states 
                WHERE video_id = ? AND status IN (?, ?)
                """,
                (video_id, VideoStatus.COMPLETED.value, VideoStatus.SKIPPED.value)
            )
            return cursor.fetchone() is not None
    
    def get_state(self, video_id: str) -> VideoState | None:
        """取得影片的處理狀態.
        
        Args:
            video_id: YouTube 影片 ID
            
        Returns:
            影片狀態，若不存在則返回 None
        """
        with self._get_connection() as conn:
            cursor = conn.execute(
                "SELECT * FROM video_states WHERE video_id = ?",
                (video_id,)
            )
            row = cursor.fetchone()
            
            if row is None:
                return None
            
            return self._row_to_state(row)
    
    def mark_pending(
        self,
        video_id: str,
        channel_name: str,
        title: str,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        """標記影片為等待處理.
        
        Args:
            video_id: YouTube 影片 ID
            channel_name: 頻道名稱
            title: 影片標題
            metadata: 額外元數據
        """
        now = time.time()
        metadata_json = json.dumps(metadata, ensure_ascii=False) if metadata else None
        
        with self._get_connection() as conn:
            conn.execute("BEGIN IMMEDIATE")
            try:
                conn.execute(
                    """
                    INSERT INTO video_states 
                    (video_id, channel_name, title, status, created_at, updated_at, metadata)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(video_id) DO UPDATE SET
                        channel_name = excluded.channel_name,
                        title = excluded.title,
                        status = excluded.status,
                        updated_at = excluded.updated_at,
                        metadata = excluded.metadata,
                        retry_count = 0,
                        error_message = NULL,
                        error_category = NULL
                    """,
                    (video_id, channel_name, title, VideoStatus.PENDING.value, now, now, metadata_json)
                )
                conn.commit()
                logger.debug("marked_pending", video_id=video_id, title=title)
            except Exception:
                conn.rollback()
                raise
    
    def mark_status(
        self,
        video_id: str,
        status: VideoStatus,
        error_message: str | None = None,
        error_category: str | None = None,
    ) -> None:
        """更新影片處理狀態.
        
        Args:
            video_id: YouTube 影片 ID
            status: 新狀態
            error_message: 錯誤訊息（若失敗）
            error_category: 錯誤分類（若失敗）
        """
        now = time.time()
        
        # 如果是失敗狀態，增加重試計數
        retry_increment = 1 if status == VideoStatus.FAILED else 0
        
        with self._get_connection() as conn:
            conn.execute("BEGIN IMMEDIATE")
            try:
                conn.execute(
                    """
                    UPDATE video_states 
                    SET status = ?,
                        error_message = ?,
                        error_category = ?,
                        retry_count = retry_count + ?,
                        updated_at = ?
                    WHERE video_id = ?
                    """,
                    (status.value, error_message, error_category, retry_increment, now, video_id)
                )
                conn.commit()
                logger.debug("status_updated", video_id=video_id, status=status.value)
            except Exception:
                conn.rollback()
                raise
    
    def mark_completed(self, video_id: str, output_path: str | None = None) -> None:
        """標記影片為已完成.
        
        Args:
            video_id: YouTube 影片 ID
            output_path: 輸出檔案路徑
        """
        now = time.time()
        metadata_update = json.dumps({"output_path": output_path}) if output_path else None
        
        with self._get_connection() as conn:
            conn.execute("BEGIN IMMEDIATE")
            try:
                if metadata_update:
                    conn.execute(
                        """
                        UPDATE video_states 
                        SET status = ?,
                            updated_at = ?,
                            metadata = ?,
                            error_message = NULL,
                            error_category = NULL
                        WHERE video_id = ?
                        """,
                        (VideoStatus.COMPLETED.value, now, metadata_update, video_id)
                    )
                else:
                    conn.execute(
                        """
                        UPDATE video_states 
                        SET status = ?,
                            updated_at = ?,
                            error_message = NULL,
                            error_category = NULL
                        WHERE video_id = ?
                        """,
                        (VideoStatus.COMPLETED.value, now, video_id)
                    )
                conn.commit()
                logger.info("marked_completed", video_id=video_id)
            except Exception:
                conn.rollback()
                raise
    
    def mark_skipped(self, video_id: str, reason: str = "") -> None:
        """標記影片為已跳過（例如會員專屬、私人影片等預期無法處理的內容）.
        
        Args:
            video_id: YouTube 影片 ID
            reason: 跳過原因（例如 "members_only", "private", "unavailable"）
        """
        self.mark_status(video_id, VideoStatus.SKIPPED, error_message=reason)
        logger.info("marked_skipped", video_id=video_id, reason=reason)
    
    def get_pending_videos(self, channel_name: str | None = None) -> list[VideoState]:
        """取得等待處理的影片列表.
        
        Args:
            channel_name: 若指定則只返回該頻道的影片
            
        Returns:
            影片狀態列表
        """
        with self._get_connection() as conn:
            if channel_name:
                cursor = conn.execute(
                    """
                    SELECT * FROM video_states 
                    WHERE channel_name = ? AND status = ?
                    ORDER BY created_at
                    """,
                    (channel_name, VideoStatus.PENDING.value)
                )
            else:
                cursor = conn.execute(
                    """
                    SELECT * FROM video_states 
                    WHERE status = ?
                    ORDER BY created_at
                    """,
                    (VideoStatus.PENDING.value,)
                )
            
            return [self._row_to_state(row) for row in cursor.fetchall()]
    
    def get_stats(self, channel_name: str | None = None) -> dict[str, int]:
        """取得處理統計資訊.
        
        Args:
            channel_name: 若指定則只統計該頻道
            
        Returns:
            各狀態數量統計
        """
        with self._get_connection() as conn:
            if channel_name:
                cursor = conn.execute(
                    "SELECT status, COUNT(*) FROM video_states WHERE channel_name = ? GROUP BY status",
                    (channel_name,)
                )
            else:
                cursor = conn.execute("SELECT status, COUNT(*) FROM video_states GROUP BY status")
            
            stats = {status.value: 0 for status in VideoStatus}
            for row in cursor.fetchall():
                stats[row[0]] = row[1]
            return stats
    
    def cleanup(self) -> int:
        """清理舊記錄.
        
        清理規則：
        1. 超過 max_age_days 天的記錄
        2. 若記錄數超過 max_records，刪除最舊的
        
        Returns:
            刪除的記錄數
        """
        cutoff_time = time.time() - (self.max_age_days * 24 * 3600)
        deleted = 0
        
        with self._get_connection() as conn:
            conn.execute("BEGIN IMMEDIATE")
            try:
                # 1. 刪除超過天數的已完成/跳過記錄
                cursor = conn.execute(
                    """
                    DELETE FROM video_states 
                    WHERE status IN (?, ?) AND updated_at < ?
                    """,
                    (VideoStatus.COMPLETED.value, VideoStatus.SKIPPED.value, cutoff_time)
                )
                deleted += cursor.rowcount
                
                # 2. 若記錄數仍超過限制，刪除最舊的已完成/跳過記錄
                cursor = conn.execute(
                    """
                    SELECT COUNT(*) FROM video_states 
                    WHERE status IN (?, ?)
                    """,
                    (VideoStatus.COMPLETED.value, VideoStatus.SKIPPED.value)
                )
                completed_count = cursor.fetchone()[0]
                
                if completed_count > self.max_records:
                    to_delete = completed_count - self.max_records
                    cursor = conn.execute(
                        """
                        DELETE FROM video_states 
                        WHERE video_id IN (
                            SELECT video_id FROM video_states 
                            WHERE status IN (?, ?)
                            ORDER BY updated_at ASC
                            LIMIT ?
                        )
                        """,
                        (VideoStatus.COMPLETED.value, VideoStatus.SKIPPED.value, to_delete)
                    )
                    deleted += cursor.rowcount
                
                conn.commit()
                if deleted > 0:
                    logger.info("cleanup_completed", deleted=deleted)
                return deleted
            except Exception:
                conn.rollback()
                raise
    
    def _row_to_state(self, row: sqlite3.Row) -> VideoState:
        """將資料庫行轉換為 VideoState."""
        metadata = None
        if row[9]:  # metadata column
            try:
                metadata = json.loads(row[9])
            except json.JSONDecodeError:
                pass
        
        return VideoState(
            video_id=row[0],
            channel_name=row[1],
            title=row[2],
            status=VideoStatus(row[3]),
            error_message=row[4],
            error_category=row[5],
            retry_count=row[6] or 0,
            created_at=row[7] or 0.0,
            updated_at=row[8] or 0.0,
            metadata=metadata,
        )
