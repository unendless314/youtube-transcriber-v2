# 狀態管理設計

> **版本**: 2.0  
> **狀態**: 📝 設計階段  
> **最後更新**: 2026-02-05

---

## 1. 設計目標

### V1 的問題
- JSON 檔案斷電時容易損壞
- 查詢需要線性掃描（O(n)）
- 無法記錄「處理中」狀態
- 檔案大小無限增長

### V2 的解決方案
- **SQLite 資料庫**：原子寫入，斷電安全
- **自動清理**：只保留最近 7 天或 100 筆
- **精確狀態**：pending → processing → success/failed/skipped
- **快速查詢**：索引優化，O(log n)

---

## 2. 狀態機

### 2.1 狀態定義

```
┌─────────────────────────────────────────────────────────────────┐
│                        VideoStatus                              │
│                                                                 │
│   ┌──────────┐                                                 │
│   │  PENDING │ 初始狀態，等待處理                               │
│   └────┬─────┘                                                 │
│        │ 開始處理                                               │
│        ▼                                                        │
│   ┌──────────┐                                                 │
│   │PROCESSING│ 正在處理中                                       │
│   └────┬─────┘                                                 │
│        │                                                        │
│   ┌────┴────┬──────────┐                                       │
│   │         │          │                                       │
│   ▼         ▼          ▼                                       │
│ ┌──────┐  ┌──────┐  ┌────────┐                                │
│ │SUCCESS│  │FAILED│  │SKIPPED │                                │
│ └──────┘  └──┬───┘  └────────┘                                │
│              │                                                  │
│              │ 重試（若 attempts < max_attempts）               │
│              └──────────────► ┌──────────┐                     │
│                               │ 回到     │                     │
│                               │ PENDING  │                     │
│                               └──────────┘                     │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 狀態轉換規則

| 從狀態 | 到狀態 | 觸發條件 |
|--------|--------|----------|
| - | PENDING | 發現新影片 |
| PENDING | PROCESSING | 開始處理影片 |
| PROCESSING | SUCCESS | 處理成功完成 |
| PROCESSING | FAILED | 處理失敗，可重試 |
| PROCESSING | SKIPPED | 處理失敗，不可重試（影片問題） |
| FAILED | PENDING | 用戶手動重置或達到重試時間 |

---

## 3. 核心操作

### 3.1 狀態查詢

```python
class StateManager:
    """狀態管理器介面"""
    
    def is_processed(self, video_id: str) -> bool:
        """
        檢查影片是否已處理（成功或跳過）。
        
        用於：決定是否跳過此影片
        """
        ...
    
    def get_video_status(self, video_id: str) -> Optional[VideoStatus]:
        """
        獲取影片當前狀態。
        
        用於：檢查點恢復、顯示狀態
        """
        ...
    
    def get_pending_videos(
        self, 
        channel: Optional[str] = None
    ) -> List[VideoRecord]:
        """
        獲取待處理影片列表。
        
        包含：
        - status = PENDING
        - status = FAILED 且 attempts < max_attempts
        
        用於：啟動時決定要處理哪些影片
        """
        ...
```

### 3.2 狀態更新

```python
def mark_pending(self, video: VideoInfo) -> None:
    """
    標記影片為待處理。
    
    時機：發現新影片時
    """
    ...

def mark_processing(self, video_id: str) -> None:
    """
    標記影片為處理中。
    
    時機：開始下載前
    作用：
    - 防止重複處理（冪等性）
    - 崩潰後知道「這部影片處理到一半」
    """
    ...

def mark_completed(self, result: ProcessingResult) -> None:
    """
    標記影片為處理成功。
    
    Args:
        result: ProcessingResult 物件，包含處理結果資訊
    
    時機：Markdown 儲存完成後
    """
    ...

def mark_failed(self, video_id: str, error: ErrorInfo) -> None:
    """
    標記影片為處理失敗。
    
    Args:
        video_id: 影片 ID
        error: ErrorInfo 物件，包含錯誤分類和訊息
        
    根據 error.category 自動決定狀態：
    - PERMANENT_SKIP → 'skipped'
    - 其他 → 'failed'
    """
    ...
