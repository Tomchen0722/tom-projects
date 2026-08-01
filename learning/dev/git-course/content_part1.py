# -*- coding: utf-8 -*-
"""單元一：基礎觀念（第 1-3 課）"""

PART = "單元一 · 基礎觀念"

LESSONS = [
{
"id": "01",
"part": PART,
"title": "Git 是什麼？為什麼工程師離不開它",
"subtitle": "先理解「版本控制」要解決的真正問題，再碰指令。",
"body": r"""
## 1. 為什麼要這樣做（原理）

想像你在寫一份很重要的報告，你可能存過這些檔案：

```text
報告.docx
報告_最終版.docx
報告_最終版_真的最終.docx
報告_最終版_老闆改過.docx
報告_這次真的不改了.docx
```

這就是「土法煉鋼的版本控制」。它有三個致命問題：

- **不知道每一版到底改了什麼**：兩個檔案打開來一行一行比對，很痛苦。
- **多人一起改會覆蓋彼此**：Alice 把檔案寄給你，你改完寄回去，結果 Bob 同時也在改，最後有人的心血被蓋掉。
- **無法安心回到過去**：你想試一個大改動，但怕改壞回不去，於是不敢動。

**Git 就是專門解決這三件事的工具。** 它是一套「版本控制系統（Version Control System, VCS）」，會幫你記錄專案在每個時間點的完整樣貌，讓你可以：隨時看到誰在什麼時候改了什麼、安全地多人協作、以及隨時回到任何一個過去的版本。

:::tip Git 的核心心智模型
Git 不是「幫你存檔」，而是「幫你拍快照（snapshot）」。每一次 commit，就像對整個專案資料夾拍一張照片，並附上一句說明「我這次做了什麼」。這些照片串成一條時間線，你可以在上面自由前進、後退、分岔。
:::

**Git 和 GitHub 不一樣，別搞混：**

| 名稱 | 是什麼 | 類比 |
| --- | --- | --- |
| **Git** | 安裝在你電腦上的版本控制軟體 | 相機（拍快照的工具） |
| **GitHub** | 放 Git 專案的雲端網站 | 相簿雲端（分享、備份、協作） |

你可以只用 Git 不用 GitHub（純本機）；但團隊協作時，GitHub 是大家交換程式碼的「中央集合點」。

## 2. 完整實戰情境：Tom、Alice、Bob

這套教材會用三個人貫穿所有情境，先認識他們：

- **Tom**（就是你）：剛加入公司的新人工程師。
- **Alice**：資深工程師，也是你的 Code Review 主要負責人。
- **Bob**：另一位隊友，常和你改到同一個檔案。

:::story 沒有 Git 的悲劇
公司要做一個網站。Tom、Alice、Bob 三人各自在自己電腦上改 `index.html`。到了下班，三人把檔案用通訊軟體丟到同一個群組。Tom 說「用我的」，於是 Alice 一整天寫的登入功能、Bob 寫的購物車，全部被 Tom 的版本蓋掉，兩人白做一天。

隔天他們改用 Git + GitHub：三人各自 commit 自己的改動並 push 到 GitHub，Git 自動把三個人「不同檔案、甚至同一檔案不同行」的修改**合併**在一起，沒有人的工作被吃掉。這就是為什麼公司一定要用 Git。
:::

## 3. 實際 Git 指令

這一課還沒開始實作，但先讓你看看「Git 的一生」長什麼樣，建立整體印象（細節後面每一課都會教）：

```bash
# 把一個資料夾變成 Git 專案（拍快照的能力開啟）
git init

# 看看目前有哪些檔案被改了
git status

# 把改動放進「準備拍照」的名單（暫存區）
git add .

# 正式拍一張快照，並寫下說明
git commit -m "完成登入頁面"

# 看看到目前為止拍過哪些快照
git log
```

:::tip 現在看不懂沒關係
上面每一個指令，第 3、4 課都會逐字拆解。這裡的目的只是讓你知道：**Git 的日常，就是不斷地 `add`（選要拍什麼）→ `commit`（拍下來並寫說明）** 這個循環。
:::

## 4. VS Code 圖形介面操作

**VS Code** 是目前最多工程師用的免費程式編輯器，而且**內建 Git 功能**，很多操作完全不用打指令。

左側工具列有一個像「分岔樹枝」的圖示，那就是 **原始碼控制（Source Control）** 面板，快捷鍵是 `Ctrl+Shift+G`。之後你會發現：

- 改了哪些檔案，這個面板會像購物清單一樣列出來。
- 打勾、按一下就能 commit，不用背指令。
- 顏色會告訴你：綠色是新增的行、藍色是修改、紅色是刪除。

:::vscode 現在只要做一件事
先確認你電腦有沒有裝 VS Code。沒有的話，下一課會教你安裝。這一課先知道「Git 的圖形介面就住在這個分岔圖示裡」即可。
:::

## 5. 公司最佳實務

- **任何專案，第一天就開 Git**：不要等到寫了一堆才想補版本控制，越早越好。
- **Git 不是備份工具的替代品**：它管的是「程式碼的演進」，重要資料仍要另外備份。
- **公司幾乎都用 Git**：市佔率超過九成，會 Git 幾乎是工程師的基本門檻，跟會用滑鼠一樣。

:::best 心態建議
新人最常見的錯誤，是把 Git 當成「一堆要背的咒語」。正確心態是：**先理解它在做什麼（拍快照、串時間線、合併多人改動），指令自然就記得住。** 這也是這套教材每一課都從「原理」開始的原因。
:::

## 6. 常見錯誤與救援方法

這一課還沒實際操作，先預告新手最常見的三個誤解，讓你提前免疫：

:::warn 誤解一：「Git 會自動幫我存檔」
不會。Git 只在你 `commit` 的那一刻拍快照。沒 commit 的改動，Git 不會記錄。養成「完成一個小段落就 commit 一次」的習慣。
:::

:::warn 誤解二：「push 上去就會蓋掉別人」
不會。Git 設計上會**合併**而非覆蓋，而且當它偵測到可能衝突時，會停下來要你確認，不會偷偷吃掉別人的工作。第 10 課會詳細教衝突怎麼解。
:::

:::warn 誤解三：「做錯了就完蛋了」
Git 幾乎所有操作都可以救回來。它會偷偷保留操作紀錄（reflog），連「誤刪的 commit」都常常能撈回來。第 20 課是一整課的「事故救援大全」。
:::

:::tip 本課重點回顧
Git 是拍快照、GitHub 是雲端相簿；Git 解決的是「版本記錄 + 多人協作 + 安全回溯」三大痛點；日常就是 `add` → `commit` 的循環。下一課，我們把工具裝起來。
:::
"""
},

{
"id": "02",
"part": PART,
"title": "安裝 Git 與 VS Code、做好初次設定",
"subtitle": "把工具備齊，並設定好你的「工程師身分證」。",
"body": r"""
## 1. 為什麼要這樣做（原理）

在拍快照之前，Git 需要知道「這張照片是誰拍的」。所以每一次 commit，Git 都會記下作者的 **名字** 和 **email**。這不是隱私外洩，而是團隊協作的基礎——當 Alice 在看歷史紀錄時，她要知道某一行是 Tom 改的還是 Bob 改的。

這就是為什麼安裝完 Git 的第一件事，是設定 `user.name` 和 `user.email`。**沒設定就 commit，Git 會拒絕或留下空白作者，之後很難補救。**

:::tip 這個設定會跟著你所有專案
用 `--global` 設定一次，之後你電腦上所有 Git 專案都會沿用同一個身分，不用每次重設。
:::

## 2. 完整實戰情境：Tom、Alice、Bob

:::story Tom 的第一天
Tom 進公司第一天，主管請他把工具裝好。他裝完 Git 就急著 `git commit`，結果 Git 跳出一段警告：`Please tell me who you are`。Tom 一頭霧水。

Alice 走過來說：「你還沒告訴 Git 你是誰。每張快照都要簽名，不然三個月後我們看歷史，會看到一堆『不知道是誰』的 commit。」Alice 教他設定名字和 email——**而且 email 要用公司 GitHub 帳號的同一個**，這樣 GitHub 上才會正確顯示是 Tom 的貢獻。
:::

## 3. 實際 Git 指令

**步驟一：安裝 Git**

到 [git-scm.com](https://git-scm.com) 下載對應你作業系統的版本，一路「下一步」安裝即可（Windows 使用者會一併裝好 Git Bash 這個終端機）。裝完後，打開終端機驗證：

```bash
git --version
# 出現類似 git version 2.45.0 就代表成功
```

**步驟二：設定你的身分（最重要）**

```bash
git config --global user.name "Tom Chen"
git config --global user.email "tomchen0722@gmail.com"
```

**步驟三：一些讓生活更好的設定**

```bash
# 讓 Git 訊息有顏色，更好讀
git config --global color.ui auto

# 設定預設分支名稱為 main（現代慣例，取代舊的 master）
git config --global init.defaultBranch main

# 把 VS Code 設為 Git 的預設編輯器（寫 commit 訊息時會用到）
git config --global core.editor "code --wait"
```

**步驟四：檢查設定有沒有成功**

```bash
git config --list
# 會列出所有設定，確認 user.name 和 user.email 正確
```

:::warn Windows 換行符注意事項
Windows 和 Mac/Linux 的「換行」字元不同，容易造成整份檔案看起來「每一行都被改過」。Windows 使用者建議加這行設定，讓 Git 自動處理：

```bash
git config --global core.autocrlf true
```

Mac/Linux 使用者則用 `git config --global core.autocrlf input`。
:::

## 4. VS Code 圖形介面操作

:::vscode 安裝與基本設定
1. 到 [code.visualstudio.com](https://code.visualstudio.com) 下載安裝 VS Code。
2. 安裝時，Windows 使用者建議勾選「加入 PATH」和「在資料夾按右鍵可用 Code 開啟」，日後超方便。
3. 打開 VS Code，按 `Ctrl+~`（波浪鍵）會叫出**內建終端機**，你可以直接在裡面打上面那些 `git config` 指令，不必另外開別的視窗。
4. 建議安裝擴充套件 **GitLens**：它會在每一行程式碼旁邊顯示「這行是誰、什麼時候、為什麼改的」，是公司工程師幾乎人手一個的神器。
:::

:::tip 用 VS Code 當終端機的好處
初學者常被「要開哪個黑色視窗」搞混。最簡單的做法：**所有指令都在 VS Code 的內建終端機打**。程式碼、Git 面板、終端機全在同一個視窗，不用切來切去。
:::

## 5. 公司最佳實務

- **email 要和 GitHub 帳號一致**：否則你在公司 repo 的貢獻不會正確歸屬到你的 GitHub 頭像，年度考核看貢獻時會很吃虧。
- **名字用真名或公司統一格式**：不要用 `xxx123` 這種暱稱，團隊看歷史時要一眼認得出人。
- **統一團隊設定**：有些公司會提供一份標準 `.gitconfig` 或設定腳本，讓全隊的換行、編輯器設定一致，減少無謂的差異。

:::best 進階：不同專案用不同身分
如果你同時參與「公司專案」和「個人 GitHub 開源」，可能想用不同 email。方法是進到某個專案資料夾後，用不加 `--global` 的指令設定「只限這個專案」的身分：

```bash
cd 這個專案資料夾
git config user.email "work@company.com"
```
:::

## 6. 常見錯誤與救援方法

:::warn 錯誤一：commit 時跳出 "Please tell me who you are"
代表你還沒設定身分。照第 3 節設定 `user.name` 和 `user.email` 即可，然後重新 commit。
:::

:::rescue 已經用錯的 email commit 了怎麼辦？
如果你發現前面幾個 commit 用了錯的 email，最單純的情況（還沒 push、只是本機最後一個 commit）可以修正作者資訊：

```bash
# 先設定正確身分
git config user.email "tomchen0722@gmail.com"
# 用正確身分重寫最後一個 commit 的作者
git commit --amend --reset-author --no-edit
```

如果錯的 commit 已經有很多個而且 push 出去了，改寫歷史會影響隊友，這時應該先問 Alice（團隊）該怎麼處理，別自己硬幹。第 20 課會談改寫歷史的風險。
:::

:::warn 錯誤二：`git` 不是可辨識的指令
代表 Git 沒裝好，或安裝時沒加入 PATH。最簡單的解法是重新執行安裝程式，這次確認勾選「加入 PATH / 環境變數」，然後**重開終端機**（設定要重開才生效）。
:::

:::tip 本課重點回顧
裝好 Git 和 VS Code，第一件事是用 `git config --global` 設定名字和 email（email 對齊 GitHub 帳號）。所有指令都可以在 VS Code 內建終端機打。下一課，我們要搞懂 Git 最核心的觀念：三大區域。
:::
"""
},

{
"id": "03",
"part": PART,
"title": "Git 三大區域：搞懂這個，一切都通了",
"subtitle": "工作區、暫存區、儲存庫——Git 所有指令都在這三者之間搬東西。",
"body": r"""
## 1. 為什麼要這樣做（原理）

**這是整套教材最重要的一課。** 90% 的 Git 新手困惑，都來自不理解這三個區域。理解了，後面所有指令都會突然變得合理。

Git 把你的檔案分成三個「地方」：

| 區域 | 英文 | 白話 | 檔案在這裡代表 |
| --- | --- | --- | --- |
| **工作區** | Working Directory | 你正在編輯的資料夾 | 你剛剛手動改的、還沒告訴 Git 的改動 |
| **暫存區** | Staging Area / Index | 「待拍照清單」 | 你已經挑好、下次 commit 要拍進去的改動 |
| **儲存庫** | Repository | 「相簿」 | 已經拍成快照、永久記錄的歷史 |

想像你在整理要寄的包裹：

- **工作區** = 你的房間，東西散落各處（你隨手改的檔案）。
- **暫存區** = 你挑出「這次要寄的東西」放進紙箱（`git add`）。
- **儲存庫** = 把紙箱封箱貼上標籤寄出，正式成為一筆記錄（`git commit`）。

```text
   工作區                暫存區               儲存庫
（你在改的檔案）  ──add──▶ （待拍照清單） ──commit──▶ （永久快照歷史）
     房間                  紙箱                  寄出的包裹
```

:::tip 為什麼要多一個「暫存區」？
新手常問：「為什麼不能改完直接存檔就好，要多一步 add？」

因為**暫存區讓你能挑選要 commit 的內容**。假設你同時改了 A 檔案（修 bug）和 B 檔案（試驗性的東西還沒好）。你可以只 `git add A`，把「修 bug」單獨 commit，B 留著慢慢弄。這讓每一個 commit 都乾淨、單一主題——這是專業工程師和新手的一大差別。
:::

## 2. 完整實戰情境：Tom、Alice、Bob

:::story Tom 的紙箱
Tom 今天改了兩個東西：修好了 `login.py` 的一個 bug，還順手在 `style.css` 試了個新顏色（但還沒確定要不要）。

他本來想全部一起 commit，Alice 提醒他：「一個 commit 只講一件事。你的 bug 修好了就先單獨寄出去，CSS 還在實驗就先別包進來。」

於是 Tom：`git add login.py`（只把修好的檔案放進紙箱）→ `git commit -m "fix: 修正登入按鈕失效"`。而 `style.css` 的改動還留在工作區，等他確定後再處理。這樣歷史紀錄清清楚楚，Alice review 時一眼就懂 Tom 這次到底做了什麼。
:::

## 3. 實際 Git 指令

**用 `git status` 隨時看檔案在哪個區域**，這是你最常打的指令：

```bash
git status
```

它會用顏色和文字告訴你：

- **Untracked files**（紅色）：Git 完全不認識的新檔案，還在工作區。
- **Changes not staged for commit**（紅色）：改過但還沒 add 的檔案（工作區）。
- **Changes to be committed**（綠色）：已經 add、在暫存區、等著被 commit。

**在三大區域之間搬東西的指令：**

```bash
# 工作區 ──▶ 暫存區（把改動放進紙箱）
git add 檔名          # 加單一檔案
git add .             # 加全部改動

# 暫存區 ──▶ 儲存庫（封箱寄出）
git commit -m "說明訊息"

# 暫存區 ──▶ 工作區（把東西從紙箱拿回房間，取消 add）
git restore --staged 檔名

# 丟棄工作區的改動（把房間裡的改動還原成上次快照的樣子，小心！）
git restore 檔名
```

:::warn `git restore 檔名` 會真的刪掉你的改動
這個指令會把檔案還原成「上一次 commit 的樣子」，你還沒 commit 的改動會消失且無法用 Git 救回。用之前先想清楚。
:::

**看快照歷史：**

```bash
git log              # 完整歷史
git log --oneline    # 每個 commit 一行，簡潔好讀（常用）
```

## 4. VS Code 圖形介面操作

VS Code 的原始碼控制面板，就是「三大區域」的視覺化版本：

:::vscode 對照三大區域
1. 按 `Ctrl+Shift+G` 打開原始碼控制面板。
2. **Changes** 區塊 = 工作區（你改了但還沒 add 的檔案）。
3. 在某個檔案上按 **`+`（Stage Changes）** = `git add`，檔案會移到上面的 **Staged Changes** 區塊（= 暫存區）。
4. 上方輸入框打訊息，按 **✓（Commit）** = `git commit`。
5. 按 **`−`（Unstage）** 就是把檔案從暫存區拿回工作區（= `git restore --staged`）。
:::

:::tip 圖形介面的最大好處：看得到 diff
在面板裡點一下任何檔案，右邊會並排顯示「改之前 vs 改之後」，綠色是新增、紅色是刪除。這比在終端機看 `git diff` 直覺非常多，強烈建議 commit 前都用這個檢查一遍自己到底改了什麼。
:::

## 5. 公司最佳實務

- **commit 前一定先看 diff**：養成「先檢查自己改了什麼，再 commit」的習慣，避免把測試用的 `print`、密碼、暫時的爛 code 一起送出去。
- **一個 commit 只做一件事**：善用暫存區挑選內容。這叫「原子性 commit（atomic commit）」，是團隊協作和事後救援的基礎。
- **常 commit、小步走**：與其一天結束才 commit 一大包，不如每完成一個小功能就 commit。快照越細，出事時越好回溯。

:::best 專業技巧：只 add 部分改動
如果同一個檔案裡，你想只 commit 其中一段改動，可以用：

```bash
git add -p 檔名
```

Git 會一段一段問你「這段要不要加入暫存？」（y/n）。這在把「一團混在一起的改動」拆成乾淨 commit 時非常好用。VS Code 裡則是選取想要的行 → 右鍵 → Stage Selected Ranges。
:::

## 6. 常見錯誤與救援方法

:::rescue 不小心 add 了不該加的檔案
還沒 commit 之前，把它從暫存區拿回來就好，改動不會消失：

```bash
git restore --staged 不小心加的檔案
```
:::

:::rescue 剛剛 commit 完，發現訊息打錯字
只要還沒 push，可以直接改最後一個 commit 的訊息：

```bash
git commit --amend -m "正確的訊息"
```
:::

:::rescue 剛剛 commit 完，發現漏了一個檔案沒加
把漏掉的檔案 add 進來，再用 `--amend` 併進上一個 commit：

```bash
git add 漏掉的檔案
git commit --amend --no-edit
```

`--no-edit` 代表沿用原本的 commit 訊息不改。
:::

:::danger 用 `git restore 檔名` 前務必確認
再強調一次：這會丟棄工作區還沒 commit 的改動，且 Git 救不回來（因為它從沒被記錄過）。不確定時，先 `git status` 看清楚，或先 commit 起來再說。
:::

:::tip 本課重點回顧
Git 有三個區域：工作區（你在改的）、暫存區（待拍照清單）、儲存庫（永久快照）。`add` 是工作區→暫存區，`commit` 是暫存區→儲存庫。`git status` 隨時告訴你檔案在哪。理解這張圖，後面所有課都會順很多。
:::
"""
},
]
