"""Pytest 配置與共用 fixtures."""

import tempfile
from pathlib import Path

import pytest
import yaml

from transcriber.config.manager import ConfigManager
from transcriber.config.models import Config
from transcriber.core.state import StateManager


@pytest.fixture
def temp_dir():
    """提供臨時目錄."""
    with tempfile.TemporaryDirectory() as tmp:
        yield Path(tmp)


@pytest.fixture
def sample_config_dict():
    """提供範例配置字典."""
    return {
        "output": {
            "base_dir": "./test_output",
            "temp_dir": "./test_temp",
        },
        "whisper": {
            "backend": "openai",
            "model": "tiny",  # 測試使用小模型
            "language": "auto",
        },
        "global": {
            "max_videos_check": 3,
            "max_duration": 10,  # 測試使用短時長
            "cookies_file": None,
        },
        "channels": [
            {
                "name": "TestChannel",
                "url": "https://www.youtube.com/@test",
                "language": "zh",
            }
        ],
    }


@pytest.fixture
def config_file(temp_dir, sample_config_dict):
    """建立臨時配置文件."""
    config_path = temp_dir / "test_config.yaml"
    with open(config_path, "w", encoding="utf-8") as f:
        yaml.dump(sample_config_dict, f, allow_unicode=True)
    return config_path


@pytest.fixture
def config_manager(config_file):
    """提供 ConfigManager 實例."""
    return ConfigManager(config_file)


@pytest.fixture
def loaded_config(config_manager):
    """提供已載入的 Config."""
    return config_manager.load()


@pytest.fixture
def state_manager(temp_dir):
    """提供 StateManager 實例."""
    db_path = temp_dir / "test_state.db"
    with StateManager(db_path) as sm:
        yield sm


@pytest.fixture
def sample_video_info():
    """提供範例影片資訊."""
    return {
        "video_id": "test123",
        "channel_name": "TestChannel",
        "title": "測試影片",
        "url": "https://www.youtube.com/watch?v=test123",
        "duration": 300,
        "published_at": "20240115",
    }
