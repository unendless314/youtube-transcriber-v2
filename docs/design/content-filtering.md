# 內容篩選過濾功能設計文件 (Content Filtering Design)

> **版本**: 1.0  
> **狀態**: 📝 規劃階段 / 待實作  
> **建立日期**: 2026-02-06  
> **相關文件**: `docs/CONTENT_FACTORY_PIPELINE.md`, `prompts/scout/`

---

## 1. 功能概述

### 1.1 目標
建立一個**內容篩選過濾模組**（代號：Scout），自動對 `output/` 目錄中已轉錄的 YouTube 影片逐字稿進行品質評分與潛力分析，篩選出具備二次創作價值的高品質內容。

### 1.2 核心價值
- **自動化初篩**: 減少人工瀏覽逐字稿的時間成本
- **領域專業化**: 不同頻道使用對應領域的評分標準（Crypto、靈性成長、宏觀金融等）
- **可擴展性**: 未來可輕易新增領域類別與評分邏輯

### 1.3 與 Pipeline 的關係
```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Transcriber    │     │  Content Scout   │     │  Future:        │
│  Pipeline       │ ──→ │  (This Module)   │ ──→ │  Persona Factory│
│  (既有的轉錄)    │     │  (內容篩選過濾)   │     │  (內容加工)      │
└─────────────────┘     └──────────────────┘     └─────────────────┘
        │                       │                         │
        ▼                       ▼                         ▼
   output/*.md            scout_reports/*.md          final_content/*.md
```

---

## 2. 架構設計

### 2.1 領域分類策略 (Domain Classification)

#### 2.1.1 分類方式：**頻道級別綁定 (Channel-Level Binding)**

每個 YouTube 頻道在訂閱時即被賦予一個固定的內容分類。這個決策基於以下觀察：

| 頻道名稱 | 固定分類 | 理由 |
|---------|---------|------|
| Benjamin Cowen | `crypto` | 專注加密貨幣技術分析 |
| Paul Selig | `spiritual_growth` | 靈性教導與通靈訊息 |
| Future Forecasting Group | `remote_viewing` | 遙視預測內容 |
| Richard Dolan | `ufo_disclosure` | UFO 揭秘與調查 |
| Coin Bureau | `crypto` | 加密貨幣教育 |
| Your Monk Haku | `spiritual_growth` | 禪修與心靈成長 |
| ... | ... | ... |

#### 2.1.2 現有分類清單

對應 `prompts/scout/` 目錄下的提示詞：

| 分類 ID | 檔案 | 適用頻道類型 |
|---------|------|-------------|
| `crypto` | `crypto.md` | 加密貨幣分析、區塊鏈技術 |
| `macro_finance` | `macro_finance.md` | 宏觀經濟、貴金屬、利率分析 |
| `spiritual_growth` | `spiritual_growth.md` | 靈性成長、能量更新、冥想引導 |
| `ufo_disclosure` | `ufo_disclosure.md` | UFO 揭秘、地外文明研究 |
| `remote_viewing` | `remote_viewing.md` | 遙視預測、未來趨勢掃描 |
| `tech_career` | `tech_career.md` | 職涯發展、技術趨勢、工程師心態 |

---

### 2.2 配置方案選擇

#### ✅ 採用方案：**擴展 `channels.yaml` 添加 `category` 欄位**

**決策理由：**
1. **簡單直覺**: 頻道與分類是靜態綁定，放一起維護成本低
2. **現有規模**: 目前僅 13 個頻道，複雜度可控
3. **減少檔案**: 避免新增獨立配置檔案，降低認知負擔
4. **向後兼容**: 可設為 optional 欄位，不影響現有功能

**配置範例：**
```yaml
# channels.yaml
channels:
  - name: "Benjamin Cowen"
    url: "https://www.youtube.com/@intothecryptoverse/videos"
    language: "en"
    category: "crypto"  # ← 新增欄位，對應 prompts/scout/crypto.md
    
  - name: "Paul Selig"
    url: "https://www.youtube.com/@PaulSelig"
    language: "en"
    category: "spiritual_growth"
    
  - name: "Future Forecasting Group"
    url: "https://www.youtube.com/@FutureForecastingGroup"
    language: "en"
    category: "remote_viewing"
```

