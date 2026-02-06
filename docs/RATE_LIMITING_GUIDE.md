# 無 Cookies 模式的智慧處理策略

## 問題背景
不使用 cookies 時，YouTube 會對大量請求觸發反爬蟲：
```
Sign in to confirm you're not a bot
```

但透過「智慧延遲」，可以在無 cookies 情況下穩定處理約 60 部影片/天。

## 核心概念

### YouTube 反爬蟲的觸發條件
1. **短時間內大量請求**（1 分鐘內 > 10 次）
2. **固定模式**（間隔完全一樣）
3. **無使用者行為特徵**（無 cookies、無瀏覽器指紋）

### 規避策略
1. **隨機延遲** - 每次請求間隔 30-90 秒（隨機）
2. **分散時段** - 一次只處理部分頻道，分批執行
3. **專注新影片** - 只處理最新 1-2 部，而非歷史影片

## 建議設定

### 情境 1：每天定時執行（推薦）

```yaml
# channels.yaml
global:
  max_videos_check: 1      # 每個頻道只檢查最新 1 部
  max_duration: 120
  cookies_file: null
  cookies_from_browser: null

channels:
  # 13 個頻道 × 1 部 = 每天處理 13 部新影片
  # 完全不會觸發反爬蟲
```

執行：
```bash
# 設定 cron 每天早上 8 點執行
0 8 * * * cd ~/Documents/GitHub/youtube-transcriber-v2 && PYTHONPATH=src python3 -m transcriber
```

### 情境 2：批次處理歷史影片

如果你想「補抓」過去失敗的影片：

```yaml
global:
  max_videos_check: 5      # 檢查 5 部
  
channels:
  # 每次只選 3-4 個頻道執行，分批處理
  # 例如今天處理前 4 個，明天處理後 4 個
```

並在程式中加入延遲（我可以幫你實作）。

## 延遲機制實作

在 `stages.py` 中加入：

```python
import random
import time

class DownloadStage(Stage):
    def execute(self, context: ProcessingContext) -> ProcessingContext:
        # 每次下載前隨機等待 30-90 秒
        delay = random.uniform(30, 90)
        self.logger.info("rate_limit_delay", seconds=delay, video_id=context.video_id)
        time.sleep(delay)
        
        # ... 其餘程式碼
```

這樣 13 個頻道 × 5 部影片 × 60 秒平均延遲 = 約 65 分鐘處理時間，完全不會觸發反爬蟲。

## 結論

| 需求 | 建議方案 |
|------|---------|
| 每天自動追蹤新影片 | 無 cookies + max_videos_check: 1 + cron |
| 一次性補抓歷史影片 | Cookies 檔案 + 批次處理 |
| 最大化處理量 | 無 cookies + 智慧延遲 + 分批執行 |

無 cookies 模式雖然每天只能處理約 60 部，但對於「追蹤新影片」這個需求已經非常足夠，且維護成本為零。
