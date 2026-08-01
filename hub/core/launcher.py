# -*- coding: utf-8 -*-
"""子專案的啟動、監看與停止。

每個專案的啟動方式都不一樣（Streamlit、Flask、靜態站、桌面程式），
這裡把差異收斂成統一的 start / stop / status 介面，Hub 只要呼叫這三個。

Windows 上停止子程序要連同它的子孫一起殺（Streamlit 會再開子程序），
所以用 taskkill /T /F 而不是單純的 terminate()。
"""
from __future__ import annotations

import os
import socket
import subprocess
import threading
import time
from pathlib import Path

from . import interpreter, winwindow

# app_id -> 執行中的狀態
_running: dict[str, dict] = {}
_lock = threading.Lock()

CREATE_NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)


# ────────────────────────────────────────────────────────────
# port 工具
# ────────────────────────────────────────────────────────────
def port_open(port: int, host: str = "127.0.0.1", timeout: float = 0.35) -> bool:
    """這個 port 是否已經有東西在聽。"""
    if not port:
        return False
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0


def wait_port(port: int, timeout: float = 60.0) -> bool:
    """等待 port 可連線，逾時回傳 False。"""
    deadline = time.time() + timeout
    while time.time() < deadline:
        if port_open(port):
            return True
        time.sleep(0.4)
    return False


# ────────────────────────────────────────────────────────────
# 指令組裝
# ────────────────────────────────────────────────────────────
def build_command(app: dict, python_exe: str, workdir: Path) -> tuple[list[str], dict]:
    """依專案型態組出啟動指令與環境變數。"""
    kind = app["kind"]
    port = app.get("port")
    env = os.environ.copy()
    # 讓子專案知道 Hub 在哪，注入的「回 Hub」按鈕會用到
    env["TOM_HUB_URL"] = f"http://127.0.0.1:{app.get('_hub_port', 7000)}"
    env["PYTHONIOENCODING"] = "utf-8"

    if kind == "streamlit":
        return [
            python_exe, "-m", "streamlit", "run", app["entry"],
            "--server.port", str(port),
            "--server.headless", "true",
            "--browser.gatherUsageStats", "false",
        ], env

    if kind == "flask":
        # Flask 專案讀 PORT 環境變數的就會照著跑；硬編碼的則沿用它自己的設定
        env["PORT"] = str(port)
        env["FLASK_RUN_PORT"] = str(port)
        return [python_exe, app["entry"]], env

    if kind in ("static", "static-build"):
        serve_dir = workdir / app.get("serve_dir", ".")
        return [
            python_exe, "-m", "http.server", str(port),
            "--bind", "127.0.0.1",
            "--directory", str(serve_dir),
        ], env

    if kind == "desktop":
        # 桌面程式用 pythonw 啟動，避免多一個黑色主控台視窗
        return [interpreter.pythonw_of(python_exe), app["entry"]], env

    raise ValueError(f"未知的專案型態：{kind}")