**未來擴展考量：**
若未來需要更複雜的分類邏輯（例如：單一頻道跨多領域），可升級為：
```yaml
# 未來可能的擴展格式
channels:
  - name: "Mixed Content Channel"
    url: "https://www.youtube.com/@mixed"
    category: ["crypto", "macro_finance"]  # 多標籤
    auto_classify: true  # 啟用 AI 自動分類每部影片
```

---

## 3. 資料流設計

### 3.1 輸入
- **逐字稿來源**: `output/{channel_name}/{YYYY-MM}/{YYYYMMDD}_{video_id}_{title}.md`
- **評分標準**: `prompts/scout/{category}.md`
- **頻道配置**: `channels.yaml` 中的 `category` 欄位

### 3.2 輸出
```
output/{channel_name}/{YYYY-MM}/
├── 20260201_xxx_Bitcoin_Report.md              # 原始逐字稿
└── .scout_reports/                              # 隱藏目錄存放評報
    └── 20260201_xxx_Bitcoin_Report_scout.md     # 評分報告
```

**評分報告格式範例：**
```markdown
---
video_id: "yLhApa2vv3s"
analyzed_at: "2026-02-06T19:30:00+08:00"
category: "crypto"
scores:
  information_quality: 8
  creative_potential: 7
priority: "high"  # high / flagged / filtered
---

### 🔥 Bitcoin: Damage Report
*   **Quality:** 8/10 | **Creative:** 7/10
*   **關鍵 Alpha:** 比特幣與白銀的歷史對比分析，指出非狂熱頂部的緩跌特徵
*   **入選理由:** Benjamin Cowen 以 S&P 對黃金比值圖說明宏觀風險，具備機構級分析深度
*   **內容類型:** 深度分析
*   **建議:** 適合製作 Blog 長文與 Threads 懶人包
```

### 3.3 狀態追蹤
使用 SQLite 記錄哪些影片已分析，避免重複呼叫 API：

```sql
CREATE TABLE scout_reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    video_id TEXT UNIQUE NOT NULL,
    channel_name TEXT NOT NULL,
    category TEXT NOT NULL,
    information_quality INTEGER,
    creative_potential INTEGER,
    priority TEXT,  -- 'high', 'flagged', 'filtered'
    analyzed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    report_path TEXT
);
```

---

## 4. 模組設計

### 4.1 核心組件

```
src/transcriber/scout/
├── __init__.py
├── analyzer.py          # ScoutAnalyzer: 核心分析邏輯
├── config.py            # ScoutConfig: 載入頻道分類配置
├── models.py            # Pydantic 模型: ScoutReport, ScoreCriteria
├── storage.py           # ScoutStorage: 報告存取與狀態管理
└── cli.py               # Scout CLI 命令
```

### 4.2 關鍵類別設計

```python
class ScoutAnalyzer:
    """內容篩選分析器"""
    
    def __init__(self, llm_client: LLMClient, prompt_loader: PromptLoader):
        self.llm = llm_client
        self.prompts = prompt_loader
    
    def analyze(self, transcript: Transcript, category: str) -> ScoutReport:
        """分析單部影片逐字稿"""
        prompt = self.prompts.load(f"scout/{category}.md")
        # 呼叫 LLM API 進行評分
        # 解析回傳結果
        return ScoutReport(...)

class ScoutConfig:
    """掃描配置管理"""
    
    def get_channel_category(self, channel_name: str) -> str | None:
        """從 channels.yaml 取得頻道分類"""
        
    def validate_category(self, category: str) -> bool:
        """驗證分類是否對應存在的 prompt 檔案"""
```

---

## 5. CLI 介面設計

### 5.1 命令結構

```bash
# 分析特定頻道的所有未分析影片
python -m transcriber scout --channel "Benjamin Cowen"

# 分析所有頻道（批次模式）
python -m transcriber scout --all

# 分析特定影片（調試用途）
python -m transcriber scout --video-id "yLhApa2vv3s"

# 僅顯示高優先級結果
python -m transcriber scout --channel "Benjamin Cowen" --priority high

# 重新分析已處理過的影片
python -m transcriber scout --channel "Benjamin Cowen" --force
```

