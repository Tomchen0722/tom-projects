import re

content = open('learning/twse-it/assets/essay-data.js', encoding='utf-8').read()
ids = re.findall(r'["\']?id["\']?:\s*"([^"]+)"', content)
titles = re.findall(r'["\']?title["\']?:\s*"([^"]+)"', content)
cats = re.findall(r'["\']?category["\']?:\s*"([^"]+)"', content)
pts = re.findall(r'["\']?points["\']?:\s*(\d+)', content)
print(f"Counts: ids={len(ids)}, titles={len(titles)}, cats={len(cats)}, pts={len(pts)}")
for i in range(len(ids)):
    p = pts[i] if i < len(pts) else "MISSING"
    print(f"  [{i+1}] {cats[i]} | {ids[i]} | pts={p} | {titles[i][:20]}")
