# 進度追蹤與可觀測性設計

> **版本**: 2.0  
> **狀態**: 📝 設計階段  
> **最後更新**: 2026-02-05

---

## 1. 設計目標

### V1 的問題
- 「黑盒運行」：用戶不知道程式在幹嘛
- 長時間無輸出，以為當機
- 無法預估「還要等多久」
- 錯誤發生後才發現問題

### V2 的解決方案
- **實時進度條**：Rich 庫提供美觀的 TUI
- **時間預估**：基於歷史數據預測剩餘時間
- **結構化日誌**：JSON 格式，便於分析
- **多層級輸出**：詳細/簡潔模式切換

---

## 2. 進度顯示

### 2.1 顯示層級

| 層級 | 內容 | 適用場景 |
|------|------|----------|
| **Minimal** | 只顯示完成數量 | CI/CD、背景執行 |
| **Normal** | 進度條 + 當前影片 | 一般用戶 |
| **Verbose** | 詳細步驟 + 時間統計 | 除錯、開發 |

### 2.2 Normal 模式顯示範例

```
YouTube Transcriber v2.0
════════════════════════════════════════════════════════════

📺 頻道進度: 老高與小茉 [2/5]
[████████████████░░░░░░░░░░░░░░░░] 40% (8/20 影片)

🎬 當前影片: 2025預言，今年一定發生
   時長: 45:23 │ 預估剩餘: 32 分鐘

   ├─ [✓] 下載音訊     (2.5 MB/s, 12s)
   ├─ [🎙️] 轉錄中      (medium模型, 已用 18m)
   ├─ [⏳] 儲存文稿    
   └─ [⏳] 清理暫存    

⏱️  總進度: [███████░░░░░░░░░░░░░░░░░░░░░░░] 23%
   已處理: 23/100 影片 │ 已用時間: 2h 15m │ 預估剩餘: 3h 30m

════════════════════════════════════════════════════════════
按 Ctrl+C 可安全中斷（當前影片處理完成後停止）
```

### 2.3 Verbose 模式顯示範例

```
[14:32:15] INFO: Starting YouTube Transcriber v2.0
[14:32:15] INFO: Loaded config from channels.yaml
[14:32:15] INFO: Found 5 channels to process

[14:32:16] INFO: Processing channel: 老高與小茉 (2/5)
[14:32:18] INFO: Fetched 20 videos from channel
[14:32:18] INFO: 8 new videos to process

[14:32:18] INFO: [1/8] Processing: 2025預言，今年一定發生
[14:32:18] INFO:   Duration: 45:23
[14:32:18] INFO:   Stage: download
[14:32:30] INFO:   Download complete: 45.2 MB (2.5 MB/s)
[14:32:30] INFO:   Stage: transcribe
[14:32:30] INFO:   Model: medium, Language: auto-detect
[14:50:45] INFO:   Transcribe complete: 5420 words, language: zh
[14:50:45] INFO:   Stage: save
[14:50:46] INFO:   Saved to: output/老高與小茉/2026-01/2026-01-15_xxx.md
[14:50:46] INFO:   Stage: cleanup
[14:50:46] INFO:   Cleanup complete
[14:50:46] INFO: [1/8] Complete in 18m 28s

[14:50:46] INFO: [2/8] Processing: 下一個影片標題...
...
```

---

## 3. ProgressTracker 實作

### 3.1 核心類別

