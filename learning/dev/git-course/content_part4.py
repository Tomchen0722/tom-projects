# -*- coding: utf-8 -*-
"""單元四：企業級流程（第 14-19 課）"""

PART = "單元四 · 企業級開發流程"

LESSONS = [
{
"id": "14",
"part": PART,
"title": "Pull Request 與 Code Review：公司協作的心臟",
"subtitle": "程式碼不是自己 merge，而是開 PR 請人審完再合——這是企業開發的核心儀式。",
"body": r"""
## 1. 為什麼要這樣做（原理）

在公司，你**幾乎不會**自己 `git merge` 進 main 然後 push。取而代之的流程是：

1. 在自己的 `feature` 分支開發、push 到 GitHub。
2. 開一個 **Pull Request（PR）**：正式提出「我想把這條分支合併進 main，請大家看看」。
3. 隊友做 **Code Review**：讀你的程式碼、留意見、要求修改或按讚。
4. 通過 review（可能還要 CI 測試通過）後，才在 GitHub 上按 **Merge** 合併。

**為什麼要這麼麻煩？** 因為 PR + Code Review 帶來四個公司極重視的價值：

- **品質把關**：至少有第二雙眼睛看過，減少 bug 和爛設計上線。
- **知識傳遞**：team 成員互相了解彼此在做什麼，不會有人變成「只有他懂的黑箱」。
- **可追溯**：每個改動都有討論紀錄、關聯的 issue、為什麼這樣做的理由。
- **保護主線**：搭配分支保護，沒 review 過的程式碼進不了 main。

:::tip PR 是 GitHub 的功能，不是 Git 指令
Git 本身只有 branch 和 merge。**Pull Request 是 GitHub（以及 GitLab 的 Merge Request）在 Git 之上加的協作機制。** 它把「合併」變成一個可以討論、審查、留言、跑自動測試的流程，而不只是一個指令。
:::

## 2. 完整實戰情境：Tom、Alice、Bob

:::story Tom 的第一個 PR
Tom 做完登入功能，push 了 `feature/login`。他在 GitHub 開 PR，標題 `feat: 加入使用者登入`，內文寫清楚做了什麼、怎麼測試、附上截圖，並指定 Alice 當 reviewer。

Alice 逐行看，留了三個 comment：一個指出密碼沒加密、一個建議變數改名、一個純稱讚。Tom 根據意見在同一條分支再 commit、push，PR 會**自動更新**。Alice 再看一次，按下 **Approve**。CI 測試也綠燈，Tom 按 **Squash and merge**，登入功能正式進入 main。分支自動刪除，乾淨俐落。

Bob 說：「你看，你的密碼漏洞在上線前就被擋下來了。這就是為什麼我們堅持 review。」
:::

## 3. 實際流程與指令

PR 本身在 GitHub 網站上操作，但前置的 Git 動作是：

```bash
# 1. 開分支開發
git switch -c feature/login
# ...寫程式、commit...

# 2. 推到 GitHub
git push -u origin feature/login

# 3. 到 GitHub，它會跳出 "Compare & pull request" 按鈕，點下去開 PR
#    填標題、說明、reviewer

# 4. 若 reviewer 要求修改，在同分支繼續改
git add .
git commit -m "fix: 依 review 意見加密密碼"
git push          # PR 自動更新，不用重開

# 5. 通過後在 GitHub 按 Merge，然後本地同步
git switch main
git pull
git branch -d feature/login    # 刪掉本地用完的分支
```

**GitHub 上的三種合併方式（按 Merge 時可選）：**

| 方式 | 效果 | 適合 |
| --- | --- | --- |
| **Create a merge commit** | 保留分支所有 commit + 一個 merge commit | 想保留完整開發歷史 |
| **Squash and merge** | 把整條分支壓成一個乾淨 commit | 最流行，主線歷史乾淨 |
| **Rebase and merge** | 把 commit 一直線接上，無 merge commit | 想要線性歷史又保留每個 commit |

## 4. VS Code 圖形介面操作

:::vscode 在 VS Code 裡開 PR 與做 Review
安裝官方 **GitHub Pull Requests** 擴充套件後：

1. push 分支後，VS Code 會跳出 **Create Pull Request** 按鈕，直接在編輯器裡填標題、說明、選 reviewer。
2. 左側會多一個 **GitHub** 面板，列出所有 PR。點開任一 PR 可看 diff、留言、Approve。
3. 身為 reviewer，你可以在程式碼的任一行直接留 comment，甚至用 **Suggested Change** 直接建議改法，作者一鍵就能採納。
4. 全程不用開瀏覽器，Code Review 在編輯器裡完成。
:::

## 5. 公司最佳實務

**當 PR 作者（發起者）：**

- **PR 要小**：一個 PR 專注一件事，幾百行以內最好 review。上千行的 PR 沒人想看、也看不出問題。
- **寫清楚說明**：做了什麼、為什麼、怎麼測試、影響範圍。附截圖或錄影對 UI 改動特別加分。
- **自己先 review 一遍**：開 PR 前先看自己的 diff，把 `print`、註解掉的爛 code、typo 清掉。
- **關聯 issue**：內文寫 `Closes #123`，merge 後自動關閉。

**當 Reviewer（審查者）：**

- **對事不對人**：評論程式碼，不是評論人。用「這裡建議…」而非「你怎麼又…」。
- **分清「必須改」和「建議」**：明確標示哪些是 blocking（一定要改）、哪些只是 nitpick（小建議）。
- **及時 review**：別讓隊友的 PR 卡好幾天，會拖垮整個團隊節奏。
- **看重點**：正確性、安全性、可讀性、有沒有測試。排版那種交給自動工具（formatter）。

:::best 分支保護規則（Branch Protection）
公司通常在 GitHub 設定裡把 main 設為受保護：**禁止直接 push、PR 必須至少 N 人 approve、CI 必須通過才能 merge。** 這用制度確保「沒 review、沒過測試的程式碼絕對進不了主線」，是企業品質控管的基石。
:::

## 6. 常見錯誤與救援方法

:::rescue PR 顯示一堆和我無關的 commit / 衝突
通常是你的分支落後 main 太多。把 main 的最新變動併進你的分支再 push：

```bash
git switch feature/login
git pull origin main      # 或 git rebase origin/main（見第 11 課鐵律）
# 解決衝突後
git push
```
PR 的 diff 就會乾淨，只剩你真正的改動。
:::

:::rescue Reviewer 要求改，但我已經在做別的分支
沒關係，隨時可以切回 PR 的分支修改：

```bash
git switch feature/login
# 改、commit、push，PR 會自動更新
```
不用重開 PR。
:::

:::warn 別把 review 意見當成人身攻擊
新人常對 review 意見玻璃心。心態調整：**被 review 出問題是好事，代表問題在上線前被擋下來了。** 資深工程師的程式碼一樣天天被 review、被挑錯。這是團隊互相把關，不是針對你。
:::

:::tip 本課重點回顧
企業流程：feature 分支 → push → 開 PR → Code Review → 通過 → 在 GitHub 按 Merge（常用 Squash and merge）。PR 是 GitHub 加在 Git 上的協作機制，帶來品質、知識、可追溯、保護主線四大價值。PR 要小、說明要清楚、review 對事不對人。main 用分支保護強制走這流程。
:::
"""
},

{
"id": "15",
"part": PART,
"title": "Fork 與 Upstream：參與開源專案",
"subtitle": "當你沒有某個 repo 的寫入權限，卻想貢獻程式碼時的標準做法。",
"body": r"""
## 1. 為什麼要這樣做（原理）

前一課的 PR 流程，前提是你對 repo 有**寫入權限**（能 push 分支）——這在公司內部沒問題。但如果你想貢獻一個**開源專案**（例如某個知名的 Python 套件），你當然沒有它的寫入權限，不能直接 push 分支上去。

這時的解法是 **Fork（分叉）**：把別人的 repo **複製一份到你自己的 GitHub 帳號下**，成為你能完全掌控的副本。你在自己的 fork 上開分支、開發、push，再對「原本的專案」開 PR，請維護者審核你的貢獻。

:::tip Fork vs Clone 差在哪？
- **Clone**：把 repo 下載到你**本機電腦**。
- **Fork**：把 repo 複製到你**自己的 GitHub 帳號**（雲端，還是在 GitHub 上）。

參與開源的完整鏈路是：原專案 →（Fork）→ 你的 GitHub 副本 →（Clone）→ 你的電腦。
:::

**兩個遠端：origin 與 upstream**

Fork 後你的本地會有兩個遠端：

- `origin` = **你自己的 fork**（你有寫入權限，push 到這裡）。
- `upstream` = **原本的專案**（你只能讀，用來抓它的最新更新，保持同步）。

```text
  upstream（原專案）──▶ 你 fetch 它的更新
        ▲                        │
        │ 你開 PR 貢獻回去          ▼
   origin（你的 fork）◀── 你 push ── 你的電腦
```

## 2. 完整實戰情境：Tom、Alice、Bob

:::story Tom 貢獻一個開源套件
Tom 發現一個熱門開源工具有個小 bug，想修好回饋社群。他不能直接改人家的 repo，於是：

1. 在 GitHub 按 **Fork**，得到 `tom/awesome-tool`（他自己的副本）。
2. `git clone` 他的 fork 到電腦。
3. 加一個 `upstream` 指向原專案，方便日後同步。
4. 開分支 `fix/typo-in-readme`，修好、push 到自己的 fork（origin）。
5. 到原專案開 PR：「我修好了這個 bug」。
6. 原專案維護者 review、approve、merge。Tom 的名字進入貢獻者名單。

幾週後原專案更新了很多，Tom 想再貢獻。他先從 `upstream` 拉最新的進來同步自己的 fork，才不會基於過時的程式碼開發。
:::

## 3. 實際 Git 指令

```bash
# 1. 在 GitHub 網頁按 Fork（得到你帳號下的副本），然後 clone 你的 fork
git clone https://github.com/你的帳號/awesome-tool.git
cd awesome-tool

# 2. 加上 upstream 指向「原本的專案」
git remote add upstream https://github.com/原作者/awesome-tool.git

# 3. 確認兩個遠端都在
git remote -v
#   origin    https://github.com/你的帳號/awesome-tool.git   （你的 fork）
#   upstream  https://github.com/原作者/awesome-tool.git       （原專案）

# 4. 開分支開發
git switch -c fix/typo-in-readme
# ...修改、commit...

# 5. push 到你的 fork（origin）
git push -u origin fix/typo-in-readme

# 6. 到 GitHub 開 PR：base 選原專案的 main，compare 選你的分支
```

**保持 fork 與原專案同步（重要）：**

```bash
# 抓原專案的最新變動
git fetch upstream

# 切到自己的 main，把原專案的 main 併進來
git switch main
git merge upstream/main

# 更新你 fork 的 main
git push origin main
```

:::tip GitHub 網頁有一鍵同步
現在 GitHub 在 fork 的頁面提供 **Sync fork** 按鈕，能一鍵把你的 fork 更新到和原專案一致，不用打指令。但理解上面的 upstream 流程仍很重要，尤其當你有本地改動時。
:::

## 4. VS Code 圖形介面操作

:::vscode 圖形化管理多個遠端
1. **Fork**：在 GitHub 網頁操作（VS Code 無法 fork）。
2. **加 upstream**：Source Control ⋯ → **Remote** → **Add Remote**，貼上原專案網址、命名為 `upstream`。
3. **抓 upstream 更新**：⋯ → **Fetch (All Remotes)**，就能看到 `upstream/main` 的最新狀態。
4. **開 PR 回原專案**：GitHub Pull Requests 擴充套件支援跨 fork 開 PR，選好 base repo（原專案）和你的分支即可。
:::

## 5. 公司最佳實務

- **公司內部通常不用 fork**：因為你對公司 repo 有寫入權限，直接開分支開 PR 即可（第 14 課的流程）。Fork 主要用於**開源貢獻**或**你沒有寫入權限的專案**。
- **貢獻開源前先讀 CONTRIBUTING.md**：多數開源專案有貢獻指南，規定分支命名、commit 格式、要不要先開 issue 討論。照做能大幅提高 PR 被接受的機率。
- **開發前先同步 upstream**：基於過時的程式碼開發，PR 會充滿衝突。動手前先 `fetch upstream` 並同步。
- **一個 PR 一件事**：開源維護者是志工，小而清楚的 PR 才審得動。

:::best 有些公司也用 fork 模式
少數重視權限隔離的大型組織，即使內部也採「fork-based workflow」：一般開發者只能 fork、開 PR，只有維護者能 merge。這和開源流程一模一樣。所以學會 fork/upstream，在企業和開源兩邊都用得上。
:::

## 6. 常見錯誤與救援方法

:::rescue 忘了加 upstream，fork 越來越落後
隨時可以補加：

```bash
git remote add upstream 原專案網址.git
git fetch upstream
git switch main
git merge upstream/main
```
:::

:::rescue 在自己 fork 的 main 上直接改了東西
建議 fork 的 main 保持乾淨、只用來同步 upstream，開發都在 feature 分支。若已在 main 改了，把改動移到分支：

```bash
git switch -c feature/我的改動
git switch main
git reset --hard upstream/main    # 讓 fork 的 main 回到和原專案一致
```
:::

:::warn PR 開錯方向 / base 選錯
開 PR 時注意 **base repository** 要選「原專案」、base 分支選它的 `main`；**head** 選你的 fork 和你的分支。方向搞反會變成「把原專案合併進你的 fork」。GitHub 介面上會清楚顯示「從哪裡合併到哪裡」，開之前看一眼。
:::

:::tip 本課重點回顧
沒有寫入權限想貢獻，就 Fork：原專案 →（Fork）→ 你的 GitHub 副本 →（Clone）→ 電腦。兩個遠端：origin（你的 fork，可 push）、upstream（原專案，只讀、用來同步）。開發前先 `fetch upstream` 保持同步，再開分支、push 到 origin、對原專案開 PR。公司內部通常不用 fork，開源必用。
:::
"""
},

{
"id": "16",
"part": PART,
"title": "版本號、Git Tag 與 GitHub Release 發布流程",
"subtitle": "怎麼幫專案標記 v1.0、v2.0，並在 GitHub 正式發佈一個版本。",
"body": r"""
## 1. 為什麼要這樣做（原理）

commit 有一長串 hash（`a1b2c3d`），人類記不住。當你要說「我們發布了 1.0 版」時，需要一個**好記的標記**指向「就是這個 commit 是 1.0」。這就是 **Tag（標籤）**。

Tag 是釘在某個 commit 上的**永久書籤**。和分支不同，**分支會一直往前移動，tag 釘上去就不動了**——它永遠指向那個發布時刻的快照。

**語意化版本號（Semantic Versioning, SemVer）** 是業界標準的版本命名法，格式 `主版本.次版本.修訂號`，例如 `v2.4.1`：

| 部分 | 什麼時候 +1 | 例子 |
| --- | --- | --- |
| **主版本 MAJOR** | 有破壞性變更，舊用法會壞 | `1.x.x → 2.0.0` |
| **次版本 MINOR** | 加了新功能，但向下相容 | `2.3.x → 2.4.0` |
| **修訂號 PATCH** | 只修 bug，沒新功能 | `2.4.0 → 2.4.1` |

:::tip 這就是為什麼 Conventional Commits 有用（第 6 課）
還記得 commit 的 `feat`、`fix`、`BREAKING CHANGE` 嗎？工具能據此**自動決定版本號**：有 `BREAKING CHANGE` 就升主版本、有 `feat` 就升次版本、只有 `fix` 就升修訂號。規範的 commit + tag + release，能組成全自動的發版流水線。
:::

## 2. 完整實戰情境：Tom、Alice、Bob

:::story 團隊發布 1.0
專案第一個穩定版做好了。Alice 在 main 最新的 commit 打上 tag `v1.0.0`，push 到 GitHub，然後建立一個 **GitHub Release**：附上這一版的更新說明（新功能、修了哪些 bug）、打包好的執行檔。

使用者到 Release 頁面就能下載 `v1.0.0`，也清楚知道這一版有什麼。三個月後他們發布 `v1.1.0`（加了新功能），又過陣子 `v1.1.1`（修了一個緊急 bug）。每個版本都有 tag、有 release、有說明，任何人都能精準回到任一版本。
:::

## 3. 實際 Git 指令

**建立 tag：**

```bash
# 附註型 tag（推薦，會記錄作者、日期、訊息）
git tag -a v1.0.0 -m "第一個正式版本"

# 輕量型 tag（只是個書籤，不記錄額外資訊）
git tag v1.0.0

# 幫「過去某個 commit」補打 tag
git tag -a v0.9.0 a1b2c3d -m "beta 版"
```

**查看與檢視 tag：**

```bash
git tag                    # 列出所有 tag
git tag -l "v1.*"          # 篩選
git show v1.0.0            # 看某 tag 指向的 commit 內容
```

**push tag 到 GitHub（重點：tag 不會被 `git push` 自動推上去）：**

```bash
git push origin v1.0.0     # 推單一 tag
git push origin --tags     # 推所有本地 tag
```

**刪除 tag：**

```bash
git tag -d v1.0.0                    # 刪本地
git push origin --delete v1.0.0      # 刪遠端
```

:::warn 最常見的坑：打了 tag 卻忘了 push
`git push` **不會**自動推送 tag！很多人打完 tag 以為好了，GitHub 上卻看不到。一定要另外 `git push origin --tags` 或 `git push origin v1.0.0`。
:::

## 4. GitHub Release 發布流程

Tag 是 Git 層級的書籤；**Release 是 GitHub 在 tag 之上做的「正式發佈」**，多了更新說明和可下載的檔案。

:::vscode 建立 Release 的步驟（GitHub 網頁）
1. 先確保 tag 已 push 到 GitHub（或在建 Release 時當場建立新 tag）。
2. 到 repo 頁面右側 **Releases** → **Draft a new release**。
3. 選一個 tag（或新建，如 `v1.0.0`）。
4. 填 **Release title**（如 `v1.0.0 - 首次發布`）。
5. 寫 **Release notes**：這版的新功能、修正、破壞性變更。可按 **Generate release notes** 讓 GitHub 依 PR 自動產生草稿。
6. 需要的話，把打包好的執行檔、安裝檔拖進附件區。
7. 按 **Publish release**。使用者就能在 Releases 頁看到並下載。
:::

VS Code 的 GitHub 擴充套件也能建立 tag（Git Graph 裡在 commit 上右鍵 → **Add Tag**），但完整的 Release（含 notes 和附件）通常在網頁或用 GitHub CLI（`gh release create`）做。

## 5. 公司最佳實務

- **一律用附註型 tag（`-a`）**：正式版本要記錄誰、何時、為何發布，輕量 tag 資訊太少。
- **遵守 SemVer**：讓使用者光看版號就知道升級風不風險（升主版本要小心、升修訂號很安全）。
- **每個 Release 附 CHANGELOG**：清楚列出這版的變更。用 Conventional Commits 可自動產生。
- **tag 命名一致**：團隊統一用 `v1.2.3`（帶 v）或 `1.2.3`（不帶），別混用。
- **beta / rc 版用預發布標記**：`v2.0.0-beta.1`、`v2.0.0-rc.1`，並在 GitHub Release 勾選 **pre-release**。

:::best 自動化發版：tag 觸發 CI
公司常設定「push 一個 `v*` tag 就自動觸發 GitHub Actions」：自動跑測試、打包、建立 Release、部署上線（第 19 課）。開發者只要 `git tag v1.2.0 && git push origin v1.2.0`，剩下全自動。這就是現代軟體的發版方式。
:::

## 6. 常見錯誤與救援方法

:::rescue tag 打錯 commit 或打錯版號
刪掉重打即可（本地 + 遠端都要刪）：

```bash
git tag -d v1.0.0                    # 刪本地
git push origin --delete v1.0.0      # 刪遠端
git tag -a v1.0.0 正確的commit -m "..." # 重打
git push origin v1.0.0               # 重推
```

**但若已經有人下載了那個 tag，改動 tag 是壞習慣**（他們的和你的會不一致）。已發布的版本最好別動，寧可發一個新的修訂版。
:::

:::warn 別把 tag 當分支用
tag 是不動的書籤，不能在上面開發 commit。如果你 checkout 一個 tag 想改東西，會進入 detached HEAD（第 7 課）。要基於某版本繼續開發，從那個 tag 開一條分支：`git switch -c hotfix/v1.0.1 v1.0.0`。
:::

:::tip 本課重點回顧
Tag 是釘在 commit 上不動的版本書籤，用 SemVer 命名（主.次.修訂）。`git tag -a v1.0.0 -m "..."` 建立，**記得 `git push origin --tags` 才會上 GitHub**。GitHub Release 是在 tag 之上的正式發佈，附更新說明和下載檔。搭配 Conventional Commits 和 CI 可全自動發版。
:::
"""
},

{
"id": "17",
"part": PART,
"title": "資安：別讓 API Key 與 .env 被推上 GitHub",
"subtitle": "最容易發生、後果最嚴重的新手事故，這一課教你預防與善後。",
"body": r"""
## 1. 為什麼要這樣做（原理）

把 API 金鑰、密碼、`.env` 推上 GitHub，是新手最常犯、代價最高的錯誤之一。後果可能是：

- **金錢損失**：外洩的雲端金鑰被爬蟲撿走，有人拿你的帳號狂跑運算，帳單暴增。
- **資料外洩**：資料庫密碼外流，用戶資料被竊。
- **難以善後**：就算你刪掉檔案，**Git 歷史裡仍留著那把金鑰**，任何人都能翻歷史找到。

:::danger 最重要的觀念：Git 會記住一切
Git 的核心就是「記住每個版本」。所以「commit 了機密 → 下個 commit 刪掉」**沒有用**——那把金鑰永遠留在歷史的某個 commit 裡。而且 GitHub 上有無數自動爬蟲**專門即時掃描新 push 的金鑰**，往往你 push 後幾分鐘內金鑰就被撿走了。因此唯一可靠的善後是：**假設它已外洩，立刻作廢那把金鑰。**
:::

**正確的機密管理方式**：機密永遠放在 `.env`（或環境變數），並用 `.gitignore` 排除，**絕不進版本控制**。程式從環境讀取，而不是寫死在程式碼裡。

## 2. 完整實戰情境：Tom、Alice、Bob

:::story Tom 的金鑰事故（與正確善後）
Tom 把 OpenAI 金鑰寫在 `config.py` 裡，`git push` 上了公司 repo。十分鐘後，Alice 收到 GitHub 的秘密掃描警告。

Alice 的處理順序（**注意順序**）：
1. **先作廢金鑰**：到 OpenAI 後台把那把 key 撤銷、產生新的。因為金鑰一旦 push，就當它已經外洩。
2. **再清理程式碼**：把金鑰改成從 `.env` 讀取，`.env` 加進 `.gitignore`。
3. **處理歷史**：因為只有 Tom 一人的分支且剛發生，用工具把歷史裡的金鑰清掉、強制更新。
4. **檢討預防**：開啟 repo 的 secret scanning 和 pre-commit 檢查，避免再犯。

Alice 說：「記住，發現外洩的第一件事永遠是**換金鑰**，不是刪檔案。刪檔案救不了已經外流的東西。」
:::

## 3. 實際做法與指令

**正確的機密管理（預防）：**

```gitignore
# .gitignore —— 第一件事就排除機密
.env
.env.*
!.env.example
*.pem
*.key
secrets.json
credentials.json
```

程式裡從環境變數讀取，而非寫死。Python 範例：

```python
import os
# 好：從環境變數讀
api_key = os.environ["OPENAI_API_KEY"]

# 壞：寫死在程式碼裡（絕對不要這樣）
# api_key = "sk-abc123..."
```

搭配 `python-dotenv` 讀 `.env`：

```python
from dotenv import load_dotenv
load_dotenv()                         # 讀取 .env（此檔已被 gitignore）
api_key = os.environ["OPENAI_API_KEY"]
```

同時 commit 一份**沒有真值**的範例檔給隊友參考：

```bash
# .env.example（這個可以 commit）
OPENAI_API_KEY=你的金鑰放這
DATABASE_URL=postgresql://...
```

**萬一機密已經 commit（善後）：**

```bash
# 步驟 0（最重要）：立刻到服務後台作廢外洩的金鑰、產生新的！

# 步驟 1：停止追蹤該檔案，但保留本地檔
git rm --cached .env
echo ".env" >> .gitignore
git commit -m "chore: 移除 .env 並加入 gitignore"

# 步驟 2：從「整個歷史」中徹底清除（用 git-filter-repo，較新且官方推薦）
pip install git-filter-repo
git filter-repo --path .env --invert-paths

# 步驟 3：強制更新遠端（會改寫歷史，需通知所有隊友重新 clone）
git push origin --force --all
```

:::warn 清歷史是「核彈級」操作
`filter-repo` 會改寫**整個歷史**，所有 commit hash 都變，其他人手上的 clone 全部作廢，必須重新 clone。所以：能作廢金鑰就先作廢（多數情況這就夠了），清歷史前務必和團隊溝通。個人專案較無妨，團隊專案要非常謹慎。
:::

## 4. VS Code 圖形介面操作與工具

:::vscode 用工具在「commit 之前」就攔下來
- **檔案總管顏色**：`.env` 被 gitignore 後會顯示灰色，若它是白色/綠色代表**沒被忽略、有危險**，立刻檢查 `.gitignore`。
- **commit 前看 diff**：在 Source Control 面板逐檔看 diff，養成「看到 `sk-`、`password=`、`token=` 就停手」的敏感度。
- **裝 pre-commit 掃描**：設定 **gitleaks** 或 **git-secrets** 當 pre-commit hook，commit 前自動掃描疑似金鑰，掃到就擋下 commit。這是最有效的自動防線。
:::

## 5. 公司最佳實務

- **機密一律走環境變數 / 密鑰管理服務**：像 AWS Secrets Manager、HashiCorp Vault、GitHub Actions Secrets，程式碼裡永遠不出現真值。
- **開啟 GitHub Secret Scanning**：GitHub 內建功能，會即時掃描並在偵測到金鑰時警告，公開 repo 免費。
- **強制 pre-commit hook**：全隊統一裝 gitleaks/git-secrets，從源頭防堵。
- **定期輪換金鑰**：即使沒外洩，重要金鑰也應定期更換。
- **最小權限原則**：金鑰只給必要的權限，萬一外洩傷害有限。

:::best 事故演練：如果今天金鑰外洩了，你的第一步是什麼？
標準答案永遠是：**作廢（revoke）那把金鑰，產生新的。** 清歷史、刪檔案都是次要的。把這個反射動作練起來——真的出事時，速度決定損害大小。
:::

## 6. 常見錯誤與救援方法

:::rescue 剛剛 push 了含金鑰的 commit（還沒被別人拉）
1. **立刻作廢金鑰、換新的**（假設已外洩）。
2. 若只是最後一個 commit：改掉程式碼從 env 讀 → `git rm --cached` → 用 `filter-repo` 清歷史 → `--force` 更新。
3. 開啟 secret scanning 和 pre-commit 防以後再犯。
:::

:::rescue .env 已經被追蹤，改了 .gitignore 也沒用
`.gitignore` 對已追蹤的檔案無效。要先解除追蹤（第 5 課也提過）：

```bash
git rm --cached .env
git commit -m "chore: 停止追蹤 .env"
```
:::

:::danger 別以為「私有 repo 就安全」
私有 repo 也可能因為權限誤設、成員離職、日後轉公開而外洩。**機密就是機密，不論 repo 公開與否都不該進版本控制。** 養成一致的習慣，不要賭。
:::

:::tip 本課重點回顧
機密（API Key、密碼、.env）**絕不進版本控制**，用 `.gitignore` 排除、從環境變數讀取、附 `.env.example` 給隊友。核心觀念：Git 記住一切，刪檔案救不了外洩——**外洩第一步永遠是作廢金鑰**。用 gitleaks/git-secrets 在 commit 前自動攔截，開啟 GitHub Secret Scanning。清歷史是核彈級操作，團隊專案要謹慎溝通。
:::
"""
},

{
"id": "18",
"part": PART,
"title": "Git LFS：管理大型模型、圖片與影片",
"subtitle": "為什麼大檔不能直接進 Git，以及 AI 專案怎麼正確處理權重和資料。",
"body": r"""
## 1. 為什麼要這樣做（原理）

Git 是為**文字檔（程式碼）**設計的，它擅長記錄「哪幾行改了」。但對於**大型二進位檔**（模型權重 `.safetensors`、影片、高解析圖片、資料集），Git 會出大問題：

- **每個版本都完整存一份**：你改一次 500MB 的模型，Git 就多存一整份 500MB。改十次，repo 就肥了 5GB，而且**永遠瘦不回來**（歷史裡都留著）。
- **clone 變超慢**：新成員 clone 要下載整個肥大歷史，等到天荒地老。
- **GitHub 有檔案大小限制**：單檔超過 100MB 會被 GitHub 直接拒絕 push。

**Git LFS（Large File Storage）** 就是解法。它的原理很聰明：**在 Git 裡只存一個很小的「指標檔」（幾百位元組，記錄這個大檔的雜湊值和大小），真正的大檔內容存到另外的 LFS 伺服器。** 你 checkout 時，LFS 才把對應的大檔內容抓下來。

```text
一般 Git：              Git LFS：
repo 裡直接塞 500MB      repo 裡只有 130 bytes 的指標
每版都存整份 →肥         大檔存 LFS 伺服器，只抓需要的版本
```

:::tip 一句話：Git 存指標，LFS 存內容
LFS 讓大檔「看起來在 Git 裡」，實際內容存在別的地方，repo 保持輕巧。你的日常操作（add/commit/push/pull）幾乎不變，LFS 在背後自動處理大檔。
:::

## 2. 完整實戰情境：Tom、Alice、Bob

:::story AI 專案的模型檔災難
Tom 的團隊做 AI 專案，他把訓練好的 1.2GB 模型 `model.safetensors` 直接 `git add` 進 repo。push 時 GitHub 直接拒絕（超過 100MB）。就算沒被拒，每次重新訓練換模型，repo 就多存 1.2GB，一個月後 repo 膨脹到 30GB，Bob 新來要 clone，跑了一小時還沒好。

Alice 導入 Git LFS：設定 `*.safetensors` 由 LFS 管理。從此模型檔只在 repo 留小指標，實體存 LFS。repo 回到輕巧，clone 幾秒完成，需要哪個版本的模型才抓哪個。Tom 學到：**大檔要嘛用 LFS，要嘛根本不進 Git（放雲端儲存，用連結引用）。**
:::

## 3. 實際 Git 指令

```bash
# 1. 安裝 Git LFS（一台電腦裝一次）
git lfs install

# 2. 告訴 LFS 要管理哪些類型的檔案（會寫進 .gitattributes）
git lfs track "*.safetensors"
git lfs track "*.ckpt"
git lfs track "*.pt"
git lfs track "*.psd"
git lfs track "*.mp4"

# 3. 一定要把 .gitattributes 也 commit（隊友才會套用同樣規則）
git add .gitattributes
git commit -m "chore: 設定 Git LFS 管理模型與影片檔"

# 4. 之後正常 add/commit/push 大檔，LFS 自動接管
git add model.safetensors
git commit -m "feat: 加入訓練好的模型 v1"
git push

# 查看目前被 LFS 管理的檔案
git lfs ls-files

# 查看 track 規則
git lfs track
```

`.gitattributes` 檔案內容長這樣（LFS 靠它判斷哪些檔案要用 LFS）：

```text
*.safetensors filter=lfs diff=lfs merge=lfs -text
*.mp4 filter=lfs diff=lfs merge=lfs -text
```

:::warn 順序很重要：先 track，再 add 大檔
LFS 只會接管「設定 track 之後才加入」的檔案。如果大檔在你設定 LFS **之前**就已經 commit 進普通 Git 了，光設定 track 不會把它移到 LFS，還得用 `git lfs migrate` 改寫歷史。所以最佳做法是**專案一開始就設好 LFS track**。
:::

## 4. VS Code 圖形介面操作

:::vscode LFS 與 VS Code
Git LFS 主要靠指令和 `.gitattributes` 設定，VS Code 沒有專門的 LFS 圖形介面，但：

1. 設好 LFS 後，日常在 VS Code 的 Source Control 面板 add/commit/push 大檔，LFS 會自動運作，操作和一般檔案無異。
2. 被 LFS 管理的檔案，commit 的其實是小指標檔，diff 面板會顯示 LFS 指標資訊而非二進位內容。
3. 記得確認 `.gitattributes` 有被納入版本控制（它會出現在檔案總管，別忽略它）。
:::

## 5. 公司最佳實務

- **專案初期就規劃大檔策略**：一開始就設好 LFS track，或決定「大檔一律不進 repo」。事後補救很痛。
- **三種大檔處置方式，依情況選**：
  - **Git LFS**：需要版本控制、且和程式碼綁在一起的大檔（設計稿、必要的模型）。
  - **雲端物件儲存**（S3、GCS、HuggingFace Hub）：大型資料集、模型權重，用腳本或 URL 下載，repo 只存下載連結。
  - **完全 gitignore**：訓練產生的中間檔、快取，根本不需要版本控制。
- **注意 LFS 有配額**：GitHub 的 LFS 免費額度有限（儲存空間與流量），超過要付費。大團隊要留意成本，很多 AI 團隊因此偏好用 HuggingFace / S3 而非 LFS。
- **commit `.gitattributes`**：這是 LFS 規則的來源，不 commit 的話隊友的大檔會變成普通 Git 檔。

:::best AI／ML 專案的典型分工
- 程式碼、設定、`.gitattributes` → 普通 Git。
- 少量必要的模型、設計稿 → Git LFS。
- 大型資料集、大量 checkpoint → HuggingFace Hub 或 S3，repo 只放下載腳本。
- 訓練輸出、log、快取 → `.gitignore` 直接排除。

這樣 repo 輕巧、協作順暢、成本可控。
:::

## 6. 常見錯誤與救援方法

:::rescue 大檔已經進了普通 Git，想改用 LFS
用 `git lfs migrate` 把歷史裡的大檔轉成 LFS（會改寫歷史，團隊需協調、重新 clone）：

```bash
git lfs migrate import --include="*.safetensors"
```
:::

:::rescue clone 下來大檔只有指標、不是真檔
可能是 LFS 沒裝或沒抓內容。執行：

```bash
git lfs install      # 確認 LFS 已安裝
git lfs pull         # 把 LFS 大檔的實際內容抓下來
```
:::

:::warn push 被擋：檔案超過 100MB
代表這個大檔沒走 LFS（直接進了普通 Git）。要先設好 LFS track、把該檔改由 LFS 管理（可能需 migrate 或把它從這次 commit 移除改走 LFS），再 push。GitHub 對單檔硬性上限 100MB。
:::

:::tip 本課重點回顧
Git 不適合大型二進位檔（每版存整份、會撐爆 repo、GitHub 限 100MB）。Git LFS 讓 repo 只存小指標、大檔內容存 LFS 伺服器。用 `git lfs track "*.副檔名"` 設定並**務必 commit `.gitattributes`**，最好專案一開始就設好。大檔三種選擇：LFS、雲端儲存、直接 gitignore。AI 團隊常因 LFS 配額成本改用 HuggingFace / S3。
:::
"""
},

{
"id": "19",
"part": PART,
"title": "GitHub Actions：自動測試與自動部署（CI/CD）",
"subtitle": "讓「每次 push 自動跑測試、每次發版自動部署」成真。",
"body": r"""
## 1. 為什麼要這樣做（原理）

想像每次有人 push，都要有人手動：跑一遍測試、檢查程式碼風格、打包、部署上線。既累又容易忘、容易出錯。**CI/CD** 就是把這些自動化：

- **CI（持續整合 Continuous Integration）**：每次 push 或開 PR，自動跑測試、檢查、建置。確保「進 main 的程式碼都是能動的」。
- **CD（持續部署 Continuous Deployment）**：測試通過後，自動把程式部署到伺服器 / 發佈。

**GitHub Actions** 是 GitHub 內建的 CI/CD 工具。你在 repo 裡放一個 YAML 設定檔，描述「什麼事件發生時（如 push），要在一台雲端機器上跑哪些步驟」。GitHub 就會在每次觸發時，自動開一台乾淨的機器執行它們。

```text
你 push ──▶ 觸發 GitHub Actions ──▶ 開一台雲端機器
                                    ├─ 裝環境
                                    ├─ 跑測試   ✅/❌
                                    ├─ 檢查風格
                                    └─（通過才）部署
```

:::tip 為什麼這是「企業級」的關鍵一環
CI/CD 是現代軟體團隊的標配。它讓「壞掉的程式碼進不了主線」（配合分支保護，第 14 課），讓發版從「一個人小心翼翼手動操作一小時」變成「push 一下、幾分鐘後自動上線」。理解它，你就理解了現代軟體怎麼被交付。
:::

## 2. 完整實戰情境：Tom、Alice、Bob

:::story 自動化守門員
以前 Bob 常忘了跑測試就開 PR，結果壞掉的程式碼合進 main，害大家的環境都爛掉。

導入 GitHub Actions 後：Tom 開 PR，Actions 自動在雲端跑完整測試。如果測試掛了，PR 上會出現紅色 ❌，而且分支保護規則讓它**根本無法 merge**。Tom 修好、再 push，Actions 重跑、變綠色 ✅，才能合併。合併進 main 後，另一個 Actions 自動把網站部署到正式環境。

Alice 說：「現在不需要有人當糾察隊了，機器 24 小時幫我們把關，而且從不偷懶。」
:::

## 3. 實際設定（Workflow YAML）

Workflow 檔放在專案的 `.github/workflows/` 資料夾，副檔名 `.yml`。以下是一個 **Python 專案自動測試** 的完整範例：

```yaml
# .github/workflows/ci.yml
name: CI

# 什麼時候觸發：push 到 main、或對 main 開 PR 時
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest      # 用一台乾淨的 Ubuntu 雲端機器
    steps:
      - name: 取出程式碼
        uses: actions/checkout@v4

      - name: 安裝 Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: 安裝相依套件
        run: |
          pip install -r requirements.txt

      - name: 跑測試
        run: |
          pytest

      - name: 檢查程式碼風格
        run: |
          pip install ruff
          ruff check .
```

**YAML 結構重點：**

| 欄位 | 意思 |
| --- | --- |
| `name` | 這個 workflow 的名字 |
| `on` | **觸發條件**（push、pull_request、tag、定時 schedule 等） |
| `jobs` | 要做的工作（可有多個，平行或有先後） |
| `runs-on` | 在哪種機器上跑（ubuntu / windows / macos） |
| `steps` | 一個 job 裡依序執行的步驟 |
| `uses` | 用別人寫好的現成動作（action） |
| `run` | 執行一段 shell 指令 |

**一個「push tag 就自動發版」的 CD 範例片段：**

```yaml
on:
  push:
    tags:
      - 'v*'          # 只要 push 的是 v 開頭的 tag 就觸發（呼應第 16 課）
jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: 建立 GitHub Release
        run: gh release create ${{ github.ref_name }} --generate-notes
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

:::warn 機密要用 Secrets，不要寫進 YAML
部署常需要金鑰（伺服器密碼、雲端 token）。**絕對不要寫在 YAML 裡**（它會進版本控制，等於外洩，呼應第 17 課）。要放進 GitHub repo 的 **Settings → Secrets and variables → Actions**，在 workflow 裡用 `${{ secrets.你的名稱 }}` 引用。
:::

## 4. VS Code 圖形介面操作

:::vscode 在 VS Code 管理 Actions
1. 建立 `.github/workflows/ci.yml`：VS Code 有 YAML 語法高亮，裝 **GitHub Actions** 官方擴充套件會有欄位自動完成與驗證，減少縮排錯誤。
2. 裝 **GitHub Actions** 擴充套件後，左側面板能直接看到每次 workflow 的執行結果（成功/失敗）、點進去看 log，不用開瀏覽器。
3. PR 面板（GitHub Pull Requests 擴充套件）也會顯示該 PR 的 checks 狀態（✅/❌）。
:::

:::tip YAML 對縮排極度敏感
YAML 用縮排表示層級，**只能用空格、不能用 Tab**，縮排錯一格整個檔案就壞。善用編輯器的 YAML 驗證，或參考現成範本（GitHub 在 Actions 頁面提供各語言的起手範本，一鍵套用）。
:::

## 5. 公司最佳實務

- **CI 必過才能 merge**：搭配分支保護（第 14 課），把「測試通過」設為 merge 的必要條件，這是品質底線。
- **CI 要快**：太慢的 CI 會拖垮開發節奏。善用快取（`actions/cache`）、平行 job、只跑受影響的測試。
- **典型 CI 內容**：跑測試、程式碼風格檢查（lint/format）、型別檢查、安全掃描（含第 17 課的金鑰掃描）、建置。
- **CD 要分階段**：通常先自動部署到測試環境（staging），正式環境（production）常保留人工核准的關卡，避免自動把問題直接推上線。
- **機密一律走 Secrets**：再次強調，永不寫進 YAML。

:::best CI/CD 帶來的文化改變
當「合併即自動測試、發版即自動部署」成為常態，團隊敢於頻繁、小步交付，因為每一步都有自動化保護網。這就是為什麼現代團隊能一天部署很多次，而不是幾個月才提心吊膽發一次版。CI/CD 不只是工具，是一種開發文化。
:::

## 6. 常見錯誤與救援方法

:::rescue workflow 沒有觸發
檢查：(1) 檔案路徑是否正好在 `.github/workflows/` 下；(2) 副檔名是 `.yml` 或 `.yaml`；(3) `on:` 的觸發條件是否符合你的動作（例如你 push 的分支不在 `branches` 清單裡就不會觸發）；(4) YAML 語法有沒有錯（Actions 頁面會顯示解析錯誤）。
:::

:::rescue CI 一直失敗，但本地是好的
常見原因：本地有裝但 `requirements.txt` 沒列到的套件、路徑大小寫差異（Linux 區分大小寫、Windows 不分）、環境變數本地有但 CI 沒設。看 Actions 的 log 逐步排查，通常錯誤訊息會直指問題。
:::

:::warn 部署步驟出錯把正式環境弄壞
這就是為什麼正式環境部署建議加**人工核准關卡**（GitHub Environments 的 required reviewers），以及先部署 staging 驗證。自動化很強大，但對「正式上線」這一步要保留剎車。
:::

:::tip 本課重點回顧
GitHub Actions 用 `.github/workflows/*.yml` 描述「什麼事件觸發、在雲端機器跑哪些步驟」。CI = 每次 push/PR 自動測試檢查；CD = 通過後自動部署。搭配分支保護讓壞程式碼進不了 main。機密一律放 Secrets、永不寫進 YAML。YAML 對縮排敏感、只用空格。單元四完成，你已掌握企業級開發全流程。最後一課，我們專攻「做錯了怎麼救」。
:::
"""
},
]
