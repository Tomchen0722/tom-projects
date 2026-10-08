import re

for fname in ['learning/twse-it/assets/notes-sysnet.js', 'learning/twse-it/assets/notes-sec.js']:
    content = open(fname, encoding='utf-8').read()
    chs = re.findall(r'["\']?chapter["\']?:\s*"([^"]+)"', content)
    titles = re.findall(r'["\']?title["\']?:\s*"([^"]+)"', content)
    print(fname, 'chapters:', len(chs))
    for i in range(len(chs)):
        print(f"  [{i+1}] {chs[i]} | {titles[i]}")
