# -*- coding: utf-8 -*-
"""把「回 Hub」按鈕注入各個網頁專案。

注入的是「內嵌」腳本而不是外部 script 標籤，原因是這些頁面有兩種使用情境：

  本機   → 由 Project Hub 啟動，返回按鈕要連到 http://127.0.0.1:7000
  線上   → 放在 GitHub Pages 上，本機的 Hub 根本不存在

如果用外部 script（src 指向 127.0.0.1:7000），線上版會載入失敗、按鈕直接消失。
所以改成內嵌，並由腳本自己判斷目前在哪個環境，線上時連回站台入口頁
（相對路徑會依檔案所在深度自動算好）。

這支腳本可以重複執行：已注入的舊版會被替換成新版，不會疊加。

執行：  python hub/tools/inject_return.py            注入或更新
        python hub/tools/inject_return.py --remove   全部移除
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

MARKER = "TOM_HUB_RETURN"

# 要注入的檔案；含 * 的樣式表示該層所有符合的檔案
TARGETS = [
    "projects/web/QR_order/templates/base.html",
    "projects/web/AI_agent/static/index.html",
    "learning/dev/CyberSecAcademy/templates/index.html",
    "learning/cloud/AWS/*.html",
    "learning/cloud/GCP-Learning/*.html",
    "learning/cloud/GCP-Learning/lessons/*.html",
    "learning/dev/git-course/site/*.html",
]

SNIPPET_TEMPLATE = """
<!-- TOM_HUB_RETURN start : 由 Project Hub 注入，可用 hub/tools/inject_return.py 重新產生 -->
<script>
(function(){{
  if (document.getElementById('tom-hub-return')) return;
  // 依所在環境決定回哪裡：
  //   本機          → 本機的 Project Hub
  //   作品集站台內  → 用相對路徑，換網域也不會壞
  //   其他網域      → 專案自己部署在 Render 等平台，相對路徑會超出根目錄，
  //                   只能用完整網址連回作品集
  var host = location.hostname;
  var local = ['127.0.0.1','localhost',''].indexOf(host) >= 0;
  var onSite = {site_host_check};
  var href = local ? 'http://127.0.0.1:7000'
           : (onSite ? '{prefix}index.html' : '{site_url}');
  var label = local ? '回 Hub' : '回作品集';
  function mount() {{
    if (!document.body) return;
    var s = document.createElement('style');
    s.textContent = '#tom-hub-return{{position:fixed;left:18px;bottom:18px;z-index:2147483000;'
      + 'display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:11px 18px;'
      + 'background:#1C1A18;color:#FEFEF9;font-family:"Noto Sans TC","Microsoft JhengHei",sans-serif;'
      + 'font-size:13px;font-weight:500;letter-spacing:.03em;line-height:1;text-decoration:none;'
      + 'box-shadow:0 6px 24px rgba(28,26,24,.22);'
      + 'transition:background .25s cubic-bezier(.22,1,.36,1),transform .25s cubic-bezier(.22,1,.36,1);}}'
      + '#tom-hub-return::after{{content:"";position:absolute;bottom:-3px;right:-3px;width:100%;height:100%;'
      + 'border:1.5px solid #3A68AD;opacity:.45;pointer-events:none;transition:opacity .25s;}}'
      + '#tom-hub-return:hover{{background:#3A68AD;transform:translateY(-2px);}}'
      + '#tom-hub-return:hover::after{{opacity:0;}}'
      + '#tom-hub-return:focus-visible{{outline:2px solid #3A68AD;outline-offset:3px;}}'
      // media query 的左大括號後面刻意留一個空格：這段也會被注入到 Jinja2 模板裡，
      // 左大括號緊接井號會被 Jinja2 當成註解開始，導致整頁解析失敗。
      + '@media(max-width:600px){{ #tom-hub-return{{left:12px;bottom:12px;padding:11px 15px;font-size:12px;}}}}'
      + '@media(prefers-reduced-motion:reduce){{ #tom-hub-return{{transition:none;}}}}'
      + '@media print{{ #tom-hub-return{{display:none;}}}}';
    document.head.appendChild(s);
    var a = document.createElement('a');
    a.id = 'tom-hub-return';
    a.href = href;
    a.title = label;
    a.setAttribute('aria-label', label);
    a.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"'
      + ' stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
      + '<line x1="19" y1="12" x2="5" y2="12"></line>'
      + '<polyline points="12 19 5 12 12 5"></polyline></svg><span>' + label + '</span>';
    document.body.appendChild(a);
  }}
  if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', mount);
  }} else {{
    mount();
  }}
}})();
</script>
<!-- TOM_HUB_RETURN end -->
"""

# 用來移除舊版注入（無論是外部 script 版還是先前的內嵌版）
OLD_BLOCK = re.compile(
    r"\n?<!--\s*TOM_HUB_RETURN.*?(?:-->\s*<script[^>]*></script>|end\s*-->)\n?",
    re.DOTALL,
)


def expand(pattern: str) -> list[Path]:
    if "*" in pattern:
        parent = ROOT / Path(pattern).parent
        if not parent.exists():
            return []
        return sorted(parent.glob(Path(pattern).name))
    path = ROOT / pattern
    return [path] if path.exists() else []


def relative_prefix(path: Path) -> str:
    """算出從這個檔案回到根目錄要幾層 ../。"""
    depth = len(path.relative_to(ROOT).parts) - 1   # 扣掉檔名本身
    return "../" * depth if depth else "./"


def site_config() -> tuple[str, str]:
    """從 projects.json 取出作品集網址與它的主機名稱。"""
    import json

    try:
        data = json.loads((ROOT / "projects.json").read_text(encoding="utf-8"))
        url = (data.get("site") or {}).get("url", "").strip()
    except Exception:  # noqa: BLE001
        url = ""

    if not url:
        return "", ""

    from urllib.parse import urlparse

    return url, (urlparse(url).hostname or "")


def build_snippet(path: Path, site_url: str, site_host: str) -> str:
    """組出要注入的腳本。"""
    if site_host:
        # 用 indexOf 判斷主機名稱，避免把 xxx.github.io.evil.com 也算進來
        host_check = f"host === {site_host!r}"
    else:
        # 還沒設定作品集網址時，非本機一律走相對路徑（原本的行為）
        host_check = "true"

    return SNIPPET_TEMPLATE.format(
        prefix=relative_prefix(path),
        site_url=site_url or "/",
        site_host_check=host_check,
    )


def inject(path: Path, site_url: str, site_host: str) -> str:
    """回傳 injected / updated / no-body。"""
    text = path.read_text(encoding="utf-8", errors="replace")

    had_old = MARKER in text
    if had_old:
        text = OLD_BLOCK.sub("\n", text)

    lower = text.lower()
    idx = lower.rfind("</body>")
    if idx == -1:
        return "no-body"

    snippet = build_snippet(path, site_url, site_host)
    path.write_text(text[:idx] + snippet + text[idx:], encoding="utf-8")
    return "updated" if had_old else "injected"


def remove(path: Path) -> str:
    """把注入的返回按鈕整段拿掉。回傳 removed / clean。"""
    text = path.read_text(encoding="utf-8", errors="replace")
    if MARKER not in text:
        return "clean"

    cleaned = OLD_BLOCK.sub("\n", text)
    # 移除後可能留下連續空行，收斂成一行，避免檔案愈改愈鬆散
    cleaned = re.sub(r"\n{3,}(?=</body>)", "\n", cleaned, flags=re.IGNORECASE)
    path.write_text(cleaned, encoding="utf-8")
    return "removed"


def check_template_safe(snippet: str) -> list[str]:
    """檢查產生的內容有沒有會讓 Jinja2 誤判的標記。

    這些檔案有一部分是 Flask 的 Jinja2 模板，注入的 CSS 若出現 `{#`、`{%`、`{{`
    會被當成模板語法，導致整頁 500。之前就是 `){#tom-hub-return{` 踩到這個雷。
    """
    problems = []
    for token, name in (("{#", "Jinja2 註解"), ("{%", "Jinja2 語句"), ("{{", "Jinja2 變數")):
        if token in snippet:
            idx = snippet.find(token)
            problems.append(f"{name} 標記 {token}（位置 {idx}：…{snippet[max(0, idx-30):idx+20]}…）")
    return problems


def main() -> int:
    if "--remove" in sys.argv:
        counts = {"removed": 0, "clean": 0, "missing": 0}
        for pattern in TARGETS:
            files = expand(pattern)
            if not files:
                counts["missing"] += 1
                continue
            for f in files:
                counts[remove(f)] += 1
        print()
        print(f"移除 {counts['removed']} 個檔案的返回按鈕，"
              f"{counts['clean']} 個本來就沒有。")
        print("要加回來的話，執行不帶 --remove 的同一支腳本即可。")
        return 0

    counts = {"injected": 0, "updated": 0, "no-body": 0, "missing": 0}

    site_url, site_host = site_config()
    if site_host:
        print(f"  作品集網址：{site_url}")
    else:
        print("  projects.json 沒有設定 site.url，"
              "部署在其他網域的專案將無法正確返回作品集")
    print()

    # 先驗證要注入的內容本身是安全的，不要等到頁面 500 才發現
    sample = SNIPPET_TEMPLATE.format(
        prefix="../", site_url=site_url or "/", site_host_check="true"
    )
    problems = check_template_safe(sample)
    if problems:
        print("注入內容含有會破壞 Jinja2 模板的標記，已中止：")
        for p in problems:
            print("  " + p)
        return 1

    for pattern in TARGETS:
        files = expand(pattern)
        if not files:
            print(f"  [找不到] {pattern}")
            counts["missing"] += 1
            continue
        for f in files:
            counts[inject(f, site_url, site_host)] += 1

    print()
    print(f"新注入 {counts['injected']} 個、更新 {counts['updated']} 個、"
          f"無 body 標籤 {counts['no-body']} 個、找不到 {counts['missing']} 個路徑。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
