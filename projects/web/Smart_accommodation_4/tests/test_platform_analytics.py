# -*- coding: utf-8 -*-
"""platform_analytics 純計算層單元測試（不讀真實資料、不需 streamlit）。"""
import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from modules import platform_analytics as pa


@pytest.fixture
def sample_df():
    """6 間房源 / 3 位房東 / 2 行政區 / 2 房型的合成母體。"""
    return pd.DataFrame({
        "id": [1, 2, 3, 4, 5, 6],
        "host_id": [10, 10, 20, 20, 30, 30],
        "neighbourhood_cleansed": ["大安區", "大安區", "大安區",
                                   "信義區", "信義區", "信義區"],
        "room_type": ["Entire home/apt", "Entire home/apt", "Private room",
                      "Entire home/apt", "Private room", "Private room"],
        "price": [1000.0, 2000.0, 1000.0, 3000.0, 1000.0, 1000.0],
        "vac_pred": [0.0, 0.5, 0.8, 0.2, 0.9, 0.9],
        "prob": [0.10, 0.40, 0.70, 0.20, 0.80, 0.90],
        "tier": ["green", "yellow", "red", "green", "red", "red"],
    })


def test_add_revenue_columns_計算年營收與平台收入(sample_df):
    out = pa.add_revenue_columns(sample_df, commission=0.15)
    # 房源 1：1000 × (1-0.0) × 365 = 365000
    assert out.loc[0, "est_annual_revenue"] == pytest.approx(365000.0)
    assert out.loc[0, "platform_revenue"] == pytest.approx(54750.0)
    # 房源 2：2000 × (1-0.5) × 365 = 365000
    assert out.loc[1, "est_annual_revenue"] == pytest.approx(365000.0)


def test_add_revenue_columns_不改動輸入(sample_df):
    pa.add_revenue_columns(sample_df, commission=0.15)
    assert "est_annual_revenue" not in sample_df.columns


def test_add_revenue_columns_缺值視為零(sample_df):
    d = sample_df.copy()
    d.loc[0, "price"] = None
    out = pa.add_revenue_columns(d, commission=0.15)
    assert out.loc[0, "est_annual_revenue"] == pytest.approx(0.0)


def test_market_kpis_基本統計(sample_df):
    k = pa.market_kpis(sample_df, commission=0.15)
    assert k["n_listings"] == 6
    assert k["n_hosts"] == 3
    assert k["avg_vacancy"] == pytest.approx((0.0+0.5+0.8+0.2+0.9+0.9) / 6)
    assert k["red_ratio"] == pytest.approx(3 / 6)
    assert k["yellow_ratio"] == pytest.approx(1 / 6)


def test_market_kpis_平台收入等於營收乘抽成(sample_df):
    k = pa.market_kpis(sample_df, commission=0.15)
    assert k["platform_revenue"] == pytest.approx(k["total_revenue"] * 0.15)


def test_market_kpis_空母體回傳零而非例外():
    empty = pd.DataFrame(columns=["id", "host_id", "neighbourhood_cleansed",
                                  "room_type", "price", "vac_pred",
                                  "prob", "tier"])
    k = pa.market_kpis(empty, commission=0.15)
    assert k["n_listings"] == 0
    assert k["n_hosts"] == 0
    assert k["avg_vacancy"] == 0.0
    assert k["red_ratio"] == 0.0
    assert k["total_revenue"] == 0.0


def test_district_health_欄位與筆數(sample_df):
    d = pa.district_health(sample_df, commission=0.15)
    assert list(d.columns) == ["行政區", "房源數", "平均空屋率", "高風險占比",
                               "預估平台收入", "空屋率vs全市"]
    assert len(d) == 2


