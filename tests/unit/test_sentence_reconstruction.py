"""句子重建與 SRT 解析的單元測試."""

import pytest
from unittest.mock import MagicMock

from transcriber.config.models import Config, OutputConfig, WhisperConfig
from transcriber.core.state import StateManager
from transcriber.pipeline.context import ProcessingContext
from transcriber.pipeline.stages import SaveStage


@pytest.fixture
def save_stage(tmp_path):
    config = MagicMock(spec=Config)
    config.output = OutputConfig(base_dir=tmp_path / "output", temp_dir=tmp_path / "temp")
    config.whisper = WhisperConfig(model="tiny", backend="openai", language="auto")
    config.channels = []
    state = MagicMock(spec=StateManager)
    return SaveStage(config, state)


class TestReconstructSentences:
    """SaveStage._reconstruct_sentences 的測試."""

    def test_basic_merge(self, save_stage):
        """3 個短句合併為 1 個完整句子."""
        segments = [
            {"start": 0, "end": 3, "text": "Let's go"},
            {"start": 3, "end": 6, "text": "and get an update"},
            {"start": 6, "end": 9, "text": "on stock tokens."},
        ]
        result = save_stage._reconstruct_sentences(segments)
        assert len(result) == 1
        assert result[0] == "[00:00] Let's go and get an update on stock tokens."

    def test_multiple_sentences(self, save_stage):
        """多個句子各自合併."""
        segments = [
            {"start": 0, "end": 3, "text": "Hello world."},
            {"start": 3, "end": 6, "text": "This is a test."},
            {"start": 6, "end": 9, "text": "It works"},
            {"start": 9, "end": 12, "text": "very well."},
        ]
        result = save_stage._reconstruct_sentences(segments)
        assert len(result) == 3
        assert "[00:00] Hello world." in result[0]
        assert "[00:03] This is a test." in result[1]
        assert "[00:06] It works very well." in result[2]

    def test_lowercase_continuation(self, save_stage):
        """小寫開頭的 segment 即使前句有句號也繼續合併."""
        segments = [
            {"start": 0, "end": 5, "text": "The U.S."},
            {"start": 5, "end": 10, "text": "government has been hiding this."},
            {"start": 10, "end": 15, "text": "New evidence emerged."},
        ]
        result = save_stage._reconstruct_sentences(segments)
        # "government" 是小寫，所以即使 "U.S." 有句號也不斷開
        assert len(result) == 2
        assert "The U.S. government has been hiding this." in result[0]
        assert "New evidence emerged." in result[1]

    def test_chinese_punctuation(self, save_stage):
        """中文句末標點 (。！？) 判斷."""
        segments = [
            {"start": 0, "end": 3, "text": "今天我們要討論"},
            {"start": 3, "end": 6, "text": "區塊鏈技術。"},
            {"start": 6, "end": 9, "text": "首先來看看"},
            {"start": 9, "end": 12, "text": "代幣化資產。"},
        ]
        result = save_stage._reconstruct_sentences(segments)
        assert len(result) == 2
        assert "今天我們要討論 區塊鏈技術。" in result[0]
        assert "首先來看看 代幣化資產。" in result[1]

    def test_safety_limit(self, save_stage):
        """超過安全上限 (10 segments) 強制輸出."""
        segments = [
            {"start": i, "end": i + 1, "text": f"word{i}"}
            for i in range(15)
        ]
        result = save_stage._reconstruct_sentences(segments)
        # 前 10 個被強制輸出，剩餘 5 個再輸出
        assert len(result) == 2

    def test_preserves_first_timestamp(self, save_stage):
        """合併後使用第一個 segment 的時間戳."""
        segments = [
            {"start": 124.5, "end": 126, "text": "Let's go"},
            {"start": 126, "end": 128, "text": "and talk about this."},
        ]
        result = save_stage._reconstruct_sentences(segments)
        assert result[0].startswith("[02:04]")

    def test_empty_segments(self, save_stage):
        """空 segments 列表回傳空結果."""
        result = save_stage._reconstruct_sentences([])
        assert result == []

    def test_question_mark(self, save_stage):
        """問號作為句末標點."""
        segments = [
            {"start": 0, "end": 3, "text": "What do you think"},
            {"start": 3, "end": 6, "text": "about this?"},
            {"start": 6, "end": 9, "text": "I think it's great."},
        ]
        result = save_stage._reconstruct_sentences(segments)
        assert len(result) == 2
        assert "What do you think about this?" in result[0]

    def test_quoted_ending(self, save_stage):
        """引號結尾的句子正確判斷."""
        segments = [
            {"start": 0, "end": 5, "text": 'He said "hello."'},
            {"start": 5, "end": 10, "text": "Then he left."},
        ]
        result = save_stage._reconstruct_sentences(segments)
        assert len(result) == 2


class TestIsNewSentenceStart:
    """SaveStage._is_new_sentence_start 的測試."""

    def test_uppercase(self, save_stage):
        assert save_stage._is_new_sentence_start("Hello world") is True

    def test_lowercase(self, save_stage):
        assert save_stage._is_new_sentence_start("and then") is False

    def test_quoted_uppercase(self, save_stage):
        assert save_stage._is_new_sentence_start('"Hello world"') is True

    def test_chinese(self, save_stage):
        assert save_stage._is_new_sentence_start("今天是好日子") is True

    def test_empty(self, save_stage):
        assert save_stage._is_new_sentence_start("") is False


class TestGenerateMarkdownIntegration:
    """整合測試：_generate_markdown 使用句子重建."""

    def test_output_has_merged_sentences(self, save_stage):
        context = ProcessingContext(
            video_id="test123",
            channel_name="TestChannel",
            title="Test Video",
            url="https://youtube.com/watch?v=test123",
            duration=300,
            published_at="2026-02-12",
        )
        context.transcript = "Hello world. This is a test."
        context.transcript_segments = [
            {"start": 0.0, "end": 3.0, "text": "Hello"},
            {"start": 3.0, "end": 6.0, "text": "world."},
            {"start": 6.0, "end": 9.0, "text": "This is"},
            {"start": 9.0, "end": 12.0, "text": "a test."},
        ]

        md = save_stage._generate_markdown(context)

        # 應該有合併後的句子，而非逐行短句
        assert "[00:00] Hello world." in md
        assert "[00:06] This is a test." in md
        # 不應該有未合併的短句
        lines = md.split("\n")
        content_lines = [l for l in lines if l.startswith("[")]
        assert len(content_lines) == 2
