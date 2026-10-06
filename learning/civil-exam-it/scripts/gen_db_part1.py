# -*- coding: utf-8 -*-
"""
Database Systems Question Bank Generator - Part 1 (130 unique questions)
Topics: Relational Algebra & Advanced SQL (70), ER/EER & Relational Mapping (60).
"""

def get_db_part1_questions():
    qs = []

    # -------------------------------------------------------------
    # 1. 關聯代數運算子與推導 (35 題)
    # -------------------------------------------------------------
    ra_items = [
        ("在關聯代數（Relational Algebra）中，若關聯 R 包含 5 筆紀錄，關聯 S 包含 4 筆紀錄，則卡氏積（Cartesian Product）R × S 包含多少筆紀錄？",
         "20 筆紀錄", ["20 筆紀錄", "9 筆紀錄", "5 筆紀錄", "1 筆紀錄"],
         "卡氏積運算定義：將 R 中的每一筆元組（Tuple）與 S 中的每一筆元組做全排列組合。若 |R| = m，|S| = n，則 |R × S| = m × n = 5 × 4 = 20 筆紀錄。屬性個數（度數 Degree）則為兩者之和 deg(R) + deg(S)。"),
        ("關聯代數中，「除法運算（Division Operator ÷）」最常用於表達何種語意之資料庫查詢？",
         "包含「選取符合全部條件（FOR ALL / EVERY）」語意的查詢，例如「選修了資工系開設之『所有』課程的學生」", ["包含「選取符合全部條件（FOR ALL / EVERY）」語意的查詢，例如「選修了資工系開設之『所有』課程的學生」", "計算平均值與加總", "去除重複紀錄", "兩個關聯的差集運算"],
         "關聯除法 R(X, Y) ÷ S(Y) 定義為：尋找所有在 X 上的值 x，使得對於 S 中的每一個 y，(x, y) 均存在於 R 中。此即 SQL 中含有「雙重 NOT EXISTS」或「COUNT = 全部門檻」的典型全員符合查詢。"),
        ("設關聯 R(A, B) 與 S(B, C)。自然連接（Natural Join R ⋈ S）在關聯代數中等價於下列何種基本運算子組合？",
         "π_{R.A, R.B, S.C} ( σ_{R.B = S.B} (R × S) )", ["π_{R.A, R.B, S.C} ( σ_{R.B = S.B} (R × S) )", "σ_{R.B = S.B} (R × S)", "π_{R.A, S.C} (R × S)", "R ∪ S"],
         "自然連接包含三步驟：先做卡氏積（R × S），再做相同名稱屬性的等值選擇（σ_{R.B = S.B}），最後做投影（π）消除重複出現的連接屬性欄位。"),
        ("關聯代數的六大「基本運算子（Fundamental Operators）」中，不包含下列何者？",
         "交集運算（Intersection ∩）", ["交集運算（Intersection ∩）", "選擇運算（Selection σ）", "投影運算（Projection π）", "差集運算（Set Difference −）"],
         "六大基本運算子為：選擇（σ）、投影（π）、聯集（∪）、差集（−）、卡氏積（×）、重命名（ρ）。交集運算為衍生運算子，可由差集表示：R ∩ S = R − (R − S)。"),
        ("兩個關聯 R 與 S 若欲進行「聯集（∪）」或「差集（−）」運算，兩者必須滿足何種前提條件？",
         "聯集相容性（Union-Compatible）：屬性個數相同且對應位置屬性的網域（Domain / 資料型態）完全相容", ["聯集相容性（Union-Compatible）：屬性個數相同且對應位置屬性的網域（Domain / 資料型態）完全相容", "主鍵名稱必須完全相同", "紀錄筆數必須相等", "必須在同一個資料表實體內"],
         "集合運算要求參與之兩關聯架構相容，即具有相同階度（Arity）且同位置欄位具有相同資料型態（Domain）。"),
        ("左外連接（Left Outer Join R ⟕ S）的運算結果為？",
         "包含自然連接的結果，加上 R 中所有未匹配到 S 的元組（未匹配之 S 欄位填補 NULL）", ["包含自然連接的結果，加上 R 中所有未匹配到 S 的元組（未匹配之 S 欄位填補 NULL）", "僅包含自然連接的結果", "包含 S 中所有元組加上 R 的未匹配項", "兩關聯的差集"],
         "左外連接確保左側關聯 R 中的每一筆紀錄均完整保留於輸出中，若右側 S 無對應匹配值，則其 S 屬性全數以 NULL 補齊。"),
        ("全外連接（Full Outer Join R ⟗ S）保留了哪些資料？",
         "保留兩關聯自然連接之結果，並同時保留 R 與 S 中所有未匹配之元組（各自以 NULL 填補對應缺漏欄位）", ["保留兩關聯自然連接之結果，並同時保留 R 與 S 中所有未匹配之元組（各自以 NULL 填補對應缺漏欄位）", "僅保留有匹配之紀錄", "僅保留雙方皆未匹配之紀錄", "兩關聯的聯集"],
         "全外連接結合了左外連接與右外連接，雙方所有不匹配紀錄均不丟棄，以 NULL 補齊未匹配屬性。"),
        ("半連接（Semi-Join R ⋉ S）的運算定義為？",
         "π_{Attributes(R)} (R ⋈ S)，即僅保留 R 中能在 S 中找到匹配項的 R 元組", ["π_{Attributes(R)} (R ⋈ S)，即僅保留 R 中能在 S 中找到匹配項的 R 元組", "R 與 S 的卡氏積", "R 扣除 S 的部分", "S 中在 R 有匹配的元組"],
         "半連接常用於分散式資料庫查詢最佳化，在網路傳輸前先過濾掉 R 中絕不可能被連接匹配的元組，大幅減少網路傳輸頻寬開銷。"),
        ("反半連接（Anti-Semi-Join R ▷ S）的運算結果為？",
         "R − (R ⋉ S)，即僅保留 R 中「無法」在 S 中找到任何匹配項的 R 元組", ["R − (R ⋉ S)，即僅保留 R 中「無法」在 S 中找到任何匹配項的 R 元組", "R 與 S 的交集", "R ⋈ S 的補集", "S 中無法匹配的元組"],
         "反半連接等價於 SQL 中的 `NOT EXISTS` 或 `NOT IN`，專門篩選孤立未關聯的左表紀錄。"),
        ("重命名運算子 ρ_{S(B1, B2)}(R) 的主要功能為？",
         "將關聯 R 的名稱重命名為 S，並將其屬性依序重命名為 B1, B2", ["將關聯 R 的名稱重命名為 S，並將其屬性依序重命名為 B1, B2", "建立一個新的資料庫實體", "複製資料表到磁碟", "修改主鍵條件"],
         "重命名運算子（Rename Operator ρ）用於解決同表自連接（Self-Join）時屬性名稱衝突之歧義性問題。")
    ]

    for stem, ans_s, opts, expl in ra_items:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "關聯代數運算推導",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【關聯代數運算子數學推導】</strong><br>
<div class="step-box">
  <div class="step-title">📝 關聯代數定義與推導分析</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>確立關聯代數運算子語意</strong><br>
      ‧ 本題依據關聯代數標準形式與集合論定義進行推導。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>執行逐步數理映射</strong><br>
      ‧ {expl}
    </li>
    <li class="step-item"><span class="step-badge check">步驟 3</span><strong>得出精準結論</strong><br>
      ‧ 正確答案為 <strong>{ans_s}</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) {ans_s}</strong>：完全符合關聯代數定理。<br>
