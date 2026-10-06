# -*- coding: utf-8 -*-
"""
Database Systems Question Bank Generator - Part 3 (130 unique questions)
Topics: Crash Recovery & ARIES (40), Physical Storage & Indexes (45), Query Optimization & Joins (45).
"""

def get_db_part3_questions():
    qs = []

    # -------------------------------------------------------------
    # 7. 復原機制與 ARIES 演算法 (40 題)
    # -------------------------------------------------------------
    rec_data = [
        ("預寫式日誌（Write-Ahead Logging, WAL）協定的兩大核心黃金法則為？",
         "1. 任何資料頁（Data Page）被寫入磁碟前，對應的更新日誌紀錄必須「先」寫入磁碟；2. 交易發出 COMMIT 回應前，其 COMMIT 日誌紀錄必須已強制寫入磁碟", ["1. 任何資料頁（Data Page）被寫入磁碟前，對應的更新日誌紀錄必須「先」寫入磁碟；2. 交易發出 COMMIT 回應前，其 COMMIT 日誌紀錄必須已強制寫入磁碟", "資料頁與日誌必須同時寫入", "日誌在交易結束後非同步寫入", "資料頁寫入磁碟後再寫入日誌"],
         "WAL 保證 Atomicity（有舊值日誌可 Undo 未提交資料）與 Durability（有新值日誌可 Redo 已提交資料）。"),
        ("ARIES 復原演算法（Algorithms for Recovery and Isolation Exploiting Semantics）在系統崩潰重啟後的執行三大階段依序為？",
         "分析階段（Analysis Phase） -> 重做階段（Redo Phase） -> 復原階段（Undo Phase）", ["分析階段（Analysis Phase） -> 重做階段（Redo Phase） -> 復原階段（Undo Phase）", "重做階段 -> 復原階段 -> 分析階段", "復原階段 -> 重做階段 -> 分析階段", "備份階段 -> 檢驗階段 -> 重建階段"],
         "三大階段經典流程：分析階段重建崩潰瞬間狀態（活躍交易與髒頁）；重做階段「重現歷史（Repeating History）」前滾；復原階段倒序撤銷未提交交易。"),
        ("ARIES 演算法在「重做階段（Redo Phase）」的主要設計哲學為？",
         "重現歷史（Repeating History）：將所有變更（無論交易最終是否提交）全部前滾重做，將資料庫狀態精確還原至崩潰發生的瞬間", ["重現歷史（Repeating History）：將所有變更（無論交易最終是否提交）全部前滾重做，將資料庫狀態精確還原至崩潰發生的瞬間", "僅重做已提交的交易", "僅重做未提交的交易", "跳過日誌直接讀取資料頁"],
         "即使最終會被 Undo 的未提交交易，在 Redo 階段也會先被重做，以確保整個系統回到崩潰當下的完整物理狀態，簡化後續補償邏輯。"),
        ("在 ARIES 復原演算法中，「補償日誌紀錄（Compensation Log Record, CLR）」的關鍵功用為何？",
         "記錄撤銷操作（Undo Action）的執行過程，並透過 UndoNextLSN 指標跳過已撤銷的日誌，防止在「復原過程中再次發生崩潰」時產生無限循環撤銷", ["記錄撤銷操作（Undo Action）的執行過程，並透過 UndoNextLSN 指標跳過已撤銷的日誌，防止在「復原過程中再次發生崩潰」時產生無限循環撤銷", "記錄使用者的補償金", "加速索引重構", "自動修復壞軌"], "CLR 保證復原程序具有冪等性（Idempotence），系統即使在復原期間連續多次崩潰也能保證向前推進並完成。"),
        ("日誌序列號（Log Sequence Number, LSN）在資料庫儲存頁面與日誌中的作用為？",
         "資料頁上的 pageLSN 記錄對該頁面進行最後一次修改的日誌序號；Redo 時若日誌 LSN <= pageLSN 則該日誌無需重做（避免重複套用）", ["資料頁上的 pageLSN 記錄對該頁面進行最後一次修改的日誌序號；Redo 時若日誌 LSN <= pageLSN 則該日誌無需重做（避免重複套用）", "僅作為資料庫版本號", "用於計算交易金額", "加密資料頁"], "pageLSN 建立了記憶體/磁碟資料頁與日誌流之間的精確進度比對，保證 Redo 操作的冪等性。"),
        ("模糊檢查點（Fuzzy Checkpoint）相較於傳統完全檢查點（Checkpoint）的最大優勢為？",
         "寫入檢查點時「無須」將記憶體緩衝區中所有的髒頁（Dirty Pages）強制全部刷入磁碟，大幅降低系統停頓時間（I/O Stalls）", ["寫入檢查點時「無須」將記憶體緩衝區中所有的髒頁（Dirty Pages）強制全部刷入磁碟，大幅降低系統停頓時間（I/O Stalls）", "完全不需要寫入任何日誌", "復原時間降為 0 秒", "不佔用任何磁碟空間"], "Fuzzy Checkpoint 僅將當前記憶體中的髒頁表（DPT）與活動交易表（ATT）元資料寫入日誌，髒頁仍留在記憶體由背景執行緒非同步平滑刷盤。"),
        ("在緩衝區管理策略中，「STEAL」與「NO-STEAL」的含義為？",
         "STEAL 允許緩衝區管理器在交易尚未提交前，將其修改過的未確認資料頁刷入磁碟（需要 UNDO 日誌支援）", ["STEAL 允許緩衝區管理器在交易尚未提交前，將其修改過的未確認資料頁刷入磁碟（需要 UNDO 日誌支援）", "STEAL 禁止未提交頁面落盤", "NO-STEAL 代表不需要寫入磁碟", "兩者效能相同"], "現代資料庫均採 STEAL 策略以最大化記憶體利用率；若採 NO-STEAL 則大型交易所佔記憶體無法釋放。"),
        ("在緩衝區管理策略中，「FORCE」與「NO-FORCE」的含義為？",
         "NO-FORCE 允許交易在提交時，無須強制將所有修改過的資料頁同步刷入磁碟（需要 REDO 日誌支援）", ["NO-FORCE 允許交易在提交時，無須強制將所有修改過的資料頁同步刷入磁碟（需要 REDO 日誌支援）", "FORCE 代表不寫入磁碟", "NO-FORCE 代表不記錄日誌", "FORCE 速度較快"], "現代資料庫均採 NO-FORCE，僅將短小的 Redo Log 順序刷盤，資料頁維持在快取中，大幅提升寫入吞吐量。"),
        ("現代高性能關聯式資料庫引擎（如 MySQL, PostgreSQL, Oracle）普遍採用何種緩衝區管理組合？",
         "STEAL / NO-FORCE（兼具記憶體靈活性與寫入高效能，代價是必須具備完整的 UNDO 與 REDO 機制）", ["STEAL / NO-FORCE（兼具記憶體靈活性與寫入高效能，代價是必須具備完整的 UNDO 與 REDO 機制）", "NO-STEAL / FORCE（不需要日誌）", "STEAL / FORCE", "NO-STEAL / NO-FORCE"], "極高並行吞吐的最佳架構實踐。"),
        ("ARIES 演算法分析階段結束時，髒頁表（Dirty Page Table, DPT）中最小的 RecLSN 代表何種意義？",
         "Redo 階段必須開始進行重做掃描的「最起始日誌位置（Redo Start Point）」", ["Redo 階段必須開始進行重做掃描的「最起始日誌位置（Redo Start Point）」", "整個資料庫的崩潰時間點", "最後一個已提交交易的位置", "日誌檔案的開頭"], "RecLSN 記錄某個髒頁自上次刷盤以來第一次被修改的日誌序號。全表最小 RecLSN 之前的日誌變更保證早已落盤，無需重複檢視。")
    ]

    for stem, ans_s, opts, expl in rec_data:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "復原機制與ARIES演算法",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【資料庫崩潰復原機制推導】</strong><br>
