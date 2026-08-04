"""把瀏覽計數器注入所有專案的 HTML 頁面。

用法：
    python hub/tools/inject_analytics.py            # 注入 / 更新
    python hub/tools/inject_analytics.py --remove   # 全部移除
    python hub/tools/inject_analytics.py --dry-run  # 只看會改哪些檔，不動手

設計重點
────────
計數器是「內嵌」注入，不是用 <script src> 外連。
原因：GitHub Pages 上專案在 /tom-projects/learning/... 的深層目錄，
本機 Flask 又是每個專案自己一個 port，兩邊的相對路徑無法統一。
內嵌雖然每頁多幾 KB，但保證兩種環境都能運作。

Supabase 設定改了之後，重跑一次這支腳本就會更新所有頁面。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFIG_JS = ROOT / "shared" / "analytics-config.js"
TRACKER_JS = ROOT / "shared" / "analytics.js"
PROJECTS_JSON = ROOT / "projects.json"

BEGIN = "<!-- portfolio-analytics:begin -->"
END = "<!-- portfolio-analytics:end -->"
BLOCK_RE = re.compile(
    re.escape(BEGIN) + r".*?" + re.escape(END),
    re.DOTALL,
)

# 這些目錄不注入
SKIP_DIRS = {
    ".git", "node_modules", "__pycache__", ".venv", "venv",
    "hub", "docs", ".github", "shared",
}


def read_supabase_config() -> tuple[str, str]:
    """從 analytics-config.js 讀出 url / key。"""
    if not CONFIG_JS.exists():
        return "", ""
    text = CONFIG_JS.read_text(encoding="utf-8")
    url = re.search(r"url\s*:\s*['\"]([^'\"]*)['\"]", text)
    key = re.search(r"key\s*:\s*['\"]([^'\"]*)['\"]", text)
    return (url.group(1) if url else ""), (key.group(1) if key else "")


def load_project_map() -> dict[Path, str]:
    """回傳「專案根目錄 → project id」的對應表，依路徑長度由深到淺排序。"""
    if not PROJECTS_JSON.exists():
        print("  找不到 projects.json，全部頁面會標成 unknown。")
        return {}
    data = json.loads(PROJECTS_JSON.read_text(encoding="utf-8"))
    mapping: dict[Path, str] = {}
    for app in data.get("apps", []):
        rel = app.get("path")
        if not rel:
            continue
        mapping[(ROOT / rel).resolve()] = app["id"]
    return mapping


def project_id_for(html: Path, mapping: dict[Path, str]) -> str:
    """判斷某個 HTML 檔屬於哪個專案。找不到就依位置給 hub 或 unknown。"""
    resolved = html.resolve()
    best: tuple[int, str] | None = None
    for proj_dir, pid in mapping.items():
        try:
            resolved.relative_to(proj_dir)
        except ValueError:
            continue
        depth = len(proj_dir.parts)
        if best is None or depth > best[0]:
            best = (depth, pid)
    if best:
        return best[1]
    # 根目錄的 index.html 就是作品集首頁
    if resolved.parent == ROOT:
        return "stats" if resolved.name == "stats.html" else "hub"
    return "unknown"


def build_block(project_id: str, url: str, key: str, tracker: str) -> str:
    # 內嵌時任何 </script 都會提前關閉標籤，連註解裡的也會。
    tracker = tracker.replace("</script", r"<\/script")
    cfg = json.dumps({"url": url, "key": key}, ensure_ascii=False)
    return (
        f"{BEGIN}\n"
        f"<script>window.ANALYTICS_CONFIG={cfg};</script>\n"
        f'<script data-project="{project_id}">\n{tracker}\n</script>\n'
        f"{END}"
    )


def inject(html: Path, block: str) -> bool:
    """把 block 放進 </body> 之前。已存在就整段替換。回傳是否有變動。"""
    text = html.read_text(encoding="utf-8", errors="replace")

    if BLOCK_RE.search(text):
        new = BLOCK_RE.sub(lambda _m: block, text, count=1)
    elif "</body>" in text:
        new = text.replace("</body>", block + "\n</body>", 1)
    elif "</html>" in text:
        new = text.replace("</html>", block + "\n</html>", 1)
    else:
        new = text + "\n" + block + "\n"

    if new == text:
        return False
    html.write_text(new, encoding="utf-8")
    return True


def remove(html: Path) -> bool:
    text = html.read_text(encoding="utf-8", errors="replace")
    if not BLOCK_RE.search(text):
        return False
    new = BLOCK_RE.sub("", text).replace("\n\n\n", "\n\n")
    html.write_text(new, encoding="utf-8")
    return True


def iter_html():
    for path in ROOT.rglob("*.html"):
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts[:-1]):
            continue
        if path.name.startswith(("_", "test_")):
            continue
        head = path.read_text(encoding="utf-8", errors="replace")[:400]
        # Jinja 子模板：內容會塞進 base.html 的 block，自己沒有 </body>，
        # 注入進去只會被樣板引擎丟掉，而且會和 base.html 重複計數。
        if "{% extends" in head or "{%extends" in head:
            continue
        yield path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--remove", action="store_true", help="移除所有已注入的計數器")
    ap.add_argument("--dry-run", action="store_true", help="只列出會改動的檔案")
    args = ap.parse_args()

    if not TRACKER_JS.exists():
        print(f"  找不到 {TRACKER_JS}")
        return 1

    # 把 IIFE 外殼拆掉，內嵌時 document.currentScript 才抓得到 data-project
    tracker = TRACKER_JS.read_text(encoding="utf-8")

    url, key = read_supabase_config()
    mapping = load_project_map()

    if args.remove:
        print("  模式：移除計數器")
    else:
        state = "已接上 Supabase" if (url and key) else "未設定 Supabase（會用本機 localStorage 計數）"
        print(f"  模式：注入計數器　狀態：{state}")
    print(f"  掃描目錄：{ROOT}")
    print("-" * 60)

    changed = 0
    total = 0
    per_project: dict[str, int] = {}

    for html in sorted(iter_html()):
        total += 1
        rel = html.relative_to(ROOT)

        if args.remove:
            if args.dry_run:
                text = html.read_text(encoding="utf-8", errors="replace")
                if BLOCK_RE.search(text):
                    print(f"  [會移除] {rel}")
                    changed += 1
            elif remove(html):
                changed += 1
            continue

        pid = project_id_for(html, mapping)
        per_project[pid] = per_project.get(pid, 0) + 1

        if args.dry_run:
            print(f"  [{pid}] {rel}")
            changed += 1
            continue

        if inject(html, build_block(pid, url, key, tracker)):
            changed += 1

    print("-" * 60)
    print(f"  掃描 {total} 個 HTML，異動 {changed} 個")

    if per_project and not args.remove:
        print("\n  各專案頁數：")
        for pid, n in sorted(per_project.items(), key=lambda kv: -kv[1]):
            flag = "  ⚠ 沒對應到 projects.json" if pid == "unknown" else ""
            print(f"    {pid:<24} {n:>3} 頁{flag}")

    if not args.remove and not (url and key):
        print(
            "\n  提醒：shared/analytics-config.js 還沒填 Supabase 資訊，\n"
            "        目前只會做本機 localStorage 計數。填完後重跑這支腳本即可。"
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
