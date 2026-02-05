# Pipeline 設計

> **版本**: 2.0  
> **狀態**: 📝 設計階段  
> **最後更新**: 2026-02-05

---

## 1. 設計目標

### 為什麼需要 Pipeline？

V1 的 `main.py` 存在以下問題：
- 函數過長，職責混雜（下載、轉錄、儲存、清理都在一處）
- 難以測試（需要 mock 所有依賴）
- 難以擴展（新增功能要改 main.py）
- 錯誤處理複雜（不同階段需要不同策略）

### Pipeline 解決方案

- **單一職責**：每個 Stage 只做一件事
- **可組合**：Stages 可自由組合、插入、移除
- **可測試**：每個 Stage 可獨立測試
- **可觀測**：每個 Stage 的執行時間、結果都可追蹤

---

## 2. Pipeline 架構

### 2.1 整體流程

```
┌─────────────────────────────────────────────────────────────────┐
│                    Video Pipeline                               │
│                                                                 │
│   Input: VideoInfo + Config                                     │
│                              │                                  │
│                              ▼                                  │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │  Stage 1: DownloadStage                                 │  │
│   │  - 使用 yt-dlp 下載音訊                                 │  │
│   │  - 驗證音訊檔案完整性                                   │  │
│   │  - 輸出: audio_path, duration                           │  │
│   └─────────────────────────────────────────────────────────┘  │
│                              │                                  │
│                              ▼                                  │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │  Stage 2: TranscribeStage                               │  │
│   │  - 使用 Whisper 轉錄                                    │  │
│   │  - 輸出: transcript_text, language, word_count          │  │
│   └─────────────────────────────────────────────────────────┘  │
│                              │                                  │
│                              ▼                                  │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │  Stage 3: SaveStage                                     │  │
│   │  - 生成 Markdown 格式                                   │  │
│   │  - 寫入檔案系統                                         │  │
│   │  - 輸出: output_path                                    │  │
│   └─────────────────────────────────────────────────────────┘  │
│                              │                                  │
│                              ▼                                  │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │  Stage 4: CleanupStage                                  │  │
│   │  - 刪除暫存音訊檔                                       │  │
│   │  - 輸出: None                                           │  │
│   └─────────────────────────────────────────────────────────┘  │
│                              │                                  │
│                              ▼                                  │
│   Output: PipelineResult (success/failed + context)             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 錯誤處理與恢復

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│ Download │ ──► │Transcribe│ ──► │   Save   │ ──► │ Cleanup  │
└────┬─────┘     └────┬─────┘     └────┬─────┘     └────┬─────┘
     │                │                │                │
     │ 失敗           │ 失敗           │ 失敗           │ 失敗
     │                │                │                │
     ▼                ▼                ▼                ▼
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│ 重試機制 │     │ 重試機制 │     │ 重試機制 │     │ 僅記錄   │
│ 或 跳過  │     │ 或 跳過  │     │ 或 跳過  │     │ 不影響   │
└──────────┘     └──────────┘     └──────────┘     └──────────┘
     │                │                │                │
     │ 重試成功       │ 重試成功       │ 重試成功       │
     │                │                │                │
     └──────────────► └──────────────► └──────────────► └───────►
                              (從失敗處繼續)
```

---

## 3. 核心接口

### 3.1 ProcessingStage Protocol

```python
from typing import Protocol, runtime_checkable
from dataclasses import dataclass
from enum import Enum, auto

class StageStatus(Enum):
    SUCCESS = auto()
    FAILED = auto()
    SKIPPED = auto()
    RETRYABLE = auto()

@dataclass
class StageResult:
    """Stage 執行結果"""
    status: StageStatus
    context_updates: dict  # 要更新到 PipelineContext 的資料
    error: Optional[ErrorInfo] = None
    retry_after_seconds: Optional[int] = None  # 僅 RETRYABLE 時使用

@runtime_checkable
class ProcessingStage(Protocol):
    """Stage 接口定義"""
    
    @property
    def name(self) -> str:
        """Stage 名稱，用於日誌和檢查點"""
        ...
    
    def execute(self, context: PipelineContext) -> StageResult:
        """執行 Stage 邏輯"""
        ...
    
    def rollback(self, context: PipelineContext) -> None:
        """
        回滾操作（可選）。
        當 Stage 失敗且需要清理時呼叫。
        """
        ...
    
    def can_skip(self, context: PipelineContext) -> bool:
        """
        檢查是否可以跳過此 Stage。
        例如：音訊檔案已存在時跳過下載。
        """
        return False
```

