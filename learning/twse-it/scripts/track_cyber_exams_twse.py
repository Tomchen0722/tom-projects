# -*- coding: utf-8 -*-
"""
臺灣證券交易所 (TWSE) 資訊人員甄試 · 最新考情、證照與資安指引自動追蹤監控器
追蹤目標：
1. 臺灣證券交易所 (TWSE) 官方網站與招募公告
2. 金融監督管理委員會 (金管會) 金融資安行動方案與指引修訂
3. 經濟部 iPAS 資訊安全工程師 (中級) 能力鑑定時程
4. 考選部高普考 / 地方特考「資通安全」考期與試題公布
"""
import sys
import json
import urllib.request
import urllib.error
from datetime import datetime

# Windows 控制台 UTF-8 相容保護
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

TARGETS = [
    {
        "name": "臺灣證券交易所 (TWSE) 官方新聞與公告",
        "category": "證交所招募",
        "url": "https://www.twse.com.tw/zh/about/news/news/",
        "description": "追蹤證交所新進人員甄試簡章、資安人員招考名額與時程"
    },
    {
        "name": "證券暨期貨市場發展基金會 (SFI) 招募專區",
        "category": "主辦試務機構",
        "url": "https://www.sfi.org.tw/",
        "description": "證交所委託辦理筆試與口試之官方報名與簡章公告網站"
    },
    {
        "name": "金融監督管理委員會 (金管會) 資安法規指引",
        "category": "主管機關規範",
        "url": "https://www.fsc.gov.tw/",
        "description": "追蹤金融資安行動方案 2.0 最新修正、F-ISAC 聯防作業程序與資安通報要點"
    },
    {
        "name": "經濟部 iPAS 資訊安全工程師能力鑑定",
        "category": "官方推薦替代題庫",
        "url": "https://www.ipas.org.tw/",
        "description": "中級「資訊安全規劃與管理」、「資訊安全防護技術」各梯次報名與公告"
    },
    {
        "name": "考選部國家考試公告 (資通安全類科)",
        "category": "官方推薦替代題庫",
        "url": "https://wwwc.moex.gov.tw/",
        "description": "高普考、地方特考「資通安全」近 3 年最新申論試題與評分標準"
    }
]

def check_targets():
    print("=" * 70)
    print(" [TWSE IT Cyber Security Tracker] 臺灣證券交易所考情與指引巡檢")
    print(f" 檢測時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    results = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    for item in TARGETS:
        status_msg = "已配置監控 (待連線測試)"
        try:
            req = urllib.request.Request(item["url"], headers=headers)
            with urllib.request.urlopen(req, timeout=5) as resp:
                code = resp.getcode()
                status_msg = f"連線正常 (HTTP {code})"
        except Exception as e:
            status_msg = f"端點可用性檢查: {type(e).__name__}"

        print(f"\n* [{item['category']}] {item['name']}")
        print(f"  URL : {item['url']}")
        print(f"  目標: {item['description']}")
        print(f"  狀態: {status_msg}")

        results.append({
            "name": item["name"],
            "url": item["url"],
            "status": status_msg
        })

    print("\n" + "=" * 70)
    print("備考策略與行動清單：")
    print("1. 每日固定檢查證券期貨發展基金會 (SFI) 與證交所首頁簡章。")
    print("2. 研習本專案 135 題全真標竿申論與 24 章核心速記講義。")
    print("3. 實作 iPAS 中級問答題與高普考資通安全申論題，強化五段式作答速度。")
    print("=" * 70)
    return results

if __name__ == "__main__":
    check_targets()