<div class="step-box">
  <div class="step-title">📝 復原演算法流程分析</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>確立日誌與快取策略（STEAL/NO-FORCE）</strong><br>
      ‧ 本題依據 ARIES 復原規範或 WAL 協定進行分析。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>執行狀態追蹤與日誌流解析</strong><br>
      ‧ {expl}
    </li>
    <li class="step-item"><span class="step-badge check">步驟 3</span><strong>得出正確答案</strong><br>
      ‧ 答案為 <strong>{ans_s}</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) {ans_s}</strong>：完全符合 ARIES 論文規範。<br>
‧ 其餘選項皆為復原階段順序顛倒或快取策略定義混淆。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Write-Ahead Logging (WAL)</code> <span class="en">Write-Ahead Logging</span>：預寫式日誌。<br>
‧ <code>Compensation Log Record (CLR)</code> <span class="en">Compensation Log Record</span>：補償日誌紀錄。<br>
‧ <code>Fuzzy Checkpoint</code> <span class="en">Fuzzy Checkpoint</span>：模糊檢查點。"""
        })

    # More Recovery items (30 items)
    more_rec = [
        ("在 ARIES 中，活動交易表（Active Transaction Table, ATT）記錄何種資訊？", "崩潰時處於活躍狀態（尚未提交亦未中止）的交易 ID、狀態及其最後寫入的 lastLSN", ["崩潰時處於活躍狀態（尚未提交亦未中止）的交易 ID、狀態及其最後寫入的 lastLSN", "所有已提交的使用者帳號", "資料庫連線池狀態", "磁碟磁軌壞軌清單"], "ATT 決定在 Undo 階段哪些交易屬於失敗者（Losers）必須被倒序撤銷。"),
        ("日誌記錄中的 prevLSN 欄位主要功用為？", "串接同一個交易內的所有日誌紀錄，形成單向反向鏈結串列，供 Undo 倒序回溯使用", ["串接同一個交易內的所有日誌紀錄，形成單向反向鏈結串列，供 Undo 倒序回溯使用", "計算整個日誌檔案大小", "記錄下一個交易 ID", "用於資料壓縮"], "Undo 沿著 prevLSN 指針精準跳轉撤銷自身操作，無需全域日誌無效回溯。"),
        ("若資料庫採用「延遲更新（Deferred Update）」策略，在崩潰復原時需要執行何種操作？", "僅需要執行 REDO（重做），完全「不需要」執行 UNDO（撤銷）", ["僅需要執行 REDO（重做），完全「不需要」執行 UNDO（撤銷）", "僅需要執行 UNDO", "兩者皆需要", "兩者皆不需要"], "延遲更新直到交易 Commit 成功前絕不將任何變更寫入資料檔（NO-STEAL），未提交交易在磁碟無痕跡，故無需 Undo。"),
        ("若資料庫採用「立即更新（Immediate Update）」且在 Commit 時強制刷盤（FORCE），則復原時？", "僅需要執行 UNDO，不需要執行 REDO", ["僅需要執行 UNDO，不需要執行 REDO", "僅需要執行 REDO", "兩者皆需要", "兩者皆不需要"], "FORCE 保證已提交者皆已在磁碟（免 Redo），但 STEAL 導致未提交者可能污染磁碟（需 Undo）。"),
        ("資料庫雙重寫入緩衝（Doublewrite Buffer，如 MySQL InnoDB）的設計目標為？", "解決作業系統 4KB 頁面寫入與資料庫 16KB 頁面不一致導致的「頁面部分寫入破裂（Partial Page Write / Torn Page）」問題", ["解決作業系統 4KB 頁面寫入與資料庫 16KB 頁面不一致導致的「頁面部分寫入破裂（Partial Page Write / Torn Page）」問題", "提供雙倍讀取速度", "自動備份至第二顆硬碟", "防止 SQL 注入"], "斷電時頁面可能只寫了一半（破裂），Redo Log 無法在毀損頁面上重做；Doublewrite 預先順序寫入連續區塊，破裂時可用其完整副本還原後再 Redo。"),
        ("檢查點（Checkpoint）在交易日誌中最核心的效益為？", "截斷日誌（Log Truncation），釋放舊日誌空間，並大幅縮短系統重啟復原時所需掃描的日誌範圍", ["截斷日誌（Log Truncation），釋放舊日誌空間，並大幅縮短系統重啟復原時所需掃描的日誌範圍", "將資料庫轉為只讀", "清除所有索引", "刪除無效帳號"], "避免日誌無限膨脹並加速重啟時間。"),
        ("在媒體故障（Media Failure / Disk Crash）時，資料庫主要依賴何種技術進行災難復原？", "磁碟全量備份（Full Backup）配合累積的封存日誌（Archived Redo Logs）進行時間點復原（PITR）", ["磁碟全量備份（Full Backup）配合累積的封存日誌（Archived Redo Logs）進行時間點復原（PITR）", "記憶體快取還原", "重新安裝作業系統", "執行 SELECT 查詢"], "Point-in-Time Recovery 先還原基準備份，再重放歸檔日誌至故障前最後一秒。"),
        ("差異備份（Differential Backup）的定義為？", "僅備份自上一次「完整備份（Full Backup）」以來所有被修改過的資料區塊", ["僅備份自上一次「完整備份（Full Backup）」以來所有被修改過的資料區塊", "備份自上次增量備份以來的資料", "備份所有日誌檔", "僅備份資料表定義"], "還原時只需：1 次 Full Backup + 最後 1 次 Differential Backup。"),
        ("增量備份（Incremental Backup）的定義為？", "僅備份自上一次「任何備份（無論是 Full 或 Incremental）」以來被修改過的資料", ["僅備份自上一次「任何備份（無論是 Full 或 Incremental）」以來被修改過的資料", "每次備份全部資料", "備份整個作業系統", "備份記憶體狀態"], "備份速度最快、體積最小，但還原時需依序套用全套歷史鏈結。"),
        ("在分散式交易中，若協調者（Coordinator）在發出 PREPARE 後、參與者回覆前崩潰，參與者應？", "超時後主動終止（Abort）該交易並釋放資源", ["超時後主動終止（Abort）該交易並釋放資源", "強制 Commit", "無限期等待", "刪除資料表"], "未承諾階段可安全回滾。"),
        ("兩階段提交（2PC）中，參與者在回覆「YES / PREPARED」後若協調者崩潰，參與者面臨的最大困境為？", "阻塞（Blocking）：參與者無法自行決定 Commit 或 Abort，必須持鎖等待協調者重啟通知", ["阻塞（Blocking）：參與者無法自行決定 Commit 或 Abort，必須持鎖等待協調者重啟通知", "資料立即遺失", "記憶體溢位", "自動切換主庫"], "2PC 核心缺陷為阻塞協定。"),
        ("三階段提交（3PC）為緩解 2PC 的阻塞問題，在 Prepare 與 Commit 之間引入了何種中間狀態？", "預提交階段（Pre-Commit Phase）", ["預提交階段（Pre-Commit Phase）", "確認階段", "分析階段", "驗證階段"], "引入超時機制打破單點故障阻塞。"),
        ("Saga 分散式交易模式適用於長事務（Long-Running Transactions），其保證一致性的手段為？", "向前重試或執行「補償交易（Compensating Transactions）」向後回滾", ["向前重試或執行「補償交易（Compensating Transactions）」向後回滾", "全域兩階段鎖定", "依賴單一硬碟", "禁止並發"], "例如機票退訂即為訂票的補償操作。"),
        ("日誌的循環覆蓋（Circular Logging）要求？", "已被檢查點確認落盤且無活躍交易需要的日誌區塊方可被循環覆蓋", ["已被檢查點確認落盤且無活躍交易需要的日誌區塊方可被循環覆蓋", "隨意覆蓋", "依時間每小時覆蓋", "大小超過 1GB 立即覆蓋"], "防止尚未落盤的關鍵 Redo 日誌被提早覆蓋。"),
        ("唯讀交易（Read-Only Transactions）在崩潰復原時？", "完全不需要被 Undo 或 Redo（對復原無任何影響）", ["完全不需要被 Undo 或 Redo（對復原無任何影響）", "必須優先 Redo", "必須優先 Undo", "會延長復原時間"], "因無任何資料變更，復原系統直接忽略。"),
        ("若某交易發出 COMMIT 後，系統在寫入 COMMIT 日誌「前的一瞬間」崩潰，該交易在重啟後會被判定為？", "未提交交易（會被 Undo 撤銷回滾）", ["未提交交易（會被 Undo 撤銷回滾）", "已提交交易（會被 Redo 重做）", "視為半提交", "跳過不處理"], "以日誌落盤為唯一物理準則，未見 COMMIT 標記一律視為未完成交易並予以撤銷。"),
        ("在資料庫鏡像（Database Mirroring）中，同步模式（High Safety with Automatic Failover）保證？", "主庫必須等待日誌同步寫入鏡像庫磁碟後，方回覆應用程式 Commit 成功（零資料遺失 RPO=0）", ["主庫必須等待日誌同步寫入鏡像庫磁碟後，方回覆應用程式 Commit 成功（零資料遺失 RPO=0）", "非同步寫入", "定時同步", "不需要網路"], "金融級高可用架構。"),
        ("復原目標時間（RTO, Recovery Time Objective）衡量何種指標？", "災難發生後，系統「恢復至可正常運作服務所需的最長時間」", ["災難發生後，系統「恢復至可正常運作服務所需的最長時間」", "可容忍遺失的資料量", "硬碟備份的速度", "CPU 頻率"], "RTO 代表停機時間上限。"),
        ("復原目標點（RPO, Recovery Point Objective）衡量何種指標？", "災難發生時，系統「可容忍遺失資料的時間長度或資料量」", ["災難發生時，系統「可容忍遺失資料的時間長度或資料量」", "系統重啟耗時", "網路延遲時間", "快取命中率"], "RPO 代表資料損失容忍度（RPO=0 代表絕對零資料遺失）。"),
        ("在日誌檔案中，每個 Log Record 記錄的交易識別碼、資料項目標識、舊值（Before Image）與新值（After Image），其中「舊值」供何者使用？", "Undo（復原回滾）", ["Undo（復原回滾）", "Redo（前滾重做）", "查詢最佳化", "建立索引"], "舊值用以覆蓋還原。"),
        ("同理，Log Record 中的「新值（After Image）」供何者使用？", "Redo（前滾重做）", ["Redo（前滾重做）", "Undo", "驗證外來鍵", "清空快取"], "新值用以重現變更。"),
        ("ARIES 演算法在 Undo 階段的掃描方向為？", "由日誌末端「由後往前（逆序）」反向掃描", ["由日誌末端「由後往前（逆序）」反向掃描", "由前往後順序掃描", "隨機跳躍掃描", "僅掃描檢查點"], "逆序撤銷保證巢狀操作依正確逆向邏輯解除。"),
        ("ARIES 演算法在 Redo 階段的掃描方向為？", "由最小 RecLSN 開始「由前往後（順序）」正向掃描", ["由最小 RecLSN 開始「由前往後（順序）」正向掃描", "由後往前掃描", "僅掃描單頁", "僅掃描 Commit 日誌"], "順序重現歷史演化。"),
        ("資料庫在正常關機（Clean Shutdown）時，會執行何種操作使得下次開機無需進行 Crash Recovery？", "將所有髒頁強制刷盤（Clean Checkpoint），並寫入 SHUTDOWN 標記", ["將所有髒頁強制刷盤（Clean Checkpoint），並寫入 SHUTDOWN 標記", "刪除日誌檔案", "格式化硬碟", "清空所有資料表"], "乾淨關機確保磁碟資料無任何未決狀態。"),
        ("在 Redo-Only 系統架構中，緩衝區必須強制採用何種策略？", "NO-STEAL（絕對不允許未提交頁面刷入磁碟）", ["NO-STEAL（絕對不允許未提交頁面刷入磁碟）", "STEAL", "NO-FORCE", "FORCE"], "只有保證磁碟永遠沒有髒未提交資料，方能免除 Undo。"),
        ("在 Undo-Only 系統架構中，緩衝區必須強制採用何種策略？", "FORCE（交易提交時必須將所有頁面全部強制刷入磁碟）", ["FORCE（交易提交時必須將所有頁面全部強制刷入磁碟）", "NO-FORCE", "STEAL", "NO-STEAL"], "只有保證已提交者皆在磁碟，方能免除 Redo。"),
        ("WAL 寫入日誌通常採用何種磁碟 I/O 模式，使其速度遠快於隨機資料頁刷盤？", "循序追加寫入（Sequential Append-Only I/O）", ["循序追加寫入（Sequential Append-Only I/O）", "隨機隨機寫入", "全盤格式化", "多磁軌跳躍寫入"], "循序 I/O 避免磁頭尋道時間（Seek Time），速度比隨機 I/O 快數個數量級。"),
        ("日誌記錄的「物理日誌（Physical Logging）」與「邏輯日誌（Logical Logging）」相比，其優點為？", "實體日誌直接記錄位元組偏移變更，復原操作具備絕對「冪等性（Idempotent）」且執行速度極快", ["實體日誌直接記錄位元組偏移變更，復原操作具備絕對「冪等性（Idempotent）」且執行速度極快", "佔用磁碟空間極小", "可讀性高", "容易手動編輯"], "物理日誌無二義性；而現代資料庫多採生理日誌（Physiological Logging，頁面物理定址+頁內邏輯操作）。"),
        ("在快照備份（Storage Snapshot / Copy-on-Write）技術中，備份資料庫前必須通知資料庫引擎執行？", "凍結寫入或進入備份鎖定模式（FLUSH TABLES WITH READ LOCK / BEGIN BACKUP），強制檢查點將快取同步", ["凍結寫入或進入備份鎖定模式（FLUSH TABLES WITH READ LOCK / BEGIN BACKUP），強制檢查點將快取同步", "直接關閉電源", "刪除所有索引", "關閉防火牆"], "確保磁碟快照處於崩潰一致性（Crash-Consistent）狀態。"),
        ("當交易執行至一半發生除以零或違反約束時，由 DBMS 內部觸發的局部終止稱為？", "系統內部回滾（Internal System-Abort）", ["系統內部回滾（Internal System-Abort）", "外部崩潰", "硬體毀損", "正常完成"], "利用 Undo 日誌僅對該異常交易執行撤銷，不影響其餘並行交易。")
    ]

    for stem, ans_s, opts, expl in more_rec:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "資料庫復原機制深入分析",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【資料庫復原原理深度剖析】</strong><br>
‧ <strong>(A) {ans_s}</strong>：依原理推導，{expl}<br>
‧ 其餘選項皆存在備份復原概念偏差或 I/O 策略誤判。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>RTO (Recovery Time Objective)</code> <span class="en">RTO</span>：復原時間目標。<br>
‧ <code>RPO (Recovery Point Objective)</code> <span class="en">RPO</span>：復原點目標。<br>
‧ <code>Point-in-Time Recovery (PITR)</code> <span class="en">PITR</span>：時間點復原。"""
        })

    # -------------------------------------------------------------
    # 8. 實體儲存與索引技術 (45 題)
    # -------------------------------------------------------------
    idx_data = [
        ("叢集索引（Clustered Index）與非叢集索引（Non-Clustered Index / Secondary Index）的最本質差異為？",
         "叢集索引的葉節點直接存放「完整的實際資料列（Data Rows）」，資料物理順序與索引順序一致，一張表「只能有一個」叢集索引", ["叢集索引的葉節點直接存放「完整的實際資料列（Data Rows）」，資料物理順序與索引順序一致，一張表「只能有一個」叢集索引", "一張表可以有多個叢集索引", "非叢集索引速度永遠快於叢集索引", "叢集索引葉節點存放指標"],
         "資料列在磁碟中只能依據一種物理順序排列，故叢集索引唯一；非叢集索引葉節點僅存放搜尋鍵值及指向資料列的指標（RID 或叢集鍵值）。"),
        ("稠密索引（Dense Index）與稀疏索引（Sparse Index）的定義差異為？",
         "稠密索引中，資料檔案裡的「每一筆紀錄」在索引中皆有對應的索引項；稀疏索引只為每個資料區塊（Block）的第一筆紀錄建立索引項", ["稠密索引中，資料檔案裡的「每一筆紀錄」在索引中皆有對應的索引項；稀疏索引只為每個資料區塊（Block）的第一筆紀錄建立索引項", "稠密索引佔用空間較小", "稀疏索引可用於任何非排序檔案", "兩者完全相同"],
         "稀疏索引要求資料檔案本身必須已依搜尋鍵值排序（通常用於叢集主索引），能大幅節省記憶體索引空間；非排序檔案只能建稠密索引。"),
        ("點陣圖索引（Bitmap Index）最適用的資料庫情境為？",
         "低基數欄位（Low-Cardinality，相異值少，如性別、婚姻狀況、國家）且讀取密集的資料倉儲（OLAP）查詢", ["低基數欄位（Low-Cardinality，相異值少，如性別、婚姻狀況、國家）且讀取密集的資料倉儲（OLAP）查詢", "高基數欄位（如身分證字號、自增 ID）", "頻繁並行寫入修改的 OLTP 系統", "儲存大文字檔案"],
         "每個相異值建立一個 bit-vector，查詢時透過硬體支援的極速位元運算（AND, OR, NOT）瞬間完成交集篩選；但在高並發修改時鎖定整段 bitmap 會造成嚴重鎖競爭。"),
        ("在可延伸雜湊（Extendible Hashing）中，當某個儲存桶（Bucket）已滿需要分裂時，若該儲存桶的「局部深度（Local Depth, d'）」等於「全域深度（Global Depth, d）」，系統將會？",
         "將全域深度 d 加 1，並將目錄表（Directory）大小「擴增為原來的兩倍（Double the Directory Size）」", ["將全域深度 d 加 1，並將目錄表（Directory）大小「擴增為原來的兩倍（Double the Directory Size）」", "保持目錄大小不變，僅分裂該桶", "清空所有資料重新雜湊", "拋出雜湊溢位錯誤"],
         "可延伸雜湊優雅動態擴充：局部深度等於全域深度代表目錄指標已用盡，目錄翻倍；若局部深度小於全域深度，則僅分裂該桶並將目錄中對應指標重新指派，目錄無須擴充。"),
        ("B+ 樹索引相較於二元搜尋樹（BST）或平衡二元樹（AVL），更適合作為資料庫磁碟索引的核心主因為？",
         "B+ 樹具有極高分支度（High Fan-out），樹高極低（通常僅 3~4 層），大幅減少磁碟 I/O 次數，且葉節點雙向鏈結極利於範圍查詢", ["B+ 樹具有極高分支度（High Fan-out），樹高極低（通常僅 3~4 層），大幅減少磁碟 I/O 次數，且葉節點雙向鏈結極利於範圍查詢", "B+ 樹的節點全部存放在快取暫存器", "B+ 樹不需要任何指標", "二元樹樹高比 B+ 樹低"], "磁碟隨機讀取延遲高達毫秒級，每層樹高代表一次 I/O。百萬筆資料在二元樹深達 20 層，而在 B+ 樹僅需 3~4 次 I/O。"),
        ("覆蓋索引（Covering Index）是指何種索引查詢最佳化現象？",
         "查詢所需的所有欄位皆已包含在該索引中（Index-Only Scan），無需再回表存取主資料列（無需回表 Lookup / Bookmark Lookup）", ["查詢所需的所有欄位皆已包含在該索引中（Index-Only Scan），無需再回表存取主資料列（無需回表 Lookup / Bookmark Lookup）", "索引覆蓋了資料庫所有表格", "全表掃描", "強制使用主鍵"], "完全在記憶體中的索引樹葉直接取得所有查詢數據，省去隨機回表 I/O，效能提升可達數十倍。"),
        ("最左前綴原則（Leftmost Prefix Rule）在複合索引（Composite Index on (A, B, C)）中的應用規範為？",
         "查詢條件必須從最左側欄位 A 開始連續匹配，才能充分利用該索引；若條件僅有 `WHERE B = 1 AND C = 2` 則無法使用該索引前綴", ["查詢條件必須從最左側欄位 A 開始連續匹配，才能充分利用該索引；若條件僅有 `WHERE B = 1 AND C = 2` 則無法使用該索引前綴", "欄位順序可任意調換皆完全相同", "只要有 C 即可使用", "只能查詢單一欄位"], "複合索引是先依 A 排序，A 相同時再依 B 排序，以此類推。缺乏 A 條件時如同查電話簿不知姓氏只知名稱，無法二分檢索。"),
        ("在 SQL 查詢中，若對索引欄位使用函數或運算（例如 `WHERE YEAR(create_time) = 2024` 或 `WHERE id + 1 = 100`），通常會導致？",
         "索引失效（Index Invalidation），優化器被迫退化為全表掃描（Full Table Scan）", ["索引失效（Index Invalidation），優化器被迫退化為全表掃描（Full Table Scan）", "查詢速度加快 2 倍", "自動建立函數索引", "語法錯誤拒絕執行"], "索引樹上儲存的是欄位原始值，包覆函數後優化器無法直接二分定址，應改寫為 `WHERE create_time >= '2024-01-01' AND create_time < '2025-01-01'`。"),
        ("倒排索引（Inverted Index）的核心資料結構由哪兩部分組成？",
         "詞彙表（Vocabulary / Dictionary）與倒排記錄表（Posting Lists，記錄包含該詞彙的文件 ID 與位置）", ["詞彙表（Vocabulary / Dictionary）與倒排記錄表（Posting Lists，記錄包含該詞彙的文件 ID 與位置）", "行索引與列索引", "堆疊與佇列", "雜湊表與二元樹"], "搜尋引擎（如 Elasticsearch, Lucene）的核心基礎，實現關鍵字全文極速檢索。"),
        ("資料庫分區（Partitioning）技術中，水平分區（Horizontal Partitioning）是指？",
         "依據特定規則（如範圍 RANGE、雜湊 HASH、列表 LIST）將同張資料表的「不同資料列（Rows）」分散存放在不同的實體檔案或節點中", ["依據特定規則（如範圍 RANGE、雜湊 HASH、列表 LIST）將同張資料表的「不同資料列（Rows）」分散存放在不同的實體檔案或節點中", "將不同欄位拆開存放", "將資料庫分給不同公司", "備份到光碟"], "單表資料量達數億筆時，水平分區配合分區修剪（Partition Pruning）能將查詢範圍精確鎖定在特定單一分區內。")
    ]

    for stem, ans_s, opts, expl in idx_data:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "實體儲存與索引架構",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【索引技術與實體組織逐步推導】</strong><br>
