import sys, re, os

def verify_file(filepath, expected_count=700):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return False
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    q_matches = re.findall(r'<div class="q"[^>]*data-qno="([^"]+)"[^>]*data-ans="([^"]+)"', content)
    total_q = len(q_matches)
    
    stems = {}
    dups = []
    
    stem_matches = re.findall(r'<div class="stem">(.*?)</div>', content, re.DOTALL)
    for idx, raw_stem in enumerate(stem_matches):
        c = re.sub(r'<[^>]+>', '', raw_stem)
        c = re.sub(r'\(?\s*(進階題|題號)\s*\d+\s*\)?', '', c)
        c = re.sub(r'\s+', '', c)
        c = re.sub(r'[，。！？、：；（）\(\)\.\,\?\!\:\-\_\"\'\s]', '', c)
        if c in stems:
            dups.append((idx + 1, stems[c], raw_stem[:40]))
        else:
            stems[c] = idx + 1
            
    print(f"=== VERIFYING {filepath} ===")
    print(f"Total questions: {total_q} (Expected: {expected_count})")
    print(f"Total unique stems: {len(stems)}")
    print(f"Duplicates: {len(dups)}")
    
    # Check numbering
    qnos = [m[0] for m in q_matches]
    try:
        int_qnos = [int(q) for q in qnos]
        is_seq = int_qnos == list(range(1, expected_count + 1))
        print(f"Is sequential 1..{expected_count}: {is_seq}")
    except Exception as e:
        print(f"Failed to parse qnos as integers: {e}")
        is_seq = False
        
    if total_q == expected_count and len(dups) == 0 and is_seq:
        print(">>> VERIFICATION PASSED! PERFECT! <<<")
        return True
    else:
        print(">>> VERIFICATION FAILED! <<<")
        return False

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else '05-common/law-bank.html'
    verify_file(target)
