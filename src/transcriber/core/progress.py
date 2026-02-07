"""進度顯示 - 使用 Rich 顯示美觀的進度條."""

import time
from dataclasses import dataclass, field
from typing import Callable

import structlog
from rich.console import Console
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TaskID,
    TaskProgressColumn,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)
from rich.table import Table

logger = structlog.get_logger(__name__)


@dataclass
class ChannelProgress:
    """頻道處理進度."""
    name: str
    total: int = 0
    completed: int = 0
    failed: int = 0
    skipped: int = 0
    cached: int = 0  # 已存在（之前處理過）
    current_video: str = ""
    
    @property
    def processed(self) -> int:
        # 已存在也要計入 processed，讓進度條能正確前進
        return self.completed + self.failed + self.skipped + self.cached
    
    @property
    def pending(self) -> int:
        return self.total - self.processed
    
    @property
    def success_rate(self) -> float:
        # 成功率只計算本次實際處理的（排除已存在和跳過）
        actual_processed = self.completed + self.failed
        if actual_processed == 0:
            return 0.0
        return self.completed / actual_processed


@dataclass
class OverallProgress:
    """整體處理進度."""
    total_channels: int = 0
    current_channel_idx: int = 0
    channels: dict[str, ChannelProgress] = field(default_factory=dict)
    start_time: float = field(default_factory=time.time)
    
    def add_channel(self, name: str, total_videos: int) -> None:
        """添加頻道."""
        self.channels[name] = ChannelProgress(name=name, total=total_videos)
    
    def update_video(
        self,
        channel_name: str,
        video_title: str,
        status: str,  # "completed", "failed", "skipped", "cached"
    ) -> None:
        """更新影片狀態. 狀態值: completed(成功), failed(失敗), skipped(跳過), cached(已存在)"""
        if channel_name not in self.channels:
            return
        
        ch = self.channels[channel_name]
        ch.current_video = video_title
        
        if status == "completed":
            ch.completed += 1
        elif status == "failed":
            ch.failed += 1
        elif status == "skipped":
            ch.skipped += 1
        elif status == "cached":
            ch.cached += 1
    
    @property
    def total_videos(self) -> int:
        return sum(ch.total for ch in self.channels.values())
    
    @property
    def total_processed(self) -> int:
        return sum(ch.processed for ch in self.channels.values())
    
    @property
    def total_completed(self) -> int:
        return sum(ch.completed for ch in self.channels.values())
    
    @property
    def total_failed(self) -> int:
        return sum(ch.failed for ch in self.channels.values())
    
    @property
    def total_skipped(self) -> int:
        return sum(ch.skipped for ch in self.channels.values())
    
    @property
    def total_cached(self) -> int:
        return sum(ch.cached for ch in self.channels.values())
    
    @property
    def overall_progress(self) -> float:
        if self.total_videos == 0:
            return 0.0
        return self.total_processed / self.total_videos
    
    @property
    def elapsed_time(self) -> float:
        return time.time() - self.start_time
    
    @property
    def estimated_remaining(self) -> float:
        """預估剩餘時間（秒）."""
        if self.total_processed == 0:
            return 0.0
        
        avg_time_per_video = self.elapsed_time / self.total_processed
        remaining_videos = self.total_videos - self.total_processed
        return avg_time_per_video * remaining_videos


