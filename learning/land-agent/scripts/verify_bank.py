import json

with open(r'c:\AI\tom-projects\learning\land-agent\assets\questions-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

prefix = 'window.QUESTION_BANK = '
idx = text.find(prefix)
json_str = text[idx + len(prefix):].rstrip(';\n ')
data = json.loads(json_str)

print('Total questions:', len(data))
assert len(data) == 600, f'Expected 600, got {len(data)}'

cats = {}
for q in data:
    cats[q['category']] = cats.get(q['category'], 0) + 1
    for k in ['id', 'question', 'options', 'answer', 'law', 'explanation', 'trap']:
        assert k in q, f"Missing {k} in {q.get('id')}"
    assert len(q['options']) == 4, f"Options count != 4 in {q['id']}"
    assert q['answer'] in ['A', 'B', 'C', 'D'], f"Invalid answer in {q['id']}"

for c, count in sorted(cats.items()):
    print(f'  {c}: {count}')
print('Verification PASSED! All 600 questions are valid, complete and structured.')
