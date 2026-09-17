# -*- coding: utf-8 -*-
"""
Full Section 1 Question Generator (150 Questions)
Writes directly to q_sec1_civil.py
"""
import os
import sys

output_path = os.path.join(os.path.dirname(__file__), "q_sec1_civil.py")

script_content = '''# -*- coding: utf-8 -*-
"""
Section 1: 民法概要與信託法概要 (150 題)
IDs: SEC-01-001 ~ SEC-01-150
"""

def get_sec1_questions():
    return [
'''

# We will generate and write each question block cleanly.