### 3.2 PipelineContext

```python
@dataclass
class PipelineContext:
    """Pipeline 執行上下文"""
    # 輸入
    video: VideoInfo
    config: ChannelConfig
    global_config: GlobalConfig
    
    # 路徑
    temp_dir: Path
    output_dir: Path
    
    # Stage 產出的中間資料
    audio_path: Optional[Path] = None
    audio_duration: Optional[int] = None  # 秒
    transcript_text: Optional[str] = None
    transcript_language: Optional[str] = None
    word_count: Optional[int] = None
    output_path: Optional[Path] = None
    
    # 執行追蹤
    current_stage: Optional[str] = None
    stage_start_time: Optional[datetime] = None
    processing_started_at: Optional[datetime] = None  # 影片開始處理時間
    
    def update(self, **kwargs) -> None:
        """更新上下文"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"PipelineContext 沒有屬性: {key}")
```

### 3.3 Pipeline Orchestrator

```python
class PipelineOrchestrator:
    """Pipeline 協調器"""
    
    def __init__(
        self,
        stages: List[ProcessingStage],
        state_manager: StateManager,
        retry_engine: RetryEngine,
        progress_tracker: Optional[ProgressTracker] = None
    ):
        self.stages = stages
        self.state_manager = state_manager
        self.retry_engine = retry_engine
        self.progress_tracker = progress_tracker
        self.logger = structlog.get_logger()
    
    def process(
        self,
        video: VideoInfo,
        config: ChannelConfig,
        global_config: GlobalConfig
    ) -> PipelineResult:
        """
        處理單一影片。
        
        流程:
        1. 檢查是否已處理（冪等性）
        2. 標記為 processing
        3. 依序執行各 Stage
        4. 每個 Stage 失敗時嘗試重試
        5. 更新最終狀態
        """
        # 檢查是否已處理
        if self.state_manager.is_processed(video.video_id):
            self.logger.info(
                "video_already_processed",
                video_id=video.video_id
            )
            return PipelineResult.skipped(video.video_id, "already_processed")
        
        # 建立上下文
        context = PipelineContext(
            video=video,
            config=config,
            global_config=global_config,
            temp_dir=Path(global_config.output.base_dir) / "temp",
            output_dir=Path(global_config.output.base_dir) / video.channel
        )
        
        # 標記為 processing
        self.state_manager.mark_processing(video.video_id)
        
        # 執行各 Stage
        for stage in self.stages:
            result = self._execute_stage(stage, context)
            
            if result.status == StageStatus.SUCCESS:
                context.update(**result.context_updates)
                continue
            
            elif result.status == StageStatus.SKIPPED:
                self.logger.info(
                    "stage_skipped",
                    stage=stage.name,
                    video_id=video.video_id
                )
                continue
            
            elif result.status == StageStatus.FAILED:
                # 執行 Stage 特定的 rollback
                try:
                    stage.rollback(context)
                except Exception as e:
                    self.logger.warning(
                        "rollback_failed",
                        stage=stage.name,
                        error=str(e)
                    )
                
                # 統一清理：刪除暫存檔（避免殘留）
                self._cleanup_on_failure(context)
                
                # 標記失敗
                self.state_manager.mark_failed(
                    video.video_id,
                    error=result.error
                )
                
                return PipelineResult.failed(
                    video.video_id,
                    stage=stage.name,
                    error=result.error
                )
            
            elif result.status == StageStatus.RETRYABLE:
                # 交由 RetryEngine 處理
                retry_result = self.retry_engine.execute(
                    lambda: self._execute_stage_raw(stage, context),
                    video_id=video.video_id,
                    stage=stage.name,
                    error=result.error
                )
                
                if not retry_result.success:
                    # 重試耗盡，統一清理
                    self._cleanup_on_failure(context)
                    
                    return PipelineResult.failed(
                        video.video_id,
                        stage=stage.name,
                        error=retry_result.error
                    )
        
        # 全部成功
        # 計算實際處理時間（從 mark_processing 到現在）
        processing_time = (
            datetime.now() - context.processing_started_at
        ).total_seconds() if context.processing_started_at else None
        
        self.state_manager.mark_completed(
            ProcessingResult(
                success=True,
                video_id=video.video_id,
                output_path=context.output_path,
                word_count=context.word_count,
                processing_time_seconds=processing_time
            )
        )
        
        return PipelineResult.success(
            video.video_id,
            output_path=context.output_path
        )
    
    def _execute_stage(
        self,
        stage: ProcessingStage,
        context: PipelineContext
    ) -> StageResult:
        """執行單個 Stage，包裝錯誤處理"""
        context.current_stage = stage.name
        context.stage_start_time = datetime.now()
        
        # 檢查是否可以跳過
        if stage.can_skip(context):
            return StageResult(
                status=StageStatus.SKIPPED,
                context_updates={}
            )
        
        try:
            result = stage.execute(context)
            return result
        
        except Exception as e:
            error = ErrorClassifier.classify(
                e,
                video_id=context.video.video_id,
                channel=context.video.channel,
                stage=stage.name
            )
            
            return StageResult(
                status=StageStatus.RETRYABLE if error.is_retryable else StageStatus.FAILED,
                context_updates={},
                error=error
            )
    
    def _cleanup_on_failure(self, context: PipelineContext) -> None:
        """
        處理失敗時的統一清理。
        
        刪除所有暫存檔案，避免殘留：
        - 音訊檔案（如果存在）
        - 部分輸出檔案（如果存在）
        """
        # 刪除音訊檔
        if context.audio_path and context.audio_path.exists():
            try:
                context.audio_path.unlink()
                self.logger.debug(
                    "cleanup_audio_on_failure",
                    path=str(context.audio_path)
                )
            except OSError as e:
                self.logger.warning(
                    "cleanup_audio_failed",
                    path=str(context.audio_path),
                    error=str(e)
                )
        
        # 刪除部分輸出檔
        if context.output_path and context.output_path.exists():
            try:
                context.output_path.unlink()
                self.logger.debug(
                    "cleanup_output_on_failure",
                    path=str(context.output_path)
                )
            except OSError as e:
                self.logger.warning(
                    "cleanup_output_failed",
                    path=str(context.output_path),
                    error=str(e)
                )
```

