# 自動化任務掛起問題分析與解決方案 (2026-02-08)

## 1. 問題描述
**現象**：
- 每日排程的自動化任務於 `03:00` 準時啟動，但在日誌中顯示長時間無動作。
- 直到早上使用者解鎖電腦並處理螢幕彈窗後，任務才繼續執行。
- 觀察到轉錄檔案（Markdown）的建立時間延遲至 `10:08` 之後。

**證據**：
- **日誌時間戳**：任務啟動於 03:00，但第一份產出檔案建立於 10:08。
- **系統彈窗**：使用者目擊 macOS 系統彈窗，提示 `Python 想要存取文件` 或 `git-credential-osxkeychain` 請求權限。
- **行程狀態**：`yt-dlp` 程序在背景處於 `Suspend`（暫停）狀態等待使用者輸入。

## 2. 根本原因分析 (Root Cause)

本次自動化任務「卡死」的主因是 **macOS 的安全性機制 (TCC / Gatekeeper)** 與 **程式呼叫架構** 的衝突。

### 架構衝突流程：
1.  **啟動層**：`auto_run.sh` 啟動專案的 Python 3.13（我們稱之為 **Process A**）。
    - *狀態*：使用者已授權 Process A 存取磁碟（Terminal/iTerm 繼承權限）。
2.  **執行層**：Process A 透過 `subprocess` 指令呼叫外部工具 `/opt/homebrew/bin/yt-dlp`。
3.  **外部依賴層**：Homebrew 的 `yt-dlp` 實際上是一個 script，它會啟動自己內建的 Python 直譯器（例如 Python 3.14，稱之為 **Process B**）。
4.  **系統攔截**：
    - Process B 嘗試寫入暫存檔。
    - macOS 檢測到 Process B 是一個 **未經簽署 (adhoc signature) 或陌生的執行檔**。
    - macOS 認為 Process B 與已授權的 Process A 是不同的實體。
    - **結果**：系統暫停 Process B，跳出權限請求視窗，導致自動化任務無限期等待。

### 為什麼升級 Python 無效？
Homebrew 安裝的工具通常綑綁了自己的 Python 環境（位於 `/opt/homebrew/Cellar/.../libexec`），這與使用者自行安裝或專案使用的 Python 環境（Process A）是完全隔離的。升級使用者的 Python 版本無法改變 Homebrew 工具內部的簽章狀態或權限繼承關係。

## 3. 建議解決方案

為了徹底解決權限彈窗問題，建議**移除對外部 binary 的依賴，改用 Python 原生呼叫**。

### 實作步驟：

1.  **安裝依賴**：
    在專案環境中直接安裝 `yt-dlp` 套件：
    ```bash
    pip install yt-dlp
    ```

2.  **重構程式碼 (`src/transcriber/pipeline/stages.py`)**：
    將原本使用 `subprocess.run` 呼叫外部指令的邏輯：
    ```python
    # 舊方式：易觸發權限問題
    subprocess.run(["yt-dlp", "--output", ...])
    ```
    改為使用 Python 函式庫直接執行：
    ```python
    # 新方式：繼承主程式權限，無彈窗
    import yt_dlp

    ydl_opts = {
        'outtmpl': '...',
        'format': 'bestaudio/best',
        # ...其他設定
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    ```

### 優點：
- **權限繼承**：下載動作由主程式（Process A）直接執行，由於 Process A 已獲得授權，系統不會再跳出彈窗。
- **環境一致性**：不再受 Homebrew 版本更新或路徑變更影響。
- **日誌控管**：可以直接在 Python 內捕獲下載進度與錯誤，無需解析標準輸出 (stdout)。

## 4. 結論
目前的權限允許可能僅是暫時性的（受限於 adhoc 簽章的不穩定性）。建議在本次轉錄任務完成並提交後，擇期執行上述的代碼重構，以確保無人值守自動化的穩定性。
