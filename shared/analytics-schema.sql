-- ═══════════════════════════════════════════════════════════
--  作品集瀏覽計數 — Supabase 建表 SQL
--  用法：Supabase 後台 → SQL Editor → New query → 貼上全部 → Run
-- ═══════════════════════════════════════════════════════════

-- ── 1. 原始瀏覽紀錄表 ──────────────────────────────────────
create table if not exists public.page_views (
  id          bigserial primary key,
  project_id  text        not null,          -- 對應 projects.json 的 id，首頁用 'hub'
  page_path   text,                          -- 該專案內的頁面路徑，例如 '02-ip-subnetting.html'
  visitor_id  text,                          -- 匿名訪客識別碼（瀏覽器隨機產生，不含個資）
  referrer    text,                           -- 來源網址
  viewed_at   timestamptz not null default now()
);

create index if not exists idx_pv_project on public.page_views (project_id);
create index if not exists idx_pv_time    on public.page_views (viewed_at desc);
create index if not exists idx_pv_daily   on public.page_views (project_id, (viewed_at::date));

-- ── 2. RLS：只允許「寫入」與「透過彙總 View 讀取」──────────
-- anon key 是設計上公開的，靠 RLS 政策限制它能做什麼。
alter table public.page_views enable row level security;

-- 任何人都可以新增一筆瀏覽紀錄（這是計數器的本質）
drop policy if exists "anyone can insert view" on public.page_views;
create policy "anyone can insert view"
  on public.page_views for insert
  to anon, authenticated
  with check (true);

-- 刻意「不」開放 select / update / delete 給 anon。
-- 訪客只能寫，不能讀原始紀錄，也不能竄改或刪除。
-- 統計數字一律透過下面的彙總 View 取得。

-- ── 3. 彙總 View（供前端讀取，不暴露原始資料）───────────────

-- 3-1 每個專案的每日瀏覽數
create or replace view public.v_views_daily
with (security_invoker = off) as
select
  project_id,
  (viewed_at at time zone 'Asia/Taipei')::date as day,
  count(*)                       as views,
  count(distinct visitor_id)     as visitors
from public.page_views
group by project_id, day;

-- 3-2 每個專案的每月瀏覽數
create or replace view public.v_views_monthly
with (security_invoker = off) as
select
  project_id,
  to_char(viewed_at at time zone 'Asia/Taipei', 'YYYY-MM') as month,
  count(*)                       as views,
  count(distinct visitor_id)     as visitors
from public.page_views
group by project_id, month;

-- 3-3 每個專案的總計 + 今日 + 本月（前端主要讀這張）
create or replace view public.v_views_summary
with (security_invoker = off) as
select
  project_id,
  count(*)                                                        as total_views,
  count(distinct visitor_id)                                      as total_visitors,
  count(*) filter (
    where (viewed_at at time zone 'Asia/Taipei')::date
        = (now() at time zone 'Asia/Taipei')::date
  )                                                               as today_views,
  count(*) filter (
    where to_char(viewed_at at time zone 'Asia/Taipei', 'YYYY-MM')
        = to_char(now() at time zone 'Asia/Taipei', 'YYYY-MM')
  )                                                               as month_views,
  max(viewed_at)                                                  as last_viewed_at
from public.page_views
group by project_id;

-- 3-4 專案內各頁面的熱門度（看哪一課最多人讀）
create or replace view public.v_views_by_page
with (security_invoker = off) as
select
  project_id,
  coalesce(page_path, '(index)') as page_path,
  count(*)                       as views
from public.page_views
group by project_id, page_path;

-- ── 4. 開放 View 的讀取權限 ────────────────────────────────
grant select on public.v_views_daily    to anon, authenticated;
grant select on public.v_views_monthly  to anon, authenticated;
grant select on public.v_views_summary  to anon, authenticated;
grant select on public.v_views_by_page  to anon, authenticated;

-- ── 5.（選用）自動清理 400 天前的原始紀錄，避免免費額度爆掉 ──
-- 彙總數字建議另外存成快照表，這裡先只做原始資料清理。
-- 需要 pg_cron extension，Supabase 免費方案可在 Database → Extensions 開啟。
--
-- select cron.schedule(
--   'purge-old-page-views', '0 4 * * *',
--   $$ delete from public.page_views where viewed_at < now() - interval '400 days' $$
-- );


-- ═══════════════════════════════════════════════════════════
--  驗證：跑完之後執行下面兩行應該都要成功
-- ═══════════════════════════════════════════════════════════
-- insert into public.page_views (project_id, page_path, visitor_id) values ('test','x','abc');
-- select * from public.v_views_summary;
