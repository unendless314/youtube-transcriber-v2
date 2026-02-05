# YouTube Transcriber V2

YouTube 頻道自動轉錄工具 - 穩定、可靠、支援斷點續傳。

## 功能特色

- 🎯 **斷點續傳**: 中斷後自動從上次進度繼續
- 📝 **AI 轉錄**: 使用 OpenAI Whisper 語音轉文字
- 📊 **進度追蹤**: SQLite 資料庫記錄處理狀態
- 🗂️  **Markdown 輸出**: 包含時間戳記的結構化輸出
- 🛡️  **錯誤隔離**: 單一影片失敗不影響其他影片

## 快速開始

### 安裝

```bash
# 安裝套件
pip install -e ".[openai-whisper]"

# 安裝 ffmpeg（必要依賴）
# macOS: brew install ffmpeg
# Ubuntu: sudo apt-get install ffmpeg
```

### 建立配置

```bash
# 建立範例配置
youtube-transcriber --init-config channels.yaml
```

### 執行

```bash
# 處理配置的頻道
youtube-transcriber --config channels.yaml

# 測試模式（不實際下載）
youtube-transcriber --config channels.yaml --dry-run

# 詳細輸出
youtube-transcriber --config channels.yaml --verbose
```

## 配置文件

```yaml
output:
  base_dir: "./output"
  temp_dir: "./temp"

whisper:
  backend: "openai"
  model: "medium"
  language: "auto"

global:
  max_videos_check: 5
  max_duration: 90

channels:
  - name: "頻道名稱"
    url: "https://www.youtube.com/@channel"
    language: "zh"
```

## 專案結構

```
src/transcriber/
├── config/          # 配置管理
├── core/            # 核心功能（狀態、錯誤）
├── pipeline/        # 處理流程（下載→轉錄→儲存）
├── backends/        # Whisper 後端（Phase 2）
└── cli.py           # CLI 入口
```

## 開發階段

- **Phase 1** (進行中): 核心基礎設施 - 基本流程、SQLite 狀態、Pipeline
- **Phase 2** (規劃中): 功能完善 - 重試機制、進度顯示、Backend 抽象
- **Phase 3** (規劃中): 品質保證 - 測試、文件、發布

## License

MIT