# ────────────────────────────────────────────────────────────
# 啟動 / 停止 / 狀態
# ────────────────────────────────────────────────────────────
def start(app: dict, root: Path, hub_port: int = 7000) -> dict:
    """啟動一個專案。回傳結果字典（含 ok / message / url）。"""
    app_id = app["id"]
    workdir = root / app["path"]
    port = app.get("port")

    if not workdir.exists():
        return {"ok": False, "message": f"找不到專案資料夾：{app['path']}"}

    with _lock:
        info = _running.get(app_id)
        if info and info["proc"].poll() is None:
            return {
                "ok": True,
                "message": "已經在執行中",
                "url": f"http://127.0.0.1:{port}" if port else None,
                "already": True,
            }

    # port 被別的東西佔用（可能是使用者自己在外面開了同一個專案）
    if port and port_open(port):
        return {
            "ok": True,
            "message": f"port {port} 已有服務在執行，直接開啟",
            "url": f"http://127.0.0.1:{port}",
            "already": True,
        }

    python_exe, missing = interpreter.resolve(app, root)
    if python_exe is None:
        return {"ok": False, "message": "找不到可用的 Python 直譯器"}

    if missing:
        return {
            "ok": False,
            "needs_install": True,
            "missing": missing,
            "python": python_exe,
            "message": "缺少套件：" + "、".join(missing),
        }

    # static-build 型態：先把靜態站產生出來
    if app["kind"] == "static-build":
        build_script = app.get("build")
        serve_index = workdir / app.get("serve_dir", ".") / app.get("entry", "index.html")
        if build_script and not serve_index.exists():
            proc = subprocess.run(
                [python_exe, build_script],
                cwd=str(workdir),
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=300,
                creationflags=CREATE_NO_WINDOW,
            )
            if proc.returncode != 0:
                return {
                    "ok": False,
                    "message": "產生靜態網站失敗：" + (proc.stderr or "")[-500:],
                }

    app = {**app, "_hub_port": hub_port}
    try:
        cmd, env = build_command(app, python_exe, workdir)
    except ValueError as exc:
        return {"ok": False, "message": str(exc)}

    log_path = root / "hub" / "logs" / f"{app_id}.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_file = open(log_path, "w", encoding="utf-8", errors="replace")

    # 先記下專案自己的 error.log 時間，啟動後若被改寫就代表程式回報了錯誤
    error_log = workdir / "error.log"
    error_before = error_log.stat().st_mtime if error_log.exists() else 0.0

    try:
        proc = subprocess.Popen(
            cmd,
            cwd=str(workdir),
            env=env,
            stdout=log_file,
            stderr=subprocess.STDOUT,
            creationflags=CREATE_NO_WINDOW,
        )
    except Exception as exc:  # noqa: BLE001
        log_file.close()
        return {"ok": False, "message": f"啟動失敗：{exc}"}

    with _lock:
        _running[app_id] = {
            "proc": proc,
            "port": port,
            "log": log_path,
            "log_file": log_file,
            "started_at": time.time(),
            "kind": app["kind"],
        }

    # 網頁類要等 port 起來才算成功；桌面類看程序是否還活著
    if port:
        if wait_port(port, timeout=90):
            return {"ok": True, "message": "啟動完成", "url": f"http://127.0.0.1:{port}"}
        tail = _read_log_tail(log_path)
        stop(app_id)
        return {"ok": False, "message": "啟動逾時，服務沒有回應", "log": tail}

    # 桌面程式沒有 port 可以探測，改用三個訊號判斷是否真的起來了：
    #   1. 程序是否已經結束（import 失敗會直接退出）
    #   2. 專案自己的 error.log 有沒有被寫入（有些 GUI 會把啟動錯誤寫在這）
    #   3. 執行記錄裡有沒有致命錯誤
    # 給 5 秒是因為 PySide6 / pandas 這類重量級套件載入需要時間，
    # 而且部分虛擬環境的 pythonw 只是啟動代理，真正的程序是它的子程序。
    time.sleep(5.0)

    if proc.poll() is not None:
        stop(app_id)
        return {
            "ok": False,
            "message": "程式啟動後隨即結束，請看下方錯誤訊息",
            "log": _read_log_tail(log_path, 30),
        }

    # 啟動失敗時要把殘留的程序收乾淨（例如只剩下一個錯誤對話框的情況），
    # 否則狀態會一直顯示「執行中」，與啟動結果互相矛盾。
    if error_log.exists() and error_log.stat().st_mtime > error_before:
        try:
            content = error_log.read_text(encoding="utf-8", errors="replace")
        except Exception:  # noqa: BLE001
            content = ""
        stop(app_id)
        return {
            "ok": False,
            "message": "程式回報了啟動錯誤（見專案的 error.log）",
            "log": "\n".join(content.splitlines()[-30:]),
        }

    tail = _read_log_tail(log_path, 60)
    if _fatal_error(tail):
        stop(app_id)
        return {
            "ok": False,
            "message": "啟動過程發生錯誤，視窗可能沒有正常開啟",
            "log": tail,
        }

    # Hub 是背景服務，它啟動的視窗不會自動取得焦點。
    # 前景化放到背景執行緒做：載入 PyTorch 這類重量級套件可能要半分鐘以上，
    # 不能讓使用者按了按鈕之後乾等，所以先回應、視窗好了再自動跳到前面。
    heavy = bool(app.get("heavy"))
    with _lock:
        info = _running.get(app_id)
        if info:
            info["window_ready"] = False
            info["window_checked"] = False
            info["heavy"] = heavy

    threading.Thread(
        target=_focus_later,
        args=(app_id, proc.pid, 120.0 if heavy else 30.0),
        daemon=True,
    ).start()

    if heavy:
        message = ("已啟動。這個專案要先載入語音模型，視窗大約 40～60 秒後出現，"
                   "屆時會自動跳到最前面，這張卡片也會更新狀態。")
    else:
        message = "已啟動，視窗開啟後會自動跳到最前面。"

    return {"ok": True, "message": message, "url": None, "waiting_window": True}


def pid_by_port(port: int) -> int | None:
    """找出正在監聽這個 port 的程序 PID。

    用來收拾「不是這次 Hub 啟動的」服務——例如 Hub 被強制關閉後留下的
    孤兒程序，使用者仍然需要有辦法把它關掉。
    """
    if not port:
        return None
    try:
        out = subprocess.run(
            ["netstat", "-ano", "-p", "TCP"],
            capture_output=True, text=True, timeout=15,
            creationflags=CREATE_NO_WINDOW,
        ).stdout
    except Exception:  # noqa: BLE001
        return None

    needle = f":{port}"
    for line in out.splitlines():
        parts = line.split()
        if len(parts) >= 5 and parts[3].upper() == "LISTENING":
            local = parts[1]
            if local.endswith(needle):
                try:
                    return int(parts[4])
                except ValueError:
                    continue
    return None


