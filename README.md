# Tom Chen — Project Hub

作品集與學習專案的本機總控台。開一個網頁，點一下卡片就在本機啟動對應的專案：
網頁類自動開分頁，桌面類直接開視窗。

視覺設計沿用 `tom-portfolio` 的紙墨色系與字體，是同一套設計語言。

---

## 快速開始

雙擊根目錄的 **`啟動Hub.bat`**，瀏覽器會自動開啟 <http://127.0.0.1:7000>。

關閉那個黑色視窗，所有由 Hub 啟動的專案都會一併停止。

也可以手動啟動：

```bash
python hub/app.py
```

---

## 目錄結構

```
tom-projects/
├── projects.json          ← 專案登記檔（新增專案改這裡）
├── 啟動Hub.bat            ← 一鍵啟動
├── hub/                   ← 總控台本體（Flask）
│   ├── app.py             ← 路由與 API
│   ├── core/
│   │   ├── registry.py    ← 讀取登記檔
│   │   ├── interpreter.py ← 挑選合適的 Python 直譯器
│   │   └── launcher.py    ← 啟動／停止／狀態偵測
│   ├── templates/         ← 首頁與說明頁
│   ├── static/            ← 樣式、前端腳本、共用返回按鈕
│   ├── tools/             ← 維護用腳本
│   └── logs/              ← 各專案執行記錄（不進版控）
├── projects/              ← 專案作品集
│   ├── web/               ← 智慧旅宿平台、QR 點餐、AI 指揮室
│   └── desktop/           ← LLM 問答、AI 會議助理、台股回測
├── learning/              ← 學習專案
│   ├── cloud/             ← AWS、GCP
│   ├── dev/               ← Git 教材、資安自學院
│   ├── ai/                ← AI 學習地圖
│   └── language/          ← 英文學習系統
└── docs/
    └── ADD_PROJECT.md     ← 如何新增專案
```

---

## 專案清單與狀態

### 專案作品集

| 專案 | 型態 | Port | 狀態 |
|------|------|------|------|
| 智慧旅宿平台 | Streamlit | 8501 | 可執行 |
| QR 點餐系統 | Flask | 3000 | 可執行（連 Supabase） |
| 自動的小龍蝦 AI 指揮室 | Flask | 5566 | 可執行 |
| LLM 問答系統 | 桌面 | — | 可執行（問答功能需 API 金鑰） |
| AI 會議助理 | 桌面 | — | 可執行 |
| 台股波段回測系統 | 桌面 | — | 可執行 |

### 學習專案

| 專案 | 型態 | Port | 狀態 |
|------|------|------|------|
| AWS 雲端筆記 | 靜態 | 7001 | 可執行 |
| GCP 學習實驗室 | 靜態 | 7002 | 可執行 |
| Git 企業級教材 | 靜態（需產生） | 7003 | 可執行 |
| 資安自學院 | Flask | 5000 | 可執行 |
| AI 學習地圖 | Streamlit | 8510 | 可執行 |
| 英文學習系統 | 桌面 | — | 可執行 |

12 個專案都已實測可正常啟動。

---

## 這個 Hub 怎麼運作

**直譯器自動挑選** — 這台機器上有多個 Python（anaconda、python.org、py launcher）。
Hub 啟動時會探測每一個，替每個專案挑出「套件最齊」的那一個，
所以不需要手動指定路徑。AI 會議助理則使用它自己的 `.venv`（內含 PyTorch）。

**缺套件自動安裝** — 點啟動時若偵測到缺少套件，會先跳出確認視窗說明缺什麼、
預估要多久，確認後才安裝，不會擅自佔用頻寬。

**回 Hub 按鈕** — 所有網頁類專案的左下角都有一顆「回 Hub」按鈕。
它是由 Hub 提供的共用腳本產生的，單獨執行專案時載入失敗會自動略過，
不會影響專案本身。

**外部程序辨識** — 如果某個 port 上已經有服務在跑，但不是 Hub 啟動的，
卡片會標成琥珀色的「外部執行中」，並且不提供停止按鈕（Hub 沒有它的控制權）。

