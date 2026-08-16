"""全站設定。所有可調參數集中在這裡。"""

import os
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:  # 沒裝 python-dotenv 也能跑,只是不讀 .env
    load_dotenv = None

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

if load_dotenv is not None:
    load_dotenv(BASE_DIR / ".env")


class Config:
    APP_NAME = "自動排班系統"

    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-change-me")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin1234")

    DB_PATH = str(DATA_DIR / "shift.db")

    # LINE
    LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET", "")
    LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", "")
    LINE_LIFF_ID = os.getenv("LINE_LIFF_ID", "")
    # LIFF 的身分驗證要用 LINE Login channel 的 Channel ID
    LINE_LOGIN_CHANNEL_ID = os.getenv("LINE_LOGIN_CHANNEL_ID", "")
    PUBLIC_BASE_URL = os.getenv("PUBLIC_BASE_URL", "http://127.0.0.1:5000").rstrip("/")

    # 排班預設規則
    MAX_CONSECUTIVE_DAYS = 6      # 最多連上幾天
    MIN_REST_HOURS = 11           # 兩班之間最少間隔時數
    DEFAULT_WEEK_START = 0        # 0=星期一

    @classmethod
    def line_enabled(cls) -> bool:
        """有填 token 才算真的接上 LINE,否則走 demo 模式。"""
        return bool(cls.LINE_CHANNEL_ACCESS_TOKEN and cls.LINE_CHANNEL_SECRET)
