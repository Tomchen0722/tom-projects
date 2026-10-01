# -*- coding: utf-8 -*-
"""
iPAS 資訊安全工程師 - 考科全真講義與專業名詞辭典生成腳本
收錄初級與中級 4 大考科、32 個核心單元（全面深度工程講義），以及專業資安名詞。
"""

import json
import os
import sys

# 確保當前目錄在模組搜尋路徑中
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from modules_basic import BASIC_SUBJECT_1_MODULES, BASIC_SUBJECT_2_MODULES
from modules_mid import MID_SUBJECT_1_MODULES, MID_SUBJECT_2_MODULES
from glossary_data_src import GLOSSARY_TERMS

LECTURE_NOTES = {
    "basic": {
        "title": "iPAS 資訊安全工程師 - 初級能力鑑定核心講義",
        "subjects": [
            {
                "subjectId": "B-SUB-1",
                "name": "考科一：資訊安全概論",
                "desc": "涵蓋資安核心三要素 (CIA)、網路通訊安全架構、作業系統強化、惡意程式分類防護、OWASP Top 10 核心弱點、密碼學應用與資安法規概要。",
                "modules": BASIC_SUBJECT_1_MODULES
            },
            {
                "subjectId": "B-SUB-2",
                "name": "考科二：資訊安全防護實務",
                "desc": "深入防火牆與次世代防護、端點偵測與回應 (EDR)、封包分析與異常流量診斷、弱點掃描評估、Syslog/Windows 事件日誌維運與 3-2-1 備份還原實務。",
                "modules": BASIC_SUBJECT_2_MODULES
            }
        ]
    },
    "mid": {
        "title": "iPAS 資訊安全工程師 - 中級能力鑑定核心講義",
        "subjects": [
            {
                "subjectId": "M-SUB-1",
                "name": "考科一：資訊安全規劃與管理",
                "desc": "深入探討 ISO/IEC 27001:2022 最新 ISMS 標準、資安風險管理全流程、業務持續 (BCP/BIA)、供應鏈與委外治理、個資與法規稽核。",
                "modules": MID_SUBJECT_1_MODULES
            },
            {
                "subjectId": "M-SUB-2",
                "name": "考科二：資訊安全防禦技術與事件應變",
                "desc": "涵蓋零信任架構落地、MITRE ATT&CK 框架、SOC 監控與 SOAR 自動化、CSIRT 五大階段事件應變、數位鑑識與證據保全、安全軟體開發 (SSDLC) 與雲端資安架構實務。",
                "modules": MID_SUBJECT_2_MODULES
            }
        ]
    }
}

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assets_dir = os.path.join(base_dir, "assets")
    notes_dir = os.path.join(base_dir, "notes")
    
    os.makedirs(assets_dir, exist_ok=True)
    os.makedirs(notes_dir, exist_ok=True)
    
    # 1. 寫入專業名詞辭典 JS
    glossary_js_path = os.path.join(assets_dir, "glossary-data.js")
    with open(glossary_js_path, "w", encoding="utf-8") as f:
        f.write("// iPAS 資訊安全工程師 - 專業英文術語與發音資料庫\n")
        f.write("window.IPAS_GLOSSARY = ")
        json.dump(GLOSSARY_TERMS, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print(f"Glossary written: {len(GLOSSARY_TERMS)} terms to {glossary_js_path}")

    # 2. 寫入講義資料 JS
    notes_js_path = os.path.join(assets_dir, "notes-data.js")
    with open(notes_js_path, "w", encoding="utf-8") as f:
        f.write("// iPAS 資訊安全工程師 - 初級與中級官方核心講義資料庫\n")
        f.write("window.IPAS_LECTURE_NOTES = ")
        json.dump(LECTURE_NOTES, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    total_modules = sum(len(sub["modules"]) for lvl in LECTURE_NOTES.values() for sub in lvl["subjects"])
    print(f"Lecture notes written: {total_modules} modules to {notes_js_path}")

    # 3. 寫入 Markdown 格式講義供閱讀
    for level_key, level_data in LECTURE_NOTES.items():
        md_file_path = os.path.join(notes_dir, f"{level_key}-lecture-notes.md")
        with open(md_file_path, "w", encoding="utf-8") as f:
            f.write(f"# {level_data['title']}\n\n")
            for sub in level_data["subjects"]:
                f.write(f"## {sub['name']}\n")
                f.write(f"> {sub['desc']}\n\n")
                for mod in sub["modules"]:
                    f.write(f"### {mod['title']}\n\n")
                    f.write(f"**關鍵字 (Keywords)**: {', '.join(mod['keywords'])}\n\n")
                    f.write(f"**核心概念概述**: {mod['summary']}\n\n")
                    f.write(mod["content"].strip() + "\n\n")
                    if "caseStudy" in mod and mod["caseStudy"]:
                        f.write(f"> 💡 **企業實務情境案例**：\n> {mod['caseStudy']}\n\n")
                    f.write("---\n\n")
        print(f"Markdown lecture notes written to {md_file_path}")

if __name__ == "__main__":
    main()