```

---

## 4. 檢查點機制

### 4.1 為什麼需要檢查點？

**情境**：一部影片的處理流程
```
Download (5 min) → Transcribe (30 min) → Save (1 sec) → Cleanup (1 sec)
```

如果在 Transcribe 階段斷電：
- **無檢查點**：下次從頭開始（重新下載、重新轉錄）= 浪費 35 分鐘
- **有檢查點**：從 Save 開始（音訊檔案已存在，可跳過 Download 和 Transcribe）

### 4.2 檢查點策略

**V2 採用：簡化檢查點（僅影片級）**

不記錄 Stage 級檢查點（太複雜），而是：
1. 每部影片處理完成後立即 commit
2. 若中斷，該影片從頭開始（可接受，因為影片數量不多）
3. 暫存檔案可復用（若存在則跳過下載）

**理由**：
- 程式碼簡單，不容易出錯
- 頻道通常只有 5-10 部新影片
- 單部影片重複處理的損失可接受

### 4.3 暫存檔案復用

```python
class DownloadStage:
    def can_skip(self, context: PipelineContext) -> bool:
        """檢查是否可跳過下載"""
        expected_path = self._get_audio_path(context)
        
        # 檔案存在且大小合理（> 10KB）
        if expected_path.exists():
            size = expected_path.stat().st_size
            if size > 10 * 1024:
                logger.info(
                    "Found existing audio file, skipping download",
                    video_id=context.video.video_id,
                    size_mb=size / 1024 / 1024
                )
                return True
        
        return False
```

---

## 5. 自動清理策略

### 5.1 清理觸發條件

| 狀態 | 保留時間 | 說明 |
|------|----------|------|
| `success` | 30 天 | 成功的影片記錄，避免短期內重複處理 |
| `failed` | 7 天 | 失敗記錄，7 天後可重試 |
| `skipped` | 7 天 | 跳過記錄，通常不會再變化 |
| `pending`/`processing` | 不清除 | 未完成的不應被清除 |

```sql
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

-- 數量限制（只清理 failed 和 skipped）
DELETE FROM processed_videos 
WHERE status IN ('failed', 'skipped')
AND video_id IN (
    SELECT video_id 
    FROM processed_videos 
    WHERE status IN ('failed', 'skipped')
    ORDER BY created_at DESC 
    LIMIT -1 OFFSET 100
);
```

### 5.2 清理時機

**自動清理**：每次插入新記錄後（由觸發器處理）

```sql
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

**理由**：
- `success` 保留 30 天：避免用戶短期內重複處理（如休假回來）
- `failed`/`skipped` 保留 7 天：足夠時間診斷問題
- 100 筆限制：控制資料庫大小，但保留足夠診斷資訊
- 無需手動維護，檔案大小穩定（約 300KB）

### 5.3 手動清理選項

```python
def cleanup(self, days: int = 7, max_records: int = 100) -> int:
    """
    手動清理舊資料。
    
    Returns:
        刪除的記錄數
    """
    ...

def reset(self) -> None:
    """
    重置資料庫（刪除所有資料）。
    
    用於：
    - 重新處理所有影片
    - 資料庫損壞時重建
    """
    ...
```

---

## 6. 資料庫檔案管理

### 6.1 檔案位置

```
預設位置：<output_dir>/.state.db

範例：
./output/
├── 老高與小茉/
│   └── 2026-01/
│       └── ...
├── .state.db          ← 狀態資料庫（隱藏檔案）
└── logs/
```

### 6.2 檔案大小預估

| 記錄數 | 預估大小 |
|--------|----------|
| 10 筆 | ~30 KB |
| 50 筆 | ~150 KB |
| 100 筆（上限） | ~300 KB |
| 500 筆 | ~1.5 MB |

**實際場景**：
- 每天處理 5 部影片
- 7 天 = 35 筆記錄
- 資料庫大小 ≈ 100 KB