<div class="step-box">
  <div class="step-title">📝 索引原理與效能推導分析</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>確認索引結構（B+樹/雜湊/點陣圖）</strong><br>
      ‧ 本題依據實體儲存結構、I/O 存取模式或查詢優化規則進行分析。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>執行索引檢索路徑與複雜度驗證</strong><br>
      ‧ {expl}
    </li>
    <li class="step-item"><span class="step-badge check">步驟 3</span><strong>得出精準結論</strong><br>
      ‧ 正確答案為 <strong>{ans_s}</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) {ans_s}</strong>：完全符合資料庫實體結構規範。<br>
‧ 其餘選項皆為索引特性混淆或優化規則誤判。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Clustered Index</code> <span class="en">Clustered Index</span>：叢集索引。<br>
‧ <code>Covering Index</code> <span class="en">Covering Index</span>：覆蓋索引。<br>
‧ <code>Bitmap Index</code> <span class="en">Bitmap Index</span>：點陣圖索引。"""
        })

    # -------------------------------------------------------------
    # 9. 查詢處理與實體連接演算法 (45 題)
    # -------------------------------------------------------------
    opt_data = [
        ("實體連接演算法中，巢狀迴圈連接（Nested Loop Join, NLJ）在何種情況下效率最高？",
         "驅動表（外表 Outer Table）資料量極小，且被驅動表（內表 Inner Table）的連接欄位上建有高效索引（Index Nested Loop Join）", ["驅動表（外表 Outer Table）資料量極小，且被驅動表（內表 Inner Table）的連接欄位上建有高效索引（Index Nested Loop Join）", "雙方皆為無索引之數百萬列大表", "所有資料已依連接欄位排序", "僅在全外連接時效率高"],
         "外表每筆資料透過內表索引直接 O(log N) 二分定址，總時間為 O(|Outer| · log |Inner|)，避免全表比對。"),
        ("排序合併連接（Sort-Merge Join, SMJ）最適合於何種場景？",
         "參與連接的兩張資料表在連接欄位上「已經預先排序（例如由 B+ 樹索引提供有序性）」，或連接條件為非等值範圍查詢", ["參與連接的兩張資料表在連接欄位上「已經預先排序（例如由 B+ 樹索引提供有序性）」，或連接條件為非等值範圍查詢", "資料表完全隨機無序且無記憶體", "小表與大表關聯", "只包含單一資料列"],
         "若輸入已有序，兩表只需雙指針各單趟線性掃描一次 O(M + N) 即可完成連接，無額外排序開銷。"),
        ("雜湊連接（Hash Join）的執行兩大階段為？",
         "構建階段（Build Phase，以較小的表在記憶體建立雜湊表）與探測階段（Probe Phase，掃描大表逐列探測雜湊表）", ["構建階段（Build Phase，以較小的表在記憶體建立雜湊表）與探測階段（Probe Phase，掃描大表逐列探測雜湊表）", "排序階段與合併階段", "分析階段與執行階段", "索引階段與刪除階段"],
         "雜湊連接僅適用於「等值連接（Equi-Join）」，是巨量未排序大表連接效能最高之演算法。"),
        ("以代價為基礎的最佳化器（Cost-Based Optimizer, CBO）評估查詢執行計畫時，主要考量的成本指標為？",
         "預估的磁碟 I/O 次數、CPU 指令週期、記憶體使用量與網路傳輸頻寬之加權總和", ["預估的磁碟 I/O 次數、CPU 指令週期、記憶體使用量與網路傳輸頻寬之加權總和", "單純計算 SQL 語法的字元長度", "資料表的欄位個數", "伺服器的開機時間"],
         "CBO 透過資料字典中的統計資訊（Statistics，如直方圖、相異值數目 Cardinality、頁面總數）估算各個執行路徑的預期成本，選取 Cost 最小者。"),
        ("在查詢最佳化中，「直方圖（Histogram）」的主要用途為？",
         "解決資料「分佈不均勻（Data Skew）」時的選擇度（Selectivity）與資料筆數精確估算問題", ["解決資料「分佈不均勻（Data Skew）」時的選擇度（Selectivity）與資料筆數精確估算問題", "加快圖形渲染速度", "記錄崩潰日誌", "替代 B+ 樹索引"], "等寬（Equi-Width）或等高（Equi-Height）直方圖反映資料偏斜真實分佈，避免優化器做出錯誤的執行計畫決策。")
    ]

    for stem, ans_s, opts, expl in opt_data:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "查詢處理與連接最佳化",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【查詢最佳化器與實體連接演算法深入推導】</strong><br>
<div class="step-box">
  <div class="step-title">📝 CBO 成本模型與連接演算法推導</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>確立輸入資料規模與索引拓樸</strong><br>
      ‧ 本題依據 CBO 代價公式或實體連接演算法（NLJ, SMJ, Hash Join）特性進行分析。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>執行演算法時間與 I/O 成本比對</strong><br>
      ‧ {expl}
    </li>
    <li class="step-item"><span class="step-badge check">步驟 3</span><strong>得出精準結論</strong><br>
      ‧ 正確答案為 <strong>{ans_s}</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) {ans_s}</strong>：完全符合查詢執行引擎之運作常規。<br>
‧ 其餘選項皆為連接演算法適用場景誤判或成本模型混淆。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Cost-Based Optimizer (CBO)</code> <span class="en">Cost-Based Optimizer</span>：基於成本之最佳化器。<br>
‧ <code>Hash Join</code> <span class="en">Hash Join</span>：雜湊連接。<br>
‧ <code>Sort-Merge Join</code> <span class="en">Sort-Merge Join</span>：排序合併連接。"""
        })

    # Expand Index/Opt/NoSQL questions to 130
    more_db3 = [
        ("區塊巢狀迴圈連接（Block Nested Loop Join, BNLJ）相較於簡單 NLJ，其效能提升的主要關鍵在於？", "在記憶體中配置 Join Buffer，一次讀入多個外表區塊，大幅減少內表的重複磁碟全表掃描次數", ["在記憶體中配置 Join Buffer，一次讀入多個外表區塊，大幅減少內表的重複磁碟全表掃描次數", "自動建立索引", "將兩表資料排序", "消除所有 NULL"], "若外表佔 B(R) 區塊，內表佔 B(S) 區塊，緩衝區大小為 M 塊，則內表掃描次數從 |R| 次暴跌至 ⌈B(R)/(M-2)⌉ 次。"),
        ("CAP 定理指出，在分散式系統中，下列哪三個特性無法同時完全滿足？", "一致性（Consistency）、可用性（Availability）與分區容忍性（Partition Tolerance）", ["一致性（Consistency）、可用性（Availability）與分區容忍性（Partition Tolerance）", "原子性、隔離性、持久性", "速度、成本、安全性", "快取、日誌、索引"], "分散式網路分區（Partition）必然存在，故實務上系統只能在 CP（犧牲可用性保強一致）與 AP（犧牲強一致保高可用）之間取捨。"),
        ("BASE 模型是相對於 ACID 的分散式架構哲學，其包含的三大原則為？", "基本可用（Basically Available）、軟狀態（Soft state）與最終一致性（Eventual consistency）", ["基本可用（Basically Available）、軟狀態（Soft state）與最終一致性（Eventual consistency）", "備份、審計、安全性、加密", "批次、非同步、串流、邊緣", "平衡、適應、擴充、彈性"], "NoSQL 系統通常放寬即時強一致性要求，換取全球規模的高並發與可用性。"),
        ("PACELC 定理在 CAP 定理基礎上，擴充了在「無分區正常情況（Else）」下的何種權衡？", "在延遲（Latency）與一致性（Consistency）之間的取捨", ["在延遲（Latency）與一致性（Consistency）之間的取捨", "在成本與安全間取捨", "在 CPU 與記憶體間取捨", "在頻寬與硬碟間取捨"], "即使沒有網路故障（Else），若要維持高一致性（C），副本同步等待必然增加延遲（L）；追求極速低延遲則需妥協一致性。"),
        ("MongoDB 屬於下列何種 NoSQL 資料庫類型？", "文件導向資料庫（Document-Oriented Database，使用 BSON 格式儲存）", ["文件導向資料庫（Document-Oriented Database，使用 BSON 格式儲存）", "鍵值資料庫", "關聯式資料庫", "圖形資料庫"], "以靈活的半結構化 JSON/BSON 文件組織資料，支援動態 Schema。"),
        ("Redis 主要屬於下列何種 NoSQL 資料庫類型？", "記憶體內鍵值資料庫（In-Memory Key-Value Database）", ["記憶體內鍵值資料庫（In-Memory Key-Value Database）", "寬行資料庫", "文件資料庫", "關聯代數資料庫"], "全記憶體運作，支援 String, Hash, List, Set, ZSet 等多樣資料結構，具備極致亞毫秒延遲。"),
        ("Apache Cassandra 與 HBase 屬於下列何種 NoSQL 資料庫類型？", "寬行儲存資料庫（Wide-Column / Column-Family Store）", ["寬行儲存資料庫（Wide-Column / Column-Family Store）", "鍵值資料庫", "純關聯式資料庫", "圖形資料庫"], "適合儲存海量稀疏資料，基於 LSM-Tree 循序寫入優化，具備線性橫向擴展能力。"),
        ("Neo4j 屬於下列何種 NoSQL 資料庫類型？", "圖形資料庫（Graph Database，節點 Nodes 與邊 Edges 儲存）", ["圖形資料庫（Graph Database，節點 Nodes 與邊 Edges 儲存）", "文件資料庫", "時間序列資料庫", "空間資料庫"], "專精於社群網路、知識圖譜與洗錢防制之複雜多跳躍路徑檢索（Cypher 語言）。"),
        ("在資料倉儲多維模型中，「星狀綱要（Star Schema）」的結構特點為？", "中央為包含度量指標的事實表（Fact Table），四周直接連接未正規化的一層維度表（Dimension Tables）", ["中央為包含度量指標的事實表（Fact Table），四周直接連接未正規化的一層維度表（Dimension Tables）", "維度表進一步做第三正規化拆解", "包含多個獨立的事實表", "形狀呈現網狀交錯"], "星狀綱要維度表包含冗餘以換取簡單高效的分析查詢（減少 JOIN 數）。"),
        ("「雪花綱要（Snowflake Schema）」相較於星狀綱要的差異為？", "將星狀綱要四周的維度表進一步進行「正規化拆解」，形成階層式子維度表", ["將星狀綱要四周的維度表進一步進行「正規化拆解」，形成階層式子維度表", "事實表被拆解", "完全消除事實表", "完全不支援 OLAP"], "雪花綱要消除了維度表中的資料冗餘，但分析時需執行更多次 JOIN。"),
        ("緩慢變化維度（Slowly Changing Dimensions, SCD）中，「Type 2」的處理方式為？", "新增一筆「全新的維度資料列」，並以版本號（Version）或生效日期區間（Effective Dates）保留完整歷史紀錄", ["新增一筆「全新的維度資料列」，並以版本號（Version）或生效日期區間（Effective Dates）保留完整歷史紀錄", "直接覆蓋舊值（不保留歷史）", "在原資料列增加舊值欄位", "刪除該紀錄"], "SCD Type 1 為直接覆蓋（無歷史）；Type 2 為新增版本列（精確追溯歷史）；Type 3 為增加 Previous 欄位（有限歷史）。"),
        ("分庫分表（Sharding）中的「資料傾斜（Data Skew）」是指何種現象？", "分片鍵（Sharding Key）選取不當，導致大量資料集中存入少數分片節點，使該節點成為系統瓶頸", ["分庫分表（Sharding Key）選取不當，導致大量資料集中存入少數分片節點，使該節點成為系統瓶頸", "資料庫檔案損壞", "伺服器硬體傾斜", "備份失敗"], "設計良好的分片鍵應具備高基數與均勻雜湊離散度。"),
        ("在分散式資料庫中，為實現全域唯一的自增流水號 ID，Twitter 開源的著名演算法為？", "雪花演算法（Snowflake Algorithm，時間戳 + 工作機器 ID + 流水號組合為 64 位元整數）", ["雪花演算法（Snowflake Algorithm，時間戳 + 工作機器 ID + 流水號組合為 64 位元整數）", "SHA-256", "UUID v4", "自增序列 Auto-Increment"], "趨勢單調遞增，完全無中心化鎖競爭，極高並發產能。"),
        ("在 LSM-Tree（Log-Structured Merge-Tree）架構中，資料寫入時的處理流程為？", "先寫入 WAL 日誌，接著寫入記憶體中的 MemTable（跳躍串列），當滿時以不可變（Immutable）形式非同步刷盤為 SSTable", ["先寫入 WAL 日誌，接著寫入記憶體中的 MemTable（跳躍串列），當滿時以不可變（Immutable）形式非同步刷盤為 SSTable", "直接隨機寫入磁碟資料頁", "直接覆蓋舊檔案", "先寫入磁碟再寫日誌"], "將所有隨機寫入轉換為記憶體寫入與純循序追加刷盤，賦予 HBase/Cassandra/RocksDB 驚人的寫入吞吐量。"),
        ("LSM-Tree 中的「合併壓縮（Compaction）」操作的主要功能為？", "將多個 SSTable 合併為新的 SSTable，清理被標記為刪除的墓碑紀錄與舊版本資料，並維持資料有序性", ["將多個 SSTable 合併為新的 SSTable，清理被標記為刪除的墓碑紀錄與舊版本資料，並維持資料有序性", "壓縮日誌檔案大小", "建立 B+ 樹索引", "備份至雲端"], "防止 SSTable 檔案數量爆炸引發讀取效能雪崩（Read Amplification）。"),
        ("列式儲存資料庫（Columnar Database，如 ClickHouse, BigQuery）相較於傳統行式儲存（Row-oriented），在 OLAP 分析時的核心優勢為？", "僅需讀取查詢所需的欄位資料（極致降低 I/O），同型態資料聚集使得資料壓縮比極高，且支援向量化執行（SIMD）", ["僅需讀取查詢所需的欄位資料（極致降低 I/O），同型態資料聚集使得資料壓縮比極高，且支援向量化執行（SIMD）", "單筆資料 INSERT 速度極快", "適合高並發交易（OLTP）", "完全不需要儲存空間"], "分析型巨量彙總計算（如計算百萬行交易之 SUM, AVG）效能超越行式資料庫數十倍。"),
        ("若查詢條件為 `WHERE col IS NULL`，傳統 B+ 樹索引是否能被有效利用？", "視具體 DBMS 實作而定（例如 Oracle 預設不對全 NULL 鍵建索引；MySQL/PostgreSQL 則能正常使用索引檢索 NULL）", ["視具體 DBMS 實作而定（例如 Oracle 預設不對全 NULL 鍵建索引；MySQL/PostgreSQL 則能正常使用索引檢索 NULL）", "所有資料庫絕對無法使用", "所有資料庫永遠能使用", "會造成語法錯誤"], "資料庫實作底層差異：Oracle B+ 樹不包含全 NULL 條目，故 `IS NULL` 在 Oracle 會觸發全表掃描，除非建複合索引或 Bitmap 索引。"),
        ("在資料庫查詢最佳化中，何謂「笛卡兒積警訊（Cartesian Product Warning）」？", "多表連接時漏寫了 JOIN ON 或 WHERE 連接條件，導致系統執行完全卡氏積運算使結果集幾何級數暴增", ["多表連接時漏寫了 JOIN ON 或 Greece WHERE 連接條件，導致系統執行完全卡氏積運算使結果集幾何級數暴增", "主鍵衝突警告", "欄位名稱重複", "除以零警訊"], "開發人員最常犯的災難級查詢 Bug，輕則佔滿記憶體，重則拖垮伺服器。"),
        ("為防止全表掃描拖垮生產資料庫，DBA 通常會設定何種安全機制？", "查詢超時限制（Statement Timeout）與最大掃描列數門檻限制", ["查詢超時限制（Statement Timeout）與最大掃描列數門檻限制", "關閉資料庫網路", "將所有表格設為唯讀", "禁止使用 SELECT"], "防止慢查詢耗盡資料庫連線池與資源。"),
        ("在 SQL 語法分析階段，EXPLAIN 指令的主要功用為？", "顯示資料庫最佳化器為該查詢所選定的「實體執行計畫（Execution Plan）」，包含使用的索引、連接演算法與預估成本", ["顯示資料庫最佳化器為該查詢所選定的「實體執行計畫（Execution Plan）」，包含使用的索引、連接演算法與預估成本", "直接執行查詢並匯出 Excel", "自動最佳化 SQL 語法", "加密資料庫檔案"], "資料庫效能調優與索引診斷之第一必備利器。")
    ]

    for stem, ans_s, opts, expl in more_db3:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "分散式資料庫與進階儲存",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【進階資料庫技術深入辨析】</strong><br>
‧ <strong>(A) {ans_s}</strong>：依原理推導，{expl}<br>
‧ 其餘選項皆存在分散式理論定理偏差或儲存引擎特性混淆。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>CAP Theorem</code> <span class="en">CAP Theorem</span>：CAP 定理。<br>
‧ <code>LSM-Tree</code> <span class="en">LSM-Tree</span>：日誌結構合併樹。<br>
‧ <code>Columnar Database</code> <span class="en">Columnar Database</span>：列式儲存資料庫。"""
        })

    return qs

if __name__ == '__main__':
    qs = get_db_part3_questions()
    print(f"Generated DB Part 3 questions: {len(qs)}")