def stop(app_id: str, port: int | None = None) -> dict:
    """停止一個專案（含其子程序）。

    若這個專案不是由本次 Hub 啟動的，但它的 port 上確實有服務在跑，
    就依 port 找出程序強制終止——否則使用者會被卡在「看得到卻關不掉」。
    """
    with _lock:
        info = _running.pop(app_id, None)

    if not info:
        if port and port_open(port):
            pid = pid_by_port(port)
            if pid:
                try:
                    subprocess.run(
                        ["taskkill", "/PID", str(pid), "/T", "/F"],
                        capture_output=True, timeout=15,
                        creationflags=CREATE_NO_WINDOW,
                    )
                    return {"ok": True, "message": "已強制停止外部服務", "forced": True}
                except Exception as exc:  # noqa: BLE001
                    return {"ok": False, "message": f"無法停止：{exc}"}
            return {"ok": False, "message": "找不到佔用這個 port 的程序"}
        return {"ok": True, "message": "本來就沒有在執行"}

    proc = info["proc"]
    if proc.poll() is None:
        try:
            subprocess.run(
                ["taskkill", "/PID", str(proc.pid), "/T", "/F"],
                capture_output=True,
                timeout=15,
                creationflags=CREATE_NO_WINDOW,
            )
        except Exception:  # noqa: BLE001
            proc.kill()

    try:
        info["log_file"].close()
    except Exception:  # noqa: BLE001
        pass

    return {"ok": True, "message": "已停止"}


def stop_all() -> None:
    """Hub 關閉時把所有子專案一起收掉，不留孤兒程序。"""
    for app_id in list(_running.keys()):
        stop(app_id)


def status(app: dict) -> dict:
    """回報一個專案目前的狀態。"""
    app_id = app["id"]
    port = app.get("port")

    with _lock:
        info = _running.get(app_id)

    if info and info["proc"].poll() is None:
        result = {
            "state": "running",
            "managed": True,
            "url": f"http://127.0.0.1:{port}" if port else None,
            "uptime": int(time.time() - info["started_at"]),
        }
        # 桌面程式額外回報視窗狀態，讓前端能分辨「還在載入」與「已經開好」
        if info.get("kind") == "desktop":
            result["window_ready"] = info.get("window_ready", False)
            result["window_checked"] = info.get("window_checked", False)
            result["window_title"] = info.get("window_title", "")
            result["heavy"] = info.get("heavy", False)
        return result

    # 不是 Hub 開的，但 port 上有服務（使用者可能自己開了）
    if port and port_open(port):
        return {
            "state": "running",
            "managed": False,
            "url": f"http://127.0.0.1:{port}",
            "uptime": None,
        }

    if info:
        with _lock:
            _running.pop(app_id, None)

    return {"state": "stopped", "managed": False, "url": None, "uptime": None}


def _focus_later(app_id: str, pid: int, timeout: float) -> None:
    """在背景等待視窗出現，把它帶到最前面，並回報結果給狀態查詢用。

    像 AI 會議助理這種要載入語音模型的程式，視窗可能 40 秒後才出現。
    前端需要知道「還在載入」還是「已經開好了」，才不會讓使用者以為壞了。
    """
    found = False
    title = ""
    try:
        found = winwindow.bring_to_front(pid, timeout=timeout)
        if found:
            title = winwindow.window_title(pid)
    except Exception:  # noqa: BLE001
        pass

    with _lock:
        info = _running.get(app_id)
        if info:
            info["window_ready"] = found
            info["window_title"] = title
            info["window_checked"] = True


def _fatal_error(text: str) -> bool:
    """判斷執行記錄裡的錯誤是否致命。

    刻意不把所有 Traceback 都當成失敗——有些套件（例如 torchcodec）會在
    警告訊息裡印出完整 Traceback，但程式其實照常運作。只有這些會讓程式
    真的起不來的例外才視為致命。
    """
    fatal_markers = (
        "ModuleNotFoundError",
        "ImportError",
        "SyntaxError",
        "IndentationError",
    )
    if any(m in text for m in fatal_markers):
        return True

    # 未被攔截的例外會讓程式結束，特徵是 Traceback 之後沒有再出現警告字樣
    if "Traceback (most recent call last)" in text and "warn" not in text.lower():
        return True

    return False


def _read_log_tail(log_path: Path, lines: int = 25) -> str:
    """讀取記錄檔尾端，用來把失敗原因回報給使用者。"""
    try:
        content = log_path.read_text(encoding="utf-8", errors="replace")
        return "\n".join(content.splitlines()[-lines:])
    except Exception:  # noqa: BLE001
        return ""
