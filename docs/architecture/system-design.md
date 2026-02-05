# V2 系統架構設計

> **版本**: 2.0  
> **狀態**: 📝 設計階段  
> **最後更新**: 2026-02-05

---

## 1. 設計原則

### Core Principles
1. **Reliability First** - 穩定性優先於性能
2. **Simplicity** - 單線程序列處理，不做過度設計
3. **Fail-Safe** - 優雅處理所有失敗場景
4. **Observable** - 內建完整的可觀測性
5. **Modular** - 高內聚、低耦合、易測試

### 關鍵決策
- **單線程**：Whisper 已吃滿資源，並行無收益
- **SQLite**：斷電安全，零配置，自動清理
- **Pipeline**：清晰的處理流程，易於擴展

---

## 2. 整體架構

### 2.1 分層架構圖

```
┌─────────────────────────────────────────────────────────────────────┐
│                           CLI Layer                                  │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐  │
│  │ Argument Parser  │  │ Progress Display │  │ Logger Setup     │  │
│  │ (Click)          │  │ (Rich)           │  │ (structlog)      │  │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     Orchestration Layer                              │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                    Pipeline Orchestrator                       │  │
│  │  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   │  │
│  │  │ Download │ → │Transcribe│ → │   Save   │ → │ Cleanup  │   │  │
│  │  │  Stage   │   │  Stage   │   │  Stage   │   │  Stage   │   │  │
│  │  └──────────┘   └──────────┘   └──────────┘   └──────────┘   │  │
│  └───────────────────────────────────────────────────────────────┘  │
│  ┌──────────────────┐  ┌──────────────────┐                         │
│  │ Channel Iterator │  │ Retry Engine     │                         │
│  └──────────────────┘  └──────────────────┘                         │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     Infrastructure Layer                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐              │
│  │ State Manager│  │ Error Handler│  │ Checkpoint   │              │
│  │ (SQLite)     │  │ & Classifier │  │ Manager      │              │
│  └──────────────┘  └──────────────┘  └──────────────┘              │
│  ┌──────────────┐  ┌──────────────┐                                 │
│  │ Config       │  │ Metrics      │                                 │
│  │ Manager      │  │ Collector    │                                 │
│  └──────────────┘  └──────────────┘                                 │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        Backend Layer                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐              │
│  │ yt-dlp       │  │ Whisper      │  │ File System  │              │
│  │ (Downloader) │  │ Backends     │  │ (Storage)    │              │
│  └──────────────┘  └──────────────┘  └──────────────┘              │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.2 資料流向

```
┌──────────────┐
│ channels.yaml│
└──────┬───────┘
       │ 1. 讀取配置
       ▼
┌──────────────┐
│ConfigManager │──────┐
└──────────────┘      │
                      │ 2. 驗證配置
                      ▼
               ┌──────────────┐
               │    Config    │
               │   (Pydantic) │
               └──────┬───────┘
                      │
       ┌──────────────┼──────────────┐
       │              │              │
       ▼              ▼              ▼
┌──────────────┐ ┌──────────┐ ┌──────────────┐
│ChannelIterator│ │StateManager│ │ProgressDisplay│
└──────┬───────┘ └──────────┘ └──────────────┘
       │
       │ 3. 遍歷每個頻道
       ▼
┌─────────────────────────────────────────────┐
│               Channel Loop                   │
│  ┌───────────────────────────────────────┐  │
│  │ 4. 獲取最新 N 部影片 (yt-dlp)          │  │
│  └───────────────────────────────────────┘  │
│                    │                         │
│                    ▼                         │
│  ┌───────────────────────────────────────┐  │
│  │ 5. 過濾已處理的影片 (SQLite 查詢)       │  │
│  └───────────────────────────────────────┘  │
│                    │                         │
│                    ▼                         │
│  ┌───────────────────────────────────────┐  │
│  │ 6. 對每部新影片執行 Pipeline           │  │
│  │   ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐│  │
│  │   │Download→Transcribe→Save→Cleanup││  │
│  │   └──────┘ └──────┘ └──────┘ └──────┘│  │
│  └───────────────────────────────────────┘  │
│                    │                         │
│                    ▼                         │
│  ┌───────────────────────────────────────┐  │
│  │ 7. 更新狀態 (SQLite)                   │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

