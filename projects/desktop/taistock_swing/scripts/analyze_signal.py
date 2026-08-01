"""台股波段系統｜訊號品質分析（在本機用真實資料執行）。

直球檢驗各籌碼訊號對未來報酬的預測力：逐日橫斷面 IC、ICIR、t 值、勝率，
以及主訊號的分位數分析（高訊號組 vs 低訊號組未來報酬）。

執行（專案根目錄）：
    python scripts/analyze_signal.py
"""
from __future__ import annotations

import sys
from pathlib import Path

# 強制 UTF-8 輸出，避免 Windows cp950 主控台編碼崩潰
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import pandas as pd  # noqa: E402

from data_panel import build_adjusted_price_panel, fetch_universe_long  # noqa: E402
from data_source import DataSource  # noqa: E402
from features_chip import build_institutional_features, build_margin_features  # noqa: E402
from signal_quality import compute_forward_returns, compute_ic, quantile_analysis  # noqa: E402

# 沿用回測的股票池與期間
UNIVERSE: list[str] = [
    "2330", "2317", "2454", "2308", "2382", "2412", "2881", "2882", "2886", "2891",
    "1301", "1303", "2002", "2603", "2379", "2357", "2409", "3008", "2303", "3711",
]
START_DATE: str = "2022-01-01"
END_DATE: str = "2024-12-31"
HORIZONS: list[int] = [5, 10, 20]          # 持有天數
MAIN_SIGNAL: str = "inst_net_5d"           # 主訊號：投信 5 日累積買超


def _to_panel(feature_panel: pd.DataFrame, col: str) -> pd.DataFrame:
    """把 tidy 特徵面板的某欄轉成 date × stock_id 寬面板。"""
    p = feature_panel.copy()
    p["date"] = pd.to_datetime(p["date"])
    return p.pivot_table(index="date", columns="stock_id", values=col, aggfunc="last")


def main() -> int:
    """執行訊號品質分析並印出比較表。"""
    print("=" * 60)
    print(f"訊號品質分析（IC）｜{START_DATE} ~ {END_DATE}｜{len(UNIVERSE)} 檔")
    print("=" * 60)

    ds = DataSource()
    print("\n抓取資料（走快取）…")
    data = fetch_universe_long(ds, UNIVERSE, START_DATE, END_DATE)

    price_panel = build_adjusted_price_panel(data["price"], data["dividend"])
    inst_feat = build_institutional_features(data["institutional"], price_df=data["price"])
    margin_feat = build_margin_features(data["margin"], price_df=data["price"])

    # 要檢驗的訊號：(顯示名, 來源面板, 欄名)
    signals: list[tuple[str, pd.DataFrame, str]] = [
        ("投信5日累積", inst_feat, "inst_net_5d"),
        ("投信單日", inst_feat, "inst_net"),
        ("外資5日累積", inst_feat, "foreign_net_5d"),
        ("三大法人5日", inst_feat, "total_net_5d"),
        ("券資比", margin_feat, "short_margin_ratio"),
        ("融資5日變化", margin_feat, "margin_chg_pct_5d"),
    ]

    # 預先算各持有期的未來報酬
    fwd_by_h = {h: compute_forward_returns(price_panel, horizon=h, exec_lag=1) for h in HORIZONS}

    print("\n各訊號 × 持有期的平均 IC（括號為 ICIR）：")
    header = f"{'訊號':<14}" + "".join(f"{f'{h}日':>16}" for h in HORIZONS)
    print("-" * 60)
    print(header)
    print("-" * 60)
    for name, panel, col in signals:
        if col not in panel.columns:
            print(f"{name:<14}（無此欄，略）")
            continue
        sig_panel = _to_panel(panel, col)
        cells = []
        for h in HORIZONS:
            _, summ = compute_ic(sig_panel, fwd_by_h[h], min_names=5)
            cells.append(f"{summ['mean_ic']:+.3f}({summ['icir']:+.2f})")
        print(f"{name:<14}" + "".join(f"{c:>16}" for c in cells))
    print("-" * 60)

    # 主訊號的詳細摘要與分位數分析（持有 10 日）
    print(f"\n主訊號『{MAIN_SIGNAL}』詳細（持有 10 日）：")
    main_panel = _to_panel(inst_feat, MAIN_SIGNAL)
    ic_series, summ = compute_ic(main_panel, fwd_by_h[10], min_names=5)
    print(
        f"  平均 IC={summ['mean_ic']:+.4f}　ICIR={summ['icir']:+.3f}　"
        f"t值={summ['t_stat']:+.2f}　勝率={summ['hit_rate']:.1%}　有效天數={int(summ['n_periods'])}"
    )
    print("  （註：未來報酬期重疊會使 t 值偏樂觀，僅供粗略參考）")

    q = quantile_analysis(main_panel, fwd_by_h[10], n_quantiles=3)
    print("\n  分位數分析（依投信5日累積分 3 組，持有 10 日平均報酬）：")
    labels = {0: "低訊號組", 1: "中訊號組", 2: "高訊號組"}
    for idx, row in q.iterrows():
        name = labels.get(idx, str(idx))
        print(f"    {name:<12}{row['mean_forward_return']:+.3%}")

    print("\n" + "=" * 60)
    print("判讀指引：股票日頻橫斷面訊號，|平均IC|≈0.02~0.05 已算有料；")
    print("IC 接近 0、且分位數多空價差不顯著 → 訊號幾乎沒有預測力。")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