```python
from rich.console import Console
from rich.progress import (
    Progress, SpinnerColumn, TextColumn,
    BarColumn, TaskProgressColumn, TimeRemainingColumn
)
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from dataclasses import dataclass
from typing import Optional
from datetime import datetime, timedelta

@dataclass
class ProgressState:
    """進度狀態"""
    current_channel: str
    channel_index: int
    total_channels: int
    current_video: Optional[str]
    video_index: int
    total_videos: int
    current_stage: str
    stage_start_time: Optional[datetime]

class ProgressTracker:
    """
    進度追蹤器。
    
    使用 Rich 庫提供美觀的 CLI 界面。
    """
    
    def __init__(
        self,
        state_manager: StateManager,
        console: Optional[Console] = None,
        verbose: bool = False
    ):
        self.state_manager = state_manager
        self.console = console or Console()
        self.verbose = verbose
        
        # 統計數據
        self.start_time = datetime.now()
        self.processed_count = 0
        self.total_processing_time = 0.0
    
    def start_channel(self, channel: str, total_videos: int) -> None:
        """開始處理新頻道"""
        self.state = ProgressState(
            current_channel=channel,
            channel_index=self.state.channel_index + 1 if hasattr(self, 'state') else 1,
            total_channels=0,  # 由外部設定
            current_video=None,
            video_index=0,
            total_videos=total_videos,
            current_stage="",
            stage_start_time=None
        )
        
        if not self.verbose:
            self.console.print(f"\n[bold cyan]📺 處理頻道: {channel}[/bold cyan]")
    
    def start_video(self, video: VideoInfo) -> None:
        """開始處理新影片"""
        self.state.current_video = video.title
        self.state.video_index += 1
        self.video_start_time = datetime.now()
        
        if self.verbose:
            self.console.print(
                f"[green]處理: {video.title} [{video.duration_formatted}][/green]"
            )
    
    def update_stage(self, stage: str) -> None:
        """更新當前 Stage"""
        self.state.current_stage = stage
        self.state.stage_start_time = datetime.now()
        
        if self.verbose:
            self.console.print(f"  [dim]{stage}...[/dim]")
    
    def complete_video(self, success: bool, word_count: int = 0) -> None:
        """影片處理完成"""
        duration = (datetime.now() - self.video_start_time).total_seconds()
        self.total_processing_time += duration
        self.processed_count += 1
        
        if success:
            icon = "✓"
            color = "green"
            msg = f"完成 ({word_count} 字, {duration/60:.1f}m)"
        else:
            icon = "✗"
            color = "red"
            msg = "失敗"
        
        if self.verbose:
            self.console.print(f"  [{color}]{icon} {msg}[/{color}]")
    
    def render(self) -> str:
        """渲染進度畫面（供 Live 使用）"""
        if self.verbose:
            return ""  # Verbose 模式不使用動態畫面
        
        # 構建進度畫面
        panels = []
        
        # 頻道進度
        channel_progress = self._render_channel_progress()
        panels.append(channel_progress)
        
        # 當前影片詳情
        if self.state.current_video:
            video_detail = self._render_video_detail()
            panels.append(video_detail)
        
        # 總進度
        overall_progress = self._render_overall_progress()
        panels.append(overall_progress)
        
        return "\n".join(panels)
    
    def _render_channel_progress(self) -> Panel:
        """渲染頻道進度"""
        state = self.state
        
        # 計算頻道進度
        channel_pct = (state.video_index / state.total_videos * 100) if state.total_videos > 0 else 0
        
        # 進度條
        bar_width = 30
        filled = int(bar_width * state.video_index / state.total_videos) if state.total_videos > 0 else 0
        bar = "█" * filled + "░" * (bar_width - filled)
        
        content = f"""\
[bold cyan]📺 {state.current_channel}[/bold cyan] [{state.channel_index}/{state.total_channels}]
[{bar}] {channel_pct:.0f}% ({state.video_index}/{state.total_videos} 影片)
"""
        return Panel(content, title="頻道進度", border_style="cyan")
    
    def _render_video_detail(self) -> Panel:
        """渲染當前影片詳情"""
        state = self.state
        
        # Stage 圖示
        stages = ["下載", "轉錄", "儲存", "清理"]
        stage_icons = []
        
        for i, stage in enumerate(stages):
            if stage == state.current_stage:
                icon = "🎙️" if stage == "轉錄" else "▶️"
                stage_icons.append(f"{icon} {stage}中")
            elif i < self._get_current_stage_index():
                stage_icons.append(f"[green]✓ {stage}[/green]")
            else:
                stage_icons.append(f"[dim]○ {stage}[/dim]")
        
        content = f"""\
[bold]{state.current_video}[/bold]
{' / '.join(stage_icons)}
"""
        return Panel(content, title="當前影片", border_style="blue")
    
    def _render_overall_progress(self) -> Panel:
        """渲染總進度"""
        elapsed = (datetime.now() - self.start_time).total_seconds()
        
        # 預估剩餘時間
        if self.processed_count > 0:
            avg_time = self.total_processing_time / self.processed_count
            # 這裡簡化計算，實際應基於剩餘影片數
            remaining = avg_time * 10  # 假設還有 10 部
            eta_str = self._format_duration(remaining)
        else:
            eta_str = "計算中..."
        
        content = f"""\
已用時間: {self._format_duration(elapsed)}
預估剩餘: {eta_str}
處理速率: {self.processed_count / elapsed * 60:.1f} 部/小時
"""
        return Panel(content, title="整體統計", border_style="green")
    
    def _format_duration(self, seconds: float) -> str:
        """格式化時間長度"""
        if seconds < 60:
            return f"{seconds:.0f}秒"
        elif seconds < 3600:
            return f"{seconds/60:.0f}分鐘"
        else:
            hours = int(seconds / 3600)
            minutes = int((seconds % 3600) / 60)
            return f"{hours}小時{minutes}分鐘"
    
    def _get_current_stage_index(self) -> int:
        """獲取當前 stage 索引"""
        stages = ["下載", "轉錄", "儲存", "清理"]
        try:
            return stages.index(self.state.current_stage)
        except ValueError:
            return 0
```

