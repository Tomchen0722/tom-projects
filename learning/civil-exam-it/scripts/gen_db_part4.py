# -*- coding: utf-8 -*-
"""
Database Systems Question Bank Generator - Part 4 (100 unique questions)
Topics: Comprehensive SQL Analytical Queries (35), Complex Relational Algebra Expressions (35), Serializability & Concurrency Graphs (30).
"""

def get_db_part4_questions():
    qs = []

    # -------------------------------------------------------------
    # 1. 複雜 SQL 分析與推導計算 (35 題)
    # -------------------------------------------------------------
    sql_calc = [
        ("執行 SQL 語句 `SELECT COUNT(*), COUNT(commission) FROM employees;`，已知員工表共有 100 人，其中 20 人有業績抽成（commission 欄位非空），其餘 80 人無抽成（commission 為 NULL）。查詢結果依序為？",
         "100 與 20", ["100 與 20", "100 與 100", "20 與 20", "100 與 80"],
         "`COUNT(*)` 計算資料表中的所有資料行數（包含 NULL，結果為 100）；`COUNT(column_name)` 僅計算該欄位「非 NULL」的資料行數（結果為 20）。"),
        ("執行 SQL 語句 `SELECT AVG(score) FROM students;`，已知共有 5 位學生，成績分別為 100, 80, 60, NULL, NULL。查詢回傳之平均分數為？",
         "80", ["80", "48", "60", "NULL"],
         "SQL 聚集函數（SUM, AVG, MIN, MAX）在計算時會「自動忽略 NULL 值」！故平均計算為 (100 + 80 + 60) / 3 = 240 / 3 = 80，而不是除以 5（48）。"),
        ("若欲計算上述學生之平均成績，並將 NULL 視為 0 分計入，正確的 SQL 語法為？",
         "`SELECT AVG(COALESCE(score, 0)) FROM students;`", ["`SELECT AVG(COALESCE(score, 0)) FROM students;`", "`SELECT AVG(score) FROM students;`", "`SELECT SUM(score) / COUNT(*) FROM students;`", "`SELECT AVG(score + 0) FROM students;`"],
         "以 COALESCE(score, 0) 先將 NULL 轉換為 0 分，再代入 AVG 即可除以 5 得 (100+80+60+0+0)/5 = 48 分。"),
        ("執行 SQL `SELECT 1 WHERE NULL = NULL;` 與 `SELECT 1 WHERE NULL IS NULL;`，其查詢回傳結果分別為？",
         "前者回傳 0 筆資料（空集合），後者回傳 1 筆數值 1", ["前者回傳 0 筆資料（空集合），後者回傳 1 筆數值 1", "兩者皆回傳 1", "兩者皆回傳空集合", "前者報錯"],
         "三值邏輯中 `NULL = NULL` 評估為 UNKNOWN，WHERE UNKNOWN 不成立；而 `NULL IS NULL` 嚴格評估為 TRUE，故能正確返回資料。"),
        ("執行 SQL `SELECT CASE WHEN 1=2 THEN 'A' WHEN NULL THEN 'B' ELSE 'C' END;`，其回傳值為？",
         "'C'", ["'C'", "'A'", "'B'", "NULL"],
         "CASE 表達式依序求值：第一個 WHEN 條件 1=2 為 FALSE；第二個 WHEN 條件為 NULL（UNKNOWN，非 TRUE 不成立）；最後命中 ELSE 子句，回傳 'C'。"),
        ("SQL 視窗函數 `FIRST_VALUE(salary) OVER (PARTITION BY dept_id ORDER BY salary DESC)` 的計算結果為？",
         "該部門中的最高薪資值（第一名薪資）", ["該部門中的最高薪資值（第一名薪資）", "全公司的最低薪資", "該部門的平均薪資", "員工本人的薪資"],
         "`FIRST_VALUE(col)` 取視窗排序後的第一筆紀錄值，配合 DESC 即為該分組最大值。"),
        ("SQL 視窗函數 `LAST_VALUE(salary) OVER (PARTITION BY dept_id ORDER BY salary DESC ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING)` 的計算結果為？",
         "該部門中的最低薪資值（最後一名薪資）", ["該部門中的最低薪資值（最後一名薪資）", "最高薪資值", "當前薪資", "NULL"],
         "注意預設畫框為 `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`，若不顯式指定 `AND UNBOUNDED FOLLOWING`，LAST_VALUE 會只取到當前行而失效！指定後可正確取到最後一名。"),
        ("執行 SQL `SELECT dept_id, SUM(salary) FROM employees GROUP BY dept_id HAVING COUNT(*) >= 5;` 的語意為？",
         "篩選出「員工人數達到或超過 5 人」的部門，並計算其薪資總和", ["篩選出「員工人數達到或超過 5 人」的部門，並計算其薪資總和", "篩選出薪資超過 5 萬的員工", "隨機選取 5 個部門", "篩選出前 5 名部門"],
         "GROUP BY 分組配合 HAVING 過濾群組屬性，精準聚合分析。"),
        ("在關聯表 T(val) 中包含一筆紀錄 val = NULL。執行 `SELECT * FROM T WHERE val > 10 OR val <= 10;` 其回傳結果為？",
         "回傳 0 筆資料（空集合）", ["回傳 0 筆資料（空集合）", "回傳該筆 NULL 紀錄", "報錯", "回傳 1 筆"],
         "`val > 10` 為 UNKNOWN，`val <= 10` 亦為 UNKNOWN。UNKNOWN OR UNKNOWN 仍為 UNKNOWN，WHERE 子句過濾掉 UNKNOWN，故查無資料！此為三值邏輯經典悖論。"),
        ("若欲在 SQL 中篩選出 val 不等於 5 的所有紀錄（包含 val 為 NULL 的紀錄），正確的條件為？",
         "`WHERE val != 5 OR val IS NULL`", ["`WHERE val != 5 OR val IS NULL`", "`WHERE val != 5`", "`WHERE val <> 5`", "`WHERE NOT (val = 5)`"],
         "單純的 `val != 5` 遇到 NULL 會判定為 UNKNOWN 而漏失 NULL 資料列，必須顯式加上 `OR val IS NULL`。")
    ]

    for stem, ans_s, opts, expl in sql_calc:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "SQL綜合運算推導",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【SQL 數理邏輯與聚合計算推導】</strong><br>
