# -*- coding: utf-8 -*-
"""
Forwarding script: now updated to 122 essays (76 sec + 46 sysnet).
"""
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CURRENT_DIR)

import build_all_122_essays

def assemble_114_essays():
    build_all_122_essays.assemble_122_essays()

if __name__ == "__main__":
    assemble_114_essays()
