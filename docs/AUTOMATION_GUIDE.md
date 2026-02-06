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
