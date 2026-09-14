# -*- coding: utf-8 -*-
"""
Full Question Bank Generator for 1,000 Unique Real Estate Salesperson Questions.
Generates:
1. assets/questions-data.js
2. exam/question-bank-full.md
"""
import os
import json

BASE_DIR = r"c:\AI\tom-projects\learning\realtor"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
EXAM_DIR = os.path.join(BASE_DIR, "exam")

os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(EXAM_DIR, exist_ok=True)

all_questions = []

def record_q(q_id, cat, q_text, opts, ans, law, exp, trap):
    all_questions.append({
        "id": q_id,
        "category": cat,
        "question": q_text,
        "options": opts,
        "answer": ans,
        "law": law,
        "explanation": exp,
        "trap": trap
    })

print("Loading question generation templates...")