---

## 3. 核心模組設計

### 3.1 ConfigManager 配置管理

**職責**：
- 讀取並解析 `channels.yaml`
- 驗證配置正確性
- 提供型別安全的配置訪問

**接口**：
```python
class ConfigManager:
    def load(self, path: Path) -> Config
    def validate(self, config: Config) -> ValidationResult
    
class Config(BaseModel):
    output: OutputConfig
    whisper: WhisperConfig
    global_settings: GlobalConfig
    channels: List[ChannelConfig]
```

**設計要點**：
- 使用 Pydantic v2 進行配置驗證
- 啟動時立即驗證，早發現錯誤
- 支援頻道級配置覆寫

---

### 3.2 StateManager 狀態管理

**職責**：
- SQLite 資料庫操作
- 影片狀態查詢與更新
- 自動清理舊資料

**接口**：
```python
class StateManager:
    def __init__(self, db_path: Path)
    
    # 查詢
    def is_processed(self, video_id: str) -> bool
    def get_pending_videos(self, channel: str) -> List[VideoRecord]
    def get_video_status(self, video_id: str) -> Optional[VideoStatus]
    
    # 更新
    def mark_pending(self, video: VideoInfo) -> None
    def mark_processing(self, video_id: str) -> None
    def mark_completed(self, result: ProcessingResult) -> None
    def mark_failed(self, video_id: str, error: ErrorInfo) -> None
    
    # 統計
    def get_channel_stats(self, channel: str) -> ChannelStats
    def cleanup_old_records(self, days: int = 7, max_records: int = 100) -> int
```

**設計要點**：
- 單線程訪問（不需要鎖）
- 每次操作後自動 commit
- 自動清理：保留最近 7 天或最近 100 筆（取較大者）

---

### 3.3 Pipeline 處理流程

**職責**：
- 協調影片處理的各個階段
- 管理 Stage 執行順序
- 處理 Stage 間的資料傳遞

**接口**：
```python
class VideoPipeline:
    def __init__(
        self,
        stages: List[ProcessingStage],
        state_manager: StateManager,
        retry_engine: RetryEngine,
        progress_tracker: ProgressTracker
    )
    
    def process(self, video: VideoInfo, context: PipelineContext) -> PipelineResult
    
class ProcessingStage(Protocol):
    name: str
    def execute(self, context: PipelineContext) -> StageResult
    def rollback(self, context: PipelineContext) -> None
```

**預設 Stages**：

| Stage | 職責 | 輸入 | 輸出 |
|-------|------|------|------|
| DownloadStage | 下載音訊 | video_id | audio_path, duration |
| TranscribeStage | Whisper 轉錄 | audio_path | transcript_text, language |
| SaveStage | 儲存 Markdown | transcript_text, metadata | output_path |
| CleanupStage | 清理暫存檔 | audio_path | - |

---

### 3.4 RetryEngine 重試引擎

**職責**：
- 根據錯誤類型決定重試策略
- 執行指數退避
- 管理重試次數上限

**接口**：
```python
class RetryEngine:
    def __init__(
        self,
        state_manager: StateManager,
        policies: Dict[ErrorCategory, RetryPolicy]
    )
    
    def execute(
        self,
        operation: Callable[[], T],
        video_id: str,
        stage: str
    ) -> T
    
class RetryPolicy:
    max_attempts: int
    backoff_strategy: str  # fixed / linear / exponential
    backoff_base_seconds: int
```

**錯誤分類與策略**：