def test_district_health_依高風險占比降冪(sample_df):
    d = pa.district_health(sample_df, commission=0.15)
    # 信義區 3 間有 2 紅(0.667) > 大安區 3 間有 1 紅(0.333)
    assert d.iloc[0]["行政區"] == "信義區"
    assert d.iloc[0]["高風險占比"] == pytest.approx(2 / 3)
    assert d.iloc[1]["高風險占比"] == pytest.approx(1 / 3)


def test_district_health_vs全市差異正負號(sample_df):
    d = pa.district_health(sample_df, commission=0.15).set_index("行政區")
    # 大安區均空屋率 (0+0.5+0.8)/3 = 0.4333;全市 0.55 → 差值為負(優於全市)
    assert d.loc["大安區", "空屋率vs全市"] < 0
    assert d.loc["信義區", "空屋率vs全市"] > 0


def test_host_risk_summary_聚合正確(sample_df):
    h = pa.host_risk_summary(sample_df, commission=0.15).set_index("host_id")
    assert len(h) == 3
    assert h.loc[30, "房源數"] == 2
    assert h.loc[30, "高風險間數"] == 2
    assert h.loc[30, "高風險占比"] == pytest.approx(1.0)
    assert h.loc[30, "平均風險分數"] == pytest.approx(0.85)
    assert h.loc[10, "高風險間數"] == 0


def test_host_risk_summary_排序把整批惡化房東排最前(sample_df):
    h = pa.host_risk_summary(sample_df, commission=0.15)
    assert int(h.iloc[0]["host_id"]) == 30
    assert int(h.iloc[-1]["host_id"]) == 10


def test_filter_scope_行政區與房型皆篩選(sample_df):
    out = pa.filter_scope(sample_df, ["大安區"], ["Entire home/apt"])
    assert len(out) == 2
    assert set(out["id"]) == {1, 2}


def test_filter_scope_None代表不篩選(sample_df):
    assert len(pa.filter_scope(sample_df, None, None)) == 6
    assert len(pa.filter_scope(sample_df, [], [])) == 6
    assert len(pa.filter_scope(sample_df, ["信義區"], None)) == 3


def test_supply_demand_matrix_門檻過濾(sample_df):
    # 每個 行政區x房型 組合最多 2 間,門檻 15 應全部濾掉
    out = pa.supply_demand_matrix(sample_df, min_listings=15)
    assert len(out) == 0
    assert list(out.columns) == ["行政區", "房型", "房源數", "平均空屋率",
                                 "中位價格", "機會標籤"]


def test_supply_demand_matrix_標籤分類():
    # 兩組合:A 空屋率低且房源少 → 招募缺口;B 空屋率高且房源多 → 供給飽和
    rows = []
    rows += [{"id": i, "host_id": 1, "neighbourhood_cleansed": "A區",
              "room_type": "Entire home/apt", "price": 1000.0,
              "vac_pred": 0.1, "prob": 0.1, "tier": "green"}
             for i in range(2)]
    rows += [{"id": 100 + i, "host_id": 2, "neighbourhood_cleansed": "B區",
              "room_type": "Private room", "price": 1000.0,
              "vac_pred": 0.9, "prob": 0.9, "tier": "red"}
             for i in range(8)]
    d = pd.DataFrame(rows)
    out = pa.supply_demand_matrix(d, min_listings=1).set_index("行政區")
    assert out.loc["A區", "機會標籤"] == "🟢 招募缺口"
    assert out.loc["B區", "機會標籤"] == "🔴 供給飽和"


# ════════════════════════════════════════════════════════════════
# 營收與成長:同儕落差診斷(2026-07-25)
# ════════════════════════════════════════════════════════════════

@pytest.fixture
def peer_df():
    """單一格(大安區×Entire home/apt)20 間,已訂率 0.05 遞增至 1.00。

    中位 = 第 10、11 名的平均 = (0.50+0.55)/2 = 0.525。
    """
    n = 20
    return pd.DataFrame({
        "id": range(n),
        "neighbourhood_cleansed": ["大安區"] * n,
        "room_type": ["Entire home/apt"] * n,
        "price": [1000.0] * n,
        "booked_rate": [round(0.05 * (i + 1), 2) for i in range(n)],
    })