---

## 4. Stage 實作

### 4.1 DownloadStage

```python
class DownloadStage:
    """音訊下載 Stage"""
    
    name = "download"
    
    def __init__(
        self,
        downloader: AudioDownloader,
        max_duration: Optional[int] = None
    ):
        self.downloader = downloader
        self.max_duration = max_duration
    
    def can_skip(self, context: PipelineContext) -> bool:
        """如果音訊檔案已存在且完整，跳過下載"""
        expected_path = self._get_audio_path(context)
        if not expected_path.exists():
            return False
        
        # 檢查檔案大小（至少 10KB 才認為有效）
        return expected_path.stat().st_size > 10 * 1024
    
    def execute(self, context: PipelineContext) -> StageResult:
        video = context.video
        
        # 下載
        try:
            result = self.downloader.download(
                video_id=video.video_id,
                output_dir=context.temp_dir,
                cookies_file=context.config.cookies_file
            )
            
            # 檢查時長限制
            if self.max_duration and result.duration_seconds > self.max_duration * 60:
                return StageResult(
                    status=StageStatus.FAILED,
                    context_updates={},
                    error=ErrorInfo(
                        type=ErrorType.PERMANENT_SKIP,
                        message=f"Video too long: {result.duration_seconds // 60}min"
                    )
                )
            
            return StageResult(
                status=StageStatus.SUCCESS,
                context_updates={
                    "audio_path": result.audio_path,
                    "audio_duration": result.duration_seconds
                }
            )
        
        except DownloadError as e:
            return StageResult(
                status=StageStatus.RETRYABLE,
                context_updates={},
                error=ErrorInfo(
                    type=ErrorType.RETRYABLE_NETWORK,
                    message=str(e)
                )
            )
    
    def rollback(self, context: PipelineContext) -> None:
        """刪除部分下載的檔案"""
        if context.audio_path and context.audio_path.exists():
            context.audio_path.unlink(missing_ok=True)
    
    def _get_audio_path(self, context: PipelineContext) -> Path:
        return context.temp_dir / f"{context.video.video_id}.mp3"
```

