# -*- coding: utf-8 -*-
"""
Forwarding script: now updated to 135 essays (89 sec + 46 sysnet).
"""
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CURRENT_DIR)

import build_all_135_essays

def assemble_125_essays():
    build_all_135_essays.assemble_135_essays()

if __name__ == "__main__":
    assemble_125_essays()
