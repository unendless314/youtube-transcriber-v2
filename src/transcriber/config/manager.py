"""配置管理器."""

from pathlib import Path

import yaml
import structlog

from .models import Config

logger = structlog.get_logger(__name__)


class ConfigManager:
    """管理配置的載入和驗證."""

    def __init__(self, config_path: Path) -> None:
        self.config_path = config_path.resolve()
        self._config: Config | None = None

    def load(self) -> Config:
        """載入並驗證配置檔案.
        
        Returns:
            驗證後的配置物件
            
        Raises:
            FileNotFoundError: 配置檔案不存在
            yaml.YAMLError: YAML 解析錯誤
            ValueError: 配置驗證失敗
        """
        logger.info("loading_config", path=str(self.config_path))
        
        if not self.config_path.exists():
            raise FileNotFoundError(f"配置檔案不存在: {self.config_path}")
        
        with open(self.config_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        
        if data is None:
            raise ValueError("配置檔案為空")
        
        self._config = Config.model_validate(data)
        logger.info(
            "config_loaded",
            channels_count=len(self._config.channels),
            whisper_backend=self._config.whisper.backend,
            whisper_model=self._config.whisper.model,
        )
        return self._config

    def get_config(self) -> Config:
        """取得已載入的配置.
        
        Returns:
            配置物件
            
        Raises:
            RuntimeError: 配置尚未載入
        """
        if self._config is None:
            raise RuntimeError("配置尚未載入，請先呼叫 load()")
        return self._config

    @staticmethod
    def create_sample_config(path: Path) -> None:
        """建立範例配置檔案.
        
        Args:
            path: 輸出路徑
        """
        sample = """# YouTube Transcriber 配置檔範例

# 輸出設定
output:
  base_dir: "./output"
  temp_dir: "./temp"

# Whisper 設定
whisper:
  backend: "openai"  # openai, cpp, faster-whisper
  model: "medium"    # tiny, base, small, medium, large, large-v3
  language: "auto"   # auto 或語言代碼 (zh, en, ja...)

# 處理設定
global:
  max_videos_check: 5      # 每個頻道檢查最新 N 部
  max_duration: 90         # 最大影片長度（分鐘）
  cookies_file: null       # 可選的 cookies 檔案路徑

# 頻道列表
channels:
  - name: "範例頻道"
    url: "https://www.youtube.com/@example"
    language: "zh"         # 可選，覆寫全域設定
    max_duration: 120      # 可選，覆寫全域設定
"""
        path.write_text(sample, encoding="utf-8")
        logger.info("sample_config_created", path=str(path))
