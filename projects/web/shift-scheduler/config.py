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

    # ---- 資料庫 ----
    # 有填 SUPABASE_DB_URL(或 DATABASE_URL)就用 Supabase,沒填就用本機 SQLite。
    # 連線字串要用 Supabase 後台的 Connection Pooler 位址,不要用直連位址,
    # 因為直連主機只有 IPv6,這台電腦連不上去。
    DATABASE_URL = ""
    DATABASE_URL_ERROR = ""

    DB_PATH = str(DATA_DIR / "shift.db")
    DB_POOL_SIZE = int(os.getenv("DB_POOL_SIZE", "8"))
    DB_CONNECT_TIMEOUT = int(os.getenv("DB_CONNECT_TIMEOUT", "10"))

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
    def uses_supabase(cls) -> bool:
        return bool(cls.DATABASE_URL)

    @classmethod
    def line_enabled(cls) -> bool:
        """有填 token 才算真的接上 LINE,否則走 demo 模式。"""
        return bool(cls.LINE_CHANNEL_ACCESS_TOKEN and cls.LINE_CHANNEL_SECRET)


def _load_database_url() -> None:
    """讀 .env 的 Supabase 連線字串並整理格式。

    格式有問題時不讓程式直接掛掉,而是記下錯誤訊息、退回 SQLite,
    這樣使用者還是進得了後台,能在「設定」頁看到到底哪裡填錯。
    """
    from scheduler.db import DbUrlError, normalize_db_url

    raw = os.getenv("SUPABASE_DB_URL") or os.getenv("DATABASE_URL") or ""
    if not raw:
        return
    try:
        Config.DATABASE_URL = normalize_db_url(raw)
    except DbUrlError as exc:
        Config.DATABASE_URL_ERROR = str(exc)


_load_database_url()