### 5.2 輸出範例

```
🎯 Content Scout: Benjamin Cowen (crypto)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📁 Scanning: output/Benjamin_Cowen/2026-02/

✅ 2026-02-01 | Bitcoin: Damage Report
   📊 Quality: 8/10 | Creative: 7/10 | 🔥 HIGH
   💡 關鍵洞察: 比特幣與白銀的歷史對比分析
   💾 Saved to: .scout_reports/20260201_..._scout.md

⚠️ 2026-02-03 | Bitcoin: The Beauty of Mathematics
   📊 Quality: 6/10 | Creative: 5/10 | ⚠️ FLAGGED
   💡 標註: 硬核乾貨，需轉化為白話文

❌ 2026-02-05 | Bitcoin Crash Continues
   📊 Quality: 4/10 | Creative: 4/10 | ❌ FILTERED
   💡 原因: 內容重複，缺乏新觀點

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Summary: 3 analyzed | 1 high | 1 flagged | 1 filtered
💰 API Cost: ~$0.15 USD
```

---

## 6. 限制與注意事項

### 6.1 API 成本管控
- 每部影片需消耗一次 LLM API 呼叫
- 建議設置**每日分析配額**（例如：每個頻道每日最多分析 3 部新影片）
- 可設定**影片時長門檻**（例如：只分析 5-60 分鐘的影片）

### 6.2 錯誤處理
- LLM API 失敗時需記錄錯誤，避免中斷批次處理
- 不完整的逐字稿應標記為 `skipped` 而非失敗
- 定期清理過期的 `scout_reports`（例如：保留 90 天）

### 6.3 未來擴展
- **影片級別分類**: 若頻道內容跨領域，可先用通用 prompt 判斷影片所屬分類，再套用專屬評分標準
- **多模型支援**: 允許不同分類使用不同 LLM 模型（例如：遙視內容用 GPT-4，一般內容用 GPT-3.5）
- **人工回饋**: 記錄用戶對評分結果的回饋，用於未來優化 prompt

---

## 7. 實作時程估算

| 任務 | 預估時間 | 說明 |
|------|---------|------|
| 更新 `channels.yaml` 格式與驗證 | 30 分鐘 | 新增 category 欄位，驗證邏輯 |
| 建立 Scout 模組架構 | 2-4 小時 | models, config, storage |
| 實作分析核心邏輯 | 4-6 小時 | analyzer, LLM 整合 |
| CLI 介面開發 | 2-3 小時 | 命令解析、進度顯示 |
| 整合測試 | 2-3 小時 | 端到端流程驗證 |
| **總計** | **1-2 天** | 不含文件撰寫 |

---

## 8. 決策紀錄 (Decision Log)

| 日期 | 決策 | 理由 | 替代方案 |
|------|------|------|---------|
| 2026-02-06 | 採用頻道級別分類 | 簡單、符合現有頻道特性 | 影片級別自動分類（複雜度過高） |
| 2026-02-06 | 擴展 `channels.yaml` | 維護成本低、向後兼容 | 新建獨立配置檔案 |
| 2026-02-06 | 評分報告存於 `.scout_reports/` | 與原始檔案分離、易於清理 | 存於資料庫或單一檔案 |
| 2026-02-06 | 使用 SQLite 記錄分析狀態 | 與現有架構一致、輕量 | 記錄於檔案名或報告內 |

---

## 9. 待確認問題

實作前需與企劃部門確認：

1. **API 預算**: 每個頻道每日分析上限？單次呼叫成本上限？
2. **時長門檻**: 是否只分析特定長度範圍的影片？
3. **保留策略**: 評分報告保留多久？是否保留 filtered 內容？
4. **觸發時機**: 轉錄完成後自動分析？還是手動執行 scout 命令？
5. **多領域頻道**: 是否有頻道可能橫跨多個分類？如何處理？

---

**文件維護者**: AI Agent  
**最後更新**: 2026-02-06
