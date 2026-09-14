# -*- coding: utf-8 -*-
"""
1,000 Unique Exam Questions Generator for Taiwan Real Estate Salesperson Certification
Each question includes:
- id: SEC-XX-YYY
- category
- question
- options: [A, B, C, D]
- answer: A / B / C / D
- law: Exact law title & article
- explanation: Detailed rationale
- trap: Exam trap warning
"""
import os
import json

BASE_DIR = r"c:\AI\tom-projects\learning\realtor"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
EXAM_DIR = os.path.join(BASE_DIR, "exam")

os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(EXAM_DIR, exist_ok=True)

questions = []

# Helper to add question
def add_q(sec_id, cat, q_text, opts, ans, law, exp, trap):
    questions.append({
        "id": sec_id,
        "category": cat,
        "question": q_text,
        "options": opts,
        "answer": ans,
        "law": law,
        "explanation": exp,
        "trap": trap
    })

print("Starting generation of 1,000 unique questions...")
