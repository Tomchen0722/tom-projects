# -*- coding: utf-8 -*-
"""
Fix inline pre styles across HTML files so that all code snippets render
with high-contrast dark theme or explicit high-contrast text.
"""
import os

files_to_fix = [
    '02-junior/prog-bank.html',
    '01-senior3/db-bank.html',
    '02-junior/net-bank.html',
    '01-senior3/net-bank.html',
    '01-senior3/ds-bank.html'
]

replacements = [
    ('style="background:#f8fafc;border:1px solid #cbd5e1;padding:12px;border-radius:8px;font-family:Consolas,monospace;line-height:1.6;"', ''),
    ('style="background:#f8fafc;border:1px solid #cbd5e1;padding:12px;border-radius:8px;font-family:Consolas,monospace;"', ''),
    ('style="background:#f8fafc;padding:8px;border-radius:6px;font-family:Consolas,monospace;"', ''),
    ('style="background:#f8fafc;padding:10px;border-radius:6px;font-family:Consolas,monospace;margin-top:6px;"', ''),
    ('style="background:#f8fafc;border-left:4px solid #3b82f6;padding:10px;font-family:Consolas,monospace;font-size:.88rem;line-height:1.7;"', ''),
    ('style="background:#f8fafc;border-left:4px solid #ef4444;padding:10px;font-family:Consolas,monospace;font-size:.88rem;line-height:1.7;"', ''),
    ('style="background:#f1f5f9;border-left:4px solid #3b82f6;padding:10px 14px;border-radius:6px;font-family:Consolas,monospace;font-size:.9rem;line-height:1.7;"', ''),
    ('style="background:#fee2e2;border:1px solid #f87171;padding:8px;border-radius:6px;font-family:Consolas,monospace;"', 'style="background:#fef2f2;border:1.5px solid #ef4444;color:#991b1b;font-weight:700;padding:12px 16px;border-radius:8px;font-family:Consolas,monospace;line-height:1.7;"')
]

for fpath in files_to_fix:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    orig_text = text
    count = 0
    for old_s, new_s in replacements:
        if old_s in text:
            occurrences = text.count(old_s)
            count += occurrences
            text = text.replace(old_s, new_s)
    
    # Clean up <pre > to <pre>
    text = text.replace('<pre >', '<pre>')
    text = text.replace('<pre  >', '<pre>')

    if text != orig_text:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Fixed {count} pre tags in {fpath}")
    else:
        print(f"No changes needed in {fpath}")

print("Pre contrast fix completed!")