def test_peer_gap_落差等於同儕中位減自身(peer_df):
    out = pa.peer_gap_table(peer_df, min_peers=15)
    assert len(out) == 20
    med = out["同儕中位已訂率"].iloc[0]
    assert med == pytest.approx(0.525)
    r = out.set_index("id")
    assert r.loc[0, "落差"] == pytest.approx(0.525 - 0.05)
    assert r.loc[19, "落差"] == pytest.approx(0.525 - 1.00)


def test_peer_gap_落後定義為落差大於門檻(peer_df):
    out = pa.peer_gap_table(peer_df, min_peers=15, gap_threshold=0.20)
    r = out.set_index("id")
    assert bool(r.loc[0, "is_laggard"]) is True        # 落差 0.475 > 0.20
    assert bool(r.loc[19, "is_laggard"]) is False      # 落差為負
    assert r.loc[0, "分組"] == "落後"
    assert r.loc[19, "分組"] == "達標"
    # 落差介於 0 與門檻之間 → 接近
    near = out[(out["落差"] > 0) & (out["落差"] <= 0.20)]
    assert len(near) > 0
    assert set(near["分組"]) == {"接近"}


def test_peer_gap_同格樣本不足整格剔除(peer_df):
    """同儕樣本 < min_peers 的格子不可比較,必須整格拿掉而非放行。"""
    out = pa.peer_gap_table(peer_df, min_peers=21)
    assert len(out) == 0


def test_peer_gap_不同格各自算各自的中位():
    """B 格全體已訂率都低,不該因為 A 格高就被判成落後。"""
    a = pd.DataFrame({
        "id": range(100, 115),
        "neighbourhood_cleansed": ["A區"] * 15,
        "room_type": ["Entire home/apt"] * 15,
        "price": [1000.0] * 15, "booked_rate": [0.90] * 15})
    b = pd.DataFrame({
        "id": range(200, 215),
        "neighbourhood_cleansed": ["B區"] * 15,
        "room_type": ["Entire home/apt"] * 15,
        "price": [1000.0] * 15, "booked_rate": [0.10] * 15})
    out = pa.peer_gap_table(pd.concat([a, b], ignore_index=True), min_peers=15)
    assert out["is_laggard"].sum() == 0
    assert set(out[out["neighbourhood_cleansed"] == "B區"]["分組"]) == {"達標"}


def test_peer_gap_空表與缺欄位不炸():
    assert len(pa.peer_gap_table(pd.DataFrame())) == 0
    lack = pd.DataFrame({"id": [1], "booked_rate": [0.5]})   # 缺行政區/房型
    out = pa.peer_gap_table(lack)
    assert "落差" in out.columns


def test_controllable_compare_相同品質時兩欄一致():
    """本頁主張的核心:落後組與達標組品質相同 → 相對差為 0。"""
    n = 30
    d = pd.DataFrame({
        "id": range(n),
        "neighbourhood_cleansed": ["大安區"] * n,
        "room_type": ["Entire home/apt"] * n,
        "price": [1000.0] * n,
        "booked_rate": [0.05] * 15 + [0.95] * 15,
        "review_scores_rating": [4.85] * n,
        "host_is_superhost": ["t"] * n,
        "minimum_nights": [3] * n,
    })
    g = pa.peer_gap_table(d, min_peers=15)
    out = pa.controllable_compare(g).set_index("項目")
    assert out.loc["整體評分", "落後組"] == pytest.approx(4.85)
    assert out.loc["整體評分", "達標組"] == pytest.approx(4.85)
    assert out.loc["整體評分", "相對差"] == pytest.approx(0.0)
    assert out.loc["超讚房東", "落後組"] == pytest.approx(1.0)   # flag 取比例