| ErrorCategory | 重試次數 | 退避策略 | 範例 |
|---------------|---------|----------|------|
| RETRYABLE_IMMEDIATE | 3 | fixed 5s | 網路斷線、超時 |
| RETRYABLE_DELAYED | 5 | exponential 5min | Rate limit 429 |
| RETRYABLE_FALLBACK | 2 | fixed 0s | OOM 換小模型 |
| PERMANENT_SKIP | 0 | - | 影片刪除、版權限制 |
| PERMANENT_FATAL | 0 | - | 磁碟滿、權限問題 |

---

### 3.5 ProgressTracker 進度追蹤

**職責**：
- 顯示實時進度
- 預估剩餘時間
- 提供處理統計

**接口**：
```python
class ProgressTracker:
    def __init__(self, state_manager: StateManager, console: Console)
    
    def start_channel(self, channel: str, total_videos: int)
    def update_video(self, video: VideoInfo, status: VideoStatus)
    def complete_channel(self, channel: str, stats: ChannelStats)
    def estimate_remaining_time(self) -> timedelta
    
    # 顯示格式
    def render_progress(self) -> RenderableType
```

**顯示範例**：
```
處理頻道: 老高與小茉 [3/10]
[████████████░░░░░░░░] 45% (9/20 videos) | ETA: 1h 23m

  ├─ [✓] 影片標題一 (5:23) - 完成 (2m 15s)
  ├─ [✓] 影片標題二 (12:45) - 完成 (5m 30s)
  ├─ [🎙️] 影片標題三 (8:12) - 轉錄中 (預估 32m)
  └─ [⏳] 影片標題四 (15:30) - 等待中

總進度: [███████░░░░░░░░░░░░░] 35% | 已處理 35/100 | ETA: 3h 45m
```

---

### 3.6 Whisper Backend 抽象

**職責**：
- 抽象不同 Whisper 實現
- 統一接口，方便切換

**接口**：
```python
class WhisperBackend(Protocol):
    def transcribe(
        self,
        audio_path: Path,
        language: Optional[str] = None,
        **options
    ) -> TranscriptionResult
    
    def is_available(self) -> bool
    def get_model_info(self) -> ModelInfo

# 實現類
class OpenAIWhisperBackend(WhisperBackend): ...
class WhisperCppBackend(WhisperBackend): ...
class FasterWhisperBackend(WhisperBackend): ...
```

---

## 4. 資料模型

### 4.1 核心資料類別

```python
@dataclass
class VideoInfo:
    """影片資訊（從 yt-dlp 獲取）"""
    video_id: str
    title: str
    channel: str
    url: str
    duration_seconds: int
    published_at: datetime

@dataclass
class PipelineContext:
    """Pipeline 執行上下文"""
    video: VideoInfo
    config: ChannelConfig
    temp_dir: Path
    output_dir: Path
    # 各 Stage 產出的資料
    audio_path: Optional[Path] = None
    transcript_text: Optional[str] = None
    transcript_language: Optional[str] = None
    output_path: Optional[Path] = None

@dataclass
class ProcessingResult:
    """
    影片處理結果。
    
    由 Pipeline 產出，傳遞給 StateManager 記錄狀態，
    或用於錯誤處理時的上下文。
    """
    success: bool
    video_id: str
    output_path: Optional[Path] = None
    word_count: Optional[int] = None
    processing_time_seconds: Optional[float] = None
    error: Optional[ErrorInfo] = None
    
    @property
    def is_success(self) -> bool:
        """是否處理成功"""
        return self.success and self.error is None
```

---

## 5. 錯誤處理架構

### 5.1 錯誤傳播流程

