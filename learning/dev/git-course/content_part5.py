# -*- coding: utf-8 -*-
"""單元五：事故救援大全（第 20 課）"""

PART = "單元五 · 事故救援大全"

LESSONS = [
{
"id": "20",
"part": PART,
"title": "Git 事故救援大全：做錯了怎麼救",
"subtitle": "reflog 是你的時光機——push 錯分支、誤刪 commit、誤 merge、reset 弄丟東西，一課全收錄。",
"body": r"""
## 1. 為什麼要這樣做（原理）

這一課是整套教材的「安心保證」。學會它，你操作 Git 時就不會綁手綁腳，因為你知道**幾乎所有事故都能救**。

救援的核心武器是 **`git reflog`（reference log，引用日誌）**。它記錄了你在本機**每一次 HEAD 的移動**——每次 commit、切分支、merge、rebase、reset 都會留下一筆，附上當時的 commit hash。

:::tip reflog 就是 Git 的「時光機黑盒子」
即使你 `reset --hard` 把 commit「刪掉」，那個 commit 其實還在 Git 的資料庫裡（只是沒有指標指向它），而 reflog 記著它的 hash。只要知道 hash，就能把分支指標移回去、或開新分支救回來。**commit 過的東西，幾乎都能靠 reflog 找回。** 這是本課最重要的觀念。
:::

**救援的黃金三原則：**

1. **先停手、別再亂操作**：出事時最怕慌張地再下一堆指令，把情況弄更複雜。先深呼吸。
2. **先看清楚狀態**：`git status`、`git log --oneline`、`git reflog` 三連看，搞清楚現在到底在哪。
3. **已 push 的用「安全」手段（revert）、沒 push 的才用「改寫」手段（reset）**：不確定是否影響別人時，選不改寫歷史的做法。

## 2. 完整實戰情境：Tom、Alice、Bob

:::story Tom 的災難日與救援
Tom 一個早上出了四次包，每次都以為完蛋了，結果每次都被救回來：

1. 把功能 push 到了錯的分支 → 用 revert / cherry-pick 搬正。
2. `reset --hard` 弄丟了兩個 commit → 用 reflog 撈回。
3. merge 錯分支合進一堆垃圾 → 用 revert 抵銷。
4. 分支刪錯 → 用 reflog 找回 hash 重建。

Alice 全程只說了一句話：「Git 很難真的弄丟東西，只要你 commit 過。先 `git reflog`，答案通常就在裡面。」下面把這些情境的解法逐一收錄，當成你的急救手冊。
:::

## 3. 救援手冊：常見事故逐一擊破

### 事故 A：commit 訊息打錯 / 漏了檔案

```bash
# 改最後一個 commit 的訊息（還沒 push）
git commit --amend -m "正確訊息"

# 補一個漏掉的檔案進上一個 commit
git add 漏掉的檔案
git commit --amend --no-edit
```

### 事故 B：commit 了但想「反悔最後幾個 commit」

```bash
# 沒 push：把最後 1 個 commit 退回工作區（改動還在，可重做）
git reset --soft HEAD~1     # 保留在暫存區
git reset HEAD~1            # 保留在工作區（預設）

# 已 push（別人可能拉了）：用 revert 產生反向 commit，安全
git revert HEAD
```

### 事故 C：`reset --hard` 或誤刪，commit 不見了 → reflog 救回

```bash
# 1. 看 reflog，找到「弄丟前」那個狀態的 hash
git reflog
# 畫面會像：
#   a1b2c3d HEAD@{0}: reset: moving to HEAD~2
#   f4e5d6c HEAD@{1}: commit: 我不小心弄丟的重要功能   ← 就是這個！

# 2a. 把目前分支拉回那個狀態
git reset --hard f4e5d6c

# 2b. 或更保險：從那個 hash 開一條救援分支
git switch -c rescue f4e5d6c
```

:::rescue reflog 是誤刪 commit 的萬用解
只要那個 commit 曾經存在於你本機（你 commit 過、或曾 checkout 過），reflog 裡就找得到它的 hash。這適用於：reset 弄丟、rebase 搞砸、分支刪錯、amend 覆蓋掉舊 commit……幾乎所有「commit 消失」的情境。
:::

### 事故 D：push 到了錯的分支

```bash
# 情況：本來要 push 到 feature/login，卻 push 到了 main

# 1. 切到收到錯誤 commit 的分支（main）
git switch main

# 2a. 若那些 commit 還沒被別人拉走、且 main 允許改寫：
git reset --hard origin/main~N     # N = 誤推的 commit 數，退回乾淨狀態
git push --force-with-lease        # 謹慎更新（共用 main 通常禁止，需先問團隊）

# 2b. 若 main 是受保護 / 已被別人拉走（較安全，推薦）：
git revert <那幾個commit>          # 在 main 上抵銷它們
git push

# 3. 把那些改動放回「正確的分支」
git switch feature/login
git cherry-pick <那幾個commit>     # 把它們挑到對的分支
git push
```

:::warn 在共用 main 上，優先用 revert 而非 force
如果誤推的分支是團隊共用的 main，且別人可能已經 pull，**不要 force**（會把別人的歷史弄亂）。用 `revert` 抵銷、再 cherry-pick 到正確分支，是最安全的組合。
:::

### 事故 E：誤 merge（把不該合的分支合進來了）

```bash
# 還沒 push：直接退回合併前
git reset --hard HEAD~1

# 已 push：用 revert 撤銷合併（合併 commit 要加 -m 1 指定保留主線那邊）
git revert -m 1 <merge-commit-hash>
git push
```

### 事故 F：改到一半發現改錯檔案，想全部丟棄回到上次 commit

```bash
# 丟棄單一檔案的未commit改動
git restore 檔名

# 丟棄所有未commit改動（危險，沒commit的會消失）
git restore .
# 或
git reset --hard HEAD
```

### 事故 G：切分支前忘了處理改動，或想把改動移到別的分支

```bash
# 把當前未commit的改動暫存，切到對的分支再拿回來
git stash
git switch 正確的分支
git stash pop
```

## 4. VS Code 圖形介面操作

:::vscode 圖形化救援
- **看 reflog / 歷史找回 commit**：**GitLens** 或 **Git Graph** 能看到比 `git log` 更完整的歷史；Git Graph 裡在任一 commit 右鍵 → **Reset to this Commit** 或 **Create Branch here**，等於圖形化的 reflog 救援。
- **Revert**：Git Graph 裡 commit 右鍵 → **Revert Commit**，安全撤銷。
- **Discard / Restore**：Source Control 面板檔案右鍵 → Discard Changes。
- **Stash**：Source Control ⋯ → Stash / Pop Stash。
- **提醒**：`git reflog` 這種救命指令，終端機仍是最完整可靠的。圖形工具是輔助，出大事時別排斥打指令。
:::

## 5. 公司最佳實務

- **出事先溝通，別自己硬幹**：尤其牽涉共用分支（main）時，一個人默默 force push 可能連累全隊。先在群組說一聲。
- **共用分支只用「不改寫歷史」的手段**：revert 而非 reset、`--force-with-lease` 而非 `--force`、能不 force 就不 force。
- **養成小步 commit 的習慣**：commit 越頻繁，reflog 的救援點越多、每次能救回的粒度越細。這是最好的「事前保險」。
- **重要操作前先備份分支**：要做 rebase、reset 這類有風險的操作前，先 `git branch backup-今天日期` 開個備份分支，出事直接切回去，比 reflog 更省心。

:::best 一個讓你永遠不怕的習慣
在做任何「聽起來很嚇人」的操作（rebase、reset --hard、filter-repo）之前，先開一條備份分支：

```bash
git branch backup-before-rebase
```

這條分支釘住了你「動手前」的狀態。就算主操作全毀，`git switch backup-before-rebase` 就回到安全點。養成這個習慣，你會敢於嘗試任何進階操作。
:::

## 6. 事故對照速查表

:::danger 危險指令紅色警戒（用前三思）
- `git reset --hard`：丟棄未 commit 的改動，沒 commit 的救不回。
- `git push --force`：覆蓋遠端歷史，共用分支的災難。改用 `--force-with-lease`。
- `git clean -fd`：刪除所有未追蹤的檔案，Git 完全救不回（它從沒被記錄）。
- `git filter-repo` / 改寫歷史：影響所有隊友，需重新 clone，務必溝通。

共通原則：**這些操作前先 `git status` 看清楚、先開 backup 分支、共用分支先問團隊。**
:::

| 我做錯了… | 救援指令 |
| --- | --- |
| commit 訊息打錯（沒push） | `git commit --amend -m "..."` |
| 漏加檔案到上個 commit | `git add x && git commit --amend --no-edit` |
| 想撤銷最後 commit（沒push） | `git reset HEAD~1` |
| 想撤銷最後 commit（已push） | `git revert HEAD` |
| reset/rebase 弄丟 commit | `git reflog` 找 hash → `git reset --hard <hash>` |
| push 到錯分支 | 錯分支 `revert` + 正確分支 `cherry-pick` |
| 誤 merge（已push） | `git revert -m 1 <merge-hash>` |
| 刪錯分支 | `git reflog` 找 hash → `git switch -c 分支 <hash>` |
| 改到一半要切分支 | `git stash` → 切 → `git stash pop` |
| 丟棄所有未commit改動 | `git restore .`（確認後） |
| 機密被 commit | 先作廢金鑰 → `git rm --cached` →（必要時）清歷史 |

:::tip 全教材總結
恭喜你走到最後一課！回顧你的旅程：從「Git 是什麼」與三大區域的原理，到單人的 add/commit/log、.gitignore、commit 規範；再到分支、merge、rebase、四大工具與 GitHub 遠端協作；接著是企業級的 PR/Code Review、Fork、Tag/Release、資安、LFS、CI/CD；最後這一課讓你明白——**Git 幾乎難以真正弄丟東西，reflog 是你的時光機。**

你現在具備了獨立開發、多人協作、參與開源、適應公司工作流程，以及冷靜處理事故的完整能力。剩下的，就是在真實專案裡不斷練習。祝你在工程師的路上，commit 順利、衝突好解、永遠有得救。⎇
:::
"""
},
]
