# -*- coding: utf-8 -*-
"""把 newq/*.json 的新題目合併進 questions_data.json（含驗證與去重）。"""
import json, glob, os, re, sys, shutil, unicodedata

BASE = os.path.dirname(os.path.abspath(__file__))
MAIN = os.path.join(BASE, 'questions_data.json')
LABELS = {
    ('beginner', 's1'): '初級 - 科目一：人工智慧基礎概論',
    ('beginner', 's2'): '初級 - 科目二：生成式 AI 應用與規劃',
    ('intermediate', 's1'): '中級 - 科目一：AI 技術應用與規劃',
    ('intermediate', 's2'): '中級 - 科目二：大數據處理分析與應用',
    ('intermediate', 's3'): '中級 - 科目三：機器學習技術與應用',
}

def norm(s):
    s = unicodedata.normalize('NFKC', s or '')
    return re.sub(r'[\s，。、（）()「」【】,.:：;；?？!！-]', '', s).lower()

def main(apply=True):
    data = json.load(open(MAIN, encoding='utf-8'))
    seen = {}
    for lvl in data:
        for q in data[lvl]:
            seen[norm(q.get('scenario', '') + q['stem'])] = 'existing'
            seen.setdefault('STEM:' + norm(q['stem']), 'existing')

    added, errors, dups = 0, [], []
    for path in sorted(glob.glob(os.path.join(BASE, 'newq', '*.json'))):
        items = json.load(open(path, encoding='utf-8'))
        fn = os.path.basename(path)
        for i, q in enumerate(items):
            tag = '%s#%d' % (fn, i + 1)
            lvl = q.get('level')
            if (lvl, q.get('subject')) not in LABELS:
                errors.append('%s 科目/等級錯誤' % tag); continue
            if len(q.get('options', [])) != 4 or len(q.get('explanations', [])) != 4:
                errors.append('%s 選項或解析數量不是 4' % tag); continue
            if not isinstance(q.get('answer'), int) or not 0 <= q['answer'] <= 3:
                errors.append('%s answer 索引錯誤' % tag); continue
            if '✅' not in q['explanations'][q['answer']]:
                errors.append('%s 正解解析缺少 ✅ 標記' % tag); continue
            if not q.get('scenario'):
                errors.append('%s 缺少 scenario（情境題必填）' % tag); continue
            if len(set(q['options'])) != 4:
                errors.append('%s 選項有重複' % tag); continue
            key = norm(q['scenario'] + q['stem'])
            if key in seen:
                dups.append('%s 與 %s 重複' % (tag, seen[key])); continue
            seen[key] = tag
            out = {
                'subject': q['subject'],
                'subjectLabel': LABELS[(lvl, q['subject'])],
                'scenario': q['scenario'],
                'stem': q['stem'],
                'options': q['options'],
                'answer': q['answer'],
                'explanations': q['explanations'],
            }
            data[lvl].append(out)
            added += 1

    print('新增 %d 題' % added)
    if dups:
        print('--- 重複 %d 題 ---' % len(dups))
        for d in dups[:40]: print(' ', d)
    if errors:
        print('--- 錯誤 %d 題 ---' % len(errors))
        for e in errors[:40]: print(' ', e)
        print('有錯誤，未寫入。')
        return 1
    if apply and added:
        shutil.copy(MAIN, MAIN + '.prev')
        json.dump(data, open(MAIN, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    for lvl in data:
        from collections import Counter
        print(lvl, len(data[lvl]), dict(Counter(q['subject'] for q in data[lvl])))
    return 0

if __name__ == '__main__':
    sys.exit(main(apply='--dry' not in sys.argv))
