# -*- coding: utf-8 -*-
"""指令速查單頁內容（迷你 Markdown）。"""

CHEATSHEET = r"""
:::tip 怎麼用這一頁
這頁收錄日常最常用的指令，按用途分組。找不到就用瀏覽器搜尋（Ctrl+F / Cmd+F）。危險指令會標紅，用前請三思。每組後面標注對應的課程，想看原理回去複習。
:::

## 設定（一台電腦設定一次）

```bash
git config --global user.name "你的名字"
git config --global user.email "你的email"     # 對齊 GitHub 帳號
git config --global init.defaultBranch main      # 預設分支叫 main
git config --global core.editor "code --wait"    # 用 VS Code 寫訊息
git config --list                                # 檢查所有設定
```
對應第 2 課。

## 開始一個專案

```bash
git init                          # 把資料夾變成 Git 專案（只做一次）
git clone <網址>                  # 從 GitHub 複製現有專案下來
```
對應第 4、13 課。

## 日常循環：add / commit / status / log

```bash
git status                        # 看目前哪些檔案改了、在哪個區域
git add <檔名>                    # 把單一檔案放進暫存區
git add .                         # 把所有改動放進暫存區
git commit -m "feat: 說明"        # 拍快照（用 Conventional Commits 格式）
git log --oneline                 # 簡潔看歷史
git log --oneline --graph         # 加上分支圖形
```
對應第 3、4、6 課。

## 看差異與還原檔案

```bash
git diff                          # 還沒 add 的改動
git diff --staged                 # 已 add、待 commit 的改動
git diff HEAD                     # 所有還沒 commit 的改動
git restore <檔名>                # 丟棄某檔未 commit 的改動（小心）
git restore --staged <檔名>       # 把檔案從暫存區退回工作區（取消 add）
git blame <檔名>                  # 看每一行是誰、哪個 commit 改的
```
對應第 3、7 課。

## 分支

```bash
git branch                        # 列出所有分支（* 是你在的）
git switch -c feature/xxx         # 建立並切換到新分支
git switch main                   # 切換到已存在的分支
git switch -                      # 切回上一個分支
git branch -m 新名字              # 改目前分支名稱
git branch -d feature/xxx         # 刪除已合併的分支
```
命名前綴：`feature/` 新功能、`fix/` 修 bug、`hotfix/` 緊急修正、`refactor/` 重構、`docs/` 文件。對應第 9 課。

## 合併與變基

```bash
git merge feature/xxx             # 把某分支合併進目前分支
git merge --abort                 # 放棄合併，回到合併前
git rebase main                   # 把目前分支的 commit 接到 main 最新處
git rebase --continue             # 解完衝突後繼續 rebase
git rebase --abort                # 放棄 rebase
git rebase -i HEAD~3              # 互動式整理最近 3 個 commit（squash 等）
```

:::warn 鐵律
公共分支（main）只 `merge`，絕不 `rebase`；rebase 只用在自己還沒 push 的分支。對應第 10、11 課。
:::

## 四大實用工具

```bash
git stash                         # 把未完成改動收進抽屜
git stash pop                     # 拿回最近一個暫存並套用
git stash list                    # 看抽屜內容
git cherry-pick <hash>            # 把某一個 commit 複製到目前分支
git revert <hash>                 # 產生反向 commit 抵銷（安全，公共分支用）
git reset --soft HEAD~1           # 撤銷 commit，改動留暫存區
git reset HEAD~1                  # 撤銷 commit，改動留工作區（預設）
```
口訣：**已 push 用 `revert`，沒 push 用 `reset`。** 對應第 12 課。

## 遠端 GitHub

```bash
git remote -v                     # 看連了哪些遠端
git remote add origin <網址>      # 加一個遠端叫 origin
git push -u origin <分支>         # 第一次推分支（-u 記住對應）
git push                          # 推本地 commit 到遠端
git pull                          # 抓遠端更新並併入（= fetch + merge）
git fetch                         # 只抓遠端更新、先不併入
```
開源用的第二個遠端：`git remote add upstream <原專案網址>`。對應第 13、15 課。

## Tag 與發版

```bash
git tag -a v1.0.0 -m "第一版"     # 建立附註型 tag
git tag                           # 列出所有 tag
git push origin v1.0.0            # 推單一 tag（push 不會自動推 tag！）
git push origin --tags            # 推所有 tag
git tag -d v1.0.0                 # 刪本地 tag
```
版本號 SemVer：`主.次.修訂`（破壞性／新功能／修 bug）。對應第 16 課。

## Git LFS（大型檔案）

```bash
git lfs install                   # 一台電腦裝一次
git lfs track "*.safetensors"     # 指定某類檔案用 LFS 管理
git add .gitattributes            # 一定要 commit 這個規則檔！
git lfs ls-files                  # 看哪些檔案被 LFS 管理
git lfs pull                      # 抓下 LFS 大檔的實際內容
```
對應第 18 課。

## 事故救援（急救手冊）

```bash
git commit --amend -m "新訊息"        # 改最後一個 commit 訊息（沒 push）
git commit --amend --no-edit          # 補漏掉的檔案進上個 commit
git reflog                            # 時光機：找回弄丟的 commit hash
git reset --hard <hash>               # 把分支拉回某個狀態（配 reflog 救援）
git switch -c rescue <hash>           # 從某 hash 開救援分支
git revert -m 1 <merge-hash>          # 撤銷一個合併 commit
git branch backup-日期                # 高風險操作前先開備份分支
```
對應第 20 課。

## 危險指令紅色警戒

:::danger 用前三思
- `git reset --hard`：丟棄未 commit 的改動，沒 commit 的救不回。
- `git push --force`：覆蓋遠端歷史，共用分支的災難。改用 `--force-with-lease`。
- `git clean -fd`：刪除所有未追蹤檔案，Git 完全救不回。
- 改寫歷史（`filter-repo`、對公共分支 rebase）：影響所有隊友，需重新 clone，務必先溝通。

共通原則：這些操作前先 `git status` 看清楚、先開 backup 分支、共用分支先問團隊。
:::

## 圖形介面 ↔ 指令對照

| VS Code 操作 | 等於指令 |
| --- | --- |
| Initialize Repository | `git init` |
| `+` Stage Changes | `git add` |
| `−` Unstage | `git restore --staged` |
| Discard Changes | `git restore` |
| 打訊息 + ✓ Commit | `git commit -m` |
| Sync Changes（↻） | `git pull` + `git push` |
| 左下角分支名 | `git switch` / `git branch` |

對應第 8 課。三個必裝擴充套件：GitLens、GitHub Pull Requests、Git Graph。
"""
