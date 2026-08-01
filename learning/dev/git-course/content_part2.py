# -*- coding: utf-8 -*-
"""單元二：單人基本操作（第 4-8 課）"""

PART = "單元二 · 單人基本操作"

LESSONS = [
{
"id": "04",
"part": PART,
"title": "建立專案與你的第一個 commit",
"subtitle": "init → add → commit → log，完整走一次 Git 的日常循環。",
"body": r"""
## 1. 為什麼要這樣做（原理）

任何資料夾都能變成 Git 專案，只要在裡面執行 `git init`。這會建立一個隱藏的 `.git` 資料夾——**那就是 Git 的大腦**，所有快照、歷史、分支都存在裡面。刪掉 `.git`，這個資料夾就變回普通資料夾（歷史全消失）。

有了 `.git` 之後，你就能開始 Git 的日常循環：**改檔案 → `add` 挑選 → `commit` 拍快照**。這一課，我們把這個循環完整走一遍。

:::tip 一個專案只要 init 一次
`git init` 只在建立專案時做一次。之後你天天都在做的是 `add` 和 `commit`，不會再 init。
:::

## 2. 完整實戰情境：Tom、Alice、Bob

:::story Tom 建立第一個專案
Tom 被指派做一個小工具，放在 `C:\AI\my-tool`。他打開 VS Code、開啟這個資料夾、按 `Ctrl+~` 叫出終端機，然後：

1. `git init` —— 資料夾左下角出現 Git 標記，Tom 知道「大腦」裝好了。
2. 建立一個 `README.md`，寫下「我的第一個工具」。
3. `git status` —— Git 說 `README.md` 是紅色的 Untracked（還沒被記錄）。
4. `git add README.md` —— 放進暫存區（紙箱）。
5. `git commit -m "初始化專案"` —— 拍下第一張快照。

Tom 看著 `git log` 裡出現自己的名字和第一個 commit，有點感動。這是他工程師生涯的第一個快照。
:::

## 3. 實際 Git 指令

```bash
# 進到你的專案資料夾
cd C:\AI\my-tool

# 1. 初始化 Git（建立 .git 大腦）
git init

# 2. 建立或修改一些檔案後，看看狀態
git status

# 3. 把改動放進暫存區
git add README.md      # 加單一檔案
git add .              # 一次加全部

# 4. 拍下快照，附上說明
git commit -m "初始化專案，加入 README"

# 5. 查看歷史
git log --oneline
```

`git log --oneline` 的輸出長這樣，每一行就是一張快照：

```text
a1b2c3d (HEAD -> main) 初始化專案，加入 README
```

- `a1b2c3d` 是這個 commit 的**唯一編號**（叫 hash / SHA，實際更長，這是縮寫）。
- `HEAD -> main` 代表你現在站在 `main` 分支的最新位置。**HEAD 就是「你現在在哪」的指標。**

:::tip commit 訊息的下法（本課先簡單版）
訊息要寫「你做了什麼」，用現在式、簡潔明確。好的：`加入使用者登入功能`。壞的：`更新`、`asdf`、`改一下`。第 6 課會教業界標準的正式規範（Conventional Commits）。
:::

## 4. VS Code 圖形介面操作

:::vscode 不打指令建立第一個 commit
1. 開啟資料夾後，到原始碼控制面板（`Ctrl+Shift+G`），若還不是 Git 專案，會出現 **「Initialize Repository」** 按鈕，按下去 = `git init`。
2. 建立 / 修改檔案後，檔案會出現在 **Changes** 清單。
3. 把游標移到檔案上，按 **`+`** 加入暫存（= `git add`）。
4. 在上方訊息框輸入 commit 訊息，按 **✓ Commit**（= `git commit`）。
5. 想看歷史，安裝 GitLens 後左側會有 **Commits** 檢視，或用內建的 Timeline 面板。
:::

## 5. 公司最佳實務

- **專案第一個 commit 通常是初始化**：常見訊息如 `chore: initial commit` 或 `初始化專案`。
- **commit 訊息要能被未來的你看懂**：三個月後你翻歷史，要一眼知道每個 commit 做了什麼。
- **不要一次塞太多改動進一個 commit**：小而清楚勝過大而混亂。

:::best 建議：先建 .gitignore 再開始
很多老手在 `git init` 之後、第一次 commit 之前，會先建立 `.gitignore`（下一課的主題），避免一開始就把垃圾檔案 commit 進去。
:::

## 6. 常見錯誤與救援方法

:::rescue 在錯的資料夾 git init 了
如果你不小心在「上一層」或桌面這種大資料夾 init，會發現 Git 開始追蹤一堆不相干的東西。解法：刪掉那個誤建的 `.git` 資料夾即可（Git 追蹤能力隨之消失，你的檔案不受影響）：

```bash
# Windows（在該資料夾）
rmdir /s /q .git
# Mac / Linux / Git Bash
rm -rf .git
```
:::

:::warn `git add .` 前先看清楚
`git add .` 會把當前資料夾所有改動都加進去，包含你可能不想要的暫存檔、密碼檔。習慣先 `git status` 看一眼，或先設好 `.gitignore`。
:::

:::rescue commit 訊息打錯
還沒 push 的話：`git commit --amend -m "新訊息"` 直接改寫最後一個 commit 的訊息。
:::

:::tip 本課重點回顧
`git init` 建立專案（只做一次）；日常是 `status` → `add` → `commit` → `log` 的循環；`HEAD` 代表你現在站在哪。下一課學怎麼叫 Git「不要追蹤某些檔案」。
:::
"""
},

{
"id": "05",
"part": PART,
"title": ".gitignore 最佳實務（Python／Node／AI 專案）",
"subtitle": "教 Git 對哪些檔案「視而不見」——這是專業與業餘的分水嶺。",
"body": r"""
## 1. 為什麼要這樣做（原理）

不是所有檔案都該進版本控制。有些檔案你**絕對不想**被 commit：

- **機密**：`.env`、API 金鑰、密碼——推上 GitHub 等於公開洩漏（第 17 課會深談）。
- **自動產生的檔案**：Python 的 `__pycache__/`、Node 的 `node_modules/`（可能上萬個檔案）、編譯產物 `dist/`。
- **個人環境檔**：`.vscode/`、`.idea/`、作業系統的 `.DS_Store`、`Thumbs.db`。
- **大型資料 / 模型**：AI 專案的 `*.ckpt`、`*.safetensors`、資料集（該用 Git LFS 或雲端，第 18 課）。

`.gitignore` 就是一份「請 Git 忽略這些」的清單。放在專案根目錄，Git 讀到後，這些檔案就**不會出現在 `git status`**，也不會被 `git add .` 加進去。

:::tip 為什麼 node_modules 一定要 ignore
`node_modules` 動輒上萬檔案、數百 MB，而且可以用 `package.json` 隨時重新裝回來。把它 commit 進去會讓 repo 肥大到無法使用。所有 Node 專案第一條 ignore 規則都是它。
:::

## 2. 完整實戰情境：Tom、Alice、Bob

:::story Tom 差點釀成資安事故
Tom 做 AI 專案時，把 OpenAI 的 API 金鑰寫在 `.env` 裡。他 `git add .`、`git commit`、`git push`——金鑰就這樣上了公司 GitHub。

Alice 在 Code Review 時臉都綠了：「Tom，你的 API key 現在全公司、甚至爬蟲都看得到，要立刻換掉並移除。」原來 Tom 少做了一件事：**開專案時就建好 `.gitignore` 把 `.env` 排除**。從那天起，Tom 養成「新專案第一件事就是寫 `.gitignore`」的習慣。
:::

## 3. 實際 Git 指令與 .gitignore 寫法

在專案根目錄建立一個名為 `.gitignore` 的檔案，裡面一行一條規則：

```gitignore
# 井字號開頭是註解

# 忽略單一檔案
.env
secrets.json

# 忽略整個資料夾（結尾加斜線）
node_modules/
__pycache__/
dist/

# 忽略某副檔名的所有檔案（* 是萬用字元）
*.log
*.tmp

# 忽略所有 .env 開頭的檔案，但保留範例檔
.env*
!.env.example
```

**規則語法重點：**

| 寫法 | 意思 |
| --- | --- |
| `檔名` | 忽略這個檔案 |
| `資料夾/` | 忽略整個資料夾 |
| `*.log` | 忽略所有 `.log` 檔 |
| `!檔名` | **例外**：不要忽略這個（驚嘆號是「反悔」） |
| `/檔名` | 只忽略根目錄的這個檔案，不含子資料夾 |

**Python 專案常用 `.gitignore`：**

```gitignore
__pycache__/
*.py[cod]
.venv/
venv/
env/
.env
*.egg-info/
dist/
build/
.pytest_cache/
.ipynb_checkpoints/
```

**AI／機器學習專案額外要加：**

```gitignore
# 模型權重與大檔（該用 Git LFS 或雲端）
*.ckpt
*.pt
*.pth
*.safetensors
*.h5
*.onnx
# 資料集
data/
datasets/
*.csv
# 訓練輸出
runs/
wandb/
outputs/
checkpoints/
```

## 4. VS Code 圖形介面操作

:::vscode 用 VS Code 管理 .gitignore
1. 在檔案總管右鍵 → 新增檔案，命名為 `.gitignore`（記得前面的點）。
2. 被忽略的檔案，在檔案總管會顯示為**灰色**，一眼就知道它不受版本控制。
3. 如果你想強制加入一個被忽略的檔案，可以在該檔案上右鍵，也有相關選項；或在 Source Control 面板它不會出現，代表 ignore 生效了。
:::

:::tip 快速產生現成的 .gitignore
不用自己從零寫。[gitignore.io](https://www.toptal.com/developers/gitignore) 或 GitHub 官方的 [github/gitignore](https://github.com/github/gitignore) 有各種語言/框架的現成範本，輸入 `Python`、`Node`、`VisualStudioCode` 就能一鍵產生完整版本。
:::

## 5. 公司最佳實務

- **新專案第一件事就建 .gitignore**：在第一個 commit 之前。
- **提供 `.env.example`**：把 `.env` 忽略，但 commit 一份 `.env.example`（只有欄位名、沒有真值），讓隊友知道需要設定哪些變數。
- **團隊統一範本**：公司常有標準 `.gitignore`，新專案直接沿用，避免有人漏掉。

:::best 個人偏好放到 global gitignore
像 `.DS_Store`（Mac）、`Thumbs.db`（Windows）這種「你個人環境的垃圾」，不該塞進每個專案的 `.gitignore`（因為那是團隊共用的）。改用**全域忽略**：

```bash
git config --global core.excludesfile ~/.gitignore_global
```

然後把個人垃圾寫進 `~/.gitignore_global`，只影響你自己。
:::

## 6. 常見錯誤與救援方法

:::danger 最經典的坑：檔案已經被 commit 過，.gitignore 沒用了
`.gitignore` **只對「還沒被 Git 追蹤過」的檔案有效**。如果 `.env` 已經被 commit 過一次，之後才加進 `.gitignore`，Git 仍會繼續追蹤它。

**救援方法**——把它從 Git 追蹤中移除，但保留你電腦上的實體檔案：

```bash
# --cached 代表「只從 Git 移除，別刪我電腦上的檔案」
git rm --cached .env
git commit -m "chore: 停止追蹤 .env"
```

之後 `.env` 就會被 `.gitignore` 正常忽略。
:::

:::danger 若機密已經 push 到 GitHub
只是 `git rm --cached` 還不夠——**歷史裡仍留著那把金鑰**，任何人都能翻歷史找到。正確做法是：**立刻把那把金鑰作廢並重新產生一把**，再處理歷史。第 17 課會完整教這個資安事故的處理流程。
:::

:::warn 忽略規則沒生效？
檢查三件事：(1) 檔名是不是正好叫 `.gitignore`（不是 `gitignore.txt`）；(2) 檔案是不是已經被追蹤過（見上面的 `git rm --cached`）；(3) 規則路徑對不對。可用 `git check-ignore -v 檔名` 查是哪條規則生效或為何沒生效。
:::

:::tip 本課重點回顧
`.gitignore` 讓 Git 忽略機密、自動產生檔、大檔。**新專案第一件事就建它**。最大的坑是「已經追蹤過的檔案 ignore 不掉」，要用 `git rm --cached` 解除。機密若已上傳，光刪不夠，要換金鑰。
:::
"""
},

{
"id": "06",
"part": PART,
"title": "Commit Message 撰寫規範：Conventional Commits",
"subtitle": "讓每一則 commit 訊息都專業、可讀、甚至能自動產生更新日誌。",
"body": r"""
## 1. 為什麼要這樣做（原理）

`git log` 是團隊的「專案日記」。如果訊息都是 `更新`、`修改`、`fix bug`、`asdf`，這本日記等於廢紙——沒人知道每個 commit 到底做了什麼。

**Conventional Commits** 是業界最廣泛採用的 commit 訊息規範。它規定訊息開頭要用一個「類型」標籤，格式如下：

```text
類型(範圍): 簡短描述

（空一行）
可選的詳細說明

（空一行）
可選的頁尾，例如關聯的 issue 編號
```

例如：`feat(auth): 加入 Google 第三方登入`。

**為什麼值得這樣做？**

- **一眼看懂**：`fix` 是修 bug、`feat` 是新功能，掃過去就知道每個 commit 的性質。
- **可自動化**：工具能根據這些標籤**自動產生 CHANGELOG（更新日誌）** 和**自動決定版本號**。
- **團隊一致**：不會每個人各寫各的風格。

## 2. 完整實戰情境：Tom、Alice、Bob

:::story 兩本專案日記
Bob 的 `git log`：`更新`、`改一下`、`又改`、`修好了`、`test`。三個月後要找「登入功能是哪個 commit 加的」，Bob 翻了半小時還找不到。

Tom 改用 Conventional Commits 後的 `git log`：

```text
feat(auth): 加入 Google 登入
fix(auth): 修正登入後導向錯誤頁面
docs(readme): 補充環境設定說明
refactor(api): 抽出共用的請求函式
```

Alice 一眼就能篩出所有 `feat`（新功能）給主管看這個 sprint 做了什麼。這就是規範的價值。
:::

## 3. 常用類型與實際指令

**核心類型（背這幾個就夠用）：**

| 類型 | 用在什麼時候 | 範例 |
| --- | --- | --- |
| `feat` | 新增功能 | `feat: 加入購物車功能` |
| `fix` | 修正 bug | `fix: 修正結帳金額計算錯誤` |
| `docs` | 只改文件 | `docs: 更新 API 使用說明` |
| `style` | 排版、空白、分號（不影響邏輯） | `style: 統一縮排為 4 空格` |
| `refactor` | 重構（不改功能也不修 bug） | `refactor: 拆分過長的函式` |
| `test` | 新增或修改測試 | `test: 補上登入的單元測試` |
| `chore` | 雜務（設定、相依套件、建置） | `chore: 升級 React 到 18` |
| `perf` | 效能優化 | `perf: 快取查詢結果減少資料庫負載` |

**實際下 commit：**

```bash
# 最常用：一行搞定
git commit -m "feat: 加入使用者個人頁面"

# 帶範圍（scope），標明改動的模組
git commit -m "fix(cart): 修正數量無法歸零的問題"

# 需要詳細說明時，不加 -m 會打開編輯器讓你寫多行
git commit
```

多行訊息的完整範例：

```text
feat(auth): 加入雙因素驗證 (2FA)

使用者可在設定頁啟用 2FA，登入時需輸入
驗證器 App 產生的六位數驗證碼。

Closes #142
```

:::tip 破壞性變更（Breaking Change）
如果你的改動會讓舊用法失效，要特別標示，在類型後加 `!` 或在頁尾寫 `BREAKING CHANGE:`：

```text
feat(api)!: 移除舊版 /v1 端點

BREAKING CHANGE: /v1/users 已停用，請改用 /v2/users
```

自動版號工具看到這個，就知道要升「主版號」（第 16 課會談版本號）。
:::

## 4. VS Code 圖形介面操作

:::vscode 在 VS Code 寫規範的 commit
1. Source Control 面板上方的訊息框，就是打 commit 訊息的地方，直接輸入 `feat: xxx` 即可。
2. 想寫多行詳細說明？點訊息框旁的展開，或直接不填、按 commit，會跳出編輯器讓你寫完整訊息（前提是第 2 課設過 `core.editor "code --wait"`）。
3. 安裝擴充套件 **Conventional Commits**：它會用選單引導你選類型、填 scope、寫描述，對新手很友善，不用死記格式。
:::

## 5. 公司最佳實務

- **描述用祈使句、現在式**：「加入登入」而非「加入了登入」或「將加入登入」。想像它在補完「這個 commit 會…」。
- **第一行控制在 50 字內**：簡短、切中重點；細節留給下面的內文。
- **關聯 issue**：頁尾寫 `Closes #123`，merge 後 GitHub 會自動關閉那個 issue。
- **團隊會用工具強制檢查**：很多公司用 `commitlint` + Git hook，訊息不符規範根本 commit 不了。

:::best 為什麼老闆也在乎這件事
規範的 commit 能自動產生**發布更新日誌（CHANGELOG）**，也能讓 `semantic-release` 這類工具**自動決定版本號並發佈**。也就是說，好的 commit 訊息直接省下團隊每次發版的手動工——這是實打實的生產力。
:::

## 6. 常見錯誤與救援方法

:::rescue 上一個 commit 訊息沒照規範
只要還沒 push：

```bash
git commit --amend -m "feat: 正確的規範訊息"
```
:::

:::rescue 想批次改寫前幾個 commit 的訊息
如果有好幾個 commit 訊息要改（且還沒 push 或團隊允許），用互動式 rebase：

```bash
# 改寫最近 3 個 commit
git rebase -i HEAD~3
```

編輯器會列出這 3 個 commit，把想改的那行前面的 `pick` 改成 `reword`，存檔關閉後 Git 會逐一讓你改訊息。**注意：這會改寫歷史，已 push 且多人共用的分支要小心（第 11、20 課詳談）。**
:::

:::warn 不要為了規範而規範
類型選不出來時，別卡住。八成情況不是 `feat` 就是 `fix`，其餘用 `chore`。重點是「訊息能讓人看懂你做了什麼」，格式是為此服務的工具，不是目的。
:::

:::tip 本課重點回顧
Conventional Commits = `類型(範圍): 描述`。核心類型記 `feat`、`fix`、`docs`、`refactor`、`chore`、`test`。它讓歷史可讀、可自動產生 CHANGELOG 與版號。訊息打錯用 `--amend`（單一）或 `rebase -i`（多個）修正。
:::
"""
},

{
"id": "07",
"part": PART,
"title": "查看歷史、比較差異、還原檔案",
"subtitle": "log、diff、restore、checkout——安全地在時間線上來回穿梭。",
"body": r"""
## 1. 為什麼要這樣做（原理）

Git 最大的價值之一，是**你隨時可以問它「這裡到底改了什麼」和「帶我回到過去某個版本」**。這一課教你四種穿梭時間的能力：

- **看歷史**（`git log`）：這條時間線上有哪些快照。
- **比差異**（`git diff`）：兩個時間點之間，到底改了哪幾行。
- **還原檔案**（`git restore`）：把某個檔案退回過去的樣子。
- **看舊版本**（`git checkout 舊commit`）：整個專案暫時跳回過去看看。

理解「Git 把每個版本都完整存著」，你就會明白：**回到過去不是奇蹟，是 Git 的本分。**

## 2. 完整實戰情境：Tom、Alice、Bob

:::story 「昨天還好好的，今天壞了」
Tom 的程式今天突然壞掉，但他不記得改了什麼。Alice 教他：「用 `git log` 看看今天的 commit，再用 `git diff` 比對昨天能動的版本和現在，差異一目了然。」

Tom 一比，發現自己昨晚手滑刪掉了一行關鍵設定。他用 `git restore` 把那個檔案退回昨天的版本，程式立刻復活。整個過程不到兩分鐘——這在沒有 Git 的年代是不可能的。
:::

## 3. 實際 Git 指令

**看歷史：**

```bash
git log                    # 完整歷史（按 q 離開）
git log --oneline          # 每個 commit 一行（最常用）
git log --oneline --graph  # 加上分支圖形
git log -3                 # 只看最近 3 個
git log --author="Tom"     # 只看 Tom 的 commit
git log 檔名               # 只看某檔案的歷史
```

**比差異：**

```bash
git diff                   # 工作區 vs 暫存區（還沒 add 的改動）
git diff --staged          # 暫存區 vs 上次 commit（已 add、將被 commit 的）
git diff HEAD              # 工作區 vs 上次 commit（所有還沒 commit 的改動）
git diff a1b2c3d HEAD      # 某個舊 commit 和現在的差異
git diff main feature      # 兩個分支的差異
```

diff 的讀法：`-` 開頭紅色行是「刪掉的」，`+` 開頭綠色行是「新增的」。

**還原檔案（退回過去的樣子）：**

```bash
# 丟棄工作區某檔案還沒 commit 的改動（退回上次 commit）
git restore 檔名

# 把某檔案退回「特定 commit」時的樣子
git restore --source=a1b2c3d 檔名
```

**整個專案跳回過去看看（唯讀地參觀歷史）：**

```bash
# 跳到某個舊 commit（會進入 detached HEAD 狀態）
git checkout a1b2c3d

# 看完要回到最新版
git switch -    # 或 git checkout main
```

:::warn checkout 舊 commit 會進入 "detached HEAD"
跳到舊 commit 時，Git 會警告你進入「detached HEAD（分離頭指標）」狀態——意思是「你正站在歷史中間，不在任何分支上」。**這時只是參觀，別急著改東西**。看完用 `git switch main` 回到最新即可。若真的想從這個舊點開新分支開發，用 `git switch -c 新分支名`。
:::

## 4. VS Code 圖形介面操作

:::vscode 圖形化看歷史與差異（超直覺）
1. **看單一檔案改了什麼**：在 Source Control 面板點該檔案，右側並排顯示前後對照，紅刪綠增，比終端機清楚太多。
2. **看整份歷史**：安裝 **GitLens** 後，左側有 **Commits / File History** 檢視，點任一 commit 就能看它改了什麼。
3. **逐行追溯**：GitLens 會在每行程式碼尾端淡淡顯示「這行是誰哪個 commit 改的」，點下去看完整 commit——查「這行為什麼長這樣」神器。
4. **還原檔案**：在 Source Control 面板某個改動的檔案上右鍵 → **Discard Changes**（= `git restore`）。
5. **Timeline 面板**：檔案總管下方的 Timeline 會列出該檔案的所有版本，點兩個版本即可比對。
:::

## 5. 公司最佳實務

- **除錯先看 diff 和 log**：「什麼時候壞的、誰改的、改了什麼」通常 `git log` + `git diff` 就能回答，不用瞎猜。
- **善用 `git blame` 追來源**：`git blame 檔名` 會標出每一行的最後修改者與 commit，是理解陌生程式碼的利器（VS Code 的 GitLens 把它變得無痛）。
- **參觀歷史別亂改**：detached HEAD 下的改動很容易遺失，要開發就先開分支。

:::best 進階：git bisect 二分搜尋找出問題 commit
當「不知道哪個 commit 弄壞的」而歷史又很長時，`git bisect` 能用二分法幫你快速定位：你標一個「好」的舊版和「壞」的新版，Git 自動幫你跳到中間，你測試後回答好或壞，幾步就能找到罪魁禍首。這在大型專案除錯非常強大。
:::

## 6. 常見錯誤與救援方法

:::rescue 用 restore 丟棄了不該丟的改動
如果改動**從沒 commit 過**，`git restore` 丟掉後 Git 救不回來（它沒被記錄）。所以不確定時，寧可先 commit 起來。若改動**曾經 commit 過**，一定能從 `git log` / `git reflog` 找回來。這也是「常 commit」的好處——commit 過的東西幾乎都能救。
:::

:::rescue checkout 舊版後回不去了 / 找不到最新
別慌，用：

```bash
git switch main      # 回到 main 分支最新狀態
```

如果剛剛在 detached HEAD 改了東西還想留下，先 `git switch -c 暫存分支` 把它保存成分支，再處理。
:::

:::warn 新舊指令對照
Git 較新的版本把老指令 `git checkout` 的功能拆成兩個更清楚的指令：`git switch`（切換分支）和 `git restore`（還原檔案）。老教學裡的 `git checkout 檔名`＝`git restore 檔名`；`git checkout 分支`＝`git switch 分支`。兩套都能用，本教材優先教新的、比較不會誤用。
:::

:::tip 本課重點回顧
`git log` 看歷史、`git diff` 比差異、`git restore` 還原檔案、`git switch/checkout` 切換版本。除錯的黃金組合是 log + diff + blame。VS Code + GitLens 讓這一切變得無痛。記住：commit 過的幾乎都救得回來。
:::
"""
},

{
"id": "08",
"part": PART,
"title": "VS Code 圖形介面完整操作（不背指令也能用 Git）",
"subtitle": "把前面學的所有操作，用滑鼠完整走一遍。",
"body": r"""
## 1. 為什麼要這樣做（原理）

指令強大，但日常 90% 的 Git 操作，用 VS Code 圖形介面點一點更快、更不容易出錯，而且**看得到自己在做什麼**。很多資深工程師平時都用圖形介面 commit，只有遇到複雜情況才回到終端機。

這一課把前面幾課的操作——init、add、commit、看 diff、看歷史、切分支、push/pull——用圖形介面**完整整合走一遍**，讓你就算暫時記不住指令，也能獨立作業。

:::tip 圖形介面 vs 指令，該學哪個？
兩個都要，但順序是：**先用圖形介面建立直覺，再用指令理解底層。** 因為圖形介面按鈕的背後就是這些指令，理解指令後你會更懂每個按鈕在做什麼，遇到按鈕做不到的複雜情況也不會卡死。
:::

## 2. 完整實戰情境：Tom、Alice、Bob

:::story Tom 的一天，全用滑鼠
Tom 早上開工：VS Code 拉最新的程式（Pull）→ 開新分支寫功能 → 邊寫邊在 Source Control 面板看自己改了哪些行 → 挑選要的改動 Stage → 打規範的 commit 訊息 → Commit → Push 到 GitHub → 開 Pull Request 請 Alice review。

整個流程 Tom 一行指令都沒打，全靠 VS Code 的按鈕。他心裡清楚每個按鈕對應哪個指令，所以就算哪天按鈕不夠用，他也能切回終端機。這就是「圖形介面打底、指令墊底」的理想狀態。
:::

## 3. 圖形介面 ↔ 指令對照表

這張表是本課精華，把你會用到的每個按鈕對應到指令：

| VS Code 操作 | 等於指令 | 在哪裡 |
| --- | --- | --- |
| Initialize Repository | `git init` | Source Control 面板 |
| 檔案上的 `+`（Stage Changes） | `git add 檔名` | Changes 清單 |
| `−`（Unstage Changes） | `git restore --staged` | Staged Changes 清單 |
| Discard Changes（垃圾桶↩） | `git restore 檔名` | Changes 清單 |
| 打訊息 + ✓（Commit） | `git commit -m` | 面板上方 |
| Sync Changes / ↻ | `git pull` + `git push` | 狀態列左下 |
| ⋯ 選單 → Push | `git push` | 面板選單 |
| ⋯ 選單 → Pull | `git pull` | 面板選單 |
| 左下角分支名 → 點它 | `git switch` / `git branch` | 狀態列 |
| Create Branch | `git switch -c 新分支` | 分支選單 |

## 4. VS Code 圖形介面操作（逐步）

:::vscode 完整流程演練
**A. 每天開工：拉最新程式**
點左下狀態列的**同步圖示（↻）**，或 Source Control 面板 ⋯ → Pull。這會把 GitHub 上隊友的最新改動拉下來。

**B. 開一條新分支再開始寫**
點左下角的**分支名稱**（例如顯示 `main`）→ 選 **Create new branch** → 命名如 `feature/login` → Enter。你現在就在新分支上了。

**C. 邊寫邊看自己改了什麼**
每改一個檔案，Source Control 面板的 **Changes** 就會列出它。點它看並排 diff（綠增紅刪），commit 前務必掃一遍。

**D. 挑選並暫存改動**
確認無誤的檔案，按 **`+`** 移到 Staged Changes。想只加檔案裡的某幾行？選取那幾行 → 右鍵 → **Stage Selected Ranges**。

**E. 寫訊息並 commit**
上方訊息框輸入 `feat: 加入登入頁`，按 **✓ Commit**。

**F. 推上 GitHub**
按 **Sync Changes**（或 ⋯ → Push）。第一次推新分支時，VS Code 會問要不要 publish（發佈）分支到 GitHub，按確定即可。

**G. 開 Pull Request**
安裝官方擴充套件 **GitHub Pull Requests**，push 後 VS Code 會跳出 **Create Pull Request** 按鈕，填標題與說明就能直接在編輯器裡開 PR（第 14 課詳談）。
:::

:::tip 三個必裝擴充套件
1. **GitLens** — 逐行歷史、blame、強大的歷史檢視。
2. **GitHub Pull Requests** — 在 VS Code 裡開 PR、做 Code Review。
3. **Git Graph** — 用漂亮的圖形顯示所有分支與 commit 的關係，看多分支專案神器。
:::

## 5. 公司最佳實務

- **commit 前一定用 diff 面板檢查**：圖形介面讓這件事變得零成本，沒理由不做。
- **善用 Git Graph 看分支全貌**：多人協作時，一張圖勝過想像。
- **圖形介面處理不了的，回終端機**：像互動式 rebase、cherry-pick、reflog 救援這類，指令仍是最可靠的。**別排斥終端機，它是你的安全網。**

:::best 團隊建議：統一工具但尊重習慣
公司通常不強制用哪個 Git 客戶端（VS Code、SourceTree、GitHub Desktop、純指令都行），但會要求**結果一致**：規範的 commit、正確的分支、乾淨的歷史。工具是手段，紀律才是重點。
:::

## 6. 常見錯誤與救援方法

:::rescue 按錯 Discard，改動不見了
Discard Changes = `git restore`，會丟棄還沒 commit 的改動。若那些改動從沒 commit 過，就救不回來。**預防勝於治療：養成小步 commit 的習慣。** VS Code 較新版本刪除前會有確認提示，別無腦按確定。
:::

:::rescue Sync 之後出現一堆衝突紅字
代表你和隊友改到同一個地方，需要解衝突。別怕，VS Code 有內建的衝突解決介面（Accept Current / Incoming / Both），第 10 課會完整教。
:::

:::warn 找不到某個按鈕？
VS Code 的 Git 按鈕會依情境出現（例如沒改東西時就沒有 Stage 按鈕）。找不到功能時，點 Source Control 面板右上的 **⋯（更多動作）**，幾乎所有 Git 指令都在那個選單裡。
:::

:::tip 本課重點回顧
VS Code 圖形介面能完成日常 90% 的 Git 操作：pull → 開分支 → 看 diff → stage → commit → push → 開 PR。每個按鈕背後都是一個指令（記住對照表）。三個必裝：GitLens、GitHub Pull Requests、Git Graph。複雜情況再回終端機。單元二完成，你已能獨立單人開發，下一單元進入多人協作的核心：分支。
:::
"""
},
]
