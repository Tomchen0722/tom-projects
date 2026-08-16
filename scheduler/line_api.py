"""LINE Messaging API 封裝。

沒填 token 時所有送出動作都會安靜地略過(demo 模式),不會讓網站掛掉。
"""

import base64
import hashlib
import hmac
import json
import logging
import urllib.error
import urllib.request

log = logging.getLogger(__name__)

REPLY_URL = "https://api.line.me/v2/bot/message/reply"
PUSH_URL = "https://api.line.me/v2/bot/message/push"
PROFILE_URL = "https://api.line.me/v2/bot/profile/{user_id}"


def verify_signature(channel_secret: str, body: bytes, signature: str) -> bool:
    """驗證 webhook 真的是 LINE 送來的。沒設 secret 時一律放行(本機測試用)。"""
    if not channel_secret:
        return True
    if not signature:
        return False
    digest = hmac.new(channel_secret.encode("utf-8"), body, hashlib.sha256).digest()
    expected = base64.b64encode(digest).decode("utf-8")
    return hmac.compare_digest(expected, signature)


def _post(url: str, token: str, payload: dict) -> bool:
    if not token:
        log.info("[LINE demo] 略過送出:%s", json.dumps(payload, ensure_ascii=False)[:300])
        return False
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return 200 <= resp.status < 300
    except urllib.error.HTTPError as exc:
        log.warning("LINE API 失敗 %s:%s", exc.code, exc.read()[:300])
    except Exception as exc:                     # noqa: BLE001
        log.warning("LINE API 連線失敗:%s", exc)
    return False


def reply_text(token: str, reply_token: str, text: str) -> bool:
    return _post(REPLY_URL, token, {
        "replyToken": reply_token,
        "messages": [{"type": "text", "text": text[:4900]}],
    })


def reply_messages(token: str, reply_token: str, messages: list) -> bool:
    return _post(REPLY_URL, token, {"replyToken": reply_token, "messages": messages[:5]})


def push_text(token: str, to: str, text: str) -> bool:
    if not to:
        return False
    return _post(PUSH_URL, token, {
        "to": to,
        "messages": [{"type": "text", "text": text[:4900]}],
    })


def liff_button(liff_id: str, label: str, path: str = ""):
    """產生一顆開啟 LIFF 頁面的按鈕訊息。"""
    url = f"https://liff.line.me/{liff_id}{path}" if liff_id else path
    return {
        "type": "template",
        "altText": label,
        "template": {
            "type": "buttons",
            "text": label,
            "actions": [{"type": "uri", "label": "開啟班表", "uri": url}],
        },
    }


def schedule_text(name: str, rows: list, title: str = "你的班表") -> str:
    """把排班資料排成 LINE 的純文字訊息。"""
    if not rows:
        return f"{name} {title}\n\n這段期間沒有排班。"
    weekday = "一二三四五六日"
    lines = [f"{name} {title}", ""]
    for r in rows:
        from datetime import date
        d = date.fromisoformat(r["work_date"])
        lines.append(
            f"{d.month:02d}/{d.day:02d}(週{weekday[d.weekday()]}) "
            f"{r['shift_name']} {r['start_time']}-{r['end_time']}"
        )
    lines.append("")
    lines.append(f"共 {len(rows)} 個班")
    return "\n".join(lines)
