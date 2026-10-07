# -*- coding: utf-8 -*-
import re

def clean_stem(stem):
    s = re.sub(r'<[^>]+>', '', stem)
    s = re.sub(r'\(?\s*(進階題|題號)\s*\d+\s*\)?', '', s)
    s = re.sub(r'\s+', '', s)
    s = re.sub(r'[，。！？、：；（）\(\)\.\,\?\!\:\-\_\"\'\s]', '', s)
    return s.strip()

with open('02-junior/net-bank.html', 'r', encoding='utf-8') as f:
    text = f.read()

parts = re.split(r'(?=<div class="q"\s+data-qno=)', text)
header = parts[0]
q_blocks = parts[1:]

seen = set()
unique = []
dups = []

for idx, q_html in enumerate(q_blocks):
    m_stem = re.search(r'<div class="stem">(.*?)</div>', q_html, re.DOTALL)
    stem = m_stem.group(1) if m_stem else ""
    c_stem = clean_stem(stem)
    if c_stem in seen:
        dups.append((idx + 1, stem[:40]))
    else:
        seen.add(c_stem)
        unique.append(q_html)

print(f"Total question blocks in 02-junior/net-bank.html: {len(q_blocks)}")
print(f"Duplicates: {len(dups)}")
print(f"Unique questions preserved: {len(unique)}")
print(f"Needed to reach 700: {700 - len(unique)}")
