# YouTube Transcriber V2 - AGENTS.md

> **版本**: 2.1  
> **狀態**: ✅ 核心功能已完成 / 🚀 進入內容運營開發階段  
> **最後更新**: 2026-02-06  
> **文件語言**: 繁體中文（與專案文件一致）

---

## 1. 專案概述

YouTube Transcriber V2 是一個生產環境可用的 YouTube 頻道自動轉錄工具。目前**核心下載與轉錄功能已開發完成並通過驗收**。未來的開發重心將轉向對逐字稿的二次加工。

### 1.1 核心設計原則
(保持不變...)

### 1.2 當前開發重心：內容加工流水線 (Content Factory)
本專案已進入「內容運營」階段。開發焦點為將生成的 Markdown 逐字稿轉化為多平台內容。
- **參考文檔：** `docs/CONTENT_FACTORY_PIPELINE.md`
- **設計目標：** 透過 AI 進行智能評分、摘要、並產出適合 Threads, Blog, Shorts 等平台的文案。
- **開發規範：** 內容加工功能應作為**獨立模組**開發，透過呼叫現有 output 目錄進行操作，不與核心 Pipeline 強耦合。

### 1.2 V2 相較 V1 的關鍵改進

- **SQLite 狀態管理** - 取代 JSON，斷電安全 + 自動清理舊資料
- **Pipeline 架構** - 清晰的 Stage 分離，降低 main.py 複雜度
- **精細錯誤處理** - 5 級錯誤分類，智能重試策略
- **進度可見性** - 實時進度條、剩餘時間預估
- **Whisper Backend 抽象** - 支援多種 Whisper 實現

---

## 2. 技術棧

| 類別 | 技術 | 版本 | 說明 |
|------|------|------|------|
| 語言 | Python | 3.9+ | 主語言 |
| 下載 | yt-dlp | latest | YouTube 下載 |
| 轉錄 | Whisper (openai/whisper.cpp/faster-whisper) | - | Backend 可切換 |
| 資料庫 | SQLite | 3.35+ | 內建，零配置 |
| CLI | Click | latest | 比 argparse 更易用 |
| 進度 | Rich | latest | 美觀的進度條 |
| 日誌 | structlog | latest | 結構化日誌 |
| 配置 | Pydantic | v2 | 型別安全 + 驗證 |

---

## 3. 專案結構（規劃中）

```
youtube-transcriber/
├── src/transcriber/           # 主要原始碼
│   ├── __init__.py
│   ├── __main__.py           # CLI 入口
│   ├── cli.py                # Click 命令定義
│   ├── config/               # 配置管理
│   │   ├── __init__.py
│   │   ├── models.py         # Pydantic 模型
│   │   └── manager.py        # ConfigManager
│   ├── pipeline/             # Pipeline 架構
│   │   ├── __init__.py
│   │   ├── orchestrator.py   # Pipeline 協調器
│   │   ├── stages.py         # Stage 實現
│   │   └── context.py        # PipelineContext
│   ├── core/                 # 核心基礎設施
│   │   ├── __init__.py
│   │   ├── state.py          # StateManager (SQLite)
│   │   ├── retry.py          # RetryEngine
│   │   ├── errors.py         # 錯誤分類
│   │   └── progress.py       # ProgressTracker
│   ├── backends/             # Whisper Backend 抽象
│   │   ├── __init__.py
│   │   ├── base.py           # WhisperBackend Protocol
│   │   ├── openai_whisper.py
│   │   ├── whisper_cpp.py
│   │   └── faster_whisper.py
│   └── utils/                # 工具函數
│       ├── __init__.py
│       ├── logging.py        # structlog 配置
│       └── validators.py     # 驗證工具
├── tests/                     # 測試
│   ├── unit/
│   ├── integration/
│   └── conftest.py
├── docs/                      # 設計文件（目前唯一存在）
│   ├── README.md             # 技術文件導覽
│   ├── PRD.md                # 產品需求規格書
│   ├── architecture/         # 架構設計
│   │   ├── system-design.md
│   │   ├── pipeline-design.md
│   │   └── database-schema.md
│   ├── design/               # 詳細設計
│   │   ├── error-handling.md
│   │   ├── state-management.md
│   │   └── progress-tracking.md
│   ├── implementation/       # 實施指南
│   │   └── roadmap.md
│   └── reference/            # 參考文件
│       └── glossary.md
├── channels.yaml.example      # 配置範例
├── pyproject.toml            # 專案配置（待建立）
└── README.md                 # 用戶指南（待建立）
```

