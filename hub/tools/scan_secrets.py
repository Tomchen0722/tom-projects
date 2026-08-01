# -*- coding: utf-8 -*-
"""推送前的機密掃描。

GitHub 有推送保護，含金鑰的 commit 會被直接擋下來，
而被擋的時候金鑰其實已經傳到 GitHub 了——所以要在本地先攔。

只掃「會進版控的檔案」（git ls-files），被 .gitignore 排除的不算。

執行：  python hub/tools/scan_secrets.py
離開碼 0 表示乾淨，1 表示有發現。
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

# (名稱, 樣式, 是否為高風險)
PATTERNS: list[tuple[str, str]] = [
    ("Hugging Face 權杖",     r"hf_[A-Za-z0-9]{30,}"),
    ("OpenAI 金鑰",           r"sk-[A-Za-z0-9]{20,}"),
    ("Anthropic 金鑰",        r"sk-ant-[A-Za-z0-9_\-]{20,}"),
    ("Google API 金鑰",       r"AIza[A-Za-z0-9_\-]{35}"),
    ("Google OAuth 權杖",     r"\bya29\.[A-Za-z0-9_\-]{20,}"),
    ("GitHub 權杖",           r"gh[pousr]_[A-Za-z0-9]{36,}"),
    ("GitLab 權杖",           r"glpat-[A-Za-z0-9_\-]{20,}"),
    ("Slack 權杖",            r"xox[baprs]-[A-Za-z0-9\-]{10,}"),
    ("AWS 存取金鑰",          r"\bAKIA[0-9A-Z]{16}\b"),
    ("Stripe 金鑰",           r"\b[sr]k_live_[A-Za-z0-9]{20,}"),
    ("私鑰檔內容",            r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    ("含密碼的連線字串",      r"(postgresql|postgres|mysql|mongodb(\+srv)?)://[^\s:@/]+:[^\s:@/]+@"),
    ("Google 服務帳戶金鑰",   r'"private_key"\s*:\s*"-----BEGIN'),
]

# 這些是說明文件、教材與工具裡的示範寫法，不是真的金鑰
ALLOW = [
    re.compile(r"sk-你的金鑰"),
    re.compile(r"hf_你的權杖"),
    re.compile(r"密碼@主機"),
    re.compile(r"<[^>]*密碼[^>]*>"),
    re.compile(r"\{[A-Za-z_]+\}"),          # f-string 樣板，例如 {USER}:{encoded}@{HOST}
    re.compile(r"使用者:密碼"),
    re.compile(r"sk-ant-\.\.\."),
    re.compile(r"AIza\.\.\."),
    # 各家官方文件的公開範例值（資安教材會拿來示範怎麼抓外洩金鑰）
    re.compile(r"EXAMPLE", re.IGNORECASE),
    re.compile(r"YOUR[_\-]?(API[_\-]?)?(KEY|TOKEN|SECRET)", re.IGNORECASE),
    re.compile(r"xxx+", re.IGNORECASE),
]


def tracked_files() -> list[Path]:
    out = subprocess.run(
        ["git", "ls-files"],
        cwd=str(ROOT), capture_output=True, text=True,
        encoding="utf-8", errors="replace",
    ).stdout
    return [ROOT / line.strip() for line in out.splitlines() if line.strip()]


def is_allowed(line: str) -> bool:
    return any(p.search(line) for p in ALLOW)


def main() -> int:
    findings: list[tuple[str, str, int, str]] = []
    compiled = [(name, re.compile(pat)) for name, pat in PATTERNS]

    for path in tracked_files():
        if not path.exists() or path.stat().st_size > 2_000_000:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue      # 二進位檔跳過

        for lineno, line in enumerate(text.splitlines(), 1):
            if is_allowed(line):
                continue
            for name, rx in compiled:
                m = rx.search(line)
                if m:
                    hit = m.group(0)
                    masked = hit[:6] + "…" + hit[-4:] if len(hit) > 14 else hit[:6] + "…"
                    rel = path.relative_to(ROOT).as_posix()
                    findings.append((name, rel, lineno, masked))

    print("=" * 66)
    print("  推送前機密掃描")
    print("=" * 66)
    print(f"  掃描 {len(tracked_files())} 個進版控的檔案")
    print()

    if not findings:
        print("  沒有發現金鑰或密碼，可以安全推送。")
        return 0

    print(f"  發現 {len(findings)} 處疑似機密：")
    print()
    for name, rel, lineno, masked in findings:
        print(f"  [{name}]")
        print(f"    {rel}:{lineno}")
        print(f"    內容：{masked}")
        print()

    print("  處理方式：")
    print("    1. 把金鑰改成從 .env 讀取，並確認 .env 已被 .gitignore 排除")
    print("    2. 如果金鑰已經 commit 過，要重寫歷史才能真正移除")
    print("    3. 外流過的金鑰一律當作已洩漏，去原服務撤銷重發")
    return 1


if __name__ == "__main__":
    sys.exit(main())
