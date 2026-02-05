# V2 開發路線圖

> **版本**: 2.0  
> **狀態**: 📝 規劃階段  
> **最後更新**: 2026-02-05

---

## 1. 開發階段總覽

```
Phase 1 (2-3 週)       Phase 2 (2 週)         Phase 3 (1-2 週)
┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│ 核心基礎設施     │   │ 功能完善        │   │ 品質保證        │
│ ─────────────── │   │ ─────────────── │   │ ─────────────── │
│ • SQLite State  │   │ • Retry Engine  │   │ • 整合測試      │
│ • Pipeline 骨架  │   │ • Progress UI   │   │ • 性能測試      │
│ • Config Mgmt   │   │ • Whisper抽象   │   │ • 文件完善      │
│ • 基本 Stages   │   │ • 錯誤處理      │   │ • 發布準備      │
└─────────────────┘   └─────────────────┘   └─────────────────┘
         │                     │                     │
         ▼                     ▼                     ▼
   ┌──────────┐          ┌──────────┐          ┌──────────┐
   │ 可執行   │          │ 可用     │          │ 可發布   │
   │ 基本流程  │          │ 生產環境  │          │ v2.0     │
   └──────────┘          └──────────┘          └──────────┘
```

---

## 2. Phase 1: 核心基礎設施（2-3 週）

### 2.1 目標
建立可執行的基本流程，能夠：
- 讀取配置並驗證
- 使用 SQLite 記錄處理狀態
- 執行完整的 Pipeline（下載→轉錄→儲存→清理）
- 基本的錯誤處理（不重試，僅記錄）

### 2.2 任務分解

#### Week 1: 專案結構與配置

| 任務 | 工時 | 驗收標準 |
|------|------|----------|
| 建立專案結構 | 4h | `pyproject.toml`, 目錄結構符合設計 |
| ConfigManager + Pydantic 模型 | 8h | 能讀取並驗證 `channels.yaml` |
| CLI 入口（Click） | 4h | `--config`, `--dry-run`, `--verbose` 參數可用 |
| 單元測試框架 | 4h | pytest 配置，首個測試通過 |

**Deliverable**: `python -m transcriber --help` 能執行

#### Week 2: SQLite State 與 Pipeline

| 任務 | 工時 | 驗收標準 |
|------|------|----------|
| StateManager + Schema | 12h | `is_processed()`, `mark_*()` 功能完整，通過測試 |
| Pipeline Orchestrator | 8h | 能依序執行多個 Stages |
| ProcessingContext | 4h | 資料能在 Stage 間傳遞 |
| Pipeline 測試 | 4h | 整合測試通過 |

**Deliverable**: 
```python
pipeline = create_pipeline(config)
result = pipeline.process(video)  # 能執行完所有 stages
```

#### Week 3: Stages 實作

| 任務 | 工時 | 驗收標準 |
|------|------|----------|
| DownloadStage | 8h | 使用 yt-dlp 成功下載音訊 |
| TranscribeStage | 8h | 使用 Whisper 成功轉錄 |
| SaveStage | 4h | 生成正確格式的 Markdown |
| CleanupStage | 2h | 成功刪除暫存檔 |
| 端到端測試 | 6h | 完整處理 1 部影片 |

**Deliverable**: 
```bash
youtube-transcriber --config channels.yaml
# 成功處理 1 個頻道的影片
```

### 2.3 Phase 1 驗收標準

- [ ] `youtube-transcriber --help` 顯示正確
- [ ] `youtube-transcriber --dry-run` 能解析配置並列出會處理的影片
- [ ] 正常執行能完整處理影片（下載→轉錄→儲存）
- [ ] 中斷後重新執行，不會重複處理已完成的影片
- [ ] 單元測試覆蓋率 > 60%

---

## 3. Phase 2: 功能完善（2 週）

### 3.1 目標
提升可用性和穩定性：
- 智能重試機制
- 美觀的進度顯示
- Whisper Backend 抽象
- 完整的錯誤處理

### 3.2 任務分解

#### Week 4: 重試與錯誤處理

| 任務 | 工時 | 驗收標準 |
|------|------|----------|
| ErrorClassifier | 6h | 能正確分類常見錯誤 |
| RetryEngine | 8h | 根據錯誤類型執行對應重試策略 |
| RetryPolicy 配置 | 4h | 5 種錯誤類別策略正確 |
| 錯誤處理測試 | 4h | 模擬各種錯誤場景 |

**Deliverable**: 網路中斷時自動重試 3 次

#### Week 5: UI 與 Backend 抽象

| 任務 | 工時 | 驗收標準 |
|------|------|----------|
| ProgressTracker (Rich) | 10h | 顯示進度條、預估時間 |
| WhisperBackend Protocol | 6h | 定義清晰接口 |
| WhisperCppBackend | 6h | 實現 whisper.cpp 支援 |
| OpenAIWhisperBackend | 4h | 實現 openai-whisper 支援 |

