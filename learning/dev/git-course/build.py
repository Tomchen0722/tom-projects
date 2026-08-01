# -*- coding: utf-8 -*-
"""
Git 企業級教材 - 靜態網站產生器
================================
執行方式：
    python build.py

會把整套教材輸出成純 HTML 檔案到 ./site/ 資料夾，
直接用瀏覽器開啟 site/index.html 即可閱讀，不需安裝任何套件、不需開伺服器。
"""
import os
import re
import html
import shutil
import importlib

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "site")

# ---------------------------------------------------------------------------
# 1. 迷你 Markdown 轉換器（自製，零相依套件）
# ---------------------------------------------------------------------------
# 支援語法：
#   ## / ### / #### 標題
#   ```lang ... ```  程式碼區塊（含複製按鈕）
#   `inline code`     行內程式碼
#   **粗體**
#   - 項目 / 1. 編號   清單
#   > 引言
#   | 表格 |
#   ---               分隔線
#   :::tip / :::warn / :::danger / :::rescue / :::story / :::vscode  提示框
#   [文字](網址)      連結

CALLOUTS = {
    "tip":    ("callout tip",    "💡 觀念重點"),
    "warn":   ("callout warn",   "⚠️ 注意"),
    "danger": ("callout danger", "🚨 危險操作"),
    "rescue": ("callout rescue", "🛟 救援方法"),
    "story":  ("callout story",  "🎬 實戰情境"),
    "vscode": ("callout vscode", "🖱️ VS Code 圖形操作"),
    "best":   ("callout best",   "🏢 公司最佳實務"),
}


def _inline(text):
    """處理行內語法：先保護行內程式碼，再處理粗體與連結。"""
    # 先抽出行內程式碼，用佔位符保護，避免內部字元被再次處理
    spans = []

    def _stash(m):
        spans.append(m.group(1))
        return "\x00%d\x00" % (len(spans) - 1)

    text = re.sub(r"`([^`]+)`", _stash, text)
    text = html.escape(text, quote=False)
    # 粗體
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    # 連結
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                  r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    # 還原行內程式碼
    def _pop(m):
        return "<code>%s</code>" % html.escape(spans[int(m.group(1))], quote=False)
    text = re.sub(r"\x00(\d+)\x00", _pop, text)
    return text


