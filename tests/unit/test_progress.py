"""進度追蹤測試 - 驗證 cached 狀態與成功率計算."""

import pytest

from transcriber.core.progress import ChannelProgress, OverallProgress


class TestChannelProgress:
    """測試頻道進度計算."""

    def test_cached_field_exists(self):
        """驗證 cached 欄位存在且可正常操作."""
        ch = ChannelProgress(name="Test")
        
        # 應該能正常設置 cached
        ch.cached = 5
        assert ch.cached == 5
        
        # 應該能累加
        ch.cached += 3
        assert ch.cached == 8

    def test_processed_includes_cached(self):
        """驗證 processed 包含 cached，讓進度條能正確前進."""
        ch = ChannelProgress(name="Test", total=10)
        
        # 設置各種狀態
        ch.completed = 2
        ch.failed = 1
        ch.skipped = 1
        ch.cached = 4
        
        # processed 應該包含所有狀態
        expected = 2 + 1 + 1 + 4  # completed + failed + skipped + cached
        assert ch.processed == expected
        assert ch.processed == 8

    def test_success_rate_excludes_cached_and_skipped(self):
        """驗證成功率只計算本次實際處理的（排除 cached 和 skipped）."""
        ch = ChannelProgress(name="Test")
        
        # 情境：5部已存在，2部成功，1部失敗，2部跳過
        ch.cached = 5
        ch.completed = 2
        ch.failed = 1
        ch.skipped = 2
        
        # 成功率 = 成功 / (成功 + 失敗) = 2/3
        assert ch.success_rate == 2 / 3

    def test_success_rate_with_no_actual_processing(self):
        """驗證沒有實際處理時成功率為 0."""
        ch = ChannelProgress(name="Test")
        
        # 只有已存在和跳過，沒有實際處理
        ch.cached = 5
        ch.skipped = 3
        
        assert ch.success_rate == 0.0

    def test_success_rate_with_only_completed(self):
        """驗證全部成功時成功率為 100%."""
        ch = ChannelProgress(name="Test")
        
        ch.completed = 5
        
        assert ch.success_rate == 1.0

    def test_pending_calculation(self):
        """驗證待處理數量計算正確."""
        ch = ChannelProgress(name="Test", total=10)
        
        ch.completed = 2
        ch.failed = 1
        ch.cached = 3
        
        # pending = total - processed = 10 - (2+1+3) = 4
        assert ch.pending == 4


class TestOverallProgress:
    """測試整體進度計算."""

    def test_total_cached_aggregation(self):
        """驗證整體已存在數量正確彙總."""
        overall = OverallProgress()
        
        # 添加兩個頻道
        overall.add_channel("ChannelA", total_videos=10)
        overall.add_channel("ChannelB", total_videos=5)
        
        # 更新狀態
        overall.update_video("ChannelA", "Video1", "cached")
        overall.update_video("ChannelA", "Video2", "cached")
        overall.update_video("ChannelB", "Video3", "cached")
        
        assert overall.total_cached == 3

    def test_mixed_status_calculation(self):
        """驗證混合狀態時各項統計正確."""
        overall = OverallProgress()
        
        overall.add_channel("TestChannel", total_videos=10)
        
        # 混合狀態：3成功、1失敗、2跳過、4已存在
        for i in range(3):
            overall.update_video("TestChannel", f"Video{i}", "completed")
        overall.update_video("TestChannel", "Failed1", "failed")
        for i in range(2):
            overall.update_video("TestChannel", f"Skipped{i}", "skipped")
        for i in range(4):
            overall.update_video("TestChannel", f"Cached{i}", "cached")
        
        ch = overall.channels["TestChannel"]
        
        # 驗證各項計數
        assert ch.completed == 3
        assert ch.failed == 1
        assert ch.skipped == 2
        assert ch.cached == 4
        assert ch.processed == 10
        
        # 驗證成功率 (3/(3+1) = 0.75)
        assert ch.success_rate == 0.75
        
        # 驗證整體彙總
        assert overall.total_completed == 3
        assert overall.total_failed == 1
        assert overall.total_skipped == 2
        assert overall.total_cached == 4

    def test_cached_status_handling(self):
        """驗證 cached 狀態能被正確識別和處理."""
        overall = OverallProgress()
        overall.add_channel("Test", total_videos=5)
        
        # 使用 cached 狀態更新
        overall.update_video("Test", "Video1", "cached")
        
        ch = overall.channels["Test"]
        assert ch.cached == 1
        assert ch.completed == 0
        assert ch.failed == 0
        assert ch.skipped == 0
