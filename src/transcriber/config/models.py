"""Pydantic 配置模型."""

from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field, HttpUrl, field_validator


class OutputConfig(BaseModel):
    """輸出設定."""

    base_dir: Path = Field(default=Path("./output"), description="輸出根目錄")
    temp_dir: Path = Field(default=Path("./temp"), description="暫存檔案目錄")

    @field_validator("base_dir", "temp_dir")
    @classmethod
    def _expand_path(cls, v: Path) -> Path:
        return v.expanduser().resolve()


class WhisperConfig(BaseModel):
    """Whisper 設定."""

    backend: Literal["openai", "cpp", "faster-whisper"] = Field(
        default="openai",
        description="Whisper 實現後端",
    )
    model: str = Field(
        default="medium",
        description="Whisper 模型名稱或路徑",
    )
    language: str = Field(
        default="auto",
        description="語言代碼 (auto 表示自動偵測)",
    )
    # whisper.cpp 專屬設定
    cpp_bin: Path | None = Field(
        default=None,
        description="whisper.cpp 執行檔路徑 (例如 whisper-cli)",
    )
    model_path: Path | None = Field(
        default=None,
        description="whisper.cpp 模型檔案路徑 (.bin)",
    )

    @field_validator("language")
    @classmethod
    def _validate_language(cls, v: str) -> str:
        if v == "auto":
            return v
        # 支援的語言代碼清單 (ISO 639-1)
        supported = {
            "zh", "en", "ja", "ko", "es", "fr", "de", "it", "pt", "ru",
            "ar", "hi", "th", "vi", "id", "ms", "tr", "pl", "nl", "sv",
        }
        if v not in supported:
            raise ValueError(f"不支援的語言代碼: {v}")
        return v


class GlobalConfig(BaseModel):
    """全域處理設定."""

    max_videos_check: int = Field(
        default=5,
        ge=1,
        le=100,
        description="每個頻道檢查最新 N 部影片",
    )
    max_duration: int = Field(
        default=90,
        ge=1,
        description="最大影片長度（分鐘）",
    )
    cookies_file: Path | None = Field(
        default=None,
        description="YouTube cookies 檔案路徑（用於會員專屬內容）",
    )

    @field_validator("cookies_file")
    @classmethod
    def _validate_cookies_file(cls, v: Path | None) -> Path | None:
        if v is not None:
            v = v.expanduser().resolve()
            if not v.exists():
                raise ValueError(f"cookies 檔案不存在: {v}")
        return v


class ChannelConfig(BaseModel):
    """單一頻道設定."""

    name: str = Field(..., min_length=1, description="頻道名稱（用於輸出目錄）")
    url: str = Field(..., min_length=1, description="YouTube 頻道 URL")
    language: str | None = Field(
        default=None,
        description="語言代碼（覆寫全域設定）",
    )
    max_duration: int | None = Field(
        default=None,
        ge=1,
        description="最大影片長度（覆寫全域設定）",
    )

    @field_validator("url")
    @classmethod
    def _validate_url(cls, v: str) -> str:
        # 簡單驗證 YouTube URL 格式
        if not ("youtube.com" in v or "youtu.be" in v):
            raise ValueError(f"無效的 YouTube URL: {v}")
        return v


class Config(BaseModel):
    """完整配置模型."""

    output: OutputConfig = Field(default_factory=OutputConfig)
    whisper: WhisperConfig = Field(default_factory=WhisperConfig)
    global_config: GlobalConfig = Field(default_factory=GlobalConfig, alias="global")
    channels: list[ChannelConfig] = Field(..., min_length=1)

    model_config = {
        "populate_by_name": True,
    }
