# -*- coding: utf-8 -*-
"""LLM 介接層：Gemini / Claude / 模擬模式，含成本估算"""
import json, os, threading, time, urllib.error, urllib.request

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")

DEFAULT_CONFIG = {
    "GEMINI_API_KEY": "",
    "ANTHROPIC_API_KEY": "",
    "GEMINI_MODEL": "gemini-2.0-flash",
    "ANTHROPIC_MODEL": "claude-sonnet-4-5",
    "MONTHLY_BUDGET_USD": 90.0,
    "FX_USD_TWD": 33.0,
    "PORT": 5566,
    "GEMINI_MIN_INTERVAL_SEC": 7.0,  # 免費版約 10-15 RPM，7 秒一發最安全
}

_gate_lock = threading.Lock()
_last_call = {"gemini": 0.0}


def _throttle(provider, interval):
    """全域節流：同一供應商的呼叫強制間隔，避免 429。"""
    while True:
        with _gate_lock:
            wait = _last_call.get(provider, 0) + interval - time.time()
            if wait <= 0:
                _last_call[provider] = time.time()
                return
        time.sleep(min(wait, 1.0))

# 估算單價 (USD / 1M tokens): (input, output)
PRICING = {
    "gemini": (0.10, 0.40),
    "claude": (3.00, 15.00),
    "mock": (0.0, 0.0),
}


def load_config():
    cfg = dict(DEFAULT_CONFIG)
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                cfg.update(json.load(f))
        except Exception:
            pass
    return cfg


def save_config(cfg):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)


def _post_json(url, payload, headers, timeout=90):
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", **headers}, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def _est_tokens(text):
    return max(1, len(text) // 3)


def call_llm(provider, system, prompt):
    """回傳 (text, cost_usd, provider_used)。無 key 時走模擬模式。"""
    cfg = load_config()
    if provider == "gemini" and cfg.get("GEMINI_API_KEY"):
        interval = float(cfg.get("GEMINI_MIN_INTERVAL_SEC", 7.0))
        last_err = None
        for attempt in range(4):
            _throttle("gemini", interval)
            try:
                data = _post_json(
                    "https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent?key=%s"
                    % (cfg["GEMINI_MODEL"], cfg["GEMINI_API_KEY"]),
                    {"system_instruction": {"parts": [{"text": system}]},
                     "contents": [{"role": "user", "parts": [{"text": prompt}]}]},
                    {})
                text = data["candidates"][0]["content"]["parts"][0]["text"]
                usage = data.get("usageMetadata", {})
                ti = usage.get("promptTokenCount", _est_tokens(system + prompt))
                to = usage.get("candidatesTokenCount", _est_tokens(text))
                p = PRICING["gemini"]
                return text, (ti * p[0] + to * p[1]) / 1e6, "gemini"
            except urllib.error.HTTPError as e:
                last_err = e
                if e.code == 429:  # 撞到速率限制：等更久再重試
                    time.sleep(interval * (attempt + 2))
                    continue
                break
            except Exception as e:
                last_err = e
                break
        note = ("gemini 免費版速率限制(429)，重試 4 次仍失敗——請稍等一分鐘再跑，"
                "或到 Google AI Studio 開啟計費提高額度"
                if getattr(last_err, "code", None) == 429
                else "gemini 呼叫失敗(%s)，改用模擬" % last_err)
        return _mock(system, prompt, note)
    if provider == "claude" and cfg.get("ANTHROPIC_API_KEY"):
        try:
            data = _post_json(
                "https://api.anthropic.com/v1/messages",
                {"model": cfg["ANTHROPIC_MODEL"], "max_tokens": 2048,
                 "system": system,
                 "messages": [{"role": "user", "content": prompt}]},
                {"x-api-key": cfg["ANTHROPIC_API_KEY"],
                 "anthropic-version": "2023-06-01"})
            text = "".join(b.get("text", "") for b in data.get("content", []))
            u = data.get("usage", {})
            p = PRICING["claude"]
            return text, (u.get("input_tokens", 0) * p[0] +
                          u.get("output_tokens", 0) * p[1]) / 1e6, "claude"
        except Exception as e:
            return _mock(system, prompt, "claude 呼叫失敗(%s)，改用模擬" % e)
    return _mock(system, prompt, None)


def _mock(system, prompt, note):
    head = "【模擬模式輸出】尚未設定 API Key，此為確定性示意內容。\n"
    if note:
        head = "【%s】\n" % note
    body = ("依據職責「%s...」，針對輸入「%s...」產出：\n"
            "1. 重點分析：已依角色職責完成初步整理。\n"
            "2. 建議行動：待接上真實模型後可得完整內容。\n"
            "3. 風險提醒：模擬內容僅供流程驗證，勿作為實際決策依據。"
            % (system[:40].replace("\n", " "), str(prompt)[:60].replace("\n", " ")))
    return head + body, 0.0, "mock"
