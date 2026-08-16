# 自動排班系統

給中小型店家用的排班工具。老闆在網頁後台管人、管班別、按一下自動排班;
員工在 LINE 裡查自己的班表、請假、申請調班。

- 介面:暖色系日式簡約,手機也能用
- 後端:Flask + SQLite(單一檔案資料庫,不用另外裝資料庫)
- 自動排班:規則排班(快)+ OR-Tools 最佳化排班(強)

---

## 快速開始

```bash
cd C:\AI\shift-scheduler
pip install -r requirements.txt
python app.py
```

打開 <http://127.0.0.1:5000>

| 用途 | 網址 | 預設密碼 |
|---|---|---|
| 老闆後台 | <http://127.0.0.1:5000> | `admin1234` |
| 員工自助頁(demo) | <http://127.0.0.1:5000/liff?emp=1> | 不用登入 |

第一次啟動會自動建好資料庫,並灌入 7 位範例員工 + 3 個班別(早班 / 中班 / 大夜),
可以直接按「開始排班」看效果。要清空重來,把 `data/shift.db` 刪掉再啟動即可。

---

## 功能

### 新增 / 修改 / 刪除
五種資料都能完整增修刪,後台是一般網頁表單,同時也提供 JSON API:

| 資料 | 後台頁面 | API |
|---|---|---|
| 員工 | `/employees` | `/api/employees` |
| 班別 | `/shifts` | `/api/shifts` |
| 請假 | `/leaves` | `/api/leaves` |
| 排班 | `/schedule` | `/api/assignments` |
| 調班 | `/swaps` | `/api/swaps` |

刪除員工會連帶刪掉他的排班紀錄。想保留歷史就按「停用」而不是「刪除」。

### 自動排班

在「排班表」頁選好月份,按「開始排班」。兩種模式:

**規則排班** — 一天一天、一個班一個班往下填,每次挑「目前最該輪到」的人
(班數最少 → 這週班數最少 → 最久沒上班)。速度快,結果好跟員工解釋。

**最佳化排班** — 把所有限制寫成數學式,交給 OR-Tools 求解器一次算出整體最好的解。
人多、班別多、限制互相打架的時候差別很明顯。

兩種模式都遵守這些**硬性限制**:

- 每個班的需求人數
- 一人一天只排一個班
- 已核准的假不排
- 手動鎖定的班保持不動
- 班別的技能需求(例如「大夜」只有會咖啡的人能上)
- 兩班之間至少休息 11 小時(跨夜班會正確計算)
- 連續上班不超過 6 天
- 每個人的每週班數上限

最佳化排班還會額外**盡量**做到:缺人最少、每個人班數平均、補足每週最低班數、
同一個人不要早晚班一直跳。

排完會列出所有不合規的地方(缺人、超時、休息不足),排不出來也不會硬排。

> 連續兩個月排班時,系統會把前 28 天的班數算進公平度,避免同一個人月月被排最多。

### 手動調整

- 月曆下方的「手動加班次」可以直接指定某人某天上某班,會自動**鎖定**
- 「班次明細」表可以直接換人或刪除
- 鎖定的班(月曆上有 ◆)重新自動排班時不會被蓋掉
- 「清空未鎖定班次」只清自動排的,不動手動調過的

### 請假與調班

員工從 LINE 送出的申請會進到後台待審。核准請假後,下次自動排班就會避開那些日子;
核准調班後,系統直接改掉那筆班次並鎖定它。

---

## LINE 整合

**沒設定也能用。** 沒填 token 時系統跑 demo 模式,網頁功能完全正常,只是不會真的推播。

設定完成後員工可以:

| 在 LINE 輸入 | 作用 |
|---|---|
| `綁定 A001` | 第一次使用,把 LINE 帳號和員工資料綁在一起 |
| `班表` | 看未來 14 天自己的班 |
| `本月班表` | 看這個月自己的班 |
| `請假 2026-08-20 事假 家裡有事` | 送出請假申請 |
| `調班` | 開啟調班畫面(LIFF 網頁) |
| `功能` | 看所有指令 |

另外,店長按下「發布班表」時,每位已綁定的同仁會各自收到自己那份班表。

### 設定步驟

1. 到 [LINE Developers](https://developers.line.biz/console/) 建立 Provider
2. 建 **Messaging API channel** → 取得 `Channel secret`、`Channel access token`
3. 建 **LINE Login channel** → 新增 **LIFF** app
   - Endpoint URL:`https://你的網址/liff`
   - Size:`Full`,Scope 勾 `profile` + `openid`
   - 取得 `LIFF ID` 和這個 Login channel 的 `Channel ID`
4. 複製 `.env.example` 成 `.env`,把四個值填進去
5. Messaging API channel 的 Webhook URL 填 `https://你的網址/line/webhook`,
   打開 Use webhook、關掉自動回覆訊息
6. 重開服務

本機測試時 LINE 連不到 `127.0.0.1`,要用 ngrok 之類的工具開一個對外 https 網址。

**身分驗證怎麼運作**(給非工程背景的說明):
LIFF 頁在 LINE 裡打開時,LINE 會發一張「數位身分證」(ID Token)給網頁。
網頁把它送到後端,後端拿去問 LINE 官方「這張是真的嗎、是誰」,
確認後才知道現在操作的是哪位員工。員工不需要另外註冊帳號密碼。

---

## 專案結構

```
shift-scheduler/
├─ app.py                    Flask 進入點
├─ config.py                 全站設定(讀 .env)
├─ requirements.txt
├─ .env.example              設定範本
├─ data/shift.db             SQLite 資料庫(自動產生,已 gitignore)
├─ scheduler/
│  ├─ db.py                  資料表結構與連線
│  ├─ repo.py                CRUD(路由層只呼叫這裡,不寫 SQL)
│  ├─ engine.py              排班共用資料結構、時間計算、結果檢查
│  ├─ rules.py               規則排班(貪婪演算法)
│  ├─ solver.py              最佳化排班(OR-Tools CP-SAT)
│  ├─ scheduling.py          排班統一入口(選引擎、寫回資料庫)
│  ├─ line_api.py            LINE Messaging API 封裝
│  ├─ notify.py              推播:班表發布、審核結果
│  ├─ seed.py                範例資料
│  └─ routes/
│     ├─ web.py              後台網頁
│     ├─ api.py              JSON API
│     └─ line_bp.py          LINE webhook + 員工自助頁
├─ templates/                Jinja2 樣板
└─ static/css, static/js
```

---

## 調整排班參數

改 `config.py`:

```python
MAX_CONSECUTIVE_DAYS = 6      # 最多連上幾天
MIN_REST_HOURS = 11           # 兩班之間最少間隔時數
```

改各員工的每週上下限,直接在「員工」頁改。
改各班別的需求人數與技能需求,直接在「班別」頁改。

最佳化排班的目標權重在 `scheduler/solver.py` 最上面:

```python
W_SHORTAGE  = 1000    # 缺人(最優先避免)
W_FAIRNESS  = 30      # 班數落差
W_MIN_SHIFT = 8       # 沒排到最低班數
W_ROTATION  = 1       # 班別跳來跳去
```

---

## 上線注意

- `.env` 的 `SECRET_KEY` 和 `ADMIN_PASSWORD` 一定要換掉
- `.env` 不要 commit 進 git(已在 `.gitignore`)
- 正式環境不要用 `python app.py`(那是開發用伺服器),改用 waitress / gunicorn
- `data/shift.db` 要定期備份,那是全部的資料
- 排班結果只是輔助,實際工時、加班、休息時間仍需符合勞基法規定,上線前請自行確認
