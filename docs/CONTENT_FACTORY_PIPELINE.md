# Content Factory Pipeline: 多領域全平台運營自動化方案 (V2)

## 1. 核心願景
利用 `YouTube Transcriber V2` 產出的高品質逐字稿，結合 LLM 的多維度創作能力，建立一套支援**多領域 (Multi-Domain)** 的內容生產流水線。系統能根據影片所屬頻道，自動切換對應的人設風格與評分邏輯，實現「一鍵轉化、精準分發」。

---

## 2. 矩陣式流水線架構 (The Matrix Funnel)

為了支援跨領域內容，系統採用「領域映射」機制，將流程分為四個階段：

### 階段一：領域掃描器 (The Domain Scout) - 潛力評估
*   **輸入：** 原始逐字稿（Markdown 格式） + 領域標籤。
*   **機制：** 根據影片分類，從 `prompts/scout/` 載入特定的評分準則。
*   **當前支持分類：**
    *   `tech_career`: 關注職場生存、技術趨勢、工程師心態。
    *   `crypto`: 關注市場動向、技術科普、風險預警。
    *   `macro_finance`: 關注宏觀經濟、貴金屬、日圓/外匯走勢。
    *   `spiritual_growth`: 關注能量更新、心靈成長、意識提升。
    *   `ufo_disclosure`: 關注解密進展、地外文明研究。
    *   `remote_viewing`: 關注遙視預測、未來趨勢掃描。
*   **輸出：** 該領域的今日高潛力素材（評分 8 分以上）。

### 階段二：風格工廠 (The Persona Factory) - 多維度創作
針對篩選出的素材，從 `prompts/personas/` 載入對應的人設模組進行創作：
1.  **社群組 (Threads/FB)：** 專注於 Hook（鉤子）、高互動率。
2.  **深度分析組 (Blog/Medium)：** 專注於結構化知識、子標題。
3.  **視覺短片腳本 (Shorts)：** 專注於 60 秒內的視覺節奏與旁白。

### 階段三：一致性審核 (The Domain Auditor) - 品質檢核
針對不同領域進行特定的「事實與語氣」校對：
*   **去 AI 化：** 刪除過於死板的連接詞，使語氣更自然。
*   **人設對齊：** 確保科技類內容「精準」、靈性類內容「共鳴」、金融類內容「中立」。
*   **風險提示：** 針對金融/投資類內容自動加入 Disclaimer。

### 階段四：總編輯看板 (The Multi-Domain Dashboard)
*   **呈現：** 按領域分類的 Markdown 報告。
*   **內容：** 「今日科技選文」、「今日金融解讀」、「今日靈性指南」。
*   **動作：** 「閱覽 -> 微調 -> 發布」。

---

## 3. 目錄結構與擴充指南

```bash
prompts/
├── scout/               # 存放各領域的評分邏輯 (Scoring Rubrics)
│   ├── tech_career.md
│   ├── crypto.md
│   └── ...
├── personas/            # 存放各領域的創作人設 (Writing Styles)
│   ├── tech_career.md
│   ├── crypto.md
│   └── ...
└── legacy/              # 存放過往珍貴的 Prompt 紀錄
    └── CRYPTO_EDUCATOR_PERSONA.md
```

### 如何增加新領域？
1.  在 `prompts/scout/` 建立評分標準。
2.  在 `prompts/personas/` 建立創作人設。
3.  (未來) 在配置中將頻道映射至新類別。

---

## 4. 預期效果
1.  **零摩擦切換：** 早上處理科技職涯內容，下午處理靈性更新，系統自動切換大腦。
2.  **高純度輸出：** 透過領域專屬的 Scout 篩選，確保輸出內容不流於表面。
3.  **知識資產化：** 所有的 Prompt 與人設均為 Markdown 格式，易於版本管理與持續優化。