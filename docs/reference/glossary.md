# 術語表 (Glossary)

> **版本**: 2.0  
> **最後更新**: 2026-02-05

---

## A

### Audio Path
音訊檔案路徑。Pipeline Context 中的欄位，指向已下載的音訊檔案位置。

---

## B

### Backend
後端實現。在 V2 中指 Whisper 的不同實現方式，如 `openai-whisper`、`whisper.cpp`、`faster-whisper`。

---

## C

### Channel
頻道。YouTube 頻道，由頻道名稱和 URL 組成，是處理的基本單位之一。

### Checkpoint
檢查點。用於記錄處理進度，在中斷後能從檢查點恢復，避免重頭開始。

### Cleanup Stage
清理階段。Pipeline 的最後一個 Stage，負責刪除暫存音訊檔案。

### CLI
Command Line Interface。命令列介面，用戶通過終端機與程式互動。

---

## D

### Download Stage
下載階段。Pipeline 的第一個 Stage，使用 yt-dlp 下載 YouTube 影片音訊。

### Dry Run
測試模式。只檢查不實際執行，用於驗證配置和預覽會處理的影片。

---

## E

### Error Category
錯誤類別。V2 將錯誤分為 5 類：RETRYABLE_IMMEDIATE、RETRYABLE_DELAYED、RETRYABLE_FALLBACK、PERMANENT_SKIP、PERMANENT_FATAL。

### Error Classifier
錯誤分類器。將 Python 例外轉換為 ErrorInfo 並分類的組件。

---

## F

### Fallback
替代方案。當主要方案失敗時的備選方案，例如 OOM 時換小模型。

---

## I

### Idempotent
冪等性。執行多次與執行一次效果相同。V2 的 Pipeline 具有冪等性，已處理的影片不會重複處理。

---

## M

### Markdown
輸出格式。轉錄結果以 Markdown 格式儲存，包含 metadata 和時間戳。

### Model
模型。Whisper 的語音識別模型，分為 tiny、base、small、medium、large 五種大小。

---

## O

### Orchestrator
協調器。Pipeline Orchestrator 負責協調各 Stage 的執行順序和錯誤處理。

---

## P

### Pending
待處理狀態。影片的初始狀態，等待被處理。

### Pipeline
處理管道。由多個 Stage 組成的處理流程，影片依次通過各 Stage 完成處理。

### Pipeline Context
管道上下文。在各 Stage 間傳遞的資料容器，包含影片資訊和中間結果。

### Progress Tracker
進度追蹤器。負責顯示處理進度和預估剩餘時間的組件。

---

## R

### Retry Engine
重試引擎。根據錯誤類型決定重試策略並執行重試的組件。

### Retry Policy
重試策略。定義特定錯誤類別的重試次數、退避策略等參數。

### Rich
Python 庫。用於在終端機顯示美觀的進度條和表格。

### Rollback
回滾。Stage 失敗時執行的清理操作，例如刪除部分下載的檔案。

---

## S

### Save Stage
儲存階段。Pipeline 的第三個 Stage，將轉錄結果儲存為 Markdown 檔案。

### Schema
資料庫結構。定義 SQLite 資料庫的表結構、索引和觸發器。

### Stage
階段。Pipeline 的基本組成單位，每個 Stage 負責單一職責（如下載、轉錄）。

### Stage Result
階段結果。Stage 執行後返回的結果，包含狀態（成功/失敗/跳過）和輸出資料。

### State Manager
狀態管理器。負責 SQLite 資料庫操作，記錄和查詢影片處理狀態。

### Structlog
Python 庫。用於生成結構化（JSON）日誌。

---

## T

### Transcribe Stage
轉錄階段。Pipeline 的第二個 Stage，使用 Whisper 將音訊轉錄為文字。

### Transcript
轉錄稿。語音轉文字的最終結果。

### Trigger
觸發器。SQLite 的資料庫物件，在特定事件（如插入）時自動執行 SQL。

---

## V

### Verbose
詳細模式。輸出更多執行資訊，便於除錯。

### Video ID
影片 ID。YouTube 影片的唯一識別碼，如 `dQw4w9WgXcQ`。

### Video Info
影片資訊。從 yt-dlp 獲取的影片 metadata，包含標題、時長、發布日期等。

---

## W

### WAL
Write-Ahead Logging。SQLite 的一種日誌模式，提供更好的並發性能。V2 不使用（單線程）。

### Whisper
OpenAI 開源的語音識別模型，用於將音訊轉錄為文字。

---

## Y

### yt-dlp
YouTube 下載工具。用於從 YouTube 下載影片和音訊的 Python 庫。

---

## 狀態值

| 狀態 | 英文 | 說明 |
|------|------|------|
| 待處理 | PENDING | 初始狀態，等待處理 |
| 處理中 | PROCESSING | 正在處理 |
| 成功 | SUCCESS | 處理成功完成 |
| 失敗 | FAILED | 處理失敗，可重試 |
| 跳過 | SKIPPED | 處理失敗，不可重試（影片問題）|

---

**最後更新**: 2026-02-05
