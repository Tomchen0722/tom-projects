# -*- coding: utf-8 -*-
"""下載開源字庫 (kajweb/dict)，產生 10000 字繁中 wordbank.json。執行一次即可。"""
import io
import json
import os
import re
import zipfile
import urllib.request

from opencc import OpenCC

CC = OpenCC("s2twp")
BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "wordbank.json")
TARGET_TOTAL = 10000

RAW = "https://raw.githubusercontent.com/kajweb/dict/master/book/"
BOOKS = [  # (level, zip)
    ("初級", "1521164669076_ChuZhongluan_2.zip"),   # 中考 1420
    ("初級", "1521164675301_GaoZhong_2.zip"),        # 高考 3668
    ("中級", "1524052539052_CET4luan_2.zip"),        # 四級 3739
    ("中級", "1524052554766_CET6_2.zip"),            # 六級 2078
    ("進階", "1521164654696_KaoYan_2.zip"),          # 考研 4533
    ("進階", "1521164657744_IELTS_2.zip"),
    ("進階", "1521164626760_BEC_2.zip"),
    ("進階", "1521164640451_TOEFL_2.zip"),
    ("進階", "1521164637271_GRE_2.zip"),           # 雅思 3427
]

WORD_RE = re.compile(r"^[A-Za-z][A-Za-z\-' .]*$")


def fetch_jsonl(url):
    print("downloading", url)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    data = urllib.request.urlopen(req, timeout=180).read()
    zf = zipfile.ZipFile(io.BytesIO(data))
    name = [n for n in zf.namelist() if n.endswith(".json")][0]
    text = zf.read(name).decode("utf-8", errors="replace")
    for line in text.splitlines():
        line = line.strip()
        if line:
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def extract(entry):
    w = entry.get("headWord", "").strip()
    if not w or not WORD_RE.match(w) or len(w) > 30:
        return None
    c = entry.get("content", {}).get("word", {}).get("content", {})
    phone = c.get("usphone") or c.get("ukphone") or ""
    ipa = f"/{phone}/" if phone and not phone.startswith("/") else (phone or "")
    trans = c.get("trans") or []
    zh_parts, pos_parts = [], []
    for t in trans[:2]:
        cn = (t.get("tranCn") or "").strip()
        if cn:
            zh_parts.append(CC.convert(cn))
        p = (t.get("pos") or "").strip()
        if p and p not in pos_parts:
            pos_parts.append(p)
    if not zh_parts:
        return None
    examples = []
    for s in (c.get("sentence", {}).get("sentences") or [])[:2]:
        en = (s.get("sContent") or "").strip()
        cn = (s.get("sCn") or "").strip()
        if en and cn:
            examples.append({"en": en, "zh": CC.convert(cn)})
    return {
        "word": w,
        "ipa": ipa,
        "pos": ("/".join(p + "." if not p.endswith(".") else p for p in pos_parts) or "—"),
        "zh": "；".join(zh_parts),
        "examples": examples,
    }


def main():
    bank = {"初級": [], "中級": [], "進階": []}
    seen = set()
    total = 0
    for level, zname in BOOKS:
        count = 0
        for entry in fetch_jsonl(RAW + zname):
            if total >= TARGET_TOTAL:
                break
            item = extract(entry)
            if not item:
                continue
            key = item["word"].lower()
            if key in seen:
                continue
            seen.add(key)
            bank[level].append(item)
            count += 1
            total += 1
        print(level, zname, "+", count, "words, total", total)
        if total >= TARGET_TOTAL:
            break
    if os.path.exists(OUT):
        os.replace(OUT, OUT + ".bak")
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(bank, f, ensure_ascii=False)
    with_ex = sum(1 for v in bank.values() for w in v if w["examples"])
    print("DONE total", total, "with_examples", with_ex,
          {k: len(v) for k, v in bank.items()})


if __name__ == "__main__":
    main()