### 6.3 備份與遷移

**備份**：SQLite 檔案可直接複製
```bash
# 手動備份
cp output/.state.db output/.state.db.backup.$(date +%Y%m%d)

# 自動備份（可選功能）
youtube-transcriber --backup-state
```

**遷移（V1 → V2）**：
```python
def migrate_from_v1(json_path: Path, db_path: Path) -> int:
    """
    將 V1 的 processed_ids.json 遷移到 V2 SQLite。
    
    Returns:
        遷移的記錄數
    """
    import json
    
    with open(json_path) as f:
        data = json.load(f)
    
    state = StateManager(db_path)
    
    for record in data.get("processed_ids", []):
        # 轉換格式並插入
        ...
    
    return migrated_count
```

---

## 7. 使用範例

### 7.1 基本流程

```python
from pathlib import Path

# 初始化
state = StateManager(Path("output/.state.db"))

# 處理流程
for video in new_videos:
    # 1. 檢查是否已處理
    if state.is_processed(video.video_id):
        print(f"Skip: {video.title}")
        continue
    
    # 2. 標記為處理中
    state.mark_processing(video.video_id)
    
    try:
        # 3. 處理影片
        result = process_video(video)
        
        # 4. 標記為成功
        state.mark_completed(
            video_id=video.video_id,
            output_path=result.output_path,
            word_count=result.word_count,
            processing_time_seconds=result.duration
        )
    
    except Exception as e:
        # 5. 標記為失敗
        state.mark_failed(
            video_id=video.video_id,
            error_type=type(e).__name__,
            error_message=str(e)
        )
```

### 7.2 查詢統計

```python
# 頻道統計
stats = state.get_channel_stats("老高與小茉")
print(f"""
頻道：{stats['channel']}
總數：{stats['total']}
成功：{stats['success']}
失敗：{stats['failed']}
待處理：{stats['pending']}
""")

# 整體統計
overall = state.get_overall_stats()
print(f"總處理影片數：{overall['total']}")

# 資料庫大小
size_kb = state.get_database_size() / 1024
print(f"資料庫大小：{size_kb:.1f} KB")
```

### 7.3 處理中斷恢復

```python
# 啟動時檢查
pending = state.get_pending_videos()

for video in pending:
    status = state.get_video_status(video.video_id)
    
    if status == VideoStatus.PROCESSING:
        # 上次處理到一半，可能是：
        # - 下載完成，轉錄中斷 → 可復用音訊檔案
        # - 其他情況 → 從頭開始
        print(f"Resuming: {video.title}")
    
    # 重新處理
    process_video(video)
```

---

## 8. 故障處理

### 8.1 資料庫損壞檢測

```python
def _verify_database(self) -> bool:
    """驗證資料庫完整性"""
    try:
        with self._get_connection() as conn:
            # SQLite 內建完整性檢查
            result = conn.execute("PRAGMA integrity_check").fetchone()
            return result[0] == "ok"
    except sqlite3.Error:
        return False

def _init_database(self) -> None:
    """初始化資料庫（含損壞檢測）"""
    if self.db_path.exists():
        if not self._verify_database():
            logger.error("Database corrupted, recreating")
            self.db_path.unlink()  # 刪除損壞檔案
    
    # 建立新資料庫
    with sqlite3.connect(self.db_path) as conn:
        conn.executescript(self.SCHEMA)
```

### 8.2 從損壞恢復

```python
def recover_or_reset(self) -> bool:
    """
    嘗試恢復或重置資料庫。
    
    Returns:
        True = 恢復成功，False = 已重置
    """
    # 嘗試修復（SQLite 內建）
    try:
        with self._get_connection() as conn:
            conn.execute("REINDEX")
            conn.execute("VACUUM")
        return True
    except:
        pass
    
    # 無法修復，重置
    self.reset()
    return False
```

---

**最後更新**: 2026-02-05  
**文件狀態**: 📝 設計階段
