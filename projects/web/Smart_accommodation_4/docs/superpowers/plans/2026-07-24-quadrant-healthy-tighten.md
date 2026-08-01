# 四象限分類「健康」門檻收緊

日期：2026-07-24　依使用者定案規則實作。

## 背景（根因）

`modules/quadrant.classify_row` 中 `BOOKED_HIGH=0.50` 為死碼：`>=0.50` 與中間帶(20–50%)
兩分支回傳相同值，導致 green tier 只要訂房率 ≥ 20% 就歸「健康」，且分類完全未參考
donut 的 `vac_pred`（模型 A 預估空房率）。使用者要求收緊。

## 定案規則（體質佳 = green tier）

| 條件 | 歸類 |
|---|---|
| 無 `booked_rate_d90` | unknown（其他）|
| red/yellow + 訂房率 < 20% | alarm（真警報）|
| red/yellow + 訂房率 ≥ 20% | discount（預測風險不符）|
| green + `vac_pred` > 60% | alarm（真警報，升級）|
| green + 訂房率 ≥ 50% 且 `vac_pred` ≤ 35% | healthy（健康）|
| green + 其餘（訂房率<50% 或 35%<vac_pred≤60%）| hidden（隱形危機）|

門檻常數：`BOOKED_FULL=0.50`、`BOOKED_EMPTY=0.20`、`VAC_HEALTHY=0.35`、`VAC_ALARM=0.60`。
`vac_pred` 為 NaN 時：不升 alarm、不算 healthy（保守歸 hidden）。

## 階段與驗收（全部完成 2026-07-24）

- [x] **S1 測試先行**：新增 `tests/test_quadrant_classify.py`，涵蓋六條規則邊界值與 NaN。
  驗收：`python -m pytest tests/test_quadrant_classify.py -q` → 先紅（尚未改邏輯）。
- **S2 改 `classify_row` + `annotate`**：新增常數、`classify_row(tier, booked, vac_pred=nan)`，
  `annotate` 補傳 `vac_pred`（缺欄預設 NaN）。
  驗收：S1 測試全綠。
- **S3 修呼叫端**：`report_builder.py:65` 補傳 `d["vac_pred"]`；確認 `notify_center` 的 annotate 相容。
  驗收：`python -m pytest tests/ -q` 全綠（無回歸）。

## 未決／待回報（不在本次程式範圍）

- green 房源現在可因 `vac_pred>60%` 落入 alarm，`QUADRANTS["alarm"]["desc"]` 寫「房子本身條件不好」
  會與 green 體質矛盾。文案調整屬品味決策，實作後向使用者回報再定。
