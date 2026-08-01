# -*- coding: utf-8 -*-
"""risk_cockpit_sections 純邏輯(不依賴 Streamlit runtime)。"""
import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from modules import risk_cockpit_sections as rc


def _hosts():
    return pd.DataFrame({
        "host_id": [12345, 12399, 88, 700123],
        "房源數": [8, 3, 1, 5],
        "高風險間數": [6, 2, 1, 1],
        "高風險占比": [0.75, 0.66, 1.0, 0.2],
        "平均風險分數": [0.71, 0.60, 0.9, 0.3],
        "預估年營收": [1.24e7, 3.1e6, 8e5, 6e6],
    })


def _listings():
    return pd.DataFrame({
        "id": [1, 2, 3, 4],
        "host_id": [12345, 12345, 99, 99],
        "tier": ["red", "yellow", "red", "green"],
        "prob": [0.82, 0.40, 0.91, 0.10],
    })


def test_resolve_哨兵與非法回傳None():
    ids = [12345, 99]
    assert rc.resolve_host_filter(rc.HOST_ALL, ids) is None
    assert rc.resolve_host_filter(None, ids) is None
    assert rc.resolve_host_filter("abc", ids) is None
    assert rc.resolve_host_filter(777, ids) is None       # 不在母體
    assert rc.resolve_host_filter(12345, ids) == 12345
    assert rc.resolve_host_filter("99", ids) == 99         # 字串數字可轉


def _quad_listings():
    """4 位房東的房源分佈:12345 有 2 間 alarm、12399 有 1 間 alarm+1 間 hidden。"""
    return pd.DataFrame({
        "id": range(1, 8),
        "host_id": [12345, 12345, 12345, 12399, 12399, 88, 700123],
        "quadrant": ["alarm", "alarm", "healthy", "alarm", "hidden",
                     "hidden", "dormant"],
    })


def test_filter_hosts_by_quadrant_名下至少一間即列出():
    res = rc.filter_hosts_by_quadrant(_hosts(), _quad_listings(), "alarm")
    # 12345(2間) 與 12399(1間) 都有 alarm → 都要列出;88/700123 沒有 → 排除
    assert res["host_id"].tolist() == [12345, 12399]


def test_filter_hosts_by_quadrant_附加該象限間數並據以排序():
    res = rc.filter_hosts_by_quadrant(_hosts(), _quad_listings(), "alarm")
    assert res.iloc[0]["該象限間數"] == 2       # 12345 有 2 間,排最前
    assert res.iloc[1]["該象限間數"] == 1


def test_filter_hosts_by_quadrant_房東可同時出現在多個象限():
    """定案採「至少 1 間」,12399 同時有 alarm 與 hidden,兩個篩選都要看得到。"""
    a = rc.filter_hosts_by_quadrant(_hosts(), _quad_listings(), "alarm")
    h = rc.filter_hosts_by_quadrant(_hosts(), _quad_listings(), "hidden")
    assert 12399 in a["host_id"].tolist()
    assert 12399 in h["host_id"].tolist()


def test_filter_hosts_by_quadrant_全部或缺資料時不篩選():
    hosts = _hosts()
    assert len(rc.filter_hosts_by_quadrant(hosts, _quad_listings(), None)) == 4
    assert len(rc.filter_hosts_by_quadrant(hosts, None, "alarm")) == 4
    # 不篩選時不應多出象限欄
    assert "該象限間數" not in rc.filter_hosts_by_quadrant(
        hosts, _quad_listings(), None).columns


def test_filter_hosts_by_quadrant_無符合房東回空表():
    res = rc.filter_hosts_by_quadrant(_hosts(), _quad_listings(), "discount")
    assert len(res) == 0


def test_filter_hosts_by_quadrant_套用顯示上限():
    res = rc.filter_hosts_by_quadrant(_hosts(), _quad_listings(), "alarm",
                                      limit=1)
    assert len(res) == 1


def test_quadrant_host_counts_依象限去重計數():
    c = rc.quadrant_host_counts(_quad_listings())
    assert c["alarm"] == 2        # 12345、12399
    assert c["hidden"] == 2       # 12399、88
    assert c["dormant"] == 1
    assert rc.quadrant_host_counts(None) == {}


def test_quadrant_listing_counts_計數總筆數():
    c = rc.quadrant_listing_counts(_quad_listings())
    assert c["alarm"] == 3        # id 1, 2, 4
    assert c["hidden"] == 2       # id 5, 6
    assert c["dormant"] == 1      # id 7
    assert rc.quadrant_listing_counts(None) == {}


def test_filter_listings_房東鎖定與層級與區間():
    d = _listings()
    # 不鎖房東、只要 red、全區間 → id 1,3(prob 降序)
    r = rc.filter_listings(d, ["red"], 0.0, 1.0, None)
    assert r["id"].tolist() == [3, 1]
    # 鎖房東 12345、red+yellow → id 1,2
    r2 = rc.filter_listings(d, ["red", "yellow"], 0.0, 1.0, 12345)
    assert set(r2["id"]) == {1, 2}
    # 風險區間收斂
    r3 = rc.filter_listings(d, ["red", "yellow", "green"], 0.0, 0.5, None)
    assert set(r3["id"]) == {2, 4}
    # 空 tiers 視同全部
    assert len(rc.filter_listings(d, [], 0.0, 1.0, None)) == 4


def test_filter_listings_象限篩選():
    d = _listings()
    qdf = pd.DataFrame({
        "id": [1, 2, 3, 4],
        "quadrant": ["alarm", "alarm", "hidden", "healthy"],
    })
    r = rc.filter_listings(d, None, 0.0, 1.0, None, quadrant_key="alarm", quad_df=qdf)
    assert set(r["id"]) == {1, 2}

    r_hidden = rc.filter_listings(d, None, 0.0, 1.0, None, quadrant_key="hidden", quad_df=qdf)
    assert set(r_hidden["id"]) == {3}


def _quad_df():
    """8 間房源,涵蓋五個象限,host_id 有重複以測涉及房東去重。"""
    return pd.DataFrame({
        "id": range(1, 9),
        "host_id": [1, 1, 2, 3, 4, 5, 6, 7],
        "quadrant": ["alarm", "alarm", "hidden", "hidden", "hidden",
                    "discount", "healthy", "dormant"],
    })


def test_kpi_counts_from_quadrant_數字與四象限彙總一致():
    k = rc.kpi_counts_from_quadrant(_quad_df())
    assert k["n_total"] == 8
    assert k["n_alarm"] == 2          # alarm 兩間
    assert k["n_hidden"] == 3         # hidden 三間
    assert k["n_dormant"] == 1        # dormant 一間
    assert k["alarm_ratio"] == pytest.approx(2 / 8)


def test_kpi_counts_from_quadrant_涉及房東去重():
    k = rc.kpi_counts_from_quadrant(_quad_df())
    # id 1,2 都是 alarm 但同一位房東(host_id=1) → 只算 1 位
    assert k["alarm_hosts"] == 1


def test_kpi_counts_from_quadrant_無alarm時房東數為零():
    d = _quad_df()
    d["quadrant"] = "healthy"
    k = rc.kpi_counts_from_quadrant(d)
    assert k["n_alarm"] == 0
    assert k["alarm_hosts"] == 0
    assert k["alarm_ratio"] == 0.0


def test_kpi_counts_from_quadrant_空表不丟例外():
    empty = pd.DataFrame(columns=["id", "host_id", "quadrant"])
    k = rc.kpi_counts_from_quadrant(empty)
    assert k["n_total"] == 0
    assert k["alarm_ratio"] == 0.0