<div class="step-box">
  <div class="step-title">📝 SQL 語意展開與三值邏輯計算</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>確認資料集內容與 NULL 狀態</strong><br>
      ‧ 本題依據 ANSI SQL 三值邏輯、聚合忽略規則或視窗畫框定義進行推導。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>執行逐步求值展開</strong><br>
      ‧ {expl}
    </li>
    <li class="step-item"><span class="step-badge check">步驟 3</span><strong>得出確切計算結果</strong><br>
      ‧ 正確答案為 <strong>{ans_s}</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) {ans_s}</strong>：完全符合 SQL 引擎規範。<br>
‧ 其餘選項常為忽略 NULL 規則或誤以為 `NULL != 5` 為 TRUE 之常見錯誤。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Aggregate Function</code> <span class="en">Aggregate Function</span>：聚集函數。<br>
‧ <code>Window Frame</code> <span class="en">Window Frame</span>：視窗畫框。<br>
‧ <code>Short-Circuit Evaluation</code> <span class="en">Short-Circuit</span>：短路求值。"""
        })

    # More SQL calc (25 items)
    more_sql_calc = [
        ("SQL 語句 `SELECT 'A' || NULL;`（字串串接）在多數標準關聯式資料庫中的結果為？", "NULL", ["NULL", "'A'", "'ANULL'", "''（空字串）"], "在 ANSI SQL 標準中，任何純量值與 NULL 串接或運算其結果皆傳播為 NULL（除非使用 CONCAT 函數在 MySQL 中的特殊處理）。"),
        ("SQL 語句 `SELECT NOT (UNKNOWN);` 的邏輯評估結果為？", "UNKNOWN", ["UNKNOWN", "TRUE", "FALSE", "NULL"], "三值邏輯否定表中：NOT TRUE = FALSE, NOT FALSE = TRUE, NOT UNKNOWN = UNKNOWN。"),
        ("SQL 語句 `SELECT TRUE AND UNKNOWN;` 的邏輯結果為？", "UNKNOWN", ["UNKNOWN", "TRUE", "FALSE", "NULL"], "AND 運算取兩者之最小值（TRUE=1, UNKNOWN=0.5, FALSE=0），min(1, 0.5) = 0.5 即 UNKNOWN。"),
        ("SQL 語句 `SELECT FALSE AND UNKNOWN;` 的邏輯結果為？", "FALSE", ["FALSE", "UNKNOWN", "TRUE", "NULL"], "min(0, 0.5) = 0 即 FALSE，只要有一方為 FALSE 則結果必為 FALSE。"),
        ("SQL 語句 `SELECT TRUE OR UNKNOWN;` 的邏輯結果為？", "TRUE", ["TRUE", "UNKNOWN", "FALSE", "NULL"], "OR 運算取最大值：max(1, 0.5) = 1 即 TRUE，只要有一方為 TRUE 則結果必為 TRUE。"),
        ("SQL 語句 `SELECT FALSE OR UNKNOWN;` 的邏輯結果為？", "UNKNOWN", ["UNKNOWN", "FALSE", "TRUE", "NULL"], "max(0, 0.5) = 0.5 即 UNKNOWN。"),
        ("在 SQL SELECT 查詢中，若同時出現 WHERE, GROUP BY, HAVING, ORDER BY，下列何者「無法」在 WHERE 子句中合法使用？", "聚集函數（如 SUM, COUNT）", ["聚集函數（如 SUM, COUNT）", "運算子 AND 與 OR", "子查詢", "BETWEEN 範圍"], "WHERE 在資料分組彙總前執行，無法引用聚合結果。"),
        ("若一資料表有 10 筆資料，執行 `SELECT TOP 50 PERCENT * FROM T;` 將回傳幾筆資料？", "5 筆資料", ["5 筆資料", "50 筆", "10 筆", "1 筆"], "PERCENT 取指定百分比筆數（10 * 50% = 5）。"),
        ("SQL 查詢中，`SELECT * FROM T ORDER BY col ASC;`，若 col 包含 NULL，在 ANSI SQL 標準下 NULL 預設排在？", "視 DBMS 實作而定（ANSI SQL 視 NULL 大於所有值，排在最後；Oracle 預設最後，MySQL 預設最前）", ["視 DBMS 實作而定（ANSI SQL 視 NULL 大於所有值，排在最後；Oracle 預設最後，MySQL 預設最前）", "所有資料庫永遠排在最前", "所有資料庫永遠排在最後", "自動忽略 NULL"], "可使用 `NULLS FIRST` 或 `NULLS LAST` 顯式控制。"),
        ("執行 SQL `SELECT 1 FROM dual WHERE 1 IN (2, 3, NULL);` 的結果為？", "回傳 0 筆資料（空集合）", ["回傳 0 筆資料（空集合）", "回傳 1", "報錯", "回傳 NULL"], "1 = 2 為 FALSE，1 = 3 為 FALSE，1 = NULL 為 UNKNOWN。FALSE OR FALSE OR UNKNOWN = UNKNOWN，不成立。"),
        ("執行 SQL `SELECT 1 FROM dual WHERE 2 IN (2, 3, NULL);` 的結果為？", "回傳 1 筆數值 1", ["回傳 1 筆數值 1", "回傳 0 筆資料", "報錯", "回傳 NULL"], "2 = 2 為 TRUE，TRUE OR ... = TRUE，命中條件。"),
        ("SQL 查詢 `SELECT employee_id, DENSE_RANK() OVER (ORDER BY salary DESC) as rk FROM emp;` 中，若有三位員工薪資最高且並列第一，下一位員工的 rk 為？", "2", ["2", "4", "3", "1"], "DENSE_RANK() 緊湊排列不跳號，三位並列 1 之後下一位必為 2。"),
        ("承上題，若改用 `RANK()` 函數，下一位員工的 rk 為？", "4", ["4", "2", "3", "1"], "RANK() 遇到同分跳號，三位佔據 1, 2, 3 號位置，下一位跳至 4。"),
        ("SQL 陳述式 `UPDATE T SET a = b, b = a;` 在標準關聯資料庫中執行時會？", "同時將 a 與 b 的數值原子性互換（Swap）", ["同時將 a 與 b 的數值原子性互換（Swap）", "使 a 與 b 皆等於 b 原來的值", "語法錯誤", "使 a 與 b 皆等於 a 原來的值"], "SQL SET 子句是原子並行求值，以資料列更新前的原始值進行賦值，優雅實現交換。"),
        ("在關聯表 T(a, b) 中，執行 `INSERT INTO T SELECT * FROM T;` 的效果為？", "將目前資料表中的所有資料列完整複製一份再次插入（資料量翻倍）", ["將目前資料表中的所有資料列完整複製一份再次插入（資料量翻倍）", "陷入無窮迴圈", "拋出主鍵衝突（若有主鍵）", "清空資料表"], "SELECT 讀取當前快照，批次插入；若有主鍵約束則因重複而失敗。"),
        ("SQL:2008 引入的 `TRUNCATE TABLE` 是否可以帶 WHERE 子句？", "絕對不能帶 WHERE 子句（一律清空全表）", ["絕對不能帶 WHERE 子句（一律清空全表）", "可以帶 WHERE 子句", "只有管理員可以帶", "視資料量而定"], "TRUNCATE 是物理釋放頁面，不支援行過濾。"),
        ("執行 SQL `SELECT COUNT(1) FROM T;` 與 `SELECT COUNT(*) FROM T;` 在現代主流資料庫引擎中的效能比較為？", "效能完全相同（最佳化器內部處理機制完全等價）", ["效能完全相同（最佳化器內部處理機制完全等價）", "COUNT(1) 明顯較快", "COUNT(*) 明顯較快", "COUNT(1) 佔用較少記憶體"], "都市傳說澄清題！現代優化器皆將其統一重寫為統計資料列總數。"),
        ("SQL 視窗函數中，若僅寫 `OVER (PARTITION BY dept_id)` 而未指定 `ORDER BY`，則預設的視窗畫框為？", "分組內的所有資料列（ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING）", ["分組內的所有資料列（ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING）", "僅當前列", "第一列到當前列", "空集合"], "無排序時整個分區視為一個整體畫框，聚合計算等價於該部門全體聚合。"),
        ("SQL 查詢 `SELECT ASCII('A');` 的回傳結果為？", "65", ["65", "97", "1", "48"], "標準 ASCII 碼字元轉換。"),
        ("SQL 查詢 `SELECT MOD(17, 5);` 的回傳結果為？", "2", ["2", "3", "3.4", "1"], "17 除以 5 商 3 餘 2。"),
        ("執行 SQL `SELECT ROUND(123.456, 2);` 的回傳結果為？", "123.46", ["123.46", "123.45", "123", "120"], "四捨五入取小數點後兩位。"),
        ("執行 SQL `SELECT TRUNCATE(123.456, 2);`（或 TRUNC）的回傳結果為？", "123.45", ["123.45", "123.46", "123", "120"], "直接截斷小數點後兩位不進位。"),
        ("SQL 函數 `SUBSTRING('DATABASE', 5, 4)` 的回傳結果為？", "'BASE'", ["'BASE'", "'DATA'", "'ATAB'", "'ASE'"], "從第 5 個字元（B）開始擷取長度為 4 的子字串。"),
        ("SQL 函數 `LENGTH('IT')` 與 `LENGTH('資訊')` 在以 UTF-8 位元組計算長度時分別為？", "2 與 6（中文字佔 3 位元組）", ["2 與 6（中文字佔 3 位元組）", "2 與 2", "2 與 4", "1 與 2"], "BYTE 長度 vs CHAR 長度區分。"),
        ("SQL 查詢中使用 `BETWEEN 10 AND 20` 是否包含端點 10 與 20？", "包含（等價於 `val >= 10 AND val <= 20` 閉區間）", ["包含（等價於 `val >= 10 AND val <= 20` 閉區間）", "不包含（開區間）", "僅包含 10", "僅包含 20"], "BETWEEN 恆為封閉區間。")
    ]

    for stem, ans_s, opts, expl in more_sql_calc:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "SQL函數與邊界運算",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【SQL 內建函數與運算子行為剖析】</strong><br>
‧ <strong>(A) {ans_s}</strong>：依 ANSI SQL 標準推導，{expl}<br>
‧ 其餘選項皆存在運算優先級或字串函數索引基數認知偏誤。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Atomic Swap</code> <span class="en">Atomic Swap</span>：原子交換。<br>
‧ <code>Closed Interval</code> <span class="en">Closed Interval</span>：閉區間。<br>
‧ <code>Dense Rank</code> <span class="en">Dense Rank</span>：無跳號密集排名。"""
        })

    # -------------------------------------------------------------
    # 2. 複雜關聯代數運算等價變換 (35 題)
    # -------------------------------------------------------------
    ra_comp = [
        ("關聯代數等價變換規則中，選擇運算對卡氏積的分配律表示為？",
         "若條件 c 僅涉及關聯 R 的屬性，則 σ_c(R × S) ≡ (σ_c(R)) × S", ["若條件 c 僅涉及關聯 R 的屬性，則 σ_c(R × S) ≡ (σ_c(R)) × S", "σ_c(R × S) ≡ σ_c(R) × σ_c(S)", "σ_c(R × S) ≡ R × σ_c(S)", "無法分配"],
         "查詢最佳化下推選擇的核心依據：若篩選條件僅依賴 R，即可在進行龐大的笛卡兒乘積前先對 R 執行過濾。"),
        ("關聯代數等價變換規則中，投影運算對聯集的分配律為？",
         "π_L(R ∪ S) ≡ π_L(R) ∪ π_L(S)", ["π_L(R ∪ S) ≡ π_L(R) ∪ π_L(S)", "π_L(R ∪ S) ≡ π_L(R) ∩ π_L(S)", "π_L(R ∪ S) ≡ π_L(R) × π_L(S)", "無法分配"],
         "對兩表聯集進行投影，等價於分別投影後再聯集。"),
        ("關聯代數等價變換中，若 L 為屬性集合，且 L ⊆ L'，則兩次投影的合成律為？",
         "π_L(π_{L'}(R)) ≡ π_L(R)", ["π_L(π_{L'}(R)) ≡ π_L(R)", "π_L(π_{L'}(R)) ≡ π_{L'}(R)", "π_L(π_{L'}(R)) ≡ R", "無法合成"],
         "連續多次投影最終等價於最後一次最嚴格（屬性最少）的投影。"),
        ("關聯代數中，自然連接 R ⋈ S 與 S ⋈ R 的關係為？",
         "完全等價（自然連接具備交換律）", ["完全等價（自然連接具備交換律）", "結果屬性順序相反故不相等", "僅在兩表大小相等時等價", "不具備交換律"],
         "關聯元組中屬性以名稱標識，順序不影響語意，自然連接嚴格滿足交換律與結合律。"),
        ("關聯代數中，差集運算與投影運算是否可自由交換？即 π_L(R − S) 與 (π_L(R) − π_L(S)) 是否等價？",
         "「不一定等價」（通常 π_L(R − S) ⊇ (π_L(R) − π_L(S))，不可任意下推）", ["「不一定等價」（通常 π_L(R − S) ⊇ (π_L(R) − π_L(S))，不可任意下推）", "必定完全等價", "必定無交集", "兩者皆為空集"],
         "反例：R = {(1, a)}, S = {(1, b)}。R - S = {(1, a)}，投影第一欄得 {1}。但 π(R) = {1}, π(S) = {1}，兩者相減為 ∅！故投影不能隨意下推至差集內部！極重要考點。"),
        ("關聯代數中，交集運算 R ∩ S 是否滿足交換律與結合律？",
         "同時滿足交換律與結合律", ["同時滿足交換律與結合律", "僅滿足交換律", "僅滿足結合律", "兩者皆不滿足"],
         "交集具對稱性，R ∩ S = S ∩ R 且 (R ∩ S) ∩ T = R ∩ (S ∩ T)。"),
        ("在關聯代數運算樹（Relational Algebra Tree）中，葉節點通常代表何者？",
         "基礎關聯資料表（Base Relations / Tables）", ["基礎關聯資料表（Base Relations / Tables）", "選擇條件", "投影欄位", "輸出結果集"],
         "語法剖析樹以關聯表為樹葉，以各代數運算子（σ, π, ⋈）為內部節點，樹根為最終輸出。"),
        ("對於包含多個連接運算式的查詢 (R ⋈ S ⋈ T)，共有幾種相異的結合順序（連接樹拓樸）？",
         "由卡特蘭數決定（多種可能順序）", ["由卡特蘭數決定（多種可能順序）", "只有 1 種", "只有 2 種", "無窮多種"],
         "最佳化器必須搜尋動態規劃空間（如左深樹 Left-Deep Tree、叢集樹 Bushy Tree）以挑選成本最小的連接拓樸。"),
        ("左深樹（Left-Deep Tree）在查詢執行引擎中受到極大青睞的主因是？",
         "便於管線化（Pipelining）執行，任何時刻記憶體中僅需常駐一張內部表的雜湊表或緩衝區", ["便於管線化（Pipelining）執行，任何時刻記憶體中僅需常駐一張內部表的雜湊表或緩衝區", "樹的高度最高", "生成的代數規則最少", "完全不需要快取"], "左深樹每一層的右子節點必為基礎表，極大降低記憶體空間開銷。"),
        ("若關聯 R 包含 1000 筆資料，S 包含 20 筆資料，計算 R ⋈ S 時，若採用雜湊連接（Hash Join），最佳策略為？",
         "以較小的 S 作為構建表（Build Table）在記憶體建立雜湊表，再掃描 R 進行探測（Probe Table）", ["以較小的 S 作為構建表（Build Table）在記憶體建立雜湊表，再掃描 R 進行探測（Probe Table）", "以 R 作為構建表，S 作為探測表", "兩表同時建立雜湊表", "隨機選擇"], "將小表放入記憶體建立雜湊映射，大表單趟串流探測即可，記憶體開銷最小。")
    ]

    for stem, ans_s, opts, expl in ra_comp:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "關聯代數等價轉換推導",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【關聯代數等價轉換與查詢樹推導】</strong><br>
