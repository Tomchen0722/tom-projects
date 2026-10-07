#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Local Civil Service Level 4 (地方特考四等) Question Bank Part 4 (80 questions).
Categories:
1. 密碼學、PKI 憑證與身分鑑別 (27 questions)
2. 網路攻擊手法、OWASP Web 安全與惡意程式 (27 questions)
3. 資安防禦架構、監控與公務資安法規/ISMS 實務 (26 questions)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from scripts.gen_local4_part4_a import get_data1, get_data2
    from scripts.gen_local4_part4_b import get_data3
except ImportError:
    from gen_local4_part4_a import get_data1, get_data2
    from gen_local4_part4_b import get_data3

def get_local4_part4_questions():
    qs = []

    all_datasets = [
        ("密碼學、PKI 憑證與身分鑑別", get_data1()),
        ("網路攻擊手法、OWASP Web 安全與惡意程式", get_data2()),
        ("資安防禦架構、監控與公務資安法規/ISMS 實務", get_data3())
    ]

    for cat_name, dataset in all_datasets:
        for stem, ans_s, opts, expl in dataset:
            choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
            qs.append({
                "tag": "資通網路與安全概要",
                "stem": stem,
                "choices": choices,
                "ans": "A",
                "ans_text": f"(A) {ans_s}",
                "explanation": f"""<strong>【地方特考四等公務實務情境深度解析】</strong><br>
<div class="step-box">
  <div class="step-title">🛡️ 地方政府資通安全維護、威脅防禦與法規遵循實務剖析</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>釐清核心安全目標、防禦機制與機關維運情境</strong><br>
      ‧ 本題依據國家考試地方特考四等《資通網路與安全概要》最新命題大綱，緊扣機關資通安全法規、密碼學應用、縱深防禦架構與 OWASP Web 弱點嚴謹命題。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>詳細技術推導與安全實務要點對照</strong><br>
      ‧ {expl}
    </li>
  </ul>
</div>
<br><strong>【各選項詳細對錯解析】</strong><br>
‧ <strong>(A) 正確</strong>：{opts[0]}。<br>
‧ <strong>(B) 錯誤</strong>：{opts[1]}（安全觀念偏差、機制混淆或名詞認知錯誤）。<br>
‧ <strong>(C) 錯誤</strong>：{opts[2]}（違背資安最佳實踐或不符實務防禦原則）。<br>
‧ <strong>(D) 錯誤</strong>：{opts[3]}（嚴重違背資通安全管理法或業界標準標準規範）。<br><br>
<strong>地特加分角度</strong>：地方特考四等在資安考科中，<strong>《資通安全管理法》事件通報時限與責任等級</strong>、<strong>對稱 vs 非對稱密碼學運作機制</strong>、<strong>OWASP Top 10 漏洞與防禦</strong>、以及<strong>縱深防禦（WAF/EDR/SIEM）協同運作</strong>為每年必考核心。作答時清楚掌握<strong>法規條文與技術防護細節</strong>，可穩拿最高分。"""
            })

    return qs

if __name__ == '__main__':
    qs = get_local4_part4_questions()
    print(f"Total Part 4 questions generated: {len(qs)}")