### 4.2 TranscribeStage

```python
class TranscribeStage:
    """語音轉錄 Stage"""
    
    name = "transcribe"
    
    def __init__(
        self,
        backend: WhisperBackend,
        model: str = "medium",
        language: Optional[str] = None
    ):
        self.backend = backend
        self.model = model
        self.language = language
    
    def execute(self, context: PipelineContext) -> StageResult:
        if not context.audio_path:
            return StageResult(
                status=StageStatus.FAILED,
                context_updates={},
                error=ErrorInfo(
                    type=ErrorType.PERMANENT_FATAL,
                    message="No audio_path in context"
                )
            )
        
        try:
            result = self.backend.transcribe(
                audio_path=context.audio_path,
                language=self.language or context.config.language,
                model=self.model
            )
            
            return StageResult(
                status=StageStatus.SUCCESS,
                context_updates={
                    "transcript_text": result.text,
                    "transcript_language": result.language,
                    "word_count": len(result.text.split())
                }
            )
        
        except OutOfMemoryError as e:
            # 記憶體不足，建議換小模型重試
            return StageResult(
                status=StageStatus.RETRYABLE,
                context_updates={},
                error=ErrorInfo(
                    type=ErrorType.RETRYABLE_FALLBACK,
                    message="Out of memory, try smaller model",
                    details={"suggested_model": "small"}
                )
            )
        
        except TranscriptionError as e:
            return StageResult(
                status=StageStatus.RETRYABLE,
                context_updates={},
                error=ErrorInfo(
                    type=ErrorType.RETRYABLE_TRANSCRIPTION,
                    message=str(e)
                )
            )
```

### 4.3 SaveStage

```python
class SaveStage:
    """儲存 Markdown Stage"""
    
    name = "save"
    
    def __init__(self, formatter: Optional[MarkdownFormatter] = None):
        self.formatter = formatter or MarkdownFormatter()
    
    def execute(self, context: PipelineContext) -> StageResult:
        if not context.transcript_text:
            return StageResult(
                status=StageStatus.FAILED,
                context_updates={},
                error=ErrorInfo(
                    type=ErrorType.PERMANENT_FATAL,
                    message="No transcript_text in context"
                )
            )
        
        # 生成輸出路徑
        output_path = self._generate_output_path(context)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 格式化 Markdown
        markdown = self.formatter.format(
            video=context.video,
            transcript=context.transcript_text,
            language=context.transcript_language,
            word_count=context.word_count or 0,
            duration_seconds=context.audio_duration or 0
        )
        
        # 寫入檔案
        try:
            output_path.write_text(markdown, encoding="utf-8")
            
            return StageResult(
                status=StageStatus.SUCCESS,
                context_updates={"output_path": output_path}
            )
        
        except IOError as e:
            return StageResult(
                status=StageStatus.RETRYABLE,
                context_updates={},
                error=ErrorInfo(
                    type=ErrorType.RETRYABLE_IO,
                    message=f"Failed to write file: {e}"
                )
            )
    
    def _generate_output_path(self, context: PipelineContext) -> Path:
        """生成輸出檔案路徑"""
        video = context.video
        date_str = video.published_at.strftime("%Y-%m-%d")
        month_str = video.published_at.strftime("%Y-%m")
        title_slug = self._slugify(video.title)[:50]  # 限制長度
        
        return (
            context.output_dir /
            month_str /
            f"{date_str}_{video.video_id}_{title_slug}.md"
        )
    
    def _slugify(self, text: str) -> str:
        """將標題轉為檔案名稱安全的格式"""
        import re
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'[-\s]+', '-', text)
        return text.strip('-').lower()
```

### 4.4 CleanupStage

