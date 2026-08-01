/* 資安自學院 前端邏輯 */
'use strict';

const API = {
  curriculum: () => fetch('/api/curriculum').then(r => r.json()),
  chapter: id => fetch('/api/chapter/' + id).then(r => r.json()),
  progress: () => fetch('/api/progress').then(r => r.json()),
  postProgress: body => fetch('/api/progress', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(body)}).then(r=>r.json()),
  quiz: (id, answers) => fetch('/api/quiz/' + id, {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({answers})}).then(r=>r.json()),
  terminal: cmd => fetch('/api/terminal', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({cmd})}).then(r=>r.json()),
  search: q => fetch('/api/search?q=' + encodeURIComponent(q)).then(r=>r.json()),
  glossary: () => fetch('/api/glossary').then(r=>r.json()),
};

const STATE = { curriculum:null, progress:null, chapterMap:{}, current:null };
const $ = s => document.querySelector(s);
const $$ = s => Array.from(document.querySelectorAll(s));
const esc = s => (s||'').replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));

/* ---- 輕量 markdown（粗體、行內碼、程式區塊、清單、段落）---- */
function mdInline(t){
  t = esc(t);
  t = t.replace(/`([^`]+)`/g, '<code>$1</code>');
  t = t.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
  return t;
}
function mdBlock(text){
  if(!text) return '';
  const parts = text.split(/```/);
  let html = '';
  parts.forEach((seg, i) => {
    if(i % 2 === 1){ // code block
      html += '<pre>' + esc(seg.replace(/^\n/,'').replace(/\n$/,'')) + '</pre>';
    } else {
      seg.split(/\n{2,}/).forEach(block => {
        block = block.trim(); if(!block) return;
        const lines = block.split('\n');
        if(lines.every(l => /^[-*] /.test(l.trim()))){
          html += '<ul>' + lines.map(l => '<li>' + mdInline(l.replace(/^[-*] /,'').trim()) + '</li>').join('') + '</ul>';
        } else if(lines.every(l => /^\d+\. /.test(l.trim()))){
          html += '<ol>' + lines.map(l => '<li>' + mdInline(l.replace(/^\d+\. /,'').trim()) + '</li>').join('') + '</ol>';
        } else {
          html += '<p>' + lines.map(mdInline).join('<br>') + '</p>';
        }
      });
    }
  });
  return html;
}

const trackColorVar = c => `var(--track-${c||'sky'})`;
const toast = msg => { const t=$('#toast'); t.textContent=msg; t.hidden=false; clearTimeout(t._t); t._t=setTimeout(()=>t.hidden=true, 2200); };

/* ================= 初始化 ================= */
async function init(){
  try {
    const [cur, prog] = await Promise.all([API.curriculum(), API.progress()]);
    STATE.curriculum = cur; STATE.progress = prog;
    cur.tracks.forEach(t => t.chapters.forEach(c => STATE.chapterMap[c.id] = {chapter:c, track:t}));
    renderSidebar(); renderHome();
    bindGlobal();
    handleHash();
  } catch(e){
    $('#trackNav').innerHTML = '<div class="nav-loading">載入失敗，請確認伺服器運作中並重新整理。</div>';
    console.error(e);
  }
}

/* ================= 側邊欄 ================= */
function renderSidebar(){
  const nav = $('#trackNav');
  const stages = {};
  STATE.curriculum.tracks.forEach(t => { (stages[t.stage] = stages[t.stage] || {name:t.stageName, tracks:[]}).tracks.push(t); });
  let html = '';
  Object.keys(stages).sort().forEach(s => {
    html += `<div class="nav-stage">${esc(stages[s].name)}</div>`;
    stages[s].tracks.forEach(t => {
      const pt = STATE.progress.perTrack[t.id] || {done:0, total:t.chapters.length};
      const activeTrack = STATE.current && STATE.chapterMap[STATE.current] && STATE.chapterMap[STATE.current].track.id === t.id;
      html += `<div class="nav-track${activeTrack?' open':''}" data-track="${t.id}">
        <div class="nav-track-head" data-toggle="${t.id}">
          <span class="tk-dot" style="background:${trackColorVar(t.color)}"></span>
          <span class="tk-name">${esc(t.title)}</span>
          <span class="tk-prog">${pt.done}/${pt.total}</span>
          <span class="tk-caret">▶</span>
        </div>
        <div class="nav-chapters">
          ${t.chapters.map(c => {
            const done = STATE.progress.read[c.id];
            return `<div class="nav-chapter${done?' done':''}${STATE.current===c.id?' active':''}" data-ch="${c.id}">
              <span class="ch-check">${done?'✓':''}</span>
              <span class="ch-title">${esc(c.title)}</span>
            </div>`;
          }).join('')}
        </div>
      </div>`;
    });
  });
  nav.innerHTML = html;
  nav.querySelectorAll('[data-toggle]').forEach(el => el.onclick = () => el.closest('.nav-track').classList.toggle('open'));
  nav.querySelectorAll('[data-ch]').forEach(el => el.onclick = () => { location.hash = '#/ch/' + el.dataset.ch; });
}

