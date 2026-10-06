import glob, os, re

files = glob.glob('**/*.html', recursive=True)

# Count question banks
bank_files = [f for f in files if 'bank' in f or 'mock' in f]
print("=== BANK FILES & QUESTION COUNTS ===")
total_questions = 0
for bf in sorted(bank_files):
    with open(bf, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    # Find all question blocks
    q_matches = re.findall(r'<div class="q"[^>]*data-ans="([^"]+)"', content)
    # Also find any essay questions if any
    essay_matches = re.findall(r'class="q"[^>]*data-essay', content)
    print(f"{bf}: {len(q_matches)} 選擇題, {len(essay_matches)} 申論題")
    total_questions += len(q_matches)

print(f"Total MC questions: {total_questions}")

# Check all occurrences of light colors in CSS and HTML
print("\n=== LIGHT COLOR OCCURRENCES IN HTML/CSS ===")
color_counts = {}
for fpath in files + glob.glob('**/*.css', recursive=True):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    matches = re.findall(r'color\s*:\s*([^;}"\'>]+)', content)
    for m in matches:
        val = m.strip().lower()
        if any(c in val for c in ['#64748b', '#94a3b8', '#9ca3af', '#cbd5e1', '#6b7280', '#4b5563', '#999', '#888', '#aaa', '#bbb', '#ccc', 'gray', 'grey']):
            color_counts[val] = color_counts.get(val, 0) + 1

for val, count in sorted(color_counts.items(), key=lambda x: -x[1]):
    print(f"{val}: {count} times")
