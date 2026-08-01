# -*- coding: utf-8 -*-
"""Python 直譯器探測。

不同專案需要的套件不一樣，而這台機器上可能同時裝了 anaconda、python.org 版本、
py launcher 管理的多個版本。這個模組負責找出「哪一個直譯器裝得最齊」，
讓專案點下去就能跑，而不是丟一個 ModuleNotFoundError 給使用者。

探測結果會快取，Hub 啟動時只做一次。
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

# 探測順序：越前面越優先。anaconda 通常套件最齊，放第一。
CANDIDATE_HINTS = [
    Path.home() / "anaconda3" / "python.exe",
    Path.home() / "miniconda3" / "python.exe",
    Path("C:/ProgramData/anaconda3/python.exe"),
]

_probe_cache: dict[str, set[str]] = {}
_interpreters: list[str] | None = None


def _run(cmd: list[str], timeout: int = 20) -> tuple[int, str]:
    """執行指令並回傳 (returncode, 輸出)。失敗不拋例外，回傳非 0。"""
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding="utf-8",
            errors="replace",
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        )
        return proc.returncode, (proc.stdout or "") + (proc.stderr or "")
    except Exception as exc:  # noqa: BLE001 - 探測失敗只當作「這個直譯器不可用」
        return 1, str(exc)


def discover_interpreters() -> list[str]:
    """列出這台機器上可用的 Python 直譯器路徑，依「套件可能最齊」排序。"""
    global _interpreters
    if _interpreters is not None:
        return _interpreters

    found: list[str] = []

    for hint in CANDIDATE_HINTS:
        if hint.exists():
            found.append(str(hint))

    # py launcher 管理的版本（新到舊）
    if shutil.which("py"):
        for ver in ("3.13", "3.12", "3.11"):
            code, out = _run(["py", f"-{ver}", "-c", "import sys; print(sys.executable)"])
            if code == 0 and out.strip():
                exe = out.strip().splitlines()[-1].strip()
                if exe and exe not in found:
                    found.append(exe)

    # PATH 上的 python
    for name in ("python", "python3"):
        exe = shutil.which(name)
        if exe:
            code, out = _run([exe, "-c", "import sys; print(sys.executable)"])
            if code == 0:
                real = out.strip().splitlines()[-1].strip()
                if real and real not in found:
                    found.append(real)

    # 跑 Hub 自己的直譯器一定可用，墊底
    if sys.executable not in found:
        found.append(sys.executable)

    _interpreters = found
    return found


def has_modules(python_exe: str, modules: list[str]) -> tuple[bool, list[str]]:
    """檢查指定直譯器是否具備這些模組，回傳 (是否全部具備, 缺少的清單)。"""
    if not modules:
        return True, []

    key = python_exe + "|" + ",".join(sorted(modules))
    if key in _probe_cache:
        missing = sorted(_probe_cache[key])
        return (not missing), missing

    script = (
        "import importlib.util as u,sys\n"
        f"mods={modules!r}\n"
        "print(','.join(m for m in mods if u.find_spec(m) is None))"
    )
    code, out = _run([python_exe, "-c", script])
    if code != 0:
        _probe_cache[key] = set(modules)
        return False, sorted(modules)

    raw = out.strip().splitlines()[-1].strip() if out.strip() else ""
    missing = [m for m in raw.split(",") if m]
    _probe_cache[key] = set(missing)
    return (not missing), missing


def resolve(app: dict, root: Path) -> tuple[str | None, list[str]]:
    """替一個專案挑出最合適的直譯器。

    回傳 (直譯器路徑, 缺少的模組)。
    - python == "venv" → 強制使用專案內建的 .venv（例如 AI 會議助理的 torch 環境）
    - python == "auto" → 挑第一個「套件全齊」的；全都不齊就挑「缺最少」的那個
    """
    mode = app.get("python", "auto")
    needs = [m for m in app.get("needs", []) if m]

    if mode == "venv":
        venv_py = root / app["path"] / ".venv" / "Scripts" / "python.exe"
        if venv_py.exists():
            _, missing = has_modules(str(venv_py), needs)
            return str(venv_py), missing
        # venv 不在就退回自動挑選，讓 Hub 有機會提示安裝
        mode = "auto"

    if mode not in ("auto", "venv"):
        # 直接指定路徑的情況
        _, missing = has_modules(mode, needs)
        return mode, missing

    best: tuple[str, list[str]] | None = None
    for exe in discover_interpreters():
        ok, missing = has_modules(exe, needs)
        if ok:
            return exe, []
        if best is None or len(missing) < len(best[1]):
            best = (exe, missing)

    if best:
        return best[0], best[1]
    return None, needs


def pythonw_of(python_exe: str) -> str:
    """取得對應的 pythonw.exe（跑桌面程式時不彈出黑色主控台視窗）。"""
    p = Path(python_exe)
    candidate = p.with_name("pythonw.exe")
    return str(candidate) if candidate.exists() else python_exe


def install_requirements(python_exe: str, req_path: Path) -> tuple[bool, str]:
    """對指定直譯器安裝 requirements.txt。回傳 (是否成功, 輸出訊息)。"""
    if not req_path.exists():
        return False, f"找不到 {req_path.name}"
    code, out = _run(
        [python_exe, "-m", "pip", "install", "-r", str(req_path)],
        timeout=3600,
    )
    return code == 0, out[-4000:]


def install_modules(python_exe: str, modules: list[str]) -> tuple[bool, str]:
    """直接安裝指定的套件清單。"""
    if not modules:
        return True, "無需安裝"
    code, out = _run(
        [python_exe, "-m", "pip", "install", *modules],
        timeout=3600,
    )
    return code == 0, out[-4000:]
