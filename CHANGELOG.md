# Changelog

所有版本更新記錄。

格式基於 [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)，
版本號遵循 [Semantic Versioning](https://semver.org/lang/zh-TW/)。

## [2.0.0] - 2026-02-XX

### 🎉 新增

- **斷點續傳** - SQLite 狀態管理，中斷後自動從上次進度繼續
- **智能重試** - 5 種錯誤類型對應不同重試策略（指數退避 + 抖動）
- **進度顯示** - Rich 進度條，頻道級和影片級雙層顯示，時間預估
- **錯誤隔離** - 單一影片失敗不影響其他影片繼續處理
- **多後端支援** - BackendFactory 支援 OpenAI Whisper（whisper.cpp / faster-whisper 預留）
- **Markdown 輸出** - 包含時間戳記的結構化輸出
- **配置驗證** - Pydantic v2 模型，啟動時驗證配置
- **自動清理** - 自動清理 7 天或 100 筆舊記錄

### 🔧 技術改進

- 模組化架構：config/core/pipeline/backends 分層
- 完整 Type Hints，通過 mypy 檢查
- 結構化日誌（structlog）
- 單元測試 + 整合測試覆蓋

### ⚠️ 不相容變更

- 從 V1 完全重寫，不向下相容
- 配置格式從 JSON 改為 YAML
- 狀態儲存從 JSON 檔案改為 SQLite 資料庫

---

## [1.0.0] - 2025-XX-XX (V1 歷史版本)

V1 為基礎實作版本，V2 為生產環境重寫版本。
