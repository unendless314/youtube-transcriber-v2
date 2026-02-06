# YouTube Cookies 設定指南

## 問題
YouTube 在偵測到大量請求時會觸發反爬蟲機制：
```
Sign in to confirm you're not a bot
```

## 解決方案

### 方法零：自動使用瀏覽器 Cookies（最簡單，推薦）

直接在 `channels.yaml` 設定：

```yaml
global:
  cookies_from_browser: "chrome"  # 支援: chrome, firefox, safari, edge
```

**要求**：
- 瀏覽器必須已登入 YouTube
- macOS 上 Safari 會有權限問題，建議使用 Chrome

**測試是否生效**：
```bash
yt-dlp --cookies-from-browser chrome --dump-json "https://www.youtube.com/watch?v=JFjuGKRJk-Y" | head -5
```

### 方法一：使用 yt-dlp 內建功能（手動測試用）

如果你的瀏覽器已登入 YouTube：

```bash
# 使用 Chrome
yt-dlp --cookies-from-browser chrome --list-formats "https://www.youtube.com/watch?v=xxx"

# 使用 Safari（macOS 通常會有權限問題）
yt-dlp --cookies-from-browser safari --list-formats "https://www.youtube.com/watch?v=xxx"

# 使用 Firefox
yt-dlp --cookies-from-browser firefox --list-formats "https://www.youtube.com/watch?v=xxx"
```

### 方法二：手動匯出 Cookies 檔案

#### macOS + Chrome/Edge 用戶：

1. **安裝 cookies.txt 擴充功能**
   - 前往 Chrome Web Store 搜尋 "cookies.txt"
   - 安裝 [Get cookies.txt locally](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckofkjlflgpihlcfldngeh)

2. **匯出 cookies**
   - 開啟 YouTube 並確保已登入帳號
   - 點擊擴充功能圖示
   - 點擊 "Export" 按鈕
   - 儲存為 `youtube_cookies.txt`

3. **移動到專案目錄**
   ```bash
   mv ~/Downloads/youtube_cookies.txt /Users/linchunchiao/Documents/GitHub/youtube-transcriber-v2/
   ```

#### macOS + Safari 用戶：

Safari 不支援直接匯出 cookies，建議：
- 臨時使用 Chrome 登入並匯出
- 或使用 Firefox + cookies.txt 擴充功能

### 方法三：使用 Python 腳本（進階）

```bash
# 安裝 yt-dlp 的瀏覽器 cookie 支援
pip install browser_cookie3

# 提取 cookies 到檔案
python3 << 'PYEOF'
import browser_cookie3
import http.cookiejar

cj = browser_cookie3.chrome(domain_name='youtube.com')
with open('youtube_cookies.txt', 'w') as f:
    for cookie in cj:
        f.write(f"{cookie.domain}\t{cookie.path}\t{cookie.secure}\t{cookie.expires}\t{cookie.name}\t{cookie.value}\n")
print("Cookies 已儲存到 youtube_cookies.txt")
PYEOF
```

## 更新設定檔

編輯 `channels.yaml`：

```yaml
global:
  cookies_file: "./youtube_cookies.txt"  # 改用這個
```

## 驗證是否生效

```bash
# 測試單一影片
yt-dlp --cookies ./youtube_cookies.txt --dump-json "https://www.youtube.com/watch?v=JFjuGKRJk-Y" | head -20
```

如果沒有出現 "Sign in to confirm you're not a bot" 就表示成功了！

## 注意事項

1. **Cookies 會過期**：YouTube cookies 通常 1-2 週後會過期，需要重新匯出
2. **不要分享檔案**：cookies.txt 包含你的登入資訊，不要上傳到 GitHub 或分享給他人
3. **已加入 .gitignore**：專案已設定忽略 `*.txt` 檔案，cookies 不會被意外提交

## 替代方案：降低請求頻率

如果無法使用 cookies，可以在 `stages.py` 中加入延遲：

```python
import time

class DownloadStage(Stage):
    def execute(self, context: ProcessingContext) -> ProcessingContext:
        time.sleep(5)  # 每次下載間隔 5 秒
        # ... 其餘程式碼
```

但這會大幅延長處理時間（13 個頻道 × 5 部影片 × 5 秒 = 5 分鐘額外等待）。
