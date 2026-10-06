import re

with open('05-common/english-bank.html', 'r', encoding='utf-8') as f:
    text = f.read()

sections = re.findall(r'<div class="card"><h3>(.*?)</h3></div>', text)
print("Sections in English Bank:")
for s in sections:
    print(" -", s)

parts = re.split(r'(?=<div class="q"\s+data-qno=)', text)
header = parts[0]
q_blocks = parts[1:]
print(f"Total q_blocks: {len(q_blocks)}")

# Check duplicates in English Bank
def clean_stem(stem):
    s = re.sub(r'<[^>]+>', '', stem)
    s = re.sub(r'\(?\s*(進階題|題號)\s*\d+\s*\)?', '', s)
    s = re.sub(r'\s+', '', s)
    s = re.sub(r'[，。！？、：；（）\(\)\.\,\?\!\:\-\_\"\'\s]', '', s)
    return s.strip()

seen = {}
dups = []
for idx, qb in enumerate(q_blocks):
    m_stem = re.search(r'<div class="stem">(.*?)</div>', qb, re.DOTALL)
    stem = m_stem.group(1) if m_stem else ""
    c = clean_stem(stem)
    m_q = re.search(r'data-qno="([^"]+)"', qb)
    qno = m_q.group(1) if m_q else str(idx+1)
    if c in seen:
        dups.append((qno, seen[c], stem[:40]))
    else:
        seen[c] = qno

print(f"Unique questions: {len(seen)}, Duplicates: {len(dups)}")
for qno, prev, s in dups[:15]:
    print(f"  Dup Q{qno} (prev Q{prev}): {s}")