**啟動失敗看得到原因** — 桌面程式沒有 port 可以探測，Hub 會檢查程序是否存活、
專案自己的 `error.log` 有沒有被寫入、執行記錄裡有沒有致命錯誤，
失敗時把錯誤訊息直接顯示在卡片上。

---

## 新增專案

1. 把專案資料夾放進對應的分類目錄
2. 在 `projects.json` 的 `apps` 陣列加一段設定
3. 重整瀏覽器（不必重啟 Hub）

詳細欄位說明見 [docs/ADD_PROJECT.md](docs/ADD_PROJECT.md)。

如果新增的是網頁專案，跑一次注入腳本讓它也有返回按鈕：

```bash
python hub/tools/inject_return.py
```

---

## 安全注意事項

**這個 repo 不包含任何金鑰或資料庫。** `.gitignore` 已經擋掉：

- `.env` 與所有環境變數檔（保留 `.env.example`）
- `projects/web/AI_agent/config.json`（內含 Gemini API 金鑰）
- 所有 `*.db` / `*.sqlite` 資料庫檔
- 虛擬環境、打包產物、執行記錄

Clone 之後要讓專案能跑，需要自己補上這些檔案。
`AI_agent` 可以複製 `config.example.json` 為 `config.json` 再填入金鑰。

**修改 `.gitignore` 最上面那段之前請務必確認**，那是防止金鑰外流的第一道防線。

---

## 線上部署

三個靜態站可以放上 GitHub Pages、兩個 Streamlit 專案可以放上 Streamlit Cloud，
根目錄的 `index.html` 是線上入口頁（會自動讀 `projects.json`，新增專案不必改它）。

設定步驟見 [docs/DEPLOY.md](docs/DEPLOY.md)。

---

## 已修正的問題

搬移過程中發現三個原專案就存在的缺陷，都已在這裡的副本修好（原資料夾未更動）：

**LLM 問答系統** — `llm_service.py` 在建構時就建立 OpenAI 客戶端，
沒有金鑰會讓程式在啟動階段就結束，連介面都看不到。
已改成第一次發問時才建立，並補上 `chat_service` 呼叫卻不存在的 `generate()` 方法。
沒有金鑰時視窗照常開啟，發問時才提示要設定：

```
OPENAI_API_KEY=sk-你的金鑰      # 放在專案資料夾的 .env
```

**台股波段回測系統** — `gui_app.py` 匯入了 `MODE_CHOICES`，
但整個專案（含先前打包的版本）都找不到這個常數的定義，
而且 `run_backtest_pipeline` 根本不讀 `params["mode"]`，選了也不影響結果。
已移除該選單，程式恢復正常啟動。

**CyberSecAcademy / AI 指揮室** — port 原本寫死，
改成優先讀 `PORT` 環境變數，讓 Hub 能指派 port，單獨執行時仍沿用原本的預設值。

---

## QR 點餐系統的資料庫

這個專案接的是 Supabase（PostgreSQL），專案裡沒有 SQLite 實作。
連線設定已經填好並實測通過，走的是 **Session Pooler**：

```
aws-1-ap-southeast-1.pooler.supabase.com:5432
```

> **不要改用直連主機 `db.<ref>.supabase.co`。**
> Supabase 免費方案的直連只提供 IPv6（`AAAA` 記錄），一般家用網路沒有對外 IPv6，
> 會出現 `could not translate host name`。Pooler 才有 IPv4。

密碼變更或換機器時，用這支工具重新設定：

```bash
python hub/tools/set_qr_db.py
```

它會隱藏輸入、自動做 URL 編碼（`/` → `%2F` 之類）、去掉貼上時常帶到的方括號，
並且**連線測試通過才寫入 `.env`**，不會留下壞掉的設定。

---

## 設計語言

| 用途 | 值 |
|------|-----|
| 底色 | `#FEFEF9` / `#F5F3EE` |
| 墨色 | `#1C1A18` / `#6A6660` / `#AAA8A3` |
| 主色 | `#3A68AD`（藍）、`#BE4E68`（玫瑰）、`#B87818`（琥珀） |
| 標題字 | Noto Serif TC |
| 內文字 | Noto Sans TC |
| 襯線裝飾 | Cormorant Garamond |
| 等寬字 | JetBrains Mono |

卡片與按鈕右下角的偏移藍框，是整套設計的簽名細節。
