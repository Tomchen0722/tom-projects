# -*- coding: utf-8 -*-
import sys, re, os

def inspect(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    parts = re.split(r'(?=<div class="q"\s+data-qno=)', text)
    header = parts[0]
    q_blocks = parts[1:]
    
    print(f"File: {path}")
    print(f"Total q_blocks: {len(q_blocks)}")
    
    # Check if footer cleanly splits
    if q_blocks:
        last = q_blocks[-1]
        m = re.search(r'(.*?)(</details>\s*</div>)(.*)', last, re.DOTALL)
        if m:
            print(f"Footer found, length: {len(m.group(3))}")
        else:
            print("Footer split not matched directly!")
            
    # Stems
    stems = set()
    dups = 0
    for q in q_blocks:
        m = re.search(r'<div class="stem">(.*?)</div>', q, re.DOTALL)
        if m:
            raw = m.group(1)
            c = re.sub(r'<[^>]+>', '', raw)
            c = re.sub(r'\(?\s*(進階題|題號)\s*\d+\s*\)?', '', c)
            c = re.sub(r'\s+', '', c)
            c = re.sub(r'[，。！？、：；（）\(\)\.\,\?\!\:\-\_\"\'\s]', '', c)
            if c in stems:
                dups += 1
            else:
                stems.add(c)
    print(f"Unique stems: {len(stems)}, Duplicates: {dups}")

if __name__ == '__main__':
    inspect(sys.argv[1] if len(sys.argv)>1 else '01-senior3/ds-bank.html')
