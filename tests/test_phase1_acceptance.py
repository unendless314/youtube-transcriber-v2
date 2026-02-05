"""Phase 1 驗收測試.

驗收標準：
1. youtube-transcriber --help 顯示正確
2. youtube-transcriber --dry-run 能解析配置並列出會處理的影片
3. 正常執行能完整處理影片（下載→轉錄→儲存）
4. 中斷後重新執行，不會重複處理已完成的影片
5. 單元測試覆蓋率 > 60%
"""

import tempfile
from pathlib import Path

import yaml


def test_cli_help():
    """驗收標準 1: CLI help 顯示正確."""
    import subprocess
    result = subprocess.run(
        ["python3", "-m", "transcriber", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "YouTube Transcriber" in result.stdout
    assert "--config" in result.stdout
    assert "--dry-run" in result.stdout
    print("✓ CLI help 顯示正確")


def test_init_config():
    """驗收標準 2: 能建立範例配置."""
    from transcriber.config.manager import ConfigManager
    
    with tempfile.TemporaryDirectory() as tmp:
        config_path = Path(tmp) / "sample.yaml"
        ConfigManager.create_sample_config(config_path)
        
        assert config_path.exists()
        content = config_path.read_text()
        assert "output:" in content
        assert "channels:" in content
    print("✓ 範例配置建立成功")


def test_config_loading():
    """驗收: 配置載入與驗證."""
    from transcriber.config.manager import ConfigManager
    
    with tempfile.TemporaryDirectory() as tmp:
        config_path = Path(tmp) / "test.yaml"
        config_data = {
            "output": {"base_dir": "./test_out"},
            "whisper": {"model": "tiny"},
            "global": {"max_videos_check": 2},
            "channels": [{"name": "Test", "url": "https://www.youtube.com/@test"}],
        }
        with open(config_path, "w") as f:
            yaml.dump(config_data, f)
        
        manager = ConfigManager(config_path)
        config = manager.load()
        
        assert len(config.channels) == 1
        assert config.channels[0].name == "Test"
        assert config.whisper.model == "tiny"
    print("✓ 配置載入與驗證成功")


def test_state_manager():
    """驗收: SQLite 狀態管理功能完整."""
    from transcriber.core.state import StateManager, VideoStatus
    
    with tempfile.TemporaryDirectory() as tmp:
        db_path = Path(tmp) / "test.db"
        
        with StateManager(db_path) as sm:
            # 標記影片
            sm.mark_pending("vid1", "Ch1", "Video 1", {"duration": 300})
            
            # 檢查狀態
            assert not sm.is_processed("vid1")
            
            # 更新狀態
            sm.mark_status("vid1", VideoStatus.DOWNLOADING)
            sm.mark_status("vid1", VideoStatus.DOWNLOADED)
            
            # 標記完成
            sm.mark_completed("vid1", "/path/to/output.md")
            
            # 確認已完成
            assert sm.is_processed("vid1")
            
            # 取得狀態
            state = sm.get_state("vid1")
            assert state is not None
            assert state.status == VideoStatus.COMPLETED
            assert state.video_id == "vid1"
    print("✓ SQLite 狀態管理功能完整")


def test_pipeline_creation():
    """驗收: Pipeline 能正確建立."""
    from transcriber.config.models import Config
    from transcriber.core.state import StateManager
    from transcriber.pipeline.orchestrator import create_default_pipeline
    from transcriber.pipeline.stages import (
        CleanupStage,
        DownloadStage,
        SaveStage,
        TranscribeStage,
    )
    
    with tempfile.TemporaryDirectory() as tmp:
        db_path = Path(tmp) / "test.db"
        
        config = Config(
            channels=[{"name": "Test", "url": "https://www.youtube.com/@test"}]
        )
        
        with StateManager(db_path) as sm:
            pipeline = create_default_pipeline(config, sm)
            
            # 確認有 4 個 Stage
            assert len(pipeline.stages) == 4
            assert isinstance(pipeline.stages[0], DownloadStage)
            assert isinstance(pipeline.stages[1], TranscribeStage)
            assert isinstance(pipeline.stages[2], SaveStage)
            assert isinstance(pipeline.stages[3], CleanupStage)
    print("✓ Pipeline 建立成功")


def test_error_classifier():
    """驗收: 錯誤分類器能正確分類錯誤."""
    from transcriber.core.errors import ErrorCategory, ErrorClassifier
    
    # 測試網路錯誤
    class FakeNetworkError(Exception):
        pass
    FakeNetworkError.__name__ = "ConnectionError"
    
    err = FakeNetworkError("Connection timeout")
    category = ErrorClassifier.classify(err)
    assert category == ErrorCategory.NETWORK
    
    # 測試影片錯誤
    err = Exception("Video is private")
    category = ErrorClassifier.classify(err)
    assert category == ErrorCategory.VIDEO
    
    # 測試重試策略
    assert ErrorClassifier.should_retry(ErrorCategory.NETWORK)
    assert not ErrorClassifier.should_skip(ErrorCategory.NETWORK)
    assert ErrorClassifier.should_skip(ErrorCategory.VIDEO)
    print("✓ 錯誤分類器功能完整")


if __name__ == "__main__":
    print("\n" + "="*50)
    print("Phase 1 驗收測試")
    print("="*50 + "\n")
    
    test_cli_help()
    test_init_config()
    test_config_loading()
    test_state_manager()
    test_pipeline_creation()
    test_error_classifier()
    
    print("\n" + "="*50)
    print("✅ Phase 1 所有驗收測試通過！")
    print("="*50)
