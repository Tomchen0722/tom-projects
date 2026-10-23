# -*- coding: utf-8 -*-
"""
Forwarding script: now updated to 114 essays (68 sec + 46 sysnet).
"""
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CURRENT_DIR)

import build_all_114_essays

def assemble_94_essays():
    build_all_114_essays.assemble_114_essays()

if __name__ == "__main__":
    assemble_94_essays()