**Deliverable**: 
```bash
youtube-transcriber --verbose
# 看到美觀的進度顯示
```

### 3.3 Phase 2 驗收標準

- [ ] 網路錯誤自動重試 3 次
- [ ] Rate limit 自動等待後重試
- [ ] 進度顯示包含：頻道進度、影片進度、預估時間
- [ ] 可通過配置切換 Whisper backend
- [ ] 單元測試覆蓋率 > 75%

---

## 4. Phase 3: 品質保證（1-2 週）

### 4.1 目標
準備生產環境發布：
- 整合測試覆蓋主要場景
- 性能測試確保穩定性
- 文件完善

### 4.2 任務分解

#### Week 6: 測試與優化

| 任務 | 工時 | 驗收標準 |
|------|------|----------|
| 整合測試 | 8h | 覆蓋正常流程、錯誤恢復、中斷續傳 |
| 性能測試 | 6h | 處理 50 部影片不中斷 |
| 壓力測試 | 4h | 記憶體使用穩定 |
| Bug 修復 | 8h | Phase 1-2 發現的問題 |

#### Week 7: 文件與發布

| 任務 | 工時 | 驗收標準 |
|------|------|----------|
| API 文檔 | 6h | 所有 public API 有 docstring |
| 用戶指南 | 8h | README 完整，包含安裝、配置、常見問題 |
| 發布準備 | 4h | pyproject.toml 配置正確 |
| 最終測試 | 4h | 發布流程測試 |

### 4.3 Phase 3 驗收標準

- [ ] 整合測試全部通過
- [ ] 連續處理 50 部影片不中斷、不洩漏記憶體
- [ ] 用戶能根據 README 完成安裝和使用
- [ ] `pip install` 能成功安裝
- [ ] 單元測試覆蓋率 > 80%

---

## 5. 里程碑與檢查點

### Milestone 1: 基礎可執行（Phase 1 結束）
```
日期: Week 3 結束
標準:
  - 能處理單一影片的完整流程
  - 有基本的 SQLite 狀態管理
  - 有基本的錯誤記錄
演示:
  - 執行程式處理 1 個頻道
  - 展示中斷後續傳
```

### Milestone 2: 生產可用（Phase 2 結束）
```
日期: Week 5 結束
標準:
  - 智能重試機制
  - 美觀的進度顯示
  - 支援多種 Whisper backend
演示:
  - 模擬網路錯誤，展示自動重試
  - 展示進度顯示和時間預估
```

### Milestone 3: 發布準備（Phase 3 結束）
```
日期: Week 7 結束
標準:
  - 測試覆蓋率 > 80%
  - 連續處理 50 部影片穩定
  - 文件完整
演示:
  - 完整測試報告
  - 用戶使用影片
  - pip 安裝演示
```

---

## 6. 風險與緩解

| 風險 | 可能性 | 影響 | 緩解措施 |
|------|--------|------|----------|
| yt-dlp API 變更 | 中 | 高 | 鎖定版本，定期更新 |
| Whisper 模型載入問題 | 中 | 高 | 啟動時檢查，清晰錯誤訊息 |
| Rich 庫效能問題 | 低 | 中 | 提供 `--no-progress` 選項 |
| SQLite 效能瓶頸 | 低 | 中 | Phase 3 性能測試 |
| 開發進度延遲 | 中 | 中 | 每週檢查點，必要時縮減範圍 |

---

## 7. 資源需求

### 開發資源

| 角色 | 人數 | 職責 |
|------|------|------|
| 後端工程師 | 1-2 | 核心功能實作 |
| QA/測試 | 0.5 | 測試用例設計與執行 |
| 技術寫手 | 0.5 | 文件撰寫 |

### 硬體需求

| 用途 | 規格 | 說明 |
|------|------|------|
| 開發機 | 8GB+ RAM | 日常開發 |
| 測試機 | 16GB+ RAM, GPU | Whisper 性能測試 |

---

## 8. 附錄

### A. 目錄結構（預期）

```
youtube-transcriber-v2/
├── src/transcriber/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── manager.py
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── orchestrator.py
│   │   ├── stages.py
│   │   └── context.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── state.py
│   │   ├── retry.py
│   │   ├── errors.py
│   │   └── progress.py
│   ├── backends/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── whisper_cpp.py
│   │   └── openai_whisper.py
│   └── utils/
│       ├── __init__.py
│       └── logging.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── conftest.py
├── docs_v2/
├── pyproject.toml
└── README.md
```

### B. 相依套件

```toml
[project.dependencies]
python = "^3.9"
click = "^8.0"
rich = "^13.0"
structlog = "^24.0"
pydantic = "^2.0"
pyyaml = "^6.0"
yt-dlp = "^2024.0"

[project.optional-dependencies]
openai-whisper = ["openai-whisper", "torch"]
faster-whisper = ["faster-whisper"]
dev = ["pytest", "pytest-asyncio", "mypy", "ruff"]
```

---

**最後更新**: 2026-02-05  
**文件狀態**: 📝 規劃階段
