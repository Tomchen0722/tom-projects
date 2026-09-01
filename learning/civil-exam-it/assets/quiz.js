/* 線上作答引擎 — 公職資訊處理國考教材
   用法：任一 .quiz 容器內的 .q[data-ans] 會自動變成可作答題目。
   容器可設：data-quiz（卷別名稱）／data-per（每題配分）／data-limit（限時分鐘）／data-pass（及格分）
   作答進度存在瀏覽器本機（localStorage），重新整理不會不見。 */
(function () {
  'use strict';

  var LS = 'civil-exam-quiz:';

  function load(k) {
    try { return JSON.parse(localStorage.getItem(LS + k) || '{}'); } catch (e) { return {}; }
  }
  function save(k, v) {
    try { localStorage.setItem(LS + k, JSON.stringify(v)); } catch (e) { /* 私密視窗等情形直接略過 */ }
  }
  function drop(k) {
    try { localStorage.removeItem(LS + k); } catch (e) { }
  }
  function el(tag, cls, html) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (html != null) n.innerHTML = html;
    return n;
  }
  function pad(n) { return (n < 10 ? '0' : '') + n; }

  function initQuiz(box, idx) {
    var qs = [].slice.call(box.querySelectorAll('.q[data-ans]'));
    if (!qs.length) return;

    var key = (box.dataset.quizId || (location.pathname + '#' + idx)).replace(/\s+/g, '');
    var per = parseFloat(box.dataset.per || '0') || (100 / qs.length);
    var pass = parseFloat(box.dataset.pass || '60');
    var limit = parseInt(box.dataset.limit || '0', 10);
    var title = box.dataset.quiz || '本卷';
    var practice = box.dataset.mode === 'practice';
    var state = load(key);
    var picked = state.picked || {};
    var graded = false;

    if (practice) { initPractice(box, qs, key, title, picked); return; }

    /* ---------- 工具列 ---------- */
    var bar = el('div', 'quiz-bar');
    var stat = el('div', 'qb-stat', '已作答 <b>0</b> / ' + qs.length + ' 題');
    var timer = el('div', 'qb-timer', '');
    var spacer = el('div', 'qb-spacer');
    var bSubmit = el('button', 'qb-submit', '📊 交卷評分');
    var bWrong = el('button', 'qb-ghost', '🔁 只看錯題');
    var bRetry = el('button', 'qb-ghost', '✏️ 重做錯題');
    var bReset = el('button', 'qb-ghost', '🗑️ 全部清除');
    var prog = el('div', 'qb-prog', '<i></i>');
    bSubmit.type = bWrong.type = bRetry.type = bReset.type = 'button';
    bWrong.disabled = bRetry.disabled = true;
    bar.appendChild(stat);
    if (limit) bar.appendChild(timer);
    bar.appendChild(spacer);
    bar.appendChild(bSubmit);
    bar.appendChild(bWrong);
    bar.appendChild(bRetry);
    bar.appendChild(bReset);
    bar.appendChild(prog);
    box.insertBefore(bar, box.firstChild);

    /* ---------- 成績面板 ---------- */
    var res = el('div', 'quiz-result');
    box.appendChild(res);

    /* ---------- 綁定選項 ---------- */
    qs.forEach(function (q, i) {
      q.id = q.id || (key.replace(/[^\w-]/g, '') + '-q' + (i + 1));
      [].slice.call(q.querySelectorAll('.ch')).forEach(function (btn) {
        btn.addEventListener('click', function () {
          if (graded) return;
          var n = q.dataset.qno || String(i + 1);
          if (picked[n] === btn.dataset.ch) delete picked[n]; else picked[n] = btn.dataset.ch;
          paint(q, n);
          persist();
          refresh();
        });
      });
    });

    function paint(q, n) {
      [].slice.call(q.querySelectorAll('.ch')).forEach(function (b) {
        b.classList.toggle('sel', picked[n] === b.dataset.ch);
      });
    }
    function persist() { save(key, { picked: picked, graded: graded }); }

    function answered() {
      return qs.filter(function (q, i) { return picked[q.dataset.qno || String(i + 1)]; }).length;
    }
    function refresh() {
      var a = answered();
      stat.innerHTML = '已作答 <b>' + a + '</b> / ' + qs.length + ' 題';
      prog.firstChild.style.width = (a / qs.length * 100) + '%';
    }

    /* ---------- 評分 ---------- */
    function grade() {
      graded = true;
      var right = 0, wrong = [], blank = [];
      qs.forEach(function (q, i) {
        var n = q.dataset.qno || String(i + 1);
        var pick = picked[n], ans = q.dataset.ans;
        q.classList.add('graded');
        q.classList.remove('ok', 'ng', 'na');
        var mark = q.querySelector('.mark') || (function () {
          var m = el('span', 'mark', '');
          q.insertBefore(m, q.firstChild);
          return m;
        })();
        [].slice.call(q.querySelectorAll('.ch')).forEach(function (b) {
          b.classList.remove('right', 'wrong');
          if (b.dataset.ch === ans) b.classList.add('right');
          else if (b.dataset.ch === pick) b.classList.add('wrong');
        });
        if (!pick) { q.classList.add('na'); mark.textContent = '未作答 · 正解 ' + ans; blank.push({ n: n, id: q.id }); }
        else if (pick === ans) { q.classList.add('ok'); mark.textContent = '✓ 答對'; right++; }
        else { q.classList.add('ng'); mark.textContent = '✗ 你選 ' + pick + '．正解 ' + ans; wrong.push({ n: n, id: q.id }); }
      });

      var score = Math.round(right * per * 10) / 10;
      var cls = score >= pass ? 'pass' : (score >= pass - 10 ? 'near' : 'fail');
      var say = cls === 'pass'
        ? '達到及格標準。請仍把錯題與未作答題看過一遍——<strong>同一個觀念下次換個問法就可能失分</strong>。'
        : (cls === 'near'
          ? '差一點。<strong>先攻錯題</strong>：把下面每一題的詳解看懂，通常補這幾個觀念就能過。'
          : '離及格還有距離。建議<strong>先回頭讀該科講義與深化教材</strong>，再回來重做本卷，不要急著寫下一份。');

      function links(arr, k) {
        if (!arr.length) return '<span style="color:#16a34a">無</span>';
        return arr.map(function (o) {
          return '<a href="#' + o.id + '" class="' + k + '" data-goto="' + o.id + '">' + o.n + '</a>';
        }).join('');
      }

      res.innerHTML =
        '<h4>📊 ' + title + '　評分結果</h4>' +
        '<div class="qr-score">' +
        '<div><span>得分</span><b>' + score + '</b></div>' +
        '<div><span>答對</span><b>' + right + '</b></div>' +
        '<div><span>答錯</span><b>' + wrong.length + '</b></div>' +
        '<div><span>未作答</span><b>' + blank.length + '</b></div>' +
        '<div><span>正確率</span><b>' + Math.round(right / qs.length * 100) + '%</b></div>' +
        '</div>' +
        '<div class="qr-verdict ' + cls + '">' + say + '</div>' +
        '<div class="qr-wrong"><strong>❌ 答錯題號</strong>（點題號跳到該題看詳解）<br>' + links(wrong, '') + '</div>' +
        '<div class="qr-wrong" style="margin-top:8px"><strong>⬜ 未作答題號</strong><br>' + links(blank, 'blank') + '</div>';
      res.classList.add('show');

      [].slice.call(res.querySelectorAll('a[data-goto]')).forEach(function (a) {
        a.addEventListener('click', function (ev) {
          ev.preventDefault();
          box.classList.remove('only-wrong');
          bWrong.classList.remove('on');
          bWrong.textContent = '🔁 只看錯題';
          var t = document.getElementById(a.dataset.goto);
          if (!t) return;
          t.scrollIntoView({ behavior: 'smooth', block: 'center' });
          t.classList.remove('flash');
          void t.offsetWidth;
          t.classList.add('flash');
        });
      });

      bSubmit.disabled = true;
      bWrong.disabled = false;
      bRetry.disabled = !(wrong.length + blank.length);
      if (tid) { clearInterval(tid); tid = 0; }
      timer.textContent = '';
      persist();
      res.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    function ungrade(keepRight) {
      graded = false;
      qs.forEach(function (q, i) {
        var n = q.dataset.qno || String(i + 1);
        var wasWrong = q.classList.contains('ng') || q.classList.contains('na');
        q.classList.remove('graded', 'ok', 'ng', 'na', 'flash');
        var m = q.querySelector('.mark');
        if (m) m.textContent = '';
        if (!keepRight || wasWrong) delete picked[n];
        [].slice.call(q.querySelectorAll('.ch')).forEach(function (b) {
          b.classList.remove('right', 'wrong');
        });
        paint(q, n);
      });
      res.classList.remove('show');
      res.innerHTML = '';
      box.classList.remove('only-wrong');
      bWrong.classList.remove('on');
      bWrong.textContent = '🔁 只看錯題';
      bSubmit.disabled = false;
      bWrong.disabled = bRetry.disabled = true;
      persist();
      refresh();
      if (limit) startTimer();
      bar.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    bSubmit.addEventListener('click', function () {
      var a = answered();
      if (a < qs.length && !confirm('還有 ' + (qs.length - a) + ' 題未作答，確定要交卷嗎？\n（正式考試不倒扣，建議每題都選）')) return;
      grade();
    });
    bWrong.addEventListener('click', function () {
      var on = box.classList.toggle('only-wrong');
      bWrong.classList.toggle('on', on);
      bWrong.textContent = on ? '📄 顯示全部' : '🔁 只看錯題';
    });
    bRetry.addEventListener('click', function () { ungrade(true); });
    bReset.addEventListener('click', function () {
      if (!confirm('將清除本卷所有作答紀錄，確定？')) return;
      picked = {};
      drop(key);
      ungrade(false);
    });

    /* ---------- 計時 ---------- */
    var tid = 0, left = limit * 60;
    function startTimer() {
      left = limit * 60;
      if (tid) clearInterval(tid);
      tick();
      tid = setInterval(tick, 1000);
    }
    function tick() {
      timer.textContent = '⏱ 剩餘 ' + pad(Math.floor(left / 60)) + ':' + pad(left % 60);
      timer.classList.toggle('warnx', left <= 300);
      if (left <= 0) { clearInterval(tid); tid = 0; grade(); return; }
      left--;
    }

    /* ---------- 還原上次進度 ---------- */
    qs.forEach(function (q, i) { paint(q, q.dataset.qno || String(i + 1)); });
    refresh();
    if (state.graded && answered()) grade();
    else if (limit) startTimer();
  }

  /* ============ 題庫練習模式：點下去立刻判對錯並展開詳解 ============ */
  function initPractice(box, qs, key, title, picked) {
    var bar = el('div', 'quiz-bar');
    var stat = el('div', 'qb-stat', '');
    var spacer = el('div', 'qb-spacer');
    var bWrong = el('button', 'qb-ghost', '🔁 只看錯題');
    var bRetry = el('button', 'qb-ghost', '✏️ 重做錯題');
    var bReset = el('button', 'qb-ghost', '🗑️ 全部清除');
    var prog = el('div', 'qb-prog', '<i></i>');
    bWrong.type = bRetry.type = bReset.type = 'button';
    bar.appendChild(stat);
    bar.appendChild(spacer);
    bar.appendChild(bWrong);
    bar.appendChild(bRetry);
    bar.appendChild(bReset);
    bar.appendChild(prog);
    box.insertBefore(bar, box.firstChild);

    function persist() { save(key, { picked: picked, practice: 1 }); }

    function tally() {
      var done = 0, right = 0;
      qs.forEach(function (q) {
        var p = picked[q.dataset.qno];
        if (!p) return;
        done++;
        if (p === q.dataset.ans) right++;
      });
      var rate = done ? Math.round(right / done * 100) : 0;
      stat.innerHTML = '已練 <b>' + done + '</b> / ' + qs.length + ' 題　答對 <b>' + right
        + '</b>　答錯 <b>' + (done - right) + '</b>　正確率 <b>' + rate + '%</b>';
      prog.firstChild.style.width = (done / qs.length * 100) + '%';
      bWrong.disabled = bRetry.disabled = (done - right) === 0;
    }

    function show(q) {
      var pick = picked[q.dataset.qno], ans = q.dataset.ans;
      var mark = q.querySelector('.mark');
      if (!mark) { mark = el('span', 'mark', ''); q.insertBefore(mark, q.firstChild); }
      q.classList.remove('graded', 'ok', 'ng');
      [].slice.call(q.querySelectorAll('.ch')).forEach(function (b) {
        b.classList.remove('right', 'wrong', 'sel');
        b.classList.toggle('sel', b.dataset.ch === pick);
      });
      var det = q.querySelector('details');
      if (!pick) { if (det) det.open = false; mark.textContent = ''; return; }
      q.classList.add('graded', pick === ans ? 'ok' : 'ng');
      mark.textContent = pick === ans ? '✓ 答對' : ('✗ 你選 ' + pick + '．正解 ' + ans);
      [].slice.call(q.querySelectorAll('.ch')).forEach(function (b) {
        if (b.dataset.ch === ans) b.classList.add('right');
        else if (b.dataset.ch === pick) b.classList.add('wrong');
      });
      if (det) det.open = true;
    }

    qs.forEach(function (q, i) {
      q.dataset.qno = q.dataset.qno || String(i + 1);
      q.id = q.id || (key.replace(/[^\w-]/g, '') + '-q' + q.dataset.qno);
      [].slice.call(q.querySelectorAll('.ch')).forEach(function (btn) {
        btn.addEventListener('click', function () {
          if (picked[q.dataset.qno]) return;      // 已作答就鎖住，避免看到答案再改
          picked[q.dataset.qno] = btn.dataset.ch;
          show(q);
          persist();
          tally();
        });
      });
      show(q);
    });

    bWrong.addEventListener('click', function () {
      var on = box.classList.toggle('only-wrong');
      bWrong.classList.toggle('on', on);
      bWrong.textContent = on ? '📄 顯示全部' : '🔁 只看錯題';
    });
    bRetry.addEventListener('click', function () {
      qs.forEach(function (q) {
        if (picked[q.dataset.qno] && picked[q.dataset.qno] !== q.dataset.ans) {
          delete picked[q.dataset.qno];
          show(q);
        }
      });
      box.classList.remove('only-wrong');
      bWrong.classList.remove('on');
      bWrong.textContent = '🔁 只看錯題';
      persist();
      tally();
      bar.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    });
    bReset.addEventListener('click', function () {
      if (!confirm('將清除「' + title + '」的所有練習紀錄，確定？')) return;
      Object.keys(picked).forEach(function (k) { delete picked[k]; });
      drop(key);
      qs.forEach(show);
      box.classList.remove('only-wrong');
      bWrong.classList.remove('on');
      bWrong.textContent = '🔁 只看錯題';
      tally();
    });

    tally();
  }

  /* ---------- 申論自評表 ---------- */
  function initSelf(box) {
    var boxes = [].slice.call(box.querySelectorAll('input[type=checkbox][data-pt]'));
    if (!boxes.length) return;
    var out = box.querySelector('.ss-out');
    var full = boxes.reduce(function (s, b) { return s + (parseFloat(b.dataset.pt) || 0); }, 0);
    function calc() {
      var got = boxes.reduce(function (s, b) { return s + (b.checked ? (parseFloat(b.dataset.pt) || 0) : 0); }, 0);
      got = Math.round(got * 10) / 10;
      var pct = full ? Math.round(got / full * 100) : 0;
      var tip = pct >= 70 ? '拿分點掌握良好，可再練速度與版面。'
        : (pct >= 50 ? '骨架有了，缺的是「地方特有限制」與「具體作法」這類具體句。'
          : '先回頭看該題的答題骨架，把每個標題各補一句具體作為再重寫。');
      out.innerHTML = '自評得分：<span style="color:var(--main)">' + got + '</span> / ' + full + ' 分（' + pct + '%）　' + tip;
    }
    boxes.forEach(function (b) { b.addEventListener('change', calc); });
    calc();
  }

  document.addEventListener('DOMContentLoaded', function () {
    [].slice.call(document.querySelectorAll('.quiz')).forEach(initQuiz);
    [].slice.call(document.querySelectorAll('.selfscore')).forEach(initSelf);
  });
})();
