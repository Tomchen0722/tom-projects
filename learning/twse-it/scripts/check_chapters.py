import re

for fname in ['learning/twse-it/assets/questions-sysnet.js', 'learning/twse-it/assets/questions-sec.js']:
    content = open(fname, encoding='utf-8').read()
    chs = re.findall(r'"chapter":\s*"([^"]+)"', content)
    unique_chs = []
    for c in chs:
        if c not in unique_chs:
            unique_chs.append(c)
    print(fname, 'total questions:', len(chs), 'unique chapters:', len(unique_chs))
    for i, c in enumerate(unique_chs):
        print(f'  [{i+1}] {c}')
