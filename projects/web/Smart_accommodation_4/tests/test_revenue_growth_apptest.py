# -*- coding: utf-8 -*-
"""💰 營收與成長「白話版」AppTest 回歸。

2026-07-25 二版:頁面改成三個問句,一句話答案在前、圖只是佐證。
一版雖然分析正確,但用了「收入池 / 落後同儕 / 保守可補回抽成」等
需要解讀的詞,且百分比要換算,使用者反映看不懂,故重寫。

無頭載入後台分析頁,驗證:
  1. 三個問句標題與白話答案都在
  2. 一律用「天數」講入住,不用已訂率百分比
  3. 主張(不是比較差的房子)與其證據表同時出現
  4. 反迴歸:一版的行話、已移除的控制項與區塊都不得回來

需 data/_calendar_metrics.csv;缺檔時該頁只渲染 empty_state,對應測試 skip。
對應 docs/superpowers/plans/2026-07-25-營收與成長敘事重構.md。
"""
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from streamlit.testing.v1 import AppTest

APP = str(ROOT / "pages" / "3_📊_後台分析.py")
TAB = "💰 營收診斷與提升"

# 一版留下的行話,全部不得再出現在畫面上
JARGON = ["收入池", "落後同儕", "可補回抽成", "保守假設", "同儕落差診斷",
          "投報排序", "行銷投放優先名單", "母體"]


@pytest.fixture(scope="module")
def at():
    a = AppTest.from_file(APP, default_timeout=300)
    a.session_state["pf_active_tab"] = TAB
    a.run()
    return a


def _md(at) -> str:
    return "\n".join(str(m.value) for m in at.markdown)


def _body(at) -> str:
    """只取版面正文。

    頁面把全站 CSS 與側欄說明包在同一個 st.markdown 裡,那塊含有
    「已訂率 / 百分點」等字樣以及 `.stApp` 這種會誤中的 class 名,
    掃「不得出現的字」時必須排除,否則測到的不是本分頁的內容。
    """
    return "\n".join(str(m.value) for m in at.markdown
                     if "<style" not in str(m.value))


def _ready(at) -> bool:
    return "平台一年賺" in _md(at)


def test_頁面無例外(at):
    assert not at.exception, [str(e) for e in at.exception]


def test_三個問句就是三個段落標題(at):
    if not _ready(at):
        pytest.skip("缺 calendar 產物,頁面僅渲染 empty_state")
    md = _md(at)
    for q in ["📊 平台營收結構與主力熱點",
              "📉 表現落後房源與營收損失診斷",
              "🎯 優先搶救房源與投入效益"]:
        assert q in md, f"缺少問句標題:{q}"


def test_答案用白話大卡片先講(at):
    if not _ready(at):
        pytest.skip("缺 calendar 產物")
    md = _md(at)
    for label in ["平台一年賺", "最賺錢的房型", "有問題的房子",
                  "先處理最嚴重的"]:
        assert label in md, f"缺少白話答案卡:{label}"


def test_入住一律用天數不用百分比(at):
    """「2%」要換算才懂,「一年只有 7 天有人住」不用。"""
    if not _ready(at):
        pytest.skip("缺 calendar 產物")
    body = _body(at) + "\n" + "\n".join(b.label for b in at.button)
    assert "一年 365 天裡，有幾天有人住？" in body     # 主圖標題
    assert "一年有幾天有人住" in body                  # 名單表欄位
    assert "隔壁同型的房子" in body
    assert "已訂率" not in _body(at)                   # 百分比只留在計算層


def test_落後門檻要講成天數而不是百分點(at):
    """一版只寫「落差 20pp」,沒講基準是什麼,使用者反映看不懂。"""
    if not _ready(at):
        pytest.skip("缺 calendar 產物")
    assert "一年比鄰居少 73 天以上有人住" in _md(at)
    assert "百分點" not in _body(at)


def test_兩個門檻都是可填入的數字框不是寫死的(at):
    """落差分布平滑遞減(10/20/30/40pp → 37%/29%/19%/12%),沒有自然斷點,
    「幾天算有問題」與「一季能處理幾間」都是營運判斷而非資料事實,
    必須讓使用者精確指定(number_input 才填得準、記得成規則;滑桿拉不準)。
    """
    if not _ready(at):
        pytest.skip("缺 calendar 產物")
    ni = {n.key: n for n in at.number_input}
    assert "pf_gap_days" in ni, "找不到天數輸入框 pf_gap_days"
    assert "pf_topn" in ni, "找不到處理間數輸入框 pf_topn"
    assert ni["pf_gap_days"].value == 73          # 預設 = 20 個百分點
    assert ni["pf_topn"].value == 300
    # 側欄的抽成率(pf_commission)本來就是滑桿,那個不動;只確認這兩個不是。
    slider_keys = {s.key for s in at.slider}
    assert not ({"pf_gap_days", "pf_topn"} & slider_keys), \
        "這兩個數字不該用滑桿,要能精確填入"