def render(md):
    """把迷你 Markdown 字串轉成 HTML。"""
    lines = md.split("\n")
    out = []
    i = 0
    n = len(lines)

    def close_list(stack):
        while stack:
            out.append("</%s>" % stack.pop())

    list_stack = []  # 目前開啟的清單標籤

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # 程式碼區塊
        if stripped.startswith("```"):
            close_list(list_stack)
            lang = stripped[3:].strip() or "bash"
            code = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1  # 跳過結尾 ```
            code_html = html.escape("\n".join(code), quote=False)
            out.append(
                '<div class="codewrap" data-lang="%s">'
                '<button class="copybtn" onclick="copyCode(this)">複製</button>'
                '<pre><code>%s</code></pre></div>' % (html.escape(lang), code_html)
            )
            continue

        # 提示框 :::key
        m = re.match(r":::(\w+)\s*(.*)$", stripped)
        if m and m.group(1) in CALLOUTS:
            close_list(list_stack)
            key = m.group(1)
            cls, label = CALLOUTS[key]
            inline_title = m.group(2).strip()
            block = []
            i += 1
            while i < n and lines[i].strip() != ":::":
                block.append(lines[i])
                i += 1
            i += 1  # 跳過結尾 :::
            head = label if not inline_title else "%s — %s" % (label, inline_title)
            out.append('<div class="%s"><div class="callout-head">%s</div><div class="callout-body">%s</div></div>'
                       % (cls, html.escape(head), render("\n".join(block))))
            continue

        # 空行
        if stripped == "":
            close_list(list_stack)
            i += 1
            continue

        # 分隔線
        if stripped == "---":
            close_list(list_stack)
            out.append("<hr>")
            i += 1
            continue

        # 標題
        m = re.match(r"(#{2,4})\s+(.*)$", stripped)
        if m:
            close_list(list_stack)
            level = len(m.group(1))
            text = _inline(m.group(2))
            anchor = re.sub(r"[^\w一-鿿]+", "-", m.group(2).strip()).strip("-")
            out.append('<h%d id="%s">%s</h%d>' % (level, anchor, text, level))
            i += 1
            continue

        # 引言
        if stripped.startswith(">"):
            close_list(list_stack)
            quote = []
            while i < n and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            out.append("<blockquote>%s</blockquote>" % _inline(" ".join(quote)))
            continue

        # 表格
        if "|" in line and i + 1 < n and re.match(r"^\s*\|?[\s:|-]+\|?\s*$", lines[i + 1]):
            close_list(list_stack)
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            i += 2  # 跳過分隔列
            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            thead = "".join("<th>%s</th>" % _inline(c) for c in header)
            tbody = ""
            for r in rows:
                tbody += "<tr>" + "".join("<td>%s</td>" % _inline(c) for c in r) + "</tr>"
            out.append('<div class="tablewrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
                       % (thead, tbody))
            continue

        # 清單（支援縮排巢狀）
        m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", line)
        if m:
            indent = len(m.group(1))
            ordered = not (m.group(2) in ("-", "*"))
            tag = "ol" if ordered else "ul"
            # 依縮排調整清單堆疊
            depth = indent // 2
            while len(list_stack) > depth + 1:
                out.append("</%s>" % list_stack.pop())
            if len(list_stack) < depth + 1:
                out.append("<%s>" % tag)
                list_stack.append(tag)
            out.append("<li>%s</li>" % _inline(m.group(3)))
            i += 1
            continue

        # 一般段落
        close_list(list_stack)
        para = [line]
        i += 1
        while i < n and lines[i].strip() and not re.match(r"^\s*([-*]|\d+\.|#{2,4}|>|```|:::|\|)", lines[i].strip()):
            para.append(lines[i])
            i += 1
        out.append("<p>%s</p>" % _inline(" ".join(s.strip() for s in para)))

    close_list(list_stack)
    return "\n".join(out)


# ---------------------------------------------------------------------------
# 2. 頁面模板
# ---------------------------------------------------------------------------
def sidebar_html(lessons, active_id=None):
    parts = []
    current_part = None
    for L in lessons:
        if L["part"] != current_part:
            if current_part is not None:
                parts.append("</ul></div>")
            current_part = L["part"]
            parts.append('<div class="nav-group"><div class="nav-part">%s</div><ul>' % html.escape(current_part))
        cls = ' class="active"' if L["id"] == active_id else ""
        parts.append('<li%s><a href="lesson-%s.html"><span class="nav-num">%s</span>%s</a></li>'
                     % (cls, L["id"], L["id"], html.escape(L["title"])))
    parts.append("</ul></div>")
    return "\n".join(parts)


PAGE = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<button id="menuToggle" onclick="toggleNav()" aria-label="選單">☰</button>
<nav id="sidebar">
  <a class="brand" href="index.html">
    <span class="brand-logo">⎇</span>
    <span class="brand-text"><b>Git 企業級教材</b><small>從零到公司實戰</small></span>
  </a>
  <div class="nav-scroll">
  <div class="nav-group"><div class="nav-part">開始</div><ul>
    <li{home_active}><a href="index.html"><span class="nav-num">★</span>課程首頁</a></li>
    <li{cheat_active}><a href="cheatsheet.html"><span class="nav-num">⌘</span>指令速查單頁</a></li>
  </ul></div>
  {sidebar}
  </div>
  <button class="theme-toggle" onclick="toggleTheme()">🌓 切換深/淺色</button>
