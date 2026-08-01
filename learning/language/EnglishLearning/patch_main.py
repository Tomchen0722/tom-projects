# -*- coding: utf-8 -*-
"""把 extra_tabs 掛載程式碼插入 main.py（可重複執行，不會重複插入）。"""
import io, os

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "main.py")
src = io.open(P, encoding="utf-8").read()

MARK = "extra_tabs.attach"
if MARK in src:
    print("already patched")
else:
    old = "        self.build_write()\n"
    new = ("        self.build_write()\n"
           "        try:\n"
           "            import extra_tabs\n"
           "            extra_tabs.attach(self, nb)\n"
           "        except Exception as _e:\n"
           "            print('extra_tabs load error:', _e)\n")
    assert src.count(old) == 1, "anchor not found"
    io.open(P, "w", encoding="utf-8").write(src.replace(old, new))
    print("patched OK")
