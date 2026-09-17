# -*- coding: utf-8 -*-
"""
Generate Section 1: 民法概要與信託法概要 (150 Questions)
"""
import sys
import os

def generate_sec1():
    dest_path = os.path.join(os.path.dirname(__file__), "q_sec1_civil.py")
    
    # We will write q_sec1_civil.py directly
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write('''# -*- coding: utf-8 -*-
"""
Section 1: 民法概要與信託法概要 (150 題)
SEC-01-001 ~ SEC-01-150
"""

def get_sec1_questions():
    return [
''')

if __name__ == "__main__":
    generate_sec1()
    print("Base generated.")
