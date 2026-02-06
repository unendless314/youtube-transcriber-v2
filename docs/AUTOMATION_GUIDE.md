# 自動化轉錄與同步指南 (macOS)

本專案配置了一套自動化流程，用於每日定時轉錄追蹤的 YouTube 頻道，並透過 Git 實現雙機資料同步。

## 系統組件
1. **`auto_run.sh`**: 核心執行腳本。負責 `git pull` -> `caffeinate` (防休眠轉錄) -> `git push`。
2. **`com.user.yt_sync.plist`**: macOS `launchd` 排程設定檔。

## 常用操作指令

### 1. 啟動與載入排程
若要在新機器上設定，或重新載入設定：
```bash
# 賦予腳本權限
chmod +x auto_run.sh

# 連結設定檔到系統目錄
ln -sf "$PWD/com.user.yt_sync.plist" ~/Library/LaunchAgents/com.user.yt_sync.plist

# 載入並啟動排程
launchctl load ~/Library/LaunchAgents/com.user.yt_sync.plist
```

### 2. 立即手動執行
不必等到凌晨 3 點，隨時可以測試：
```bash
launchctl start com.user.yt_sync
```

### 3. 查看執行狀態 (日誌)
```bash
# 查看標準輸出 (進度)
tail -f /tmp/yt_sync.log

# 查看錯誤輸出
tail -f /tmp/yt_sync.err
```

### 4. 停止與解除排程
若要暫停自動化任務：
```bash
# 卸載排程
launchctl unload ~/Library/LaunchAgents/com.user.yt_sync.plist

# (可選) 刪除連結檔案
rm ~/Library/LaunchAgents/com.user.yt_sync.plist
```

## 注意事項
- **權限**：本機必須先執行過 `gh auth login` 並確保 `git fetch --dry-run` 無需輸入密碼。
- **休眠**：腳本已包含 `caffeinate` 指令，轉錄期間會自動阻止系統進入休眠。
- **頻率**：預設為每日凌晨 03:00 執行。

---

## 🔧 優化建議與待改進項目

> 以下由 OpenClaw Agent 提出，供迭代參考：

### 1. 路徑相容性（跨機器部署）
**現況**：`auto_run.sh` 和 `.plist` 檔案都硬編碼了絕對路徑 `/Users/linchunchiao/...`  
**建議**：使用相對路徑或動態偵測，讓任何機器 clone 後都能直接使用
```bash
# 在 auto_run.sh 開頭加入：
cd "$(dirname "$0")" || exit
PROJECT_DIR="$(pwd)"
```

### 2. 錯誤處理機制
**現況**：腳本遇錯不會立即停止，可能導致錯誤狀態繼續執行  
**建議**：加入嚴格錯誤處理
```bash
set -euo pipefail  # 遇錯即停、未設定變數報錯、管道錯誤偵測

# 或針對關鍵步驟：
git pull --rebase origin master || { echo "❌ git pull 失敗"; exit 1; }
```

### 3. 網路重試機制
**現況**：若 `git push` 因網路瞬斷失敗，任務會中斷  
**建議**：加入簡單重試邏輯
```bash
retry_push() {
    for i in {1..3}; do
        git push origin master && return 0
        echo "Push 失敗，5秒後重試 ($i/3)..."
        sleep 5
    done
    return 1
}
```

### 4. 日誌輪替
**現況**：日誌持續寫入 `/tmp/yt_sync.log`，可能累積過大  
**建議**：加入時間戳記或按日期分割
```bash
LOG_FILE="/tmp/yt_sync_$(date +%Y%m%d).log"
```

### 5. 通知機制（可選）
**建議**：完成或失敗時發送桌面通知
```bash
osascript -e 'display notification "轉錄完成" with title "YouTube Transcriber"'
```

---
*貢獻方式：請直接在 Mac mini 上修改並 push，這台電腦會自動同步。*
