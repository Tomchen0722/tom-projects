# -*- coding: utf-8 -*-
"""patch 2：掛載 writing_plus、文章導讀加搜尋框、寫作分頁改名「完整寫作」。可重複執行。"""
import io, os

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "main.py")
s = io.open(P, encoding="utf-8").read()
changed = []

# 1) 掛載 writing_plus
if "writing_plus" not in s:
    a = ("        except Exception as _e:\n"
         "            print('extra_tabs load error:', _e)\n")
    b = a + ("        try:\n"
             "            import writing_plus\n"
             "            writing_plus.attach(self, nb)\n"
             "        except Exception as _e:\n"
             "            print('writing_plus load error:', _e)\n")
    assert a in s, "anchor1 not found"
    s = s.replace(a, b)
    changed.append("writing_plus attach")

# 2) 分頁改名
if '" ✍ 英文寫作 "' in s:
    s = s.replace('nb.add(self.tab_write, text=" ✍ 英文寫作 ")',
                  'nb.add(self.tab_write, text=" ✍ 完整寫作 ")')
    changed.append("tab rename")

# 3) 文章導讀搜尋框
if "read_search" not in s:
    a = '        self.read_list = tk.Listbox(left, font=FONT, width=32, height=22)\n'
    b = ('        self.read_search = tk.StringVar()\n'
         '        _se = ttk.Entry(left, textvariable=self.read_search, font=FONT)\n'
         '        _se.pack(fill="x", pady=(6, 0))\n'
         '        self.read_search.trace_add("write", lambda *a: self.refresh_read_list())\n'
         '        ttk.Label(left, text="↑ 搜尋文章標題", foreground="#888").pack(anchor="w")\n'
         + a)
    assert a in s, "anchor3a not found"
    s = s.replace(a, b)
    a2 = '        items = [a for a in self.articles if lv == "全部" or a.get("level") == lv]\n'
    b2 = (a2 +
          '        q = self.read_search.get().strip().lower() if hasattr(self, "read_search") else ""\n'
          '        if q:\n'
          '            items = [a for a in items if q in a["title"].lower() or q in a.get("title_zh", "")]\n')
    assert a2 in s, "anchor3b not found"
    s = s.replace(a2, b2)
    changed.append("article search")

if changed:
    io.open(P, "w", encoding="utf-8").write(s)
print("patched:", changed or "nothing (already done)")