```
┌───────────────────────────────────────────────────────────────┐
│                         執行操作                               │
└───────────────────────┬───────────────────────────────────────┘
                        │
            ┌───────────┴───────────┐
            │                       │
            ▼                       ▼
    ┌───────────────┐       ┌───────────────┐
    │    成功       │       │    失敗       │
    └───────┬───────┘       └───────┬───────┘
            │                       │
            │                       ▼
            │               ┌───────────────┐
            │               │ ErrorClassifier│
            │               └───────┬───────┘
            │                       │
            │           ┌───────────┼───────────┐
            │           │           │           │
            │           ▼           ▼           ▼
            │    ┌──────────┐ ┌──────────┐ ┌──────────┐
            │    │ RETRYABLE│ │ PERMANENT│ │  FATAL   │
            │    │          │ │  _SKIP   │ │          │
            │    └────┬─────┘ └────┬─────┘ └────┬─────┘
            │         │            │            │
            │         ▼            ▼            ▼
            │    ┌──────────┐ ┌──────────┐ ┌──────────┐
            │    │  重試    │ │  跳過    │ │  終止    │
            │    │  (N次)   │ │  影片    │ │  程式    │
            │    └────┬─────┘ └────┬─────┘ └────┬─────┘
            │         │            │            │
            └─────────┴────────────┴────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │ 更新 SQLite 狀態 │
                    └─────────────────┘
```

### 5.2 錯誤隔離保證

- **Stage 級隔離**：單一 Stage 失敗可選擇重試或跳過
- **影片級隔離**：單一影片失敗不影響其他影片
- **頻道級隔離**：單一頻道失敗不影響其他頻道（除非 FATAL 錯誤）

---

## 6. 部署與運行

### 6.1 專案結構

```
youtube-transcriber-v2/
├── src/
│   └── transcriber/
│       ├── __init__.py
│       ├── __main__.py          # CLI 入口
│       ├── cli.py               # Click 命令定義
│       ├── config/
│       │   ├── __init__.py
│       │   ├── models.py        # Pydantic 模型
│       │   └── manager.py       # ConfigManager
│       ├── pipeline/
│       │   ├── __init__.py
│       │   ├── orchestrator.py  # Pipeline 協調器
│       │   ├── stages.py        # Stage 實現
│       │   └── context.py       # PipelineContext
│       ├── core/
│       │   ├── __init__.py
│       │   ├── state.py         # StateManager
│       │   ├── retry.py         # RetryEngine
│       │   ├── errors.py        # 錯誤分類
│       │   └── progress.py      # ProgressTracker
│       ├── backends/
│       │   ├── __init__.py
│       │   ├── base.py          # WhisperBackend Protocol
│       │   ├── openai_whisper.py
│       │   ├── whisper_cpp.py
│       │   └── faster_whisper.py
│       └── utils/
│           ├── __init__.py
│           ├── logging.py       # structlog 配置
│           └── validators.py    # 驗證工具
├── tests/
│   ├── unit/
│   ├── integration/
│   └── conftest.py
├── docs_v2/
├── channels.yaml.example
├── pyproject.toml
└── README.md
```

### 6.2 安裝與運行

```bash
# 安裝
pip install youtube-transcriber-v2

# 或使用 uv
uv pip install youtube-transcriber-v2

# 首次運行（生成範例配置）
youtube-transcriber --init

# 編輯配置
vim channels.yaml

# 測試模式
youtube-transcriber --dry-run

# 正式運行
youtube-transcriber
```

---

## 7. 技術債務與風險

### 7.1 已知限制

| 限制 | 說明 | 緩解 |
|------|------|------|
| 單線程 | 無法並行處理多部影片 | 文檔說明，未來可考慮 multi-process |
| SQLite 單機 | 不支援多機部署 | 本質是單機工具，非設計目標 |
| YouTube 限制 | 可能被封鎖 IP | cookies 支援、rate limiting |

### 7.2 未來擴展點

- **並行處理**：如需並行，可將 Pipeline 改為 multi-process（每部影片獨立程序）
- **雲端儲存**：Backend 抽象可擴展支援 S3/GCS
- **API 模式**：CLI 層可抽離，暴露 HTTP API

---

**最後更新**: 2026-02-05  
**文件狀態**: 📝 設計階段，待 Review
