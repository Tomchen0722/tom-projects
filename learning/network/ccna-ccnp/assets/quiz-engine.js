/* 共用測驗引擎 — 支援單選/複選、練習模式、模擬考模式、計時、錯題複習、進度保存
   用法：QuizEngine.init({ mount:'#quiz', bank: QUESTION_BANK, examCount:60, examMinutes:90, passScore:80, storageKey:'ccna' }) */
(function (global) {
  'use strict';

  var S = {};           // state
  var CFG = {};
  var root;

  function el(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html !== undefined) e.innerHTML = html;
    return e;
  }

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function shuffle(arr) {
    var a = arr.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  function store(key, val) {
    try {
      if (val === undefined) return JSON.parse(localStorage.getItem(CFG.storageKey + ':' + key) || 'null');
      localStorage.setItem(CFG.storageKey + ':' + key, JSON.stringify(val));
    } catch (e) { return null; }
  }

  function domains() {
    var m = {};
    CFG.bank.forEach(function (q) { m[q.domain] = (m[q.domain] || 0) + 1; });
    return m;
  }

  /* ---------- 首頁 ---------- */
  function renderHome() {
    clearTimer();
    var d = domains();
    var wrong = store('wrong') || [];
    var hist = store('history') || [];
    var h = '';

    h += '<div class="qz-hero">';
    h += '<h2>' + esc(CFG.title || '模擬試題') + '</h2>';
    h += '<p>' + CFG.bank.length + ' 題題庫 · 每題附詳解 · 進度自動保存在本機瀏覽器</p>';
    h += '</div>';

    h += '<div class="qz-modes">';
    h += '<div class="qz-mode" data-mode="exam"><div class="qz-mi">📝</div><h3>模擬考模式</h3>'
      + '<p>隨機抽 ' + CFG.examCount + ' 題，限時 ' + CFG.examMinutes + ' 分鐘，交卷後才看答案。'
      + '及格標準 ' + CFG.passScore + ' 分。</p><button class="qz-btn">開始模擬考</button></div>';
    h += '<div class="qz-mode" data-mode="practice"><div class="qz-mi">📚</div><h3>練習模式</h3>'
      + '<p>不限時，作答後立刻看詳解。適合邊讀邊練，可依主題篩選。</p><button class="qz-btn qz-btn2">開始練習</button></div>';
    h += '<div class="qz-mode" data-mode="wrong"><div class="qz-mi">🔁</div><h3>錯題複習</h3>'
      + '<p>目前累積 <b>' + wrong.length + '</b> 題錯題。反覆做到全對為止，答對就自動移出。</p>'
      + '<button class="qz-btn qz-btn3"' + (wrong.length ? '' : ' disabled') + '>複習錯題</button></div>';
    h += '</div>';

    h += '<div class="qz-panel"><h3>依主題練習</h3><div class="qz-dom">';
    Object.keys(d).forEach(function (k) {
      h += '<button class="qz-chip" data-domain="' + esc(k) + '">' + esc(k) + ' <span>' + d[k] + '</span></button>';
    });
    h += '</div></div>';

    if (hist.length) {
      h += '<div class="qz-panel"><h3>歷史成績</h3><table class="qz-tbl"><thead><tr><th>日期</th><th>模式</th><th>分數</th><th>結果</th></tr></thead><tbody>';
      hist.slice(-10).reverse().forEach(function (r) {
        h += '<tr><td>' + esc(r.date) + '</td><td>' + esc(r.mode) + '</td><td>' + r.score + ' / ' + r.total
          + '（' + r.pct + '%）</td><td>' + (r.pass ? '<span class="qz-pass">通過</span>' : '<span class="qz-fail">未達標</span>') + '</td></tr>';
      });
      h += '</tbody></table><button class="qz-clear">清除歷史紀錄</button></div>';
    }

    root.innerHTML = h;

    root.querySelectorAll('.qz-mode').forEach(function (m) {
      m.querySelector('button').addEventListener('click', function () {
        var mode = m.getAttribute('data-mode');
        if (mode === 'exam') start('exam', shuffle(CFG.bank).slice(0, CFG.examCount));
        else if (mode === 'practice') start('practice', shuffle(CFG.bank));
        else {
          var ids = store('wrong') || [];
          var qs = CFG.bank.filter(function (q) { return ids.indexOf(q.id) >= 0; });
          if (qs.length) start('wrong', shuffle(qs));
        }
      });
    });
    root.querySelectorAll('.qz-chip').forEach(function (c) {
      c.addEventListener('click', function () {
        var dm = c.getAttribute('data-domain');
        start('practice', shuffle(CFG.bank.filter(function (q) { return q.domain === dm; })));
      });
    });
    var cl = root.querySelector('.qz-clear');
    if (cl) cl.addEventListener('click', function () { store('history', []); renderHome(); });
  }

  /* ---------- 開始作答 ---------- */
  function start(mode, questions) {
    S = { mode: mode, qs: questions, i: 0, answers: {}, revealed: {}, startedAt: Date.now() };
    if (mode === 'exam') {
      S.deadline = Date.now() + CFG.examMinutes * 60000;
      startTimer();
    }
    renderQuestion();
  }

  var timerId = null;
  function startTimer() {
    clearTimer();
    timerId = setInterval(function () {
      var left = S.deadline - Date.now();
      var t = root.querySelector('.qz-timer');
      if (left <= 0) { clearTimer(); finish(); return; }
      if (t) {
        var m = Math.floor(left / 60000), s = Math.floor((left % 60000) / 1000);
        t.textContent = '⏱ ' + m + ':' + (s < 10 ? '0' : '') + s;
        t.className = 'qz-timer' + (left < 300000 ? ' qz-urgent' : '');
      }
    }, 500);
  }
  function clearTimer() { if (timerId) { clearInterval(timerId); timerId = null; } }

  /* ---------- 題目畫面 ---------- */
  function renderQuestion() {
    var q = S.qs[S.i];
    var multi = q.answer.length > 1;
    var picked = S.answers[q.id] || [];
    var revealed = !!S.revealed[q.id];
    var h = '';

    h += '<div class="qz-bar">';
    h += '<button class="qz-back">← 離開</button>';
    h += '<div class="qz-prog"><div class="qz-prog-in" style="width:' + ((S.i + 1) / S.qs.length * 100) + '%"></div></div>';
    h += '<span class="qz-count">' + (S.i + 1) + ' / ' + S.qs.length + '</span>';
    if (S.mode === 'exam') h += '<span class="qz-timer">⏱ --:--</span>';
    h += '</div>';

    h += '<div class="qz-q">';
    h += '<div class="qz-meta"><span class="qz-tag">' + esc(q.domain) + '</span>'
      + (multi ? '<span class="qz-tag qz-multi">複選 · 選 ' + q.answer.length + ' 項</span>' : '<span class="qz-tag">單選</span>')
      + (q.level ? '<span class="qz-tag qz-lv' + q.level + '">' + (q.level === 1 ? 'CCNA' : 'CCNP') + '</span>' : '')
      + '</div>';
    h += '<div class="qz-stem">' + q.q + '</div>';
    if (q.code) h += '<pre class="qz-code"><code>' + esc(q.code) + '</code></pre>';

    h += '<div class="qz-opts">';
    q.options.forEach(function (opt, idx) {
      var cls = 'qz-opt';
      if (picked.indexOf(idx) >= 0) cls += ' qz-sel';
      if (revealed) {
        if (q.answer.indexOf(idx) >= 0) cls += ' qz-right';
        else if (picked.indexOf(idx) >= 0) cls += ' qz-wrong';
      }
      h += '<button class="' + cls + '" data-idx="' + idx + '"' + (revealed ? ' disabled' : '') + '>'
        + '<span class="qz-letter">' + 'ABCDEF'[idx] + '</span><span class="qz-text">' + opt + '</span></button>';
    });
    h += '</div>';

    if (revealed) {
      var correct = isCorrect(q, picked);
      h += '<div class="qz-exp ' + (correct ? 'qz-exp-ok' : 'qz-exp-no') + '">';
      h += '<div class="qz-exp-h">' + (correct ? '✅ 答對了' : '❌ 答錯了') + '　正確答案：'
        + q.answer.map(function (a) { return 'ABCDEF'[a]; }).join('、') + '</div>';
      h += '<div class="qz-exp-b">' + q.explain + '</div>';
      if (q.ref) h += '<div class="qz-ref">📖 延伸閱讀：<a href="' + q.ref + '">' + esc(q.refText || '相關章節') + '</a></div>';
      h += '</div>';
    }

    h += '<div class="qz-nav">';
    h += '<button class="qz-prev"' + (S.i === 0 ? ' disabled' : '') + '>← 上一題</button>';
    if (S.mode !== 'exam' && !revealed) h += '<button class="qz-check qz-btn">送出答案</button>';
    if (S.i === S.qs.length - 1) h += '<button class="qz-finish qz-btn">交卷看成績</button>';
    else h += '<button class="qz-next">下一題 →</button>';
    h += '</div>';

    h += '</div>';
    root.innerHTML = h;

    root.querySelectorAll('.qz-opt').forEach(function (b) {
      b.addEventListener('click', function () {
        var idx = +b.getAttribute('data-idx');
        var cur = S.answers[q.id] || [];
        if (multi) {
          var p = cur.indexOf(idx);
          if (p >= 0) cur.splice(p, 1); else cur.push(idx);
        } else {
          cur = [idx];
        }
        S.answers[q.id] = cur;
        if (S.mode !== 'exam' && !multi) S.revealed[q.id] = true;
        renderQuestion();
      });
    });

    root.querySelector('.qz-back').addEventListener('click', function () {
      if (confirm('確定要離開？目前作答不會保存。')) { clearTimer(); renderHome(); }
    });
    var pv = root.querySelector('.qz-prev');
    if (pv) pv.addEventListener('click', function () { if (S.i > 0) { S.i--; renderQuestion(); } });
    var nx = root.querySelector('.qz-next');
    if (nx) nx.addEventListener('click', function () { S.i++; renderQuestion(); });
    var ck = root.querySelector('.qz-check');
    if (ck) ck.addEventListener('click', function () { S.revealed[q.id] = true; renderQuestion(); });
    var fi = root.querySelector('.qz-finish');
    if (fi) fi.addEventListener('click', function () { if (S.mode !== 'exam' || confirm('確定交卷？')) finish(); });

    if (S.mode === 'exam') startTimer();
  }

  function isCorrect(q, picked) {
    if (!picked || picked.length !== q.answer.length) return false;
    return q.answer.every(function (a) { return picked.indexOf(a) >= 0; });
  }

  /* ---------- 成績 ---------- */
  function finish() {
    clearTimer();
    var right = 0, byDomain = {}, wrongList = [];
    S.qs.forEach(function (q) {
      var ok = isCorrect(q, S.answers[q.id]);
      byDomain[q.domain] = byDomain[q.domain] || { r: 0, t: 0 };
      byDomain[q.domain].t++;
      if (ok) { right++; byDomain[q.domain].r++; } else { wrongList.push(q); }
    });
    var pct = Math.round(right / S.qs.length * 100);
    var pass = pct >= CFG.passScore;

    // 更新錯題本
    var wrongIds = store('wrong') || [];
    S.qs.forEach(function (q) {
      var ok = isCorrect(q, S.answers[q.id]);
      var at = wrongIds.indexOf(q.id);
      if (!ok && at < 0) wrongIds.push(q.id);
      if (ok && at >= 0) wrongIds.splice(at, 1);
    });
    store('wrong', wrongIds);

    var hist = store('history') || [];
    hist.push({
      date: new Date().toLocaleString('zh-TW', { hour12: false }).slice(0, 16),
      mode: { exam: '模擬考', practice: '練習', wrong: '錯題複習' }[S.mode],
      score: right, total: S.qs.length, pct: pct, pass: pass
    });
    store('history', hist.slice(-50));

    var mins = Math.round((Date.now() - S.startedAt) / 60000);
    var h = '';
    h += '<div class="qz-result ' + (pass ? 'qz-r-pass' : 'qz-r-fail') + '">';
    h += '<div class="qz-score">' + pct + '<span>%</span></div>';
    h += '<div class="qz-verdict">' + (pass ? '🎉 通過！' : '再加把勁') + '</div>';
    h += '<p>答對 ' + right + ' / ' + S.qs.length + ' 題　·　用時 ' + mins + ' 分鐘　·　及格線 ' + CFG.passScore + '%</p>';
    h += '</div>';

    h += '<div class="qz-panel"><h3>各主題表現</h3><table class="qz-tbl"><thead><tr><th>主題</th><th>答對</th><th>正確率</th><th></th></tr></thead><tbody>';
    Object.keys(byDomain).sort(function (a, b) {
      return (byDomain[a].r / byDomain[a].t) - (byDomain[b].r / byDomain[b].t);
    }).forEach(function (k) {
      var v = byDomain[k], p = Math.round(v.r / v.t * 100);
      h += '<tr><td>' + esc(k) + '</td><td>' + v.r + ' / ' + v.t + '</td><td>' + p + '%</td>'
        + '<td><div class="qz-mini"><div class="qz-mini-in" style="width:' + p + '%;background:'
        + (p >= 80 ? '#22C55E' : p >= 60 ? '#D97706' : '#EF4444') + '"></div></div></td></tr>';
    });
    h += '</tbody></table></div>';

    if (wrongList.length) {
      h += '<div class="qz-panel"><h3>錯題檢討（' + wrongList.length + ' 題）</h3>';
      wrongList.forEach(function (q) {
        var picked = S.answers[q.id] || [];
        h += '<div class="qz-rev"><div class="qz-rev-q">' + q.q + '</div>';
        h += '<div class="qz-rev-a"><b>你的答案：</b>' + (picked.length ? picked.map(function (i) { return 'ABCDEF'[i]; }).join('、') : '未作答')
          + '　<b>正解：</b>' + q.answer.map(function (i) { return 'ABCDEF'[i]; }).join('、') + '</div>';
        h += '<div class="qz-rev-e">' + q.explain + '</div></div>';
      });
      h += '</div>';
    }

    h += '<div class="qz-nav"><button class="qz-home qz-btn">回測驗首頁</button>';
    if (wrongList.length) h += '<button class="qz-redo qz-btn qz-btn3">立刻重做這 ' + wrongList.length + ' 題錯題</button>';
    h += '</div>';

    root.innerHTML = h;
    root.querySelector('.qz-home').addEventListener('click', renderHome);
    var rd = root.querySelector('.qz-redo');
    if (rd) rd.addEventListener('click', function () { start('wrong', shuffle(wrongList)); });
    window.scrollTo(0, 0);
  }

  global.QuizEngine = {
    init: function (cfg) {
      CFG = cfg;
      CFG.examCount = Math.min(cfg.examCount || 50, cfg.bank.length);
      CFG.examMinutes = cfg.examMinutes || 90;
      CFG.passScore = cfg.passScore || 80;
      CFG.storageKey = cfg.storageKey || 'quiz';
      root = document.querySelector(cfg.mount);
      renderHome();
    }
  };
})(window);
