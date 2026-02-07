#!/bin/bash

# =================================================================
# YouTube Transcriber 自動同步與轉錄腳本
# =================================================================

# 1. 進入專案目錄
cd "$(dirname "$0")" || exit
PROJECT_DIR="$(pwd)"
export PYTHONPATH="$PYTHONPATH:$PROJECT_DIR/src"

echo "--- [$(date +'%Y-%m-%d %H:%M:%S')] 啟動自動化任務 ---"

# 2. 同步雲端最新資料 (防止衝突)
echo "正在拉取雲端最新內容..."
git pull --rebase origin master

# 3. 執行轉錄任務
# 使用 caffeinate 確保轉錄期間系統不休眠 (-i 代表防止系統閒置休眠)
echo "開始執行轉錄 (使用 caffeinate 預防休眠)..."
# 這裡使用 python3 -m transcriber 執行，這是最穩定的方式
caffeinate -i python3 -m transcriber --config channels.yaml

# 4. 檢查是否有新產生的 Markdown 檔案
echo "檢查變動並準備推送..."
git add output/

# 只有在有變動時才 commit 並 push
if ! git diff-index --quiet HEAD --; then
    echo "偵測到新內容，正在推送到 GitHub..."
    git commit -m "auto: 每日定時轉錄與雙機同步 $(date +'%Y-%m-%d %H:%M')"
    git push origin master
    echo "--- [$(date +'%Y-%m-%d %H:%M:%S')] 同步完成 ---"
else
    echo "沒有新產生的轉錄內容，無需更新。"
    echo "--- [$(date +'%Y-%m-%d %H:%M:%S')] 任務結束 ---"
fi