---

## 4. 架構概覽

### 4.1 分層架構

```
┌─────────────────────────────────────────────────────────────┐
│                        CLI Layer                             │
│   Argument Parser │ Progress Display │ Logging               │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   Orchestration Layer                        │
│   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐ │
│   │ Download │ → │Transcribe│ → │   Save   │ → │ Cleanup  │ │
│   │  Stage   │   │  Stage   │   │  Stage   │   │  Stage   │ │
│   └──────────┘   └──────────┘   └──────────┘   └──────────┘ │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   Infrastructure Layer                       │
│   State Manager │ Retry Engine │ Metrics │ Logger            │
└─────────────────────────────────────────────────────────────┘
```

### 4.2 Pipeline 處理流程

每部影片依序通過以下 Stages：

1. **DownloadStage** - 使用 yt-dlp 下載音訊 (mp3)
2. **TranscribeStage** - 使用 Whisper 進行語音轉錄
3. **SaveStage** - 將結果儲存為 Markdown 格式
4. **CleanupStage** - 清理暫存音訊檔案

---

## 5. 開發階段與路線圖

### Phase 1: 核心基礎設施（2-3 週）
- 建立專案結構與 `pyproject.toml`
- ConfigManager + Pydantic 配置驗證
- StateManager (SQLite) 實作
- Pipeline Orchestrator 骨架
- 基本 Stages 實作

**驗收標準**: 能完整處理一部影片，中斷後不會重複處理

### Phase 2: 功能完善（2 週）
- ErrorClassifier 錯誤分類
- RetryEngine 重試機制
- ProgressTracker (Rich UI)
- WhisperBackend 抽象與多實現

**驗收標準**: 網路錯誤自動重試，有美觀進度顯示

### Phase 3: 品質保證（1-2 週）
- 整合測試覆蓋主要場景
- 性能測試（連續處理 50 部影片）
- 文件完善
- 發布準備

**驗收標準**: 測試覆蓋率 > 80%，可 pip 安裝

### Phase 4: 內容工廠流水線 (進行中)
- 實作「智能評分員」Prompt (評分與篩選)
- 實作「多維度創作」Prompt (Threads, Blog, Shorts)
- 實作「執行編輯」Prompt (品質檢核與去 AI 化)
- 建立獨立的內容加工執行腳本 (獨立模組)

---

## 6. 預期使用的建置與測試命令

```bash
# 安裝依賴（規劃中）
pip install -e ".[dev]"
# 或
uv pip install -e ".[dev]"

# 執行測試
pytest
pytest --cov=transcriber --cov-report=html

# 類型檢查
mypy src/transcriber

# 程式碼格式化與檢查
ruff check src/
ruff format src/

# 執行程式
python -m transcriber --help
python -m transcriber --config channels.yaml --dry-run
python -m transcriber --config channels.yaml
```

---

## 7. 代碼風格指南（規劃中）

- **類型提示**: 所有函數使用 Type Hints，通過 mypy 檢查
- **格式化**: 使用 ruff 進行格式化與檢查
- **文件**: 所有 public API 有 docstring（Google 風格）
- **日誌**: 使用 structlog 產生結構化 JSON 日誌
- **錯誤處理**: 使用 ErrorClassifier 統一錯誤分類

---

## 8. 測試策略（規劃中）

### 測試層級

1. **單元測試** - 測試單個函數/類別，使用 mock 隔離依賴
2. **整合測試** - 測試模組間整合（如 Pipeline 完整流程）
3. **端到端測試** - 測試完整使用場景

