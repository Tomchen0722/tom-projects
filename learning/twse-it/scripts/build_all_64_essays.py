# -*- coding: utf-8 -*-
"""
Assembler script to combine original 24 essays + 20 new sec essays + 20 new sysnet essays
Total: 64 full-mark essays for the TWSE exam platform.
"""
import os
import sys
import json

# Ensure scripts dir is in path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CURRENT_DIR)

import build_essays
import new_sec_essays
import new_sysnet_essays
import new_sysnet_essays_part2

def assemble_all_essays():
    # 1. Original 24 essays (12 sysnet + 12 sec)
    original_data = build_essays.get_essay_data()
    orig_sysnet = [e for e in original_data if e["category"] == "sysnet"]
    orig_sec = [e for e in original_data if e["category"] == "sec"]

    # 2. New 20 sec essays
    new_sec_1 = new_sec_essays.get_20_new_sec_essays()
    new_sec_2 = new_sec_essays.get_more_sec_essays_21_to_32()
    all_new_sec = new_sec_1 + new_sec_2

    # 3. New 20 sysnet essays
    new_sys_1 = new_sysnet_essays.get_20_new_sysnet_essays()
    new_sys_2 = new_sysnet_essays_part2.get_more_sysnet_essays_18_to_32()
    all_new_sysnet = new_sys_1 + new_sys_2

    print(f"Original Sysnet count: {len(orig_sysnet)}")
    print(f"New Sysnet count:      {len(all_new_sysnet)}")
    print(f"Total Sysnet count:    {len(orig_sysnet) + len(all_new_sysnet)}")
    print("-" * 40)
    print(f"Original Sec count:    {len(orig_sec)}")
    print(f"New Sec count:         {len(all_new_sec)}")
    print(f"Total Sec count:       {len(orig_sec) + len(all_new_sec)}")
    print("-" * 40)

    # Order: As user requested, prioritize Information Security (資通安全為主，系統與網路為輔)
    # We can group sec first then sysnet, or sysnet then sec. Let's provide:
    # all_sec (32) + all_sysnet (32)
    # This ensures sec questions are prioritized!
    combined = (orig_sec + all_new_sec) + (orig_sysnet + all_new_sysnet)
    print(f"Overall Total Essays: {len(combined)}")

    # Verify uniqueness of IDs
    ids = [e["id"] for e in combined]
    assert len(ids) == len(set(ids)), f"Duplicate IDs found: {len(ids)} vs {len(set(ids))}"
    assert len(combined) == 64, f"Expected 64 essays, got {len(combined)}"

    output_path = os.path.join(CURRENT_DIR, "..", "assets", "essay-data.js")
    output_path = os.path.normpath(output_path)

    js_header = """/**
 * 臺灣證券交易所 (TWSE) 招募備考系統 - 滿分精要申論題庫 (64 題全真標竿高分範本)
 * 收錄資通安全 (32 題，主考科) 與 系統與網路管理 (32 題，輔考科)
 * 遵循國家考試與證交所招募評分標準（破題立論、條列架構、橫向對比表、實務參數調校、得分秘笈與深度解說）
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
    assemble_all_essays()
