# -*- coding: utf-8 -*-
"""
Compiles all 4 Land Agent sections into:
1. assets/questions-data.js
2. exam/question-bank-full.md
"""
import os
import json
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from q_sec1_civil import get_sec1_questions
from q_sec2_landlaw import get_sec2_questions
from q_sec3_registration import get_sec3_questions
from q_sec4_tax import get_sec4_questions

BASE_DIR = os.path.abspath(os.path.join(current_dir, ".."))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
EXAM_DIR = os.path.join(BASE_DIR, "exam")

os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(EXAM_DIR, exist_ok=True)

print("Gathering questions from all 4 professional sections...")
q1 = get_sec1_questions() # 150
q2 = get_sec2_questions() # 150
q3 = get_sec3_questions() # 150
q4 = get_sec4_questions() # 150

all_qs = q1 + q2 + q3 + q4

print(f"Total collected questions: {len(all_qs)}")
print(f"  SEC-01 (民法概要與信託法概要): {len(q1)}")
print(f"  SEC-02 (土地法規): {len(q2)}")
print(f"  SEC-03 (土地登記規則與地籍測量): {len(q3)}")
print(f"  SEC-04 (土地稅法規): {len(q4)}")

# Verify IDs are unique
ids = [q['id'] for q in all_qs]
unique_ids = set(ids)
if len(ids) != len(unique_ids):
    raise ValueError(f"Duplicate IDs detected! Total: {len(ids)}, Unique: {len(unique_ids)}")

print("All 600 question IDs are verified unique!")

# 1. Output assets/questions-data.js
js_path = os.path.join(ASSETS_DIR, "questions-data.js")
with open(js_path, "w", encoding="utf-8") as f:
    f.write("// 地政士（土地登記專業代理人）專技普考 600 題完整解析題庫資料庫\n")
    f.write("window.QUESTION_BANK = ")
    json.dump(all_qs, f, ensure_ascii=False, indent=2)
    f.write(";\n")
print(f"Successfully generated: {js_path} ({os.path.getsize(js_path):,} bytes)")

# 2. Output exam/question-bank-full.md
md_path = os.path.join(EXAM_DIR, "question-bank-full.md")
with open(md_path, "w", encoding="utf-8") as f:
    f.write("# 專門職業及技術人員普通考試地政士考試：600 題全真題庫與精闢解析全書\n\n")
    f.write("> 本書完整收錄地政士國家考試 4 大專業考科共 600 道標準試題。每一題均嚴格附有完整選項、官方正確答案、法定法條依據、深入白話解析與高頻考點防呆陷阱提示！\n\n")
    f.write("---\n\n")
    
    current_cat = None
    for item in all_qs:
        if item['category'] != current_cat:
            current_cat = item['category']
            f.write(f"\n## 【科目】{current_cat}\n\n")
            f.write("---\n\n")
            
        f.write(f"### 題號：{item['id']}\n\n")
        f.write(f"**【題目】** {item['question']}\n\n")
        for opt in item['options']:
            f.write(f"- {opt}\n")
        f.write(f"\n- **【正確答案】**：`{item['answer']}`\n")
        f.write(f"- **【法條依據】**：{item['law']}\n")
        f.write(f"- **【詳細解析】**：{item['explanation']}\n")
        f.write(f"- **【考點防呆】**：💡 {item['trap']}\n\n")
        f.write("---\n\n")

print(f"Successfully generated: {md_path} ({os.path.getsize(md_path):,} bytes)")
print("Question bank compilation finished successfully!")