def test_調整天數後整頁跟著重算():
    """②③ 的房子數、金額、名單都要跟著門檻走,不能只有文案變。"""
    a = AppTest.from_file(APP, default_timeout=300)
    a.session_state["pf_active_tab"] = TAB
    a.run()
    if "平台一年賺" not in _md(a):
        pytest.skip("缺 calendar 產物")
    assert "一年比鄰居少 73 天以上有人住" in _md(a)

    next(n for n in a.number_input if n.key == "pf_gap_days").set_value(150)
    a.run()

    md = _md(a)
    assert "一年比鄰居少 150 天以上有人住" in md
    assert "一年比鄰居少 73 天以上有人住" not in md
    assert not a.exception, [str(e) for e in a.exception]


def test_調整處理間數後金額與名單跟著重算():
    a = AppTest.from_file(APP, default_timeout=300)
    a.session_state["pf_active_tab"] = TAB
    a.run()
    if "平台一年賺" not in _md(a):
        pytest.skip("缺 calendar 產物")
    assert "先處理最嚴重的 300 間" in _md(a)

    next(n for n in a.number_input if n.key == "pf_topn").set_value(50)
    a.run()

    md = _md(a)
    assert "先處理最嚴重的 50 間" in md
    assert "先處理最嚴重的 300 間" not in md
    assert "300 間中的前 20 間" not in md
    assert not a.exception, [str(e) for e in a.exception]


def test_填的間數超過名單長度時夾住並說明():
    """②的門檻調嚴會讓名單變短。此時 pf_topn 不可因超出範圍而報錯,
    要夾到名單長度並告訴使用者怎麼辦。
    """
    a = AppTest.from_file(APP, default_timeout=300)
    a.session_state["pf_active_tab"] = TAB
    a.run()
    if "平台一年賺" not in _md(a):
        pytest.skip("缺 calendar 產物")

    next(n for n in a.number_input if n.key == "pf_topn").set_value(9999)
    a.run()

    assert not a.exception, [str(e) for e in a.exception]
    assert "比你填的 9,999 間少" in _md(a)





def test_不得再出現需要解讀的行話(at):
    body = _body(at)
    found = [w for w in JARGON if w in body]
    assert not found, f"這些一版的行話又回來了:{found}"


def test_已移除房東端平台端切換(at):
    """兩個口徑只差一個常數倍率、圖形等價,不得再加回來。"""
    assert not [r for r in at.radio if r.key == "rev_heat_scope"]


def test_已移除長短租一句話結論(at):
    assert "長短租策略一句話結論" not in _md(at)


def test_已移除成長機會供需矩陣(at):
    """它用模型預估空屋率 + 全體 listings,與本頁其他段落口徑不同,
    同頁並列必須另寫一大段口徑說明 —— 正是要消滅的「需要解讀的東西」。
    函式保留未刪,要放回來需連同口徑說明一起處理。
    """
    md = _md(at)
    assert "成長機會供需矩陣" not in md
    assert "本區塊口徑與上方不同" not in md


def test_第三段要標出風險模型有沒有抓到(at):
    """同樣是「訂不到」,模型抓得到的和抓不到的要做不同的事,不能混在一起。"""
    if not _ready(at):
        pytest.skip("缺 calendar 產物")
    md = _md(at)
    assert "這些房子，風險模型有沒有抓到？" in md
    for card in ["風險模型也覺得有問題", "模型說沒事、實際卻沒人住", "模型沒評估到"]:
        assert card in md, f"缺少分流卡:{card}"


def test_隱形危機那批不得走輔導通知流程(at):
    """風險模型對它們的歸因只會列出優點,寄輔導信方向是反的 —— 畫面要明講。"""
    if not _ready(at):
        pytest.skip("缺 calendar 產物")
    md = _md(at)
    if "隱形危機" not in md:
        pytest.skip("目前門檻下沒有隱形危機房源")
    assert "不能" in md and "輔導通知" in md
    assert "你這間很棒" in md          # 講清楚為什麼方向是反的


def test_隱形危機要給出可行動的建議且標明是規則不是模型(at):
    if not _ready(at):
        pytest.skip("缺 calendar 產物")
    md = _md(at)
    if "隱形危機" not in md:
        pytest.skip("目前門檻下沒有隱形危機房源")
    assert "建議作法" in md
    # 建議是規則判斷,不是模型預測 —— 不可讓觀眾誤以為是 AI 算出來的
    assert "規則判斷" in md and "不是模型預測" in md
    # 四條規則至少要出現一條
    assert any(k in md for k in ["還想不想做", "調降價格", "放寬門檻", "曝光"])


