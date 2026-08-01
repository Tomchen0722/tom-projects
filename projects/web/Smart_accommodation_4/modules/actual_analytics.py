# -*- coding: utf-8 -*-
"""actual_analytics.py — 「預估 vs 實際」對照的純計算層。

刻意不 import streamlit:DataFrame in / DataFrame out,可離線用 pytest 驗證;
快取由呼叫端負責。實際值來自 scripts/build_actual_metrics.py 的離線產物。

口徑(2026-07-25 定案,見 docs/superpowers/plans/2026-07-25-預估vs實際對照.md)
-----------------------------------------------------------------------
實際入住天數 = Inside Airbnb 官方公式(評論數 × 2 × max(min_nights, 3),有上限),
窗口 2025-09-30 ~ 2026-06-30 共 273 天。

**同母體鐵律**:排除 is_dormant(前後兩期都零評論=無經營跡象)時,
預估欄必須跟著排除同一批,否則比較不公平。故本模組回傳的「預估」值
刻意不等於市場總覽卡片的全母體數字,呼叫端必須在介面上標明原因。

**本表不足以推論模型準確度**:落差同時混入(a)構念差異(模型 Y 是日曆開放率,
屬供給面;實際是估計入住,屬需求面)、(b)評論代理低估、(c)模型誤差三種來源,
三者無法乾淨拆開,(a)為主因。正式評估請見數據分析①②區塊。
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
ACTUAL_PATH = DATA_DIR / "_actual_metrics.csv"

WINDOW_DAYS = 273
WINDOW_LABEL = "2025-09-30 ~ 2026-06-30"
HIGH_RISK_TH = 0.60          # 與市場總覽同一門檻,雙邊一致才可比

# 介面文案的唯一來源(數據分析⑤與任何報表共用,避免各處各抄一份)
CAUSES = [
    ("構念不同（主因）",
     "模型的目標是「日曆上顯示可預訂的天數」，屬供給面（房東開放意願）；"
     "實際值是「估計真的有人住的天數」，屬需求面。實測同一批房源、同一時間窗口下，"
     "兩種定義本身就差 26.5 個百分點。"),
    ("評論代理低估",
     "實際值用評論數回推入住，官方公式已假設 50% 住客會留評論並乘以 2 校正，"
     "但真實留評率若低於 50%，實際入住會被低估、空屋率被高估。"),
    ("模型預測誤差",
     "模型本身的預測不準度。其影響被前兩項淹沒，無法從本表單獨分離出來。"),
]

# 注意:文案會被塞進 HTML div(note/_caveat),Streamlit 不處理 div 內的 markdown,
# 故強調一律用 <strong> 而非 **粗體**,否則畫面會出現字面星號。
CAVEAT = ("本表<strong>不足以</strong>推論模型準確度：上述三種成因無法乾淨拆開，"
          "其中構念差異為主因。模型的正式評估（GroupKFold OOF、前瞻驗證）"
          "請見本頁①②區塊。")


def available() -> bool:
    """離線產物是否已產出。"""
    return ACTUAL_PATH.exists()


def load_actual() -> pd.DataFrame:
    """讀取房源層級實際指標;缺檔回傳空表(呼叫端負責顯示提示)。"""
    if not available():
        return pd.DataFrame(columns=["id", "rev_window", "occ_days", "real_vac",
                                     "real_revenue_365", "is_dormant"])
    return pd.read_csv(ACTUAL_PATH, encoding="utf-8")


def join_actual(preds: pd.DataFrame, actual: pd.DataFrame) -> pd.DataFrame:
    """併入實際指標並排除無經營跡象房源(同母體鐵律的執行點)。"""
    if len(preds) == 0 or len(actual) == 0:
        return preds.merge(actual, on="id", how="inner")
    d = preds.merge(actual, on="id", how="inner")
    return d[d["is_dormant"] == 0].reset_index(drop=True)


def _num(s: pd.Series) -> pd.Series:
    return pd.to_numeric(s, errors="coerce").fillna(0.0)


def compare_kpis(preds: pd.DataFrame, actual: pd.DataFrame,
                 commission: float) -> pd.DataFrame:
    """五項 KPI 的預估 vs 實際對照。

    回傳欄位:指標 / 預估 / 實際 / 落差 / 格式(供呼叫端決定顯示方式)。
    空母體回傳全零而非例外。
    """
    d = join_actual(preds, actual)
    if len(d) == 0:
        return pd.DataFrame({
            "指標": ["活躍房東數", "平均空屋率", "高風險占比",
                     "年營收總額", "平台年收入"],
            "預估": [0, 0.0, 0.0, 0.0, 0.0],
            "實際": [0, 0.0, 0.0, 0.0, 0.0],
            "落差": [0, 0.0, 0.0, 0.0, 0.0],
            "格式": ["count", "pct", "pct", "money", "money"],
        })

    vac_pred = _num(d["vac_pred_365"])
    real_vac = _num(d["real_vac"])
    price = _num(d["price"])

    pred_rev = float((price * (1.0 - vac_pred).clip(0, 1) * 365).sum())
    real_rev = float(_num(d["real_revenue_365"]).sum())

    rows = [
        ("活躍房東數",
         int(d["host_id"].nunique()),
         int(d.loc[d["rev_window"] > 0, "host_id"].nunique()),
         "count"),
        ("平均空屋率", float(vac_pred.mean()), float(real_vac.mean()), "pct"),
        ("高風險占比",
         float((vac_pred >= HIGH_RISK_TH).mean()),
         float((real_vac >= HIGH_RISK_TH).mean()), "pct"),
        ("年營收總額", pred_rev, real_rev, "money"),
        ("平台年收入", pred_rev * float(commission),
         real_rev * float(commission), "money"),
    ]
    out = pd.DataFrame(rows, columns=["指標", "預估", "實際", "格式"])
    out["落差"] = out["實際"] - out["預估"]
    return out[["指標", "預估", "實際", "落差", "格式"]]


def population_note(preds: pd.DataFrame, actual: pd.DataFrame) -> dict:
    """母體說明:總數、排除數、納入數 —— 介面必須標示,否則使用者會以為數字打架。"""
    total = int(len(preds))
    if len(actual) == 0:
        return {"total": total, "dormant": 0, "kept": total}
    m = preds.merge(actual[["id", "is_dormant"]], on="id", how="inner")
    dormant = int((m["is_dormant"] == 1).sum())
    return {"total": total, "dormant": dormant, "kept": int(len(m)) - dormant}
