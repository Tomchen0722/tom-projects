"""自動排班系統 — Flask 進入點。

啟動:
    python app.py
然後打開 http://127.0.0.1:5000
"""

import logging
import os

from flask import Flask

from config import Config
from scheduler.db import close_db, init_db
from scheduler.routes import api_bp, line_bp, web_bp


def create_app(config_object=Config) -> Flask:
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object(config_object)
    app.config["DB_PATH"] = config_object.DB_PATH
    app.config["MAX_CONSECUTIVE_DAYS"] = config_object.MAX_CONSECUTIVE_DAYS
    app.config["MIN_REST_HOURS"] = config_object.MIN_REST_HOURS
    app.config["APP_NAME"] = config_object.APP_NAME

    # 連不上資料庫時不要讓整個程式起不來 —— 記下錯誤,讓使用者還能進後台看設定頁
    app.config["DB_ERROR"] = config_object.DATABASE_URL_ERROR
    if not app.config["DB_ERROR"]:
        try:
            init_db(app)
        except Exception as exc:                        # noqa: BLE001
            app.config["DB_ERROR"] = f"連不上資料庫:{exc}"
            app.logger.error(app.config["DB_ERROR"])

    app.teardown_appcontext(close_db)

    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(line_bp)

    @app.context_processor
    def inject_globals():
        return {
            "app_name": app.config["APP_NAME"],
            "line_configured": bool(app.config.get("LINE_CHANNEL_ACCESS_TOKEN")),
            "db_error": app.config.get("DB_ERROR", ""),
        }

    if not app.config["DB_ERROR"]:
        with app.app_context():
            from scheduler.seed import seed_if_empty

            try:
                if seed_if_empty():
                    app.logger.info("已建立範例員工與班別")
            except Exception as exc:                    # noqa: BLE001
                app.config["DB_ERROR"] = f"資料庫讀取失敗:{exc}"
                app.logger.error(app.config["DB_ERROR"])

    # CLI:python -m flask --app app seed
    @app.cli.command("seed")
    def seed_command():
        """灌入範例資料(資料庫是空的才會執行)。"""
        from scheduler.seed import seed_if_empty

        print("已灌入範例資料" if seed_if_empty() else "已經有資料,略過")

    return app


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
app = create_app()

if __name__ == "__main__":
    # Hub 啟動時會傳 PORT 環境變數;單獨執行時沿用預設 5000
    port = int(os.environ.get("PORT") or os.environ.get("FLASK_RUN_PORT") or 5000)
    where = "Supabase (PostgreSQL)" if Config.uses_supabase() else f"本機 SQLite  {Config.DB_PATH}"
    print(f"\n  {Config.APP_NAME}  →  http://127.0.0.1:{port}")
    print(f"  資料庫:{where}")
    if app.config.get("DB_ERROR"):
        print(f"  [!] {app.config['DB_ERROR']}")
    print(f"  後台密碼:{Config.ADMIN_PASSWORD}")
    print(f"  員工自助頁:http://127.0.0.1:{port}/liff?emp=1\n")
    app.run(host="0.0.0.0", port=port, debug=True)
