# -*- coding: utf-8 -*-
import io
p = "build_wordbank.py"
s = io.open(p, encoding="utf-8").read()
anchor = '("進階", "1521164657744_IELTS_2.zip"),'
extra = (anchor +
         '\n    ("進階", "1521164626760_BEC_2.zip"),'
         '\n    ("進階", "1521164640451_TOEFL_2.zip"),'
         '\n    ("進階", "1521164637271_GRE_2.zip"),')
if "1521164640451" in s:
    print("already patched")
else:
    assert anchor in s, "anchor not found"
    io.open(p, "w", encoding="utf-8").write(s.replace(anchor, extra))
    print("PATCHED")
