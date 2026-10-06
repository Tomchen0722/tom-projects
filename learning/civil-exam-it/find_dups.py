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
    # remove html tags, whitespace, punctuation
    s = re.sub(r'<[^>]+>', '', stem)
    s = re.sub(r'\s+', '', s)
    s = re.sub(r'[，。！？、：；（）\(\)\.\,\?\!\:\-\_\"\']', '', s)
    return s.strip()

print("=== CHECKING FOR DUPLICATES IN BANK FILES ===")
total_dups = 0

for bf in bank_files:
    if not os.path.exists(bf):
        print(f"File not found: {bf}")
        continue
    with open(bf, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match each question block
    # Pattern: <div class="q" data-qno="(\d+)" data-ans="([A-D])">...<div class="stem">(.*?)</div>
    questions = []
    # Use re.finditer to parse <div class="q" ...> ... </div>
    pattern = re.compile(r'<div class="q"[^>]*data-qno="([^"]+)"[^>]*data-ans="([^"]+)"[^>]*>(.*?)</div>\s*<details>', re.DOTALL)
    
    stems = defaultdict(list)
    q_count = 0
    
    # Also find stems via regex
    q_blocks = re.findall(r'<div class="q"[^>]*data-qno="(\d+)"[^>]*data-ans="([A-D])"[^>]*>.*?<div class="stem">(.*?)</div>', content, re.DOTALL)
    
    for qno, ans, stem in q_blocks:
        q_count += 1
        cleaned = clean_stem(stem)
        stems[cleaned].append((qno, stem[:60].replace('\n', ' ')))
        
    dups_in_file = {k: v for k, v in stems.items() if len(v) > 1 and len(k) > 5}
    dup_count = sum(len(v) - 1 for v in dups_in_file.values())
    total_dups += dup_count
    
    print(f"\n{bf}: {q_count} questions found. Duplicates found: {dup_count}")
    if dups_in_file:
        for k, v in list(dups_in_file.items())[:10]:
            print(f"  Duplicate ({len(v)} occurrences):")
            for qno, raw_stem in v:
                print(f"    - Q{qno}: {raw_stem}")

print(f"\nTotal duplicates across all files: {total_dups}")
