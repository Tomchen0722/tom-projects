# -*- coding: utf-8 -*-
"""
Comprehensive Data Structures Question Bank Generator (395 unique questions)
For 01-senior3/ds-bank.html to reach exactly 700 unique, high-difficulty exam questions.
"""

def get_all_ds_questions():
    qs = []

    # -------------------------------------------------------------
    # 1. 遞迴關係式與主定理推導 (40 題)
    # -------------------------------------------------------------
    recurrence_data = [
        ("T(n) = 2T(n/2) + n", "Θ(n log n)", "Case 2", "a=2, b=2, f(n)=n. log_b(a) = log_2(2) = 1, n^1 = n = f(n). 為 Case 2，T(n) = Θ(n log n)。Merge Sort 經典遞迴式。"),
        ("T(n) = 4T(n/2) + n", "Θ(n²)", "Case 1", "a=4, b=2, f(n)=n. log_b(a) = log_2(4) = 2, n^2 比 f(n)=n 大多項式等級。為 Case 1，樹葉層主導，T(n) = Θ(n²)。"),
        ("T(n) = 4T(n/2) + n²", "Θ(n² log n)", "Case 2", "a=4, b=2, f(n)=n². log_b(a) = log_2(4) = 2, n^2 = f(n)。為 Case 2，T(n) = Θ(n² log n)。"),
        ("T(n) = 4T(n/2) + n³", "Θ(n³)", "Case 3", "a=4, b=2, f(n)=n³. log_b(a) = 2, f(n)=n³ 大於 n²。正則條件 4(n/2)³ = n³/2 <= c*n³ (c=1/2)。為 Case 3，T(n) = Θ(n³)。"),
        ("T(n) = 8T(n/2) + n²", "Θ(n³)", "Case 1", "a=8, b=2, f(n)=n². log_b(a) = log_2(8) = 3, n^3 大於 n²。為 Case 1，T(n) = Θ(n³)。"),
        ("T(n) = 2T(n/2) + 1", "Θ(n)", "Case 1", "a=2, b=2, f(n)=1. log_b(a) = 1, n^1 大於 1。為 Case 1，T(n) = Θ(n)。"),
        ("T(n) = T(n/2) + 1", "Θ(log n)", "Case 2", "a=1, b=2, f(n)=1. log_b(a) = 0, n^0 = 1 = f(n)。為 Case 2，T(n) = Θ(log n)。二元搜尋經典遞迴。"),
        ("T(n) = T(n/2) + n", "Θ(n)", "Case 3", "a=1, b=2, f(n)=n. log_b(a) = 0, n^0 = 1. f(n)=n 大於 1。正則條件 1*(n/2) <= 0.5*n。為 Case 3，T(n) = Θ(n)。QuickSelect 平均情況。"),
        ("T(n) = 3T(n/3) + n", "Θ(n log n)", "Case 2", "a=3, b=3, f(n)=n. log_b(a) = log_3(3) = 1, n^1 = f(n)。為 Case 2，T(n) = Θ(n log n)。"),
        ("T(n) = 7T(n/2) + n²", "Θ(n^(log₂7))", "Case 1", "a=7, b=2, f(n)=n². log_2(7) ≈ 2.807 > 2。n^2.807 大於 n²。為 Case 1，T(n) = Θ(n^log₂7) ≈ Θ(n^2.81)。Strassen 矩陣乘法。"),
        ("T(n) = 2T(n/4) + √n", "Θ(√n log n)", "Case 2", "a=2, b=4, f(n)=√n. log_4(2) = 0.5, n^0.5 = f(n)。為 Case 2，T(n) = Θ(√n log n)。"),
        ("T(n) = 2T(n/4) + 1", "Θ(√n)", "Case 1", "a=2, b=4, f(n)=1. log_4(2) = 0.5, n^0.5 大於 1。為 Case 1，T(n) = Θ(√n)。"),
        ("T(n) = 9T(n/3) + n", "Θ(n²)", "Case 1", "a=9, b=3, f(n)=n. log_3(9) = 2, n^2 大於 n。為 Case 1，T(n) = Θ(n²)。"),
        ("T(n) = 9T(n/3) + n²", "Θ(n² log n)", "Case 2", "a=9, b=3, f(n)=n². log_3(9) = 2, n^2 = f(n)。為 Case 2，T(n) = Θ(n² log n)。"),
        ("T(n) = 9T(n/3) + n³", "Θ(n³)", "Case 3", "a=9, b=3, f(n)=n³. log_3(9) = 2, n^3 大於 n²。正則條件成立。為 Case 3，T(n) = Θ(n³)。"),
        ("T(n) = 8T(n/4) + n²", "Θ(n²)", "Case 3", "a=8, b=4, f(n)=n². log_4(8) = 1.5, n^1.5 小於 n²。正則條件 8*(n/4)² = n²/2 <= 0.5 n²。為 Case 3，T(n) = Θ(n²)。"),
        ("T(n) = 3T(n/2) + n", "Θ(n^(log₂3))", "Case 1", "a=3, b=2, f(n)=n. log_2(3) ≈ 1.585 > 1。n^1.585 大於 n。為 Case 1，T(n) = Θ(n^log₂3)。Karatsuba 大整數乘法。"),
        ("T(n) = 2T(n/2) + n log n", "Θ(n log² n)", "Extended Case 2", "a=2, b=2, f(n)=n log n. log_2(2) = 1, f(n) = Θ(n log^k n) 其中 k=1。故 T(n) = Θ(n log^(k+1) n) = Θ(n log² n)。"),
        ("T(n) = 2T(n/2) + n / log n", "Θ(n log log n)", "Extended Case 2", "f(n) = n / log n = n log^(-1) n。代入主定理擴充情況，積分後得到 T(n) = Θ(n log log n)。"),
        ("T(n) = T(n-1) + 1", "Θ(n)", "線性遞迴", "展開法：T(n) = T(n-1)+1 = T(n-2)+2 = ... = T(1) + (n-1) = Θ(n)。線性搜尋走訪。"),
        ("T(n) = T(n-1) + n", "Θ(n²)", "階差遞迴", "展開法：T(n) = T(1) + 2 + 3 + ... + n = n(n+1)/2 = Θ(n²)。插入排序最差情況。"),
        ("T(n) = T(n-1) + log n", "Θ(n log n)", "對數累加", "展開法：T(n) = ∑_{i=1}^n log i = log(n!) = Θ(n log n)（依 Stirling 公式）。堆積插入 n 次之最差時間。"),
        ("T(n) = 2T(n-1) + 1", "Θ(2ⁿ)", "指數遞迴", "展開法：T(n) = 2(2T(n-2)+1)+1 = 2^(n-1) T(1) + 2^(n-1)-1 = 2^n - 1 = Θ(2ⁿ)。河內塔（Tower of Hanoi）遞迴。"),
        ("T(n) = T(√n) + 1", "Θ(log log n)", "變數變換法", "令 n = 2^m，m = log n。S(m) = T(2^m) = T(2^(m/2)) + 1 = S(m/2) + 1。S(m) = O(log m) = O(log log n)。"),
        ("T(n) = 2T(√n) + log n", "Θ(log n log log n)", "變數變換法", "令 n = 2^m，S(m) = 2S(m/2) + m。由主定理 Case 2 得 S(m) = Θ(m log m) = Θ(log n log log n)。"),
        ("T(n) = T(n/3) + T(2n/3) + n", "Θ(n log n)", "遞迴樹法", "每層總工作量皆為 n。最淺葉節點深度 log_3 n，最深葉節點深度 log_{3/2} n。兩者皆為 O(log n)，故總複雜度為 Θ(n log n)。"),
        ("T(n) = T(n-1) + n²", "Θ(n³)", "平方和遞迴", "展開法：∑_{i=1}^n i² = n(n+1)(2n+1)/6 = Θ(n³)。"),
        ("T(n) = 16T(n/4) + n²", "Θ(n² log n)", "Case 2", "a=16, b=4, f(n)=n². log_4(16) = 2, n^2 = f(n)。為 Case 2，T(n) = Θ(n² log n)。"),
        ("T(n) = 16T(n/4) + n", "Θ(n²)", "Case 1", "a=16, b=4, f(n)=n. log_4(16) = 2, n^2 大於 n。為 Case 1，T(n) = Θ(n²)。"),
        ("T(n) = 16T(n/4) + n³", "Θ(n³)", "Case 3", "a=16, b=4, f(n)=n³. log_4(16) = 2, n^3 大於 n²。正則條件成立。為 Case 3，T(n) = Θ(n³)。"),
        ("T(n) = 3T(n/4) + n log n", "Θ(n log n)", "Case 3", "a=3, b=4, log_4(3) ≈ 0.793. f(n)=n log n 大於 n^0.793。正則條件 3*(n/4) log(n/4) <= (3/4) n log n 成立。為 Case 3，T(n) = Θ(n log n)。"),
        ("T(n) = 2T(n/2) + n/2", "Θ(n log n)", "Case 2", "a=2, b=2, f(n)=0.5n. log_2(2) = 1, n^1 同階於 0.5n。為 Case 2，T(n) = Θ(n log n)。"),
        ("T(n) = 8T(n/2) + n³", "Θ(n³ log n)", "Case 2", "a=8, b=2, f(n)=n³. log_2(8) = 3, n^3 = f(n)。為 Case 2，T(n) = Θ(n³ log n)。"),
        ("T(n) = 5T(n/5) + n", "Θ(n log n)", "Case 2", "a=5, b=5, f(n)=n. log_5(5) = 1, n^1 = f(n)。為 Case 2，T(n) = Θ(n log n)。"),
        ("T(n) = 4T(n/4) + √n", "Θ(n)", "Case 1", "a=4, b=4, f(n)=√n. log_4(4) = 1, n^1 大於 n^0.5。為 Case 1，T(n) = Θ(n)。"),
        ("T(n) = 3T(n/3) + 1", "Θ(n)", "Case 1", "a=3, b=3, f(n)=1. log_3(3) = 1, n^1 大於 1。為 Case 1，T(n) = Θ(n)。"),
        ("T(n) = T(n/3) + n", "Θ(n)", "Case 3", "a=1, b=3, f(n)=n. log_3(1) = 0, n^0 = 1. f(n) 大於 1。為 Case 3，T(n) = Θ(n)。"),
        ("T(n) = 6T(n/6) + n log n", "Θ(n log² n)", "Extended Case 2", "a=6, b=6, f(n)=n log n. log_6(6)=1. 適用 Case 2 擴充形式，T(n) = Θ(n log² n)。"),
        ("T(n) = 2T(n/4) + n", "Θ(n)", "Case 3", "a=2, b=4, f(n)=n. log_4(2)=0.5, n^0.5 < n。正則條件成立，為 Case 3，T(n) = Θ(n)。"),
        ("T(n) = T(n/2) + log n", "Θ(log² n)", "變數替換/展開", "展開法：log n + log(n/2) + log(n/4) + ... = log n + (log n - 1) + ... = Θ(log² n)。")
    ]

    for rec, ans_str, case_type, expl in recurrence_data:
        opts = [ans_str, "Θ(n)", "Θ(n²)", "Θ(n log n)"]
        if ans_str in opts[1:]:
            opts[opts.index(ans_str)] = "Θ(n³)" if ans_str != "Θ(n³)" else "Θ(log n)"
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "主定理與遞迴推導",
            "stem": f"在演算法時間複雜度分析中，試求遞迴關係式 {rec}（其中初值 T(1) = 1）之漸進時間複雜度為下列何者？",
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_str}",
            "explanation": f"""<strong>【遞迴關係式逐步計算推導】</strong><br>
<div class="step-box">
  <div class="step-title">📝 漸進複雜度分析：{rec}</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>確立分析模型與參數</strong><br>
      評估方法：{case_type}。<br>
      展開或代入標準式 <code>T(n) = a T(n/b) + f(n)</code>。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>臨界函數成長率嚴格比對</strong><br>
      {expl}
    </li>
    <li class="step-item"><span class="step-badge check">步驟 3</span><strong>得出漸進緊密界限（Tight Bound）</strong><br>
      最終時間複雜度收斂為 <strong>{ans_str}</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) {ans_str}</strong>：依主定理或展開法之嚴謹數學推導完全正確。<br>
‧ <strong>(B)</strong>：複雜度估算不足，忽略遞迴樹分支累積效應或非遞迴項主導。<br>
‧ <strong>(C)</strong>：過度放大漸進階數，誤判多項式次方。<br>
‧ <strong>(D)</strong>：計算錯誤或未檢驗正則收斂條件。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Master Theorem</code> <span class="en">Master Theorem</span>：主定理。<br>
‧ <code>Recurrence Relation</code> <span class="en">Recurrence Relation</span>：遞迴關係式。<br>
‧ <code>Asymptotic Complexity</code> <span class="en">Asymptotic Complexity</span>：漸進複雜度。"""
        })

    # -------------------------------------------------------------
    # 2. 陣列位址與矩陣壓縮計算 (35 題)
    # -------------------------------------------------------------
    array_configs = [
        # (name, R_low, R_high, C_low, C_high, elem_sz, base_addr, target_r, target_c)
        ("A", 1, 10, 1, 20, 4, 1000, 5, 8),
        ("B", 0, 9, 0, 19, 2, 2000, 4, 15),
        ("C", -2, 5, 3, 8, 8, 500, 2, 6),
        ("D", 1, 15, 1, 30, 4, 4000, 10, 20),
        ("E", 0, 12, 0, 8, 1, 300, 7, 5),
        ("F", 5, 15, 10, 25, 4, 1200, 8, 18),
        ("G", -5, 5, -3, 3, 2, 800, 0, 1),
        ("H", 1, 8, 1, 12, 8, 1500, 6, 9),
        ("K", 0, 20, 0, 30, 4, 5000, 12, 14),
        ("M", 2, 10, 4, 16, 2, 600, 7, 11),
        ("P", 1, 50, 1, 10, 4, 10000, 25, 6),
        ("Q", -4, 4, 0, 10, 8, 2500, 1, 7)
    ]

    for arr_name, r1, r2, c1, c2, sz, base, tr, tc in array_configs:
        rows = r2 - r1 + 1
        cols = c2 - c1 + 1
        
        # Row-major
        offset_rm = ((tr - r1) * cols + (tc - c1)) * sz
        addr_rm = base + offset_rm
        step_rm = f"列優先公式：Loc = Base + [({tr} - {r1}) * {cols} + ({tc} - {c1})] * {sz} = {base} + [{tr - r1} * {cols} + {tc - c1}] * {sz} = {base} + {offset_rm} = {addr_rm}"
        
        opts_rm = [str(addr_rm), str(addr_rm + sz*2), str(addr_rm - sz*cols), str(addr_rm + sz*cols)]
        choices_rm = [("A", opts_rm[0]), ("B", opts_rm[1]), ("C", opts_rm[2]), ("D", opts_rm[3])]
        qs.append({
            "tag": "陣列位址推導",
            "stem": f"已知二維陣列 {arr_name}[{r1}..{r2}, {c1}..{c2}] 之起始基底位址 Loc({arr_name}[{r1},{c1}]) = {base}，每個元素占用 {sz} 位元組。若在記憶體中採<strong>以列為主（Row-Major）</strong>儲存，則元素 {arr_name}[{tr},{tc}] 的記憶體位址為？",
            "choices": choices_rm,
            "ans": "A",
            "ans_text": f"(A) {addr_rm}",
            "explanation": f"""<strong>【以列為主（Row-Major）陣列位址逐步推導】</strong><br>
<div class="step-box">
  <div class="step-title">📝 位址映射計算步驟</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>確認陣列邊界與行數長度</strong><br>
      ‧ 第 1 維（列索引範圍）：[{r1} .. {r2}]，總列數 R = {rows}。<br>
      ‧ 第 2 維（行索引範圍）：[{c1} .. {c2}]，總行數 C = {cols}。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>套用列優先位移公式</strong><br>
      ‧ {step_rm}。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 3</span><strong>得出最終記憶體位址</strong><br>
      ‧ 計算結果為 <strong>{addr_rm}</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) {addr_rm}</strong>：完全精準。<br>
‧ <strong>(B)</strong>：元素偏移計算多算 2 個元素。<br>
‧ <strong>(C)</strong>：少算一整列的元素寬度。<br>
‧ <strong>(D)</strong>：誤把目標索引加乘一整列。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Row-Major Order</code> <span class="en">Row-Major Order</span>：以列為主排列。<br>
‧ <code>Base Address</code> <span class="en">Base Address</span>：基底位址。"""
        })

        # Col-major
        offset_cm = ((tc - c1) * rows + (tr - r1)) * sz
        addr_cm = base + offset_cm
        step_cm = f"行優先公式：Loc = Base + [({tc} - {c1}) * {rows} + ({tr} - {r1})] * {sz} = {base} + [{tc - c1} * {rows} + {tr - r1}] * {sz} = {base} + {offset_cm} = {addr_cm}"
        
        opts_cm = [str(addr_cm), str(addr_cm + sz*rows), str(addr_cm - sz), str(addr_cm + sz)]
        choices_cm = [("A", opts_cm[0]), ("B", opts_cm[1]), ("C", opts_cm[2]), ("D", opts_cm[3])]
        qs.append({
            "tag": "陣列位址推導",
            "stem": f"已知二維陣列 {arr_name}[{r1}..{r2}, {c1}..{c2}] 之起始基底位址 Loc({arr_name}[{r1},{c1}]) = {base}，每個元素占用 {sz} 位元組。若在記憶體中採<strong>以行為主（Column-Major）</strong>儲存，則元素 {arr_name}[{tr},{tc}] 的記憶體位址為？",
            "choices": choices_cm,
            "ans": "A",
            "ans_text": f"(A) {addr_cm}",
            "explanation": f"""<strong>【以行為主（Column-Major）陣列位址逐步推導】</strong><br>
<div class="step-box">
  <div class="step-title">📝 位址映射計算步驟</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>確認陣列維度跨度</strong><br>
      ‧ 每一整行包含之列數 R = {rows}。<br>
      ‧ 目標元素前已經填滿之行數為 {tc} - {c1} = {tc - c1} 行。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>套用行優先位移公式</strong><br>
      ‧ {step_cm}。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 3</span><strong>得出最終記憶體位址</strong><br>
      ‧ 計算結果為 <strong>{addr_cm}</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) {addr_cm}</strong>：精確代入行主位址公式。<br>
‧ <strong>(B)</strong>：多跨越了一整行之記憶體邊界。<br>
‧ <strong>(C)</strong>：索引下標偏誤一格。<br>
‧ <strong>(D)</strong>：偏移量加減方向錯誤。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Column-Major Order</code> <span class="en">Column-Major Order</span>：以行為主排列。<br>
‧ <code>Offset Calculation</code> <span class="en">Offset Calculation</span>：偏移量計算。"""
        })

    # Triangular matrix compression (11 questions)
    tri_configs = [
        ("對稱矩陣（Symmetric Matrix）A[1..n, 1..n]", "n(n+1)/2", ["n(n+1)/2", "n²", "n(n-1)/2", "n(n+1)"], "只儲存下三角或上三角元素，元素總數為 1 + 2 + ... + n = n(n+1)/2。"),
        ("下三角矩陣（Lower Triangular Matrix）A[1..n, 1..n] 採列主存入一維陣列 B[1..k]，A[i, j]（其中 i >= j）對應之一維索引為？", "i(i-1)/2 + j", ["i(i-1)/2 + j", "i(i+1)/2 + j", "(i-1)n + j", "j(j-1)/2 + i"], "前 i-1 列之元素總數為 1 + 2 + ... + (i-1) = i(i-1)/2。第 i 列中 A[i, j] 為第 j 個元素，故對應索引為 i(i-1)/2 + j。"),
        ("上三角矩陣（Upper Triangular Matrix）A[1..n, 1..n] 採列主存入一維陣列 B[1..k]，A[i, j]（其中 i <= j）對應之一維索引為？", "(i-1)n - (i-1)(i-2)/2 + (j - i + 1)", ["(i-1)n - (i-1)(i-2)/2 + (j - i + 1)", "i(i-1)/2 + j", "(i-1)n + j", "j(j+1)/2 + i"], "前 i-1 列每列分別有 n, n-1, ..., n-i+2 個元素，加總為 (i-1)n - (i-1)(i-2)/2，再加上該列偏移 (j - i + 1)。"),
        ("三對角矩陣（Tridiagonal Matrix）A[1..n, 1..n] 中非零元素僅出現在 |i - j| <= 1 之位置，其非零元素總數為？", "3n - 2", ["3n - 2", "3n", "3n - 1", "3n - 3"], "主對角線有 n 個元素，主對角線上下一條副對角線各擁有 n-1 個元素。總數 = n + (n-1) + (n-1) = 3n - 2。"),
        ("三對角矩陣 A[1..n, 1..n] 壓縮至一維陣列 B[1..3n-2]，元素 A[i, j]（|i-j|<=1）若依列主儲存，其索引為？", "2i + j - 2", ["2i + j - 2", "3i + j - 3", "2i + j - 1", "3i - j"], "第 1 列有 2 個元素，第 2 到 i-1 列各有 3 個元素（共 3(i-2) 個）。在第 i 列中，起始元素為 A[i, i-1]（對應偏移量）。加總推導：2 + 3(i-2) + (j - i + 2) = 3i - 4 + j - i + 2 = 2i + j - 2。"),
        ("帶狀矩陣（Band Matrix）頻寬為 w（半頻寬 k = (w-1)/2），非零元素總數上限約為？", "n·w", ["n·w", "n²", "w²", "n·w / 2"], "每一列最多包含 w 個非零元素，共 n 列，故空間複雜度上限為 O(n·w)。"),
        ("以十字鏈結串列（Orthogonal Linked List）表示稀疏矩陣（Sparse Matrix），每個非零節點需要幾個指標（Pointers）？", "2 個（right 與 down）", ["2 個（right 與 down）", "1 個", "3 個", "4 個"], "十字鏈結串列中每個節點記錄 row, col, value，以及向右（同一列的下一個非零元素 right 指標）與向下（同一行的下一個非零元素 down 指標），共 2 個指標。"),
        ("稀疏矩陣三元組（Triplet）表示法中，第一列（標頭 Header）通常記錄何種資訊？", "矩陣的總列數、總行數與非零元素總個數", ["矩陣的總列數、總行數與非零元素總個數", "第一列第一個非零元素的數值與座標", "矩陣的反矩陣維度", "稀疏度百分比"], "三元組陣列第 0 列儲存元資料（Metadata）：Rows, Cols, Non-Zero Terms。"),
        ("下三角矩陣 A[1..10, 1..10] 採列主存入一維陣列 B[1..55]，元素 A[6, 4] 位於陣列 B 的哪一個索引位置？", "19", ["19", "20", "18", "21"], "前 5 列元素總數 = 5 * 6 / 2 = 15。在第 6 列中，A[6, 4] 為第 4 個元素。故索引 = 15 + 4 = 19。"),
        ("下三角矩陣 A[1..20, 1..20] 採列主存入一維陣列 B[1..210]，元素 A[10, 7] 位於陣列 B 的哪一個索引位置？", "52", ["52", "53", "51", "50"], "前 9 列元素總數 = 9 * 10 / 2 = 45。在第 10 列中，A[10, 7] 為第 7 個元素。故索引 = 45 + 7 = 52。"),
        ("對稱矩陣 A[1..8, 1..8] 僅存下三角於一維陣列，元素 A[7, 3] 位於一維陣列（1-indexed）第幾格？", "24", ["24", "25", "23", "22"], "前 6 列元素總數 = 6 * 7 / 2 = 21。在第 7 列中偏移為 3。故位置 = 21 + 3 = 24。")
    ]

    for stem, ans_s, opts, expl in tri_configs:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "特殊矩陣壓縮推導",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【矩陣壓縮儲存與位址對應推導】</strong><br>
