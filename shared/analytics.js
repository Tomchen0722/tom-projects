/* ═══════════════════════════════════════════════════════════
   作品集瀏覽計數器 — 前端追蹤 + 顯示
   ───────────────────────────────────────────────────────────
   使用方式（在頁面底部加兩行）：

     <script>window.ANALYTICS_CONFIG={url:'https://xxx.supabase.co',key:'eyJ...'}</script>
     <script src="路徑/analytics.js" data-project="ccna-ccnp"></script>

   data-project 對應 projects.json 的 id，首頁請填 hub。
   沒設定 url / key 時會自動退回本機 localStorage 計數，不會報錯。

   顯示計數：在頁面放一個 <span id="view-counter"></span> 即可。
   ═══════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  var CFG = window.ANALYTICS_CONFIG || {};
  var script = document.currentScript;
  var PROJECT = (script && script.getAttribute('data-project')) || 'unknown';
  var PAGE = (function () {
    var f = location.pathname.split('/').pop();
    return f && f !== '' ? f : 'index.html';
  })();
  var LIVE = !!(CFG.url && CFG.key);
  var DEDUPE_MINUTES = 30;

  /* ── 匿名訪客 ID：隨機字串，不含任何個人資訊 ── */
  function visitorId() {
    var k = 'pf:vid', v;
    try {
      v = localStorage.getItem(k);
      if (!v) {
        v = 'v' + Math.random().toString(36).slice(2) + Date.now().toString(36);
        localStorage.setItem(k, v);
      }
    } catch (e) {
      v = 'anon';
    }
    return v;
  }

  /* ── 短時間內重複整理不重複計數 ── */
  function shouldCount() {
    var k = 'pf:seen:' + PROJECT + ':' + PAGE;
    try {
      var last = +(sessionStorage.getItem(k) || 0);
      if (Date.now() - last < DEDUPE_MINUTES * 60000) return false;
      sessionStorage.setItem(k, Date.now());
    } catch (e) { /* 隱私模式下就照常計數 */ }
    return true;
  }

  /* ── 本機備援計數（未設定 Supabase 時使用）── */
  function localBump() {
    var k = 'pf:count:' + PROJECT;
    try {
      var d = JSON.parse(localStorage.getItem(k) || '{"total":0,"days":{}}');
      var today = new Date().toISOString().slice(0, 10);
      d.total++;
      d.days[today] = (d.days[today] || 0) + 1;
      localStorage.setItem(k, JSON.stringify(d));
      return d;
    } catch (e) { return { total: 0, days: {} }; }
  }

  function localRead() {
    try {
      return JSON.parse(localStorage.getItem('pf:count:' + PROJECT) || '{"total":0,"days":{}}');
    } catch (e) { return { total: 0, days: {} }; }
  }

  /* ── 送出一筆瀏覽紀錄 ── */
  function track() {
    if (!shouldCount()) return Promise.resolve();
    if (!LIVE) { localBump(); return Promise.resolve(); }

    return fetch(CFG.url + '/rest/v1/page_views', {
      method: 'POST',
      headers: {
        'apikey': CFG.key,
        'Authorization': 'Bearer ' + CFG.key,
        'Content-Type': 'application/json',
        'Prefer': 'return=minimal'
      },
      body: JSON.stringify({
        project_id: PROJECT,
        page_path: PAGE,
        visitor_id: visitorId(),
        referrer: document.referrer ? document.referrer.slice(0, 300) : null
      })
    }).catch(function () { localBump(); });
  }

  /* ── 讀取某專案的統計摘要 ── */
  function summary(projectId) {
    projectId = projectId || PROJECT;
    if (!LIVE) {
      var d = localRead();
      var today = new Date().toISOString().slice(0, 10);
      var ym = today.slice(0, 7);
      var month = Object.keys(d.days).reduce(function (s, k) {
        return k.indexOf(ym) === 0 ? s + d.days[k] : s;
      }, 0);
      return Promise.resolve({
        project_id: projectId, total_views: d.total,
        today_views: d.days[today] || 0, month_views: month, local: true
      });
    }
    return fetch(CFG.url + '/rest/v1/v_views_summary?project_id=eq.' + encodeURIComponent(projectId),
      { headers: { 'apikey': CFG.key, 'Authorization': 'Bearer ' + CFG.key } })
      .then(function (r) { return r.json(); })
      .then(function (rows) {
        return rows[0] || { project_id: projectId, total_views: 0, today_views: 0, month_views: 0 };
      })
      .catch(function () { return { project_id: projectId, total_views: 0, today_views: 0, month_views: 0, error: true }; });
  }

  /* ── 讀取全部專案的統計 ── */
  function allSummary() {
    if (!LIVE) return Promise.resolve([]);
    return fetch(CFG.url + '/rest/v1/v_views_summary?order=total_views.desc',
      { headers: { 'apikey': CFG.key, 'Authorization': 'Bearer ' + CFG.key } })
      .then(function (r) { return r.json(); }).catch(function () { return []; });
  }

  /* ── 讀取每日趨勢（近 N 天）── */
  function daily(projectId, days) {
    if (!LIVE) return Promise.resolve([]);
    var since = new Date(Date.now() - (days || 30) * 86400000).toISOString().slice(0, 10);
    var q = '/rest/v1/v_views_daily?day=gte.' + since + '&order=day.asc';
    if (projectId) q += '&project_id=eq.' + encodeURIComponent(projectId);
    return fetch(CFG.url + q, { headers: { 'apikey': CFG.key, 'Authorization': 'Bearer ' + CFG.key } })
      .then(function (r) { return r.json(); }).catch(function () { return []; });
  }

  /* ── 讀取每月統計 ── */
  function monthly(projectId) {
    if (!LIVE) return Promise.resolve([]);
    var q = '/rest/v1/v_views_monthly?order=month.asc';
    if (projectId) q += '&project_id=eq.' + encodeURIComponent(projectId);
    return fetch(CFG.url + q, { headers: { 'apikey': CFG.key, 'Authorization': 'Bearer ' + CFG.key } })
      .then(function (r) { return r.json(); }).catch(function () { return []; });
  }

  /* ── 把數字填進 #view-counter ── */
  function paint() {
    var box = document.getElementById('view-counter');
    if (!box) return;
    summary().then(function (s) {
      box.innerHTML =
        '<span class="vc-item"><b>' + (s.today_views || 0) + '</b> 今日</span>' +
        '<span class="vc-item"><b>' + (s.month_views || 0) + '</b> 本月</span>' +
        '<span class="vc-item"><b>' + (s.total_views || 0) + '</b> 總計</span>' +
        (s.local ? '<span class="vc-note">本機計數</span>' : '');
      box.classList.add('vc-ready');
    });
  }

  window.PortfolioAnalytics = {
    project: PROJECT, live: LIVE,
    track: track, summary: summary, allSummary: allSummary,
    daily: daily, monthly: monthly, paint: paint
  };

  function boot() { track().then(paint); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
