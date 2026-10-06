import re, os

def clean_stem(stem):
    s = re.sub(r'<[^>]+>', '', stem)
    s = re.sub(r'\(?\s*(進階題|題號)\s*\d+\s*\)?', '', s)
    s = re.sub(r'\s+', '', s)
    s = re.sub(r'[，。！？、：；（）\(\)\.\,\?\!\:\-\_\"\'\s]', '', s)
    return s.strip()

with open('05-common/law-bank.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern to extract question blocks
# Each question block begins with <div class="q" ...> and ends with </div> (closing details) and </div> (closing .q)
# Let's split by <div class="q"
parts = re.split(r'(?=<div class="q"\s+data-qno=)', text)
header = parts[0]
q_blocks = parts[1:]

print(f"Header length: {len(header)}")
print(f"Total q_blocks: {len(q_blocks)}")

# The last q_block also contains trailing cards, footer, scripts.
# Let's separate the last question from the footer.
last_block = q_blocks[-1]
# A question block ends after </details>\s*</div>
m_last = re.search(r'(.*?)(</details>\s*</div>)(.*)', last_block, re.DOTALL)
if m_last:
    q_blocks[-1] = m_last.group(1) + m_last.group(2)
    footer = m_last.group(3)
else:
    print("Could not separate footer from last question!")
    footer = ""

print(f"Footer length: {len(footer)}")

parsed_qs = []
seen_stems = {}
dups = []

for idx, q_html in enumerate(q_blocks):
    # Extract qno, ans
    m_q = re.search(r'<div class="q"[^>]*data-qno="([^"]+)"[^>]*data-ans="([^"]+)"', q_html)
    if not m_q:
        print(f"Block {idx} failed to match data-qno/data-ans")
        continue
    qno = m_q.group(1)
    ans = m_q.group(2)
    
    m_stem = re.search(r'<div class="stem">(.*?)</div>', q_html, re.DOTALL)
    stem = m_stem.group(1) if m_stem else ""
    c_stem = clean_stem(stem)
    
    if c_stem in seen_stems:
        dups.append((qno, seen_stems[c_stem], stem[:40]))
    else:
        seen_stems[c_stem] = qno
        parsed_qs.append({
            'orig_qno': qno,
            'ans': ans,
            'stem': stem,
            'clean_stem': c_stem,
            'html': q_html
        })

print(f"Unique questions parsed: {len(parsed_qs)}")
print(f"Duplicates removed: {len(dups)}")