def test_controllable_compare_flag欄位取比例而非中位():
    n = 20
    d = pd.DataFrame({
        "id": range(n),
        "neighbourhood_cleansed": ["大安區"] * n,
        "room_type": ["Entire home/apt"] * n,
        "price": [1000.0] * n,
        "booked_rate": [0.05] * 10 + [0.95] * 10,
        # 落後組(前 10)一半是超讚房東,達標組全部不是
        "host_is_superhost": ["t"] * 5 + ["f"] * 5 + ["f"] * 10,
    })
    g = pa.peer_gap_table(d, min_peers=15)
    out = pa.controllable_compare(g).set_index("項目")
    assert out.loc["超讚房東", "落後組"] == pytest.approx(0.5)
    assert out.loc["超讚房東", "達標組"] == pytest.approx(0.0)
    assert out.loc["超讚房東", "相對差"] == pytest.approx(0.5)   # flag 用差值(pp)


def test_controllable_compare_空表不炸():
    assert len(pa.controllable_compare(pd.DataFrame())) == 0


def test_peer_gap_天數欄位供畫面使用不需換算(peer_df):
    """畫面一律講「一年有幾天有人住」,百分比只留在計算層。"""
    out = pa.peer_gap_table(peer_df, min_peers=15).set_index("id")
    # 房源 0 已訂率 0.05 → 一年 18 天;同儕中位 0.525 → 192 天
    assert out.loc[0, "自己有人住天數"] == pytest.approx(0.05 * 365)
    assert out.loc[0, "鄰居有人住天數"] == pytest.approx(0.525 * 365)
    assert out.loc[0, "少住天數"] == pytest.approx((0.525 - 0.05) * 365)
    # 門檻常數也要是天數,畫面才講得出「少 73 天以上」
    assert pa.LAGGARD_GAP_DAYS == round(pa.LAGGARD_GAP_DEFAULT * 365)


def test_uplift_一年少賺是價格乘少住天數乘抽成(peer_df):
    g = pa.peer_gap_table(peer_df, min_peers=15)
    out = pa.uplift_ranking(g, commission=0.15)
    top = out.iloc[0]
    # 最落後那間:落差 0.475 × 1000 元 × 365 天 × 15%
    assert top["一年少賺"] == pytest.approx(0.475 * 1000 * 365 * 0.15)
    # 抽成率為線性係數:加倍則金額加倍
    out2 = pa.uplift_ranking(g, commission=0.30)
    assert out2["一年少賺"].sum() == pytest.approx(out["一年少賺"].sum() * 2)


def test_uplift_不再有需要解釋的保守係數():
    """『保守可補回抽成』要先解釋 shrink 才看得懂,已從 API 移除。"""
    assert not hasattr(pa, "SHRINK_DEFAULT")
    import inspect
    assert "shrink" not in inspect.signature(pa.uplift_ranking).parameters


def test_uplift_只收落後組(peer_df):
    g = pa.peer_gap_table(peer_df, min_peers=15, gap_threshold=0.20)
    out = pa.uplift_ranking(g)
    assert len(out) == int(g["is_laggard"].sum())
    assert bool(out["is_laggard"].all())


def test_uplift_累積金額單調遞增且收斂於一(peer_df):
    g = pa.peer_gap_table(peer_df, min_peers=15)
    out = pa.uplift_ranking(g)
    assert out["一年少賺"].is_monotonic_decreasing        # 由大到小排序
    assert out["累積占比"].is_monotonic_increasing
    assert out["累積占比"].iloc[-1] == pytest.approx(1.0)
    assert out["累積金額"].iloc[-1] == pytest.approx(out["一年少賺"].sum())
    assert list(out["名次"]) == list(range(1, len(out) + 1))