<div class="step-box">
  <div class="step-title">📝 代數等價規則與最佳化分析</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>確認代數運算子分配與結合性質</strong><br>
      ‧ 本題依據關聯代數等價變換定理進行結構分析。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>執行代數恆等式驗證</strong><br>
      ‧ {expl}
    </li>
    <li class="step-item"><span class="step-badge check">步驟 3</span><strong>得出精準結論</strong><br>
      ‧ 正確答案為 <strong>{ans_s}</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) {ans_s}</strong>：完全符合關聯代數定理。<br>
‧ 其餘選項皆為投影下推邊界條件遺漏或左深樹特性誤判。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Left-Deep Tree</code> <span class="en">Left-Deep Tree</span>：左深樹。<br>
‧ <code>Equivalence Rule</code> <span class="en">Equivalence Rule</span>：等價變換規則。<br>
‧ <code>Pipelining</code> <span class="en">Pipelining</span>：管線化串流處理。"""
        })

    # More RA equivalent items (25 items)
    more_ra_comp = [
        ("在關聯代數中，σ_{c1 ∨ c2}(R) 等價於下列何種集合操作？", "σ_{c1}(R) ∪ σ_{c2}(R)", ["σ_{c1}(R) ∪ σ_{c2}(R)", "σ_{c1}(R) ∩ σ_{c2}(R)", "σ_{c1}(R) − σ_{c2}(R)", "σ_{c1}(R) × σ_{c2}(R)"], "OR 條件可分解為兩次獨立選擇的聯集。"),
        ("在關聯代數中，σ_{c1 ∧ c2}(R) 等價於下列何種集合操作？", "σ_{c1}(R) ∩ σ_{c2}(R)", ["σ_{c1}(R) ∩ σ_{c2}(R)", "σ_{c1}(R) ∪ σ_{c2}(R)", "σ_{c1}(R) − σ_{c2}(R)", "σ_{c1}(R × S)"], "AND 條件等價於兩次選擇結果的交集。"),
        ("若在自然連接 R ⋈ S 中，R 與 S 之間「沒有任何同名屬性」，則該自然連接等價於？", "卡氏積（Cartesian Product R × S）", ["卡氏積（Cartesian Product R × S）", "空集合 ∅", "R ∪ S", "R − S"], "無任何公共約束，自然退化為完全全排列卡氏積。"),
        ("查詢最佳化中，啟發式規則（Heuristic Rules）通常優先執行的轉換為？", "盡早執行選擇運算（Pushdown Selection）與投影運算（Pushdown Projection）", ["盡早執行選擇運算（Pushdown Selection）與投影運算（Pushdown Projection）", "盡早執行全表掃描", "最後再執行選擇運算", "增加卡氏積運算"], "大幅消除中間結果資料量。"),
        ("若關聯 R 包含 10 筆資料，S 包含 10 筆資料，則 R ∪ S 的紀錄筆數範圍為？", "10 筆到 20 筆之間", ["10 筆到 20 筆之間", "恰好 20 筆", "恰好 10 筆", "0 筆到 20 筆之間"], "若雙方完全重疊則為 10 筆；若完全無重疊則為 20 筆。"),
        ("若關聯 R 包含 10 筆資料，S 包含 10 筆資料，則 R ∩ S 的紀錄筆數範圍為？", "0 筆到 10 筆之間", ["0 筆到 10 筆之間", "恰好 10 筆", "10 筆到 20 筆之間", "20 筆"], "交集上限為 min(|R|, |S|)，下限為空集 0。"),
        ("若關聯 R 包含 10 筆資料，S 包含 10 筆資料，則 R − S 的紀錄筆數範圍為？", "0 筆到 10 筆之間", ["0 筆到 10 筆之間", "恰好 10 筆", "10 筆到 20 筆之間", "0 筆"], "若 R 完全被 S 包含則為 0；若兩者互斥則為 10。"),
        ("元組關聯演算（Tuple Relational Calculus, TRC）的表達式形式通常為？", "{ t | P(t) }（尋找所有使述語 P 成立的元組 t）", ["{ t | P(t) }（尋找所有使述語 P 成立的元組 t）", "{ <x, y> | P(x, y) }", "SELECT t FROM R", "σ_P(R)"], "變數 t 代表完整的資料列元組（Tuple Variable）。"),
        ("領域關聯演算（Domain Relational Calculus, DRC）的表達式形式通常為？", "{ <x1, x2, ..., xn> | P(x1, x2, ..., xn) }（變數代表單一欄位網域值）", ["{ <x1, x2, ..., xn> | P(x1, x2, ..., xn) }（變數代表單一欄位網域值）", "{ t | P(t) }", "π(R)", "R × S"], "變數代表個別屬性領域（Domain Variable），QBE（Query-By-Example）語言即基於 DRC 開發。"),
        ("QBE（Query-By-Example）是以何種理論模型為基礎所發展出的視覺化查詢語言？", "領域關聯演算（Domain Relational Calculus, DRC）", ["領域關聯演算（Domain Relational Calculus, DRC）", "元組關聯演算", "關聯代數", "第一正規化"], "IBM 著名二維表格範例填空查詢語言。"),
        ("若查詢包含嵌套的關聯代數式，資料庫系統會先將其轉換為？", "查詢樹（Query Tree / Logical Query Plan）", ["查詢樹（Query Tree / Logical Query Plan）", "二進位執行檔", "組合語言", "作業系統執行緒"], "建立代數樹以便應用等價規則進行最佳化重構。"),
        ("外連接能否與普通內部連接自由互換次序？", "不能（外連接通常不具備與內連接之結合律，需極為小心重排）", ["不能（外連接通常不具備與內連接之結合律，需極為小心重排）", "完全可以自由互換", "視欄位數量而定", "僅在兩表為空時可以"], "外連接保留 NULL，重排順序會改變過濾結果，優化器通常無法隨意交換外連接與內連接。"),
        ("下列何種運算子可以由選擇與卡氏積直接合成？", "θ-連接（Theta Join）", ["θ-連接（Theta Join）", "聯集", "差集", "投影"], "R ⋈_θ S = σ_θ (R × S)。"),
        ("投影運算 π_{A}(R) 在關聯代數中必然滿足何種性質？", "去除重複項後輸出唯一的 A 數值集合", ["去除重複項後輸出唯一的 A 數值集合", "保留重複項", "自動按升序排列", "輸出 NULL"], "純集合運算自然去重。"),
        ("若關聯 R 包含 0 筆資料（空表），則 R × S 的結果為？", "0 筆資料（空集合）", ["0 筆資料（空集合）", "S 的資料筆數", "NULL", "1 筆"], "0 × |S| = 0。"),
        ("若關聯 R 包含 0 筆資料，則 R ∪ S 的結果為？", "S 的所有資料（|S| 筆）", ["S 的所有資料（|S| 筆）", "空集合", "NULL", "0 筆"], "∅ ∪ S = S。"),
        ("若關聯 R 包含 0 筆資料，則 R ∩ S 的結果為？", "空集合（0 筆）", ["空集合（0 筆）", "S 的資料", "NULL", "報錯"], "∅ ∩ S = ∅。"),
        ("若關聯 R 包含 0 筆資料，則 R − S 的結果為？", "空集合（0 筆）", ["空集合（0 筆）", "S 的資料", "負數", "報錯"], "∅ − S = ∅。"),
        ("若關聯 R 包含 0 筆資料，則 S − R 的結果為？", "S 的所有資料（|S| 筆）", ["S 的所有資料（|S| 筆）", "空集合", "0 筆", "報錯"], "S − ∅ = S。"),
        ("關聯代數運算式中，最耗費運算資源的原始運算子通常為？", "卡氏積（Cartesian Product ×）", ["卡氏積（Cartesian Product ×）", "投影 π", "選擇 σ", "重命名 ρ"], "資料規模呈乘積暴增，需盡可能避免純卡氏積。"),
        ("在關聯代數中，若 A 為主鍵，則 σ_{A=val}(R) 的結果元組數最多為？", "1 筆", ["1 筆", "0 筆", "無限多筆", "與資料表大小相同"], "主鍵保證唯一性。"),
        ("若要表達「所有修習了 C1 課程的學生學號」，關聯代數應寫為？", "π_{sid} ( σ_{cid='C1'} (Enroll) )", ["π_{sid} ( σ_{cid='C1'} (Enroll) )", "σ_{sid} ( π_{cid='C1'} (Enroll) )", "Enroll ÷ C1", "Enroll × C1"], "標準投影與選擇組合。"),
        ("在 SQL:2016 中支援多態資料表函數（PTF），其在關聯代數中屬於？", "擴展關聯運算子", ["擴展關聯運算子", "基本運算子", "卡氏積", "差集"], "現代擴充語義。"),
        ("若 R 與 S 的交集 R ∩ S 可用差集表示為？", "R − (R − S)", ["R − (R − S)", "R − S", "(R − S) ∪ S", "S − R"], "從 R 中扣除「專屬於 R 的部分」，剩餘的即為共有交集。"),
        ("在分散式查詢中，將查詢分解為多個片段在本地端並行執行的技術稱為？", "分散式關聯代數查詢重寫（Query Localization & Parallelization）", ["分散式關聯代數查詢重寫（Query Localization & Parallelization）", "集中式處理", "單線程運算", "強制同步"], "透過水平分片聯合將全局運算下推至各節點並行完成。")
    ]

    for stem, ans_s, opts, expl in more_ra_comp:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "關聯代數深度性質",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【關聯代數進階運算剖析】</strong><br>
‧ <strong>(A) {ans_s}</strong>：依原理推導，{expl}<br>
‧ 其餘選項皆存在集合代數運算邊界誤判。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Query Tree</code> <span class="en">Query Tree</span>：查詢樹。<br>
‧ <code>Domain Relational Calculus (DRC)</code> <span class="en">Domain Relational Calculus</span>：領域關聯演算。<br>
‧ <code>Cartesian Bottleneck</code> <span class="en">Cartesian Bottleneck</span>：卡氏積效能瓶頸。"""
        })

    # -------------------------------------------------------------
    # 3. 交易排程可序列化與圖形推導 (30 題)
    # -------------------------------------------------------------
    tx_graph = [
        ("給定排程 S: r1(A); w1(A); r2(A); w2(A); r1(B); w1(B); r2(B); w2(B)。檢驗其優先圖（Precedence Graph）：",
         "包含有向邊 T1 -> T2，無環，故為衝突可序列化（Conflict Serializable）且等價於串列順序 <T1, T2>", ["包含有向邊 T1 -> T2，無環，故為衝突可序列化（Conflict Serializable）且等價於串列順序 <T1, T2>", "包含雙向邊產生環，非衝突可序列化", "等價於 <T2, T1>", "包含死結無法執行"],
         "分析衝突操作：w1(A) 先於 r2(A)/w2(A) 執行，產生邊 T1 -> T2；w1(B) 先於 r2(B)/w2(B) 執行，產生邊 T1 -> T2。圖中僅有 T1 -> T2，無反向邊，圖為 DAG（無環），等價於 <T1, T2>。"),
        ("給定排程 S: r1(A); w2(A); r2(B); w1(B)。檢驗其優先圖：",
         "包含邊 T1 -> T2（因 r1(A) 先於 w2(A)）與邊 T2 -> T1（因 r2(B) 先於 w1(B)），存在環，故「非衝突可序列化」", ["包含邊 T1 -> T2（因 r1(A) 先於 w2(A)）與邊 T2 -> T1（因 r2(B) 先於 w1(B)），存在環，故「非衝突可序列化」", "為衝突可序列化", "等價於 <T1, T2>", "無任何衝突操作"],
         "兩交易相互等待交錯寫入，優先圖形成循環環路 T1 -> T2 -> T1，破壞衝突可序列化！"),
        ("若一個排程為衝突可序列化，對其優先圖進行下列何種演算法即可求得等價的循序交易序列？",
         "拓樸排序演算法（Topological Sort）", ["拓樸排序演算法（Topological Sort）", "Dijkstra 最短路徑", "Kruskal 演算法", "二元搜尋"],
         "DAG 拓樸排序所得之線性序列即為等價的交易串列執行序列。"),
        ("在兩階段鎖定（2PL）中，若交易 T 在釋放了某個共用鎖後，又發出請求欲取得一個排他鎖，該行為違反了？",
         "2PL 的收縮階段（Shrinking Phase）規則（一旦釋放鎖，便絕對不能再獲取任何鎖）", ["2PL 的收縮階段（Shrinking Phase）規則（一旦釋放鎖，便絕對不能再獲取任何鎖）", "成長階段規則", "死結預防規則", "ACID 原子性"],
         "2PL 核心鐵律：成長期只加不釋，收縮期只釋不加。違反此規則將無法保證衝突可序列化。"),
        ("保守兩階段鎖定（Conservative 2PL / Static 2PL）的具體作法為？",
         "交易在「開始執行前，一次預先宣告並取得其所需的所有鎖定」；若無法全數取得則一個都不拿並等待", ["交易在「開始執行前，一次預先宣告並取得其所需的所有鎖定」；若無法全數取得則一個都不拿並等待", "隨用隨鎖", "僅在 Commit 時取鎖", "不使用任何鎖"],
         "一次全拿策略徹底消除了「持有並等待（Hold and Wait）」條件，故「保證絕不發生死結（Deadlock-Free）」；缺點是並發度大幅降低且需預知所有存取資料。"),
        ("死結（Deadlock）發生的四個必要條件（Coffman 條件）中，不包含下列何者？",
         "可搶佔性（Preemption Allowed）", ["可搶佔性（Preemption Allowed）", "互斥條件（Mutual Exclusion）", "持有並等待（Hold and Wait）", "循環等待（Circular Wait）"],
         "必要條件為「不可搶佔（No Preemption）」！若資源可被隨意搶佔，死結便無法形成。"),
        ("在鎖定機制中，何謂「鎖定升級（Lock Escalation）」？",
         "當單一交易所持有的細粒度鎖定（如列鎖 Row Locks）過多時，系統自動將其轉換為粗粒度鎖定（如表鎖 Table Lock）以節省記憶體", ["當單一交易所持有的細粒度鎖定（如列鎖 Row Locks）過多時，系統自動將其轉換為粗粒度鎖定（如表鎖 Table Lock）以節省記憶體", "將共用鎖轉為排他鎖", "延長鎖定時間", "強制釋放鎖定"], "降低鎖定管理員的記憶體負載，但會重創其他交易的並行存取自由度。"),
        ("何謂「鎖定降級（Lock Demotion）」？",
         "將交易持有的排他鎖（X-Lock）轉化為共享鎖（S-Lock）", ["將交易持有的排他鎖（X-Lock）轉化為共享鎖（S-Lock）", "釋放所有鎖定", "表鎖轉列鎖", "強制交易中止"], "允許在完成寫入後轉為只讀，在 2PL 收縮階段中屬於合法操作。"),
        ("在多版本並行控制（MVCC）中，每筆資料列通常隱含兩個系統欄位，分別記錄？",
         "創建該資料列的交易 ID（xmin / DB_TRX_ID）與刪除/過期該資料列的交易 ID（xmax / DB_ROLL_PTR）", ["創建該資料列的交易 ID（xmin / DB_TRX_ID）與刪除/過期該資料列的交易 ID（xmax / DB_ROLL_PTR）", "使用者密碼與權限", "硬碟磁軌號與磁區號", "索引高度與指針"], "透過比較當前查詢交易的 ID 與資料列的版本區間，決定該列對當前交易是否可見。"),
        ("若交易 T1 優先圖中指向 T2，T2 指向 T3，T3 指向 T1，則系統發生了？",
         "非衝突可序列化異常（若為 Precedence Graph），或死結狀態（若為 Wait-For Graph）", ["非衝突可序列化異常（若為 Precedence Graph），或死結狀態（若為 Wait-For Graph）", "系統正常完成", "自動提升權限", "快取命中"], "優先圖有環破壞可序列化；等待圖有環代表互相鎖定死結。")
    ]

    for stem, ans_s, opts, expl in tx_graph:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "交易圖論與死結矩陣",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【優先圖與死結等待圖嚴格推導】</strong><br>
