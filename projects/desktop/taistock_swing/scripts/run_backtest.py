"""台股波段系統｜端到端回測（在本機用真實 FinMind 資料執行）。

流程：抓資料 → 建籌碼特徵 → 複合訊號權重 → 裁判評分 → 印報告。
價格採用還原股價（免費 TaiwanStockPrice + 除權息結果表自行還原），除權息假跌已校正。
訊號依 IC 分析挑選：外資5日累積買超(+1) + 融資5日變化(反指標,-1)。

執行（專案根目錄）：
    python scripts/run_backtest.py
"""
from __future__ import annotations

import sys
from pathlib import Path

# 強制 UTF-8 輸出，避免 Windows cp950 主控台編不動報告符號而崩潰
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from data_panel import (  # noqa: E402
    build_adjusted_price_panel,
    fetch_benchmark_returns,
    fetch_universe_long,
)
from data_source import DataSource  # noqa: E402
from evaluation import evaluate  # noqa: E402
from features_chip import build_institutional_features, build_margin_features  # noqa: E402
from signals import build_composite_signal, feature_to_panel  # noqa: E402
from strategy_baseline import DEFAULT_REBALANCE_DAYS, DEFAULT_TOP_K, build_weight_matrix  # noqa: E402

# ── 回測設定（可自行調整）─────────────────────────────────
# 股票池放大到約 50 檔（降低橫斷面 IC 的雜訊）
UNIVERSE: list[str] = [
    "2330", "2317", "2454", "2308", "2382", "2412", "2881", "2882", "2886", "2891",
    "1301", "1303", "2002", "2603", "2379", "2357", "2409", "3008", "2303", "3711",
    "2884", "2885", "2887", "2890", "2892", "5880", "2880", "2883", "2609", "2615",
    "1216", "1101", "1102", "2207", "2301", "2327", "2345", "2377", "2395", "3034",
    "3231", "2408", "3037", "4938", "2912", "2105", "2474", "3045", "4904", "6505",
]
BENCHMARK_ID: str = "0050"
START_DATE: str = "2022-01-01"  # 含 2022 下跌年，可檢驗體制轉換
END_DATE: str = "2024-12-31"


def main() -> int:
    """執行端到端回測並印出評估報告。

    回傳:
        0 表示流程完整跑通；非 0 表示中途失敗。

    例外:
        不主動拋出例外；資料層/評估層的例外會冒泡由 Python 顯示。
    """
    print("=" * 56)
    print(f"端到端回測｜{START_DATE} ~ {END_DATE}｜{len(UNIVERSE)} 檔")
    print("=" * 56)

    ds = DataSource()

    print("\n[1/4] 抓取股票池資料（首次較慢，之後走快取）…")
    data = fetch_universe_long(ds, UNIVERSE, START_DATE, END_DATE)
    print(
        f"  price={len(data['price'])} 筆、institutional={len(data['institutional'])} 筆、"
        f"margin={len(data['margin'])} 筆、dividend={len(data['dividend'])} 筆"
    )

    print("\n[2/4] 建立籌碼特徵（投信/外資 + 融資融券）…")
    inst_feat = build_institutional_features(data["institutional"], price_df=data["price"])
    margin_feat = build_margin_features(data["margin"], price_df=data["price"])
    print(f"  三大法人特徵 {len(inst_feat)} 列、融資融券特徵 {len(margin_feat)} 列")

    print("\n[3/4] 建立還原股價面板與複合訊號策略權重…")
    price_panel = build_adjusted_price_panel(data["price"], data["dividend"])
    # 依 IC 分析挑出真正有 edge 的訊號：外資5日累積(+1) + 融資5日變化(反指標,-1)
    foreign_wide = feature_to_panel(inst_feat, "foreign_net_5d")
    margin_wide = feature_to_panel(margin_feat, "margin_chg_pct_5d")
    composite = build_composite_signal([(foreign_wide, 1.0), (margin_wide, -1.0)])
    weights = build_weight_matrix(
        composite,
        price_panel.index,
        signal_col="composite_signal",
        top_k=DEFAULT_TOP_K,
        rebalance_days=DEFAULT_REBALANCE_DAYS,
    )
    print(f"  價格面板 {price_panel.shape[0]} 日 × {price_panel.shape[1]} 檔；訊號=外資買超+融資反向")

    print("\n[4/4] 抓基準（0050，同樣還原）並交裁判評分…")
    benchmark = fetch_benchmark_returns(ds, BENCHMARK_ID, START_DATE, END_DATE)
    result = evaluate(weights, price_panel, benchmark)

    print("\n" + result["report"])
    print("\n✔ 本次已用還原股價（除權息校正）+ 依 IC 挑選的複合訊號。")
    print(f"  本次資料層取用次數：{len(ds.provider_log)}（含快取命中）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