def test_uplift_空表與無落後者不炸():
    assert len(pa.uplift_ranking(pd.DataFrame())) == 0
    n = 15
    d = pd.DataFrame({
        "id": range(n),
        "neighbourhood_cleansed": ["大安區"] * n,
        "room_type": ["Entire home/apt"] * n,
        "price": [1000.0] * n, "booked_rate": [0.5] * n})   # 全體相同→無落後
    out = pa.uplift_ranking(pa.peer_gap_table(d, min_peers=15))
    assert len(out) == 0


# ════════════════════════════════════════════════════════════════
# 風險模型盲區:「模型說安全、實際卻沒人住」的分流與建議(2026-07-25)
# ════════════════════════════════════════════════════════════════

@pytest.fixture
def lag_df():
    """4 間落後房源,用於 annotate_model_view / suggest_actions。"""
    return pd.DataFrame({
        "id": [1, 2, 3, 4],
        "listing_id": [1, 2, 3, 4],
        "neighbourhood_cleansed": ["大安區"] * 4,
        "room_type": ["Entire home/apt"] * 4,
        "price": [1000.0, 2000.0, 1000.0, 1000.0],
        "自己有人住天數": [5.0, 100.0, 100.0, 100.0],
        "minimum_nights": [2, 2, 30, 2],
        "一年少賺": [100.0, 200.0, 300.0, 400.0],
        "診斷分類": ["隱形危機"] * 4,
    })


def test_annotate_model_view_依tier分成三類():
    d = pd.DataFrame({"id": [1, 2, 3, 4], "一年少賺": [1.0] * 4})
    pred = pd.DataFrame({"id": [1, 2, 3],
                         "tier": ["green", "red", "yellow"],
                         "prob": [0.2, 0.8, 0.5]})
    out = pa.annotate_model_view(d, pred).set_index("id")
    # green = 模型說安全,但這份 df 本身就是「實際上滯銷」的名單 → 隱形危機
    assert out.loc[1, "診斷分類"] == "隱形危機"
    assert out.loc[2, "診斷分類"] == "模型有抓到"
    assert out.loc[3, "診斷分類"] == "模型有抓到"
    # 不在風險模型母體內(calendar/listings 有 31% 對不上)→ 未評估,不可當成安全
    assert out.loc[4, "診斷分類"] == "未評估"
    assert out.loc[1, "模型風險分數"] == pytest.approx(0.2)


def test_annotate_model_view_缺預測檔時全標未評估():
    """缺 _predictions.csv 不可讓整頁掛掉,也不可默默把房源當成安全。"""
    d = pd.DataFrame({"id": [1, 2], "一年少賺": [1.0, 2.0]})
    for pred in (None, pd.DataFrame()):
        out = pa.annotate_model_view(d, pred)
        assert set(out["診斷分類"]) == {"未評估"}
    assert len(pa.annotate_model_view(pd.DataFrame(), None)) == 0


def test_suggest_actions_幾乎沒開張者優先問意願(lag_df):
    """一年只住 5 天 → 先確認房東還想不想做,不要急著談降價或曝光。"""
    out = pa.suggest_actions(lag_df).set_index("id")
    assert "還想不想做" in out.loc[1, "建議作法"]


def test_suggest_actions_訂價偏高者建議調價(lag_df):
    peer = pd.DataFrame({"neighbourhood_cleansed": ["大安區"],
                         "room_type": ["Entire home/apt"],
                         "peer_price": [1000.0]})
    out = pa.suggest_actions(lag_df, peer).set_index("id")
    # id=2 價格 2000 / 同儕 1000 = 2.0 > 1.15,且有在營業(100 天)
    assert "調降價格" in out.loc[2, "建議作法"]
    # id=1 價格雖也偏高,但幾乎沒開張 → 先問意願的規則優先
    assert "還想不想做" in out.loc[1, "建議作法"]


