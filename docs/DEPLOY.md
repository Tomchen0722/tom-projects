# 線上部署指引

從上傳 GitHub 到兩個平台部署的完整流程。

12 個專案裡，5 個可以放到網路上、7 個只能在本機執行。

---

## 零、先上傳到 GitHub

commit 與 remote 都已經設定好了（分支 `main`，remote 指向
`https://github.com/Tomchen0722/tom-projects.git`），只差推送這一步：

```bash
git -C C:\AI\tom-projects push -u origin main
```

第一次執行會跳出 GitHub 登入視窗（Git Credential Manager），
用瀏覽器授權一次之後，之後就不會再問。

推完可以確認一下：

```bash
git -C C:\AI\tom-projects log --oneline -1
```

### 之後要更新內容

```bash
git -C C:\AI\tom-projects add -A
git -C C:\AI\tom-projects commit -m "說明這次改了什麼"
git -C C:\AI\tom-projects push
```

### 推之前確認沒有機密外洩

```bash
git -C C:\AI\tom-projects ls-files | grep -E "\.env$|\.db$|\.sqlite|config\.json$"
```

只應該看到 `tsconfig.json` 這種正常的設定檔。
`.env`、`AI_agent/config.json` 與所有資料庫檔都已被 `.gitignore` 排除。

---

| 專案 | 平台 | 狀態 |
|------|------|------|
| AWS 雲端筆記 | GitHub Pages | 純靜態，推上去就能用 |
| GCP 學習實驗室 | GitHub Pages | 純靜態，推上去就能用 |
| Git 企業級教材 | GitHub Pages | 純靜態，推上去就能用 |
| 智慧旅宿平台 | Streamlit Cloud | 需設定 Main file path |
| AI 學習地圖 | Streamlit Cloud | 需設定 Main file path |

其餘 7 個是桌面應用、或需要資料庫與 API 金鑰的服務，沒辦法放在靜態網站上執行。

---

## 一、GitHub Pages（三個靜態站）

### 設定步驟

1. 把 repo 推上 GitHub
2. 進入 repo 的 **Settings → Pages**
3. Source 選 **Deploy from a branch**
4. Branch 選 **main**（或你的預設分支），資料夾選 **/ (root)**
5. 按 Save，等一兩分鐘

完成後網址會是：

```
https://tomchen0722.github.io/tom-projects/
```

三個靜態站的直接網址：

```
https://tomchen0722.github.io/tom-projects/learning/cloud/AWS/index.html
https://tomchen0722.github.io/tom-projects/learning/cloud/GCP-Learning/index.html
https://tomchen0722.github.io/tom-projects/learning/dev/git-course/site/index.html
```

根目錄的 `index.html` 就是入口頁，會自動列出所有專案。三個靜態站直接從那裡點進去。

### 為什麼選 root 而不是 /docs

三個靜態站分散在 `learning/cloud/` 與 `learning/dev/` 底下，用 root 才能讓它們各自的相對路徑（CSS、圖片、子頁面）維持原狀，不必搬動任何檔案。

### 入口頁怎麼知道有哪些專案

`index.html` 會讀取 `projects.json`，所以**新增專案不需要改這一頁**，
只要在登記檔加一段設定就會自動出現。

---

## 二、Streamlit Community Cloud（兩個 Streamlit 專案）

到 <https://share.streamlit.io> 建立 App，兩個專案各建一個。

### 智慧旅宿平台

| 欄位 | 填什麼 |
|------|--------|
| Repository | `Tomchen0722/tom-projects` |
| Branch | `main` |
| Main file path | `projects/web/Smart_accommodation_4/index.py` |

資料檔（`data/` 75 MB、`models/` 46 MB）已經在 repo 裡，程式用
`Path(__file__).parent.parent / "data"` 定位，放在子目錄一樣讀得到。

**選用：LLM 建議功能**
沒有金鑰時這個功能會顯示提示訊息，其他功能照常運作。要啟用的話，
在 App 的 **Settings → Secrets** 貼上：

```toml
GEMINI_API_KEY = "你的金鑰"
```

（也支援 `ANTHROPIC_API_KEY`，兩者擇一即可。）

### AI 學習地圖

| 欄位 | 填什麼 |
|------|--------|
| Repository | `Tomchen0722/tom-projects` |
| Branch | `main` |
| Main file path | `learning/ai/ml-tutorial/app.py` |

**這個專案的 requirements.txt 已經調整過**：原本列了 `torch`、`jupyter`、`notebook`，
但教材裡的 PyTorch 程式碼只是展示用的字串，App 本身不會 import——
留著會讓 Streamlit Cloud 為了 2.5 GB 的依賴而 build 失敗。

若要在本機跑 `notebooks/` 的實戰練習，另外裝就好：

```bash
pip install torch torchvision jupyter notebook
```

---

## 三、部署完成後：把網址填回登記檔

兩個 Streamlit App 上線後，把網址填進 `projects.json`：

```json
{
  "id": "smart-accommodation",
  "deploy": {
    "type": "streamlit",
    "url": "https://你的-app-名稱.streamlit.app"
  }
}
```

填好後入口頁的卡片會從「準備部署中」變成「可線上瀏覽」，
按鈕也會從停用狀態變成可以點的連結。

---

## 四、注意事項

### 機密檔案不會被推上去

`.gitignore` 已經擋掉 `.env`、`AI_agent/config.json`、所有 `*.db` 與 `*.sqlite`。
推之前可以自己確認一次：

```bash
git ls-files | grep -E "\.env$|\.db$|\.sqlite|config\.json$"
```

只應該看到 `tsconfig.json` 之類的正常設定檔。

### repo 大小

版控內容約 119 MB（708 個檔案），最大單檔 29 MB，都在 GitHub 的限制內。
虛擬環境與打包產物都已排除。

### 靜態站的返回按鈕

三個靜態站左下角有「回作品集」按鈕。它會自己判斷環境：

- 在本機（localhost）→ 連到 Project Hub
- 在 GitHub Pages 上 → 連回入口頁

要重新產生這些按鈕，執行：

```bash
python hub/tools/inject_return.py
```
