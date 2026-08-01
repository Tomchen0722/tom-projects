# Streamlit Cloud 部署教學（白話版）

## 這是在做什麼

你的專案現在只能在自己電腦上跑。別人想看，你得把電腦借他。

**Streamlit Cloud 是一台免費的公用電腦**，你把程式放上去，它幫你 24 小時開著，
任何人用網址就能打開。就像把影片上傳 YouTube，別人不用你的電腦也看得到。

它是 Streamlit 官方提供的，免費，不用綁信用卡。

---

## 為什麼 12 個專案只有 2 個能上

Streamlit Cloud 這台公用電腦**只認得 Streamlit 寫的程式**，其他的它跑不動。

| 你的專案 | 用什麼寫的 | 能不能上 |
|---|---|---|
| 智慧旅宿平台 | Streamlit | 可以 |
| AI 學習地圖 | Streamlit | 可以 |
| QR 點餐、AI 指揮室、資安自學院 | Flask | 不行，要換別的平台 |
| LLM 問答、AI 會議助理、台股回測、英文學習 | 桌面程式 | 不行，網頁開不了視窗 |
| AWS、GCP、Git 教材 | 純網頁 | 不用 Streamlit，走 GitHub Pages |

所以這份教學只處理那 2 個。

---

## 開始之前

確認兩件事：

1. 程式已經推上 GitHub（你已經做完了）
2. 你有 GitHub 帳號（`Tomchen0722`）

---

## 第一步：登入

1. 打開瀏覽器，網址列輸入 **share.streamlit.io**
2. 畫面上會有一顆按鈕寫 **Continue with GitHub**，點它
3. GitHub 會問你「要授權 Streamlit 讀取你的專案嗎」，按 **Authorize**

> 授權是什麼意思：你允許 Streamlit 這個網站去看你 GitHub 上的程式碼。
> 不授權它就找不到你的專案。這是必要的，也可以隨時取消。

登入後會看到一個空白的工作台，上面有一顆 **Create app** 或 **New app** 的按鈕。

---

## 第二步：建立第一個 App（智慧旅宿平台）

點 **Create app**，如果它問你要用哪種方式，選 **Deploy a public app from GitHub**。

接著會看到一張表單，有四個欄位要填：

### 欄位 1：Repository（專案位置）

點下拉選單，找到並選擇：

```
Tomchen0722/tom-projects
```

> 如果找不到：可能是授權範圍不夠。畫面上通常會有一行小字
> 「Can't find your repo?」，點它照指示補授權即可。

### 欄位 2：Branch（分支）

選 **main**。

> 分支是什麼：同一個專案可以有很多條開發線，`main` 是主線。
> 你目前只有這一條，直接選它。

### 欄位 3：Main file path（主程式在哪）

**這一格是重點，也最容易填錯。**

它問的是「要執行哪一個檔案」。你的專案裡有幾百個檔案，
要明確告訴它從哪一個開始跑。

複製貼上這一整串：

```
projects/web/Smart_accommodation_4/index.py
```

> 為什麼這麼長：因為檔案放在資料夾裡面的資料夾。
> 這串的意思是「先進 projects 資料夾 → 再進 web → 再進 Smart_accommodation_4
> → 執行裡面的 index.py」。斜線就是「進入下一層」的意思。
>
> 注意大小寫要完全一樣，`Smart_accommodation_4` 的 S 是大寫。

### 欄位 4：App URL（網址）

它會自動幫你產生一組，你也可以自己改。例如：

```
tom-smart-accommodation
```

最後網址就會是 `https://tom-smart-accommodation.streamlit.app`

> 這串只能用小寫英文、數字和連字號，不能有中文或空格。

### 按下 Deploy

填完按 **Deploy!**

---

## 第三步：等它安裝（會等比較久）

按下去之後畫面會跳到一個黑底的視窗，一直捲動文字。那是它在做這些事：

1. 把你的程式從 GitHub 抓下來
2. 讀 `requirements.txt`，把程式需要的工具一個一個裝起來
3. 啟動你的程式

