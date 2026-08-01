"""台股波段系統｜策略評估框架（裁判）。

本模組是整個系統的「裁判」：在建任何模型或特徵之前先存在，
用一致、誠實的標準判定一條策略「是否有效」，杜絕自我欺騙。

核心紀律：
1. 成本內建進報酬（手續費、證交稅、滑價），不是事後才扣。
2. 防未來函數：決策日 T 的權重，套用執行延遲後才實現報酬。
3. 只看風險調整後報酬：用 3 倍風險多賺 20% 不是 alpha，是槓桿。
4. 及格線先寫死：淨超額 > 0、Sharpe 明顯優於 benchmark、撐得過下跌年。

本模組為純運算，不連任何外部網路。
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

# 一年的交易日數，用於年化換算（台股約 245~252，取 252 為業界慣例）
_TRADING_DAYS_PER_YEAR: int = 252


@dataclass(frozen=True)
class CostConfig:
    """交易成本設定（台股波段實況）。

    參數:
        fee_rate: 券商手續費牌告費率，台股為 0.001425（0.1425%）。
        fee_discount: 手續費折數，例如 6 折填 0.6。
        tax_rate: 證券交易稅率，一般賣出為 0.003（0.3%）；波段不套用當沖減半。
        slippage_rate: 單邊滑價假設（比率），例如 5 bps 填 0.0005。

    例外:
        不主動拋出例外；不合理數值（如負費率）由呼叫端負責。
    """

    fee_rate: float = 0.001425
    fee_discount: float = 0.6
    tax_rate: float = 0.003
    slippage_rate: float = 0.0005

    @property
    def buy_cost_rate(self) -> float:
        """買進單邊成本率（手續費 + 滑價）。"""
        return self.fee_rate * self.fee_discount + self.slippage_rate

    @property
    def sell_cost_rate(self) -> float:
        """賣出單邊成本率（手續費 + 證交稅 + 滑價）。"""
        return self.fee_rate * self.fee_discount + self.tax_rate + self.slippage_rate


@dataclass(frozen=True)
class VerdictConfig:
    """及格線設定。門檻集中管理，避免魔術數字散落各處。

    參數:
        min_excess_ann_return: 年化淨超額報酬的最低要求，預設 0（需為正）。
        min_sharpe_margin: 策略 Sharpe 需高於 benchmark 的最小差距，預設 0.2（「明顯」）。
        require_survive_down_years: 是否要求在 benchmark 為負的年份，策略當年報酬 >= benchmark。
    """

    min_excess_ann_return: float = 0.0
    min_sharpe_margin: float = 0.2
    require_survive_down_years: bool = True


@dataclass(frozen=True)
class BacktestConfig:
    """回測執行設定。

    參數:
        exec_lag: 決策到執行的延遲交易日數。預設 1，代表「T 日用當晚可得資料
                  決策，T+1 執行」，這是評估層防未來函數的關鍵開關。
        risk_free_annual: 年化無風險利率，用於 Sharpe/Sortino，預設 0。
    """

    exec_lag: int = 1
    risk_free_annual: float = 0.0


def compute_strategy_returns(
    weights: pd.DataFrame,
    prices: pd.DataFrame,
    cost: CostConfig,
    backtest: BacktestConfig,
) -> pd.DataFrame:
    """由每日目標權重與還原股價，計算扣成本後的每日策略報酬。

    參數:
        weights: 每日目標權重矩陣，index 為日期（datetime），columns 為股票代碼，
                 值為當日目標權重（0 表示不持有）；每列權重和 <= 1，其餘視為現金。
        prices: 還原股價矩陣，index 為日期，columns 為股票代碼，值為調整後收盤價。
                欄位需涵蓋 weights 的所有股票。
        cost: 交易成本設定。
        backtest: 回測執行設定（含防未來函數的 exec_lag）。

    回傳:
        DataFrame，index 為日期，包含欄位：
            gross_return（毛報酬）、cost（當日成本）、net_return（淨報酬）、
            turnover（當日雙邊換手率）。

    例外:
        ValueError: 當輸入為空、weights 有欄位不在 prices 中、或 index 非日期型別。
    """
    if weights.empty or prices.empty:
        raise ValueError("weights 或 prices 為空，無法回測。請確認輸入資料。")

    missing = set(weights.columns) - set(prices.columns)
    if missing:
        raise ValueError(f"prices 缺少 weights 中的股票欄位：{sorted(missing)}")

    if not isinstance(weights.index, pd.DatetimeIndex):
        raise ValueError("weights.index 必須是 DatetimeIndex（日期），目前不是。")
    if not isinstance(prices.index, pd.DatetimeIndex):
        raise ValueError("prices.index 必須是 DatetimeIndex（日期），目前不是。")

    # 以 weights 的日期為主軸，對齊還原股價並只取相關股票欄位
    prices_aligned = prices.reindex(weights.index)[weights.columns].sort_index()
    weights = weights.sort_index()

    # 每日資產報酬（還原股價的日變動率）；fill_method=None 不前向填補缺值
    asset_returns = prices_aligned.pct_change(fill_method=None)

    # 防未來函數：T 日決策的權重，位移 exec_lag 後才生效（在 T+lag 開始賺報酬）
    effective_weights = weights.shift(backtest.exec_lag).fillna(0.0)

    # 毛報酬：生效權重 × 當日資產報酬（缺值資產報酬視為 0，不貢獻損益）
    gross_return = (effective_weights * asset_returns.fillna(0.0)).sum(axis=1)

    # 換手：生效權重相對前一日的變化。買進與賣出成本率不同，需分開計。
    weight_change = effective_weights.diff().fillna(effective_weights)
    buy_turnover = weight_change.clip(lower=0.0).sum(axis=1)   # 權重增加 = 買進
    sell_turnover = (-weight_change.clip(upper=0.0)).sum(axis=1)  # 權重減少 = 賣出
    turnover = buy_turnover + sell_turnover

    cost_series = buy_turnover * cost.buy_cost_rate + sell_turnover * cost.sell_cost_rate

    net_return = gross_return - cost_series

    return pd.DataFrame(
        {
            "gross_return": gross_return,
            "cost": cost_series,
            "net_return": net_return,
            "turnover": turnover,
        }
    )


def _max_drawdown(returns: pd.Series) -> float:
    """計算最大回撤（回傳負值或 0）。

    參數:
        returns: 每日報酬序列。

    回傳:
        最大回撤（float，<= 0）。空序列回傳 0.0。
    """
    if returns.empty:
        return 0.0
    equity = (1.0 + returns).cumprod()
    running_max = equity.cummax()
    drawdown = equity / running_max - 1.0
    return float(drawdown.min())


def compute_metrics(
    net_return: pd.Series,
    benchmark_return: pd.Series,
    backtest: BacktestConfig,
) -> dict[str, float]:
    """計算風險調整後績效指標，並與 benchmark 對比。

    參數:
        net_return: 策略每日淨報酬序列（已扣成本）。
        benchmark_return: 對照基準（如 0050 買進持有）每日報酬序列，index 需可與策略對齊。
        backtest: 回測設定（提供無風險利率）。

    回傳:
        dict，包含策略與基準的年化報酬、年化波動、Sharpe、Sortino、
        最大回撤、Calmar、累積報酬、勝率、盈虧比，以及年化淨超額報酬與 Sharpe 差距。

    例外:
        ValueError: 當 net_return 為空。
    """
    if net_return.empty:
        raise ValueError("net_return 為空，無法計算指標。")

    # 對齊策略與基準的共同交易日，避免長度不一造成的偏誤
    bench = benchmark_return.reindex(net_return.index).fillna(0.0)
    rf_daily = backtest.risk_free_annual / _TRADING_DAYS_PER_YEAR

    def _stats(r: pd.Series) -> dict[str, float]:
        """單一報酬序列的統計摘要。"""
        n = len(r)
        cumulative = float((1.0 + r).prod() - 1.0)
        # 年化報酬用幾何法，避免高波動下算術平均高估
        ann_return = float((1.0 + cumulative) ** (_TRADING_DAYS_PER_YEAR / n) - 1.0) if n > 0 else 0.0
        ann_vol = float(r.std(ddof=1) * np.sqrt(_TRADING_DAYS_PER_YEAR)) if n > 1 else 0.0
        excess = r - rf_daily
        sharpe = float(excess.mean() * _TRADING_DAYS_PER_YEAR / ann_vol) if ann_vol > 0 else 0.0
        downside = r[r < 0]
        downside_vol = float(downside.std(ddof=1) * np.sqrt(_TRADING_DAYS_PER_YEAR)) if len(downside) > 1 else 0.0
        sortino = float(excess.mean() * _TRADING_DAYS_PER_YEAR / downside_vol) if downside_vol > 0 else 0.0
        mdd = _max_drawdown(r)
        calmar = float(ann_return / abs(mdd)) if mdd < 0 else 0.0
        wins = r[r > 0]
        losses = r[r < 0]
        win_rate = float((r > 0).mean()) if n > 0 else 0.0
        profit_loss_ratio = (
            float(wins.mean() / abs(losses.mean())) if len(wins) > 0 and len(losses) > 0 else 0.0
        )
        return {
            "cumulative_return": cumulative,
            "ann_return": ann_return,
            "ann_vol": ann_vol,
            "sharpe": sharpe,
            "sortino": sortino,
            "max_drawdown": mdd,
            "calmar": calmar,
            "win_rate": win_rate,
            "profit_loss_ratio": profit_loss_ratio,
        }

    strat = _stats(net_return)
    bmk = _stats(bench)

    metrics: dict[str, float] = {}
    for key, value in strat.items():
        metrics[f"strategy_{key}"] = value
    for key, value in bmk.items():
        metrics[f"benchmark_{key}"] = value

    metrics["excess_ann_return"] = strat["ann_return"] - bmk["ann_return"]
    metrics["sharpe_margin"] = strat["sharpe"] - bmk["sharpe"]
    return metrics


def yearly_breakdown(
    net_return: pd.Series,
    benchmark_return: pd.Series,
) -> pd.DataFrame:
    """分年度績效拆解，用於檢驗策略在下跌年的體質。

    參數:
        net_return: 策略每日淨報酬序列。
        benchmark_return: 基準每日報酬序列。

    回傳:
        DataFrame，index 為年度，欄位為 strategy_return、benchmark_return、
        excess_return、strategy_max_drawdown。空輸入回傳空 DataFrame。
    """
    if net_return.empty:
        return pd.DataFrame(
            columns=["strategy_return", "benchmark_return", "excess_return", "strategy_max_drawdown"]
        )

    bench = benchmark_return.reindex(net_return.index).fillna(0.0)
    rows: list[dict[str, float]] = []
    for year, idx in net_return.groupby(net_return.index.year).groups.items():
        s = net_return.loc[idx]
        b = bench.loc[idx]
        s_ret = float((1.0 + s).prod() - 1.0)
        b_ret = float((1.0 + b).prod() - 1.0)
        rows.append(
            {
                "year": int(year),
                "strategy_return": s_ret,
                "benchmark_return": b_ret,
                "excess_return": s_ret - b_ret,
                "strategy_max_drawdown": _max_drawdown(s),
            }
        )
    return pd.DataFrame(rows).set_index("year")


def verdict(
    metrics: dict[str, float],
    yearly: pd.DataFrame,
    config: VerdictConfig,
) -> dict[str, object]:
    """依及格線判定策略是否通過。

    參數:
        metrics: compute_metrics 的輸出。
        yearly: yearly_breakdown 的輸出。
        config: 及格線設定。

    回傳:
        dict，包含各項判定（excess_return_ok、sharpe_ok、survive_down_years_ok）
        與 overall_pass（全部通過才為 True）。

    例外:
        不主動拋出例外。
    """
    excess_ok = metrics.get("excess_ann_return", 0.0) > config.min_excess_ann_return
    sharpe_ok = metrics.get("sharpe_margin", 0.0) >= config.min_sharpe_margin

    survive_ok = True
    if config.require_survive_down_years and not yearly.empty:
        down_years = yearly[yearly["benchmark_return"] < 0]
        if not down_years.empty:
            # 下跌年要求：策略當年報酬不劣於基準（相對抗跌）
            survive_ok = bool((down_years["excess_return"] >= 0).all())

    overall = bool(excess_ok and sharpe_ok and survive_ok)
    return {
        "excess_return_ok": bool(excess_ok),
        "sharpe_ok": bool(sharpe_ok),
        "survive_down_years_ok": bool(survive_ok),
        "overall_pass": overall,
    }


def format_report(
    metrics: dict[str, float],
    yearly: pd.DataFrame,
    verdict_result: dict[str, object],
) -> str:
    """把評估結果組成一份可讀的繁體中文報告字串。

    參數:
        metrics: compute_metrics 的輸出。
        yearly: yearly_breakdown 的輸出。
        verdict_result: verdict 的輸出。

    回傳:
        報告字串（不含任何 print，由呼叫端決定輸出方式）。
    """
    def pct(x: float) -> str:
        return f"{x * 100:.2f}%"

    lines: list[str] = []
    lines.append("=" * 52)
    lines.append("台股波段系統｜策略評估報告")
    lines.append("=" * 52)
    lines.append(f"{'指標':<16}{'策略':>14}{'基準(0050)':>16}")
    lines.append("-" * 52)
    lines.append(f"{'累積報酬':<18}{pct(metrics['strategy_cumulative_return']):>12}{pct(metrics['benchmark_cumulative_return']):>16}")
    lines.append(f"{'年化報酬':<18}{pct(metrics['strategy_ann_return']):>12}{pct(metrics['benchmark_ann_return']):>16}")
    lines.append(f"{'年化波動':<18}{pct(metrics['strategy_ann_vol']):>12}{pct(metrics['benchmark_ann_vol']):>16}")
    lines.append(f"{'Sharpe':<20}{metrics['strategy_sharpe']:>10.2f}{metrics['benchmark_sharpe']:>16.2f}")
    lines.append(f"{'Sortino':<20}{metrics['strategy_sortino']:>10.2f}{metrics['benchmark_sortino']:>16.2f}")
    lines.append(f"{'最大回撤':<18}{pct(metrics['strategy_max_drawdown']):>12}{pct(metrics['benchmark_max_drawdown']):>16}")
    lines.append(f"{'Calmar':<20}{metrics['strategy_calmar']:>10.2f}{metrics['benchmark_calmar']:>16.2f}")
    lines.append(f"{'勝率':<19}{pct(metrics['strategy_win_rate']):>12}{pct(metrics['benchmark_win_rate']):>16}")
    lines.append("-" * 52)
    lines.append(f"年化淨超額報酬：{pct(metrics['excess_ann_return'])}    Sharpe 差距：{metrics['sharpe_margin']:+.2f}")
    lines.append("（提醒：勝率非主指標，風險調整後超額報酬才是。）")

    lines.append("")
    lines.append("分年度績效（檢驗下跌年體質）")
    lines.append("-" * 52)
    if yearly.empty:
        lines.append("（無資料）")
    else:
        lines.append(f"{'年度':<8}{'策略':>10}{'基準':>10}{'超額':>10}{'策略MDD':>12}")
        for year, row in yearly.iterrows():
            lines.append(
                f"{year:<8}{pct(row['strategy_return']):>10}{pct(row['benchmark_return']):>10}"
                f"{pct(row['excess_return']):>10}{pct(row['strategy_max_drawdown']):>12}"
            )

    lines.append("")
    lines.append("及格線判定")
    lines.append("-" * 52)
    def mark(ok: bool) -> str:
        """把布林判定轉成可讀標記。"""
        return "✔ 通過" if ok else "✘ 未過"
    lines.append(f"{mark(verdict_result['excess_return_ok'])}　淨超額報酬為正")
    lines.append(f"{mark(verdict_result['sharpe_ok'])}　Sharpe 明顯優於基準")
    lines.append(f"{mark(verdict_result['survive_down_years_ok'])}　撐得過下跌年")
    lines.append("=" * 52)
    overall = verdict_result["overall_pass"]
    lines.append(f"總判定：{'✔ PASS — 值得進入 paper trade' if overall else '✗ FAIL — 尚未證明有 edge'}")
    lines.append("=" * 52)
    return "\n".join(lines)


def evaluate(
    weights: pd.DataFrame,
    prices: pd.DataFrame,
    benchmark_return: pd.Series,
    cost: CostConfig | None = None,
    backtest: BacktestConfig | None = None,
    verdict_config: VerdictConfig | None = None,
) -> dict[str, object]:
    """一站式評估入口：由權重與價格算出報酬、指標、分年度與及格線判定。

    參數:
        weights: 每日目標權重矩陣。
        prices: 還原股價矩陣。
        benchmark_return: 基準每日報酬序列。
        cost: 成本設定，None 時用預設值。
        backtest: 回測設定，None 時用預設值。
        verdict_config: 及格線設定，None 時用預設值。

    回傳:
        dict，包含 returns（每日報酬明細 DataFrame）、metrics、yearly、
        verdict（判定）、report（繁中報告字串）。

    例外:
        ValueError: 由 compute_strategy_returns / compute_metrics 傳遞而來。
    """
    cost = cost or CostConfig()
    backtest = backtest or BacktestConfig()
    verdict_config = verdict_config or VerdictConfig()

    returns = compute_strategy_returns(weights, prices, cost, backtest)
    metrics = compute_metrics(returns["net_return"], benchmark_return, backtest)
    yearly = yearly_breakdown(returns["net_return"], benchmark_return)
    verdict_result = verdict(metrics, yearly, verdict_config)
    report = format_report(metrics, yearly, verdict_result)

    return {
        "returns": returns,
        "metrics": metrics,
        "yearly": yearly,
        "verdict": verdict_result,
        "report": report,
    }
