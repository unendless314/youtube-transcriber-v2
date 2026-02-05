"""配置模組測試."""

import pytest
from pydantic import ValidationError

from transcriber.config.models import ChannelConfig, Config, OutputConfig, WhisperConfig


class TestOutputConfig:
    """測試輸出配置."""
    
    def test_default_values(self):
        """測試預設值."""
        config = OutputConfig()
        assert config.base_dir.name == "output"
        assert config.temp_dir.name == "temp"
    
    def test_path_expansion(self):
        """測試路徑展開."""
        config = OutputConfig(base_dir="~/test_output")
        assert "~" not in str(config.base_dir)


class TestWhisperConfig:
    """測試 Whisper 配置."""
    
    def test_default_values(self):
        """測試預設值."""
        config = WhisperConfig()
        assert config.backend == "openai"
        assert config.model == "medium"
        assert config.language == "auto"
    
    def test_valid_backends(self):
        """測試有效的後端."""
        for backend in ["openai", "cpp", "faster-whisper"]:
            config = WhisperConfig(backend=backend)
            assert config.backend == backend
    
    def test_valid_models(self):
        """測試有效的模型."""
        for model in ["tiny", "base", "small", "medium", "large", "large-v3"]:
            config = WhisperConfig(model=model)
            assert config.model == model
    
    def test_valid_languages(self):
        """測試有效的語言."""
        for lang in ["zh", "en", "ja", "auto"]:
            config = WhisperConfig(language=lang)
            assert config.language == lang
    
    def test_invalid_language(self):
        """測試無效的語言."""
        with pytest.raises(ValidationError):
            WhisperConfig(language="invalid")


class TestChannelConfig:
    """測試頻道配置."""
    
    def test_valid_config(self):
        """測試有效配置."""
        config = ChannelConfig(
            name="Test Channel",
            url="https://www.youtube.com/@test",
        )
        assert config.name == "Test Channel"
        assert config.language is None
    
    def test_empty_name_raises(self):
        """測試空名稱拋出錯誤."""
        with pytest.raises(ValidationError):
            ChannelConfig(name="", url="https://www.youtube.com/@test")
    
    def test_invalid_url_raises(self):
        """測試無效 URL 拋出錯誤."""
        with pytest.raises(ValidationError):
            ChannelConfig(name="Test", url="https://invalid.com")


class TestConfig:
    """測試完整配置."""
    
    def test_minimal_config(self, sample_config_dict):
        """測試最小配置."""
        config = Config.model_validate(sample_config_dict)
        assert len(config.channels) == 1
        assert config.channels[0].name == "TestChannel"
    
    def test_empty_channels_raises(self):
        """測試空頻道列表拋出錯誤."""
        with pytest.raises(ValidationError):
            Config(channels=[])
