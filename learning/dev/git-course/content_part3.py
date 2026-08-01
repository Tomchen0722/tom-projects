# -*- coding: utf-8 -*-
"""單元三：分支與遠端協作（第 9-13 課）"""

PART = "單元三 · 分支與遠端協作"

LESSONS = [
{
"id": "09",
"part": PART,
"title": "分支 Branch：多人協作的核心",
"subtitle": "為什麼有了分支，三個人才能同時開發不打架。",
"body": r"""
## 1. 為什麼要這樣做（原理）

到目前為止，你的所有 commit 都排在同一條線上（`main`）。但真實團隊不是這樣運作的——**如果三個人都直接往 main 塞 commit，會亂成一團，而且任何人推一個半成品就會弄壞大家的主線。**

**分支（branch）** 就是解法。它讓你從主線「分岔」出一條平行時間線，在上面安心開發，完成、測試、review 之後，再合併回主線。

:::tip 分支的本質：一個超輕量的指標
很多人以為分支是「複製一份程式碼」，其實不是。**一個分支只是一個指向某個 commit 的指標（37 個位元組）**，所以 Git 建分支、切分支快到幾乎瞬間。`HEAD` 則是「你現在站在哪個分支」的指標。理解這點，分支就不神秘了。
:::

```text
             （feature/login 分支）
              o---o---o
             /
  o---o---o---o---o   （main 主線）
                  ↑
                HEAD（你在這）
```

**每個功能開一條分支**，是所有現代團隊的基本工作方式。你不會在 main 上直接開發，而是：從 main 開一條 `feature/xxx` → 在上面做完 → 合併回 main。

## 2. 完整實戰情境：Tom、Alice、Bob

:::story 三人三分支，互不干擾
專案要同時做三件事。三人各開一條分支：

- Tom：`git switch -c feature/login`（做登入）
- Alice：`git switch -c feature/cart`（做購物車）
- Bob：`git switch -c fix/header-bug`（修一個 bug）

三人在各自的分支上盡情 commit，完全不影響彼此，也不影響 main。Bob 的 bug 先修好，先合併回 main；Tom、Alice 隨後也各自完成、合併。main 始終保持「可運作」的狀態，因為半成品都在分支上，不會污染主線。
:::

## 3. 實際 Git 指令

```bash
# 看目前有哪些分支（* 是你現在所在的）
git branch

# 建立並切換到新分支（一步到位，最常用）
git switch -c feature/login
# 舊寫法：git checkout -b feature/login

# 只建立、不切換
git branch feature/login

# 切換到已存在的分支
git switch main
# 舊寫法：git checkout main

# 切回上一個待過的分支
git switch -

# 改分支名稱（改目前所在分支）
git branch -m 新名字

# 刪除已合併的分支
git branch -d feature/login

# 強制刪除未合併的分支（小心！會丟掉還沒合併的 commit）
git branch -D feature/login
```

:::tip 切分支前記得先處理好手上的改動
如果你有還沒 commit 的改動，切分支可能被擋下來或把改動帶著跑。乾淨的做法：切分支前先 commit，或用 `git stash` 暫存（第 12 課）。養成「切分支前先 `git status` 看一眼」的習慣。
:::

## 4. VS Code 圖形介面操作

:::vscode 用滑鼠管理分支
1. **看/切分支**：點左下角**狀態列的分支名稱**，會跳出所有分支清單，選一個就切過去。
2. **開新分支**：同一個選單裡選 **Create new branch**，輸入名稱。
3. **看分支全貌**：安裝 **Git Graph** 擴充套件，能用圖形看到所有分支怎麼分岔、怎麼合併，多分支專案必備。
4. **刪分支**：Git Graph 裡在分支上右鍵 → Delete Branch。
:::

## 5. 公司最佳實務

**分支命名規範**——公司通常有固定格式，讓人一看就懂分支目的：

| 前綴 | 用途 | 範例 |
| --- | --- | --- |
| `feature/` | 新功能 | `feature/user-profile` |
| `fix/` 或 `bugfix/` | 修 bug | `fix/login-redirect` |
| `hotfix/` | 緊急修正上線問題 | `hotfix/payment-crash` |
| `refactor/` | 重構 | `refactor/api-layer` |
| `chore/` | 雜務 | `chore/update-deps` |
| `docs/` | 文件 | `docs/api-guide` |

- **常見完整慣例**：`feature/1234-user-login`（加上 issue 編號，方便追溯）。
- **用小寫加連字號**：`feature/user-login`，不要空格或中文。
- **main 永遠保持可運作**：不直接在 main 開發，一律開分支。
- **分支要短命**：一條分支專注一件事，做完盡快合併並刪除，不要放到長滿灰塵、跟 main 差異巨大到難以合併。

:::best 兩種常見的團隊分支策略
- **GitHub Flow（最流行、最簡單）**：只有一條長期分支 `main`，每個功能開短命的 `feature/*` 分支，透過 Pull Request 合併回 main，合併即部署。適合大多數團隊與持續部署。
- **Git Flow（較複雜、較舊）**：有 `main`、`develop` 兩條長期分支，外加 `feature/*`、`release/*`、`hotfix/*`。適合有明確版本發布週期的產品。

新手先掌握 GitHub Flow 就夠用了。
:::

## 6. 常見錯誤與救援方法

:::rescue 不小心在 main 上開發了
你本該開分支卻直接在 main 上 commit 了。別怕，把這些 commit「搬」到新分支即可：

```bash
# 假設你在 main 上多 commit 了東西，還沒 push
git switch -c feature/我剛做的東西   # 從現在位置開新分支（改動跟過來）
git switch main                      # 回到 main
git reset --hard origin/main         # 把 main 退回和遠端一致（乾淨）
git switch feature/我剛做的東西       # 回到新分支繼續
```

若不確定，先問隊友，別對已 push 的 main 亂用 `reset --hard`。
:::

:::rescue 刪錯分支了
用 `-d` 刪掉的分支若還沒被合併，Git 其實會擋下來提醒你。萬一你用 `-D` 強制刪了，commit 通常還能從 `git reflog` 找回來，再重建分支：

```bash
git reflog                      # 找到被刪分支最後的 commit hash
git switch -c 分支名 a1b2c3d     # 用那個 hash 重建分支
```
:::

:::warn 分支跟 main 差太多會很難合併
分支活太久、跟 main 差異越來越大，合併時衝突會越多。解法：**定期把 main 的最新變動併回你的分支**（`git merge main` 或 `git rebase main`），保持同步，別讓分支孤立太久。
:::

:::tip 本課重點回顧
分支是輕量指標，讓多人平行開發互不干擾。`git switch -c 名稱` 開新分支、`git switch` 切換。命名用 `feature/`、`fix/` 等前綴。main 永遠保持可運作、開發一律開分支、分支要短命。下一課學怎麼把分支「合併」回來。
:::
"""
},

{
"id": "10",
"part": PART,
"title": "合併 Merge 與解決衝突 Merge Conflict",
"subtitle": "把分支的成果併回主線，並學會冷靜處理「衝突」這件新手最怕的事。",
"body": r"""
## 1. 為什麼要這樣做（原理）

功能在分支上做完了，要讓它進入主線，就要**合併（merge）**。合併就是「把某分支的改動，融合進你目前所在的分支」。

大多數時候，Git 會自動完成合併，你什麼都不用做。但當**兩個分支改到「同一個檔案的同一行」**，Git 無法判斷該聽誰的，就會停下來說：「這裡我不敢決定，你來。」——這就是**合併衝突（merge conflict）**。

:::tip 衝突不是錯誤，是 Git 在保護你
新手看到 CONFLICT 會嚇到，以為壞了。其實相反：**衝突代表 Git 很負責，它寧可停下來問你，也不願自作主張蓋掉某個人的心血。** 解衝突就是「告訴 Git 這幾行最後要長怎樣」，是完全正常的日常操作。
:::

**兩種合併方式：**

- **Fast-forward（快轉）**：如果主線從你分岔後就沒動過，合併只是把 main 指標往前移，不產生新 commit。
- **三方合併（產生 merge commit）**：如果兩邊都有新 commit，Git 會做一個「合併 commit」把兩條線接起來。

## 2. 完整實戰情境：Tom、Alice、Bob

:::story Tom 與 Bob 撞在同一行
Tom 在 `feature/login` 把首頁標題從 `歡迎` 改成 `歡迎登入`。同時 Bob 在 `main` 把同一行改成 `歡迎光臨`。

Bob 先合併進 main。輪到 Tom 要把他的分支合併時，Git 發現同一行有兩種版本，跳出衝突。Tom 打開檔案，看到 Git 用特殊記號標出「你的版本」和「Bob 的版本」，他和 Bob 討論後決定用 `歡迎登入`，刪掉記號、留下正確內容、commit，衝突解決。

Alice 說：「看，衝突沒有很可怕吧？它只是要你們兩個人類決定該聽誰的，因為機器不知道。」
:::

## 3. 實際 Git 指令

**基本合併流程：**

```bash
# 1. 先切到「要接收改動」的分支（通常是 main）
git switch main

# 2. 先確保 main 是最新的（多人協作時）
git pull

# 3. 把 feature 分支合併進來
git merge feature/login

# 4. 合併完、確認沒問題，刪掉用完的分支
git branch -d feature/login
```

**遇到衝突時，Git 會這樣提示：**

```text
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
```

打開衝突的檔案，你會看到 Git 插入的記號：

```text
<<<<<<< HEAD
歡迎光臨          （這是目前分支 main 的版本，Bob 的）
=======
歡迎登入          （這是要併進來 feature/login 的版本，Tom 的）
>>>>>>> feature/login
```

**解衝突三步驟：**

```bash
# 1. 編輯檔案：刪掉 <<<<<<<、=======、>>>>>>> 三行記號，
#    只留下你最終要的內容（可以是其中一邊，或兩邊融合）

# 2. 告訴 Git 這個檔案解好了
git add index.html

# 3. 完成合併
git commit         # 會自動帶好合併訊息，直接存檔即可
```

:::warn 解衝突時務必刪乾淨那三行記號
`<<<<<<<`、`=======`、`>>>>>>>` 這三種記號**一定要全部刪掉**，只留真正要的程式碼。忘了刪會讓程式語法錯誤。解完後搜尋一下專案還有沒有殘留的 `<<<<<<<`，是很好的習慣。
:::

**想放棄這次合併、回到合併前？**

```bash
git merge --abort     # 取消合併，回到乾淨的合併前狀態
```

## 4. VS Code 圖形介面操作

:::vscode VS Code 的衝突解決介面（比手改記號好用太多）
發生衝突時，VS Code 會把衝突的檔案標紅，打開後每一段衝突上方會出現四個藍色小按鈕：

- **Accept Current Change**：採用目前分支（HEAD）的版本。
- **Accept Incoming Change**：採用要併進來的版本。
- **Accept Both Changes**：兩邊都留。
- **Compare Changes**：並排比較兩邊。

點一下就解決一段，不用手動刪記號。全部解完後，到 Source Control 面板把檔案 Stage、Commit 即可。VS Code 還有 **Merge Editor**（三欄式：左邊你的、右邊對方的、中間結果），對複雜衝突特別清楚。
:::

## 5. 公司最佳實務

- **合併前先更新目標分支**：合併進 main 前先 `git pull` 確保 main 最新，減少意外。
- **公司幾乎都透過 Pull Request 合併**：不會有人在自己電腦上 `git merge` 進 main 直接 push。而是 push 分支 → 開 PR → Code Review → 在 GitHub 上按「Merge」（第 14 課）。本課的指令是幫你理解底層原理。
- **衝突當面/線上溝通**：撞到同一行時，別自己猜對方要什麼，直接問寫另一邊的人。
- **小步、常合併**：分支越小、越常和 main 同步，衝突越少越好解。

:::best Merge commit 訊息別亂寫
自動合併產生的 merge commit 通常保留預設訊息即可。但公司若要求，可加上這次合併了什麼、關聯哪個 PR。有些團隊為了歷史乾淨會選擇 rebase 或 squash（下一課、第 14 課會談），減少 merge commit。
:::

## 6. 常見錯誤與救援方法

:::rescue 衝突解到一半，越解越亂
別硬撐，直接放棄重來：

```bash
git merge --abort
```

這會回到合併前的乾淨狀態，你可以喘口氣、想清楚再重新 `git merge`。
:::

:::rescue 合併完才發現合錯了 / 合進一堆不該進的東西
如果這個 merge commit 還沒 push：

```bash
git reset --hard HEAD~1    # 退回合併前（注意會丟棄合併，確認後再用）
```

如果已經 push 且別人可能已經拉走了，改用 `git revert`（產生一個「反向 commit」抵銷合併，安全不改歷史，第 12、20 課詳談）。
:::

:::warn 「Already up to date」是正常的
執行 `git merge` 出現 `Already up to date`，代表要合併的分支沒有比目前分支多任何東西，不是錯誤，只是沒事可合。
:::

:::tip 本課重點回顧
merge 把分支改動融合進目前分支。撞到同一行會產生衝突——這是 Git 在保護你，不是壞掉。解衝突 = 編輯檔案留下正確內容（刪掉 `<<<`/`===`/`>>>` 記號）→ `add` → `commit`。想反悔用 `git merge --abort`。VS Code 的衝突介面讓這件事變簡單。下一課學 merge 的替代方案：rebase。
:::
"""
},

{
"id": "11",
"part": PART,
"title": "Rebase 與「Merge 還是 Rebase？」的抉擇",
"subtitle": "讓歷史變乾淨的另一種合併方式，以及它的黃金鐵律。",
"body": r"""
## 1. 為什麼要這樣做（原理）

`merge` 會保留分岔的真實歷史，但分支一多，歷史圖會變成一團義大利麵。**`rebase`（變基）** 提供另一種選擇：它把你分支上的 commit「搬家」，接到目標分支的最新位置後面，讓歷史變成一條漂亮的直線。

```text
merge 的歷史（保留分岔）        rebase 的歷史（一直線）
  o---o---M  (main)             o---o---o---o'---o'  (main)
 /       /
o---o---o  (feature)           （feature 的 commit 被複製、接到最新後面）
```

**關鍵理解**：rebase 不是移動原本的 commit，而是**用你的改動產生一組「新的 commit」接到新基底上**（所以它們的 hash 會變）。這就是「rebase 會改寫歷史」的意思，也是它危險的來源。

:::tip 一句話分辨
- **merge**：「把兩條線接起來」，保留真實發生的分岔，多一個 merge commit。
- **rebase**：「假裝我是從最新的 main 才開始開發的」，歷史變一直線，沒有 merge commit。
:::

## 2. 完整實戰情境：Tom、Alice、Bob

:::story Tom 讓自己的 PR 歷史變乾淨
Tom 的 `feature/login` 開了三天，期間 main 被 Bob 更新了好幾次。Tom 準備開 PR，但他的分支落後 main 很多。

他用 `git rebase main`，把自己的 3 個 commit 重新接到 main 的最新位置後面。現在他的分支就像「剛從最新的 main 分出來」一樣乾淨，PR 的 diff 只顯示他真正做的登入功能，沒有一堆無關的 merge 雜訊。Alice review 時清爽多了。

但 Alice 提醒：「rebase 只在你**自己一個人**的分支上做。如果 Bob 也在用這條分支，你 rebase 會把他搞爛——因為你把歷史改掉了。」
:::

## 3. 實際 Git 指令

**用 rebase 把分支接到最新的 main：**

```bash
# 在你的 feature 分支上
git switch feature/login
git rebase main
```

如果 rebase 過程中遇到衝突，流程和 merge 略不同：

```bash
# 1. 解決衝突的檔案（編輯內容、刪掉衝突記號）
# 2. 加入解決結果
git add 衝突的檔案
# 3. 繼續 rebase（注意：不是 commit，是 --continue）
git rebase --continue

# 想放棄整個 rebase、回到原狀
git rebase --abort
```

**互動式 rebase（整理自己的 commit）**——把凌亂的 commit 合併、改序、改訊息：

```bash
git rebase -i HEAD~3    # 整理最近 3 個 commit
```

編輯器會列出 commit，每行前面可改的指令：

| 指令 | 作用 |
| --- | --- |
| `pick` | 保留這個 commit（預設） |
| `reword` | 保留但改訊息 |
| `squash` | 把這個 commit 併進上一個（合併） |
| `fixup` | 像 squash 但丟棄這個的訊息 |
| `drop` | 刪掉這個 commit |

:::best 超實用場景：把「wip、typo、再修一下」壓成一個乾淨 commit
你開發時常留下 `wip`、`修個 typo`、`忘了存` 這種零碎 commit。開 PR 前用 `git rebase -i` 把它們 `squash` 成一個有意義的 commit，歷史立刻專業。很多公司甚至在 PR 合併時用 **Squash and merge** 自動幫你做這件事（第 14 課）。
:::

## 4. VS Code 圖形介面操作

:::vscode 圖形化 rebase
1. **Git Graph** 擴充套件：在某個分支或 commit 上右鍵，有 **Rebase current branch on this branch** 選項，圖形化執行 rebase。
2. 遇到衝突時，一樣用 VS Code 的衝突解決介面處理，解完在 Source Control 面板會看到 **Continue** 的提示。
3. 互動式 rebase（squash 那類）圖形工具支援有限，建議還是用終端機 `git rebase -i`，搭配 VS Code 當編輯器最順。
:::

## 5. 公司最佳實務：Merge vs Rebase 怎麼選

:::danger Rebase 的黃金鐵律
**永遠不要 rebase 一條「已經 push 且別人可能在用」的公共分支。**

因為 rebase 改寫歷史（commit hash 全變），別人手上的舊歷史會和你的新歷史對不上，造成嚴重混亂。安全準則：**rebase 只用在「還沒 push」或「只有你自己在用」的分支。** 公共的 main、develop 絕不 rebase。
:::

**實務上的選擇：**

| 情境 | 建議 |
| --- | --- |
| 更新自己的 feature 分支跟上 main | `rebase`（歷史乾淨） |
| 把 feature 合併回公共 main | `merge`（通常透過 PR，安全） |
| 整理自己還沒 push 的凌亂 commit | `rebase -i`（squash） |
| 分支已多人共用 | 一律 `merge`，絕不 rebase |

很多團隊的政策是：**「本地整理用 rebase，合併進主線用 merge（PR）」**，兼得乾淨歷史與安全。

## 6. 常見錯誤與救援方法

:::rescue rebase 到一半衝突太多、想放棄
```bash
git rebase --abort
```
回到 rebase 前的原狀，什麼都沒發生。
:::

:::rescue rebase 後發現搞砸了，想找回原本的分支
rebase 前的舊 commit 沒有真的消失，可用 reflog 找回：

```bash
git reflog                     # 找到 rebase 前那個狀態的 hash（例如標示 "before rebase"）
git reset --hard a1b2c3d       # 把分支拉回那個狀態
```

這是 rebase 出事時的救命稻草，第 20 課會再深入。
:::

:::warn 不小心對已 push 的分支 rebase 了
如果你 rebase 了共用分支並 push（可能要 `--force`），會影響隊友。**發現時立刻通知團隊**，大家協調用 `git pull --rebase` 或重新同步。預防遠勝於補救——記住黃金鐵律。
:::

:::tip 本課重點回顧
rebase 把 commit 搬到目標分支最新處，歷史變一直線、沒有 merge commit，代價是改寫歷史（hash 變）。互動式 `rebase -i` 能 squash 整理 commit。**黃金鐵律：只 rebase 沒 push 或自己專屬的分支，公共分支一律 merge。** 出事用 reflog 救。下一課學四個超實用的小工具：stash、cherry-pick、revert、reset。
:::
"""
},

{
"id": "12",
"part": PART,
"title": "Stash、Cherry-pick、Revert、Reset 四大工具",
"subtitle": "四個名字很像但用途完全不同的實用指令，一次搞懂何時用哪個。",
"body": r"""
## 1. 為什麼要這樣做（原理）

這四個指令新手最容易混淆，但各有明確用途。先用一句話記住它們：

| 指令 | 一句話 | 典型情境 |
| --- | --- | --- |
| **stash** | 「先把手上的活收進抽屜」 | 臨時要切分支，但改到一半不想 commit |
| **cherry-pick** | 「只挑某一個 commit 過來」 | 別的分支有個 commit 我這也想要 |
| **revert** | 「做一個反向 commit 抵銷它」 | 要撤銷已 push 的改動，又不想改歷史 |
| **reset** | 「把分支指標移回過去」 | 撤銷還沒 push 的本地 commit |

**revert 和 reset 的核心差異**（最常混）：revert 是「往前走、產生一個抵銷的新 commit」（安全，適合公共分支）；reset 是「往後退、直接移動指標」（會改變歷史，適合本地）。

## 2. 完整實戰情境：Tom、Alice、Bob

:::story 四種情境各來一次
- **stash**：Tom 正在 `feature/login` 寫到一半，突然 Alice 說 main 有個緊急 bug 要他先修。Tom 不想把半成品 commit，於是 `git stash` 把改動收進抽屜，切去修 bug，修完再 `git stash pop` 把活拿回來繼續。
- **cherry-pick**：Bob 在他的分支寫了一個好用的工具函式（某個 commit）。Tom 也想要，但不想合併 Bob 整條分支，於是只 `cherry-pick` Bob 那一個 commit 過來。
- **revert**：Tom 昨天 push 的一個改動上線後出包了。因為已經 push、別人也拉了，他用 `git revert` 產生一個反向 commit 安全地撤銷。
- **reset**：Tom 本地連續 commit 了三個爛東西還沒 push，他用 `git reset` 把它們一次退掉重來。
:::

## 3. 實際 Git 指令

**Stash——把未完成的改動暫存起來：**

```bash
git stash                 # 把工作區改動收進抽屜，回到乾淨狀態
git stash -m "登入寫一半"  # 收進去並加註說明
git stash list            # 看抽屜裡有哪些暫存
git stash pop             # 拿出最近一個並套用（同時從抽屜移除）
git stash apply           # 拿出來套用但保留在抽屜
git stash drop            # 丟掉最近一個暫存
git stash clear           # 清空抽屜
```

**Cherry-pick——把指定 commit 複製到目前分支：**

```bash
git cherry-pick a1b2c3d              # 挑一個 commit 過來
git cherry-pick a1b2c3d f4e5d6c      # 一次挑多個
git cherry-pick a1b2c3d^..f4e5d6c    # 挑一段範圍
```

**Revert——產生反向 commit 撤銷某次改動（安全、不改歷史）：**

```bash
git revert a1b2c3d        # 產生一個抵銷 a1b2c3d 的新 commit
git revert HEAD           # 撤銷最後一個 commit
```

**Reset——移動分支指標，撤銷本地 commit（三種模式）：**

```bash
# --soft：退回 commit，但改動留在暫存區（想重新 commit 時用）
git reset --soft HEAD~1

# --mixed（預設）：退回 commit，改動留在工作區（最常用）
git reset HEAD~1

# --hard：退回 commit，且丟棄所有改動（危險！東西會消失）
git reset --hard HEAD~1
```

:::danger `git reset --hard` 是全教材最危險的指令之一
它會**直接丟棄工作區的改動**，沒 commit 過的東西救不回來。用之前務必 `git status` 確認，或先 stash/commit 備份。不確定就別用 `--hard`，改用 `--mixed`（預設）比較安全。
:::

## 4. VS Code 圖形介面操作

:::vscode 圖形化操作這四個
- **Stash**：Source Control 面板 ⋯ → **Stash**（收）/ **Pop Stash**（拿回）。GitLens 也有專門的 Stashes 檢視，能看抽屜內容。
- **Cherry-pick**：Git Graph 裡在某個 commit 上右鍵 → **Cherry Pick**。
- **Revert**：Git Graph 裡在 commit 上右鍵 → **Revert Commit**。
- **Reset**：Git Graph 裡在某 commit 上右鍵 → **Reset current branch to this Commit**，並讓你選 soft / mixed / hard 模式（圖形化選擇很直覺）。
:::

## 5. 公司最佳實務

- **公共分支用 revert，本地用 reset**：已經 push、別人拉過的東西要撤銷，**一律用 `revert`**（不改歷史、安全）；只有自己本地還沒 push 的才用 `reset`。這是團隊協作的鐵律。
- **stash 不是長期倉庫**：stash 拿來暫存幾分鐘、幾小時可以，別把重要工作長期丟 stash（容易忘記、容易弄丟）。長期保存請開分支 commit。
- **cherry-pick 用於 hotfix 回填**：常見於「main 修好的緊急修正，要 cherry-pick 回正在發布的 release 分支」。但別過度使用，否則同一改動散落多處難追蹤。

:::best 把「還沒好但要切走」變成習慣
新人常因為「改到一半不敢切分支」而卡住。記住這個組合技：`git stash` → 去做別的事 → 回來 `git stash pop`。或更保險：直接開個 wip commit（`git commit -m "wip"`），之後用 `rebase -i` 整理掉。兩種都比把改動晾著好。
:::

## 6. 常見錯誤與救援方法

:::rescue stash pop 出現衝突
`stash pop` 時如果和目前檔案衝突，會像 merge 一樣要你解衝突。解完 `git add` 即可。注意：pop 衝突時該 stash **不會**自動從抽屜移除，解決後可自行 `git stash drop`。
:::

:::rescue 用了 reset --hard 把東西弄丟了
只要那些改動**曾經 commit 過**，就能救。用 reflog 找回：

```bash
git reflog                   # 找到被丟掉的 commit hash
git reset --hard a1b2c3d     # 或 git switch -c 救援分支 a1b2c3d
```

若那些改動**從沒 commit 過**（只在工作區被 --hard 清掉），則 Git 救不回，只能看編輯器有沒有本地歷史。這就是「動 --hard 前先 commit / stash」的原因。
:::

:::warn revert 一個 merge commit 要加參數
撤銷普通 commit 直接 `git revert`；但撤銷「合併 commit」時 Git 需要你指定保留哪一邊，要加 `-m 1`（`git revert -m 1 <merge-hash>`）。這是新手常踩的坑，遇到再查即可。
:::

:::tip 本課重點回顧
stash 收進抽屜、cherry-pick 挑單一 commit、revert 產生反向 commit（安全、公共分支用）、reset 移動指標（本地用，`--hard` 最危險）。核心口訣：**已 push 用 revert，沒 push 用 reset。** 弄丟東西先想 reflog。下一課終於連上 GitHub，進入真正的遠端協作。
:::
"""
},

{
"id": "13",
"part": PART,
"title": "連上 GitHub：clone、remote、push、pull、fetch",
"subtitle": "把本機的 Git 和雲端的 GitHub 接起來，真正開始多人協作。",
"body": r"""
## 1. 為什麼要這樣做（原理）

到目前為止，你的 Git 都在自己電腦裡。要和團隊協作，需要一個**大家都能存取的中央倉庫**——那就是 GitHub 上的 remote（遠端倉庫）。

運作模型很簡單：**每個人電腦裡都有一份完整的 repo（本地），GitHub 上有一份共用的（遠端）。大家把自己的 commit `push`（推）到遠端，也 `pull`（拉）別人推上去的改動下來。**

```text
   Tom 的電腦 ─push─▶                  ◀─pull─ Alice 的電腦
                     GitHub（遠端 origin）
   Tom 的電腦 ◀─pull─                  ─push─▶ Alice 的電腦
```

`origin` 是遠端倉庫的預設名字（就是個代號）。`main` 是分支。所以 `git push origin main` = 「把 main 分支推到叫 origin 的遠端」。

:::tip 本地分支 vs 遠端分支
你電腦裡有 `main`，GitHub 上也有一個 `main`。Git 用 `origin/main` 代表「我上次看到的遠端 main 長這樣」。`push` 是把本地 main 送上去更新遠端；`pull` 是把遠端的更新抓下來併進本地。理解這個「兩份 main」是掌握協作的關鍵。
:::

## 2. 完整實戰情境：Tom、Alice、Bob

:::story 三人透過 GitHub 協作的一天
1. Alice 在 GitHub 建了專案 repo，Tom 和 Bob 各自 `git clone` 到自己電腦。
2. Tom 開分支寫登入、`push` 到 GitHub。Bob 開分支修 bug、也 `push` 上去。
3. Bob 的修正先合併進遠端 main。Tom 早上開工前先 `git pull`，把 Bob 的修正抓下來，確保自己站在最新的地基上。
4. 三人各自 push / pull，GitHub 成為三人程式碼的匯流點，沒有人再用通訊軟體傳檔案。
:::

## 3. 實際 Git 指令

**情境 A：從 GitHub 複製一個現有專案下來（最常見的開始方式）：**

```bash
git clone https://github.com/公司/專案.git
cd 專案
# clone 會自動設好 origin、抓下所有歷史、切到 main，開箱即用
```

**情境 B：把本機既有專案推上一個新的 GitHub repo：**

```bash
# 先在 GitHub 網站上建立一個空 repo，複製它的網址，然後：
git remote add origin https://github.com/你的帳號/專案.git
git branch -M main
git push -u origin main
# -u 記住對應關係，之後只要打 git push 就好
```

**日常最常用的四個：**

```bash
git push               # 把本地 commit 推到遠端
git pull               # 抓遠端更新並併入本地（= fetch + merge）
git fetch              # 只抓遠端更新，先不併入（讓你先看看）
git remote -v          # 看目前連了哪些遠端
```

**push 新分支到遠端（第一次）：**

```bash
git push -u origin feature/login
# 之後在這條分支只要 git push 即可
```

:::tip pull = fetch + merge
`git pull` 其實是兩個動作的組合：`git fetch`（把遠端最新狀態抓到本地的 `origin/main`）+ `git merge`（把 `origin/main` 併進你的 `main`）。想更謹慎的人會先 `git fetch` 看看遠端有什麼變化，再決定怎麼併。想要乾淨歷史的人會用 `git pull --rebase`（用 rebase 取代 merge）。
:::

:::warn 現在 push 需要的是 Token，不是密碼
GitHub 早已不接受用「帳號密碼」push。第一次 push 時它會要你驗證，你需要用 **Personal Access Token（PAT）** 或設定 **SSH 金鑰**。最簡單的方式：安裝 **Git Credential Manager**（Windows 版 Git 通常內建），第一次會跳出瀏覽器讓你登入 GitHub 授權，之後就自動記住，不用再處理 token。
:::

## 4. VS Code 圖形介面操作

:::vscode 圖形化遠端操作
- **Clone**：`Ctrl+Shift+P` → 輸入 `Git: Clone` → 貼上 repo 網址 → 選存放位置。
- **登入 GitHub**：VS Code 左下角人像圖示可直接登入 GitHub 帳號，登入後 push/pull 免處理 token。
- **Push / Pull**：Source Control 面板 ⋯ → Push / Pull，或點左下狀態列的 **Sync Changes（↻）** 一次做完 pull+push。
- **狀態列的箭頭數字**：左下角會顯示 `↓2 ↑1`，代表「遠端有 2 個 commit 你還沒拉、你有 1 個 commit 還沒推」，一眼掌握同步狀態。
- **Publish Branch**：本地新分支還沒上遠端時，會出現 **Publish Branch** 按鈕，一鍵把分支推到 GitHub。
:::

## 5. 公司最佳實務

- **每天開工先 pull**：站在最新的地基上開始，能大幅減少之後的衝突。
- **push 前先 pull**：如果 push 被拒（remote 有你沒有的 commit），先 `git pull` 併好再 push，別急著 `--force`。
- **不要直接 push 到 main**：公司的 main 通常會設**分支保護（branch protection）**，禁止直接 push，強制走 PR。你日常是 push 你的 feature 分支，再開 PR（第 14 課）。
- **用 SSH 或 Credential Manager**：設定一次，之後 push/pull 免輸入，安全又省事。

:::best 看懂「你的分支落後/超前遠端」
`git status` 常出現這類訊息：
- `Your branch is ahead of 'origin/main' by 2 commits` → 你有 2 個 commit 還沒 push。
- `Your branch is behind 'origin/main' by 3 commits` → 遠端有 3 個你還沒 pull。
- `have diverged` → 兩邊都各有對方沒有的 commit，需要 pull 併起來。

看懂這幾句，你就永遠知道自己和團隊的同步狀態。
:::

## 6. 常見錯誤與救援方法

:::rescue push 被拒：`Updates were rejected`
最常見的原因是遠端有你本地沒有的 commit（別人先 push 了）。**不要用 `--force`**，正確做法：

```bash
git pull            # 先把遠端的抓下來併好（可能要解衝突）
git push            # 再推
```
:::

:::danger 絕對不要對共用分支 `git push --force`
`--force` 會用你的版本**覆蓋遠端歷史**，把別人已經 push 的 commit 直接抹掉，是團隊災難。若真的非改寫不可（例如自己的 feature 分支 rebase 後要更新），也請用比較安全的 `git push --force-with-lease`（它會在偵測到別人有新 push 時擋下來，避免誤蓋）。共用的 main 一律不 force。
:::

:::rescue clone 錯 repo / 想換遠端網址
```bash
git remote -v                                   # 看目前的遠端網址
git remote set-url origin 新的網址.git           # 改掉 origin 指向
```
:::

:::warn 認證失敗 / 一直要我輸入帳密
代表 credential 沒設好。安裝 Git Credential Manager，或在 VS Code 左下角登入 GitHub 帳號，或改用 SSH 金鑰。設定一次之後就不會再煩你。
:::

:::tip 本課重點回顧
遠端協作模型：本地各有完整 repo，GitHub 上有共用的 origin。`clone` 複製專案、`push` 推、`pull` 拉（=fetch+merge）、`fetch` 只抓不併。每天開工先 pull、push 前先 pull、被拒別 force。認證用 Credential Manager 或 SSH 設一次搞定。單元三完成，你已具備多人協作能力。下一單元進入真正的企業級流程。
:::
"""
},
]
