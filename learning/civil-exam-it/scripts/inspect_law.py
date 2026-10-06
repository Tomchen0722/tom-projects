import re

with open('05-common/law-bank.html', 'r', encoding='utf-8') as f:
    text = f.read()

sections = re.findall(r'<div class="card"><h3>(.*?)</h3></div>', text)
print("Sections:")
for s in sections:
    print(" -", s)

# Check all question blocks
# A question block starts with <div class="q" and ends before the next <div class="q" or <div class="card"> or </div>\s*</div> (container)
q_matches = list(re.finditer(r'<div class="q"[^>]*data-qno="([^"]+)"[^>]*data-ans="([^"]+)"', text))
print(f"Total q tags: {len(q_matches)}")
