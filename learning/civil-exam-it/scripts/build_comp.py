# -*- coding: utf-8 -*-
"""
Builder for 02-junior/computer-bank.html to achieve exactly 700 unique questions.
"""
import re, os
from gen_comp_part1 import get_comp_part1_questions
from gen_comp_part2 import get_comp_part2_questions
from gen_comp_part3 import get_comp_part3_questions
from gen_comp_part4 import get_comp_part4_questions
from gen_comp_part5 import get_comp_part5_questions

def clean_stem(stem):
    s = re.sub(r'<[^>]+>', '', stem)
    s = re.sub(r'\(?\s*(進階題|題號)\s*\d+\s*\)?', '', s)
    s = re.sub(r'\s+', '', s)
    s = re.sub(r'[，。！？、：；（）\(\)\.\,\?\!\:\-\_\"\'\s]', '', s)
    return s.strip()

with open('02-junior/computer-bank.html', 'r', encoding='utf-8') as f:
    text = f.read()

parts = re.split(r'(?=<div class="q"\s+data-qno=)', text)
header = parts[0]
q_blocks = parts[1:]

last_block = q_blocks[-1]
m_last = re.search(r'(.*?)(</details>\s*</div>)(.*)', last_block, re.DOTALL)
if m_last:
    q_blocks[-1] = m_last.group(1) + m_last.group(2)
    footer = m_last.group(3)
else:
    raise Exception("Could not separate footer cleanly!")

unique_qs = []
seen_stems = set()

for idx, q_html in enumerate(q_blocks):
    m_stem = re.search(r'<div class="stem">(.*?)</div>', q_html, re.DOTALL)
    stem = m_stem.group(1) if m_stem else ""
    c_stem = clean_stem(stem)
    if not c_stem or c_stem in seen_stems:
        continue
    seen_stems.add(c_stem)
    unique_qs.append(q_html)

print(f"Original unique questions preserved: {len(unique_qs)}")

# Load new questions
new_questions_pool = (get_comp_part1_questions() + 
                      get_comp_part2_questions() + 
                      get_comp_part3_questions() + 
                      get_comp_part4_questions() + 
                      get_comp_part5_questions())
print(f"Total new questions available: {len(new_questions_pool)}")

new_blocks = []
for q in new_questions_pool:
    c_stem = clean_stem(q['stem'])
    if c_stem in seen_stems:
        continue
    seen_stems.add(c_stem)
    
    # format choices
    choices_html = '<div class="choices two">\n'
    for ch_letter, ch_text in q['choices']:
        choices_html += f'      <button type="button" class="ch" data-ch="{ch_letter}"><b>{ch_letter}</b><span>{ch_text}</span></button>\n'
    choices_html += '    </div>'
    
    q_html = f'''  <div class="q" data-qno="TEMP" data-ans="{q['ans']}"><span class="no">TEMP</span><span class="tag">{q['tag']}</span>
    <div class="stem">{q['stem']}</div>
    {choices_html}
    <details><summary>詳解</summary><div class="ans">
      <strong>答案：{q['ans_text']}</strong><br><br>
      {q['explanation']}
    </div></details>
  </div>\n'''
    new_blocks.append(q_html)

all_qs = unique_qs + new_blocks
print(f"Total merged questions before truncation: {len(all_qs)}")

if len(all_qs) < 700:
    raise Exception(f"Not enough questions! Have {len(all_qs)}, need 700")

all_qs = all_qs[:700]
print(f"Final questions count: {len(all_qs)}")

# Renumber questions 1 to 700 cleanly
renumbered_blocks = []
for i, q_html in enumerate(all_qs, 1):
    q_mod = re.sub(r'data-qno="[^"]+"', f'data-qno="{i}"', q_html, count=1)
    q_mod = re.sub(r'<span class="no">[^<]+</span>', f'<span class="no">{i}</span>', q_mod, count=1)
    renumbered_blocks.append(q_mod)

# Update header counts
new_header = re.sub(r'共\s*\d+\s*題', '共 700 題', header)
new_header = re.sub(r'題庫\s*\d+\s*題', '題庫 700 題', new_header)

full_output = new_header + "\n".join(renumbered_blocks) + footer

with open('02-junior/computer-bank.html', 'w', encoding='utf-8') as f:
    f.write(full_output)

print("Successfully written 700 questions to 02-junior/computer-bank.html!")