</nav>
<div id="overlay" onclick="toggleNav()"></div>
<main>
<div class="content">
{content}
</div>
{pager}
<footer>Git 企業級教材 · 用 Python 產生的純靜態網站 · 可自由離線閱讀</footer>
</main>
<script src="assets/script.js"></script>
<!-- TOM_HUB_RETURN：由 Project Hub 注入的返回按鈕。單獨開啟本教材時載入失敗會自動略過，不影響閱讀。 -->
<script src="http://127.0.0.1:7000/shared/hub-return.js" defer></script>
</body>
</html>"""


def pager_html(lessons, idx):
    prev_l = lessons[idx - 1] if idx > 0 else None
    next_l = lessons[idx + 1] if idx < len(lessons) - 1 else None
    left = ('<a class="pg pg-prev" href="lesson-%s.html"><small>← 上一課</small><span>%s</span></a>'
            % (prev_l["id"], html.escape(prev_l["title"]))) if prev_l else '<span class="pg pg-empty"></span>'
    right = ('<a class="pg pg-next" href="lesson-%s.html"><small>下一課 →</small><span>%s</span></a>'
             % (next_l["id"], html.escape(next_l["title"]))) if next_l else '<a class="pg pg-next" href="index.html"><small>回到 →</small><span>課程首頁</span></a>'
    return '<div class="pager">%s%s</div>' % (left, right)


def quiz_html(lesson_id):
    """依課程 id 產生「自我檢核 + 動手練習」區塊。"""
    try:
        from content_quiz import QUIZ
    except Exception:
        return ""
    q = QUIZ.get(lesson_id)
    if not q:
        return ""
    parts = ['<div class="quiz">']
    checks = q.get("check", [])
    if checks:
        parts.append('<h2 class="quiz-title">🧠 自我檢核</h2>')
        parts.append('<p class="quiz-hint">先自己想過答案，再點開對照。答得出來代表這一課掌握了。</p>')
        for i, (question, answer) in enumerate(checks, 1):
            parts.append(
                '<details class="qa"><summary><span class="qnum">Q%d</span>%s</summary>'
                '<div class="qa-body">%s</div></details>'
                % (i, html.escape(question), render(answer))
            )
    practice = q.get("practice", [])
    if practice:
        parts.append('<h2 class="quiz-title">⌨️ 動手練習</h2>')
        parts.append('<p class="quiz-hint">建議開一個測試用資料夾實際操作，做錯也不怕（你已經學過怎麼救）。</p>')
        parts.append('<ol class="practice-list">')
        for task in practice:
            parts.append("<li>%s</li>" % render(task).replace("<p>", "").replace("</p>", ""))
        parts.append("</ol>")
    parts.append("</div>")
    return "\n".join(parts)


def lesson_page(lessons, idx):
    L = lessons[idx]
    body = render(L["body"])
    header = (
        '<div class="lesson-head">'
        '<div class="lesson-part">%s</div>'
        '<h1>第 %s 課 · %s</h1>'
        '<p class="lesson-sub">%s</p>'
        '</div>' % (html.escape(L["part"]), L["id"].lstrip("0") or L["id"],
                    html.escape(L["title"]), html.escape(L.get("subtitle", "")))
    )
    content = header + body + quiz_html(L["id"])
    return PAGE.format(
        title="第 %s 課 %s｜Git 企業級教材" % (L["id"], L["title"]),
        sidebar=sidebar_html(lessons, L["id"]),
        home_active="",
        cheat_active="",
        content=content,
        pager=pager_html(lessons, idx),
    )


def index_page(lessons):
    cards = []
    current_part = None
    for L in lessons:
        if L["part"] != current_part:
            if current_part is not None:
                cards.append("</div>")
            current_part = L["part"]
            cards.append('<h2 class="part-title">%s</h2><div class="card-grid">' % html.escape(current_part))
        cards.append(
            '<a class="lesson-card" href="lesson-%s.html">'
            '<div class="card-num">%s</div>'
            '<div class="card-body"><b>%s</b><small>%s</small></div></a>'
            % (L["id"], L["id"], html.escape(L["title"]), html.escape(L.get("subtitle", "")))
        )
    cards.append("</div>")

    hero = """