### 測試覆蓋率目標

- Phase 1: > 60%
- Phase 2: > 75%
- Phase 3: > 80%

### 測試檔案結構

```
tests/
├── unit/
│   ├── config/
│   ├── pipeline/
│   ├── core/
│   └── backends/
├── integration/
│   ├── test_pipeline.py
│   └── test_state_manager.py
├── e2e/
│   └── test_full_workflow.py
└── conftest.py           # 共用 fixtures
```

---

## 9. 關鍵設計決策

### 9.1 為什麼使用 SQLite 而非 JSON？

- **原子寫入**: 斷電時不會產生損壞檔案
- **索引查詢**: O(log n) 查詢速度
- **自動清理**: 使用 SQL 觸發器自動清理舊資料
- **事務支援**: 保證資料一致性

### 9.2 為什麼單線程處理？

- Whisper 已吃滿 CPU/GPU 資源，並行無收益
- 簡化設計，避免併發問題
- 單機工具，無需擴展性考量

### 9.3 錯誤分類策略

| ErrorCategory | 重試次數 | 退避策略 | 範例 |
|---------------|---------|----------|------|
| RETRYABLE_IMMEDIATE | 3 | fixed 5s | 網路斷線 |
| RETRYABLE_DELAYED | 5 | exponential 5min | Rate limit 429 |
| RETRYABLE_FALLBACK | 2 | fixed 0s | OOM 換小模型 |
| PERMANENT_SKIP | 0 | - | 影片刪除 |
| PERMANENT_FATAL | 0 | - | 磁碟滿 |

---

## 10. 配置檔格式

```yaml
# channels.yaml
output:
  base_dir: "./output"

whisper:
  backend: "cpp"  # openai, cpp, faster-whisper
  model: "medium"
  language: "auto"

global:
  max_videos_check: 5
  max_duration: 90
  cookies_file: null

channels:
  - name: "頻道名稱"
    url: "https://www.youtube.com/@channel"
    language: "zh"
    max_duration: 120
```

---

## 11. 文件導覽

### 入門必讀
1. `docs/PRD.md` - 產品需求規格書
2. `docs/architecture/system-design.md` - 整體系統架構
3. `docs/architecture/pipeline-design.md` - Pipeline 設計

### 詳細設計
- `docs/architecture/database-schema.md` - SQLite Schema 設計
- `docs/design/error-handling.md` - 錯誤處理與重試策略
- `docs/design/state-management.md` - 狀態管理與檢查點
- `docs/design/progress-tracking.md` - 進度追蹤與日誌

### 實施指南
- `docs/implementation/roadmap.md` - 開發路線圖
- `docs/reference/glossary.md` - 術語表

---

## 12. 當前狀態

✅ **核心下載與轉錄引擎已實作完成**。

### 已完成的設計與實作
- [x] 系統架構設計與 Pipeline 實作
- [x] StateManager (SQLite) 與狀態管理
- [x] 錯誤處理策略與 RetryEngine
- [x] ProgressTracker (Rich UI)
- [x] 多種 Whisper Backend 支援
- [x] CLI 介面實作

### 待實作項目 (內容加工模組)
- [ ] 智能評分與摘要模組
- [ ] 多平台創作 Prompt 範本
- [ ] 品質檢核與去 AI 化流程
- [ ] 獨立的內容加工執行腳本

---

## 13. 給 AI Agent 的開發建議

### 開始實作前
1. 仔細閱讀相關設計文件
2. 遵循已定義的接口規範
3. 先寫測試，再寫實作（TDD）

### 實作時
1. **保持簡單**: 不做過度設計
2. **類型安全**: 使用 Type Hints，通過 mypy
3. **錯誤隔離**: 單一影片失敗不影響其他影片
4. **日誌完善**: 使用 structlog 記錄關鍵事件

### 驗收時
1. 確認符合設計文件的接口規範
2. 新增對應的單元測試
3. 更新此文件中的狀態

---

**最後更新**: 2026-02-05  
**作者**: AI Agent
