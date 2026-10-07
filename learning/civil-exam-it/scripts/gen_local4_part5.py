#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Local Civil Service Level 4 (地方特考四等) Question Bank Part 5 (80 questions).
Categories:
1. 程式語言基礎與資料結構 (27 questions)
2. 關聯式資料庫與 SQL 查詢實務 (27 questions)
3. 演算法分析、排序搜尋與軟體工程 (26 questions)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from scripts.gen_local4_part5_a import get_data1, get_data2
    from scripts.gen_local4_part5_b import get_data3
except ImportError:
    from gen_local4_part5_a import get_data1, get_data2
    from gen_local4_part5_b import get_data3

def get_local4_part5_questions():
    qs = []

    all_datasets = [
        ("程式語言基礎與資料結構", get_data1()),
        ("關聯式資料庫與 SQL 查詢實務", get_data2()),
        ("演算法分析、排序搜尋與軟體工程", get_data3())
    ]

    for cat_name, dataset in all_datasets:
        for stem, ans_s, opts, expl in dataset:
            choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
            qs.append({
                "tag": "程式設計概要",
                "stem": stem,
                "choices": choices,
                "ans": "A",
                "ans_text": f"(A) {ans_s}",
                "explanation": f"""<strong>【地方特考四等公務實務情境深度解析】</strong><br>
<div class="step-box">
  <div class="step-title">💻 地方政府程式設計、演算法效能與資料庫實務剖析</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>釐清核心語法語意、演算法複雜度與資料模型</strong><br>
      ‧ 本題依據國家考試地方特考四等《程式設計概要》與《計算機概要》考綱，緊扣 C/Python 語言特性、樹/圖資料結構、正規化 SQL 語法與軟體工程生命週期嚴謹命題。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>詳細邏輯推導與公務資訊系統應用對照</strong><br>
      ‧ {expl}
    </li>
  </ul>
</div>
<br><strong>【各選項詳細對錯解析】</strong><br>
‧ <strong>(A) 正確</strong>：{opts[0]}。<br>
‧ <strong>(B) 錯誤</strong>：{opts[1]}（邏輯概念偏差、複雜度計算錯誤或語意混淆）。<br>
‧ <strong>(C) 錯誤</strong>：{opts[2]}（違背資料結構定義或不合語言規範）。<br>
‧ <strong>(D) 錯誤</strong>：{opts[3]}（極端荒謬之技術描述或違背軟體工程標準）。<br><br>
<strong>地特加分角度</strong>：地方特考四等在程式設計考科中，<strong>二元樹追蹤（前/中/後序）與高度性質</strong>、<strong>Big-O 排序演算法時空複雜度</strong>、<strong>SQL 語法（GROUP BY/HAVING/JOIN）與 ACID 特性</strong>、以及<strong>資料庫 1NF~BCNF 正規化拆解</strong>為每年必考核心。作答時清楚掌握<strong>推導計算與邊界條件</strong>，可穩拿最高分。"""
            })

    return qs

if __name__ == '__main__':
    qs = get_local4_part5_questions()
    print(f"Total Part 5 questions generated: {len(qs)}")
