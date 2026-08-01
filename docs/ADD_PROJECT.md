# 新增專案

三個步驟：放資料夾 → 改 `projects.json` → 重整瀏覽器。不需要重啟 Hub，也不需要改任何程式碼。

---

## 步驟一：放進對應目錄

| 分類 | 子分類 | 目錄 |
|------|--------|------|
| 專案作品集 | Web 應用 | `projects/web/` |
| 專案作品集 | 桌面應用 | `projects/desktop/` |
| 學習專案 | 雲端 | `learning/cloud/` |
| 學習專案 | 開發工具 | `learning/dev/` |
| 學習專案 | AI / 機器學習 | `learning/ai/` |
| 學習專案 | 語言學習 | `learning/language/` |

要新增子分類，在 `projects.json` 的 `categories` 裡加一段，並建立對應資料夾即可。

---

## 步驟二：登記到 projects.json

在 `apps` 陣列加一段：

```json
{
  "id": "my-project",
  "name": "我的專案",
  "en": "My Project",
  "category": "projects",
  "sub": "web",
  "path": "projects/web/MyProject",
  "kind": "flask",
  "entry": "app.py",
  "port": 5200,
  "python": "auto",
  "needs": ["flask"],
  "requirements": "requirements.txt",
  "desc": "一到兩句話說明這個專案在做什麼、解決什麼問題。",
  "tags": ["Flask", "SQLite"],
  "highlight": false
}
```

### 欄位說明

| 欄位 | 必填 | 說明 |
|------|------|------|
| `id` | 是 | 唯一代號，用小寫與連字號。API 路徑與記錄檔名都用它 |
| `name` | 是 | 中文名稱，顯示在卡片標題 |
| `en` | 是 | 英文名稱，顯示在標題下方 |
| `category` | 是 | `projects` 或 `learning` |
| `sub` | 是 | 子分類 id，要和 `categories` 裡的一致 |
| `path` | 是 | 相對於本檔案根目錄的專案路徑 |
| `kind` | 是 | 專案型態，見下表 |
| `entry` | 是 | 進入點檔名（相對於專案資料夾） |
| `port` | 網頁類必填 | 服務要用的 port；桌面類填 `null` |
| `python` | 是 | `auto` 自動挑選，`venv` 使用專案內建的 `.venv` |
| `needs` | 是 | 執行所需的模組名稱（import 用的名稱，不是套件名） |
| `requirements` | 否 | requirements.txt 路徑；沒有就填 `null` |
| `desc` | 是 | 卡片上的說明文字 |
| `tags` | 是 | 技術標籤陣列 |
| `heavy` | 否 | 設為 `true` 時，安裝確認視窗會提醒依賴很大 |
| `build` | `static-build` 專用 | 產生靜態檔的腳本 |
| `serve_dir` | `static-build` 專用 | 產生出來的資料夾（例如 `site`） |

### kind 的五種型態

| kind | 啟動方式 | 適用 |
|------|----------|------|
| `streamlit` | `python -m streamlit run <entry> --server.port <port>` | Streamlit 應用 |
| `flask` | `python <entry>`，並帶入 `PORT` 環境變數 | Flask / 一般 HTTP 服務 |
| `static` | `python -m http.server <port>` 直接服務該資料夾 | 純 HTML 網站 |
| `static-build` | 先跑 `build`，再服務 `serve_dir` | 需要先產生的靜態網站 |
| `desktop` | `pythonw <entry>` | Tkinter / PySide6 / CustomTkinter |

### needs 要填 import 名稱

填的是 `import` 時用的名稱，不是 pip 安裝的套件名。常見差異：

| pip 套件名 | `needs` 要填 |
|-----------|-------------|
| `python-dotenv` | `dotenv` |
| `psycopg2-binary` | `psycopg2` |
| `pillow` | `PIL` |
| `beautifulsoup4` | `bs4` |
| `faster-whisper` | `faster_whisper` |

填錯會導致 Hub 誤判「缺少套件」而一直要求安裝。

### port 不要重複

目前已使用：

```
3000  QR 點餐系統          5000  資安自學院
5566  AI 指揮室            7000  Hub 本身（保留）
7001  AWS                  7002  GCP
7003  Git 教材             8501  智慧旅宿平台
8510  AI 學習地圖
```

新專案建議從 `7010` 之後往上取，避開常見服務的預設 port。

---

## 步驟三：網頁專案加上返回按鈕

在 `hub/tools/inject_return.py` 的 `TARGETS` 加入檔案路徑，然後執行：

```bash
python hub/tools/inject_return.py
```

路徑可以用萬用字元，例如 `projects/web/MyProject/templates/*.html`。
這個腳本可以重複執行，已經注入過的檔案會自動跳過。

**Flask 專案**只需要注入繼承用的 `base.html`，子頁面會自動繼承。

**Streamlit 專案**不吃外部腳本，要直接在程式裡加。
可以參考 `learning/ai/ml-tutorial/app.py` 裡那段 `st.markdown`，
複製過去放在 `st.set_page_config()` 之後即可。

---

## 讓專案接受 Hub 指派的 port

Hub 會用 `PORT` 環境變數告訴 Flask 專案要聽哪個 port。
如果專案把 port 寫死，改成這樣就能同時支援兩種用法：

```python
port = int(os.environ.get("PORT", 5000))   # 單獨執行時沿用原本的預設值
app.run(host="127.0.0.1", port=port)
```

`learning/dev/CyberSecAcademy/app.py` 與 `projects/web/AI_agent/app.py` 都是這樣改的，
可以直接參考。

---

## 檢查有沒有設定成功

```bash
curl http://127.0.0.1:7000/api/check/my-project
```

回傳 `missing` 是空陣列就表示環境齊備，可以直接啟動。