def test_suggest_actions_最低入住天數過長者建議放寬(lag_df):
    peer = pd.DataFrame({"neighbourhood_cleansed": ["大安區"],
                         "room_type": ["Entire home/apt"],
                         "peer_price": [1000.0]})
    out = pa.suggest_actions(lag_df, peer).set_index("id")
    assert "放寬門檻" in out.loc[3, "建議作法"]      # minimum_nights=30


def test_suggest_actions_條件都正常者歸因曝光(lag_df):
    peer = pd.DataFrame({"neighbourhood_cleansed": ["大安區"],
                         "room_type": ["Entire home/apt"],
                         "peer_price": [1000.0]})
    out = pa.suggest_actions(lag_df, peer).set_index("id")
    assert "曝光" in out.loc[4, "建議作法"]


def test_suggest_actions_只對隱形危機給建議(lag_df):
    """模型有抓到的那批走既有 LIME 輔導信流程,不該在這裡另給一套建議。"""
    d = lag_df.copy()
    d["診斷分類"] = ["隱形危機", "模型有抓到", "未評估", "模型有抓到"]
    out = pa.suggest_actions(d).set_index("id")
    assert out.loc[1, "建議作法"] != ""
    assert out.loc[2, "建議作法"] == ""
    assert out.loc[3, "建議作法"] == ""
    assert out.loc[4, "建議作法"] == ""


def test_suggest_actions_空表不炸():
    out = pa.suggest_actions(pd.DataFrame())
    assert len(out) == 0
    assert "建議作法" in out.columns


# ── 「模型沒評估到」的原因(2026-07-25)────────────────────────────

def test_coverage_cutoff_取模型母體內最晚的房東加入日():
    """動態算切點而非寫死日期,模型重訓後會自動更新。"""
    d = pd.DataFrame({
        "id": [1, 2, 3],
        "host_since": ["2020-01-01", "2024-09-30", "2025-05-06"]})
    pred = pd.DataFrame({"id": [1, 2]})          # 3 不在模型母體內
    assert pa.model_coverage_cutoff(d, pred) == pd.Timestamp("2024-09-30")


def test_coverage_cutoff_缺資料時回None():
    """講不出原因時要能誠實回 None,不可硬掰一個日期。"""
    d = pd.DataFrame({"id": [1], "host_since": ["2020-01-01"]})
    assert pa.model_coverage_cutoff(d, None) is None
    assert pa.model_coverage_cutoff(d, pd.DataFrame()) is None
    assert pa.model_coverage_cutoff(pd.DataFrame(), pd.DataFrame({"id": [1]})) is None
    assert pa.model_coverage_cutoff(pd.DataFrame({"id": [1]}),
                                    pd.DataFrame({"id": [1]})) is None  # 缺 host_since


def test_explain_unevaluated_晚於切點者講出加入年月():
    d = pd.DataFrame({
        "id": [1, 2, 3],
        "診斷分類": ["未評估", "未評估", "隱形危機"],
        "host_since": ["2025-05-06", None, "2015-01-01"]})
    out = pa.explain_unevaluated(d, pd.Timestamp("2024-09-30")).set_index("id")
    assert "2025-05" in out.loc[1, "未評估原因"]
    assert "晚於模型訓練資料" in out.loc[1, "未評估原因"]
    # 沒有 host_since 就別硬掰時間差,退回中性說法
    assert out.loc[2, "未評估原因"] == "不在模型的訓練資料裡"
    # 已被模型評估的房源不需要解釋
    assert out.loc[3, "未評估原因"] == ""


def test_explain_unevaluated_無切點時退回中性說法():
    d = pd.DataFrame({"id": [1], "診斷分類": ["未評估"],
                      "host_since": ["2025-05-06"]})
    out = pa.explain_unevaluated(d, None)
    assert out.loc[0, "未評估原因"] == "不在模型的訓練資料裡"


def test_explain_unevaluated_空表不炸():
    out = pa.explain_unevaluated(pd.DataFrame())
    assert len(out) == 0
    assert "未評估原因" in out.columns