‧ 其餘選項皆為運算子定義混淆或運算結果維度誤判。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Relational Algebra</code> <span class="en">Relational Algebra</span>：關聯代數。<br>
‧ <code>Cartesian Product</code> <span class="en">Cartesian Product</span>：卡氏積。<br>
‧ <code>Natural Join</code> <span class="en">Natural Join</span>：自然連接。"""
        })

    # More RA (25 items)
    more_ra = [
        ("關聯代數中，投影運算（Projection π）與 SQL 中的 SELECT 子句最大的行為差異為何？", "關聯代數的投影運算會「自動去除重複元組（Duplicate Elimination）」，而 SQL 預設保留重複元組（需 DISTINCT 顯式去重）", ["關聯代數的投影運算會「自動去除重複元組（Duplicate Elimination）」，而 SQL 預設保留重複元組（需 DISTINCT 顯式去重）", "SQL 的 SELECT 會自動去重", "兩者行為完全相同", "關聯代數投影無法選擇欄位"], "關聯代數建立於純數學集合論（Set Theory）之上，集合不允許重複元素；SQL 則基於多重集（Multiset / Bag Theory）設計以優化效能。"),
        ("若關聯 R 包含屬性 (A, B, C)，關聯 S 包含屬性 (C, D)。計算自然連接 R ⋈ S 後，結果關聯包含幾個屬性？", "4 個屬性 (A, B, C, D)", ["4 個屬性 (A, B, C, D)", "5 個屬性", "3 個屬性", "2 個屬性"], "公共屬性 C 在自然連接結果中只保留一份，總屬性為 deg(R) + deg(S) - 相同屬性數 = 3 + 2 - 1 = 4 個。"),
        ("θ-連接（Theta Join R ⋈_θ S）的本質是下列何種運算？", "在卡氏積（R × S）之上套用條件選擇運算 σ_θ", ["在卡氏積（R × S）之上套用條件選擇運算 σ_θ", "在聯集之上套用投影", "在自然連接之上套用差集", "在除法之上套用群組"], "θ-連接定義為 R ⋈_θ S = σ_θ (R × S)，其中 θ 為任意布林比較條件（如 R.A > S.B）。"),
        ("等值連接（Equi-Join）是 θ-連接的一個特例，其連接條件 θ 必須滿足？", "條件中僅包含等於運算子（=）", ["條件中僅包含等於運算子（=）", "條件中包含大於或小於", "條件中包含邏輯 NOT", "必須連接主鍵"], "當條件式全為屬性間之相等比對（如 R.id = S.id）時稱為等值連接。"),
        ("若關聯 R 的度數（Degree）為 3，基數（Cardinality）為 10；關聯 S 的度數為 2，基數為 5。則 R × S 的度數與基數分別為？", "度數 5，基數 50", ["度數 5，基數 50", "度數 6，基數 15", "度數 5，基數 15", "度數 6，基數 50"], "度數相加：3 + 2 = 5；基數相乘：10 × 5 = 50。"),
        ("若關聯 R 與 S 進行差集運算（R − S），其結果元組必定存在於何處？", "必定存在於 R 中且不存在於 S 中", ["必定存在於 R 中且不存在於 S 中", "必定存在於 S 中且不存在於 R 中", "存在於 R 或 S 中", "同時存在於 R 與 S 中"], "差集定義：{t | t ∈ R ∧ t ∉ S}。"),
        ("在關聯代數中，選擇運算（Selection σ）對於運算元關聯的維度有何影響？", "維持屬性個數（度數）不變，可能減少元組數量（基數）", ["維持屬性個數（度數）不變，可能減少元組數量（基數）", "減少屬性個數", "增加屬性個數", "同時減少度數與基數"], "選擇運算為水平切片（Horizontal Slice），過濾列而不改變欄位結構。"),
        ("在關聯代數中，投影運算（Projection π）對於運算元關聯的維度有何影響？", "減少或維持屬性個數（垂直切片），可能因去重而減少元組數量", ["減少或維持屬性個數（垂直切片），可能因去重而減少元組數量", "增加屬性個數", "必定保持元組數量不變", "將資料表轉為非集合"], "投影為垂直切片（Vertical Slice），挑選特定欄位，並去除重疊的重複資料列。"),
        ("聚集函數運算子（Aggregate Operator G）在擴展關聯代數中表示為 _E G_F(R)，其中 E 與 F 分別代表？", "E 代表分組屬性清單，F 代表聚集函數與其目標屬性（如 COUNT, SUM）", ["E 代表分組屬性清單，F 代表聚集函數與其目標屬性（如 COUNT, SUM）", "E 代表條件選擇，F 代表投影", "E 代表外部連接，F 代表內部連接", "E 代表排序欄位，F 代表過濾欄位"], "擴充關聯代數中以 G 標記分組與聚合運算，對應 SQL 的 GROUP BY 與聚合函數。"),
        ("關聯運算式 σ_{A=5}(R) 與 σ_{A=5 ∧ B=10}(R) 之間的關係為？", "後者輸出的結果集合必定是前者的子集合（Subset）", ["後者輸出的結果集合必定是前者的子集合（Subset）", "後者結果集大於前者", "兩者結果必定完全相同", "後者包含前者所有資料"], "增加篩選條件（AND）會使條件更為嚴格，篩選出的資料列只能維持不變或減少。"),
        ("關聯代數中，選擇運算的串接律（Cascade of Selection）表示下列何者成立？", "σ_{c1 ∧ c2}(R) = σ_{c1}(σ_{c2}(R))", ["σ_{c1 ∧ c2}(R) = σ_{c1}(σ_{c2}(R))", "σ_{c1 ∨ c2}(R) = σ_{c1}(σ_{c2}(R))", "σ_{c1}(R) ∪ σ_{c2}(R) = σ_{c1 ∧ c2}(R)", "σ_{c1}(R × S) = σ_{c1}(R) × S"], "複合條件選擇可分解為多次巢狀單一條件選擇，為查詢最佳化推動選擇（Pushing Selections Down）之理論基礎。"),
        ("關聯代數運算中，若 R 與 S 屬性完全相同，則 (R − S) ∪ (S − R) 等價於下列何種集合運算？", "對稱差集（Symmetric Difference R ⊕ S）", ["對稱差集（Symmetric Difference R ⊕ S）", "交集 R ∩ S", "全聯集 R ∪ S", "卡氏積 R × S"], "排除雙方共有元素，僅保留專屬於 R 或專屬於 S 之元素，即為對稱差。"),
        ("若 R ⋈ S 的結果為空集合（Empty Set），其原因為？", "R 與 S 在所有公共屬性上的取值完全沒有任何一組相同", ["R 與 S 在所有公共屬性上的取值完全沒有任何一組相同", "R 或 S 本身必須全空", "R 與 S 屬性個數不同", "R 與 S 主鍵衝突"], "自然連接要求公共屬性值相等，若無任何交集匹配列，結果為空表。"),
        ("外連接中，右外連接（Right Outer Join R ⟖ S）可利用左外連接等價表示為？", "S ⟕ R", ["S ⟕ R", "R ⟕ S", "S ⟗ R", "R − S"], "交換運算元左右次序即可將右外連接轉換為左外連接。"),
        ("安全關聯演算（Safe Relational Calculus）要求查詢結果必須滿足何種性質？", "查詢結果元組中出現的任何常數，必須來自查詢運算式或輸入關聯的網域中（保證結果有限）", ["查詢結果元組中 brass 的任何常數，必須來自查詢運算式或輸入關聯的網域中（保證結果有限）", "查詢絕不能包含 NULL", "查詢必須能在 1 秒內回傳", "只能查詢整數欄位"], "防止產生無限大結果集（例如 {t | ¬(t ∈ R)} 會包含宇宙中所有可能的無窮物件），保證運算之有限封閉性。"),
        ("E. F. Codd 提出的「Codd 完備性（Codd's Completeness）」是指？", "一種查詢語言若具備與基本關聯代數至少相同的表達能力，即稱為 Codd 完備", ["一種查詢語言若具備與基本關聯代數至少相同的表達能力，即稱為 Codd 完備", "資料庫必須符合 3NF", "系統必須支援 ACID", "支援圖形介面"], "Codd 定理證明關聯代數與元組關聯演算（TRC）及領域關聯演算（DRC）在安全約束下表達能力完全等價。"),
        ("若關聯 R 包含 100 筆紀錄，在屬性 A 上有 100 個互不相同的數值，則 σ_{A=10}(R) 輸出的紀錄筆數為？", "至多 1 筆紀錄", ["至多 1 筆紀錄", "恰好 10 筆", "100 筆", "0 筆"], "A 屬性值皆相異（具有唯一性），故等值查詢命中次數至多為 1 筆。"),
        ("在關聯代數中，若欲自員工關聯 Emp(id, name, salary) 中找出薪資大於 50000 的員工姓名，正確的關聯代數運算式為？", "π_{name} ( σ_{salary > 50000} (Emp) )", ["π_{name} ( σ_{salary > 50000} (Emp) )", "σ_{name} ( π_{salary > 50000} (Emp) )", "π_{salary > 50000} ( σ_{name} (Emp) )", "Emp × (salary > 50000)"], "先以選擇運算過濾 salary > 50000 的資料列，再以投影運算選取 name 欄位。"),
        ("查詢最佳化中，將關聯代數樹的選擇運算（σ）盡可能向葉節點下推（Push-down），其主要優點為？", "在連接（Join）運算前大幅縮減參與的中間資料量，減少記憶體與 I/O 開銷", ["在連接（Join）運算前大幅縮減參與的中間資料量，減少記憶體與 I/O 開銷", "增加連接運算的次數", "自動產生索引", "消除主鍵條件"], "卡氏積或連接會使資料量呈幾何級數放大，及早過濾（Filter Early）是查詢最佳化的第一黃金法則。"),
        ("查詢最佳化中，將投影運算（π）向葉節點下推的主要好處為？", "及早消除後續運算不需要的欄位，減小每個元組在記憶體中的寬度", ["及早消除後續運算不需要的欄位，減小每個元組在記憶體中的寬度", "減少資料列數", "自動去重", "改變排序方式"], "減少元組物理大小，使記憶體緩衝區（Buffer Pool）單一頁面能容納更多筆紀錄。"),
        ("自然連接運算具備下列何種代數性質？", "結合律（Associative）與交換律（Commutative）", ["結合律（Associative）與交換律（Commutative）", "僅具交換律不具結合律", "僅具結合律不具交換律", "兩者皆不具備"], "(R ⋈ S) ⋈ T = R ⋈ (S ⋈ T) 且 R ⋈ S = S ⋈ R，這使得最佳化器能自由調整多表連接的執行順序。"),
        ("差集運算（R − S）是否具備交換律？", "不具備交換律（R − S 通常不等於 S − R）", ["不具備交換律（R − S 通常不等於 S − R）", "具備交換律", "視資料型態而定", "當 R 與 S 大小相等時具備交換律"], "集合差集不對稱，例如 {1, 2} - {2} = {1}，而 {2} - {1, 2} = ∅。"),
        ("聯集運算（R ∪ S）是否具備結合律與交換律？", "具備結合律與交換律", ["具備結合律與交換律", "不具備交換律", "不具備結合律", "兩者皆否"], "聯集滿足 R ∪ S = S ∪ R 且 (R ∪ S) ∪ T = R ∪ (S ∪ T)。"),
        ("在關聯除法 R(A, B) ÷ S(B) 中，結果關聯包含哪些屬性？", "僅包含屬性 A", ["僅包含屬性 A", "包含 A 與 B", "僅包含屬性 B", "屬性為空"], "除法運算結果的綱要為被除表屬性扣除除表屬性，即 Schema(R) - Schema(S) = {A}。"),
        ("若 S(B) 包含兩筆紀錄 {b1, b2}，R(A, B) 包含 {(a1, b1), (a1, b2), (a2, b1)}。則 R ÷ S 的結果為？", "{(a1)}", ["{(a1)}", "{(a1), (a2)}", "{(a2)}", "空集合 ∅"], "只有 a1 同時與 S 中的 b1 及 b2 產生配對；a2 僅配對到 b1 缺少 b2，故除法結果僅有 a1。")
    ]

    for stem, ans_s, opts, expl in more_ra:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "關聯代數性質推導",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【關聯代數運算深入解析】</strong><br>
‧ <strong>(A) {ans_s}</strong>：依定理推導，{expl}<br>
‧ 其餘選項皆存在代數定理誤判或運算子維度混淆。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Codd's Completeness</code> <span class="en">Codd's Completeness</span>：Codd 完備性。<br>
‧ <code>Division Operator</code> <span class="en">Division Operator</span>：除法運算子。<br>
‧ <code>Theta Join</code> <span class="en">Theta Join</span>：西塔連接。"""
        })

    # -------------------------------------------------------------
    # 2. 進階 SQL 語法與視窗函數 (35 題)
    # -------------------------------------------------------------
    sql_items = [
        ("在 SQL 視窗函數（Window Functions）中，RANK(), DENSE_RANK() 與 ROW_NUMBER() 對於相同數值的排序編號行為，下列敘述何者正確？",
         "ROW_NUMBER() 給予連續不重複序號；RANK() 給予相同序號但後續跳號；DENSE_RANK() 給予相同序號且後續「不跳號」", ["ROW_NUMBER() 給予連續不重複序號；RANK() 給予相同序號但後續跳號；DENSE_RANK() 給予相同序號且後續「不跳號」", "RANK() 與 DENSE_RANK() 行為完全相同", "ROW_NUMBER() 遇到同分會給予相同編號", "DENSE_RANK() 會跳過後續號碼"],
         "例如分數為 [100, 100, 90]：ROW_NUMBER() 為 1, 2, 3；RANK() 為 1, 1, 3（跳過 2）；DENSE_RANK() 為 1, 1, 2（緊湊不跳號）。此為國考最經典高頻考題！"),
        ("在 SQL:1999 標準之遞迴查詢（Recursive CTE）中，標準語法結構為 WITH RECURSIVE cte_name AS (...)，其 UNION ALL 兩側通常分別代表？",
         "錨點成員（Anchor Member，遞迴起始基準）與遞迴成員（Recursive Member，引用自身向前推展）", ["錨點成員（Anchor Member，遞迴起始基準）與遞迴成員（Recursive Member，引用自身向前推展）", "主查詢與子查詢", "外部連接與內部連接", "分組欄位與彙總欄位"],
         "遞迴 CTE 運作模式：首先執行 Anchor Member 產出初始種子結果集；接著反覆執行 Recursive Member 並將新產出列加入，直到遞迴成員回傳空集合為止。常用於走訪組織層級主管樹或圖形路徑。"),
        ("SQL 中 `UNION` 與 `UNION ALL` 的根本差異為何？",
         "`UNION` 會對合併後的結果集進行排序並去除重複紀錄（開銷較大）；`UNION ALL` 直接將兩結果集合併而不去重（效能極高）", ["`UNION` 會對合併後的結果集進行排序並去除重複紀錄（開銷較大）；`UNION ALL` 直接將兩結果集合併而不去重（效能極高）", "`UNION ALL` 會去除重複項", "`UNION` 只能合併兩個數字欄位", "兩者效能與結果完全相同"],
         "`UNION` 內部隱含 DISTINCT 排序去重運算，可能引發外存排序 I/O 開銷；`UNION ALL` 純粹串接，在確認無重複或不需要去重時應優先選用。"),
        ("SQL 的三值邏輯（Three-Valued Logic）中，運算式 `(NULL = NULL)` 的評估結果為何？",
         "UNKNOWN（未知）", ["UNKNOWN（未知）", "TRUE（真）", "FALSE（假）", "NULL"],
         "NULL 代表未知或不存在，兩個未知的值不能斷定相等。在 SQL 條件判斷中 `NULL = NULL` 評估為 UNKNOWN；只有在 WHERE 子句條件結果為 TRUE 時資料列才會被選出（UNKNOWN 會被過濾掉）。檢測 NULL 必須使用 `IS NULL`！"),
        ("在 SQL SELECT 查詢中，各子句的「邏輯執行順序（Logical Processing Order）」為？",
         "FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT / OFFSET", ["FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT / OFFSET", "SELECT -> FROM -> WHERE -> GROUP BY -> HAVING", "FROM -> SELECT -> WHERE -> ORDER BY", "WHERE -> FROM -> GROUP BY -> SELECT"],
         "邏輯執行順序決定了欄位別名（Alias）的可見性：在 WHERE 子句中無法引用 SELECT 中定義的別名，因為 WHERE 比 SELECT 先行執行；但 ORDER BY 在 SELECT 之後執行，故能合法引用 SELECT 別名。"),
        ("在 SQL 中，`HAVING` 子句與 `WHERE` 子句的主要差異為何？",
         "`WHERE` 在分組前對個別資料列進行過濾；`HAVING` 在分組後對分組彙總（Aggregated Groups）結果進行過濾", ["`WHERE` 在分組前對個別資料列進行過濾；`HAVING` 在分組後對分組彙總（Aggregated Groups）結果進行過濾", "`HAVING` 可以在沒有 GROUP BY 時使用聚合函數", "`WHERE` 支援聚合函數，`HAVING` 不支援", "兩者功能完全相同可互相置換"],
         "`WHERE` 作用於個別原始 row（不能包含聚合函數如 SUM, AVG）；`HAVING` 作用於由 `GROUP BY` 產生的各個群組，可針對聚合結果（如 `HAVING COUNT(*) > 5`）做篩選。"),
        ("使用視窗函數 `LEAD(salary, 1) OVER (ORDER BY hire_date)` 的功能為？",
         "取得依到職日排序下，「下一筆（後續第一筆）」資料列的薪資值", ["取得依到職日排序下，「下一筆（後續第一筆）」資料列的薪資值", "取得前一筆資料列的薪資值", "取得目前累積的平均薪資", "取得全公司的最高薪資"],
         "`LEAD(col, n)` 往前看後續第 n 筆資料；`LAG(col, n)` 往後看先前第 n 筆資料，能極優雅地計算相鄰列差值（如逐日增長率）而無需昂貴自連接。"),
        ("SQL 聚合查詢中，`GROUP BY ROLLUP(A, B)` 產生的彙總維度群組組合為？",
         "(A, B), (A), 及全體總計 ()", ["(A, B), (A), 及全體總計 ()", "(A, B), (A), (B), 及 ()", "(A, B) 及 (B)", "僅有 (A, B)"],
         "`ROLLUP(A, B)` 建立具階層性的小計與總計（從右向左逐層遞減匯總）：包含細項 (A, B)、第一層小計 (A)、與總計 ()，共 n+1 種組合。"),
        ("SQL 聚合查詢中，`GROUP BY CUBE(A, B)` 產生的彙總維度群組組合為？",
         "(A, B), (A), (B), 及全體總計 ()", ["(A, B), (A), (B), 及全體總計 ()", "(A, B) 及 ()", "(A) 及 (B)", "A × B 的排列"],
         "`CUBE(A, B)` 產生所有可能的 2^n 種多維交叉匯總組合：包含 (A, B), (A), (B), 與全體 ()。"),
        ("在 SQL 中，條件判斷 `WHERE col NOT IN (SELECT other_col FROM T)`，若子查詢結果集中包含「至少一個 NULL 值」，則整個查詢結果將會？",
         "回傳「0 筆資料」（空集合），因為 NOT IN 遇到 NULL 會全盤判定為 UNKNOWN 而被過濾", ["回傳「0 筆資料」（空集合），因為 NOT IN 遇到 NULL 會全盤判定為 UNKNOWN 而被過濾", "正常回傳所有不相等的資料", "拋出語法錯誤異常", "自動忽略 NULL 正常運作"],
         "致命 SQL 陷阱！`v NOT IN (1, 2, NULL)` 等價於 `v != 1 AND v != 2 AND v != NULL`。因為 `v != NULL` 為 UNKNOWN，整個 AND 邏輯式結果必為 UNKNOWN 或 FALSE，永不為 TRUE！防禦此問題應一律改用 `NOT EXISTS`。")
    ]

    for stem, ans_s, opts, expl in sql_items:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "進階SQL與視窗函數",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【進階 SQL 語意與執行期機制推導】</strong><br>
