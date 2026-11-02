# OmniSearch 全球萬維智慧搜尋引擎

媲美 Google 的現代化智慧搜尋引擎 — 跨網頁全域檢索、即時自動補全、Google 新聞 RSS、維基百科知識圖譜、圖片檢索、AI 智慧摘要與深色/淺色模式。

---

## 🌟 核心特色功能

1. **🌐 全域實時網頁檢索 (Live Web Search)**
   - 採用 DuckDuckGo Lite 實時爬梳引擎，支援任何中英文詞彙、程式語言、國際新聞與即時資訊檢索。
   - 解析網站 Favicon、完整階層網址（Breadcrumb）、高亮關鍵字標題與內文摘要。
   - 具備 Wikipedia 權威全文與 Google 新聞 RSS 智慧備援機制，保證查詢絕不留白。

2. **⚡ Google 級即時補全建議 (Google Suggest Autocomplete)**
   - 整合 Google Suggest API，打字瞬間提供 8 組最相關建議字詞。
   - 支援鍵盤方向鍵（↑ / ↓）選取、Enter 立即搜尋與 Escape 關閉。
   - 當輸入框為空時，智慧提示最近搜尋歷史紀錄。

3. **✨ Google SGE / Gemini 風格 AI 智慧摘要 (AI Overview)**
   - 針對搜尋關鍵字，自前列網頁即時萃取精華、歸納 3~4 項核心要點與條列解析。
   - 附帶參考來源標籤（Source Chips），可直接點擊回溯來源。

4. **📚 Google 知識圖譜卡片 (Knowledge Graph Panel)**
   - 桌面版右側即時展示權威維基百科圖譜：高畫質首圖、核心介紹、資訊方塊與官方百科直達連結。

5. **📰 多維度分類檢索 (Tabs)**
   - **🌐 全部 (All)**：全網各類網頁與權威站台。
   - **📰 新聞 (News)**：Google News RSS 即時媒體報導與發佈時間。
   - **🖼️ 圖片 (Images)**：維基媒體高解析圖庫與專屬燈箱大圖預覽（Lightbox）。
   - **📚 知識百科 (Knowledge)**：維基百科深入專題條目。

6. **🎯 Google 級精緻細節與貼心設計**
   - **好手氣 (I'm Feeling Lucky)**：一鍵直接導向最相關的首選目標網頁。
   - **📖 閱讀速覽模式 (Reader Mode Modal)**：不用跳出搜尋引擎，在純淨閱讀視窗中預覽網頁內容。
   - **⭐ 星號收藏夾 (Bookmarks Drawer)**：支援收藏喜愛的網頁結果，資料長效保存於本機。
   - **🎙️ 語音搜尋 (Voice Search)**：整合 Web Speech API，支援國語與英語語音即時辨識。
   - **🌙 深色/淺色雙主題**：完美遵循 Google Material Design 3 與 Google 深色模式規範。
   - **🧮 即時運算小工具**：直接輸入數學算式（如 `25*40`、`1024/8`）瞬間計算結果。

---

## 🚀 快速啟動

### 方式一：透過 Tom Chen Project Hub 一鍵啟動
在根目錄啟動 Hub (`啟動Hub.bat`)，點選「OmniSearch 全球萬維搜尋引擎」卡片即可自動開啟 <http://127.0.0.1:7050>。

### 方式二：手動啟動
```bash
python projects/web/omni-search/app.py
```
開啟瀏覽器前往 <http://127.0.0.1:7050>。

---

## 📁 專案架構

```
omni-search/
├── app.py              # Flask 後端伺服器 (API 路由、CORS、速覽提取)
├── search_engine.py    # 搜尋爬蟲核心 (DuckDuckGo, Google Suggest, Google News, Wikipedia)
├── requirements.txt    # 相依套件
├── README.md           # 專案詳細說明文件
├── start.bat           # Windows 快速啟動捷徑
└── static/             # Google 風格前端 Single Page Application
    ├── index.html      # 語意化 HTML5 架構
    ├── style.css       # Material Design 3 設計系統、主題切換與微動畫
    └── app.js          # 即時搜尋、語音辨識、鍵盤導覽與收藏夾
```