<div class="hero">
  <div class="hero-badge">完全初學者 → 企業級開發者</div>
  <h1>Git &amp; GitHub 企業級實戰教材</h1>
  <p class="hero-sub">20 堂課，從「Git 是什麼」一路帶到公司真正在用的分支流程、Code Review、CI/CD 與事故救援。每一課都用 <b>Tom、Alice、Bob</b> 三人協作情境，教你原理、指令、VS Code 圖形操作、公司最佳實務，以及「做錯了怎麼救」。</p>
  <div class="hero-facts">
    <div><b>20</b><small>完整課程</small></div>
    <div><b>6</b><small>每課段落</small></div>
    <div><b>3</b><small>協作角色</small></div>
    <div><b>0</b><small>需安裝套件</small></div>
  </div>
  <a class="hero-cta" href="lesson-01.html">從第 1 課開始 →</a>
</div>
<div class="learn-goals">
  <h2>學完你將能夠</h2>
  <ul class="goal-list">
    <li>✅ 獨立使用 Git 與 GitHub 開發專案</li>
    <li>✅ 理解多人協作流程，不怕 Merge Conflict</li>
    <li>✅ 用 Branch、Pull Request、Code Review 完成企業級開發</li>
    <li>✅ 知道何時該用 Merge、Rebase、Stash、Cherry-pick、Revert</li>
    <li>✅ 處理大部分 Git 常見事故，不必每次都上網搜尋</li>
    <li>✅ 適應大多數軟體公司的 Git 工作流程</li>
  </ul>
</div>
"""
    content = hero + "\n".join(cards)
    return PAGE.format(
        title="Git 企業級教材｜從零到公司實戰",
        sidebar=sidebar_html(lessons, None),
        home_active=' class="active"',
        cheat_active="",
        content=content,
        pager="",
    )


def cheatsheet_page(lessons):
    from content_cheatsheet import CHEATSHEET
    content = '<div class="lesson-head"><div class="lesson-part">隨手速查</div><h1>Git 指令速查單頁</h1><p class="lesson-sub">最常用的指令一頁掌握，按用途分組。找不到就用瀏覽器搜尋 Ctrl+F。</p></div>'
    content += render(CHEATSHEET)
    return PAGE.format(
        title="Git 指令速查單頁｜Git 企業級教材",
        sidebar=sidebar_html(lessons, None),
        home_active="",
        cheat_active=' class="active"',
        content=content,
        pager="",
    )


# ---------------------------------------------------------------------------
# 3. 靜態資源（CSS / JS）
# ---------------------------------------------------------------------------
def write_assets():
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    with open(os.path.join(OUT, "assets", "style.css"), "w", encoding="utf-8") as f:
        f.write(CSS)
    with open(os.path.join(OUT, "assets", "script.js"), "w", encoding="utf-8") as f:
        f.write(JS)


# ---------------------------------------------------------------------------
# 4. 主流程
# ---------------------------------------------------------------------------
def load_lessons():
    lessons = []
    for mod_name in ["content_part1", "content_part2", "content_part3",
                     "content_part4", "content_part5"]:
        mod = importlib.import_module(mod_name)
        lessons.extend(mod.LESSONS)
    lessons.sort(key=lambda L: L["id"])
    return lessons


def main():
    if os.path.isdir(OUT):
        # 有些掛載環境不允許刪除檔案，忽略錯誤後直接覆寫即可
        shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    write_assets()
    lessons = load_lessons()
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_page(lessons))
    with open(os.path.join(OUT, "cheatsheet.html"), "w", encoding="utf-8") as f:
        f.write(cheatsheet_page(lessons))
    for idx in range(len(lessons)):
        with open(os.path.join(OUT, "lesson-%s.html" % lessons[idx]["id"]), "w", encoding="utf-8") as f:
            f.write(lesson_page(lessons, idx))
    print("完成！共產生 %d 課。" % len(lessons))
    print("請用瀏覽器開啟：%s" % os.path.join(OUT, "index.html"))


# CSS 與 JS 內容放在檔案最後，保持主邏輯清爽
from assets_data import CSS, JS  # noqa: E402

if __name__ == "__main__":
    main()
