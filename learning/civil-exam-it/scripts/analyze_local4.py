# -*- coding: utf-8 -*-
import re

def clean_stem(stem):
    s = re.sub(r'<[^>]+>', '', stem)
    s = re.sub(r'\(?\s*(進階題|題號)\s*\d+\s*\)?', '', s)
    s = re.sub(r'\s+', '', s)
    s = re.sub(r'[，。！？、：；（）\(\)\.\,\?\!\:\-\_\"\'\s]', '', s)
    return s.strip()

with open('04-local4/bank.html', 'r', encoding='utf-8') as f:
    text = f.read()

parts = re.split(r'(?=<div class="q"\s+data-qno=)', text)
header = parts[0]
q_blocks = parts[1:]

print(f"Total q blocks found: {len(q_blocks)}")

last_block = q_blocks[-1]
m_last = re.search(r'(.*?)(</details>\s*</div>)(.*)', last_block, re.DOTALL)
if m_last:
    q_blocks[-1] = m_last.group(1) + m_last.group(2)
    footer = m_last.group(3)
    print("Cleanly separated footer! Footer length:", len(footer))
else:
    print("WARNING: Could not separate footer cleanly!")

stems = {}
dups = []
for idx, q_html in enumerate(q_blocks):
    m_stem = re.search(r'<div class="stem">(.*?)</div>', q_html, re.DOTALL)
    stem = m_stem.group(1) if m_stem else ""
    c = clean_stem(stem)
    if c in stems:
        dups.append((idx + 1, stems[c], stem[:40]))
    else:
        stems[c] = idx + 1

print(f"Total raw questions: {len(q_blocks)}")
print(f"Total unique stems: {len(stems)}")
print(f"Duplicates found: {len(dups)}")
for d in dups[:10]:
    print("  Dup:", d)

needed = 700 - len(stems)
print(f"Questions needed to reach 700: {needed}")

# Let's inspect tags in local4
tags = re.findall(r'<span class="tag">([^<]+)</span>', text)
from collections import Counter
print("Tags distribution:")
for k, v in Counter(tags).most_common(10):
    print(f"  {k}: {v}")
