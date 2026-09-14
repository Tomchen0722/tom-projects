# -*- coding: utf-8 -*-
"""
Compiles all 8 sections into:
1. assets/questions-data.js
2. exam/question-bank-full.md
"""
import os
import json
import sys

# Append scripts folder to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from q_sec1 import get_sec1_questions
from q_sec2 import get_sec2_questions
from q_sec3 import get_sec3_questions
from q_sec4 import get_sec4_questions
from q_sec5_8 import get_sec5_questions, get_sec6_questions, get_sec7_questions, get_sec8_questions

BASE_DIR = r"c:\AI\tom-projects\learning\realtor"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
EXAM_DIR = os.path.join(BASE_DIR, "exam")

os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(EXAM_DIR, exist_ok=True)

print("Gathering questions from all 8 sections...")
q1 = get_sec1_questions() # 150
q2 = get_sec2_questions() # 150
q3 = get_sec3_questions() # 150
q4 = get_sec4_questions() # 150
q5 = get_sec5_questions() # 100
q6 = get_sec6_questions() # 100
q7 = get_sec7_questions() # 100
q8 = get_sec8_questions() # 100

all_qs = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8

print(f"Total collected questions: {len(all_qs)}")
print(f"  SEC-01: {len(q1)}")
print(f"  SEC-02: {len(q2)}")
print(f"  SEC-03: {len(q3)}")
print(f"  SEC-04: {len(q4)}")
print(f"  SEC-05: {len(q5)}")
print(f"  SEC-06: {len(q6)}")
print(f"  SEC-07: {len(q7)}")
print(f"  SEC-08: {len(q8)}")

# Verify IDs are unique
ids = [q['id'] for q in all_qs]
unique_ids = set(ids)
if len(ids) != len(unique_ids):
    raise ValueError(f"Duplicate IDs detected! Total: {len(ids)}, Unique: {len(unique_ids)}")

print("All 1,000 question IDs are verified unique!")

# 1. Output assets/questions-data.js
js_path = os.path.join(ASSETS_DIR, "questions-data.js")
with open(js_path, "w", encoding="utf-8") as f:
    f.write("// 不動產經紀營業員 1000 題完整解析題庫資料庫\n")
    f.write("window.QUESTION_BANK = ")
    json.dump(all_qs, f, ensure_ascii=False, indent=2)
    f.write(";\n")
print(f"Successfully generated: {js_path} ({os.path.getsize(js_path):,} bytes)")

# 2. Output exam/question-bank-full.md
md_path = os.path.join(EXAM_DIR, "question-bank-full.md")
with open(md_path, "w", encoding="utf-8") as f:
    f.write("# 不動產經紀營業員資格測驗：1,000 題完整題庫與精闢解析全書\n\n")
    f.write("> 本書收錄全真考試涵蓋之 8 大法規科目共 1,000 道不重複標準測驗題目。每一題均附完整選項、正確答案、法定法條依據、精闢白話解析與考點防呆陷阱提示！\n\n")
    f.write("---\n\n")
    
    current_cat = None
    for q in all_qs:
        if q['category'] != current_cat:
            current_cat = q['category']
            f.write(f"\n## 【科目】{current_cat}\n\n")
            f.write("---\n\n")
            
        f.write(f"### 題號：{q['id']}\n\n")
        f.write(f"**【題目】** {q['question']}\n\n")
        for opt in q['options']:
            f.write(f"- {opt}\n")
        f.write(f"\n- **【正確答案】**：`{q['answer']}`\n")
        f.write(f"- **【法條依據】**：{q['law']}\n")
        f.write(f"- **【詳細解析】**：{q['explanation']}\n")
        f.write(f"- **【考點陷阱】**：💡 {q['trap']}\n\n")
        f.write("---\n\n")

print(f"Successfully generated: {md_path} ({os.path.getsize(md_path):,} bytes)")
print("Question bank build finished successfully!")