<div class="step-box">
  <div class="step-title">📝 數學公式推導過程</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>分析特殊矩陣之對稱/零元素分佈</strong><br>
      ‧ 本題結構：特殊壓縮儲存模型。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>計算累積元素個數</strong><br>
      ‧ {expl}
    </li>
    <li class="step-item"><span class="step-badge check">步驟 3</span><strong>確立對應結果</strong><br>
      ‧ 答案為 <strong>{ans_s}</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) {ans_s}</strong>：完全符合推導。<br>
‧ 其餘選項皆為累積等差級數公式套錯或邊界 1-indexed / 0-indexed 混淆之常見錯誤。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Triangular Matrix</code> <span class="en">Triangular Matrix</span>：三角矩陣。<br>
‧ <code>Tridiagonal Matrix</code> <span class="en">Tridiagonal Matrix</span>：三對角矩陣。<br>
‧ <code>Sparse Matrix</code> <span class="en">Sparse Matrix</span>：稀疏矩陣。"""
        })

    # -------------------------------------------------------------
    # 3. 鏈結串列與跳躍串列 (30 題)
    # -------------------------------------------------------------
    ll_data = [
        ("在單向鏈結串列（Singly Linked List）中，若欲在指標 p 所指節點後方插入指標 new_node 所指之新節點，正確的操作順序為？",
         "new_node->next = p->next; p->next = new_node;",
         ["new_node->next = p->next; p->next = new_node;", "p->next = new_node; new_node->next = p->next;", "new_node->next = p; p->next = new_node;", "p->next = new_node->next; new_node->next = p;"],
         "必須先讓 new_node->next 指向 p 原本的後繼節點，再讓 p->next 指向 new_node。若順序顛倒（先 p->next = new_node），原本後方的所有節點鏈結將完全遺失，造成嚴重的記憶體洩漏（Memory Leak）。"),
        ("在雙向鏈結串列（Doubly Linked List）中，若欲刪除節點 p，正確的指標更新指令為？",
         "p->prev->next = p->next; p->next->prev = p->prev; free(p);",
         ["p->prev->next = p->next; p->next->prev = p->prev; free(p);", "p->next = p->prev; free(p);", "p->prev = p->next; free(p);", "p->next->prev = p->prev->next; free(p);"],
         "令 p 的前驅節點的 next 指向 p 的後繼節點，令 p 的後繼節點的 prev 指向 p 的前驅節點，最後釋放 p 的記憶體。"),
        ("使用快慢指標（Floyd's Tortoise and Hare Algorithm）判斷單向鏈結串列是否存在環（Cycle），快指標每次移動 2 步，慢指標每次移動 1 步。若串列有長度為 C 的環，兩指標相遇時的時間複雜度為？",
         "O(n)",
         ["O(n)", "O(n²)", "O(log n)", "O(1)"],
         "慢指標進入環後，快慢指標每走一步相對距離縮短 1 格。最慢在慢指標繞環一圈內快指標必定追上慢指標，故總移動步數為 O(n)，時間複雜度為線性時間 O(n)。"),
        ("在一個僅維護尾指標（rear）的環狀單向鏈結串列（Circular Singly Linked List）中，欲在「串列開頭」插入節點與「串列末尾」插入節點的時間複雜度分別為？",
         "開頭插入 O(1)，末尾插入 O(1)",
         ["開頭插入 O(1)，末尾插入 O(1)", "開頭插入 O(1)，末尾插入 O(n)", "開頭插入 O(n)，末尾插入 O(1)", "開頭插入 O(n)，末尾插入 O(n)"],
         "rear->next 即為頭節點（front）。在開頭插入：new_node->next = rear->next; rear->next = new_node（O(1)）；在末尾插入：同前兩步，最後多一步 rear = new_node（O(1)）。兩者皆為 O(1)。"),
        ("反轉一個長度為 n 的單向鏈結串列（In-place Reverse），最少需要額外宣告幾個輔助指標變數？",
         "3 個（prev, curr, next）",
         ["3 個（prev, curr, next）", "1 個", "n 個", "0 個"],
         "標準迭代反轉演算法需要 prev（前驅）、curr（當前）、next（暫存後繼以防斷鏈）三個指標，空間複雜度為 O(1)。"),
        ("跳躍串列（Skip List）若節點晉升至上一層的機率 p = 1/2，則包含 n 個元素的跳躍串列之平均搜尋時間複雜度與空間複雜度分別為？",
         "時間 O(log n)，空間 O(n)",
         ["時間 O(log n)，空間 O(n)", "時間 O(n)，空間 O(n)", "時間 O(log n)，空間 O(n log n)", "時間 O(1)，空間 O(n)"],
         "每一層元素數量期望值減半，總層數期望值為 log_{1/p} n = O(log n)。各節點指標數期望值為 ∑ (1/2)^i = 2，故總空間為 2n = O(n)，兼具平衡二元樹的 O(log n) 效率與實作簡潔性。"),
        ("跳躍串列（Skip List）在最差情況（Worst Case）下的搜尋時間複雜度為何？",
         "O(n)",
         ["O(n)", "O(log n)", "O(n log n)", "O(1)"],
         "若隨機投擲硬幣極端不幸所有節點皆未晉升至高層（只有底層單向串列），搜尋退化為線性走訪 O(n)。"),
        ("若一個單向鏈結串列中每個節點包含資料欄位 data 與指標欄位 next，若欲在 O(1) 時間內刪除指標 p 所指節點（假設 p 不是最後一個節點，且無給定頭指標），該如何達成？",
         "將 p->next 的資料複製到 p，再將 p->next 節點刪除",
         ["將 p->next 的資料複製到 p，再將 p->next 節點刪除", "直接 free(p)", "令 p->next = NULL", "無法在 O(1) 完成，必須從頭尋找 p 的前驅節點"],
         "經典妙解：複製下一節點之內容覆蓋當前節點（p->data = p->next->data），然後越過下一節點（temp = p->next; p->next = temp->next; free(temp)），即可在 O(1) 達成刪除。"),
        ("尋找單向鏈結串列倒數第 k 個節點（k-th to last node），最佳演算法只需走訪串列一次，應採用何種技巧？",
         "快慢雙指標法（Two Pointers），快指標先走 k 步",
         ["快慢雙指標法（Two Pointers），快指標先走 k 步", "先走訪計算總長度 n 再走訪 n-k 步", "將串列元素全部放入陣列", "遞迴反轉串列"],
         "讓快指標 fast 先走 k 步，接著快慢指標每次同步各走 1 步。當 fast 到達結尾 NULL 時，慢指標 slow 恰好停在倒數第 k 個節點，只需單趟走訪 O(n)，輔助空間 O(1)。"),
        ("在異或鏈結串列（XOR Linked List / Memory Efficient Doubly Linked List）中，每個節點的單一指標欄位儲存何種數值？",
         "前驅節點位址 ⊕ 後繼節點位址（位元互斥或 XOR）",
         ["前驅節點位址 ⊕ 後繼節點位址（位元互斥或 XOR）", "前驅節點位址 + 後繼節點位址", "後繼節點位址的補數", "前驅節點位址 & 後繼節點位址"],
         "XOR 鏈結串列每個節點只用一個 pointer_diff = prev ⊕ next。走訪時已知當前與前驅，即可由 curr->diff ⊕ prev 算出 next 位址，節省一半指標記憶體空間。")
    ]

    for item in ll_data:
        stem, ans_s, opts, expl = item
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "鏈結串列指標推導",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【鏈結串列結構與指標推導】</strong><br>
<div class="step-box">
  <div class="step-title">📝 指標操作與複雜度證明</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>分析指標指向與記憶體拓樸</strong><br>
      ‧ 本題檢驗指標操作順序與鏈結邊界安全。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>執行逐步演算</strong><br>
      ‧ {expl}
    </li>
    <li class="step-item"><span class="step-badge check">步驟 3</span><strong>確立正確操作</strong><br>
      ‧ 正確解為 <strong>{ans_s}</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) {ans_s}</strong>：邏輯嚴密，指標更新符合資料結構定義。<br>
‧ 其餘選項存在指標斷鏈（Dangling Pointer）、記憶體洩漏（Memory Leak）或複雜度非最佳之缺失。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Singly Linked List</code> <span class="en">Singly Linked List</span>：單向鏈結串列。<br>
‧ <code>Doubly Linked List</code> <span class="en">Doubly Linked List</span>：雙向鏈結串列。<br>
‧ <code>Skip List</code> <span class="en">Skip List</span>：跳躍串列。"""
        })

    # Expand LL questions to 30 with parameterized pointer scenarios
    more_ll = [
        ("長度為 n 的環狀單向串列中，從任一已知節點 p 出發走訪完整個串列需多少時間？", "O(n)", ["O(n)", "O(1)", "O(n²)", "O(log n)"], "走訪所有 n 個節點直至指針再度等於 p，循環 n 次，時間複雜度為 O(n)。"),
        ("靜態鏈結串列（Static Linked List）是利用何種基礎資料結構來模擬指標串列？", "一維陣列與游標（Cursor）", ["一維陣列與游標（Cursor）", "動態記憶體堆積（Heap）", "堆疊（Stack）", "樹（Tree）"], "在沒有指針語法的語言中，使用結構陣列配合 cursor（下一個元素的陣列下標）來模擬鏈結串列。"),
        ("合併兩個長度分別為 m 與 n 的已排序單向鏈結串列，最佳時間複雜度為？", "O(m + n)", ["O(m + n)", "O(m * n)", "O(max(m, n))", "O(log(m + n))"], "每次比對兩串列首節點，將較小者串接於新串列尾端，總比對次數至多 m+n-1 次，時間複雜度為 O(m+n)。"),
        ("在單向鏈結串列的末端插入一個節點，若只有頭指標（head），時間複雜度為？", "O(n)", ["O(n)", "O(1)", "O(log n)", "O(n²)"], "必須從頭走訪 n 個節點找到尾端節點，故為 O(n)。"),
        ("在單向鏈結串列中，若維護頭指標（head）與尾指標（tail），執行刪除最後一個節點的時間複雜度為？", "O(n)", ["O(n)", "O(1)", "O(log n)", "O(n²)"], "刪除尾節點需要將 tail 移至其前驅節點，但單向鏈結無法逆向回溯，必須自 head 重新走訪至倒數第二節點，故為 O(n)。"),
        ("雙向鏈結串列中刪除尾節點（已知 tail 指標），時間複雜度為？", "O(1)", ["O(1)", "O(n)", "O(log n)", "O(n²)"], "可透過 tail->prev 直接存取倒數第二個節點並更新指標，耗時 O(1)。"),
        ("若一個串列頻繁在「中間位置」進行插入與刪除，且已知目標節點之指標，下列何者效率最高？", "雙向鏈結串列", ["雙向鏈結串列", "動態陣列（Dynamic Array）", "靜態陣列", "環狀陣列"], "陣列在中間增刪需搬移大量元素 O(n)；雙向鏈結串列在已知指標下只需常數次指針重新指派 O(1)。"),
        ("在單向鏈結串列中實作佇列（Queue），應如何設定指標以使 enqueue 與 dequeue 皆為 O(1)？", "鏈結串列尾端入隊（enqueue），前端出隊（dequeue），維護 head 與 tail", ["鏈結串列尾端入隊（enqueue），前端出隊（dequeue），維護 head 與 tail", "前端入隊，尾端出隊", "兩端皆可自由入出", "必須使用環狀陣列"], "前端刪除出隊為 O(1)，尾端插入入隊為 O(1)；反之若前端入隊、尾端出隊，尾端刪除需找前驅耗時 O(n)。"),
        ("對於記憶體局部性（Locality of Reference），鏈結串列相較於循序陣列之表現通常為何？", "較差（空間局部性差，容易引發 Cache Miss）", ["較差（空間局部性差，容易引發 Cache Miss）", "較佳（快取命中率高）", "兩者完全相同", "視元素大小而定"], "陣列元素在記憶體中連續存放，具極高空間局部性；鏈結串列各節點分散於 Heap，每次跳躍存取極易造成 CPU 快取未命中。"),
        ("在一個未排序的長度為 n 之單向鏈結串列中搜尋特定值，平均需要比對幾次？", "(n + 1) / 2 次", ["(n + 1) / 2 次", "n 次", "log₂ n 次", "n / 4 次"], "成功搜尋平均比對次數為 ∑_{i=1}^n i / n = (n+1)/2 次。"),
        ("若欲判斷兩個無環單向鏈結串列是否相交（Intersect），最佳判定條件為？", "兩串列的最後一個節點是否相同（位址相等）", ["兩串列的最後一個節點是否相同（位址相等）", "兩串列長度是否相等", "兩串列的首節點是否相同", "兩串列的中間節點是否相同"], "若兩串列相交成 Y 字型，相交點後的所有節點共享，因此其最後一個節點必為同一個記憶體位址。"),
        ("在 Skip List 中，若每隔 4 個節點往上升一層（p = 1/4），則查詢一個元素之平均時間複雜度為？", "O(log₄ n) = O(log n)", ["O(log₄ n) = O(log n)", "O(4n)", "O(n / 4)", "O(n log n)"], "底數為 4 之對數階層，依大 O 漸進記號常數係數可省略，時間複雜度仍為 O(log n)。"),
        ("自我組織串列（Self-Organizing List）中，「移至前端（Move-To-Front, MTF）」啟發策略的平攤比對成本至多為最佳靜態離線排序的幾倍？", "2 倍", ["2 倍", "4 倍", "n 倍", "log n 倍"], "依 Sleator 與 Tarjan 著名之競爭分析（Competitive Analysis），MTF 演算法相對於最佳離線演算法為 2-競爭（2-competitive）。"),
        ("在循環鏈結串列中，若終止條件判斷錯誤，最容易發生下列何種執行期異常？", "無窮迴圈（Infinite Loop）", ["無窮迴圈（Infinite Loop）", "記憶體即時釋放", "堆疊溢位", "編譯階段語法錯誤"], "循環鏈結串列末節點指向頭節點，若走訪時未正確檢查 curr == head，走訪迴圈將永遠無法終止。"),
        ("帶有頭節點（Dummy Head / Sentinel Node）的鏈結串列，其最大優點為何？", "消除在串列首節點進行插入與刪除時的特例判斷邏輯", ["消除在串列首節點進行插入與刪除時的特例判斷邏輯", "大幅節省記憶體使用量", "將搜尋時間複雜度降為 O(1)", "防止指標溢位"], "啞節點（Sentinel）使得所有實際資料節點皆擁有前驅節點，插入與刪除演算法無需撰寫額外的 if (head == NULL) 分支。"),
        ("反轉單向鏈結串列之遞迴演算法，其呼叫堆疊（Call Stack）的空間複雜度為？", "O(n)", ["O(n)", "O(1)", "O(log n)", "O(n²)"], "遞迴深入至最後一個節點，堆疊深度達到 n 層，故額外需要 O(n) 的記憶體堆疊空間。"),
        ("在單向鏈結串列中尋找中間節點（Middle Node），快慢指標法當快指標到達末端時，慢指標恰在何處？", "串列中間節點", ["串列中間節點", "串列開頭", "串列結尾", "倒數第二節點"], "快指標速度為慢指標 2 倍，當快指標走完 2k 步（到達末端），慢指標恰走 k 步，精準停於中間節點。"),
        ("給定單向鏈結串列，欲在 O(n) 時間且 O(1) 輔助空間下判斷其是否為迴文（Palindrome），應採何種步驟？", "找到中點、反轉後半段、同步比對前半段與後半段", ["找到中點、反轉後半段、同步比對前半段與後半段", "使用堆疊將所有元素壓入再彈出比對", "複製整個串列並反轉", "兩層迴圈逐對比對"], "快慢指針找中點 O(n)；原地反轉後半部 O(n) 且 O(1) 空間；雙指針比對 O(n)。空間完全維持 O(1)。"),
        ("將兩個環狀單向鏈結串列合併為一個環狀串列，給定其各自尾指標 rear1 與 rear2，最快需時？", "O(1)", ["O(1)", "O(n)", "O(n + m)", "O(log n)"], "交換 rear1->next 與 rear2->next 的指向，即可在常數次指標操作內將兩環縫合為一，時間複雜度為 O(1)。"),
        ("在長度為 n 的陣列與長度為 n 的鏈結串列中分別執行隨機存取（Random Access，如取得第 k 個元素），其時間複雜度分別為？", "陣列 O(1)，鏈結串列 O(n)", ["陣列 O(1)，鏈結串列 O(n)", "陣列 O(n)，鏈結串列 O(1)", "兩者皆為 O(1)", "兩者皆為 O(n)"], "陣列可透過基底位址與下標偏移直接常數時間定址 O(1)；鏈結串列必須從頭循序走訪至第 k 步 O(n)。")
    ]

    for stem, ans_s, opts, expl in more_ll:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "鏈結串列進階觀念",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【鏈結串列演算法特性解析】</strong><br>
