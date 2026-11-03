# OmniSearch 全球萬維智慧搜尋引擎 (100% 非 Google 模組自主架構)

全新的現代化自主搜尋引擎 — **完全不依賴任何 Google 模組、API 或服務**，採用開源與隱私友好的技術棧：跨網頁全域檢索、即時開放式自動補全、即時新聞 RSS、維基百科知識圖譜、高解析圖片檢索、AI 智慧摘要與流暢深色/淺色主題。

---

## 🌟 核心特色功能 (100% 獨立自主架構)

1. **🌐 全域實時網頁檢索 (Live Web Search)**
   - 採用 DuckDuckGo Lite 實時爬梳引擎，支援任何中英文詞彙、程式語言、國際新聞與即時資訊檢索。
   - 解析網站 Favicon (DuckDuckGo Icons 服務)、完整階層網址（Breadcrumb）、高亮關鍵字標題與內文摘要。
   - 具備 Wikipedia 權威全文與即時新聞備援機制，保證查詢絕不留白。

2. **⚡ 開放式即時補全建議 (Autocomplete Suggestions)**
   - 整合 DuckDuckGo Autocomplete API 與維基百科 OpenSearch，打字瞬間提供 8 組最相關建議字詞。
   - 零 Google 服務呼叫，開放跨域原生支援。
   - 支援鍵盤方向鍵（↑ / ↓）選取、Enter 立即搜尋與 Escape 關閉。
   - 當輸入框為空時，智慧提示最近搜尋歷史紀錄。

3. **✨ AI 智慧摘要概覽 (AI Overview)**
   - 針對搜尋關鍵字，自前列網頁即時萃取精華、歸納 3~4 項核心要點與條列解析。
   - 附帶參考來源標籤（Source Chips），可直接點擊回溯來源。

4. **📚 權威知識圖譜卡片 (Knowledge Graph Panel)**
   - 桌面版右側即時展示權威維基百科圖譜：高畫質首圖、核心介紹、資訊方塊與官方百科直達連結。

5. **📰 多維度分類檢索 (Tabs)**
   - **🌐 全部 (All)**：全網各類網頁與權威站台。
   - **📰 新聞 (News)**：Bing News RSS 即時媒體報導與發佈時間。
   - **🖼️ 圖片 (Images)**：維基媒體（Wikimedia Commons）高解析圖庫與專屬燈箱大圖預覽（Lightbox）。
   - **📚 知識百科 (Knowledge)**：維基百科深入專題條目。

6. **🎯 精緻細節與貼心設計**
   - **好手氣 (I'm Feeling Lucky)**：一鍵直接導向最相關的首選目標網頁。
   - **📖 閱讀速覽模式 (Reader Mode Modal)**：不用跳出搜尋引擎，在純淨閱讀視窗中預覽網頁內容。
   - **⭐ 星號收藏夾 (Bookmarks Drawer)**：支援收藏喜愛的網頁結果，資料長效保存於本機。
   - **🎙️ 語音搜尋 (Voice Search)**：整合 Web Speech API，支援國語與英語語音即時辨識。
   - **🌙 深色/淺色雙主題**：採用現代系統無感字型與流暢深淺色主題。
   - **🧮 即時運算小工具**：直接輸入數學算式（如 `25*40`、`1024/8`）瞬間計算結果。

---

## 🚀 三種執行與使用方式

### 方式一：線上免安裝、免伺服器直接使用（推薦！可在手機、平板與他人電腦直接開）
本專案內建**「雙模自動切換引擎」**：
- 當沒有啟動本機 Python 後端時，前端會自動啟用純前端免伺服器檢索引擎，透過開放式 CORS 全球資訊庫與開放補全服務直接提供搜尋服務。
- 只要部署到 GitHub Pages，任何人打開網址：
  `https://tomchen0722.github.io/tom-projects/projects/web/omni-search/static/index.html`
  **完全不用在電腦上執行任何程式，用手機、平板或任何瀏覽器點開即可搜尋！**

### 方式二：免費雲端 24 小時線上部署（Render / Vercel）
若需要 24 小時全功能的 Python 爬蟲檢索服務：
1. 專案內已附帶 `render.yaml` 與 `Procfile`、`vercel.json`。
2. 前往 [Render.com](https://render.com) 連結此 GitHub 倉庫建立免費 Web Service。
3. 即可獲得永久專屬公開網址（如 `https://omni-search-xxxx.onrender.com`），不需開機也能隨時連線。

### 方式三：透過 Tom Chen Project Hub 本機一鍵啟動
在根目錄啟動 Hub (`啟動Hub.bat`)，點選「OmniSearch 全球萬維搜尋引擎」卡片即可自動開啟 <http://127.0.0.1:7050>。

也可以手動在終端執行：
```bash
python projects/web/omni-search/app.py
```

---

## 📁 專案架構

```
omni-search/
├── app.py              # Flask 後端伺服器 (API 路由、CORS、速覽提取)
├── search_engine.py    # 100% 非 Google 獨立搜尋爬蟲核心 (DuckDuckGo Lite, Bing News RSS, Wikipedia)
├── requirements.txt    # 相依套件
├── Procfile            # 雲端 PaaS (Render, Heroku, Railway) 啟動配置
├── render.yaml         # Render 免費雲端自動部署設定
├── vercel.json         # Vercel 靜態/雲端路由設定
├── README.md           # 專案詳細說明文件
├── 搜尋引擎運作原理與技術架構解析.md # 深度技術架構、爬蟲原理與搜尋生命週期詳解手冊
├── start.bat           # Windows 快速啟動捷徑
└── static/             # 獨立前端 Single Page Application (支援純前端免伺服器模式)
    ├── index.html      # 語意化 HTML5 架構與狀態標記
    ├── style.css       # 現代獨立設計系統、主題切換與微動畫
    └── app.js          # 雙模檢索引擎 (後端 API + 純前端開放檢索)
```
