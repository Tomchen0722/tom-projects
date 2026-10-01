# -*- coding: utf-8 -*-
"""
iPAS 資安工程師 - 全量 1,600 題題庫與講義詞典完整性驗證系統
"""

import json
import os

def load_js_data(filepath, prefix):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    idx = content.find(prefix)
    if idx == -1:
        raise ValueError(f"Prefix '{prefix}' not found in {filepath}")
    json_str = content[idx + len(prefix):].rstrip(';\n ')
    return json.loads(json_str)

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assets_dir = os.path.join(base_dir, "assets")

    # 1. 驗證初級 800 題
    basic_path = os.path.join(assets_dir, "questions-basic.js")
    basic_data = load_js_data(basic_path, "window.IPAS_QUESTIONS_BASIC = ")
    print(f"[1/4] Verifying Basic Questions: Total {len(basic_data)}...")
    assert len(basic_data) == 800, f"Expected 800 basic questions, got {len(basic_data)}"

    # 2. 驗證中級 800 題
    mid_path = os.path.join(assets_dir, "questions-mid.js")
    mid_data = load_js_data(mid_path, "window.IPAS_QUESTIONS_MID = ")
    print(f"[2/4] Verifying Mid Questions: Total {len(mid_data)}...")
    assert len(mid_data) == 800, f"Expected 800 mid questions, got {len(mid_data)}"

    total_data = basic_data + mid_data
    assert len(total_data) == 1600, f"Expected 1,600 total questions, got {len(total_data)}"
    print(f"[3/4] Verifying All 1,600 Questions Integrity & Uniqueness...")

    all_ids = set()
    basic_scenarios = 0
    mid_scenarios = 0
    terms_count = 0

    for q in total_data:
        qid = q.get('id')
        assert qid, "Question missing id"
        assert qid not in all_ids, f"Duplicate Question ID found: {qid}"
        all_ids.add(qid)

        assert q.get('level') in ['初級', '中級'], f"Invalid level in {qid}"
        assert q.get('subject'), f"Missing subject in {qid}"
        assert q.get('domain'), f"Missing domain in {qid}"
        assert len(q.get('options', [])) == 4, f"Options != 4 in {qid}"
        assert q.get('answer') in ['A', 'B', 'C', 'D'], f"Invalid answer in {qid}"
        assert q.get('explanation'), f"Missing explanation in {qid}"
        assert q.get('trap'), f"Missing trap in {qid}"
        assert q.get('law'), f"Missing law in {qid}"

        if q['level'] == '初級' and q.get('scenario'):
            basic_scenarios += 1
        elif q['level'] == '中級' and q.get('scenario'):
            mid_scenarios += 1

        terms = q.get('terms', [])
        assert isinstance(terms, list), f"terms must be a list in {qid}"
        terms_count += len(terms)
        for t in terms:
            assert 'en' in t and 'zh' in t and 'ipa' in t, f"Incomplete term in {qid}: {t}"

    basic_pct = (basic_scenarios / 800) * 100
    mid_pct = (mid_scenarios / 800) * 100
    print(f"  - Basic Scenario Questions: {basic_scenarios}/800 ({basic_pct:.1f}%)")
    print(f"  - Mid Scenario Questions: {mid_scenarios}/800 ({mid_pct:.1f}%)")
    print(f"  - Total Tagged English Terms with Pronunciation: {terms_count}")
    assert basic_pct >= 90.0, f"Basic scenario percentage {basic_pct}% < 90%"
    assert mid_pct >= 90.0, f"Mid scenario percentage {mid_pct}% < 90%"

    # 4. 驗證講義與專業辭典
    glossary_path = os.path.join(assets_dir, "glossary-data.js")
    glossary_data = load_js_data(glossary_path, "window.IPAS_GLOSSARY = ")
    print(f"[4/4] Verifying Glossary: {len(glossary_data)} terms...")
    assert len(glossary_data) >= 30, "Glossary has too few terms"

    notes_path = os.path.join(assets_dir, "notes-data.js")
    notes_data = load_js_data(notes_path, "window.IPAS_LECTURE_NOTES = ")
    assert "basic" in notes_data and "mid" in notes_data, "Notes data missing basic/mid"

    print("\n" + "="*60)
    print(" ALL 1,600 QUESTIONS & LECTURE NOTES VERIFICATION PASSED!")
    print(" - Total Questions: 1,600 (800 Basic + 800 Intermediate)")
    print(" - 100% Unique Question IDs (No Duplication)")
    print(f" - Scenario Questions: {basic_scenarios + mid_scenarios}/1600 ({(basic_scenarios+mid_scenarios)/16:.1f}%) >= 90%")
    print(" - Full English Pronunciation (IPA & Web Speech API) & Traditional Chinese Support")
    print("="*60)

if __name__ == "__main__":
    main()