```python
import structlog

class CleanupStage:
    """清理暫存檔 Stage"""
    
    name = "cleanup"
    
    def __init__(self):
        self.logger = structlog.get_logger(__name__)
    
    def execute(self, context: PipelineContext) -> StageResult:
        """刪除暫存音訊檔"""
        if context.audio_path and context.audio_path.exists():
            try:
                context.audio_path.unlink()
                self.logger.debug(
                    "temp_file_deleted",
                    path=str(context.audio_path)
                )
            except OSError as e:
                # 清理失敗不影響整體結果，只記錄警告
                self.logger.warning(
                    "cleanup_failed",
                    path=str(context.audio_path),
                    error=str(e)
                )
        
        return StageResult(
            status=StageStatus.SUCCESS,
            context_updates={}
        )
```

---

## 5. Pipeline 配置與使用

### 5.1 建立預設 Pipeline

```python
def create_default_pipeline(
    config: GlobalConfig,
    state_manager: StateManager
) -> PipelineOrchestrator:
    """建立預設的處理 Pipeline"""
    
    # 建立各 Stage
    stages: List[ProcessingStage] = [
        DownloadStage(
            downloader=YTDLPAudioDownloader(),
            max_duration=config.global_settings.max_duration
        ),
        TranscribeStage(
            backend=create_whisper_backend(config.whisper),
            model=config.whisper.model,
            language=config.whisper.language
        ),
        SaveStage(),
        CleanupStage()
    ]
    
    # 建立 RetryEngine
    retry_engine = RetryEngine(
        state_manager=state_manager,
        policies=DEFAULT_RETRY_POLICIES
    )
    
    # 建立 Pipeline
    return PipelineOrchestrator(
        stages=stages,
        state_manager=state_manager,
        retry_engine=retry_engine
    )
```

### 5.2 使用範例

```python
# 初始化
config = ConfigManager().load("channels.yaml")
state_manager = StateManager(Path("state.db"))
pipeline = create_default_pipeline(config, state_manager)

# 處理影片
for channel in config.channels:
    videos = get_recent_videos(channel.url, max_videos=5)
    
    for video in videos:
        result = pipeline.process(
            video=video,
            config=channel,
            global_config=config
        )
        
        if result.success:
            print(f"✓ {video.title}")
        else:
            print(f"✗ {video.title}: {result.error}")
```

---

## 6. 擴展 Pipeline

### 6.1 新增 Stage（例如：AI 摘要）

```python
class SummarizeStage:
    """在轉錄後新增 AI 摘要"""
    
    name = "summarize"
    
    def __init__(self, ai_client: AIClient):
        self.ai_client = ai_client
    
    def execute(self, context: PipelineContext) -> StageResult:
        summary = self.ai_client.summarize(context.transcript_text)
        
        # 將摘要加入 context，供 SaveStage 使用
        return StageResult(
            status=StageStatus.SUCCESS,
            context_updates={"summary": summary}
        )

# 插入 Pipeline
stages = [
    DownloadStage(),
    TranscribeStage(),
    SummarizeStage(),  # ← 新增
    SaveStage(),       # ← 修改 SaveStage 以支援 summary
    CleanupStage()
]
```

---

## 7. 測試策略

### 7.1 Stage 單元測試

```python
def test_download_stage():
    # Arrange
    mock_downloader = MockAudioDownloader()
    stage = DownloadStage(downloader=mock_downloader)
    context = create_test_context()
    
    # Act
    result = stage.execute(context)
    
    # Assert
    assert result.status == StageStatus.SUCCESS
    assert context.audio_path is not None

def test_download_stage_rollback():
    # Arrange
    stage = DownloadStage(downloader=MockFailingDownloader())
    context = create_test_context()
    context.audio_path = Path("/tmp/test.mp3")
    context.audio_path.write_text("test")  # 建立測試檔案
    
    # Act
    stage.rollback(context)
    
    # Assert
    assert not context.audio_path.exists()
```

### 7.2 Pipeline 整合測試

```python
def test_full_pipeline():
    # Arrange
    pipeline = create_test_pipeline()
    video = VideoInfo(
        video_id="test123",
        title="Test Video",
        channel="Test Channel",
        ...
    )
    
    # Act
    result = pipeline.process(video, config, global_config)
    
    # Assert
    assert result.success
    assert result.output_path.exists()
    assert result.output_path.read_text().startswith("# Test Video")
```

---

**最後更新**: 2026-02-05  
**文件狀態**: 📝 設計階段
