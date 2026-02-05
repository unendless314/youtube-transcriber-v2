"""性能測試.

測試目標：
1. 狀態查詢效能 < 10ms (NFR-008)
2. 記憶體使用穩定
3. 長時間運行不崩潰
"""

import tempfile
import time
from pathlib import Path

import pytest

from transcriber.core.state import StateManager, VideoStatus


class TestStatePerformance:
    """狀態管理性能測試."""
    
    def test_is_processed_query_time(self):
        """測試 is_processed 查詢時間 < 10ms.
        
        NFR-008: 查詢影片是否已處理 < 10ms
        """
        with tempfile.TemporaryDirectory() as tmp:
            db_path = Path(tmp) / "perf.db"
            sm = StateManager(db_path)
            
            # 預先建立 1000 條記錄
            for i in range(1000):
                sm.mark_pending(f"vid{i:04d}", "Ch1", f"Video {i}")
                if i % 2 == 0:
                    sm.mark_completed(f"vid{i:04d}")
            
            # 測試查詢時間
            times = []
            for i in range(100):
                start = time.perf_counter()
                sm.is_processed(f"vid{i:04d}")
                elapsed = (time.perf_counter() - start) * 1000  # 轉換為毫秒
                times.append(elapsed)
            
            avg_time = sum(times) / len(times)
            max_time = max(times)
            
            print(f"\n查詢時間統計:")
            print(f"  平均: {avg_time:.3f}ms")
            print(f"  最大: {max_time:.3f}ms")
            
            # 驗證：平均時間 < 10ms
            assert avg_time < 10.0, f"平均查詢時間 {avg_time:.3f}ms 超過 10ms 限制"
            
            sm.close()
    
    def test_bulk_insert_performance(self):
        """測試批量寫入效能."""
        with tempfile.TemporaryDirectory() as tmp:
            db_path = Path(tmp) / "bulk.db"
            sm = StateManager(db_path)
            
            # 批量插入 1000 條記錄
            start = time.perf_counter()
            
            for i in range(1000):
                sm.mark_pending(f"vid{i}", "Ch1", f"Video {i}")
            
            elapsed = time.perf_counter() - start
            
            print(f"\n批量寫入 1000 條記錄: {elapsed:.3f}s")
            print(f"  平均: {elapsed/1000*1000:.3f}ms/條")
            
            # 驗證：平均 < 5ms/條
            assert elapsed / 1000 < 0.005, "寫入效能過慢"
            
            sm.close()
    
    def test_cleanup_performance(self):
        """測試清理舊記錄效能."""
        with tempfile.TemporaryDirectory() as tmp:
            db_path = Path(tmp) / "cleanup.db"
            sm = StateManager(db_path)
            
            # 建立 500 條舊記錄
            for i in range(500):
                sm.mark_pending(f"old{i}", "Ch1", f"Old Video {i}")
                sm.mark_completed(f"old{i}")
            
            # 修改時間為很久以前
            import time as time_module
            old_time = time_module.time() - (30 * 24 * 3600)
            conn = sm._get_connection()
            conn.execute("UPDATE video_states SET updated_at = ?", (old_time,))
            conn.commit()
            
            # 測試清理時間
            start = time.perf_counter()
            deleted = sm.cleanup()
            elapsed = time.perf_counter() - start
            
            print(f"\n清理 {deleted} 條舊記錄: {elapsed:.3f}s")
            
            assert deleted == 500
            assert elapsed < 1.0, "清理效能過慢"
            
            sm.close()


class TestMemoryUsage:
    """記憶體使用測試."""
    
    def test_state_manager_memory_stable(self):
        """測試 StateManager 記憶體使用穩定."""
        # 這個測試檢查基本行為，實際記憶體測試需要更專業的工具
        with tempfile.TemporaryDirectory() as tmp:
            db_path = Path(tmp) / "memory.db"
            sm = StateManager(db_path)
            
            # 建立大量記錄
            for i in range(1000):
                sm.mark_pending(f"vid{i}", f"Ch{i%10}", f"Video {i}")
                if i % 3 == 0:
                    sm.mark_completed(f"vid{i}")
            
            # 查詢多次
            for _ in range(10):
                for i in range(1000):
                    sm.get_state(f"vid{i}")
            
            # 如果記憶體管理有問題，這裡會很慢或崩潰
            stats = sm.get_stats()
            assert stats[VideoStatus.PENDING.value] == 666
            assert stats[VideoStatus.COMPLETED.value] == 334
            
            sm.close()


class TestLongRunningSimulation:
    """長時間運行模擬測試."""
    
    def test_simulate_50_videos_processing(self):
        """模擬處理 50 部影片."""
        with tempfile.TemporaryDirectory() as tmp:
            db_path = Path(tmp) / "longrun.db"
            sm = StateManager(db_path)
            
            # 模擬處理 50 部影片
            success = 0
            failed = 0
            skipped = 0
            
            for i in range(50):
                vid = f"video_{i:03d}"
                sm.mark_pending(vid, "TestChannel", f"Test Video {i}")
                
                # 模擬不同結果
                if i % 10 == 0:  # 10% 失敗
                    sm.mark_status(vid, VideoStatus.FAILED, "Network error", "NETWORK")
                    failed += 1
                elif i % 5 == 0:  # 20% 跳過（已存在）
                    # 先完成再標記為跳過
                    sm.mark_completed(vid)
                    sm.mark_pending(vid, "TestChannel", f"Test Video {i} (retry)")
                    skipped += 1
                else:  # 70% 成功
                    sm.mark_status(vid, VideoStatus.DOWNLOADING)
                    sm.mark_status(vid, VideoStatus.DOWNLOADED)
                    sm.mark_completed(vid)
                    success += 1
            
            # 驗證統計
            stats = sm.get_stats()
            assert stats[VideoStatus.COMPLETED.value] > 0
            assert stats[VideoStatus.FAILED.value] > 0
            
            print(f"\n模擬處理 50 部影片:")
            print(f"  成功: {stats[VideoStatus.COMPLETED.value]}")
            print(f"  失敗: {stats[VideoStatus.FAILED.value]}")
            print(f"  等待: {stats[VideoStatus.PENDING.value]}")
            
            sm.close()
    
    def test_database_size_growth(self):
        """測試資料庫大小增長."""
        with tempfile.TemporaryDirectory() as tmp:
            db_path = Path(tmp) / "growth.db"
            sm = StateManager(db_path)
            
            # 記錄初始大小
            initial_size = db_path.stat().st_size
            
            # 建立 1000 條記錄
            for i in range(1000):
                sm.mark_pending(f"vid{i}", "Ch1", f"Video {i}")
            
            # 記錄中間大小
            mid_size = db_path.stat().st_size
            
            # 完成所有記錄
            for i in range(1000):
                sm.mark_completed(f"vid{i}")
            
            # 記錄最終大小
            final_size = db_path.stat().st_size
            
            print(f"\n資料庫大小增長:")
            print(f"  初始: {initial_size} bytes")
            print(f"  1000 條 PENDING: {mid_size} bytes")
            print(f"  1000 條 COMPLETED: {final_size} bytes")
            print(f"  每條記錄約: {(final_size - initial_size) / 1000:.1f} bytes")
            
            # 驗證：每條記錄 < 1KB
            assert (final_size - initial_size) / 1000 < 1024, "資料庫增長過快"
            
            sm.close()
