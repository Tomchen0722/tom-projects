# -*- coding: utf-8 -*-
import io
p = "generate_articles.py"
s = io.open(p, encoding="utf-8").read()
anchor = """        if count < PER_TEMPLATE:
            print("WARN", tmpl.__name__, "only", count)
"""
extra = anchor + """
    # 不足 1980 篇時，用其他模板補足
    tries = 0
    while len(generated) < 1980 and tries < 400000:
        tries += 1
        art = rng.choice(TEMPLATES)(rng)
        key = json.dumps([p["en"] for p in art["paragraphs"]], ensure_ascii=False)
        if key in seen:
            continue
        seen.add(key)
        art["source"] = "生成"
        generated.append(art)
"""
if "用其他模板補足" in s:
    print("already patched")
else:
    assert anchor in s, "anchor not found"
    io.open(p, "w", encoding="utf-8").write(s.replace(anchor, extra))
    print("PATCHED")