def test_未評估到的原因有註解(at):
    """使用者想知道「模型沒評估到」是為什麼,不能只丟一個數字。

    查證結果:已納入模型的房源 host_since 最晚 2024-09-30、未納入的最早
    2024-10-11,全站 392 間完全不重疊 —— 是訓練資料的時間切點,
    不是資料品質不足(第一版誤判為「評論太少」,已更正)。
    """
    if not _ready(at):
        pytest.skip("缺 calendar 產物")
    md = _md(at)
    if "模型沒評估到" not in md:
        pytest.skip("目前門檻下沒有『未評估』的房源")
    # st.caption 在 AppTest 歸在 at.caption,不在 at.markdown。
    cap = " ".join(str(c.value) for c in at.caption)
    assert "時間切點" in cap
    assert "重新訓練就會納入" in cap        # 給出「之後會解決」的預期
    assert "不是本頁計算錯誤" in cap


def test_未評估的房源每列都有滑鼠提示(at):
    """使用者要的是「圈起來那一列」滑鼠移過去就看得到原因,不是常駐文字、
    也不用捲回上面的彙總卡去猜是哪一間。改用純 CSS 的 hover 提示
    (.pf-tip-bubble),不是每列常駐的 st.caption —— 20 列常駐說明會把
    列表撐得很長,滑鼠提示才不占版面。
    """
    if not _ready(at):
        pytest.skip("缺 calendar 產物")
    md = _md(at)
    if "模型沒評估到" not in md:
        pytest.skip("目前門檻下沒有『未評估』的房源")
    if "⚪ 沒評估到" not in md:
        pytest.skip("前 20 名裡沒有未評估房源")
    assert "pf-tip-bubble" in md               # hover 提示的容器存在
    assert ("晚於模型訓練資料" in md
            or "不在模型的訓練資料裡" in md)   # 提示內容正確
    # 不該回退成每列常駐的 caption(那是使用者要我改掉的舊做法)
    cap = " ".join(str(c.value) for c in at.caption)
    assert "晚於模型訓練資料" not in cap


def test_名單每列都標出風險模型怎麼看(at):
    if not _ready(at):
        pytest.skip("缺 calendar 產物")
    md = _md(at)
    assert "風險模型怎麼看" in md        # 表頭
    assert any(k in md for k in ["說沒事卻沒人住", "模型也抓到", "沒評估到"])


# ── 2026-07-25:③名單「房源編號」跳轉到風險管理 ─────────────────
# 這兩個模組是不同母體(營收與成長用 calendar∩listings,風險管理用
# _predictions.csv 的風險模型母體,見計畫書已知的 31% 落差),所以名單裡
# 的房源不保證都在風險模型範圍內 —— 兩種結果(找到 / 找不到)都要驗證。

def _get(at, kind, key):
    return next((w for w in getattr(at, kind) if w.key == key), None)


def test_點房源編號會跳到風險管理並鎖定展開該房源():
    a = AppTest.from_file(APP, default_timeout=300)
    a.session_state["pf_active_tab"] = TAB
    a.run()
    if "平台一年賺" not in _md(a):
        pytest.skip("缺 calendar 產物")
    jump = next((b for b in a.button if str(b.key).startswith("pf_jump_")), None)
    if jump is None:
        pytest.skip("目前門檻下沒有落後同儕的房源可跳轉")
    lid = int(str(jump.key)[len("pf_jump_"):])

    jump.click().run()

    assert not a.exception, [str(e) for e in a.exception]
    assert a.session_state["pf_active_tab"] == "🚨 風險管理"
    assert a.session_state["rm_view"] == "listings"
    assert a.session_state["rm_focus_id"] == lid
    assert a.session_state["rm_expanded_id"] == lid
    assert a.session_state["rm_focus_from"] == "營收與成長"

    # 兩種合法結果之一:該房源在風險模型母體內(展開 LIME+派信鈕,st.info
    # 鎖定橫幅),或不在母體內(st.warning 說明,不報例外)。
    # st.info/st.warning 在 AppTest 歸在 at.info/at.warning,不在 at.markdown。
    send = _get(a, "button", f"rm_send1_{lid}")
    info_text = " ".join(str(i.value) for i in a.info)
    warn_text = " ".join(str(w.value) for w in a.warning)
    found_in_model = send is not None and f"已鎖定房源 #{lid}" in info_text
    missing_from_model = "不在風險模型評估範圍內" in warn_text
    assert found_in_model or missing_from_model, \
        "跳轉後畫面既沒有展開 LIME,也沒有『不在範圍內』的說明"


def test_清除鎖定按鈕會清空跳轉鎖定():
    a = AppTest.from_file(APP, default_timeout=300)
    a.session_state["pf_active_tab"] = TAB
    a.run()
    if "平台一年賺" not in _md(a):
        pytest.skip("缺 calendar 產物")
    jump = next((b for b in a.button if str(b.key).startswith("pf_jump_")), None)
    if jump is None:
        pytest.skip("目前門檻下沒有落後同儕的房源可跳轉")
    jump.click().run()

    clear = _get(a, "button", "rm_clear_focus")
    assert clear is not None, "跳轉後應該出現『清除鎖定』按鈕"
    clear.click().run()

    assert not a.exception, [str(e) for e in a.exception]
    assert a.session_state["rm_focus_id"] is None
    assert a.session_state["rm_expanded_id"] is None