/* ================= 首頁 ================= */
function renderHome(){
  const cur = STATE.curriculum, prog = STATE.progress, st = prog.stats;
  $('#heroStats').innerHTML = [
    ['路線', cur.totals.tracks], ['章節', cur.totals.chapters], ['測驗題', cur.totals.quiz], ['模擬指令', '180+']
  ].map(([l,v]) => `<div class="st"><b>${v}</b><span>${l}</span></div>`).join('');

  $('#progressPanel').innerHTML = `
    <div class="pp-head"><strong>你的學習進度</strong>
      <span class="pp-streak">🔥 連續學習 ${prog.streakDays} 天</span></div>
    <div class="bigbar"><i style="width:${st.percent}%"></i></div>
    <div class="pp-metrics">
      <div>已完成章節 <b>${st.chaptersDone}/${st.chaptersTotal}</b></div>
      <div>測驗得分 <b>${st.quizScore}/${st.quizTotal}</b></div>
      <div>完成度 <b>${st.percent}%</b></div>
    </div>`;

  const firstUnread = () => {
    for(const t of cur.tracks) for(const c of t.chapters) if(!prog.read[c.id]) return c.id;
    return cur.tracks[0].chapters[0].id;
  };
  $('#startBtn').onclick = () => location.hash = '#/ch/' + cur.tracks[0].chapters[0].id;
  const cont = $('#continueBtn');
  if(st.chaptersDone > 0){ cont.hidden = false; cont.onclick = () => location.hash = '#/ch/' + firstUnread(); }

  const stages = {};
  cur.tracks.forEach(t => { (stages[t.stage]=stages[t.stage]||{name:t.stageName,tracks:[]}).tracks.push(t); });
  let html = '';
  Object.keys(stages).sort().forEach(s => {
    html += `<div class="rm-stage-label">${esc(stages[s].name)}</div>`;
    stages[s].tracks.forEach((t, i) => {
      const pt = prog.perTrack[t.id] || {done:0,total:t.chapters.length};
      const pct = pt.total ? Math.round(pt.done/pt.total*100) : 0;
      const num = cur.tracks.indexOf(t)+1;
      html += `<div class="track-card" style="--tk:${trackColorVar(t.color)}" data-track="${t.id}">
        <div class="tc-head"><span class="tc-num">${String(num).padStart(2,'0')}</span>
          <div><div class="tc-title">${esc(t.title)}</div><div class="tc-code">${esc(t.code)}</div></div></div>
        <div class="tc-tagline">${esc(t.tagline)}</div>
        <div class="tc-foot">
          <div class="tc-bar"><i style="width:${pct}%"></i></div>
          <span class="tc-meta">${pt.done}/${pt.total} 章 · ${t.chapters.length} 節</span>
        </div>
      </div>`;
    });
  });
  $('#roadmap').innerHTML = html;
  $$('.track-card').forEach(el => el.onclick = () => {
    const t = cur.tracks.find(x => x.id === el.dataset.track);
    location.hash = '#/ch/' + t.chapters[0].id;
  });
}

/* ================= 章節閱讀 ================= */
async function openChapter(id){
  const home = $('#homeView'), reader = $('#readerView');
  reader.innerHTML = '<div class="nav-loading">載入章節中…</div>';
  home.hidden = true; reader.hidden = false; window.scrollTo(0,0);
  STATE.current = id;
  let ch;
  try { ch = await API.chapter(id); } catch(e){ reader.innerHTML='<p>載入失敗。</p>'; return; }
  if(ch.error){ reader.innerHTML = '<p>' + esc(ch.error) + '</p>'; return; }
  STATE.currentData = ch;
  renderChapter(ch);
  renderSidebar();
  document.body.classList.remove('nav-open');
}

