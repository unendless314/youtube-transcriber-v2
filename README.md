# YouTube Transcriber V2 🎙️

YouTube 頻道自動轉錄工具 - 穩定、可靠、支援斷點續傳。

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ 功能特色

- 🎯 **斷點續傳**: 中斷後自動從上次進度繼續，斷電不丟失進度
- 📝 **AI 轉錄**: 使用 OpenAI Whisper 語音轉文字，支援多種模型大小
- 📊 **進度追蹤**: 美觀的 Rich 進度條，頻道級和影片級雙層顯示
- 🛡️ **智能重試**: 5 種錯誤類型對應不同重試策略（指數退避 + 抖動）
- 🗂️ **Markdown 輸出**: 包含時間戳記的結構化輸出
- ⚡ **錯誤隔離**: 單一影片失敗不影響其他影片繼續處理
- 🔧 **多後端支援**: OpenAI Whisper（已實作），whisper.cpp / faster-whisper（預留）

## 📦 安裝

### 系統需求

- Python 3.9+
- ffmpeg（yt-dlp 必要依賴）

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt-get install ffmpeg

# Windows (使用 chocolatey)
choco install ffmpeg
```

### 安裝套件

```bash
# 從 PyPI 安裝（推薦）
pip install youtube-transcriber[openai-whisper]

# 或從原始碼安裝
git clone https://github.com/yourusername/youtube-transcriber.git
cd youtube-transcriber
pip install -e ".[openai-whisper]"
```

## 🚀 快速開始

### 1. 建立配置檔案

```bash
# 建立範例配置
youtube-transcriber --init-config channels.yaml
```

### 2. 編輯配置

```yaml
output:
  base_dir: "./output"     # 轉錄檔案輸出目錄
  temp_dir: "./temp"       # 暫存音訊檔案目錄

whisper:
  backend: "openai"        # openai, cpp, faster-whisper
  model: "medium"          # tiny, base, small, medium, large, large-v3
  language: "auto"         # auto 或語言代碼 (zh, en, ja...)

global:
  max_videos_check: 5      # 每個頻道檢查最新 N 部
  max_duration: 90         # 最大影片長度（分鐘）
  cookies_file: null       # 可選：cookies 檔案路徑（會員專屬內容）

channels:
  - name: "頻道名稱"
    url: "https://www.youtube.com/@channel"
    language: "zh"         # 可選，覆寫全域設定
    max_duration: 120      # 可選，覆寫全域設定
```

### 3. 執行轉錄

```bash
# 基本使用
youtube-transcriber --config channels.yaml

# 測試模式（不實際下載/轉錄）
youtube-transcriber --config channels.yaml --dry-run

# 詳細輸出
youtube-transcriber --config channels.yaml --verbose

# 停用進度顯示（輸出到檔案時）
youtube-transcriber --config channels.yaml --no-progress

# 指定輸出目錄
youtube-transcriber --config channels.yaml --output ./my-transcripts
```

## 📁 輸出格式

```
output/
├── {channel_name}/
│   └── {YYYY-MM}/
│       └── {YYYY-MM-DD}_{video_id}_{title_slug}.md
├── temp/                    # 暫存音訊檔（自動清理）
└── .transcriber.db          # 狀態資料庫（斷點續傳用）
```

### Markdown 格式範例

```markdown
---
channel: "頻道名稱"
video_id: "abc123xyz"
title: "影片標題"
published_at: "2026-01-15"
duration: "45:30"
word_count: 5420
---

# 影片標題

[00:00] 大家好，歡迎來到我的頻道...
[01:30] 今天我們要聊的是...
[03:45] 首先我們來看看...
```

## ⚙️ 進階配置

### 使用 Cookies（會員專屬內容）

1. 安裝 [Get cookies.txt LOCALLY](https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckofkjlflfgjphcngknhnd) 瀏覽器擴充
2. 登入 YouTube 後匯出 cookies
3. 在配置中指定：

```yaml
global:
  cookies_file: "/path/to/youtube_cookies.txt"
```

### 選擇 Whisper 模型

| 模型 | 記憶體需求 | 相對速度 | 用途 |
|------|----------|---------|------|
| tiny | ~1 GB | ~32x | 快速測試 |
| base | ~1 GB | ~16x | 英文內容 |
| small | ~2 GB | ~6x | 一般用途 |
| medium | ~5 GB | ~2x | **推薦** |
| large | ~10 GB | 1x | 最高品質 |

### 自定義重試策略

目前支援 5 種錯誤類型的自動重試：

| 錯誤類型 | 重試次數 | 延遲策略 | 說明 |
|---------|---------|---------|------|
| NETWORK | 3 | 1s → 2s → 4s | 網路問題 |
| RATE_LIMIT | 5 | 5s → 10s → ... | 請求過頻 |
| RESOURCE | 2 | 3s | 資源不足 |
| VIDEO | 0 | - | 影片問題（私人/刪除） |
| SYSTEM | 0 | - | 系統問題 |

## 🧪 開發

### 執行測試

```bash
# 安裝開發依賴
pip install -e ".[dev]"

# 執行所有測試
pytest

# 執行單元測試
pytest tests/unit/

# 執行整合測試
pytest tests/integration/

# 產生覆蓋率報告
pytest --cov=src/transcriber --cov-report=html
```

### 專案結構

```
src/transcriber/
├── config/          # 配置管理（Pydantic 模型）
├── core/            # 核心功能
│   ├── state.py     # SQLite 狀態管理 ⭐
│   ├── retry.py     # 智能重試機制
│   ├── errors.py    # 錯誤分類
│   └── progress.py  # 進度顯示
├── pipeline/        # 處理流程
│   ├── stages.py    # Download/Transcribe/Save/Cleanup
│   └── orchestrator.py
├── backends/        # Whisper 後端
│   ├── base.py      # 抽象介面
│   └── openai_whisper.py
└── cli.py           # CLI 入口
```

## 📊 效能指標

- 狀態查詢: < 10ms（NFR-008）
- 支援影片長度: 無限制（依記憶體）
- 長時間運行: 已測試 50+ 部影片穩定運行
- 資料庫: 自動清理 7 天/100 筆舊記錄

## 🔍 故障排除

### 常見問題

**Q: 程式中斷後如何續傳？**  
A: 直接重新執行相同命令，會自動跳過已處理影片。

**Q: 如何重新處理已完成的影片？**  
A: 刪除狀態資料庫（預設在 `output/.transcriber.db`）或手動刪除該影片的輸出檔案。

**Q: 遇到 "Sign in to confirm you're not a bot"？**  
A: YouTube 可能暫時封鎖了 IP，請：
1. 等待 1-2 小時後重試
2. 使用 `--cookies` 傳入登入憑證
3. 使用 VPN 更換 IP

**Q: Whisper 模型載入失敗？**  
A: 確認已安裝對應後端：
```bash
pip install openai-whisper torch
```

## 📝 授權

MIT License - 詳見 [LICENSE](LICENSE) 檔案

## 🙏 致謝

- [OpenAI Whisper](https://github.com/openai/whisper) - 語音轉錄引擎
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - YouTube 下載工具
- [Rich](https://github.com/Textualize/rich) - 終端美化函式庫
