"""自動排班系統 — Flask 進入點。

啟動:
    python app.py
然後打開 http://127.0.0.1:5000
"""

import logging

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

    init_db(app.config["DB_PATH"])
    app.teardown_appcontext(close_db)

    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(line_bp)

    @app.context_processor
    def inject_globals():
        return {
            "app_name": app.config["APP_NAME"],
            "line_configured": bool(app.config.get("LINE_CHANNEL_ACCESS_TOKEN")),
        }

    with app.app_context():
        from scheduler.seed import seed_if_empty

        if seed_if_empty():
            app.logger.info("已建立範例員工與班別")

    # CLI:python -m flask --app app seed / reset
    @app.cli.command("seed")
    def seed_command():
        """灌入範例資料(資料庫是空的才會執行)。"""
        from scheduler.seed import seed_if_empty

        print("已灌入範例資料" if seed_if_empty() else "已經有資料,略過")

    return app


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
app = create_app()

if __name__ == "__main__":
    print(f"\n  {Config.APP_NAME}  →  http://127.0.0.1:5000")
    print(f"  後台密碼:{Config.ADMIN_PASSWORD}")
    print(f"  員工自助頁:http://127.0.0.1:5000/liff?emp=1\n")
    app.run(host="0.0.0.0", port=5000, debug=True)