### 3.2 使用方式

```python
# 基本使用
tracker = ProgressTracker(state_manager, verbose=False)

with Live(tracker.render(), refresh_per_second=4):
    for channel in channels:
        tracker.start_channel(channel.name, total_videos=len(videos))
        
        for video in videos:
            tracker.start_video(video)
            
            for stage in pipeline.stages:
                tracker.update_stage(stage.name)
                result = stage.execute(context)
            
            tracker.complete_video(success=True, word_count=1500)

# Verbose 模式
tracker = ProgressTracker(state_manager, verbose=True)
# Verbose 模式下直接 print，不使用 Live
```

---

## 4. 時間預估算法

### 4.1 單部影片預估

```python
def estimate_video_time(
    video_duration_seconds: int,
    model: str,
    historical_data: List[ProcessingRecord]
) -> timedelta:
    """
    預估單部影片處理時間。
    
    公式：
    總時間 = 下載時間 + 轉錄時間 + 其他
    
    下載時間 = 檔案大小 / 網速
    轉錄時間 = 影片時長 × 模型係數
    
    模型係數（經驗值）：
    - tiny:   1:1（1分鐘影片 = 1分鐘轉錄）
    - base:   1:2
    - small:  1:3
    - medium: 1:4
    - large:  1:8
    """
    MODEL_RATIOS = {
        "tiny": 1,
        "base": 2,
        "small": 3,
        "medium": 4,
        "large": 8
    }
    
    ratio = MODEL_RATIOS.get(model, 4)
    transcribe_seconds = video_duration_seconds * ratio
    
    # 加上下載時間（假設 5MB/min，網速 2MB/s）
    estimated_size_mb = video_duration_seconds / 60 * 5
    download_seconds = estimated_size_mb / 2
    
    # 加上緩衝（20%）
    total_seconds = (transcribe_seconds + download_seconds) * 1.2
    
    return timedelta(seconds=int(total_seconds))
```

### 4.2 整體預估

```python
def estimate_remaining_time(
    pending_videos: List[VideoInfo],
    model: str,
    history: List[ProcessingRecord]
) -> timedelta:
    """
    預估整體剩餘時間。
    """
    total_seconds = 0
    
    for video in pending_videos:
        # 檢查是否有歷史數據（相同頻道、相近時長）
        similar = find_similar_record(history, video)
        
        if similar:
            # 使用歷史平均
            total_seconds += similar.avg_processing_time
        else:
            # 使用預估
            total_seconds += estimate_video_time(
                video.duration_seconds, model, history
            ).total_seconds()
    
    return timedelta(seconds=int(total_seconds))
```

