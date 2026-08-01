# 三個 Flask 專案要放哪裡（白話版）

## 先講結論

| 專案 | 狀態 | 說明 |
|---|---|---|
| 資安自學院 | 已上線 | 零依賴、無資料庫、無金鑰，最單純 |
| QR 點餐系統 | 已上線 | 需要 Supabase 連線與六條環境變數 |
| AI 指揮室 | **可以上，用模擬模式** | 不設金鑰就完全不呼叫 API，零成本 |

---

## 為什麼不能用 Streamlit Cloud

Streamlit Cloud 只認得 Streamlit 寫的程式。你這三個是用 **Flask** 寫的，
它跑不動。Flask 和 Streamlit 是兩套不同的工具，就像 Word 打不開 Excel 檔。

---

## 平台選哪一個

網路上能放 Flask 的免費平台很多，我比較過之後推薦 **Render**：

| 平台 | 免費方案 | 適不適合你 |
|---|---|---|
| **Render** | 有，每月 750 小時 | **推薦**。支援長連線、程式會一直開著 |
| Railway | 只有 $5 試用額度，用完要付費 | 不推薦，會開始收錢 |
| Vercel | 有，但只支援「短時間跑完就結束」的程式 | **不行**，你的 QR 點餐需要長連線 |
| PythonAnywhere | 有，介面簡單 | 不行，它不支援 QR 點餐的即時推播 |
| Fly.io | 額度很少，需要寫 Docker 設定 | 太複雜，不建議初學 |

### Render 的免費方案有什麼限制

**15 分鐘沒人使用會自動休眠。** 下次有人打開網址時要等大約 50 秒才會醒來。

這對作品集展示還可以接受 —— 面試官點進去等 50 秒，畫面會轉圈圈然後正常顯示。
但如果你要給客戶真正使用，就需要付費方案（每月 7 美元，不休眠）。

---

## AI 指揮室：用模擬模式部署（不花錢）

這個專案本身就內建「模擬模式」——**沒有設定 API 金鑰時，它不會對外呼叫任何 AI，
而是回傳一段固定格式的示意內容**。整套介面、部門編制、任務流程、帳本都照常運作，
只有 AI 產出的文字是假的。

拿來當作品集展示剛剛好：看得到完整的系統設計，又完全不會產生費用。

### 為什麼確定不會花錢

程式邏輯在 `llm.py` 的 `call_llm()`：

```python
if provider == "gemini" and cfg.get("GEMINI_API_KEY"):   # 有金鑰才走這條
    ...呼叫 Google API...
if provider == "claude" and cfg.get("ANTHROPIC_API_KEY"): # 有金鑰才走這條
    ...呼叫 Anthropic API...
return _mock(system, prompt, None)                        # 沒金鑰一律走這條
```

而 `config.json`（放金鑰的檔案）已經被 `.gitignore` 排除，**不會上傳到 GitHub，
Render 上也不會有**。`load_config()` 找不到檔案時會用預設值，金鑰是空字串。

實測驗證過：把對外連線函式換成「一被呼叫就報錯」，跑完全程都沒被觸發，
成本計算也是 `0.0`。

### 自動駕駛保持關閉

`app.py` 裡的 `engine.start_autopilot_thread()` 已經註解掉了。

即使在模擬模式下不花錢，那個 `while True` 迴圈每 8 秒跑一次、
持續寫入資料庫，會白白吃掉 Render 免費方案的運算額度。

展示時用介面上的「立即執行」手動觸發任務就夠了，效果一樣。

### Render 設定