function renderChapter(ch){
  const tkVar = trackColorVar(ch.track.color);
  const done = !!STATE.progress.read[ch.id];
  const booked = STATE.progress.bookmarks.includes(ch.id);
  let h = `<div class="reader" style="--tk:${tkVar}">`;
  h += `<div class="reader-top">
    <div class="crumb"><b>${esc(ch.track.title)}</b> / ${esc(ch.level)}</div>
    <div class="reader-actions">
      <button class="chip-btn${booked?' on':''}" id="bookmarkBtn">${booked?'★ 已收藏':'☆ 收藏'}</button>
    </div></div>`;
  h += `<h1>${esc(ch.title)}</h1>`;
  if(ch.subtitle) h += `<div class="subtitle">${esc(ch.subtitle)}</div>`;
  h += `<div class="meta-row"><span class="level">● ${esc(ch.level)}</span>
    <span>⏱ 約 ${ch.minutes} 分鐘</span>
    <span>📝 ${ch.quiz.length} 題測驗</span>
    <span>⌨ ${(ch.labs||[]).reduce((a,l)=>a+l.steps.length,0)} 條指令</span></div>`;

  if(ch.why) h += `<div class="why-box"><div class="why-label">為什麼要學這個</div><div class="body">${mdBlock(ch.why)}</div></div>`;

  (ch.sections||[]).forEach(s => {
    h += `<div class="section"><h2>${esc(s.heading)}</h2><div class="body">${mdBlock(s.body)}</div>`;
    if(s.example) h += `<div class="callout example"><span class="c-label">💡 舉例說明</span><div class="body">${mdBlock(s.example)}</div></div>`;
    if(s.note) h += `<div class="callout note"><span class="c-label">⚑ 重點提醒 / 考點</span><div class="body">${mdBlock(s.note)}</div></div>`;
    h += `</div>`;
  });

  if(ch.diagram) h += `<div class="diagram-box">${ch.diagram}</div>`;

  if(ch.table){
    h += `<div class="table-wrap"><table class="data-table"><caption>${esc(ch.table.caption||'')}</caption><thead><tr>`;
    h += ch.table.head.map(x=>`<th>${esc(x)}</th>`).join('') + '</tr></thead><tbody>';
    ch.table.rows.forEach(r => { h += '<tr>' + r.map(x=>`<td>${mdInline(x)}</td>`).join('') + '</tr>'; });
    h += '</tbody></table></div>';
  }

  (ch.labs||[]).forEach((lab, li) => {
    h += `<div class="lab"><div class="lab-head"><span class="lab-tag">⌨ 動手做</span>
      <h3>${esc(lab.title)}</h3><div class="lab-goal">${esc(lab.goal)}</div></div>`;
    if(lab.warn) h += `<div class="lab-warn">⚠ ${mdInline(lab.warn)}</div>`;
    h += `<div class="lab-steps">`;
    lab.steps.forEach((st, si) => {
      h += `<div class="lab-step">
        <div class="lab-cmd"><span class="prompt">$</span><span class="cmd-text">${esc(st.cmd)}</span>
          <button class="run-cmd" data-cmd="${esc(st.cmd)}">▶ 在終端機試</button></div>
        <div class="lab-explain">${mdInline(st.explain)}</div>
        <div class="lab-output">${st.output ? formatOutput(st.output) : ''}</div>
      </div>`;
    });
    h += `</div></div>`;
  });

  // 測驗
  if(ch.quiz && ch.quiz.length){
    h += `<div class="quiz-wrap" id="quizWrap"><h2>📝 章節測驗</h2>
      <div class="quiz-sub">共 ${ch.quiz.length} 題。作答後點「批改」看解析。這些題目模擬真實證照考試的題型。</div>`;
    ch.quiz.forEach((q, qi) => {
      h += `<div class="qz-item" data-q="${qi}"><div class="qz-q"><span class="qn">Q${qi+1}.</span>${esc(q.q)}</div><div class="qz-opts">`;
      q.options.forEach((op, oi) => {
        h += `<div class="qz-opt" data-q="${qi}" data-o="${oi}"><span class="opt-key">${'ABCD'[oi]}</span><span>${esc(op)}</span></div>`;
      });
      h += `</div><div class="qz-why" id="why-${qi}"></div></div>`;
    });
    h += `<div class="quiz-actions"><button class="primary-btn" id="gradeBtn">批改測驗</button>
      <button class="chip-btn" id="resetQuizBtn">重作</button>
      <span class="quiz-score" id="quizScore"></span></div></div>`;
  }

  if(ch.takeaway && ch.takeaway.length){
    h += `<div class="takeaway"><div class="tk-label">🎯 帶走這三句</div><ul>${ch.takeaway.map(t=>`<li>${mdInline(t)}</li>`).join('')}</ul></div>`;
  }

  h += `<button class="mark-done-btn${done?' done':''}" id="markDoneBtn">${done?'✓ 已完成本章（點此取消）':'標記本章為已完成'}</button>`;

  // 上下章
  h += `<div class="reader-nav">`;
  h += ch.prev ? `<button data-go="${ch.prev}"><span class="rn-dir">← 上一章</span><span class="rn-title">${esc(STATE.chapterMap[ch.prev]?STATE.chapterMap[ch.prev].chapter.title:'')}</span></button>` : `<button disabled><span class="rn-dir">← 上一章</span><span class="rn-title">已是第一章</span></button>`;
  h += ch.next ? `<button class="next" data-go="${ch.next}"><span class="rn-dir">下一章 →</span><span class="rn-title">${esc(STATE.chapterMap[ch.next]?STATE.chapterMap[ch.next].chapter.title:'')}</span></button>` : `<button class="next" disabled><span class="rn-dir">下一章 →</span><span class="rn-title">已是最後一章</span></button>`;
  h += `</div></div>`;

  $('#readerView').innerHTML = h;
  bindChapter(ch);
}

