import glob, re, os

banks = [
    '05-common/law-bank.html',
    '05-common/english-bank.html',
    '01-senior3/ds-bank.html',
    '01-senior3/db-bank.html',
    '01-senior3/net-bank.html',
    '01-senior3/mis-bank.html',
    '02-junior/computer-bank.html',
    '02-junior/net-bank.html',
    '02-junior/prog-bank.html',
    '03-local3/bank.html',
    '04-local4/bank.html',
]

print(f"{'Target Bank':<32} | {'Count':<6} | {'Status'}")
print("-" * 55)

for b in banks:
    if not os.path.exists(b):
        continue
    with open(b, 'r', encoding='utf-8') as f:
        content = f.read()
    q_matches = re.findall(r'<div class="q"[^>]*data-qno="([^"]+)"[^>]*data-ans="([^"]+)"', content)
    count = len(q_matches)
    status = "DONE (700 題達標)" if count == 700 else f"剩餘需補 {700 - count} 題"
    print(f"{b:<32} | {count:<6} | {status}")
