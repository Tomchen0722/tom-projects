# -*- coding: utf-8 -*-
"""
Assembler script to combine:
- 64 original essays (32 sec + 32 sysnet)
- 30 predicted essays (16 sec + 14 sysnet)
- 20 new sec essays (sec-essay-49 ~ sec-essay-68)
- 8 core simulation sec essays (sec-essay-69 ~ sec-essay-76)
- 3 core facility & physical security sec essays (sec-essay-77 ~ sec-essay-79)
- 10 new facility, physical & CI security sec essays (sec-essay-80 ~ sec-essay-89)
Total: 135 full-mark essays for the TWSE recruit exam platform.
(89 Information Security + 46 System & Network Management)
"""
import os
import sys
import json

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CURRENT_DIR)

import build_essays
import new_sec_essays
import new_sysnet_essays
import new_sysnet_essays_part2
import new_30_twse_essays
import new_sec_20_essays
import new_core_8_essays
import new_facility_3_essays
import new_facility_10_essays

def assemble_135_essays():
    # 1. Original 24 essays (12 sysnet + 12 sec)
    original_data = build_essays.get_essay_data()
    orig_sysnet = [e for e in original_data if e["category"] == "sysnet"]
    orig_sec = [e for e in original_data if e["category"] == "sec"]

    # 2. Previous new 20 sec essays (sec-essay-13 to 32)
    new_sec_1 = new_sec_essays.get_20_new_sec_essays()
    new_sec_2 = new_sec_essays.get_more_sec_essays_21_to_32()
    prev_all_sec = orig_sec + new_sec_1 + new_sec_2  # 32 sec essays

    # 3. Previous new 20 sysnet essays (sn-essay-13 to 32)
    new_sys_1 = new_sysnet_essays.get_20_new_sysnet_essays()
    new_sys_2 = new_sysnet_essays_part2.get_more_sysnet_essays_18_to_32()
    prev_all_sysnet = orig_sysnet + new_sys_1 + new_sys_2  # 32 sysnet essays

    # 4. Brand new 30 predicted essays (16 sec + 14 sysnet)
    brand_new = new_30_twse_essays.get_30_new_essays()
    brand_new_sec = [e for e in brand_new if e["category"] == "sec"]
    brand_new_sysnet = [e for e in brand_new if e["category"] == "sysnet"]

    # 5. Brand new 20 Information Security essays (sec-essay-49 to 68)
    new_20_sec = new_sec_20_essays.get_20_new_sec_essays()

    # 6. Core 8 Information Security simulation essays (sec-essay-69 to 76)
    core_8_sec = new_core_8_essays.get_8_core_twse_essays()

    # 7. Core 3 Facility & Physical Security essays (sec-essay-77 to 79)
    facility_3_sec = new_facility_3_essays.get_3_new_facility_essays()

    # 8. Brand new 10 Facility & CI Physical Security essays (sec-essay-80 to 89)
    facility_10_sec = new_facility_10_essays.get_10_new_facility_essays()

    total_sec = prev_all_sec + brand_new_sec + new_20_sec + core_8_sec + facility_3_sec + facility_10_sec # 32 + 16 + 20 + 8 + 3 + 10 = 89 sec
    total_sysnet = prev_all_sysnet + brand_new_sysnet                                                      # 32 + 14 = 46 sysnet
    combined = total_sec + total_sysnet                                                                    # 89 + 46 = 135 total

    print(f"Total Sec Essays:    {len(total_sec)} (89 expected)")
    print(f"Total Sysnet Essays: {len(total_sysnet)} (46 expected)")
    print(f"Grand Total Essays:  {len(combined)} (135 expected)")

    # Ensure IDs are unique
    ids = [e["id"] for e in combined]
    assert len(ids) == len(set(ids)), f"Duplicate IDs detected: {len(ids)} vs {len(set(ids))}"
    assert len(combined) == 135, f"Expected 135 essays, got {len(combined)}"

    output_path = os.path.join(CURRENT_DIR, "..", "assets", "essay-data.js")
    output_path = os.path.normpath(output_path)

    js_header = """/**
 * 臺灣證券交易所 (TWSE) 招募備考系統 - 滿分精要申論題庫 (135 題全真標竿高分範本 · 內含 71 題最新預測猜題)
 * 收錄資通安全 (89 題，主考科) 與 系統與網路管理 (46 題，輔考科)
 * 遵循國家考試與證交所招募評分標準（破題立論、條列架構、關鍵對比剖析、實務參數調校、得分秘笈與深度解說）
 */

const TWSE_ESSAY_DATA = """

    js_footer = """;

// 關鍵導出：附掛於全局 window 物件以利跨腳本存取
window.TWSE_ESSAY_DATA = TWSE_ESSAY_DATA;
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(js_header + json.dumps(combined, ensure_ascii=False, indent=2) + js_footer)

    print(f"Successfully generated {output_path} with {len(combined)} full-mark essays!")

if __name__ == "__main__":
    assemble_135_essays()