function formatOutput(out){
  return esc(out).split('\n').map(line =>
    /^\s*#/.test(line) ? `<span class="cmt">${line}</span>` : line
  ).join('\n');
}

function bindChapter(ch){
  $$('.run-cmd').forEach(b => b.onclick = () => { openTerminal(); runInTerminal(b.dataset.cmd); });
  const md = $('#markDoneBtn');
  if(md) md.onclick = async () => {
    const isDone = md.classList.contains('done');
    await API.postProgress({action: isDone?'unread':'read', chapterId: ch.id});
    STATE.progress = await API.progress();
    md.classList.toggle('done'); md.textContent = isDone ? '標記本章為已完成' : '✓ 已完成本章（點此取消）';
    renderSidebar();
    toast(isDone ? '已取消完成標記' : '🎉 已完成本章！');
  };
  const bm = $('#bookmarkBtn');
  if(bm) bm.onclick = async () => {
    await API.postProgress({action:'bookmark', chapterId: ch.id});
    STATE.progress = await API.progress();
    const on = STATE.progress.bookmarks.includes(ch.id);
    bm.classList.toggle('on', on); bm.textContent = on ? '★ 已收藏' : '☆ 收藏';
  };
  $$('.reader-nav [data-go]').forEach(b => b.onclick = () => location.hash = '#/ch/' + b.dataset.go);

  // 測驗互動
  const answers = {};
  $$('.qz-opt').forEach(op => op.onclick = () => {
    if($('#quizWrap').classList.contains('graded')) return;
    const q = op.dataset.q;
    $$(`.qz-opt[data-q="${q}"]`).forEach(x => x.classList.remove('sel'));
    op.classList.add('sel'); answers[q] = parseInt(op.dataset.o);
  });
  const grade = $('#gradeBtn');
  if(grade) grade.onclick = async () => {
    if(Object.keys(answers).length < ch.quiz.length){ toast('還有題目沒作答'); }
    const res = await API.quiz(ch.id, answers);
    $('#quizWrap').classList.add('graded');
    res.results.forEach(r => {
      const picked = answers[r.id];
      if(picked !== undefined) $$(`.qz-opt[data-q="${r.id}"][data-o="${picked}"]`).forEach(x=>x.classList.add(r.correct?'correct':'wrong'));
      $$(`.qz-opt[data-q="${r.id}"][data-o="${r.answer}"]`).forEach(x=>x.classList.add('correct'));
      const why = $('#why-'+r.id);
      why.className = 'qz-why show ' + (r.correct?'ok':'no');
      why.innerHTML = `<strong>${r.correct?'✓ 答對':'✗ 正解是 '+'ABCD'[r.answer]}</strong> — ${mdInline(r.why)}`;
    });
    $('#quizScore').innerHTML = `得分 ${res.score}/${res.total}` + (res.best>res.score?` （最佳 ${res.best}）`:'');
    STATE.progress = await API.progress();
    if(res.score === res.total) toast('💯 滿分！太厲害了');
  };
  const rq = $('#resetQuizBtn');
  if(rq) rq.onclick = () => renderChapter(ch);
}

