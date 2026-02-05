"""狀態管理模組測試."""

import time

import pytest

from transcriber.core.state import StateManager, VideoState, VideoStatus


class TestStateManager:
    """測試狀態管理器."""
    
    def test_init_creates_database(self, temp_dir):
        """測試初始化建立資料庫."""
        db_path = temp_dir / "test.db"
        with StateManager(db_path) as sm:
            assert db_path.exists()
    
    def test_mark_pending_and_get_state(self, state_manager):
        """測試標記等待和取得狀態."""
        state_manager.mark_pending("vid1", "Channel1", "Test Video", {"duration": 300})
        
        state = state_manager.get_state("vid1")
        assert state is not None
        assert state.video_id == "vid1"
        assert state.channel_name == "Channel1"
        assert state.title == "Test Video"
        assert state.status == VideoStatus.PENDING
    
    def test_is_processed(self, state_manager):
        """測試檢查是否已處理."""
        # 新影片未處理
        assert not state_manager.is_processed("vid1")
        
        # 標記為等待，仍不算處理
        state_manager.mark_pending("vid1", "Channel1", "Test")
        assert not state_manager.is_processed("vid1")
        
        # 標記為完成，算處理
        state_manager.mark_completed("vid1")
        assert state_manager.is_processed("vid1")
    
    def test_mark_status(self, state_manager):
        """測試更新狀態."""
        state_manager.mark_pending("vid1", "Channel1", "Test")
        state_manager.mark_status("vid1", VideoStatus.DOWNLOADING)
        
        state = state_manager.get_state("vid1")
        assert state.status == VideoStatus.DOWNLOADING
    
    def test_mark_completed(self, state_manager):
        """測試標記完成."""
        state_manager.mark_pending("vid1", "Channel1", "Test")
        state_manager.mark_completed("vid1", "/path/to/output.md")
        
        state = state_manager.get_state("vid1")
        assert state.status == VideoStatus.COMPLETED
    
    def test_mark_failed(self, state_manager):
        """測試標記失敗."""
        state_manager.mark_pending("vid1", "Channel1", "Test")
        state_manager.mark_status(
            "vid1",
            VideoStatus.FAILED,
            error_message="Network error",
            error_category="NETWORK",
        )
        
        state = state_manager.get_state("vid1")
        assert state.status == VideoStatus.FAILED
        assert state.error_message == "Network error"
        assert state.error_category == "NETWORK"
        assert state.retry_count == 1
    
    def test_get_pending_videos(self, state_manager):
        """測試取得等待影片."""
        state_manager.mark_pending("vid1", "Channel1", "Video 1")
        state_manager.mark_pending("vid2", "Channel1", "Video 2")
        state_manager.mark_pending("vid3", "Channel2", "Video 3")
        
        # 標記一個為完成
        state_manager.mark_completed("vid2")
        
        pending = state_manager.get_pending_videos()
        assert len(pending) == 2
        
        # 只取得 Channel1 的
        pending_ch1 = state_manager.get_pending_videos("Channel1")
        assert len(pending_ch1) == 1
        assert pending_ch1[0].video_id == "vid1"
    
    def test_get_stats(self, state_manager):
        """測試取得統計."""
        state_manager.mark_pending("vid1", "Channel1", "Video 1")
        state_manager.mark_pending("vid2", "Channel1", "Video 2")
        state_manager.mark_completed("vid1")
        
        stats = state_manager.get_stats()
        assert stats[VideoStatus.PENDING.value] == 1
        assert stats[VideoStatus.COMPLETED.value] == 1
    
    def test_cleanup_old_records(self, state_manager):
        """測試清理舊記錄."""
        # 建立一些完成記錄
        for i in range(5):
            state_manager.mark_pending(f"vid{i}", "Channel1", f"Video {i}")
            state_manager.mark_completed(f"vid{i}")
        
        # 模擬時間流逝（透過直接修改資料庫）
        old_time = time.time() - (10 * 24 * 3600)  # 10 天前
        conn = state_manager._get_connection()
        conn.execute(
            "UPDATE video_states SET updated_at = ?",
            (old_time,)
        )
        conn.commit()
        
        # 清理應該刪除舊記錄
        deleted = state_manager.cleanup()
        assert deleted == 5
    
    def test_skip_duplicate_pending(self, state_manager):
        """測試重複標記等待會更新."""
        state_manager.mark_pending("vid1", "Channel1", "Original")
        state_manager.mark_pending("vid1", "Channel1", "Updated", {"new": "data"})
        
        state = state_manager.get_state("vid1")
        assert state.title == "Updated"
