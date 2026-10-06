import re

def clean_stem(stem):
    s = re.sub(r'<[^>]+>', '', stem)
    s = re.sub(r'\(?\s*(進階題|題號)\s*\d+\s*\)?', '', s)
    s = re.sub(r'\s+', '', s)
    s = re.sub(r'[，。！？、：；（）\(\)\.\,\?\!\:\-\_\"\'\s]', '', s)
    return s.strip()

with open('02-junior/computer-bank.html', 'r', encoding='utf-8') as f:
    text = f.read()

parts = re.split(r'(?=<div class="q"\s+data-qno=)', text)
header = parts[0]
q_blocks = parts[1:]

seen = set()
unique_qs = []
duplicates = 0

for q in q_blocks:
    m = re.search(r'<div class="stem">(.*?)</div>', q, re.DOTALL)
    stem = m.group(1) if m else ""
    c = clean_stem(stem)
    if not c:
        continue
    if c in seen:
        duplicates += 1
    else:
        seen.add(c)
        unique_qs.append(q)

print(f"Total question blocks in file: {len(q_blocks)}")
print(f"Duplicates found: {duplicates}")
print(f"Unique questions preserved: {len(unique_qs)}")
print(f"Questions needed to reach 700: {700 - len(unique_qs)}")