/* ================= 模擬終端機 ================= */
function openTerminal(){
  const m = $('#terminalModal'); m.hidden = false;
  if(!$('#termBody').dataset.init){
    $('#termBody').dataset.init = '1';
    API.terminal('help').then(r => appendTerm('', r.output));
  }
  setTimeout(()=>$('#termInput').focus(), 50);
}
function appendTerm(cmd, out){
  const body = $('#termBody');
  if(cmd) body.innerHTML += `<div><span class="t-prompt">student@academy:~$</span> <span class="t-cmd">${esc(cmd)}</span></div>`;
  if(out) body.innerHTML += `<div class="t-out">${formatOutput(out)}</div>`;
  body.scrollTop = body.scrollHeight;
}
async function runInTerminal(cmd){
  appendTerm(cmd, '');
  const r = await API.terminal(cmd);
  if(r.clear){ $('#termBody').innerHTML=''; return; }
  appendTerm('', r.output);
}

/* ================= 全域綁定 ================= */
function bindGlobal(){
  $('#menuToggle').onclick = () => document.body.classList.toggle('nav-open');
  $('#terminalBtn').onclick = openTerminal;
  $('#termInput').addEventListener('keydown', e => {
    if(e.key==='Enter'){ const v=e.target.value.trim(); if(v){ runInTerminal(v); e.target.value=''; } }
  });
  $$('.modal [data-close]').forEach(b => b.onclick = () => b.closest('.modal').hidden = true);
  $$('.modal').forEach(m => m.addEventListener('click', e => { if(e.target===m) m.hidden=true; }));
  document.addEventListener('keydown', e => { if(e.key==='Escape') $$('.modal').forEach(m=>m.hidden=true); });

  // 搜尋
  let timer;
  $('#searchInput').addEventListener('input', e => {
    clearTimeout(timer); const q = e.target.value.trim();
    const box = $('#searchResults');
    if(!q){ box.hidden = true; return; }
    timer = setTimeout(async () => {
      const r = await API.search(q); box.hidden = false;
      if(!r.results.length){ box.innerHTML = '<div class="sr-empty">找不到相關章節</div>'; return; }
      box.innerHTML = r.results.map(x => `<a href="#/ch/${x.id}"><span class="sr-track" style="color:${trackColorVar(x.color)}">${esc(x.track)}</span><div class="sr-title">${esc(x.title)}</div></a>`).join('');
      box.querySelectorAll('a').forEach(a => a.onclick = () => { box.hidden=true; $('#searchInput').value=''; });
    }, 180);
  });
  document.addEventListener('click', e => { if(!e.target.closest('.search-box')) $('#searchResults').hidden = true; });

  // 術語辭典
  $('#glossaryBtn').onclick = async () => {
    $('#glossaryModal').hidden = false;
    if(!$('#glossaryList').dataset.init){
      const r = await API.glossary();
      $('#glossaryList').dataset.init = '1'; $('#glossaryList').dataset.all = JSON.stringify(r.items);
      renderGlossary(r.items);
    }
  };
  $('#glossarySearch').addEventListener('input', e => {
    const all = JSON.parse($('#glossaryList').dataset.all || '[]');
    const q = e.target.value.toLowerCase();
    renderGlossary(all.filter(x => x.term.toLowerCase().includes(q) || x.desc.toLowerCase().includes(q)));
  });

  // 重設
  $('#resetBtn').onclick = async () => {
    if(!confirm('確定要清除所有學習進度、測驗成績與收藏嗎？此動作無法復原。')) return;
    await API.postProgress({action:'reset'});
    STATE.progress = await API.progress();
    renderSidebar();
    if($('#homeView').hidden === false) renderHome();
    else if(STATE.currentData) renderChapter(STATE.currentData);
    toast('已重設所有進度');
  };

  window.addEventListener('hashchange', handleHash);
}
function renderGlossary(items){
  $('#glossaryList').innerHTML = items.map(x =>
    `<div class="gl-item"><div class="gl-term">${esc(x.term)}</div><div class="gl-desc">${esc(x.desc)}</div></div>`
  ).join('') || '<div class="sr-empty" style="padding:14px">找不到術語</div>';
}

function handleHash(){
  const m = location.hash.match(/^#\/ch\/(.+)$/);
  if(m){ openChapter(m[1]); }
  else { $('#homeView').hidden=false; $('#readerView').hidden=true; STATE.current=null; renderHome(); renderSidebar(); }
}

init();
