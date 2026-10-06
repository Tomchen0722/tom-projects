import glob, re, os
from collections import defaultdict

bank_files = [
    '01-senior3/ds-bank.html',
    '01-senior3/db-bank.html',
    '01-senior3/net-bank.html',
    '01-senior3/mis-bank.html',
    '02-junior/computer-bank.html',
    '02-junior/net-bank.html',
    '02-junior/prog-bank.html',
    '03-local3/bank.html',
    '04-local4/bank.html',
    '05-common/english-bank.html',
    '05-common/law-bank.html',
]

def clean_stem(stem):
    s = re.sub(r'<[^>]+>', '', stem)
    s = re.sub(r'\(?\s*(進階題|題號)\s*\d+\s*\)?', '', s)
    s = re.sub(r'\s+', '', s)
    s = re.sub(r'[，。！？、：；（）\(\)\.\,\?\!\:\-\_\"\'\s]', '', s)
    return s.strip()

out_lines = []
out_lines.append("=== UNIQUE QUESTION SUMMARY ===")

for bf in bank_files:
    if not os.path.exists(bf):
        continue
    with open(bf, 'r', encoding='utf-8') as f:
        content = f.read()

    q_iter = re.finditer(r'<div class="q"[^>]*data-qno="([^"]+)"[^>]*data-ans="([^"]+)"[^>]*>(.*?)</div>\s*<details>', content, re.DOTALL)
    
    seen_stems = {}
    unique_count = 0
    duplicate_count = 0
    
    for m in q_iter:
        qno = m.group(1)
        ans = m.group(2)
        inner = m.group(3)
        stem_match = re.search(r'<div class="stem">(.*?)</div>', inner, re.DOTALL)
        stem = stem_match.group(1) if stem_match else ""
        c = clean_stem(stem)
        if c in seen_stems:
            duplicate_count += 1
        else:
            seen_stems[c] = qno
            unique_count += 1
            
    out_lines.append(f"{bf}:")
    out_lines.append(f"  Total raw questions: {unique_count + duplicate_count}")
    out_lines.append(f"  Duplicates to remove: {duplicate_count}")
    out_lines.append(f"  Unique questions: {unique_count}")
    out_lines.append(f"  Needed to reach 700: {max(0, 700 - unique_count)}")

with open('unique_summary.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(out_lines))

print("Summary written to unique_summary.txt")
