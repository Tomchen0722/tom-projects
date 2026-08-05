/* ═══════════════════════════════════════════════════════════
   瀏覽計數器設定 — 填入你的 Supabase 專案資訊
   ───────────────────────────────────────────────────────────
   到 Supabase 後台 → Project Settings → API：

     url  = Project URL          （例如 https://abcdefgh.supabase.co）
     key  = Project API keys 的 anon / public 那一把

   ⚠️ 一定要用 anon（public）那把，絕對不要貼 service_role。
      service_role 有完整讀寫刪除權限，貼到前端等於把資料庫交出去。
      anon key 設計上就是公開的，安全性靠 analytics-schema.sql 裡的 RLS 政策把關。

   兩個值留空時，計數器會自動退回本機 localStorage 模式，
   頁面照常運作、不會報錯，只是數字僅代表你自己這台瀏覽器。
   ═══════════════════════════════════════════════════════════ */
window.ANALYTICS_CONFIG = {
  url: 'https://rkotktpmpatojxxnqlpj.supabase.co',
  key: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJrb3RrdHBtcGF0b2p4eG5xbHBqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODEyOTgxMTAsImV4cCI6MjA5Njg3NDExMH0.GRs9u9t7pU5ERTtXkMYovCL0d1bqCcQGXvIdNxAtGqk'
};
