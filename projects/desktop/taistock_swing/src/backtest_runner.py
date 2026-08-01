"""台股波段系統｜回測核心 runner（與介面解耦）。

把「一組參數 → 評估報告」的流程抽成純協調函式，供 GUI 與 CLI 共用。
以 log 回呼輸出進度，讓呼叫端（GUI 文字框 / 主控台）自行決定顯示方式。
"""
from __future__ import annotations

from typing import Callable

from data_panel import build_adjusted_price_panel, fetch_benchmark_returns, fetch_universe_long
from evaluation import evaluate
from features_chip import build_institutional_features, build_margin_features
from signals import build_composite_signal, feature_to_panel
from strategy_baseline import build_weight_matrix

# 介面可選的訊號 → (來源, 欄名)。"composite" 為外資+融資反向複合訊號。
SINGLE_SIGNALS: dict[str, str] = {
    "投信5日買超": "inst_net_5d",
    "外資5日買超": "foreign_net_5d",
    "三大法人5日": "total_net_5d",
}
SIGNAL_CHOICES: list[str] = ["外資+融資反向(複合)", *SINGLE_SIGNALS.keys()]


def _build_signal(choice: str, inst_feat, margin_feat):
    """依選擇建立 (訊號 tidy 面板, 訊號欄名)。

    參數:
        choice: SIGNAL_CHOICES 之一。
        inst_feat: 三大法人特徵面板。
        margin_feat: 融資融券特徵面板。

    回傳:
        (tidy 面板, signal_col 欄名)。

    例外:
        ValueError: 當 choice 不在支援清單。
    """
    if choice.startswith("外資+融資"):
        foreign_wide = feature_to_panel(inst_feat, "foreign_net_5d")
        margin_wide = feature_to_panel(margin_feat, "margin_chg_pct_5d")
        composite = build_composite_signal([(foreign_wide, 1.0), (margin_wide, -1.0)])
        return composite, "composite_signal"
    if choice in SINGLE_SIGNALS:
        return inst_feat, SINGLE_SIGNALS[choice]
    raise ValueError(f"未知訊號選擇：{choice}。可用：{SIGNAL_CHOICES}")


def run_backtest_pipeline(
    params: dict,
    data_source,
    log: Callable[[str], None] = print,
) -> dict[str, object]:
    """由參數與資料源跑完整回測，回傳評估結果。

    參數:
        params: 含 universe(list[str])、start(str)、end(str)、benchmark_id(str)、
                top_k(int)、rebalance_days(int)、signal_choice(str)。
        data_source: DataSource 實例（或具相同介面的 mock）。
        log: 進度輸出回呼，預設 print。

    回傳:
        evaluate 的結果 dict（含 report、metrics、yearly、verdict、returns）。

    例外:
        ValueError: 參數不合法（空股票池、抓不到資料等）。
    """
    universe = [s.strip() for s in params["universe"] if s.strip()]
    if not universe:
        raise ValueError("股票代碼不可為空。")

    log(f"抓取 {len(universe)} 檔資料（首次較慢，之後走快取）…")
    data = fetch_universe_long(data_source, universe, params["start"], params["end"])
    if data["price"].empty:
        raise ValueError("抓不到價格資料，請確認股票代碼、日期與 token。")

    log("建立籌碼特徵…")
    inst_feat = build_institutional_features(data["institutional"], price_df=data["price"])
    margin_feat = build_margin_features(data["margin"], price_df=data["price"])

    log(f"建立訊號（{params['signal_choice']}）與還原股價面板…")
    signal_panel, signal_col = _build_signal(params["signal_choice"], inst_feat, margin_feat)
    price_panel = build_adjusted_price_panel(data["price"], data["dividend"])
    if price_panel.empty:
        raise ValueError("還原股價面板為空。")

    weights = build_weight_matrix(
        signal_panel,
        price_panel.index,
        signal_col=signal_col,
        top_k=int(params["top_k"]),
        rebalance_days=int(params["rebalance_days"]),
    )

    log(f"抓基準（{params['benchmark_id']}）並交裁判評分…")
    benchmark = fetch_benchmark_returns(data_source, params["benchmark_id"], params["start"], params["end"])

    result = evaluate(weights, price_panel, benchmark)
    log("完成。")
    return result
