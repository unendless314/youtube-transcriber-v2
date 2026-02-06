# Whisper.cpp CLI 整合說明

本文件紀錄了針對使用者本地環境（macOS + Homebrew 安裝的 `whisper.cpp`）所做的客製化串接調整。

## 變更背景

使用者在其本地目錄 `/Users/linchunchiao/Documents/Youtube_Videos` 已具備編譯好的 `whisper-cli` 執行檔以及多個 `ggml` 模型檔案。

原始程式碼框架預期透過 `whisper-cpp-python` 套件進行串接，但考慮到：
1. 使用者已有穩定的 CLI 工作流。
2. 直接執行編譯好的 C++ 執行檔效能通常優於 Python 封裝。
3. 避免安裝額外的 Python 二進制依賴（可能會有編譯問題）。

因此將後端修改為直接呼叫 CLI 執行檔模式。

## 修改內容

### 1. 設定模型擴充 (`src/transcriber/config/models.py`)
在 `WhisperConfig` 中新增了兩個選填欄位：
- `cpp_bin`: 指向 `whisper-cli` 或 `main` 執行檔的路徑。
- `model_path`: 指向 `.bin` 模型檔案的路徑。

### 2. 後端實作修改 (`src/transcriber/backends/whisper_cpp.py`)
- **音訊預處理**: 加入了 `_convert_to_wav` 方法，使用 `ffmpeg` 將輸入音訊強制轉換為 `16kHz`, `mono`, `pcm_s16le` 格式（此為 `whisper.cpp` 的硬性要求）。
- **CLI 呼叫**: 使用 `subprocess.run` 呼叫執行檔，並傳遞 `-m`, `-f`, `-l`, `-otxt` 等參數。
- **結果解析**: 讀取生成的 `.txt` 檔案內容並回傳。

### 3. 工廠與 Pipeline 串接
- 更新 `BackendFactory` 與 `TranscribeStage` 以支援傳遞上述新增的參數。

## 如何使用

在你的 `channels.yaml` 設定檔中，請確保 `whisper` 區塊如下設定：

```yaml
whisper:
  backend: "cpp"
  model: "large-v3-turbo"  # 僅供紀錄，實際會使用下方 model_path
  cpp_bin: "/Users/linchunchiao/Documents/Youtube_Videos/whisper-cli"
  model_path: "/Users/linchunchiao/Documents/Youtube_Videos/ggml-large-v3-turbo.bin"
```

## 注意事項
- 系統必須安裝有 `ffmpeg` 執行檔。
- 目前實現為讀取 `.txt` 輸出，因此 `TranscriptionResult` 中的 `segments` 會將整段文字包裝在單一片段中。若未來需要精確的時間戳，可擴充解析 `.srt` 或 `.json` 輸出的邏輯。
