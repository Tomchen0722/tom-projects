import re
from collections import Counter

with open('assets/questions-sec.js', 'r', encoding='utf-8') as f:
    text = f.read()

subtopics = re.findall(r'"subtopic":\s*"([^"]+)"', text)
counts = Counter(subtopics)
for sub, count in sorted(counts.items()):
    print(f"{sub}: {count} 題")
