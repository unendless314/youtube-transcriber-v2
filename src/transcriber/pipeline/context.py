"""Pipeline 處理上下文."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class ProcessingContext:
    """影片處理上下文，用於在 Stage 間傳遞資料.
    
    Attributes:
        video_id: YouTube 影片 ID
        channel_name: 頻道名稱
        title: 影片標題
        url: YouTube 影片 URL
        duration: 影片長度（秒）
        published_at: 發布日期（ISO 格式）
        audio_path: 下載的音訊檔案路徑
        transcript: 轉錄結果文字
        output_path: 輸出的 Markdown 檔案路徑
        metadata: 額外元數據
        stage_results: 各 Stage 的執行結果
    """
    
    # 基本資訊
    video_id: str
    channel_name: str
    title: str
    url: str
    
    # 影片資訊
    duration: int = 0
    published_at: str = ""
    
    # 處理中產生的檔案
    audio_path: Path | None = None
    
    # 轉錄結果
    transcript: str = ""
    transcript_segments: list[dict[str, Any]] = field(default_factory=list)
    
    # 輸出
    output_path: Path | None = None
    
    # 額外資料
    metadata: dict[str, Any] = field(default_factory=dict)
    stage_results: dict[str, Any] = field(default_factory=dict)
    
    def to_metadata(self) -> dict[str, Any]:
        """轉換為可儲存的元數據."""
        return {
            "duration": self.duration,
            "published_at": self.published_at,
            "url": self.url,
        }
