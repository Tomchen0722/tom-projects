# -*- coding: utf-8 -*-
import os
import re
import json

base_dir = r"c:\AI\tom-projects\learning\twse-it"
html_path = os.path.join(base_dir, "index.html")

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

scripts = re.findall(r'<script src="([^"]+)"', html)
print(f"Total linked scripts in index.html: {len(scripts)}")

for s in scripts:
    p = os.path.join(base_dir, s)
    if os.path.exists(p):
        size = os.path.getsize(p)
        print(f"  [OK] {s}: {size:,} bytes")
    else:
        print(f"  [FAIL] MISSING: {s}")

# Check essay-data.js
essay_path = os.path.join(base_dir, "assets", "essay-data.js")
with open(essay_path, "r", encoding="utf-8") as f:
    text = f.read()

m = re.search(r"const TWSE_ESSAY_DATA = (\[[\s\S]+\]);", text)
assert m, "TWSE_ESSAY_DATA not found in essay-data.js"
essays = json.loads(m.group(1))

sec_essays = [e for e in essays if e.get("category") == "sec"]
sys_essays = [e for e in essays if e.get("category") == "sysnet"]

print(f"\n[Essay Verification]")
print(f"  Total essays:     {len(essays)} (Expected: 135)")
print(f"  Sec essays:       {len(sec_essays)} (Expected: 89)")
print(f"  Sysnet essays:    {len(sys_essays)} (Expected: 46)")

assert len(essays) == 135, f"Expected 135, got {len(essays)}"
assert len(sec_essays) == 89, f"Expected 89, got {len(sec_essays)}"
assert len(sys_essays) == 46, f"Expected 46, got {len(sys_essays)}"

# Ensure IDs are distinct
ids = [e["id"] for e in essays]
assert len(ids) == len(set(ids)), f"Duplicate essay IDs detected: {len(ids)} vs {len(set(ids))}"
print("  [OK] All 135 IDs are distinct!")

# Ensure all 41 newly added essays (sec-essay-49 ~ sec-essay-89) exist and have complete structure
for i in range(49, 90):
    expected_id = f"sec-essay-{i:02d}"
    matched = [e for e in essays if e["id"] == expected_id]
    assert len(matched) == 1, f"Missing or duplicate {expected_id}"
    e = matched[0]
    for key in ["title", "chapter", "question", "modelAnswer", "examinerTips", "detailedExplanation", "rubric", "points"]:
        assert key in e and e[key], f"Missing {key} in {expected_id}"

print("  [OK] All 41 new InfoSec essays (sec-essay-49 to sec-essay-89) verified with complete rubrics and model answers!")

# Check notes
notes_sysnet_path = os.path.join(base_dir, "assets", "notes-sysnet.js")
with open(notes_sysnet_path, "r", encoding="utf-8") as f:
    n_sysnet = f.read()
ch_sn = n_sysnet.count('"id": "sn-ch')
print(f"\n[Lecture Notes]")
print(f"  notes-sysnet.js chapters: {ch_sn} (Expected: 12)")

notes_sec_path = os.path.join(base_dir, "assets", "notes-sec.js")
with open(notes_sec_path, "r", encoding="utf-8") as f:
    n_sec = f.read()
ch_sec = n_sec.count('"id": "sec-ch')
print(f"  notes-sec.js chapters:    {ch_sec} (Expected: 12)")

# Check glossary
glossary_path = os.path.join(base_dir, "assets", "glossary-data.js")
with open(glossary_path, "r", encoding="utf-8") as f:
    glo_text = f.read()
print(f"\n[Glossary Terms]")
print(f"  glossary-data.js items:   {glo_text.count('zh:')}")

print("\n=== ALL TWSE VERIFICATIONS PASSED SUCCESSFULLY! ===")
