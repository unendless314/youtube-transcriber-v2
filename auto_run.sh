#!/bin/bash

# =================================================================
# YouTube Transcriber 自動同步與轉錄腳本
# =================================================================

# 1. 環境變數設定
# 確保 PATH 包含 Homebrew bin (yt-dlp, ffmpeg, whisper-cli 通常在此)
export PATH="/opt/homebrew/bin:$PATH"

# 進入專案目錄
cd "/Users/linchunchiao/Automation/youtube-transcriber-v2" || exit
PROJECT_DIR="$(pwd)"

# 指定 Python 執行檔路徑 (Python 3.13)
PYTHON_BIN="/Library/Frameworks/Python.framework/Versions/3.13/bin/python3"
export PYTHONPATH="$PYTHONPATH:$PROJECT_DIR/src"

echo "--- [$(date +'%Y-%m-%d %H:%M:%S')] 啟動自動化任務 ---"
echo "工作目錄: $PROJECT_DIR"
echo "使用 Python: $PYTHON_BIN"

# 2. 同步雲端最新資料
echo "正在檢查雲端更新..."

# 檢查是否有本地未提交的變更
if [ -n "$(git status --porcelain)" ]; then
    echo "警告: 偵測到本地有未提交的變更，跳過 Git 同步以避免衝突。"
    echo "將使用目前本地版本繼續執行。"
else
    # 嘗試 rebase pull，如果失敗則僅顯示警告但不中斷流程
    if git pull --rebase origin master; then
        echo "Git 同步成功。"
    else
        echo "警告: Git 同步失敗 (可能是網路問題或衝突)。將使用目前本地版本繼續執行。"
    fi
fi

# 3. 執行轉錄任務
echo "開始執行轉錄 (使用 caffeinate 預防休眠)..."
# 使用 caffeinate 確保轉錄期間系統不休眠
# 這裡不使用 'set -e' 導致整個腳本退出，而是捕捉 python 的回傳值
if caffeinate -i "$PYTHON_BIN" -m transcriber --config channels.yaml; then
    echo "轉錄任務執行完成。"
else
    echo "錯誤: 轉錄任務執行期間發生錯誤。" >&2
    # 注意：這裡不 exit，因為即使部分失敗，可能仍有產出的檔案需要同步
fi

# 4. 檢查是否有新產生的 Markdown 檔案並同步
echo "檢查變動並準備推送..."
git add output/

# 只有在有變動時才 commit 並 push
if ! git diff-index --quiet HEAD --; then
    echo "偵測到新內容，正在推送到 GitHub..."
    if git commit -m "auto: 每日定時轉錄與雙機同步 $(date +'%Y-%m-%d %H:%M')"; then
        if git push origin master; then
            echo "--- [$(date +'%Y-%m-%d %H:%M:%S')] 同步完成 ---"
        else
            echo "錯誤: 推送到 GitHub 失敗。"
        fi
    else
        echo "錯誤: Commit 建立失敗。"
    fi
else
    echo "沒有新產生的轉錄內容，無需更新。"
    echo "--- [$(date +'%Y-%m-%d %H:%M:%S')] 任務結束 ---"
fi