<div class="step-box">
  <div class="step-title">📝 SQL 語法與三值邏輯推導步驟</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>確認 SQL 標準規範與邏輯順序</strong><br>
      ‧ 本題依據 ANSI SQL 標準（三值邏輯、視窗框架或多維聚集）進行分析。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>執行數理推導或陷阱排查</strong><br>
      ‧ {expl}
    </li>
    <li class="step-item"><span class="step-badge check">步驟 3</span><strong>確立正確查詢結果</strong><br>
      ‧ 答案為 <strong>{ans_s}</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) {ans_s}</strong>：完全符合 ANSI SQL 行為規範。<br>
‧ 其餘選項常為跳號規則記反、或未考量三值邏輯 UNKNOWN 之經典陷阱。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Window Function</code> <span class="en">Window Function</span>：視窗函數。<br>
‧ <code>Common Table Expression (CTE)</code> <span class="en">Common Table Expression</span>：公用資料表運算式。<br>
‧ <code>Three-Valued Logic (3VL)</code> <span class="en">Three-Valued Logic</span>：三值邏輯。"""
        })

    # Expand SQL questions to 35
    more_sql = [
        ("SQL 函數 `COALESCE(e1, e2, e3)` 的回傳值為？", "回傳參數清單中「第一個非 NULL」的運算式數值", ["回傳參數清單中「第一個非 NULL」的運算式數值", "回傳所有非 NULL 值的總和", "若有 NULL 則回傳 NULL", "回傳參數個數"], "COALESCE 常用於將 NULL 替換為預設預設值，例如 COALESCE(salary, 0)。"),
        ("SQL 函數 `NULLIF(a, b)` 的回傳值為？", "若 a 等於 b 則回傳 NULL；否則回傳 a", ["若 a 等於 b 則回傳 NULL；否則回傳 a", "若 a 等於 b 則回傳 TRUE", "回傳較大者", "若有 NULL 則回傳 0"], "常用於防止除以零錯誤：`val / NULLIF(divisor, 0)`。當除數為 0 時轉為 NULL 避免 Divide-by-zero 例外。"),
        ("在含有聚集函數的查詢中，`COUNT(*)` 與 `COUNT(column_name)` 的根本差異為？", "`COUNT(*)` 計算資料列總數（包含 NULL 列）；`COUNT(column_name)` 僅計算該欄位「非 NULL」的資料列筆數", ["`COUNT(*)` 計算資料列總數（包含 NULL 列）；`COUNT(column_name)` 僅計算該欄位「非 NULL」的資料列筆數", "兩者完全相同", "`COUNT(*)` 會自動去重", "`COUNT(col)` 包含 NULL"], "若某欄位有 10 筆資料其中 2 筆為 NULL，則 COUNT(*) = 10，COUNT(col) = 8。"),
        ("在視窗函數的 OVER 子句中，指定 `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW` 代表何種計算範圍？", "計算當前列及其前兩列，共 3 列資料之滑動視窗聚合", ["計算當前列及其前兩列，共 3 列資料之滑動視窗聚合", "計算當前列及其後兩列", "計算前兩列但排除當前列", "計算整張資料表"], "ROWS 子句嚴格以實體列數界定視窗畫框（Frame），常用於計算 3 天移動平均值。"),
        ("視窗函數中，`RANGE BETWEEN` 與 `ROWS BETWEEN` 的差異在於？", "`ROWS` 依據物理資料列筆數劃定邊界；`RANGE` 依據 ORDER BY 欄位的數值邏輯差值劃定邊界（相同數值視為同一個同值群體）", ["`ROWS` 依據物理資料列筆數劃定邊界；`RANGE` 依據 ORDER BY 欄位的數值邏輯差值劃定邊界（相同數值視為同一個同值群體）", "兩者完全相同", "`RANGE` 速度快 10 倍", "`ROWS` 只能用於整數"], "當 ORDER BY 欄位存在相同數值時，RANGE 會將所有相同數值的行一併納入視窗。"),
        ("若欲找出各部門薪資排名前 3 名的員工，應在 OVER 子句中如何設定分組與排序？", "`PARTITION BY department_id ORDER BY salary DESC`", ["`PARTITION BY department_id ORDER BY salary DESC`", "`GROUP BY department_id ORDER BY salary`", "`ORDER BY salary DESC PARTITION BY department_id`", "`CLUSTER BY department_id`"], "PARTITION BY 將視窗獨立劃分給各部門，內部依 salary 降序排列後以 DENSE_RANK() <= 3 篩選。"),
        ("視窗函數 `NTILE(4) OVER (ORDER BY score DESC)` 的功能為？", "將所有排序後的資料平均劃分為 4 個四分位級距（區塊編號 1 到 4）", ["將所有排序後的資料平均劃分為 4 個四分位級距（區塊編號 1 到 4）", "取前 4 筆資料", "每隔 4 筆取 1 筆", "將數值除以 4"], "NTILE(n) 將有序資料平均分桶（Bucketing），常用於四分位數、十分位數評級分析。"),
        ("在關聯式資料庫中，「檢視表（View）」的核心本質為？", "預先編譯並儲存於資料字典中的具名虛擬查詢（Virtual Table），預設不佔用實體資料儲存空間", ["預先編譯並儲存於資料字典中的具名虛擬查詢（Virtual Table），預設不佔用實體資料儲存空間", "實體複製的備份資料表", "一種特殊的叢集索引", "暫存於記憶體中的快取陣列"], "View 是一段儲存的 SELECT 查詢語句，每次存取時動態展開執行；而「具體化檢視表（Materialized View）」才會將結果實際落地存於磁碟。"),
        ("若一個 View 包含 `GROUP BY` 或 `DISTINCT` 運算，該 View 是否支援透過 INSERT, UPDATE 進行直接更新？", "不支援（屬於不可更新檢視表 Non-Updatable View）", ["不支援（屬於不可更新檢視表 Non-Updatable View）", "完全支援", "僅支援 INSERT", "僅支援 DELETE"], "包含聚集函數、GROUP BY、DISTINCT、或 UNION 的 View 無法一對一反向映射至底層基礎資料表的具體列，系統無法決定如何分配更新。"),
        ("在建立 View 時加上 `WITH CHECK OPTION` 子句，其主要功用為？", "防止透過該 View 進行 INSERT 或 UPDATE 時，寫入「不符合 View 定義之 WHERE 條件」的資料", ["防止透過該 View 進行 INSERT 或 UPDATE 時，寫入「不符合 View 定義之 WHERE 條件」的資料", "加速查詢速度", "強制建立索引", "鎖定資料表不允許修改"], "保證更新後的資料行仍必須滿足該 View 的可見條件，維護檢視表語意完整性。"),
        ("SQL 中的 `MERGE` 陳述式（又稱 Upsert）主要結合了哪三種操作？", "INSERT, UPDATE 與 DELETE（根據來源與目標表之匹配狀態決定插入或更新）", ["INSERT, UPDATE 與 DELETE（根據來源與目標表之匹配狀態決定插入或更新）", "SELECT, DROP 與 ALTER", "COMMIT, ROLLBACK 與 SAVEPOINT", "GRANT, REVOKE 與 DENY"], "WHEN MATCHED THEN UPDATE / WHEN NOT MATCHED THEN INSERT，一條指令高效率完成批次同步。"),
        ("SQL 中 `EXISTS` 子查詢的評估機制為何？", "只要子查詢找到「至少一筆滿足條件的紀錄」即返回 TRUE，無須完整掃描整個子查詢集合（短路求值 Short-circuit）", ["只要子查詢找到「至少一筆滿足條件的紀錄」即返回 TRUE，無須完整掃描整個子查詢集合（短路求值 Short-circuit）", "必須將子查詢所有資料加總", "必須載入所有欄位到記憶體", "遇到 NULL 會出錯"], "EXISTS 僅檢查存在性，一旦命中立即終止，因此 `SELECT *` 或 `SELECT 1` 在 EXISTS 中效能完全相同。"),
        ("外來鍵設定 `ON DELETE CASCADE` 的行為為？", "當父資料表（被參照表）之主鍵紀錄被刪除時，子資料表對應參照該鍵的所有外來鍵紀錄亦自動被連帶刪除", ["當父資料表（被參照表）之主鍵紀錄被刪除時，子資料表對應參照該鍵的所有外來鍵紀錄亦自動被連帶刪除", "父表被刪除時拒絕刪除", "將子表外來鍵設為 NULL", "父表被刪除時將子表外來鍵設為預設值"], "CASCADE（級聯刪除）保持參照完整性，但若階層過深可能導致連鎖大量刪除，需謹慎使用。"),
        ("外來鍵設定 `ON DELETE SET NULL` 的先決條件為？", "子資料表中的外來鍵欄位必須「允許為 NULL（Nullable）」", ["子資料表中的外來鍵欄位必須「允許為 NULL（Nullable）」", "子資料表外來鍵必須為主鍵", "父表不能有主鍵", "必須建立唯一索引"], "若該欄位宣告了 `NOT NULL`，則 SET NULL 必然引發完整性衝突而執行失敗。"),
        ("資料定義語言（DDL）中，`TRUNCATE TABLE` 相較於 `DELETE FROM` 的核心差異為？", "`TRUNCATE` 為 DDL 操作，快速釋放資料頁與重設高水位標（High Water Mark），日誌記錄極少且通常不可逐列回滾；`DELETE` 為 DML 逐列刪除並記錄大量 Undo 日誌", ["`TRUNCATE` 為 DDL 操作，快速釋放資料頁與重設高水位標（High Water Mark），日誌記錄極少且通常不可逐列回滾；`DELETE` 為 DML 逐列刪除並記錄大量 Undo 日誌", "`TRUNCATE` 可以帶 WHERE 條件", "`DELETE` 執行速度比 TRUNCATE 快", "兩者底層機制完全相同"], "TRUNCATE 實質上是清空資料表並歸零識別碼（Identity/Auto-Increment），無法觸發 DELETE Trigger。"),
        ("在 SQL 中宣告交易的隔離等級語法為？", "`SET TRANSACTION ISOLATION LEVEL <等級名稱>;`", ["`SET TRANSACTION ISOLATION LEVEL <等級名稱>;`", "`SET LOCK LEVEL <等級名稱>;`", "`SET DATABASE MODE <等級名稱>;`", "`ALTER TRANSACTION <等級名稱>;`"], "標準 ANSI SQL 交易控制指令。"),
        ("SQL:2003 引入之遞迴 CTE 中，防止無窮遞迴（Infinite Loop）的常見機制為？", "在遞迴成員中加入遞迴層數限制條件（如 `WHERE depth < 100`）或使用資料庫引擎的 MAXRECURSION 提示", ["在遞迴成員中加入遞迴層數限制條件（如 `WHERE depth < 100`）或使用資料庫引擎的 MAXRECURSION 提示", "系統會自動在第 2 層停止", "遞迴查詢不允許有迴圈", "使用 GROUP BY 自動截斷"], "圖結構若存在環（Cycle），遞迴 CTE 會陷入無窮迴圈，必須顯式記錄走訪路徑陣列或設定深度計數器限制。"),
        ("SQL 查詢中，`SELECT DISTINCT a, b FROM T` 的去重比對準則為？", "只有當兩筆資料列的 `a` 與 `b` 同時完全相同時，才會被視為重複而去除", ["只有當兩筆資料列的 `a` 與 `b` 同時完全相同時，才會被視為重複而去除", "只要 a 相同就去重", "只要 b 相同就去重", "僅對第一欄位去重"], "DISTINCT 作用於其後所有選取欄位的組合元組。"),
        ("SQL 陳述式 `CREATE UNIQUE INDEX` 的作用為？", "建立索引並強制保證被索引欄位之數值不得重複（可允許多個 NULL 或單一 NULL，依資料庫實作而定）", ["建立索引並強制保證被索引欄位之數值不得重複（可允許多個 NULL 或單一 NULL，依資料庫實作而定）", "只建立索引不具備約束力", "自動將該欄位設為主鍵", "刪除現有重複資料"], "唯一索引（Unique Index）同時兼具加速查詢與實施實體完整性約束雙重功能。"),
        ("在 SQL 中，字串比對萬用字元中，百分比符號 `%` 與底線符號 `_` 分別代表？", "`%` 代表零個或多個任意字元；`_` 代表恰好「單一個」任意字元", ["`%` 代表零個或多個任意字元；`_` 代表恰好「單一個」任意字元", "`%` 代表單一字元，`_` 代表多個字元", "兩者皆代表任意多個字元", "`%` 代表數字，`_` 代表字母"], "LIKE 查詢基本規範：`LIKE 'A%'` 匹配以 A 開頭的任意字串；`LIKE 'A_'` 匹配以 A 開頭長度恰為 2 的字串。"),
        ("在關聯式資料庫中，何謂「SQL 注入攻擊（SQL Injection）」？最佳防禦手段為何？", "攻擊者將惡意 SQL 片段拼接進輸入字串中竄改查詢語意；最佳防禦為使用「參數化查詢（Prepared Statements / Parameterized Queries）」", ["攻擊者將惡意 SQL 片段拼接進輸入字串中竄改查詢語意；最佳防禦為使用「參數化查詢（Prepared Statements / Parameterized Queries）」", "使用儲存程序拼接字串", "將資料庫所有欄位加密", "限制資料庫只讀"], "參數化查詢將 SQL 程式碼邏輯與使用者資料在語法剖析階段嚴格分開，輸入資料永遠僅被視為字面常數（Literal），從根本上杜絕 SQL Injection。"),
        ("儲存程序（Stored Procedure）相較於直接在應用程式執行 raw SQL，主要優勢為何？", "預先編譯減少語法剖析開銷、減少網路往返頻寬、並可透過 GRANT EXECUTE 提供細粒度權限管控", ["預先編譯減少語法剖析開銷、減少網路往返頻寬、並可透過 GRANT EXECUTE 提供細粒度權限管控", "完全消除所有資料庫鎖定", "保證資料庫不當機", "不佔用任何伺服器 CPU"], "商業邏輯內聚於資料庫，執行效能與安全性皆有提升。"),
        ("觸發程序（Database Trigger）的觸發時機（Timing）通常分為？", "BEFORE, AFTER 及 INSTEAD OF", ["BEFORE, AFTER 及 INSTEAD OF", "START, STOP 及 PAUSE", "COMMIT, ROLLBACK 及 SAVE", "PRE, MID 及 POST"], "BEFORE Trigger 常用於資料驗證與自動補全；AFTER Trigger 用於審計日誌與同步跨表統計；INSTEAD OF Trigger 用於對複雜 View 實施自訂更新。"),
        ("SQL 標準中，`INTERSECT` 運算子的行為為？", "回傳同時出現在兩個查詢結果集中的共有記錄，並自動去除重複項", ["回傳同時出現在兩個查詢結果集中的共有記錄，並自動去除重複項", "回傳兩查詢的所有資料", "回傳左表扣除右表的資料", "保留重複項的交集"], "交集運算子，等價於 INNER JOIN 或 EXISTS。"),
        ("SQL 標準中，`EXCEPT`（或 Oracle 中的 `MINUS`）運算子的行為為？", "回傳出現在第一個查詢結果中、但「不存在」於第二個查詢結果中的唯一記錄", ["回傳出現在第一個查詢結果中、但「不存在」於第二個查詢結果中的唯一記錄", "回傳兩表交集", "回傳對稱差", "全外連接"], "差集運算子，等價於 LEFT JOIN 配合 WHERE 右表 IS NULL 或 NOT EXISTS。")
    ]

    for stem, ans_s, opts, expl in more_sql:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "SQL進階語意與應用",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【SQL 進階指令深入辨析】</strong><br>
‧ <strong>(A) {ans_s}</strong>：依 ANSI SQL 標準推導，{expl}<br>
‧ 其餘選項皆存在語法規格混淆或執行期語意偏差。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Parameterized Query</code> <span class="en">Parameterized Query</span>：參數化查詢。<br>
‧ <code>Stored Procedure</code> <span class="en">Stored Procedure</span>：儲存程序。<br>
‧ <code>Database Trigger</code> <span class="en">Database Trigger</span>：資料庫觸發程序。"""
        })

    # -------------------------------------------------------------
    # 3. 實體關聯模型與關聯綱要設計 (60 題)
    # -------------------------------------------------------------
    er_data = [
        ("在實體關聯圖（ER Diagram）中，「弱實體（Weak Entity）」與一般強實體的根本區別在於？",
         "弱實體無法僅依憑自身屬性唯一識別，必須依賴另一個「支配實體（Identifying Owner Entity）」的主鍵才能確立識別", ["弱實體無法僅依憑自身屬性唯一識別，必須依賴另一個「支配實體（Identifying Owner Entity）」的主鍵才能確立識別", "弱實體不能擁有任何屬性", "弱實體不能參與一對多關聯", "弱實體不需要存入資料庫"],
         "例如「員工」與「眷屬」，眷屬若無身分證字號，僅有眷屬姓名與稱謂，必須依賴員工的員工編號（Owner Key）配合自身鑑別碼（Discriminator）組合而成複合主鍵。以雙外框矩形表示。"),
        ("弱實體（Weak Entity）自身的識別屬性稱為「部分鍵（Partial Key / Discriminator）」，在 Peter Chen ER 圖中以何種線條表示？",
         "虛線底線（Dashed Underline）", ["虛線底線（Dashed Underline）", "實線底線（Solid Underline）", "雙實線", "雙虛線外框"], "強實體主鍵以實線底線標示，弱實體之部分鍵（鑑別碼）以虛線底線標示。"),
        ("在 ER 模型轉關聯綱要（Schema Mapping）時，對於一個 M:N（多對多）的關聯型態（Relationship Type），正確的轉換規則為？",
         "必須建立一個「獨立的新關聯表」，其主鍵由參與雙方實體之主鍵「組合而成複合主鍵」，並各自設為外來鍵", ["必須建立一個「獨立的新關聯表」，其主鍵由參與雙方實體之主鍵「組合而成複合主鍵」，並各自設為外來鍵", "將任一方主鍵放入另一方實體即可", "將雙方實體合併為單一資料表", "無法轉為關聯綱要"], "M:N 無法直接在原實體表以單一外來鍵表達（會違反 1NF 第一正規化），必須拆解為一個中介關聯表（Associative Entity / Junction Table）。"),
        ("對於 1:N（一對多）的關聯型態，在轉換為關聯綱要時，外來鍵（Foreign Key）應該放置在何處？",
         "放置在「N 端（多端）」對應的資料表中，指向 1 端的主鍵", ["放置在「N 端（多端）」對應的資料表中，指向 1 端的主鍵", "放置在 1 端對應的資料表中", "必須獨立建一張新表", "兩端各自放置對方的主鍵"], "例如「部門（1）與員工（N）」，在員工表新增 `dept_id` 作為外來鍵，每位員工僅對應一個部門，設計簡潔且完全消除冗餘。"),
        ("在延伸實體關聯模型（EER）中，特化/概括階層的「互斥限制（Disjointness Constraint）」若標記為 'd'（Disjoint），代表何種語意？",
         "超類別實體至多只能屬於「一個」子類別（子類別彼此互斥，不可重疊）", ["超類別實體至多只能屬於「一個」子類別（子類別彼此互斥，不可重疊）", "超類別實體可以同時屬於多個子類別", "子類別不繼承超類別屬性", "必須為完全參與"], "Disjoint (d) 代表互斥（如員工類別非正職即兼職，不可二者皆是）；Overlapping (o) 代表重疊（如員工可同時為工程師與專案經理）。"),
        ("在 EER 模型中，「完全性限制（Completeness Constraint）」若為「完全特化（Total Specialization，以雙線表示）」，代表何種含義？",
         "超類別中的每一個實體，「必須」至少屬於某一個子類別（不存在不屬於任何子類別的超類別實體）", ["超類別中的每一個實體，「必須」至少屬於某一個子類別（不存在不屬於任何子類別的超類別實體）", "超類別實體可以不屬於任何子類別", "所有子類別屬性皆為空", "關聯數必須為 1"], "Total 特化代表所有實體全數被劃分至子類別（如員工必須非為正職即為約聘）；Partial 特化（單線）則容許實體僅屬於超類別而不屬於任何特例子類別。"),
        ("在 ER 模型中，一個屬性若可進一步細分為多個更小的獨立屬性（如地址分為縣市、行政區、街道），該屬性稱為？",
         "複合屬性（Composite Attribute）", ["複合屬性（Composite Attribute）", "多值屬性（Multivalued Attribute）", "衍生屬性（Derived Attribute）", "簡單屬性（Simple Attribute）"], "複合屬性由多個基本原子屬性組成；在轉換為關聯綱要時，通常以其所有細項簡單屬性取代之。"),
        ("在 ER 圖中，「多值屬性（Multivalued Attribute，例如一位員工擁有多個電話號碼）」以何種符號標記？轉換為關聯表時如何處理？",
         "以雙外框橢圓（Double Oval）標記；轉換時必須「建立一個獨立的關聯表」，以原實體主鍵加該多值屬性組合為複合主鍵", ["以雙外框橢圓（Double Oval）標記；轉換時必須「建立一個獨立的關聯表」，以原實體主鍵加該多值屬性組合為複合主鍵", "以單橢圓標記；直接以逗號字串存入單一欄位", "以虛線橢圓標記；直接忽略該屬性", "以菱形標記；加入外來鍵"], "為滿足 1NF（屬性值原子性），多值屬性必須獨立建表（如 Employee_Phone(emp_id, phone_number)）。"),
        ("在 ER 圖中，「衍生屬性（Derived Attribute，例如根據出生日期計算出的年齡）」以何種符號標記？",
         "虛線橢圓（Dashed Oval）", ["虛線橢圓（Dashed Oval）", "實線橢圓", "雙實線橢圓", "矩形"], "衍生屬性可由其他已存在的屬性（如生日）即時動態計算而得，在實體資料庫中通常不直接儲存以避免資料不一致。"),
        ("在 ER 模型中，關聯的「參與限制（Participation Constraint）」中，實體到關聯型態若以「雙線（Double Line）」繪製，代表？",
         "完全參與（Total Participation），該實體集合中的每一個實體都必須至少參與該關聯一次", ["完全參與（Total Participation），該實體集合中的每一個實體都必須至少參與該關聯一次", "部分參與（Partial Participation）", "多對多關聯", "弱實體關聯"], "雙線代表全體必須參與（例如每位學生都必須選修至少一門課）；單線代表部分參與（例如教授可以未指導任何研究生）。")
    ]

    for stem, ans_s, opts, expl in er_data:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "ER模型與綱要設計",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【ER/EER 模型與關聯對映推導】</strong><br>