| 欄位 | 填什麼 |
|---|---|
| Name | `ai-agent`（網址會是 `ai-agent-xxxx.onrender.com`） |
| Region | Singapore |
| Branch | `main` |
| **Root Directory** | `projects/web/AI_agent` |
| Build Command | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app --bind 0.0.0.0:$PORT` |
| Instance Type | Free |

**環境變數：一條都不用設。** 這是它跟 QR 點餐最大的差別。

### 部署後會看到什麼

- 完整的指揮室介面、部門與角色配置
- 建立任務、手動執行、查看帳本與稽核紀錄都正常
- AI 產出的內容開頭會標示「**【模擬模式輸出】尚未設定 API Key，此為確定性示意內容。**」

這行標示其實對作品集有加分——它明白告訴看的人「這是刻意的展示模式」，
而不是系統壞了。

### 兩個限制要知道

**資料不會保存。** Render 免費方案的檔案系統是暫時的，
服務休眠或重新部署後，SQLite 裡的任務與帳本會全部消失，回到初始狀態。
展示用途沒差，但別把它當正式系統用。

**想改成真的呼叫 AI 的話**，在 Render 的 Environment Variables 加金鑰是**不夠的**——
這個專案是從 `config.json` 讀金鑰，不是讀環境變數。要嘛改程式碼，
要嘛透過介面上的設定頁面填入（但重啟後會消失）。
既然是展示用，維持模擬模式最單純。

---

## 實際操作：把資安自學院放上 Render

先從最單純的開始，成功一次之後其他就照做。

### 第一步：準備兩個檔案

Render 需要知道兩件事：要裝什麼、怎麼啟動。

**檔案一**：`learning/dev/CyberSecAcademy/requirements.txt`（已經有了）

它目前只有一行 `Flask>=3.0`。要再加一行，因為雲端不能用 Flask 內建的伺服器：

```
Flask>=3.0
gunicorn>=21.0
```

> **gunicorn 是什麼**：Flask 內建的伺服器只適合自己測試用，
> 一次只能服務少數人，官方明講不要拿來正式上線。
> gunicorn 是專門處理正式流量的伺服器，速度快也穩定。
> 這是 Python 網站上線的標準做法。

**檔案二**：不用另外建，Render 網頁上直接填啟動指令就好。

### 第二步：在 Render 建立服務

1. 打開 **render.com**，按 **Get Started**，選 **GitHub** 登入
2. 授權 Render 讀取你的 GitHub（跟 Streamlit 一樣的流程）
3. 登入後按右上角 **New +** → 選 **Web Service**
4. 找到 `Tomchen0722/tom-projects`，按 **Connect**

### 第三步：填設定

會看到一張表單：

| 欄位 | 填什麼 | 說明 |
|---|---|---|
| Name | `cybersec-academy` | 網址會變成 `cybersec-academy.onrender.com` |
| Region | `Singapore` | 選離台灣最近的，速度較快 |
| Branch | `main` | |
| **Root Directory** | `learning/dev/CyberSecAcademy` | **重點**：告訴它程式在哪個資料夾 |
| Runtime | `Python 3` | |
| **Build Command** | `pip install -r requirements.txt` | 開機前先裝套件 |
| **Start Command** | `gunicorn app:app --bind 0.0.0.0:$PORT` | 怎麼啟動程式 |
| Instance Type | `Free` | 選免費 |

> **Start Command 那串在說什麼**：
> - `gunicorn` = 用這個伺服器啟動
> - `app:app` = 打開 `app.py` 這個檔案，找裡面叫 `app` 的那個 Flask 物件
> - `--bind 0.0.0.0:$PORT` = 監聽 Render 指定的埠號
>   （`$PORT` 是 Render 自動給的，不要自己填數字）

### 第四步：按 Create Web Service

它會開始安裝，大約 2 到 5 分鐘。畫面會捲動黑色文字，這是正常的。

最後看到 `Your service is live` 就成功了，網址在頁面上方。

---

## QR 點餐系統怎麼上

流程一樣，只有三個地方不同：

| 欄位 | 填什麼 |
|---|---|
| Root Directory | `projects/web/QR_order` |
| Start Command | `gunicorn app:app --bind 0.0.0.0:$PORT --timeout 120` |

（`--timeout 120` 是因為它有即時推播，連線要撐久一點）

### 還要設定環境變數

這個專案需要資料庫密碼等資訊。**這些絕對不能寫進程式碼**，
要用 Render 的環境變數功能：

在建立服務的頁面往下捲，找到 **Environment Variables**，按 **Add Environment Variable**，
把 `.env` 裡的內容一條一條加進去：

| Key | Value |
|---|---|
| `DATABASE_URL` | 你的 Supabase 連線字串 |
| `ADMIN_PASSWORD` | 你的後台密碼 |
| `ADMIN_SECRET` | 你的 session 金鑰 |
| `PUBLIC_URL` | `https://你的服務名.onrender.com` |
| `PAYMENT_PROVIDER` | `mock` |

> `PUBLIC_URL` 要填部署後的網址，因為 QR Code 裡面會包含這個網址，
> 客人掃碼才連得到正確的地方。可以先隨便填，服務建好後再回來改。

### 注意 Supabase 也會睡

你的 Supabase 是免費方案，**閒置 7 天會自動暫停**（之前就發生過一次）。
Supabase 睡著時，QR 點餐網站會顯示資料庫連線錯誤。

要嘛定期去點一下讓它保持活躍，要嘛接受這個限制。

---

## 三個專案上線後的網址

```
https://cybersec-academy.onrender.com
https://qr-order.onrender.com
```

拿到網址之後，記得填回 `projects.json`，線上入口頁的卡片就會自動變成可以點的連結。
在對應專案的 `deploy` 區塊改成：

```json
"deploy": {
  "type": "external",
  "url": "https://cybersec-academy.onrender.com"
}
```

---

## 常見狀況

**Q：Build 失敗，出現紅字**

把錯誤訊息複製下來看最後幾行。最常見是套件版本問題，改 `requirements.txt` 即可。

**Q：網站開得起來但顯示 Internal Server Error**

到 Render 頁面左邊選 **Logs**，看最後的錯誤訊息。
通常是環境變數沒設定（例如少了 `DATABASE_URL`）。

**Q：第一次打開很慢**

免費方案休眠後喚醒需要約 50 秒，這是正常的。重新整理一次就好。

**Q：會不會不小心被收錢**

Render 免費方案不需要綁信用卡，額度用完就是停止服務，不會自動扣款。
**真正要小心的是 AI 指揮室那種會呼叫付費 API 的程式**，
那筆錢是算在你的 API 帳號上，跟 Render 無關。
