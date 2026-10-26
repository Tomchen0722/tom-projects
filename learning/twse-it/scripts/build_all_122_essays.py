# -*- coding: utf-8 -*-
"""
Forwarding script: now updated to 125 essays (79 sec + 46 sysnet).
"""
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CURRENT_DIR)

import build_all_125_essays

def assemble_122_essays():
    build_all_125_essays.assemble_125_essays()

if __name__ == "__main__":
    assemble_122_essays()