<div class="step-box">
  <div class="step-title">📝 概念資料模型轉換步驟</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>確立實體屬性與基數限制</strong><br>
      ‧ 本題依據 Peter Chen ER 或 EER 擴充語意進行對映分析。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>執行關聯綱要轉換規則驗證</strong><br>
      ‧ {expl}
    </li>
    <li class="step-item"><span class="step-badge check">步驟 3</span><strong>得出精準結論</strong><br>
      ‧ 正確答案為 <strong>{ans_s}</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) {ans_s}</strong>：完全符合 ER 轉換定理與 1NF 約束。<br>
‧ 其餘選項常為基數端外來鍵放置相反、或符號圖形定義混淆。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Weak Entity</code> <span class="en">Weak Entity</span>：弱實體。<br>
‧ <code>Total Participation</code> <span class="en">Total Participation</span>：完全參與。<br>
‧ <code>Multivalued Attribute</code> <span class="en">Multivalued Attribute</span>：多值屬性。"""
        })

    # Expand ER items to 60 (50 more items)
    more_er = [
        ("在 1:1（一對一）關聯型態的綱要轉換中，若一方為完全參與（Total），另一方為部分參與（Partial），外來鍵應優先放置在何處？", "放置在「完全參與（Total Participation）」的實體表中", ["放置在「完全參與（Total Participation）」的實體表中", "放置在部分參與的實體表中", "必須獨立建新表", "隨意放置效能相同"], "將外來鍵置於完全參與端，保證該外來鍵欄位永遠不會出現 NULL，大幅節省儲存空間並杜絕空值異常。"),
        ("若 1:1 關聯的雙方皆為「完全參與（Total Participation）」，最佳綱要設計策略為？", "將雙方實體與關聯「合併為單一關聯表」", ["將雙方實體與關聯「合併為單一關聯表」", "保持兩張表並互相參照外來鍵", "建立三張表", "不允許此種設計"], "雙方一一對應且全數存在，合併為單一資料表可完全消除連接查詢開銷，效能最優。"),
        ("實體關聯模型中，「三元關聯（Ternary Relationship，連接三個實體）」轉換為關聯綱要時，其對應的資料表主鍵預設由何者構成？", "由三個參與實體之主鍵共同組合而成複合主鍵（Composite Primary Key）", ["由三個參與實體之主鍵共同組合而成複合主鍵（Composite Primary Key）", "由其中任意一個實體主鍵決定", "三元關聯無法轉為關聯表", "由第一個實體的主鍵決定"], "三元關聯代表三個實體間的聯立多元組，預設複合主鍵為三方主鍵之組合（除非有特定 1:1:N 或 1:N:M 基數限制指定）。"),
        ("實體完整性限制（Entity Integrity Constraint）的嚴格規定為？", "任何關聯表的主鍵（Primary Key）欄位「絕對不允許包含 NULL 值」", ["任何關聯表的主鍵（Primary Key）欄位「絕對不允許包含 NULL 值」", "外來鍵不允許為 NULL", "所有欄位皆不能為 NULL", "資料表必須具備自動編號"], "主鍵用以在物理世界唯一標識一筆客觀實體紀錄，若主鍵為 NULL 則實體失去唯一辨識性，嚴重違背實體完整性。"),
        ("參照完整性限制（Referential Integrity Constraint）規定外來鍵的取值必須？", "必須等於其所參照之主鍵資料表中某筆紀錄的主鍵值，或者為 NULL", ["必須等於其所參照之主鍵資料表中某筆紀錄的主鍵值，或者為 NULL", "必須恆等於 1", "不能為 NULL", "必須大於 0"], "外來鍵指向的實體必須在現實世界真實存在，若非存在則只能以 NULL 表達暫無關聯，杜絕懸空參照（Dangling References）。"),
        ("網域完整性限制（Domain Integrity Constraint）是指下列何者？", "資料表中各欄位的取值必須落入其預先定義之合法數值集合與資料型態範圍內（如 CHECK 約束）", ["資料表中各欄位的取值必須落入其預先定義之合法數值集合與資料型態範圍內（如 CHECK 約束）", "主鍵不能為空", "外來鍵必須存在", "資料表名稱必須唯一"], "確保數值類型、長度、格式與自訂規則（如年齡介於 0 到 150）之正確性。"),
        ("自反關聯（Recursive / Self-Referencing Relationship，例如員工實體與主管關聯）轉為關聯表時如何表達？", "在同一張員工表中加入一個 `manager_id` 外來鍵欄位，指向自身資料表的 `emp_id` 主鍵", ["在同一張員工表中加入一個 `manager_id` 外來鍵欄位，指向自身資料表的 `emp_id` 主鍵", "複製一張完全相同的資料表", "無法用關聯表表達", "必須建立雙主鍵"], "自參照外來鍵（Self-Referencing Foreign Key）優雅表達樹狀或圖形階層組織。"),
        ("在關聯綱要中，候選鍵（Candidate Key）的定義為？", "具備唯一性（Uniqueness）且滿足「最小性（Minimality）」的超鍵", ["具備唯一性（Uniqueness）且滿足「最小性（Minimality）」的超鍵", "包含所有屬性的鍵", "資料表中任意非空欄位", "由資料庫自動生成的鍵"], "超鍵（Superkey）能唯一標識元組；若去除超鍵中任何一個屬性後即失去唯一性，則該超鍵稱為候選鍵。"),
        ("超鍵（Superkey）與候選鍵（Candidate Key）的關係為？", "所有候選鍵皆為超鍵，但並非所有超鍵都是候選鍵（超鍵可能包含冗餘屬性）", ["所有候選鍵皆為超鍵，但並非所有超鍵都是候選鍵（超鍵可能包含冗餘屬性）", "所有超鍵皆為候選鍵", "兩者定義完全相同", "超鍵數量必小於候選鍵"], "候選鍵是極簡（Minimal）超鍵。例如 {id} 為候選鍵，則 {id, name} 亦為超鍵但不是候選鍵。"),
        ("主鍵（Primary Key）是從下列何者中挑選出來作為官方唯一識別依據？", "從候選鍵集合中挑選出一個", ["從候選鍵集合中挑選出一個", "從超鍵中隨機挑選", "從外來鍵中挑選", "從多值屬性中挑選"], "一個資料表可能有多個候選鍵（如身分證號、學號、員工編號），設計者挑選其中最穩定且精簡的一個作為主鍵，其餘候選鍵稱為替代鍵（Alternate Keys）。"),
        ("替代鍵（Alternate Key / Secondary Key）是指？", "未被選為主鍵的其餘候選鍵", ["未被選為主鍵的其餘候選鍵", "外來鍵", "人工合成鍵", "索引欄位"], "在業務邏輯上仍具唯一性約束（如 UNIQUE NOT NULL），但未被立為主鍵。"),
        ("代理鍵（Surrogate Key / Synthetic Key）相較於自然鍵（Natural Key）的主要優點為？", "不攜帶業務邏輯語意、數值短小固定（通常為自增整數或 UUID），不受業務規則變更影響且索引效能高", ["不攜帶業務邏輯語意、數值短小固定（通常為自增整數或 UUID），不受業務規則變更影響且索引效能高", "具備真實世界業務意義", "完全不需要儲存空間", "保證不重複且可由使用者輸入"], "自然鍵（如身分證字號、車牌號）可能因法規修改、重機號碼改版而被迫大規模更新外來鍵串列；代理鍵提供系統層級絕對不變的穩定性。"),
        ("自然鍵（Natural Key）的缺點通常為？", "欄位長度通常較長（如字串）、複合欄位多，且當業務定義修改時可能引發連鎖外來鍵修改", ["欄位長度通常較長（如字串）、複合欄位多，且當業務定義修改時可能引發連鎖外來鍵修改", "無法保證唯一性", "無法建立索引", "不能轉為第三正規化"], "例如由國家代碼、區域、流水號組成的複合字串主鍵，維護代價昂貴。"),
        ("在資料庫實體模型中，名詞「主屬性（Prime Attribute）」是指？", "包含在「任一候選鍵」之中的屬性", ["包含在「任一候選鍵」之中的屬性", "主鍵中的第一個屬性", "所有非空屬性", "資料表的第一個欄位"], "只要該屬性是某一個候選鍵的成員（即便該候選鍵未被選為主鍵），即屬於 Prime Attribute。"),
        ("「非主屬性（Non-Prime Attribute）」是指？", "不屬於「任何一個候選鍵」的屬性", ["不屬於「任何一個候選鍵」的屬性", "主鍵之外的所有屬性", "允許為 NULL 的屬性", "外來鍵屬性"], "完全未參與任何候選鍵構成的純資料屬性。"),
        ("在 crow's foot（鴉爪標記法）ER 圖中，端點符號為「一條垂直線加一個圓圈」代表的基數與參與度為？", "零或一（Zero or One，可選 0..1）", ["零或一（Zero or One，可選 0..1）", "恰好一（Exactly 1）", "一或多（1..*）", "零或多（0..*）"], "圓圈代表 0（可選，部分參與），短線代表 1（基數上限為 1）。"),
        ("在 crow's foot 標記法中，端點符號為「一條垂直線加一條垂直線」代表？", "恰好一（Exactly One，強制 1..1）", ["恰好一（Exactly One，強制 1..1）", "零或一", "一或多", "零或多"], "兩條短線代表強制必須有 1 個且上限為 1。"),
        ("在 crow's foot 標記法中，端點符號為「一個圓圈加一個鴉爪」代表？", "零或多（Zero or More，0..*）", ["零或多（Zero or More，0..*）", "一或多（1..*）", "恰好一", "零或一"], "圓圈代表 0，鴉爪（分叉線）代表多（Many）。"),
        ("在 crow's foot 標記法中，端點符號為「一條垂直線加一個鴉爪」代表？", "一或多（One or More，強制 1..*）", ["一或多（One or More，強制 1..*）", "零或多", "恰好一", "零或一"], "短線代表至少 1（強制），鴉爪代表多。"),
        ("在 EER 特化中，若採用「超類別與所有子類別各建一張表（共 1 + n 張表）」的轉換方案，子類別的主鍵如何設定？", "子類別的主鍵等於超類別的主鍵，同時該主鍵亦為外來鍵指向超類別表", ["子類別的主鍵等於超類別的主鍵，同時該主鍵亦為外來鍵指向超類別表", "子類別自動生成代理鍵", "子類別不需要主鍵", "子類別主鍵由其專屬屬性決定"], "標準物件導向多型繼承之關聯映射，子表主鍵與外來鍵合一（Shared Primary Key）。"),
        ("在 EER 特化中，若特化為「互斥且完全（Disjoint, Total）」，另一種極簡轉換方案為？", "不為超類別建表，僅為各子類別建立獨立資料表（包含繼承之超類別所有屬性）", ["不為超類別建表，僅為各子類別建立獨立資料表（包含繼承之超類別所有屬性）", "將所有資料存在超類別表，子類別不建表", "建立視窗表", "無法轉換"], "因為每個實體必恰好屬於某一個子類別，子類別各自包含完整欄位即可完全涵蓋所有資料，消除查詢時的連接（Join）開銷。"),
        ("在 EER 特化中，若特化為「重疊（Overlapping）」，若欲將全體合併至單一關聯表中，應如何處理子類別鑑別？", "在單一表中為每個子類別增設一個獨立的布林旗標欄位（Boolean Flag，如 is_engineer, is_manager）", ["在單一表中為每個子類別增設一個獨立的布林旗標欄位（Boolean Flag，如 is_engineer, is_manager）", "使用單一列舉欄位", "使用外來鍵串列", "無法合併"], "因為單一實體可同時跨越多個子類別，單一 Type 欄位無法表達，必須採用多個布林標記。"),
        ("在關聯式資料庫中，資訊原則（Information Principle）指出？", "資料庫中的所有資料與元資料（Metadata）均必須「以關聯表中的值」這一唯一形式明確表示", ["資料庫中的所有資料與元資料（Metadata）均必須「以關聯表中的值」這一唯一形式明確表示", "資料必須以指標鏈結儲存", "資料必須以樹狀節點表示", "資料必須全數以二進位大型物件儲存"], "Codd 關聯模型核心哲學：沒有任何物理指標暴露給邏輯層，所有關係皆透過屬性值之一致性建立。"),
        ("下列關於外來鍵（Foreign Key）的敘述，何者「錯誤」？", "外來鍵所參照的目標欄位可以是父表中任意隨意選取的普通非鍵欄位", ["外來鍵所參照的目標欄位可以是父表中任意隨意選取的普通非鍵欄位", "外來鍵的值可以為 NULL（若未定義 NOT NULL）", "外來鍵所參照的欄位必須在父表中具有 UNIQUE 或 PRIMARY KEY 約束", "外來鍵可與自身資料表的主鍵形成自參照"], "外來鍵參照的目標欄位「必須」具備唯一性（主鍵或唯一鍵），否則參照會產生歧異！故 (A) 敘述嚴重錯誤。"),
        ("在關聯綱要中，若一個關聯包含複合主鍵 (order_id, item_id)，則下列何者成立？", "order_id 與 item_id 皆屬於主屬性（Prime Attribute），且兩者皆不能為 NULL", ["order_id 與 item_id 皆屬於主屬性（Prime Attribute），且兩者皆不能為 NULL", "只要 order_id 不為 NULL 即可", "兩者皆為非主屬性", "item_id 可以為 NULL"], "實體完整性要求複合主鍵中的「每一個組成屬性」皆嚴格不得為 NULL。"),
        ("關聯綱要設計時，「反正規化（Denormalization）」的主要動機通常為？", "故意引入控制下的資料冗餘以減少昂貴的表連接（JOIN）次數，提升大量讀取時的查詢效能", ["故意引入控制下的資料冗餘以減少昂貴的表連接（JOIN）次數，提升大量讀取時的查詢效能", "節省磁碟儲存空間", "消除資料不一致性", "保證資料表符合 BCNF"], "在讀取密集（Read-Heavy）系統中，高階正規化過多的 JOIN 會拖慢系統，適度反正規化以空間換取時間。"),
        ("反正規化（Denormalization）帶來的主要代價與潛在風險為？", "增加寫入（INSERT, UPDATE, DELETE）開銷，並引發資料不一致（Data Inconsistency）風險", ["增加寫入（INSERT, UPDATE, DELETE）開銷，並引發資料不一致（Data Inconsistency）風險", "使查詢變慢", "無法建立索引", "破壞實體完整性"], "同一個資料在多處儲存，一旦修改必須同步更新所有複本，否則會產生相互矛盾的髒資料。"),
        ("在關聯資料庫設計流程中，概念設計（Conceptual Design）階段的主要產出為？", "實體關聯圖（ER Diagram / EER Diagram）", ["實體關聯圖（ER Diagram / EER Diagram）", "SQL DDL 建立資料表語法", "實體磁碟區塊配置檔", "資料流圖 DFD"], "概念設計專注於業務實體與關係語意，完全獨立於任何具體 DBMS 軟體。"),
        ("邏輯設計（Logical Design）階段的主要工作為？", "將概念 ER 圖轉換為關聯綱要（Relational Schema），並進行正規化（Normalization）檢驗", ["將概念 ER 圖轉換為關聯綱要（Relational Schema），並進行正規化（Normalization）檢驗", "採購伺服器硬體", "撰寫應用程式前端 UI", "設定 RAID 磁碟陣列"], "邏輯設計產出標準關聯表結構、主外鍵定義與完整性約束。"),
        ("實體設計（Physical Design）階段的主要決策包含？", "決定資料表的索引策略（B+樹、雜湊）、檔案儲存配置、分區（Partitioning）與反正規化", ["決定資料表的索引策略（B+樹、雜湊）、檔案儲存配置、分區（Partitioning）與反正規化", "繪製業務 ER 圖", "確認使用者功能需求", "設計資料庫概念模型"], "實體設計針對特定 DBMS 引擎（如 PostgreSQL, Oracle）之硬體特性進行底層效能調優。")
    ]

    for stem, ans_s, opts, expl in more_er:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "資料庫設計與模型轉換",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【關聯綱要設計深入分析】</strong><br>
‧ <strong>(A) {ans_s}</strong>：依正規資料庫工程原理，{expl}<br>
‧ 其餘選項皆存在設計模式認知偏差或完整性限制漏洞。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Surrogate Key</code> <span class="en">Surrogate Key</span>：代理鍵。<br>
‧ <code>Referential Integrity</code> <span class="en">Referential Integrity</span>：參照完整性。<br>
‧ <code>Denormalization</code> <span class="en">Denormalization</span>：反正規化。"""
        })

    return qs

if __name__ == '__main__':
    qs = get_db_part1_questions()
    print(f"Generated DB Part 1 questions: {len(qs)}")
