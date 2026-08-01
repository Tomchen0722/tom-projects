# -*- coding: utf-8 -*-
"""Tom Chen — Project Hub

作品集與學習專案的本機總控台。
瀏覽器點一下卡片，Hub 就在背景啟動對應的專案並開啟分頁。

啟動：  python hub/app.py       （或直接執行根目錄的 啟動Hub.bat）
網址：  http://127.0.0.1:7000
"""
from __future__ import annotations

import atexit
import json
import sys
import threading
import webbrowser
from pathlib import Path

# 讓 `python hub/app.py` 也能正確 import core 套件
sys.path.insert(0, str(Path(__file__).resolve().parent))

from flask import Flask, jsonify, render_template, request, send_from_directory

from core import interpreter, launcher
from core.registry import Registry

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "projects.json"

registry = Registry(CONFIG)
app = Flask(__name__, static_folder="static", template_folder="templates")
app.config["JSON_AS_ASCII"] = False

# Flask 在非 debug 模式會快取模板。這是本機工具，改完版面重整就該看到，
# 不必為了改一行 HTML 重啟整個 Hub。
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.jinja_env.auto_reload = True
# 靜態檔（CSS / JS）同理，不要讓瀏覽器拿到舊版
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0


# ────────────────────────────────────────────────────────────
# 頁面
# ────────────────────────────────────────────────────────────
@app.get("/")
def index():
    return render_template(
        "index.html",
        hub=registry.hub,
        tree=registry.tree(),
        total=len(registry.apps),
    )


@app.get("/doc/<app_id>")
def doc(app_id: str):
    """顯示專案的 README（給沒有可執行畫面、或想先了解內容的專案看）。"""
    item = registry.get(app_id)
    if not item:
        return "找不到這個專案", 404

    readme = ""
    folder = ROOT / item["path"]
    for name in ("README.md", "readme.md", "README.txt", "AI_README.md"):
        candidate = folder / name
        if candidate.exists():
            readme = candidate.read_text(encoding="utf-8", errors="replace")
            break

    return render_template("doc.html", app=item, readme=readme, hub=registry.hub)


# ────────────────────────────────────────────────────────────
# API
# ────────────────────────────────────────────────────────────
@app.get("/api/apps")
def api_apps():
    """所有專案 + 目前狀態。前端輪詢這支更新狀態燈。"""
    data = []
    for item in registry.apps:
        st = launcher.status(item)
        row = {
            "id": item["id"],
            "state": st["state"],
            "managed": st["managed"],
            "url": st["url"],
            "uptime": st["uptime"],
        }
        # 桌面程式的視窗狀態（載入中／已開啟），前端據此更新卡片文案
        for key in ("window_ready", "window_checked", "window_title", "heavy"):
            if key in st:
                row[key] = st[key]
        data.append(row)
    return jsonify({"apps": data})


@app.post("/api/start/<app_id>")
def api_start(app_id: str):
    item = registry.get(app_id)
    if not item:
        return jsonify({"ok": False, "message": "找不到這個專案"}), 404

    hub_port = registry.hub.get("port", 7000)
    result = launcher.start(item, ROOT, hub_port=hub_port)
    return jsonify(result)


@app.post("/api/stop/<app_id>")
def api_stop(app_id: str):
    item = registry.get(app_id)
    if not item:
        return jsonify({"ok": False, "message": "找不到這個專案"}), 404
    # 帶上 port，讓 Hub 也能收拾不是自己啟動的孤兒服務
    return jsonify(launcher.stop(app_id, port=item.get("port")))


@app.post("/api/install/<app_id>")
def api_install(app_id: str):
    """安裝專案缺少的套件。第一次執行某些專案時會用到。"""
    item = registry.get(app_id)
    if not item:
        return jsonify({"ok": False, "message": "找不到這個專案"}), 404

    python_exe, missing = interpreter.resolve(item, ROOT)
    if python_exe is None:
        return jsonify({"ok": False, "message": "找不到可用的 Python 直譯器"}), 500
    if not missing:
        return jsonify({"ok": True, "message": "套件都齊全，不需要安裝"})

    req = item.get("requirements")
    if req:
        req_path = ROOT / item["path"] / req
        ok, out = interpreter.install_requirements(python_exe, req_path)
    else:
        ok, out = interpreter.install_modules(python_exe, missing)

    return jsonify({
        "ok": ok,
        "message": "安裝完成" if ok else "安裝失敗",
        "log": out[-2000:],
    })


@app.get("/api/check/<app_id>")
def api_check(app_id: str):
    """檢查專案的執行環境是否齊備，讓卡片能先標示「需要安裝」。"""
    item = registry.get(app_id)
    if not item:
        return jsonify({"ok": False, "message": "找不到這個專案"}), 404

    python_exe, missing = interpreter.resolve(item, ROOT)
    return jsonify({
        "ok": not missing,
        "python": python_exe,
        "missing": missing,
        "heavy": bool(item.get("heavy")),
    })


@app.get("/api/log/<app_id>")
def api_log(app_id: str):
    """取得專案的執行記錄，啟動失敗時用來查原因。"""
    log_path = ROOT / "hub" / "logs" / f"{app_id}.log"
    if not log_path.exists():
        return jsonify({"log": "（尚無記錄）"})
    content = log_path.read_text(encoding="utf-8", errors="replace")
    return jsonify({"log": "\n".join(content.splitlines()[-200:])})


@app.post("/api/stop-all")
def api_stop_all():
    launcher.stop_all()
    return jsonify({"ok": True, "message": "已停止所有執行中的專案"})


# ────────────────────────────────────────────────────────────
# 共用資源：讓子專案能載入 Hub 的返回按鈕樣式
# ────────────────────────────────────────────────────────────
@app.get("/shared/<path:filename>")
def shared(filename: str):
    resp = send_from_directory(str(ROOT / "hub" / "static" / "shared"), filename)
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


# ────────────────────────────────────────────────────────────
def main() -> None:
    port = registry.hub.get("port", 7000)
    atexit.register(launcher.stop_all)

    if launcher.port_open(port):
        print(f"  Hub 已經在 http://127.0.0.1:{port} 執行中，直接開啟瀏覽器。")
        webbrowser.open(f"http://127.0.0.1:{port}")
        return

    banner = registry.hub.get("title", "Project Hub")
    print("=" * 60)
    print(f"  {banner}")
    print(f"  共 {len(registry.apps)} 個專案")
    print(f"  網址：http://127.0.0.1:{port}")
    print("  關閉這個視窗就會一併停止所有已啟動的專案。")
    print("=" * 60)

    threading.Timer(1.2, lambda: webbrowser.open(f"http://127.0.0.1:{port}")).start()

    try:
        app.run(host="127.0.0.1", port=port, debug=False, threaded=True)
    finally:
        launcher.stop_all()


if __name__ == "__main__":
    main()
