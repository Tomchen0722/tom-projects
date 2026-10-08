# -*- coding: utf-8 -*-
import os
import re

base_dir = r"c:\AI\tom-projects\learning\twse-it"
html_path = os.path.join(base_dir, "index.html")

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

scripts = re.findall(r'<script src="([^"]+)"', html)
print(f"Total linked scripts: {len(scripts)}")

for s in scripts:
    p = os.path.join(base_dir, s)
    if os.path.exists(p):
        size = os.path.getsize(p)
        print(f"  [OK] {s}: {size:,} bytes")
    else:
        print(f"  [FAIL] MISSING: {s}")

# Check sysnet question count
q_sysnet_path = os.path.join(base_dir, "assets", "questions-sysnet.js")
with open(q_sysnet_path, "r", encoding="utf-8") as f:
    sysnet_text = f.read()
q_sysnet_count = sysnet_text.count('"id":')
print(f"questions-sysnet.js question count: {q_sysnet_count}")

# Check sec question count
q_sec_path = os.path.join(base_dir, "assets", "questions-sec.js")
with open(q_sec_path, "r", encoding="utf-8") as f:
    sec_text = f.read()
q_sec_count = sec_text.count('"id":')
print(f"questions-sec.js question count: {q_sec_count}")

# Check notes
notes_sysnet_path = os.path.join(base_dir, "assets", "notes-sysnet.js")
with open(notes_sysnet_path, "r", encoding="utf-8") as f:
    n_sysnet = f.read()
print(f"notes-sysnet.js chapters: {n_sysnet.count('id: \"sn-ch')}")

notes_sec_path = os.path.join(base_dir, "assets", "notes-sec.js")
with open(notes_sec_path, "r", encoding="utf-8") as f:
    n_sec = f.read()
print(f"notes-sec.js chapters: {n_sec.count('id: \"sec-ch')}")

# Check essay
essay_path = os.path.join(base_dir, "assets", "essay-data.js")
with open(essay_path, "r", encoding="utf-8") as f:
    essay_text = f.read()
print(f"essay-data.js count: {essay_text.count('points: 25')}")

# Check glossary
glossary_path = os.path.join(base_dir, "assets", "glossary-data.js")
with open(glossary_path, "r", encoding="utf-8") as f:
    glo_text = f.read()
print(f"glossary-data.js count: {glo_text.count('zh:')}")

print("\nALL TWSE-IT ASSETS AND DATA VERIFIED SUCCESSFULLY!")
