# -*- coding: utf-8 -*-
"""每一課的「自我檢核（含解答）」與「動手練習」。
key = 課程 id（字串），value = {"check": [(問題, 解答), ...], "practice": [任務, ...]}
解答支援迷你 Markdown（可含程式碼區塊）。
"""

QUIZ = {
"01": {
"check": [
("Git 和 GitHub 有什麼不同？",
 "**Git** 是裝在你電腦上的版本控制軟體（拍快照的工具）；**GitHub** 是放 Git 專案的雲端網站（分享、備份、協作的相簿）。可以只用 Git 不用 GitHub，但團隊協作時 GitHub 是大家交換程式碼的中央集合點。"),
("Git 的核心心智模型是「存檔」還是「拍快照」？為什麼？",
 "是**拍快照**。每次 `commit` 就像對整個專案拍一張照片並附上說明，這些照片串成可前進、後退、分岔的時間線。它不是單純幫你覆蓋存檔，而是保留每一個版本。"),
("版本控制主要解決哪三個痛點？",
 "1. 不知道每一版改了什麼；2. 多人協作互相覆蓋；3. 無法安心回到過去。Git 讓這三件事都變簡單。"),
],
"practice": [
"用自己的話，寫一段話向朋友解釋「為什麼工程師要用 Git」，不要用專有名詞。",
"回想你過去有沒有存過類似 `報告_最終版_真的最終.docx` 的檔案——那就是你需要版本控制的證據。",
],
},

"02": {
"check": [
("安裝完 Git 後，第一件必做的事是什麼？用什麼指令？",
 "設定身分（名字與 email），因為每個 commit 都要「簽名」：\n\n```bash\ngit config --global user.name \"你的名字\"\ngit config --global user.email \"你的email\"\n```"),
("為什麼 email 要和 GitHub 帳號一致？",
 "這樣你在 GitHub 上的貢獻才會正確歸屬到你的帳號與頭像。用不一致的 email，commit 不會算進你的貢獻紀錄。"),
("`--global` 代表什麼意思？",
 "代表這個設定套用到你電腦上**所有** Git 專案。若只想針對單一專案設定，就在該專案資料夾裡用不加 `--global` 的指令。"),
],
"practice": [
"安裝 Git 與 VS Code，並用 `git --version` 確認安裝成功。",
"設定好你的 `user.name` 和 `user.email`，然後用 `git config --list` 檢查是否正確。",
"在 VS Code 按 Ctrl+~ 打開內建終端機，試著在裡面打一次 `git config --list`。",
],
},

"03": {
"check": [
("Git 的三大區域是哪三個？各自的白話比喻是什麼？",
 "**工作區**（你在改的檔案／房間）、**暫存區**（待拍照清單／紙箱）、**儲存庫**（永久快照歷史／寄出的包裹）。"),
("`git add` 和 `git commit` 分別在哪兩個區域之間搬東西？",
 "`git add`：工作區 → 暫存區（把改動放進紙箱）。`git commit`：暫存區 → 儲存庫（封箱寄出，成為永久快照）。"),
("為什麼要多一個「暫存區」，不能改完直接 commit 嗎？",
 "因為暫存區讓你能**挑選**要 commit 的內容。例如同時改了兩個檔案，你可以只把其中一個 commit，讓每個 commit 主題單一乾淨。"),
("哪個指令能隨時告訴你檔案在哪個區域？",
 "`git status`。紅色通常是工作區的改動、綠色是已加入暫存區待 commit 的。"),
],
"practice": [
"建一個測試資料夾、`git init`，新增一個檔案，用 `git status` 觀察它是紅色 Untracked。",
"`git add` 它，再 `git status`，觀察它變綠色（進入暫存區）。",
"`git commit -m \"第一個 commit\"`，然後 `git log --oneline` 看你的第一張快照。",
"試著 `git restore --staged 檔名` 把檔案退回工作區，感受兩個區域的移動。",
],
},

"04": {
"check": [
("`git init` 一個專案要做幾次？",
 "只做一次（建立專案時）。之後天天做的是 `add` 和 `commit`，不會再 init。"),
("`.git` 資料夾是什麼？刪掉會怎樣？",
 "它是 Git 的「大腦」，存放所有快照、歷史、分支。刪掉後資料夾變回普通資料夾，版本歷史全部消失（但你的檔案本身不受影響）。"),
("`HEAD` 代表什麼？",
 "代表「你現在站在哪裡」的指標，通常指向你目前分支的最新 commit。"),
],
"practice": [
"完整走一次：`git init` → 建檔 → `git add` → `git commit` → `git log --oneline`。",
"做兩三個 commit，觀察 `git log --oneline` 裡的時間線如何增長。",
"故意把上一個 commit 訊息打錯，再用 `git commit --amend -m \"正確訊息\"` 修正。",
],
},

"05": {
"check": [
(".gitignore 的作用是什麼？哪些檔案最該被忽略？",
 "讓 Git 忽略指定檔案，使它們不出現在 `git status`、也不會被 `git add`。最該忽略：機密（`.env`、金鑰）、自動產生檔（`node_modules/`、`__pycache__/`）、個人環境檔、大型模型／資料。"),
("最經典的坑：檔案已經被 commit 過了，再加進 .gitignore 有用嗎？怎麼解？",
 "**沒用**。`.gitignore` 只對「還沒被追蹤過」的檔案有效。已被追蹤要先解除：\n\n```bash\ngit rm --cached .env\ngit commit -m \"chore: 停止追蹤 .env\"\n```"),
("`.env` 被忽略了，怎麼讓隊友知道需要哪些環境變數？",
 "commit 一份 `.env.example`（只有欄位名、沒有真值）當範本，`.env` 本身仍被忽略。"),
],
"practice": [
"在測試專案建立 `.gitignore`，加入 `.env` 和 `__pycache__/`，並確認 `git status` 不再顯示它們。",
"故意先 commit 一個檔案，再把它加進 `.gitignore`，觀察它仍被追蹤；然後用 `git rm --cached` 解除。",
"到 gitignore.io 產生一份 Python 專案的 `.gitignore` 範本，看看業界會忽略哪些東西。",
],
},

"06": {
"check": [
("Conventional Commits 的基本格式是什麼？",
 "`類型(範圍): 簡短描述`，例如 `feat(auth): 加入 Google 登入`。範圍可省略。"),
("`feat`、`fix`、`docs`、`refactor`、`chore` 分別用在什麼時候？",
 "`feat`=新功能、`fix`=修 bug、`docs`=只改文件、`refactor`=重構（不改功能不修 bug）、`chore`=雜務（設定、相依套件）。"),
("規範的 commit 訊息除了好讀，還能帶來什麼自動化好處？",
 "工具能據此**自動產生 CHANGELOG**、**自動決定版本號**（`fix`→修訂號、`feat`→次版本、`BREAKING CHANGE`→主版本），甚至自動發版。"),
],
"practice": [
"把下面三個爛訊息改寫成 Conventional Commits：「更新」「修好了」「改一下 css」。",
"做一個 commit 時故意違反規範，再用 `git commit --amend` 改成規範格式。",
"想像一個「移除舊 API」的破壞性變更，寫出它完整的 commit 訊息（含 BREAKING CHANGE）。",
],
},

"07": {
"check": [
("要看「還沒 add 的改動」和「已 add 待 commit 的改動」，分別用什麼指令？",
 "`git diff`（工作區 vs 暫存區，還沒 add 的）；`git diff --staged`（暫存區 vs 上次 commit，已 add 的）。"),
("checkout 一個舊 commit 會進入什麼狀態？該注意什麼？",
 "進入 **detached HEAD（分離頭指標）**——你站在歷史中間、不在任何分支上。此時只是「參觀」，別急著改東西；看完 `git switch main` 回到最新。要在此開發就先開分支。"),
("`git switch` 和 `git restore` 各自取代了老指令 `git checkout` 的哪個功能？",
 "`git switch` = 切換分支；`git restore` = 還原檔案。新指令把老 `checkout` 的兩種用途拆得更清楚、更不易誤用。"),
],
"practice": [
"改一個檔案但先別 add，用 `git diff` 看綠增紅刪；`git add` 後改用 `git diff --staged` 看。",
"用 `git log --oneline --graph` 看你目前的歷史圖。",
"checkout 一個舊 commit 感受 detached HEAD，再 `git switch main` 回來。",
],
},

"08": {
"check": [
("VS Code 裡按 `+`（Stage Changes）等於哪個指令？打訊息按 ✓ 呢？",
 "`+` = `git add`；打訊息按 ✓ Commit = `git commit`。"),
("圖形介面處理不了的複雜操作（如互動式 rebase、reflog 救援）該怎麼辦？",
 "回終端機用指令。圖形介面打底、指令墊底——別排斥終端機，它是你的安全網。"),
("哪三個 VS Code 擴充套件對 Git 工作最有幫助？",
 "GitLens（逐行歷史／blame）、GitHub Pull Requests（在編輯器開 PR 與 review）、Git Graph（圖形化看分支）。"),
],
"practice": [
"純用 VS Code 圖形介面完成一次：改檔 → 看 diff → Stage → Commit，全程不打指令。",
"安裝 GitLens，把游標停在某行程式碼上，看它顯示「這行是誰、何時改的」。",
"對照本課的「圖形介面 ↔ 指令」表，把每個按鈕在心裡對應到指令。",
],
},

"09": {
"check": [
("分支的本質是什麼？為什麼建分支、切分支這麼快？",
 "分支只是一個「指向某個 commit 的輕量指標」（幾十位元組），不是複製整份程式碼，所以操作幾乎瞬間。"),
("為什麼團隊不直接在 main 上開發？",
 "因為任何人推一個半成品就會弄壞主線。每個功能開自己的分支，做完、測試、review 後再合併回 main，能讓 main 永遠保持可運作。"),
("`feature/`、`fix/`、`hotfix/` 前綴分別代表什麼？",
 "`feature/`=新功能、`fix/`(或 bugfix/)=修 bug、`hotfix/`=緊急修正已上線的問題。用前綴讓人一眼看懂分支目的。"),
],
"practice": [
"用 `git switch -c feature/test` 開一條分支，做一個 commit，再 `git switch main` 觀察 main 上沒有那個改動。",
"用 `git branch` 列出所有分支，找出 `*` 標記你目前在哪。",
"想像三個功能同時進行，替它們各取一個符合命名規範的分支名。",
],
},

"10": {
"check": [
("合併衝突（merge conflict）發生的原因是什麼？它是錯誤嗎？",
 "當兩個分支改到「同一檔案的同一行」，Git 無法判斷聽誰的就會停下來要你決定。它**不是錯誤**，而是 Git 在保護你、不自作主張蓋掉某人的心血。"),
("解衝突的三個步驟是什麼？",
 "1. 編輯檔案，刪掉 `<<<<<<<`、`=======`、`>>>>>>>` 三種記號，只留最終要的內容；2. `git add 檔名`；3. `git commit` 完成合併。"),
("合併解到一半越弄越亂，怎麼放棄重來？",
 "```bash\ngit merge --abort\n```\n回到合併前的乾淨狀態。"),
],
"practice": [
"刻意製造衝突：開兩條分支改同一檔案的同一行，合併時觀察衝突記號。",
"用 VS Code 的衝突解決按鈕（Accept Current / Incoming / Both）解一次衝突。",
"再製造一次衝突，這次用 `git merge --abort` 放棄，感受「隨時可以反悔」。",
],
},

"11": {
"check": [
("merge 和 rebase 最大的差別是什麼？",
 "merge 保留分岔的真實歷史、多一個 merge commit；rebase 把 commit 搬到目標分支最新處，歷史變一直線、沒有 merge commit，但**會改寫歷史**（commit hash 改變）。"),
("Rebase 的黃金鐵律是什麼？",
 "**永遠不要 rebase 一條已經 push 且別人可能在用的公共分支**（如 main）。rebase 只用在還沒 push 或只有自己在用的分支。"),
("互動式 rebase（`rebase -i`）的 `squash` 有什麼用？",
 "把多個零碎 commit（wip、typo…）合併成一個乾淨、有意義的 commit，開 PR 前整理歷史用。"),
],
"practice": [
"在自己的 feature 分支上做幾個零碎 commit，用 `git rebase -i HEAD~3` 把它們 squash 成一個。",
"背下鐵律：公共分支只 merge、私有分支才 rebase。用自己的話解釋為什麼。",
"若 rebase 出事，寫下你會用哪個指令查找救援用的 hash（提示：reflog）。",
],
},

"12": {
"check": [
("stash、cherry-pick、revert、reset 各用一句話描述。",
 "stash=先把手上的活收進抽屜；cherry-pick=只挑某一個 commit 過來；revert=做一個反向 commit 抵銷（安全、公共分支用）；reset=移動分支指標撤銷本地 commit。"),
("revert 和 reset 的核心差異？分別適用什麼情境？",
 "revert 往前走、產生抵銷的新 commit，**不改歷史、適合已 push 的公共分支**；reset 往後退、直接移動指標，**會改變歷史、只適合本地還沒 push 的**。口訣：已 push 用 revert，沒 push 用 reset。"),
("`git reset --hard` 為什麼危險？",
 "它會直接丟棄工作區的改動，沒 commit 過的東西救不回來。用前務必 `git status` 確認或先備份。"),
],
"practice": [
"改到一半時 `git stash`，切到別的分支，再回來 `git stash pop`。",
"在測試 repo 用 `git reset --soft HEAD~1` 撤銷一個 commit，觀察改動還留在暫存區。",
"用 `git revert HEAD` 撤銷最後一個 commit，觀察它「產生新 commit」而非刪除。",
],
},

"13": {
"check": [
("`git clone`、`git push`、`git pull`、`git fetch` 各做什麼？",
 "clone=把整個遠端專案複製到本機；push=把本地 commit 推到遠端；pull=抓遠端更新並併入本地（=fetch+merge）；fetch=只抓遠端更新、先不併入。"),
("`origin` 是什麼？`git push origin main` 是什麼意思？",
 "`origin` 是遠端倉庫的預設代號。`git push origin main` = 把本地 main 分支推到叫 origin 的遠端。"),
("push 被拒（Updates were rejected）通常怎麼解？能用 `--force` 嗎？",
 "通常是遠端有你沒有的 commit。**不要 force**，先 `git pull` 併好（可能解衝突）再 `git push`。共用分支絕不 `--force`。"),
],
"practice": [
"在 GitHub 建一個空 repo，把本機專案用 `git remote add origin` + `git push -u origin main` 推上去。",
"用 `git remote -v` 確認遠端網址。",
"改一個檔案 commit 後 push，到 GitHub 網頁確認改動出現了。",
],
},

"14": {
"check": [
("公司裡合併進 main 的正確流程是什麼？（不是自己 git merge）",
 "在 feature 分支開發 → push → 開 **Pull Request** → 隊友 **Code Review** → 通過（且 CI 綠燈）→ 在 GitHub 按 **Merge**。"),
("Pull Request 是 Git 指令還是 GitHub 功能？",
 "是 **GitHub 功能**（GitLab 叫 Merge Request）。Git 本身只有 branch 和 merge，PR 是在其上加的「可討論、審查、跑測試」的協作機制。"),
("當 PR 作者，為什麼「PR 要小」很重要？",
 "小 PR（幾百行內）才容易被 review、才看得出問題；上千行的 PR 沒人想看也看不出問題，品質把關會失效。"),
],
"practice": [
"push 一條分支，到 GitHub 開一個 PR，練習寫清楚的標題與說明（做了什麼、怎麼測）。",
"想像你是 reviewer，對一段程式碼寫一則「對事不對人」的 comment。",
"了解你常用 repo 的合併方式：Merge commit / Squash / Rebase，各自的差別。",
],
},

"15": {
"check": [
("Fork 和 Clone 差在哪？",
 "Fork=把 repo 複製到你**自己的 GitHub 帳號**（雲端副本）；Clone=把 repo 下載到你**本機電腦**。參與開源的鏈路是：原專案→Fork→你的 GitHub→Clone→你的電腦。"),
("Fork 後本地的 `origin` 和 `upstream` 分別指向哪裡？",
 "`origin`=你自己的 fork（可 push）；`upstream`=原本的專案（只讀，用來抓它的最新更新保持同步）。"),
("公司內部通常用 fork 嗎？什麼時候才需要 fork？",
 "公司內部通常不用（你對公司 repo 有寫入權限，直接開分支開 PR 即可）。Fork 主要用於**開源貢獻**或你沒有寫入權限的專案。"),
],
"practice": [
"到 GitHub fork 一個你喜歡的開源專案，clone 下來，加上 `upstream` 遠端。",
"用 `git remote -v` 確認 origin 和 upstream 都在、方向正確。",
"用 `git fetch upstream` + `git merge upstream/main` 練習同步 fork。",
],
},

"16": {
"check": [
("Tag 和分支有什麼不同？",
 "分支會一直往前移動；tag 釘在某個 commit 上就**不動了**，永遠指向那個發布時刻的快照。"),
("語意化版本 `v2.4.1` 的三個數字分別在什麼時候 +1？",
 "主版本（2）：有破壞性變更；次版本（4）：新增向下相容的功能；修訂號（1）：只修 bug。"),
("最常見的 tag 坑是什麼？",
 "`git push` **不會**自動推送 tag！打完 tag 要另外 `git push origin --tags`（或 `git push origin v1.0.0`），否則 GitHub 上看不到。"),
],
"practice": [
"對一個 commit 打附註型 tag：`git tag -a v1.0.0 -m \"第一版\"`，再 `git push origin v1.0.0`。",
"到 GitHub 的 Releases 頁，用那個 tag 建立一個 Release 並寫更新說明。",
"用 `git tag` 列出所有 tag，`git show v1.0.0` 看它指向哪個 commit。",
],
},

"17": {
"check": [
("為什麼「commit 了金鑰、下個 commit 刪掉」沒有用？",
 "因為 Git 記住每個版本，金鑰永遠留在歷史某個 commit 裡，任何人翻歷史都找得到。而且 GitHub 上有爬蟲即時掃描新 push 的金鑰。"),
("發現金鑰外洩，第一步該做什麼？",
 "**立刻作廢那把金鑰、產生新的**（假設已外洩）。刪檔案、清歷史都是次要——刪檔案救不了已經外流的東西。"),
("機密的正確管理方式是什麼？",
 "放在 `.env`／環境變數，用 `.gitignore` 排除，**絕不進版本控制**；程式從環境讀取而非寫死；附一份沒有真值的 `.env.example` 給隊友。"),
],
"practice": [
"在測試專案把一個假金鑰寫進 `.env`，並確認 `.gitignore` 有排除它（檔案總管顯示灰色）。",
"寫一小段 Python，用 `os.environ[...]` 從環境變數讀金鑰，而不是寫死在程式裡。",
"了解 gitleaks 或 git-secrets，思考如何在 commit 前自動攔截金鑰。",
],
},

"18": {
"check": [
("為什麼大型二進位檔（模型、影片）不適合直接進 Git？",
 "Git 每個版本都完整存一份，改一次大檔就多存一整份、且歷史裡永遠瘦不回來，會撐爆 repo、拖慢 clone；GitHub 還限制單檔 100MB。"),
("Git LFS 的原理是什麼？（一句話）",
 "Git 裡只存一個很小的「指標檔」，真正的大檔內容存到 LFS 伺服器，checkout 時才抓下來——**Git 存指標，LFS 存內容**。"),
("設定 LFS 時，除了 `git lfs track`，還有哪個檔案一定要 commit？為什麼？",
 "`.gitattributes`。它記錄了 LFS 的 track 規則，不 commit 的話隊友不會套用同樣規則，大檔會變成普通 Git 檔。"),
],
"practice": [
"（若已裝 LFS）在測試 repo 執行 `git lfs track \"*.mp4\"`，觀察 `.gitattributes` 內容。",
"列出 AI 專案的四種檔案，分別歸類該用：普通 Git / LFS / 雲端儲存 / gitignore。",
"想想為什麼很多 AI 團隊寧可用 HuggingFace/S3 而非 LFS（提示：配額成本）。",
],
},

"19": {
"check": [
("CI 和 CD 分別是什麼？",
 "CI（持續整合）=每次 push/PR 自動跑測試、檢查、建置，確保進 main 的程式碼能動；CD（持續部署）=測試通過後自動部署／發佈。"),
("GitHub Actions 的 workflow 檔要放在哪個資料夾？靠什麼決定何時執行？",
 "放在 `.github/workflows/`，副檔名 `.yml`。靠 `on:` 欄位定義觸發條件（push、pull_request、tag、schedule 等）。"),
("部署需要的金鑰該放哪裡？為什麼不能寫進 YAML？",
 "放進 GitHub 的 **Secrets**（Settings → Secrets and variables → Actions），用 `${{ secrets.名稱 }}` 引用。寫進 YAML 等於進版本控制、等於外洩。"),
],
"practice": [
"在測試 repo 建立 `.github/workflows/ci.yml`，讓它在 push 時印出一句話（最小可行 workflow）。",
"push 後到 GitHub 的 Actions 分頁，觀察 workflow 執行的 log。",
"想像一個「push v* tag 就自動建立 Release」的流程，寫出它 `on:` 的觸發條件。",
],
},

"20": {
"check": [
("救援的核心武器是什麼？它記錄了什麼？",
 "`git reflog`。它記錄你在本機**每一次 HEAD 的移動**（commit、切分支、merge、rebase、reset…），附上當時的 commit hash。commit 過的東西幾乎都能靠它找回。"),
("`reset --hard` 弄丟了 commit，怎麼救？",
 "```bash\ngit reflog            # 找到弄丟前那個狀態的 hash\ngit reset --hard <hash>   # 或 git switch -c rescue <hash>\n```"),
("救援黃金三原則是什麼？",
 "1. 先停手別亂操作；2. 先看清楚狀態（status / log / reflog 三連看）；3. 已 push 用安全手段（revert），沒 push 才用改寫手段（reset）。"),
("做高風險操作（rebase、reset --hard）前，最省心的保險是什麼？",
 "先開一條備份分支：`git branch backup-今天日期`。出事直接 `git switch` 回去，比 reflog 更省心。"),
],
"practice": [
"故意 `git reset --hard HEAD~1` 弄丟一個 commit，再用 `git reflog` + `git reset --hard <hash>` 救回來。",
"用 `git revert HEAD` 撤銷一個 commit，比較它和 reset 的差別（一個產生新 commit、一個移動指標）。",
"把本課最後的「事故對照速查表」存成書籤，真的出事時直接查。",
],
},
}
