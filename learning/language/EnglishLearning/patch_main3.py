# -*- coding: utf-8 -*-
"""patch 3：掛載 essay_tools（範文生成＋批閱）。可重複執行。"""
import io, os

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "main.py")
s = io.open(P, encoding="utf-8").read()

if "essay_tools" in s:
    print("already patched")
else:
    a = ("        except Exception as _e:\n"
         "            print('writing_plus load error:', _e)\n")
    b = a + ("        try:\n"
             "            import essay_tools\n"
             "            essay_tools.attach(self, nb)\n"
             "        except Exception as _e:\n"
             "            print('essay_tools load error:', _e)\n")
    assert a in s, "anchor not found"
    io.open(P, "w", encoding="utf-8").write(s.replace(a, b))
    print("PATCHED")
