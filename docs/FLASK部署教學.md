# 三個 Flask 專案要放哪裡（白話版）

## 先講結論

| 專案 | 建議 | 原因 |
|---|---|---|
| 資安自學院 | **馬上可以上 Render** | 零依賴、無資料庫、無金鑰，最單純 |
| QR 點餐系統 | 可以上 Render，但要先確認 Supabase 沒睡著 | 需要資料庫連線 |
| AI 指揮室 | **建議先不要上** | 它會自己一直呼叫 AI，24 小時持續花錢 |

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

## 為什麼 AI 指揮室建議先不要上

這個要特別說明，因為**牽涉到錢**。

我看了 `engine.py` 的程式碼，它有一段「自動駕駛」的背景程式：

```
第 259 行：while True:          ← 無限迴圈，永遠不停
第 274 行：time.sleep(8)        ← 每 8 秒跑一次
第 36 行：call_llm(...)         ← 呼叫 AI 模型（要付費）
```

翻成白話：**這個程式一啟動，就會每 8 秒去問一次 AI，永遠不停。**

在你自己電腦上，你關掉視窗它就停了。但放到雲端**它會 24 小時不間斷地跑**，
一天就是 10800 次呼叫。就算每次只花 0.001 美元，一個月也要 300 多美元。

而且金鑰是你的 Gemini API 金鑰，帳單會算在你頭上。

### 如果還是想上，有三個做法

**做法一（最安全）：只放展示畫面，關掉自動駕駛**

修改 `app.py` 最後幾行，把這一行拿掉或註解：

```python
engine.start_autopilot_thread()      # 把這行前面加 #
```

這樣網站能開、畫面能看，但不會自己去呼叫 AI。

**做法二：加上預算上限**

`config.json` 裡本來就有 `MONTHLY_BUDGET_USD` 這個設定，
確認程式真的有在檢查它、超過就停。這個要先驗證過才敢上線。

**做法三：不上線，只在本機用 Hub 啟動**

作品集頁面放截圖和說明，想看的人可以下載程式碼自己跑。
這是最省錢也最安全的做法。

> **我的建議是做法三或做法一。** 一個作品集專案不值得冒著不小心產生
> 幾百美元帳單的風險。

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
