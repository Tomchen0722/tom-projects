# 自動排班系統

給中小型店家用的排班工具。老闆在網頁後台管人、管班別、按一下自動排班;
員工在 LINE 裡查自己的班表、請假、申請調班。

- 介面:暖色系日式簡約,手機也能用
- 後端:Flask
- 資料庫:Supabase(PostgreSQL)為主,本機 SQLite 為輔,填不填 `.env` 決定用哪個
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

第一次啟動會自動建好資料表,並灌入 9 位範例員工 + 3 個班別(早班 / 中班 / 大夜),
可以直接按「開始排班」看效果。

**沒設定 Supabase 時資料存在本機的 `data/shift.db`**,要清空重來把這個檔案刪掉再啟動即可。
接上 Supabase 的方法看下面「資料庫」一節。

---

## 資料庫

系統可以接兩種資料庫,靠 `.env` 有沒有填 `SUPABASE_DB_URL` 自動判斷:

| 情況 | 用哪個 | 適合 |
|---|---|---|
| `.env` 沒填 | 本機 `data/shift.db`(SQLite) | 一台電腦自己用、開發測試 |
| `.env` 有填 | Supabase(PostgreSQL) | 正式營運、多台裝置共用、要從外面連 |

程式碼只寫一套 SQL,由 `scheduler/db.py` 負責翻譯成兩種資料庫各自的語法,
所以換資料庫不用改任何業務邏輯。

### 接上 Supabase

1. 到 [supabase.com](https://supabase.com) 註冊,建立 Project(免費方案就夠),
   **記下你設定的資料庫密碼**,那個密碼之後看不到第二次。

2. 進 **Project Settings > Database > Connection string**,
   切到 **Connection pooling** 那一段複製連線字串。

   > ⚠️ **一定要用 Connection pooling 的位址**(主機名含 `pooler.supabase.com`)。
   > 上面那個 Direct connection 的 `db.xxxxx.supabase.co` **只有 IPv6 位址**,
   > 一般家用 / 辦公室網路沒有對外 IPv6,填了會連不上。

3. 複製 `.env.example` 成 `.env`,填進去:

   ```
   SUPABASE_DB_URL=postgresql://postgres.專案代號:你的密碼@aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres
   ```

   從後台複製常會連 `[YOUR-PASSWORD]` 佔位符一起帶上,記得換成真的密碼。
   密碼含 `/ @ # ? &` 這些符號不用自己處理,程式會自動編碼。

4. 確認連得上:

   ```bash
   python scripts/db_check.py
   ```

   連不上時它會直接告訴你是密碼錯、位址錯、還是 IPv6 的問題,不用自己看英文錯誤。

5. 啟動 `python app.py`,資料表會自動建好。
   想自己在後台建也可以,把 `supabase_schema.sql` 貼到 Supabase 的 SQL Editor 執行。

6. 後台「設定與 LINE」頁最上面會顯示現在接的是哪一個資料庫。

### 把現有資料搬上雲端

本機已經排了一堆班,想直接帶上去:

```bash
python scripts/migrate_to_supabase.py
```

先試跑,只列出會搬什麼、不寫入。確認數字沒問題再加 `--run`:

```bash
python scripts/migrate_to_supabase.py --run --wipe
```

`--wipe` 是先清空 Supabase 現有資料再搬。搬完會自動重設流水號並逐表比對筆數,
對不上就整批復原,不會搬一半。本機的 SQLite 檔案不會被刪掉。

### 資料安全

建表時會對所有表打開 **Row Level Security 但不建任何 policy**。
意思是:Supabase 對外的 anon / service 前端金鑰完全讀不到這些表,
只有我們用資料庫帳號直連才存取得到。員工姓名電話是個資,不應該讓拿到前端金鑰的人直接撈走。

### 已知限制

- Supabase 免費方案的專案**閒置一段時間會被自動暫停**,暫停期間系統會連不上,
  要到後台按一下恢復。正式營運建議升級付費方案。
- 資料在雲端不等於有備份。Supabase 免費方案沒有自動備份,
  重要資料請自己定期匯出,或升級到有 Point-in-Time Recovery 的方案。

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
├─ supabase_schema.sql       Supabase 建表語法(可貼進 SQL Editor)
├─ data/shift.db             本機 SQLite(沒接 Supabase 時才用,已 gitignore)
├─ scripts/
│  ├─ db_check.py            檢查資料庫連線,連不上會說明原因
│  └─ migrate_to_supabase.py 把本機資料搬上 Supabase
├─ tests/
│  └─ test_db_dialect.py     SQL 方言翻譯與兩種資料庫的端對端測試
├─ scheduler/
│  ├─ db.py                  連線層:SQLite / PostgreSQL 雙支援與方言翻譯
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
- `.env` 裡有資料庫密碼,**絕對不要 commit 進 git**(已在 `.gitignore`)
- 正式環境不要用 `python app.py`(那是開發用伺服器),改用 waitress / gunicorn
- 資料備份:用 Supabase 就靠它的備份機制(免費方案沒有,要自己匯出);
  用 SQLite 就定期複製 `data/shift.db`
- 排班結果只是輔助,實際工時、加班、休息時間仍需符合勞基法規定,上線前請自行確認

---

## 測試

```bash
python tests/test_db_dialect.py
```

驗證 SQL 方言翻譯、連線字串處理,以及在 SQLite 上跑完整套 CRUD 加排班。

想連真的 PostgreSQL 一起測(Supabase 就是 PostgreSQL,本機測得過就會過):

```bash
python tests/test_db_dialect.py --pg "postgresql://postgres:密碼@127.0.0.1:5432/postgres?sslmode=disable"
```

它會開一個獨立的 schema 跑測試,跑完刪掉,不會動到你的正式資料。
