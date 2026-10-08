import json, re

with open('assets/questions-sec.js', 'r', encoding='utf-8') as f:
    text = f.read()

# find all items where chapter is Chapter 2
# Let's parse items using regex or json
blocks = re.findall(r'\{\s*"id":\s*(\d+).*?"chapter":\s*"([^"]+)".*?"subtopic":\s*"([^"]+)".*?"question":\s*"([^"]+)"', text, re.DOTALL)
print(f"Found {len(blocks)} questions")
ch2 = [b for b in blocks if "第 2 章" in b[1]]
print(f"Chapter 2 has {len(ch2)} questions:")
for q_id, ch, sub, q_text in ch2[:15]:
    print(f"[{q_id}] {sub} -> {q_text[:40]}...")
