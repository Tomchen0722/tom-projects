"""台股波段系統｜資料層設定。

集中管理所有「魔術數字」與資料集規格：FinMind 資料集名稱、必要欄位、
免費/付費層級、公布時間（供 available_date 使用），以及快取路徑與 API 端點。

⚠️ FinMind 資料集英文名稱與欄位依官方文件重建，實作連線前請以 FinMind
   llms-full.txt / DataList 頁面核對，不符再於此處集中修改即可。
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

# ── API 端點 ──────────────────────────────────────────────
FINMIND_DATA_URL: str = "https://api.finmindtrade.com/api/v4/data"
FINMIND_USER_INFO_URL: str = "https://api.web.finmindtrade.com/v2/user_info"

# ── 速率與重試（免費註冊帳號上限 600/hr）──────────────────
FREE_TIER_HOURLY_LIMIT: int = 600
# 保守節流：預留 buffer，不打滿上限。預設每小時最多打 500 次。
DEFAULT_HOURLY_BUDGET: int = 500
MAX_RETRIES: int = 3
BACKOFF_BASE_SECONDS: float = 2.0  # 指數退避基數：2, 4, 8 秒

# ── 快取 ──────────────────────────────────────────────────
# 預設快取目錄（相對於專案根）。呼叫端可覆寫。
DEFAULT_CACHE_DIR: Path = Path("data") / "cache"

# ── 環境變數名稱（token 不寫死於程式碼）───────────────────
TOKEN_ENV_VAR: str = "FINMIND_TOKEN"

# ── 三大法人類別在 institutional 資料 name 欄位的值 ────────
# 已用實際資料核對（2024 樣本 unique name 值）。
INSTITUTION_NAMES: dict[str, str] = {
    "investment_trust": "Investment_Trust",   # 投信
    "foreign": "Foreign_Investor",            # 外資及陸資（不含外資自營）
    "foreign_dealer_self": "Foreign_Dealer_Self",  # 外資自營商
    "dealer_self": "Dealer_self",             # 自營商（自行買賣）
    "dealer_hedging": "Dealer_Hedging",       # 自營商（避險）
}

# ── 融資融券欄名（已用實際 margin 資料核對）────────────────
MARGIN_COLS: dict[str, str] = {
    "margin_balance": "MarginPurchaseTodayBalance",   # 融資今日餘額
    "margin_balance_prev": "MarginPurchaseYesterdayBalance",  # 融資昨日餘額
    "margin_limit": "MarginPurchaseLimit",            # 融資限額
    "short_balance": "ShortSaleTodayBalance",         # 融券今日餘額
}

# ── P1 特徵設定（窗長等，集中避免魔術數字）────────────────
FEATURE_WINDOW_DAYS: int = 5  # N 日累積的預設窗長；屬超參數，交給裁判驗證，勿手調至最漂亮


@dataclass(frozen=True)
class DatasetSpec:
    """單一資料集的規格。

    參數:
        finmind_name: FinMind API 的 dataset 字串。
        required_cols: 回傳資料必須包含的欄位（缺一即報錯）。
        tier: "free" 或 "paid"；paid 在免費帳號會被跳過並提示。
        release: 公布時間描述（人類可讀）。
        frequency: "daily" 或 "weekly"，供 available_date 計算參考。

    例外:
        不主動拋出例外。
    """

    finmind_name: str
    required_cols: tuple[str, ...]
    tier: str
    release: str
    frequency: str


# 資料集登錄表：P1 所需 + 存活者/校正基礎設施 + P2(付費,先登錄後跳過)
DATASETS: dict[str, DatasetSpec] = {
    # ── P1 籌碼訊號 ──
    "institutional": DatasetSpec(
        finmind_name="TaiwanStockInstitutionalInvestorsBuySell",
        required_cols=("date", "stock_id", "name", "buy", "sell"),
        tier="free",
        release="T 日盤後（當日晚間），可用於 T+1 決策",
        frequency="daily",
    ),
    "holding_shares": DatasetSpec(
        finmind_name="TaiwanStockHoldingSharesPer",
        required_cols=("date", "stock_id", "HoldingSharesLevel", "people", "percent"),
        tier="paid",  # 集保股權分散為 FinMind 贊助限定，免費帳號回 400，自動跳過
        release="週更（集保每週結算，約週末公布，含數日 lag）",
        frequency="weekly",
    ),
    # ── 校正 / 對齊基礎設施 ──
    "price": DatasetSpec(
        finmind_name="TaiwanStockPrice",
        required_cols=("date", "stock_id", "open", "max", "min", "close", "Trading_Volume"),
        tier="free",
        release="T 日盤後",
        frequency="daily",
    ),
    "price_adj": DatasetSpec(
        finmind_name="TaiwanStockPriceAdj",
        required_cols=("date", "stock_id", "open", "max", "min", "close", "Trading_Volume"),
        tier="paid",  # 還原股價為 FinMind 贊助限定；免費層改用 price + 除權息自行還原
        release="T 日盤後",
        frequency="daily",
    ),
    "margin": DatasetSpec(
        finmind_name="TaiwanStockMarginPurchaseShortSale",
        # 保守列必要欄位，完整欄位待連線驗證後補全
        required_cols=("date", "stock_id"),
        tier="free",
        release="T 日盤後，可用於 T+1 決策",
        frequency="daily",
    ),
    "trading_date": DatasetSpec(
        finmind_name="TaiwanStockTradingDate",
        required_cols=("date",),
        tier="free",
        release="年度公告",
        frequency="daily",
    ),
    "stock_info": DatasetSpec(
        finmind_name="TaiwanStockInfo",
        required_cols=("stock_id", "stock_name", "industry_category", "type"),
        tier="free",
        release="不定期更新",
        frequency="daily",
    ),
    "delisting": DatasetSpec(
        finmind_name="TaiwanStockDelisting",
        required_cols=("date", "stock_id"),
        tier="free",
        release="事件發生時",
        frequency="daily",
    ),
    "dividend_result": DatasetSpec(
        finmind_name="TaiwanStockDividendResult",
        required_cols=("date", "stock_id", "before_price", "after_price"),
        tier="free",
        release="除權息時（含除息前後參考價，供還原）",
        frequency="daily",
    ),
    # ── P2 主力分點（免費帳號為付費資料集，先登錄，實作時自動跳過）──
    "broker_report": DatasetSpec(
        finmind_name="TaiwanStockTradingDailyReport",
        required_cols=("date", "securities_trader_id", "stock_id", "buy", "sell"),
        tier="paid",
        release="T 日盤後",
        frequency="daily",
    ),
}