‧ <strong>(A) {ans_s}</strong>：依資料結構原理分析，{expl}<br>
‧ 其餘選項均存在複雜度分析偏差或操作邏輯錯誤。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Dummy Head Node</code> <span class="en">Dummy Head Node</span>：虛擬頭節點（啞節點）。<br>
‧ <code>Two Pointers Technique</code> <span class="en">Two Pointers</span>：雙指標技巧。"""
        })

    # -------------------------------------------------------------
    # 4. 堆疊、佇列與運算式轉換 (35 題)
    # -------------------------------------------------------------
    expr_items = [
        ("將中序運算式（Infix） A + B * C 轉換為後序運算式（Postfix），其結果為？", "A B C * +", ["A B C * +", "A B + C *", "+ A * B C", "A B C + *"], "運算子優先權：乘法 * 高於加法 +。B*C 先轉為 BC*，再與 A 相加，轉為 A BC* +。"),
        ("將中序運算式 (A + B) * (C - D) / E 轉換為後序運算式，其結果為？", "A B + C D - * E /", ["A B + C D - * E /", "A B C D + - * E /", "+ A B * - C D / E", "A B + * C D - E /"], "括號優先：(A+B)->AB+，(C-D)->CD-。兩者相乘->AB+ CD- *。最後除以 E->AB+ CD- * E /。"),
        ("將中序運算式 A * B + C / D 轉換為前序運算式（Prefix），其結果為？", "+ * A B / C D", ["+ * A B / C D", "* + A B / C D", "+ A * B / C D", "/ + * A B C D"], "A*B 轉為 *AB；C/D 轉為 /CD。兩者以 + 連接，轉為 + *AB /CD。"),
        ("計算後序運算式 5 3 2 + * 4 / 的數值結果為？", "6.25", ["6.25", "25", "4", "5"], "逐步求值：遇到 3, 2 及 +，計算 3+2=5；遇到 5, 5 及 *，計算 5*5=25；遇到 4 及 /，計算 25/4 = 6.25。"),
        ("計算後序運算式 12 4 / 3 * 2 + 的數值結果為？", "11", ["11", "18", "7", "14"], "逐步求值：12 4 / -> 12/4 = 3；3 3 * -> 3*3 = 9；9 2 + -> 9+2 = 11。"),
        ("計算後序運算式 6 2 3 + - 3 8 2 / + * 2 ^ 3 + 的運算過程中，堆疊（Stack）內最多同時存放幾個數值（最大深度）？", "4 個", ["4 個", "3 個", "5 個", "6 個"], "分析各階段連續 push 之運算元數量，最深出現在 [3, 8, 2] 連同前運算暫存值時，堆疊最多同時累積 4 個運算元。"),
        ("將中序運算式 A + B * C ^ D - E 轉換為後序運算式，已知次方 ^ 優先權最高且具「右結合性（Right-Associative）」，結果為？", "A B C D ^ * + E -", ["A B C D ^ * + E -", "A B + C D ^ * E -", "A B C * D ^ + E -", "A B C D * ^ + E -"], "優先權順序：C^D -> CD^；B*(CD^) -> B CD^ *；A + (B CD^ *) -> A B CD^ * +；最後減 E -> A B CD^ * + E -。"),
        ("容量為 M 的環狀佇列（Circular Queue），以陣列索引 0 到 M-1 實作，維護 front 與 rear 指標。若採取「保留一個空位」區分空與滿，則「佇列已滿（Queue Full）」的判別條件為？", "(rear + 1) % M == front", ["(rear + 1) % M == front", "rear == front", "(front + 1) % M == rear", "rear == M - 1"], "當 front == rear 時定義為佇列全空。為了防止佇列全滿時 rear 也追上 front 造成無法區分，規定當 rear 的下一個位置剛好等於 front 時即視為已滿。"),
        ("容量為 M 的環狀佇列，若 front 指向隊頭元素的前一格，rear 指向隊尾元素。當前佇列中實際容納的元素個數計算公式為？", "(rear - front + M) % M", ["(rear - front + M) % M", "rear - front", "(rear - front + 1) % M", "(front - rear + M) % M"], "考慮環狀繞回（Wrap-around），加上 M 後取模 (rear - front + M) % M 可精確求出兩指標間之元素總數。"),
        ("給定包含 4 個相異元素的輸入序列，依序進入一個堆疊，在任意時刻可進行 push 或 pop。總共可產生多少種相異的合法輸出序列？", "14 種", ["14 種", "24 種", "16 種", "12 種"], "出棧合法序列數量由卡特蘭數（Catalan Number）決定：C₄ = (1/(4+1)) * (8! / (4! * 4!)) = (1/5) * 70 = 14 種。")
    ]

    for stem, ans_s, opts, expl in expr_items:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "堆疊運算式轉換推導",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【運算式轉換與堆疊求值推導】</strong><br>
<div class="step-box">
  <div class="step-title">📝 步進求值推導步驟</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>運算子優先權與結合性解析</strong><br>
      ‧ 括號 > 次方（右結合） > 乘除（左結合） > 加減（左結合）。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>執行堆疊轉換/求值展開</strong><br>
      ‧ {expl}
    </li>
    <li class="step-item"><span class="step-badge check">步驟 3</span><strong>得出最終運算結果</strong><br>
      ‧ 正確解為 <strong>{ans_s}</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) {ans_s}</strong>：符號優先權與結合性推演精確。<br>
‧ 其餘選項常為加減乘除優先順序錯置、或由左至右括號配對失誤。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Infix Expression</code> <span class="en">Infix Expression</span>：中序運算式。<br>
‧ <code>Postfix Expression (RPN)</code> <span class="en">Postfix Expression</span>：後序運算式（逆波蘭表示法）。<br>
‧ <code>Circular Queue</code> <span class="en">Circular Queue</span>：環狀佇列。"""
        })

    # More Stack/Queue (25 questions)
    more_sq = [
        ("使用兩個堆疊（Stack 1 與 Stack 2）實作一個先進先出佇列（Queue），入隊 push 入 Stack 1，出隊從 Stack 2 pop（若空則將 Stack 1 元素全部倒入）。此設計中每個元素出入隊的平攤時間複雜度（Amortized Time）為？", "O(1)", ["O(1)", "O(n)", "O(log n)", "O(n²)" ], "每個元素一生僅歷經：push 入 S1(1)、pop 出 S1(1)、push 入 S2(1)、pop 出 S2(1)，共 4 次常數操作。均攤成本為 O(1)。"),
        ("使用兩個佇列（Queue 1 與 Queue 2）實作一個後進先出堆疊（Stack），若要求 pop 操作為 O(1)，則 push 操作的時間複雜度為？", "O(n)", ["O(n)", "O(1)", "O(log n)", "O(n²)"], "push 新元素入 Q2，將 Q1 所有元素依次 dequeue 並 enqueue 入 Q2，最後交換 Q1 與 Q2 指標，push 耗時 O(n)，使 Q1 隊頭常保最新元素。"),
        ("在括號對稱性檢查演算法中（包含 ()、[]、{}），當掃描到左括號時應執行何種操作？", "將左括號壓入堆疊（push）", ["將左括號壓入堆疊（push）", "將左括號彈出堆疊（pop）", "將左括號放入佇列", "忽視並繼續掃描"], "遇到開括號先 push 進堆疊暫存；遇到閉括號時檢視堆疊頂端是否為對應的開括號並 pop，若不符則對稱失敗。"),
        ("雙向佇列（Deque / Double-Ended Queue）具備下列何種功能特性？", "允許在前端與後端同時進行插入與刪除操作", ["允許在前端與後端同時進行插入與刪除操作", "只能在前端插入、後端刪除", "只能在一端插入、另一端刪除", "只能在中央插入"], "Deque（雙端佇列）支援 push_front, pop_front, push_back, pop_back，可在兩端常數時間 O(1) 操作。"),
        ("利用堆疊實作非遞迴走訪（如樹的深度優先搜尋 DFS），堆疊的主要功用為何？", "記錄回溯路徑（Backtracking）與待處理節點", ["記錄回溯路徑（Backtracking）與待處理節點", "將時間複雜度降為 O(1)", "保證寬度優先順序", "自動排序節點鍵值"], "堆疊保存尚未探索完畢的節點位址，以便在分支探索至底後能依後進先出順序正確回溯。"),
        ("若一環狀佇列容量大小為 8（索引 0..7），初始 front=3, rear=3。依序加入 4 個元素、移除 2 個元素、再加入 3 個元素後，此時 front 與 rear 的值分別為？", "front = 5, rear = 2", ["front = 5, rear = 2", "front = 5, rear = 1", "front = 3, rear = 2", "front = 1, rear = 5"], "初始 f=3, r=3。加4: r=(3+4)%8=7; 移2: f=(3+2)%8=5; 加3: r=(7+3)%8=2。故 f=5, r=2。"),
        ("若一環狀佇列大小為 10，front = 8, rear = 2，則目前佇列內共有幾個元素？", "4 個", ["4 個", "6 個", "5 個", "3 個"], "元素個數 = (rear - front + M) % M = (2 - 8 + 10) % 10 = 4 個（分別佔用索引 8, 9, 0, 1 中的元素）。"),
        ("下列哪一種問題「最不適合」使用堆疊（Stack）來解決？", "作業系統排程之先來先服務（FCFS / First-Come First-Served）", ["作業系統排程之先來先服務（FCFS / First-Come First-Served）", "函式遞迴呼叫時之區域變數與返回位址儲存", "編譯器之語法括號配對分析", "瀏覽器之上一頁（Back）歷史記錄追蹤"], "先來先服務要求先進先出（FIFO），必須使用佇列（Queue）；其餘三者皆為標準後進先出（LIFO）應用。"),
        ("優先佇列（Priority Queue）中，每次被 dequeue 取出的元素為？", "優先權最高（或數值最小/最大）的元素", ["優先權最高（或數值最小/最大）的元素", "最早進入佇列的元素", "最晚進入佇列的元素", "位於中央位置的元素"], "優先佇列不再遵循先進先出，而是依據元素的優先權權重（Priority）決定出隊順序。"),
        ("堆疊溢位（Stack Overflow）最常見於下列何種程式設計失誤？", "無窮遞迴呼叫（Infinite Recursion，缺少終止條件）", ["無窮遞迴呼叫（Infinite Recursion，缺少終止條件）", "動態記憶體配置過多", "陣列索引未由 0 開始", "迴圈變數未宣告為全域變數"], "每次函式呼叫均需在 Call Stack 建立 Stack Frame，無窮遞迴會迅速耗盡呼叫堆疊空間導致 Stack Overflow Crash。"),
        ("單調堆疊（Monotonic Stack）最常用於在 O(n) 時間內解決下列何種經典問題？", "尋找陣列中每個元素左側或右側「第一個大於/小於該元素」的值（Next Greater Element）", ["尋找陣列中每個元素左側或右側「第一個大於/小於該元素」的值（Next Greater Element）", "快速排序中的數值分割", "求兩點間最短路徑", "字串雜湊值計算"], "維持堆疊內部元素單調遞增或遞減，每個元素僅出入棧一次，能以線性時間 O(n) 找出下一個更大或更小元素。"),
        ("單調佇列（Monotonic Queue）最常用於解決下列何種滑動視窗問題？", "滑動視窗最大值/最小值（Sliding Window Maximum）在 O(n) 時間內求得", ["滑動視窗最大值/最小值（Sliding Window Maximum）在 O(n) 時間內求得", "矩陣乘法優化", "拓樸排序", "平衡二元樹旋轉"], "雙端佇列維護視窗內候選最值，淘汰過期與次優元素，使視窗滑動時取得最值均攤為 O(1)，總時間 O(n)。"),
        ("對於一個空堆疊，若輸入元素為 1, 2, 3，則不可能產生的輸出排列為？", "3, 1, 2", ["3, 1, 2", "3, 2, 1", "1, 2, 3", "2, 1, 3"], "若 3 先出棧，表示 1, 2, 3 均已入棧，棧內剩餘 [1, 2]，下一位必須出棧 2，絕不可能越過 2 先出 1。"),
        ("已知輸入序列 A, B, C, D 依序進入堆疊，下列哪一個不是合法的出棧序列？", "C, A, B, D", ["C, A, B, D", "B, A, D, C", "D, C, B, A", "A, B, C, D"], "若 C 先出棧，堆疊內留有 A, B（A在底B在頂），此時若欲出棧下一位只能是 B，不可能越過 B 先輸出 A！故 C, A, B, D 不合法。"),
        ("廣度優先搜尋（BFS）演算法通常使用下列何種資料結構來管理待拜訪節點？", "佇列（Queue）", ["佇列（Queue）", "堆疊（Stack）", "優先堆積（Heap）", "跳躍串列（Skip List）"], "BFS 遵循由近及遠、一層一層往外擴展之原則，先進節點其相鄰頂點先被探索，標準 FIFO 佇列。"),
        ("將中序運算式 A + B 轉換為前序與後序，正確的表述分別為？", "前序 + A B，後序 A B +", ["前序 + A B，後序 A B +", "前序 A B +，後序 + A B", "前序 + A B，後序 + B A", "前序 A + B，後序 B + A"], "運算子置於運算元前即為前序（+ A B）；置於運算元後即為後序（A B +）。"),
        ("在後序運算式中，運算元與運算子的相對出現次序有何特性？", "絕不需要括號來指示運算優先順序", ["絕不需要括號來指示運算優先順序", "必須使用中括號輔助", "運算子一律出現在最前端", "次方運算必須具括號"], "後序表示法結構嚴謹無二義性，由位置順序直接界定優先權，完全免除括號需求。"),
        ("迷宮尋路演算法（Maze Problem）若採用回溯法（Backtracking），通常利用何種資料結構記錄探索路徑？", "堆疊（Stack）", ["堆疊（Stack）", "佇列（Queue）", "二元樹", "雜湊表"], "每向前一步將坐標與方向 push 入堆疊，遇死路時 pop 出堆疊以回溯至上一個路口。"),
        ("佇列的「假溢位（False Overflow）」是指何種現象？", "循序陣列中 rear 已達陣列上限，但 front 前方仍有大量閒置空間", ["循序陣列中 rear 已達陣列上限，但 front 前方仍有大量閒置空間", "記憶體完全耗盡", "佇列指標溢位為負數", "元素數值超過整數範圍"], "一維循序陣列實作中，多次 enqueue/dequeue 使整段有效資料往右飄移，rear 抵達 M-1 時無法再插入，即便前端有空位，環狀佇列即為解決此問題而生。"),
        ("卡特蘭數（Catalan Number）第 3 項 C₃ 之數值為？", "5", ["5", "14", "2", "9"], "C₃ = (1/4) * (6! / (3! * 3!)) = (1/4) * 20 = 5。對應 3 個元素有 5 種不同二元樹形狀或合法出棧序列。"),
        ("若佇列只允許在一端插入，且允許在兩端刪除，此種資料結構稱為？", "輸入受限雙端佇列（Input-Restricted Deque）", ["輸入受限雙端佇列（Input-Restricted Deque）", "輸出受限雙端佇列", "優先佇列", "環狀堆疊"], "Input-Restricted Deque 僅允許在單一端 enqueue，但兩端皆可 dequeue。"),
        ("若佇列允許在兩端插入，但僅允許在一端刪除，此種資料結構稱為？", "輸出受限雙端佇列（Output-Restricted Deque）", ["輸出受限雙端佇列（Output-Restricted Deque）", "輸入受限雙端佇列", "雙向佇列", "堆疊佇列"], "Output-Restricted Deque 允許在兩端進行 insert，但僅在單一端進行 remove。"),
        ("在編譯器語法分析中，將中序運算式轉為後序運算式時，當讀入右括號 ')' 時應做何處置？", "持續將堆疊頂端之運算子 pop 並輸出，直到遇到左括號 '(' 為止，並將該 '(' 丟棄", ["持續將堆疊頂端之運算子 pop 並輸出，直到遇到左括號 '(' 為止，並將該 '(' 丟棄", "將右括號壓入堆疊", "清空整個堆疊", "回傳語法錯誤"], "右括號象徵子運算式封閉，堆疊內直到匹配的左括號間之所有運算子依序彈出輸出，括號本身不輸出。"),
        ("在呼叫副程式時，系統自動將參數、區域變數與返回位址封裝成的記憶體區塊稱為？", "活動紀錄（Activation Record / Stack Frame）", ["活動紀錄（Activation Record / Stack Frame）", "PCB 行程控制區塊", "TLB 快表", "Inode 節點"], "副程式調用時在 Call Stack 配置之空間單位稱為 Activation Record 或 Stack Frame。"),
        ("將後序運算式轉回中序運算式，最佳策略為？", "由左至右掃描，遇到運算元 push 入堆疊，遇到運算子 pop 出兩個運算元組合為中序子字串再 push 回堆疊", ["由左至右掃描，遇到運算元 push 入堆疊，遇到運算子 pop 出兩個運算元組合為中序子字串再 push 回堆疊", "由右至左掃描直接輸出", "使用佇列循序還原", "先轉為前序再轉中序"], "每次遇到運算子 op，彈出右運算元 op2 與左運算元 op1，組合為 '(op1 op op2)' 壓回堆疊，掃描完畢堆疊頂即為完整中序式。")
    ]

    for stem, ans_s, opts, expl in more_sq:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "堆疊與佇列原理分析",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【堆疊與佇列機制剖析】</strong><br>
‧ <strong>(A) {ans_s}</strong>：依原理推導，{expl}<br>
‧ 其餘選項皆違反 LIFO/FIFO 行為準則或複雜度評估失真。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>FIFO (First-In First-Out)</code> <span class="en">First-In First-Out</span>：先進先出。<br>
‧ <code>LIFO (Last-In First-Out)</code> <span class="en">Last-In First-Out</span>：後進先出。<br>
‧ <code>Stack Frame</code> <span class="en">Stack Frame</span>：堆疊框架（活動紀錄）。"""
        })

    # Return accumulated qs so far
    return qs

if __name__ == '__main__':
    qs = get_all_ds_questions()
    print(f"Generated Phase 1 DS questions: {len(qs)}")
