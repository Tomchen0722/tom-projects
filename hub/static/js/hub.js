/* ══════════════════════════════════════════════════════════════
   Tom Chen — Project Hub 前端
   負責：卡片狀態同步、啟動／停止流程、缺套件時的安裝確認、篩選。
   ══════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  const cards = Array.from(document.querySelectorAll('.card'));
  const toasts = document.getElementById('toasts');
  const runningCountEl = document.getElementById('runningCount');
  const chipRunningEl = document.getElementById('chipRunning');
  const stopAllBtn = document.getElementById('stopAll');

  // 正在啟動中的專案：輪詢時不要覆蓋它們的過渡狀態
  const busy = new Set();

  const STATE_TEXT = {
    stopped:  '未啟動',
    starting: '啟動中',
    running:  '執行中',
    error:    '啟動失敗',
  };

  // ── 小工具 ────────────────────────────────────────────────
  function toast(message, type) {
    const el = document.createElement('div');
    el.className = 'toast' + (type ? ' ' + type : '');
    el.textContent = message;
    toasts.appendChild(el);
    // 3.5 秒自動消失，不搶焦點
    setTimeout(() => {
      el.style.transition = 'opacity .25s, transform .25s';
      el.style.opacity = '0';
      el.style.transform = 'translateY(8px)';
      setTimeout(() => el.remove(), 260);
    }, 3500);
  }

  function setState(card, state, managed) {
    // managed 未傳入時沿用卡片上既有的判定，避免流程中途被覆蓋
    if (managed === undefined) managed = card.dataset.managed !== 'false';

    const status = card.querySelector('.status');
    const external = state === 'running' && !managed;

    status.dataset.state = state;
    status.querySelector('.status-text').textContent =
      external ? '外部執行中' : (STATE_TEXT[state] || state);
    card.classList.toggle('is-running', state === 'running');
    card.classList.toggle('is-external', external);
    card.dataset.managed = managed ? 'true' : 'false';

    const startBtn = card.querySelector('[data-act="start"]');
    const stopBtn = card.querySelector('[data-act="stop"]');
    const kind = card.dataset.kind;

    if (state === 'running') {
      startBtn.querySelector('.label').textContent = kind === 'desktop' ? '已開啟' : '開啟畫面';
      startBtn.disabled = kind === 'desktop';
      // 外部服務也讓使用者關得掉，只是點下去會先確認一次
      stopBtn.hidden = false;
      stopBtn.textContent = '';
      stopBtn.insertAdjacentHTML('beforeend',
        '<svg width="13" height="13" aria-hidden="true"><use href="#i-stop"></use></svg>'
        + (external ? '強制停止' : '停止'));
    } else {
      startBtn.querySelector('.label').textContent = '啟動';
      startBtn.disabled = false;
      stopBtn.hidden = true;
    }
  }

  function setBusy(card, on, text) {
    const btn = card.querySelector('[data-act="start"]');
    const label = btn.querySelector('.label');
    const icon = btn.querySelector('svg');

    btn.disabled = on;
    if (on) {
      busy.add(card.dataset.id);
      icon.style.display = 'none';
      if (!btn.querySelector('.spinner')) {
        const sp = document.createElement('span');
        sp.className = 'spinner';
        btn.insertBefore(sp, label);
      }
      label.textContent = text || '啟動中…';
    } else {
      busy.delete(card.dataset.id);
      icon.style.display = '';
      const sp = btn.querySelector('.spinner');
      if (sp) sp.remove();
    }
  }

  function hint(card, message, isError, log) {
    const el = card.querySelector('.card-hint');
    if (!message) {
      el.hidden = true;
      el.innerHTML = '';
      return;
    }
    el.hidden = false;
    el.className = 'card-hint' + (isError ? ' err' : '');
    el.innerHTML = '';

    const p = document.createElement('div');
    p.textContent = message;
    el.appendChild(p);

    if (log) {
      const pre = document.createElement('pre');
      pre.textContent = log;
      el.appendChild(pre);
    }
  }

  async function api(path, options) {
    const res = await fetch(path, Object.assign({ method: 'GET' }, options));
    if (!res.ok && res.status >= 500) throw new Error('伺服器錯誤 ' + res.status);
    return res.json();
  }

  // ── 確認對話框 ────────────────────────────────────────────
  function confirmDialog({ title, body, confirmText, danger }) {
    return new Promise((resolve) => {
      const scrim = document.createElement('div');
      scrim.className = 'modal-scrim';
      scrim.innerHTML = `
        <div class="modal" role="dialog" aria-modal="true" aria-labelledby="mdT">
          <p class="eyebrow">CONFIRM</p>
          <h3 id="mdT"></h3>
          <div class="modal-body"></div>
          <div class="modal-actions">
            <button class="btn btn-ghost" data-x="cancel">取消</button>
            <button class="btn btn-primary" data-x="ok"></button>
          </div>
        </div>`;
      scrim.querySelector('#mdT').textContent = title;
      scrim.querySelector('.modal-body').innerHTML = body;
      scrim.querySelector('[data-x="ok"]').textContent = confirmText || '確認';
      if (danger) scrim.querySelector('[data-x="ok"]').classList.add('btn-danger');

      function close(result) {
        document.removeEventListener('keydown', onKey);
        scrim.remove();
        resolve(result);
      }
      function onKey(e) {
        if (e.key === 'Escape') close(false);   // 一定要有離開的方法
      }

      scrim.addEventListener('click', (e) => {
        if (e.target === scrim) close(false);
        if (e.target.closest('[data-x="cancel"]')) close(false);
        if (e.target.closest('[data-x="ok"]')) close(true);
      });
      document.addEventListener('keydown', onKey);

      document.body.appendChild(scrim);
      scrim.querySelector('[data-x="ok"]').focus();
    });
  }

  // ── 啟動流程 ──────────────────────────────────────────────
  async function start(card) {
    const id = card.dataset.id;
    const name = card.querySelector('h4').textContent;
    const kind = card.dataset.kind;

    // 已在執行 → 直接開啟畫面
    const status = card.querySelector('.status');
    if (status.dataset.state === 'running') {
      const url = card.dataset.url;
      if (url) window.open(url, '_blank', 'noopener');
      return;
    }

    hint(card, '');

    // 先確認環境，缺套件就問過再裝
    let check;
    try {
      check = await api('/api/check/' + id);
    } catch (err) {
      toast('無法檢查執行環境：' + err.message, 'err');
      return;
    }

    if (check.missing && check.missing.length) {
      const heavy = check.heavy;
      const ok = await confirmDialog({
        title: '需要先安裝套件',
        body: `<p><strong>${name}</strong> 缺少下列套件：</p>
               <p style="font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--blue)">
                 ${check.missing.join('、')}
               </p>
               <p>${heavy
                  ? '這個專案的依賴較大（約 2.5&nbsp;GB，含 PyTorch），視網速可能需要 10–30 分鐘。'
                  : '安裝過程約需數十秒到數分鐘。'}</p>
               <p>要現在安裝嗎？</p>`,
        confirmText: '開始安裝',
      });
      if (!ok) return;

      setBusy(card, true, '安裝中…');
      setState(card, 'starting');
      hint(card, '正在安裝套件，這段時間可以先做別的事，完成後會自動啟動。');

      try {
        const res = await api('/api/install/' + id, { method: 'POST' });
        if (!res.ok) {
          setBusy(card, false);
          setState(card, 'error');
          hint(card, '套件安裝失敗，可依下方訊息排除後再試一次。', true, res.log);
          toast(name + ' 安裝失敗', 'err');
          return;
        }
        toast(name + ' 套件安裝完成', 'ok');
      } catch (err) {
        setBusy(card, false);
        setState(card, 'error');
        hint(card, '安裝過程發生錯誤：' + err.message, true);
        return;
      }
    }

    // 正式啟動
    setBusy(card, true, '啟動中…');
    setState(card, 'starting');
    hint(card, kind === 'desktop'
      ? '正在開啟桌面視窗，請稍候。'
      : '正在啟動服務，第一次啟動可能需要十幾秒。');

    let res;
    try {
      res = await api('/api/start/' + id, { method: 'POST' });
    } catch (err) {
      setBusy(card, false);
      setState(card, 'error');
      hint(card, '啟動失敗：' + err.message, true);
      return;
    }

    setBusy(card, false);

    if (!res.ok) {
      setState(card, 'error');
      hint(card, res.message || '啟動失敗', true, res.log);
      toast(name + ' 啟動失敗', 'err');
      return;
    }

    setState(card, 'running');

    if (res.url) {
      card.dataset.url = res.url;
      hint(card, '服務已就緒：' + res.url);
      window.open(res.url, '_blank', 'noopener');
      toast(name + ' 已啟動，已為你開啟新分頁', 'ok');
    } else {
      // 顯示後端的實際回報：重量級專案會說明視窗還要多久才出現
      hint(card, res.message || '桌面程式已啟動。');
      if (res.waiting_window) {
        card.dataset.waitingWindow = '1';
        setState(card, 'starting');
        toast(name + ' 啟動中，視窗準備好會自動跳出來');
      } else {
        toast(name + ' 桌面視窗已開啟', 'ok');
      }
    }
    refresh();
  }

  async function stop(card) {
    const id = card.dataset.id;
    const name = card.querySelector('h4').textContent;
    const btn = card.querySelector('[data-act="stop"]');
    const external = card.classList.contains('is-external');

    // 不是 Hub 啟動的服務，可能是使用者自己開的，關掉前先問一聲
    if (external) {
      const ok = await confirmDialog({
        title: '強制停止外部服務',
        body: `<p><strong>${name}</strong> 目前的服務不是由 Hub 啟動的，`
            + '可能是你自己在別的視窗開的，或是上次 Hub 沒有正常關閉留下來的。</p>'
            + '<p>要強制結束這個程序嗎？未存檔的內容可能會遺失。</p>',
        confirmText: '強制停止',
        danger: true,
      });
      if (!ok) return;
    }

    btn.disabled = true;

    try {
      await api('/api/stop/' + id, { method: 'POST' });
      setState(card, 'stopped');
      hint(card, '');
      delete card.dataset.url;
      toast(name + ' 已停止');
    } catch (err) {
      toast('停止失敗：' + err.message, 'err');
    } finally {
      btn.disabled = false;
      refresh();
    }
  }

  // ── 狀態輪詢 ──────────────────────────────────────────────
  async function refresh() {
    let data;
    try {
      data = await api('/api/apps');
    } catch (err) {
      return;   // 輪詢失敗就安靜略過，下一輪再試
    }

    let running = 0;
    data.apps.forEach((item) => {
      const card = cards.find((c) => c.dataset.id === item.id);
      if (!card) return;
      if (item.state === 'running') running += 1;
      if (busy.has(item.id)) return;   // 啟動中的卡片交由流程自己控制

      if (item.url) card.dataset.url = item.url;
      const current = card.querySelector('.status').dataset.state;
      if (current === 'error' && item.state === 'stopped') return;  // 保留失敗訊息

      // 桌面程式：視窗還沒出現前維持「啟動中」，不要謊稱已經開好了
      if (item.state === 'running' && card.dataset.kind === 'desktop'
          && item.window_checked === false) {
        setState(card, 'starting', item.managed);
        const secs = item.uptime || 0;
        hint(card, item.heavy
          ? `正在載入語音模型並開啟視窗，已經過 ${secs} 秒（通常需要 40～60 秒）。`
          : `正在開啟視窗，已經過 ${secs} 秒。`);
        return;
      }

      setState(card, item.state, item.managed);

      // 視窗檢查完成後，把結果如實反映在卡片上
      if (item.state === 'running' && card.dataset.kind === 'desktop'
          && item.window_checked === true && card.dataset.waitingWindow === '1') {
        delete card.dataset.waitingWindow;
        if (item.window_ready) {
          hint(card, '視窗「' + (item.window_title || '已開啟') + '」已開啟並移到最前面。');
        } else {
          hint(card, '程式在執行中，但沒有偵測到視窗。'
            + '請看看工作列，有些程式會常駐在系統匣；'
            + '若確實沒開起來，按「停止」後再試一次。');
        }
      }

      // 外部程序佔用同一個 port 時說明清楚，否則使用者會以為開到的是這裡的版本
      if (item.state === 'running' && !item.managed) {
        hint(card, '這個 port 上已經有服務在執行，但不是由 Hub 啟動的。'
          + '點「開啟畫面」會連到既有的服務；要改用這裡的版本，請先關閉外部那一個。');
      }
    });

    runningCountEl.textContent = running;
    chipRunningEl.textContent = running;
    stopAllBtn.disabled = running === 0;
    applyFilter();
  }

  // ── 篩選 ──────────────────────────────────────────────────
  let currentFilter = 'all';

  function applyFilter() {
    cards.forEach((card) => {
      const state = card.querySelector('.status').dataset.state;
      let show = true;
      if (currentFilter.startsWith('cat:')) {
        show = card.dataset.cat === currentFilter.slice(4);
      } else if (currentFilter === 'running') {
        show = state === 'running' || state === 'starting';
      }
      card.style.display = show ? '' : 'none';
    });

    // 整個子分類都被篩掉時，連同標題一起隱藏，避免留下空標題
    document.querySelectorAll('.subsection').forEach((sub) => {
      const visible = Array.from(sub.querySelectorAll('.card'))
        .some((c) => c.style.display !== 'none');
      sub.style.display = visible ? '' : 'none';
    });
    document.querySelectorAll('.section').forEach((sec) => {
      const visible = Array.from(sec.querySelectorAll('.card'))
        .some((c) => c.style.display !== 'none');
      sec.style.display = visible ? '' : 'none';
    });
  }

  document.querySelectorAll('.chip').forEach((chip) => {
    chip.addEventListener('click', () => {
      document.querySelectorAll('.chip').forEach((c) => c.setAttribute('aria-pressed', 'false'));
      chip.setAttribute('aria-pressed', 'true');
      currentFilter = chip.dataset.filter;
      applyFilter();
    });
  });

  // ── 事件綁定 ──────────────────────────────────────────────
  cards.forEach((card) => {
    card.querySelector('[data-act="start"]').addEventListener('click', () => start(card));
    card.querySelector('[data-act="stop"]').addEventListener('click', () => stop(card));
  });

  stopAllBtn.addEventListener('click', async () => {
    const ok = await confirmDialog({
      title: '停止所有專案',
      body: '<p>將關閉目前所有執行中的專案服務與桌面視窗。未存檔的內容可能會遺失。</p>',
      confirmText: '全部停止',
      danger: true,
    });
    if (!ok) return;

    stopAllBtn.disabled = true;
    try {
      await api('/api/stop-all', { method: 'POST' });
      cards.forEach((c) => { setState(c, 'stopped'); hint(c, ''); });
      toast('已停止所有專案');
    } catch (err) {
      toast('停止失敗：' + err.message, 'err');
    }
    refresh();
  });

  // ── 進場動畫收尾 ──────────────────────────────────────────
  // fade-in 用 animation-fill-mode: forwards，播完會把 transform 鎖在 0，
  // 蓋掉卡片 hover 的上浮效果，所以動畫結束後必須把 class 拿掉。
  function clearFadeIn(card) {
    if (!card.classList.contains('fade-in')) return;
    card.classList.remove('fade-in');
    for (var i = 1; i <= 6; i += 1) card.classList.remove('fade-in-' + i);
  }

  cards.forEach(function (card) {
    card.addEventListener('animationend', function (e) {
      if (e.animationName === 'fadeInUp') clearFadeIn(card);
    });
  });

  // 保底：animationend 不是每種情況都會送達（分頁在背景時瀏覽器不合成畫面、
  // 動畫被程式提前結束等），時間到就直接清掉，避免 hover 永久失效。
  // 最長延遲 .35s + 動畫 .6s，抓 1.5s 綽綽有餘。
  setTimeout(function () { cards.forEach(clearFadeIn); }, 1500);

  // ── 啟動 ──────────────────────────────────────────────────
  refresh();
  setInterval(refresh, 4000);
})();
