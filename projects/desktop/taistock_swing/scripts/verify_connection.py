"""台股波段系統｜FinMind 連線驗證腳本。

用途：設好 FINMIND_TOKEN 後的第一個測試點。驗證三件事：
1. token 有效、可查額度用量。
2. P1 各資料集實際抓得到樣本。
3. 實際回傳欄位是否與 config.py 重建的 schema 一致（拆掉「已知限制 1」）。

執行方式（在專案根目錄）：
    python scripts/verify_connection.py

輸出會逐一標示每個資料集 ✔ 一致 或 ⚠ 需修正（並列出缺少/多出的欄位）。
若有 ⚠，把 config.py 中該資料集的 required_cols 改成實際欄位即可。
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

# 讓腳本能匯入 src 模組
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import config  # noqa: E402
from data_source import FinMindProvider  # noqa: E402

# 要驗證的資料集，以及各自的樣本查詢參數
# (資料集鍵, data_id, start_date, end_date)；start/end 留空字串代表不送日期
_SAMPLES: list[tuple[str, str | None, str, str]] = [
    ("stock_info", None, "", ""),                      # 不吃日期，留空
    ("price", "2330", "2024-01-01", "2024-01-31"),     # 免費：未還原日 K
    ("institutional", "2330", "2024-01-01", "2024-01-31"),
    ("margin", "2330", "2024-01-01", "2024-01-31"),    # 免費：融資融券
    ("trading_date", None, "2024-01-01", "2024-12-31"),
    ("price_adj", "2330", "2024-01-01", "2024-01-31"),      # 付費：還原股價（會標示跳過）
    ("holding_shares", "2330", "2024-01-01", "2024-03-31"),  # 付費：集保股權分散（會標示跳過）
]


def compare_columns(actual_cols: list[str], required_cols: tuple[str, ...]) -> dict[str, object]:
    """比對實際欄位與規格必要欄位。

    參數:
        actual_cols: API 實際回傳的欄位清單。
        required_cols: config 中登錄的必要欄位。

    回傳:
        dict，含 ok（是否全部必要欄位都在）、missing（缺少的）、
        extra（實際多出的，供參考）。

    例外:
        不主動拋出例外。
    """
    actual = set(actual_cols)
    required = set(required_cols)
    missing = sorted(required - actual)
    extra = sorted(actual - required)
    return {"ok": len(missing) == 0, "missing": missing, "extra": extra}


def check_quota(token: str) -> None:
    """查詢 FinMind API 額度用量並印出（不印 token 本身）。

    參數:
        token: FinMind 授權 token。

    回傳:
        無（結果直接列印）。

    例外:
        不主動拋出例外；查詢失敗時印出提示而非中斷。
    """
    import requests

    try:
        headers = {"Authorization": f"Bearer {token}"}
        resp = requests.get(config.FINMIND_USER_INFO_URL, headers=headers, timeout=15)
        data = resp.json()
        used = data.get("user_count", "未知")
        limit = data.get("api_request_limit", "未知")
        print(f"  額度用量：{used} / {limit}（每小時）")
    except Exception as exc:  # noqa: BLE001 — 查額度失敗不應中斷主流程
        print(f"  （額度查詢失敗，不影響後續測試）：{exc}")


def main() -> int:
    """執行完整連線驗證流程。

    回傳:
        0 表示全部資料集 schema 一致；1 表示有資料集需修正或抓取失敗。

    例外:
        不主動拋出例外；個別資料集失敗會記錄後續。
    """
    token = os.environ.get(config.TOKEN_ENV_VAR, "")
    print("=" * 56)
    print("FinMind 連線驗證")
    print("=" * 56)
    if not token:
        print(f"✘ 找不到環境變數 {config.TOKEN_ENV_VAR}。")
        print("  請先設定 token（見前一步說明），再重新執行本腳本。")
        return 1
    print(f"✔ 已讀到 {config.TOKEN_ENV_VAR}（長度 {len(token)}，內容不顯示）")
    check_quota(token)

    provider = FinMindProvider(token=token)
    all_ok = True
    print("\n逐一驗證資料集 schema：")
    print("-" * 56)
    for dataset_key, data_id, start, end in _SAMPLES:
        spec = config.DATASETS[dataset_key]
        target = f"{dataset_key}（{spec.finmind_name}）"

        # 付費資料集在免費帳號無法驗證，標示跳過（不算失敗）
        if spec.tier == "paid":
            print(f"⏭ {target}：付費層，免費帳號跳過（升級或改用免費替代來源）")
            continue

        try:
            raw = provider.fetch(spec, data_id, start, end)
        except Exception as exc:  # noqa: BLE001 — 逐一回報，不讓單一失敗中斷全部
            print(f"⚠ {target}：抓取失敗 → {exc}")
            all_ok = False
            continue

        if raw.empty:
            print(f"⚠ {target}：抓到 0 筆（換個日期區間或確認資料集名稱）")
            all_ok = False
            continue

        result = compare_columns(list(raw.columns), spec.required_cols)
        if result["ok"]:
            print(f"✔ {target}：{len(raw)} 筆，必要欄位齊全")
        else:
            all_ok = False
            print(f"⚠ {target}：{len(raw)} 筆，但缺少必要欄位 {result['missing']}")
            print(f"    實際欄位：{sorted(raw.columns)}")
            print(f"    → 請把 config.py 中 {dataset_key} 的 required_cols 改成實際欄位")

    print("=" * 56)
    if all_ok:
        print("✔ 全部通過：資料層 schema 與實際一致，可往上疊 P1 特徵層。")
    else:
        print("⚠ 有項目需修正：依上方提示改 config.py 後重跑，直到全綠。")
    print("=" * 56)
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
