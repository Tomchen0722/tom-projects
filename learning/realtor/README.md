# 不動產經紀營業員資格測驗：證照通關全能學習系統

> **目標 100% 考取證照！收錄最新修訂八大考科深度講義、1,000 題不重複完整解析題庫與全真 60 分鐘模擬考 Web 學習平台。**

---

## 🌟 專案特色亮點

1. **八大考科高頻系統講義（`notes/`）**：
   - 深入整理：經紀業管理條例、民法概要、土地法與平均地權條例（含最新打炒房重罰五千萬修法）、不動產稅法（房地合一2.0、囤房稅2.0、土增稅一生一次與一生一屋）、公平交易法、消保法、公寓大廈管理條例、各式契約書範本與應記載及不得記載事項。
2. **1,000 題不重複標準題庫（`assets/questions-data.js` & `exam/question-bank-full.md`）**：
   - 題題嚴格包含：【題目】、【選項 A/B/C/D】、【正確答案】、【明確法規依據】、【詳細白話精闢解析】與【考點防呆陷阱提點】。
3. **現代化單機離線互動測驗平台（`index.html`）**：
   - **全真模擬考試**：隨機抽取 100 題、60 分鐘倒數計時、自動評分（60 分及格）。
   - **章節循序練習**：支援八大考科獨立篩選練習，即選即揭示答案與解析。
   - **錯題強化筆記本**：練習或模考做錯之題目自動保存於 LocalStorage，支援針對錯題反覆重測。
   - **全題庫關鍵字即時搜尋**：輸入關鍵字（如「房地合一」、「30日」、「定金」）即時調出對應考題。
   - **高頻數字速記卡**：考前 10 分鐘必讀數字密碼（天數、金額、比例、罰鍰）。
   - **支援深色 / 淺色護眼模式切換**。

---

## 📁 專案目錄結構

```
c:\AI\tom-projects\learning\realtor\ (同步連結至 C:\AI\realtor)
├── index.html                    # 互動學習與模擬考 Web 平台主入口
├── README.md                     # 專案說明文件
├── assets/
│   ├── app.css                   # 和金高奢風格樣式表 (深/淺色支援)
│   ├── app.js                    # 測驗引擎、計時器、錯題本、搜尋邏輯
│   └── questions-data.js         # 1,000 題結構化題庫資料庫 (JSON 陣列)
├── notes/                        # 八大考科深度講義 Markdown
│   ├── 00-study-guide.md         # 證照通關全戰略指南與讀書計畫
│   ├── 01-broker-act.md          # 不動產經紀業管理條例深度講義
│   ├── 02-civil-law.md           # 民法概要（總則/物權/買賣租賃）講義
│   ├── 03-land-law.md            # 土地法規與平均地權條例講義
│   ├── 04-real-estate-tax.md     # 不動產相關稅法與節稅講義
│   ├── 05-fair-trade.md          # 公平交易法與不實廣告講義
│   ├── 06-consumer-protection.md # 消費者保護法與定型化契約講義
│   ├── 07-apartment-condo.md     # 公寓大廈管理條例深度講義
│   └── 08-standard-contracts.md  # 各式契約書範本應記載事項實務講義
├── exam/                         # 題庫與速記卡電子書
│   ├── question-bank-full.md     # 1,000 題完整題庫電子書 (方便列印自修)
│   └── quick-review-cards.md     # 考前 30 分鐘必備：100 個關鍵數字考點速記卡
└── scripts/                      # 題庫與講義自動生成腳本庫
    ├── build_notes.py
    ├── build_remaining_notes.py
    ├── build_cards.py
    ├── q_sec1.py
    ├── q_sec2.py
    ├── q_sec3.py
    ├── q_sec4.py
    ├── q_sec5_8.py
    └── compile_bank.py
```

---

## 🚀 快速開始學習

1. **使用瀏覽器直接開始刷題與模考**：
   - 雙擊開啟 [`index.html`](file:///C:/AI/realtor/index.html)，即可在電腦上直接進行 100 題模擬考與錯題複習。
2. **閱讀 1,000 題完整解析電子書**：
   - 使用 VS Code 或 Markdown 閱讀器開啟 [`exam/question-bank-full.md`](file:///C:/AI/realtor/exam/question-bank-full.md)。
3. **考前 30 分鐘衝刺**：
   - 閱讀 [`exam/quick-review-cards.md`](file:///C:/AI/realtor/exam/quick-review-cards.md) 的 100 個數字考點速記清單。

祝您輕鬆斬獲 85 分以上高分，順利考取不動產經紀營業員專業證照！