**智慧旅宿平台需要裝的東西比較多**（機器學習相關的套件），
第一次大概要 **5 到 15 分鐘**。這很正常，不是當掉了。

你可以先去做別的事，它跑完會自動開啟你的網站。

> 如果最後出現紅字說 error：把那段文字複製給我，我幫你看。
> 最常見的原因是某個套件版本不合，改一行就能解決。

---

## 第四步：建立第二個 App（AI 學習地圖）

回到 share.streamlit.io 的工作台，再按一次 **Create app**，
一樣的四個欄位，只有第三格不同：

| 欄位 | 填什麼 |
|---|---|
| Repository | `Tomchen0722/tom-projects` |
| Branch | `main` |
| Main file path | `learning/ai/ml-tutorial/app.py` |
| App URL | 例如 `tom-ml-tutorial` |

這個裝得比較快，大概 3 到 5 分鐘。

---

## 第五步：把網址填回專案（讓入口頁自動更新）

兩個 App 都好了之後，你會拿到兩組網址，像這樣：

```
https://tom-smart-accommodation.streamlit.app
https://tom-ml-tutorial.streamlit.app
```

打開這個檔案：

```
C:\AI\tom-projects\projects.json
```

用記事本或 VS Code 都可以。**搜尋 `"deploy"`**，你會看到這樣的段落：

```json
"deploy": {
  "type": "streamlit",
  "url": ""
}
```

把兩個引號中間填上網址，變成：

```json
"deploy": {
  "type": "streamlit",
  "url": "https://tom-smart-accommodation.streamlit.app"
}
```

> 有兩個地方要填：一個在 `smart-accommodation` 那段，
> 另一個在 `ml-tutorial` 那段。搜尋 `"url": ""` 就能找到。
>
> 注意網址要放在雙引號裡面，最後不要多加逗號。

存檔後，把改動推上 GitHub：

```bash
git -C C:\AI\tom-projects add -A
git -C C:\AI\tom-projects commit -m "填入 Streamlit 網址"
git -C C:\AI\tom-projects push
```

這樣線上入口頁的那兩張卡片，就會從灰色的「準備部署中」
變成可以點的「開啟專案」。

---

## 選用：讓智慧旅宿平台的 AI 建議功能生效

那個專案有一個「AI 智慧建議」功能，需要 Google 的 API 金鑰。
**不設定也能用，只是那一個功能會顯示提示訊息**，其他功能都正常。

想開啟的話：

1. 到 <https://aistudio.google.com/apikey> 申請一組免費金鑰
2. 回到 Streamlit 的 App 頁面，右下角有個 **⋮** 或 **Settings**
3. 點 **Settings → Secrets**
4. 在空白框裡貼上這一行（把金鑰換成你的）：

```toml
GEMINI_API_KEY = "你申請到的金鑰"
```

5. 按 Save，App 會自動重啟

> **金鑰要放這裡，不要寫進程式碼。** 程式碼會上傳到 GitHub 給所有人看到，
> 金鑰被撿走別人就能用你的額度。Secrets 是加密保存的，只有你看得到。

---

## 常見狀況

**Q：網站打開顯示「This app has gone to sleep」**

免費方案的 App 一段時間沒人看會自動休眠，省資源用的。
畫面上會有一顆按鈕寫 **Yes, get this app back up!**，點下去等 30 秒就會醒來。

**Q：我改了程式，網站沒變**

Streamlit Cloud 會自動偵測 GitHub 的更新。你只要 `git push`，
它一兩分鐘內就會自己重新部署。如果沒動靜，到 App 頁面按 **Reboot app**。

**Q：安裝時出現紅字錯誤**

通常是 `requirements.txt` 裡某個套件版本在雲端裝不起來。
把錯誤訊息複製給我，我幫你調整版本。

**Q：可以刪掉重來嗎**

可以。在工作台把滑鼠移到 App 上，右邊有 **⋮** 選單，選 **Delete**。
刪掉不影響你 GitHub 上的程式碼。