<div class="step-box">
  <div class="step-title">📝 優先圖（Precedence Graph）分析步驟</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>列舉所有衝突操作對</strong><br>
      ‧ 檢驗跨交易、同變數、含寫入之操作先後順序。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>繪製有向邊並檢測有向環</strong><br>
      ‧ {expl}
    </li>
    <li class="step-item"><span class="step-badge check">步驟 3</span><strong>得出精準結論</strong><br>
      ‧ 答案為 <strong>{ans_s}</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) {ans_s}</strong>：衝突邊拓樸分析完全精確。<br>
‧ 其餘選項皆為漏看衝突操作或環路方向判定錯誤。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Precedence Graph (Serialization Graph)</code> <span class="en">Precedence Graph</span>：優先圖。<br>
‧ <code>Wait-For Graph (WFG)</code> <span class="en">Wait-For Graph</span>：等待圖。<br>
‧ <code>Lock Escalation</code> <span class="en">Lock Escalation</span>：鎖定升級。"""
        })

    # More tx graph items (20 items)
    more_tx_graph = [
        ("在資料庫排程 S 中，若所有交易的操作完全不交錯，一個交易執行完畢 commit 後下一個交易才開始，此種排程稱為？", "循序排程（Serial Schedule）", ["循序排程（Serial Schedule）", "並行排程", "非可序列化排程", "隨機排程"], "串列排程天然保證絕對一致性，但完全無並行度。"),
        ("若一個並行排程與某個循序排程具有完全相同的執行結果，稱該並行排程為？", "可序列化排程（Serializable Schedule）", ["可序列化排程（Serializable Schedule）", "嚴格排程", "無鎖排程", "死結排程"], "並行排程的最高正確性黃金準則。"),
        ("若排程 S 可以透過交換一系列相鄰的「非衝突操作」轉化為循序排程 S'，則稱 S 為？", "衝突可序列化排程（Conflict Serializable Schedule）", ["衝突可序列化排程（Conflict Serializable Schedule）", "檢視可序列化", "嚴格排程", "兩階段排程"], "衝突等價定義。"),
        ("在資料庫中，讀取操作是否會持有排他鎖？", "不會，讀取操作預設僅請求共用鎖（S-Lock）", ["不會，讀取操作預設僅請求共用鎖（S-Lock）", "會，永遠持有排他鎖", "視資料庫名稱而定", "僅在星期一持有"], "排他鎖僅賦予修改寫入操作。"),
        ("語法 `SELECT ... FOR UPDATE` 在交易中的功用為？", "在讀取資料時顯式對該資料列加上「排他鎖（X-Lock）」，防止其他交易在此期間修改", ["在讀取資料時顯式對該資料列加上「排他鎖（X-Lock）」，防止其他交易在此期間修改", "自動修改資料", "強制提交", "刪除該資料列"], "悲觀鎖（Pessimistic Locking）標準語法，確保後續更新時資料未被他人竄改。"),
        ("語法 `SELECT ... LOCK IN SHARE MODE`（或 FOR SHARE）的功用為？", "對讀取的資料列加上共用鎖（S-Lock），防止其他交易進行修改但允許其他交易並行讀取", ["對讀取的資料列加上共用鎖（S-Lock），防止其他交易進行修改但允許其他交易並行讀取", "加上排他鎖", "解除鎖定", "忽略鎖定"], "顯式宣告共享鎖。"),
        ("在分散式死結偵測中，邊緣追蹤演算法（Edge-Chasing Algorithm）透過在節點間傳遞何種訊息偵測死結？", "探針訊息（Probe Messages / Initiator Probes）", ["探針訊息（Probe Messages / Initiator Probes）", "日誌檔案", "心跳封包", "資料表副本"], "沿着等待鏈轉發 Probe，若發起者收到自己發出的 Probe 即偵測到全域死結環。"),
        ("在樂觀並行控制的驗證階段中，若交易 Ti 意圖提交，其必須與所有「並行且已提交的交易 Tj」驗證何種條件？", "Ti 的讀取集合（ReadSet）不得與 Tj 的寫入集合（WriteSet）發生交集重疊", ["Ti 的讀取集合（ReadSet）不得與 Tj 的寫入集合（WriteSet）發生交集重疊", "Ti 與 Tj 必須存取相同資料", "Ti 必須比 Tj 晚啟動", "交易金額必須相等"], "確保 Ti 讀取的資料在此期間未被 Tj 污染。"),
        ("時間戳排序協定中，若交易 T 發出 write(Q)，但其時間戳 TS(T) < R-TS(Q)（即 Q 已經被更年輕的交易讀取過了），系統將？", "中止並回滾 T（Abort and Rollback T），並賦予新時間戳重試", ["中止並回滾 T（Abort and Rollback T），並賦予新時間戳重試", "允許覆蓋", "忽略該寫入", "暫停系統"], "防止年輕交易讀到過時舊值。"),
        ("Thomas 寫入規則（Thomas' Write Rule）對上述情況的例外優化為？", "若 TS(T) < W-TS(Q)，此寫入為過時的盲寫，系統直接「忽略該 write 操作」而無須回滾 T！", ["若 TS(T) < W-TS(Q)，此寫入為過時的盲寫，系統直接「忽略該 write 操作」而無須回滾 T！", "強制回滾", "拋出例外", "鎖定資料表"], "巧妙利用盲寫特性，減少無謂的回滾，使排程超越衝突可序列化達成檢視可序列化。"),
        ("樹狀鎖定協定（Tree-Locking Protocol / Directed Graph Locking）適用於何種資料庫模型？", "資料項目呈現偏序樹狀結構（如 B+ 樹節點存取），不遵循 2PL 亦能保證可序列化且無死結", ["資料項目呈現偏序樹狀結構（如 B+ 樹節點存取），不遵循 2PL 亦能保證可序列化且無死結", "所有關聯表", "文字檔案", "隨機圖形"], "先鎖父再鎖子、由上而下，保證無環無死結，早期釋放鎖提升並行度。"),
        ("意圖鎖（IS / IX）通常存放在資料庫系統的？", "記憶體中的鎖定表（Lock Table in RAM）", ["記憶體中的鎖定表（Lock Table in RAM）", "磁碟資料頁標頭", "Redo Log 檔案", "用戶端快取"], "高效率雜湊鎖定表。"),
        ("兩階段鎖定中，若所有交易皆以「全域相同的字典順序」請求鎖定（如一律先鎖 A 再鎖 B），則？", "保證絕不發生死結（Deadlock-Free）", ["保證絕不發生死結（Deadlock-Free）", "必然發生死結", "無法序列化", "時間複雜度變為 O(n²)"], "破壞循環等待（Circular Wait）條件。"),
        ("在多粒度鎖定中，若欲修改某資料頁中的某一列，正確的加鎖路徑為？", "在資料庫加 IX 鎖 -> 在資料表加 IX 鎖 -> 在資料頁加 IX 鎖 -> 在資料列加 X 鎖", ["在資料庫加 IX 鎖 -> 在資料表加 IX 鎖 -> 在資料頁加 IX 鎖 -> 在資料列加 X 鎖", "直接在資料列加 X 鎖", "在資料庫加 X 鎖", "全表加 S 鎖"], "自根向下加意圖鎖，葉端加實際排他鎖。"),
        ("在多粒度鎖定中，若欲讀取整個資料表，應在表層級請求何種鎖？", "共享鎖（S-Lock）", ["共享鎖（S-Lock）", "意圖共享鎖（IS）", "排他鎖（X）", "意圖排他鎖（IX）"], "表級 S 鎖確保整張表讀取期間無人能在任何列進行修改。"),
        ("並行控制中，「封鎖粒度（Lock Granularity）」越大（如表鎖 vs 列鎖），對系統的影響為？", "並行度降低（Concurrency drops），但鎖定開銷極小（Lock overhead is low）", ["並行度降低（Concurrency drops），但鎖定開銷極小（Lock overhead is low）", "並行度升高", "鎖定開銷增加", "完全無影響"], "粒度粗省記憶體但並行差；粒度細並發高但管理鎖開銷大。"),
        ("死結預防策略相較於死結偵測與解除策略，其缺點為？", "可能產生大量不必要的「無辜交易回滾（Spurious Aborts）」或降低資源利用率", ["可能產生大量不必要的「無辜交易回滾（Spurious Aborts）」或降低資源利用率", "演算法極其複雜", "佔用大量 CPU", "無法保證不發生死結"], "寧可錯殺一千不可使一人等待，防衛過當導致回滾過多。"),
        ("死結解除時，「回滾到儲存點（Savepoint）」的優勢為？", "僅部分回滾（Partial Rollback）打破等待環，避免整個長事務完全重頭執行", ["僅部分回滾（Partial Rollback）打破等待環，避免整個長事務完全重頭執行", "清空資料庫", "不需要日誌", "自動消除所有鎖"], "細粒度儲存點大幅降低重試代價。"),
        ("在 ANSI 隔離等級中，READ UNCOMMITTED 允許何種並行異常？", "允許髒讀、不可重複讀與幻讀", ["允許髒讀、不可重複讀與幻讀", "僅允許幻讀", "不允許髒讀", "杜絕所有異常"], "最低隔離等級，完全不加讀鎖。"),
        ("在 ANSI 隔離等級中，READ COMMITTED 杜絕了下列何種異常？", "杜絕髒讀（但仍允許不可重複讀與幻讀）", ["杜絕髒讀（但仍允許不可重複讀與幻讀）", "杜絕幻讀", "杜絕不可重複讀", "杜絕寫入偏斜"], "主流資料庫（如 Oracle, PostgreSQL）之預設等級。")
    ]

    for stem, ans_s, opts, expl in more_tx_graph:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "排程分析與進階鎖定",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【鎖定協定與排程分析機制】</strong><br>
‧ <strong>(A) {ans_s}</strong>：依原理推導，{expl}<br>
‧ 其餘選項皆存在並行控制術語或多粒度路徑判定錯誤。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Thomas' Write Rule</code> <span class="en">Thomas' Write Rule</span>：湯瑪斯寫入規則。<br>
‧ <code>Lock Granularity</code> <span class="en">Lock Granularity</span>：鎖定粒度。<br>
‧ <code>Pessimistic Locking</code> <span class="en">Pessimistic Locking</span>：悲觀鎖定。"""
        })

    return qs

if __name__ == '__main__':
    qs = get_db_part4_questions()
    print(f"Generated DB Part 4 questions: {len(qs)}")
