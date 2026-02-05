
import pytest
from pathlib import Path
from unittest.mock import Mock, MagicMock, patch

from transcriber.config.models import Config, ChannelConfig, WhisperConfig, OutputConfig
from transcriber.core.state import StateManager, VideoStatus, VideoState
from transcriber.pipeline.context import ProcessingContext
from transcriber.pipeline.stages import DownloadStage, TranscribeStage, SaveStage
from transcriber.core.errors import DownloadError

@pytest.fixture
def mock_config(tmp_path):
    config = MagicMock(spec=Config)
    config.output = OutputConfig(base_dir=tmp_path / "output", temp_dir=tmp_path / "temp")
    config.whisper = WhisperConfig(model="tiny", backend="openai", language="auto")
    config.global_config = MagicMock()
    config.global_config.cookies_file = None
    config.global_config.max_duration = 90
    config.channels = [
        ChannelConfig(name="Channel_EN", url="https://youtube.com/@en", language="en"),
        ChannelConfig(name="Channel_JA", url="https://youtube.com/@ja", language="ja"),
    ]
    return config

@pytest.fixture
def mock_state_manager():
    manager = MagicMock(spec=StateManager)
    manager.get_state.return_value = None
    return manager

class TestDownloadStage:
    def test_find_downloaded_file_strict_matching(self, mock_config, mock_state_manager, tmp_path):
        """Test that file matching is strict enough to avoid partial matches."""
        stage = DownloadStage(mock_config, mock_state_manager)
        temp_dir = mock_config.output.temp_dir
        temp_dir.mkdir(parents=True)
        
        # Create a file that partially matches the video_id "123"
        (temp_dir / "12345_long_video.mp3").touch()
        
        # This shouldn't match "123"
        assert stage._find_downloaded_file(temp_dir, "123") is None
        
        # This should match "123"
        (temp_dir / "123.mp3").touch()
        assert stage._find_downloaded_file(temp_dir, "123") == temp_dir / "123.mp3"

class TestTranscribeStage:
    @patch("transcriber.backends.base.BackendFactory")
    def test_transcribe_stage_switches_language(self, mock_factory, mock_config, mock_state_manager):
        """Test that TranscribeStage correctly switches languages for different channels."""
        # Setup mocks for backends
        mock_backend_en = MagicMock()
        mock_backend_en.transcribe.return_value.text = "Hello"
        mock_backend_en.transcribe.return_value.segments = []
        
        mock_backend_ja = MagicMock()
        mock_backend_ja.transcribe.return_value.text = "Konnichiwa"
        mock_backend_ja.transcribe.return_value.segments = []

        # Factory returns different backends based on language arg
        def create_side_effect(backend, model, language=None):
            if language == "en":
                return mock_backend_en
            elif language == "ja":
                return mock_backend_ja
            return MagicMock()
            
        mock_factory.create.side_effect = create_side_effect

        stage = TranscribeStage(mock_config, mock_state_manager)

        # Context 1: English Channel
        ctx1 = ProcessingContext(
            video_id="v1", channel_name="Channel_EN", title="English Video", url="http://y.com/1"
        )
        ctx1.audio_path = MagicMock(exists=lambda: True)
        
        stage.execute(ctx1)
        
        # Context 2: Japanese Channel
        ctx2 = ProcessingContext(
            video_id="v2", channel_name="Channel_JA", title="Japanese Video", url="http://y.com/2"
        )
        ctx2.audio_path = MagicMock(exists=lambda: True)
        
        stage.execute(ctx2)

        # Verify calls
        # We expect create to be called with "en" then "ja"
        # If the bug exists, it might be called only once or with wrong language
        calls = mock_factory.create.call_args_list
        langs_requested = [call.kwargs.get('language') for call in calls]
        
        assert "en" in langs_requested, "English backend should have been requested"
        assert "ja" in langs_requested, "Japanese backend should have been requested"