class ProgressTracker:
    """進度追蹤器 - 管理 Rich 進度顯示."""
    
    def __init__(self, console: Console | None = None) -> None:
        """初始化進度追蹤器.
        
        Args:
            console: Rich Console 實例，若為 None 創建新的
        """
        self.console = console or Console()
        self.progress: Progress | None = None
        self.overall_task: TaskID | None = None
        self.channel_task: TaskID | None = None
        self._overall = OverallProgress()
        self._current_channel: str = ""
        self._enabled = True
    
    def enable(self) -> None:
        """啟用進度顯示."""
        self._enabled = True
    
    def disable(self) -> None:
        """停用進度顯示（例如輸出到檔案時）."""
        self._enabled = False
    
    def __enter__(self) -> "ProgressTracker":
        """進入上下文，啟動進度顯示."""
        if not self._enabled:
            return self
        
        self.progress = Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]{task.description}"),
            BarColumn(bar_width=40),
            TaskProgressColumn(),
            "•",
            TimeElapsedColumn(),
            "•",
            TimeRemainingColumn(),
            console=self.console,
            transient=True,
        )
        self.progress.start()
        
        # 創建整體進度任務
        self.overall_task = self.progress.add_task(
            "[cyan]整體進度",
            total=100,
            completed=0,
        )
        
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """退出上下文，停止進度顯示."""
        if self.progress:
            self.progress.stop()
            self.progress = None
    
    def start_channels(self, channels: list[tuple[str, int]]) -> None:
        """開始處理多個頻道.
        
        Args:
            channels: [(頻道名稱, 影片數量), ...]
        """
        self._overall.total_channels = len(channels)
        
        for name, count in channels:
            self._overall.add_channel(name, count)
        
        if self.progress and self.overall_task is not None:
            self.progress.update(
                self.overall_task,
                total=self._overall.total_videos,
                completed=0,
                description=f"[cyan]整體進度 (0/{len(channels)} 頻道)",
            )
    
    def start_channel(self, channel_name: str) -> None:
        """開始處理單個頻道.
        
        Args:
            channel_name: 頻道名稱
        """
        self._current_channel = channel_name
        self._overall.current_channel_idx += 1
        
        ch = self._overall.channels.get(channel_name)
        if not ch:
            return
        
        if self.progress:
            # 更新或創建頻道任務
            if self.channel_task is not None:
                self.progress.remove_task(self.channel_task)
            
            self.channel_task = self.progress.add_task(
                f"[green]{channel_name}",
                total=ch.total,
                completed=0,
            )
    
    def update_video(
        self,
        video_title: str,
        status: str,
        message: str = "",
    ) -> None:
        """更新當前影片狀態.
        
        Args:
            video_title: 影片標題
            status: 狀態（"processing", "completed", "failed", "skipped", "cached"）
                  - processing: 處理中
                  - completed: 成功完成
                  - failed: 處理失敗
                  - skipped: 跳過（會員專屬/私人影片等）
                  - cached: 已存在（之前已處理過）
            message: 額外訊息
        """
        self._overall.update_video(self._current_channel, video_title, status)
        
        if not self.progress:
            return
        
        ch = self._overall.channels.get(self._current_channel)
        if not ch:
            return
        
        # 更新頻道進度
        if self.channel_task is not None:
            self.progress.update(
                self.channel_task,
                completed=ch.processed,
                description=f"[green]{self._current_channel} ({ch.processed}/{ch.total})",
            )
        
        # 更新整體進度
        if self.overall_task is not None:
            total_ch = self._overall.total_channels
            current_ch = self._overall.current_channel_idx
            self.progress.update(
                self.overall_task,
                completed=self._overall.total_processed,
                description=f"[cyan]整體進度 ({current_ch}/{total_ch} 頻道)",
            )
    
    def print_summary(self) -> None:
        """列印處理摘要."""
        if not self._enabled:
            return
        
        # 創建摘要表格
        table = Table(title="處理摘要")
        table.add_column("頻道", style="cyan")
        table.add_column("總數", justify="right")
        table.add_column("成功", justify="right", style="green")
        table.add_column("失敗", justify="right", style="red")
        table.add_column("已存在", justify="right", style="dim")
        table.add_column("跳過", justify="right", style="yellow")
        table.add_column("成功率", justify="right")
        
        for ch in self._overall.channels.values():
            table.add_row(
                ch.name,
                str(ch.total),
                str(ch.completed),
                str(ch.failed),
                str(ch.cached),
                str(ch.skipped),
                f"{ch.success_rate:.1%}",
            )
        
        # 總計行
        actual_total_processed = self._overall.total_completed + self._overall.total_failed
        overall_success_rate = (
            self._overall.total_completed / actual_total_processed
            if actual_total_processed > 0 else 0.0
        )
        table.add_row(
            "[bold]總計",
            str(self._overall.total_videos),
            str(self._overall.total_completed),
            str(self._overall.total_failed),
            str(self._overall.total_cached),
            str(self._overall.total_skipped),
            f"{overall_success_rate:.1%}",
            style="bold",
        )
        
        self.console.print()
        self.console.print(table)
        
        # 時間統計
        elapsed = self._overall.elapsed_time
        remaining = self._overall.estimated_remaining
        
        time_table = Table(show_header=False)
        time_table.add_row("耗時:", self._format_duration(elapsed))
        if remaining > 0:
            time_table.add_row("預估剩餘:", self._format_duration(remaining))
        
        self.console.print(time_table)
    
    def _format_duration(self, seconds: float) -> str:
        """格式化時間為易讀格式."""
        if seconds < 60:
            return f"{seconds:.0f} 秒"
        elif seconds < 3600:
            return f"{seconds/60:.1f} 分鐘"
        else:
            return f"{seconds/3600:.1f} 小時"
    
    def print_error(self, message: str) -> None:
        """列印錯誤訊息."""
        if self._enabled:
            self.console.print(f"[red]❌ {message}[/red]")
    
    def print_success(self, message: str) -> None:
        """列印成功訊息."""
        if self._enabled:
            self.console.print(f"[green]✅ {message}[/green]")
    
    def print_info(self, message: str) -> None:
        """列印資訊訊息."""
        if self._enabled:
            self.console.print(f"[blue]ℹ️ {message}[/blue]")