---

## 5. 日誌系統

### 5.1 結構化日誌

使用 `structlog` 生成 JSON 格式日誌：

```python
import structlog

# 配置
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.JSONRenderer()
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
)

logger = structlog.get_logger()

# 使用
logger.info(
    "video_processing_started",
    video_id="abc123",
    channel="老高與小茉",
    duration_seconds=2700,
    model="medium"
)

# 輸出
# {
#   "event": "video_processing_started",
#   "video_id": "abc123",
#   "channel": "老高與小茉",
#   "duration_seconds": 2700,
#   "model": "medium",
#   "timestamp": "2026-01-15T14:32:18.123456"
# }
```

### 5.2 日誌級別

| 級別 | 用途 | 範例 |
|------|------|------|
| DEBUG | 詳細執行資訊 | 進入函數、參數值 |
| INFO | 正常流程事件 | 開始處理影片、Stage 完成 |
| WARNING | 需要注意但可繼續 | 重試、Fallback |
| ERROR | 處理失敗 | 影片處理失敗 |
| CRITICAL | 需要終止程式 | 磁碟滿、權限問題 |

### 5.3 日誌檔案

```
logs/
├── transcriber.log          # 主日誌（JSON 格式）
├── {channel_name}_errors.log  # 頻道錯誤日誌（文字格式，便於查看）
└── summary.json             # 執行摘要
```

---

## 6. 執行摘要

### 6.1 摘要內容

```python
@dataclass
class ExecutionSummary:
    """執行摘要"""
    start_time: datetime
    end_time: datetime
    total_duration_seconds: float
    
    channels_processed: int
    videos_processed: int
    videos_success: int
    videos_failed: int
    videos_skipped: int
    
    total_words: int
    avg_processing_time: float
    
    errors: List[ErrorSummary]

@dataclass
class ErrorSummary:
    """錯誤摘要"""
    video_id: str
    channel: str
    error_type: str
    error_message: str
```

### 6.2 輸出範例

```
════════════════════════════════════════════════════════════
                      執行摘要
════════════════════════════════════════════════════════════

⏱️  執行時間: 2小時35分鐘

📊 處理統計:
   頻道數: 5
   檢查影片: 100
   新影片: 23
   ├─ ✓ 成功: 20 (87%)
   ├─ ✗ 失敗: 2 (9%)
   └─ ⊘ 跳過: 1 (4%)

📝 轉錄統計:
   總字數: 45,230
   平均每部: 2,262 字
   平均處理時間: 7m 30s

⚠️  錯誤記錄:
   [老高與小茉] video_xxx: 網路超時 (已重試3次)
   [TechLead] video_yyy: 影片不存在 (404)

════════════════════════════════════════════════════════════
```

---

## 7. 測試與驗證

### 7.1 進度顯示測試

```python
def test_progress_tracker():
    state = MockStateManager()
    console = Console(force_terminal=True, width=80)
    tracker = ProgressTracker(state, console, verbose=False)
    
    tracker.start_channel("Test Channel", 10)
    tracker.start_video(VideoInfo(
        video_id="test",
        title="Test Video",
        duration_seconds=300
    ))
    
    output = tracker.render()
    assert "Test Channel" in output
    assert "Test Video" in output
```

### 7.2 時間預估測試

```python
def test_time_estimation():
    # 5 分鐘影片，medium 模型
    estimated = estimate_video_time(300, "medium", [])
    # 預估: 5min * 4 (ratio) * 1.2 (buffer) = 24min
    assert timedelta(minutes=20) < estimated < timedelta(minutes=30)
```

---

**最後更新**: 2026-02-05  
**文件狀態**: 📝 設計階段
