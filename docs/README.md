# YouTube Transcriber V2 - 技術文檔

> **版本**: 2.0  
> **狀態**: 📝 設計階段  
> **最後更新**: 2026-02-05

---

## 📚 文檔導覽

### 入門文檔
| 文檔 | 說明 | 適合讀者 |
|------|------|----------|
| [PRD.md](./PRD.md) | 產品需求規格書 - 功能需求與非功能需求 | 全體 |
| [Glossary](./reference/glossary.md) | 術語表 | 全體 |

### 架構設計
| 文檔 | 說明 |
|------|------|
| [System Design](./architecture/system-design.md) | 整體系統架構、模組劃分、資料流向 |
| [Pipeline Design](./architecture/pipeline-design.md) | Stage-based 處理流程設計 |
| [Database Schema](./architecture/database-schema.md) | SQLite Schema 設計與說明 |

### 詳細設計
| 文檔 | 說明 |
|------|------|
| [Error Handling](./design/error-handling.md) | 錯誤分類、重試策略、熔斷機制 |
| [State Management](./design/state-management.md) | 狀態管理、檢查點機制、清理策略 |
| [Progress Tracking](./design/progress-tracking.md) | 進度顯示、時間預估、日誌系統 |

### 實施指南
| 文檔 | 說明 |
|------|------|
| [Roadmap](./implementation/roadmap.md) | 開發階段、Milestone、驗收標準 |

---

## 🎯 V2 核心目標

### 設計原則
1. **Reliability First** - 斷電不丟失進度是最高優先級
2. **Simplicity** - 不做過度設計，單線程序列處理
3. **Observable** - 用戶隨時知道「現在在幹嘛」「還要等多久」
4. **Maintainable** - 模組化、可測試、文檔完整

### 關鍵改進（相較 V1）
- ✅ **SQLite 狀態管理** - 取代 JSON，斷電安全 + 自動清理舊資料
- ✅ **Pipeline 架構** - 清晰的 Stage 分離，降低 main.py 複雜度
- ✅ **精細錯誤處理** - 5 級錯誤分類，智能重試策略
- ✅ **進度可見性** - 實時進度條、剩餘時間預估
- ✅ **Whisper Backend 抽象** - 支援多種 Whisper 實現

---

## 🏗️ 系統概覽

```
┌─────────────────────────────────────────────────────────────────┐
│                         CLI Layer                                │
│     Argument Parser │ Progress Display │ Logging                 │
└─────────────────────────────────────────────────────────────────┘
                                │
┌─────────────────────────────────────────────────────────────────┐
│                     Pipeline Orchestrator                        │
│   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐    │
│   │ Download │ → │Transcribe│ → │   Save   │ → │ Cleanup  │    │
│   │  Stage   │   │  Stage   │   │  Stage   │   │  Stage   │    │
│   └──────────┘   └──────────┘   └──────────┘   └──────────┘    │
└─────────────────────────────────────────────────────────────────┘
                                │
┌─────────────────────────────────────────────────────────────────┐
│                    Infrastructure Layer                          │
│   SQLite State Manager │ Retry Engine │ Metrics │ Logger        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📋 快速參考

### 核心資料流

```
1. 讀取 channels.yaml
2. 對每個頻道：
   a. 獲取最新 N 部影片（yt-dlp）
   b. 查詢 SQLite：哪些已處理？
   c. 對每部新影片：
      i.   下載音訊
      ii.  轉錄（Whisper）
      iii. 儲存 Markdown
      iv.  清理暫存檔
      v.   更新狀態（SQLite）
3. 輸出執行摘要
```

### 狀態機

```
                    ┌─────────────┐
         ┌─────────►│   pending   │◄────────┐
         │          └──────┬──────┘         │
         │                 │ 開始處理        │ 重置/重試
         │                 ▼                │
    成功/跳過        ┌─────────────┐         │
         │          │  processing │         │
         │          └──────┬──────┘         │
         │                 │                │
         │      ┌─────────┼─────────┐       │
         │      │         │         │       │
         │      ▼         ▼         ▼       │
         │  ┌────────┐ ┌────────┐ ┌──────┐ │
         └──┤ success│ │ failed │ │skipped├─┘
            └────────┘ └────────┘ └──────┘
```

---

## 🔧 技術棧

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

## 📖 給開發者的話

### 閱讀順序建議

**如果你是架構師/資深工程師：**
1. PRD.md - 了解需求
2. architecture/system-design.md - 理解整體架構
3. architecture/pipeline-design.md - 理解核心流程

**如果你要實作具體功能：**
1. 先看對應模組的設計文檔
2. 參考 V1 的實作（`src/youtube_transcriber/`）
3. 遵循 Roadmap 的階段規劃

### V1 → V2 遷移注意事項

- V1 的 `processed_ids.json` 在 V2 首次啟動時可選遷移至 SQLite
- V1 的模組劃分可參考，但內部實現需重寫
- 保持錯誤隔離原則：單一影片失敗不影響其他影片

---

## 📝 文檔維護

| 日期 | 變更 | 作者 |
|------|------|------|
| 2026-02-05 | 初始建立 V2 技術文檔集 | AI Agent |
| 2026-02-06 | 新增內容篩選過濾設計文件 | AI Agent |

---

**提示**: 本文檔集為工程師實作導向，所有設計決策都應在具體實作前經過技術 Review。
