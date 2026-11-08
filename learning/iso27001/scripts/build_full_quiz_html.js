const fs = require('fs');
const path = require('path');

const questions = JSON.parse(fs.readFileSync(path.join(__dirname, 'all_questions.json'), 'utf8'));
console.log('Total questions to inject:', questions.length);

const htmlTemplate = `<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ISO 27001 互動模擬試題（五大考證題型全真題庫）</title>
<style>
  :root {
    --blue: #1e40af;
    --sky: #0ea5e9;
    --dark: #0f172a;
    --bg: #f0f4ff;
    --good: #16a34a;
    --bad: #dc2626;
    --muted: #64748b;
    --border: #e2e8f0;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: "Segoe UI", "Microsoft JhengHei", sans-serif; }
  body { background: var(--bg); min-height: 100vh; color: #1e293b; }
  .topbar { background: var(--blue); color: #fff; padding: 12px 20px; display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }
  .topbar a { color: rgba(255,255,255,.85); text-decoration: none; font-size: .85rem; }
  .topbar .sep { opacity: .4; }
  .hero { background: linear-gradient(135deg, #0f172a, #1e3a8a); color: #fff; padding: 40px 24px 32px; text-align: center; }
  .hero h1 { font-size: 1.8rem; margin-bottom: 8px; }
  .hero h1 span { color: #60a5fa; }
  .hero p { opacity: .88; max-width: 680px; margin: 0 auto; line-height: 1.8; font-size: .92rem; }
  .wrap { max-width: 820px; margin: 0 auto; padding: 28px 16px 60px; }
  .card { background: #fff; border-radius: 16px; padding: 26px; box-shadow: 0 3px 14px rgba(0,0,0,.08); margin-bottom: 16px; }
  .card h2 { font-size: 1.18rem; color: var(--blue); }
  .card h3 { font-size: 1rem; color: #1e293b; }
  .stat { font-size: .85rem; color: var(--muted); line-height: 1.7; }
  
  /* Setup Mode Options */
  .setup-section-title { font-size: .95rem; font-weight: 700; color: #475569; margin: 16px 0 8px; display: flex; align-items: center; gap: 6px; }
  .setup-opt { border: 2px solid var(--border); border-radius: 12px; padding: 15px 18px; margin-bottom: 10px; cursor: pointer; transition: .15s; background: #fff; }
  .setup-opt:hover { border-color: var(--sky); background: #f0f9ff; transform: translateX(3px); }
  .setup-opt h3 { font-size: .98rem; color: #1e293b; margin-bottom: 4px; display: flex; align-items: center; gap: 6px; }
  .setup-opt p { font-size: .82rem; color: var(--muted); line-height: 1.6; }
  
  /* Progress Bar */
  .progress-wrap { background: #dbeafe; border-radius: 8px; height: 8px; overflow: hidden; margin-bottom: 10px; }
  .progress-bar { height: 100%; background: linear-gradient(90deg, var(--blue), var(--sky)); transition: width .3s; }
  
  /* Tags & Headers */
  .tag-row { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin-bottom: 12px; }
  .domain-tag { display: inline-block; background: #dbeafe; color: var(--blue); padding: 4px 12px; border-radius: 12px; font-size: .75rem; font-weight: 700; }
  .qtype-tag { display: inline-flex; align-items: center; gap: 4px; padding: 4px 12px; border-radius: 12px; font-size: .75rem; font-weight: 700; }
  .qtype-single { background: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe; }
  .qtype-multi  { background: #fdf4ff; color: #9333ea; border: 1px solid #f0abfc; }
  .qtype-fill   { background: #f0fdf4; color: #15803d; border: 1px solid #bbf7d0; }
  .qtype-match  { background: #fffbeb; color: #b45309; border: 1px solid #fde68a; }
  .qtype-sort   { background: #f0f9ff; color: #0284c7; border: 1px solid #bae6fd; }
  
  .q-text { font-size: 1.05rem; color: #1e293b; line-height: 1.85; margin-bottom: 16px; font-weight: 600; }
  
  /* Type Hint */
  .type-hint { display: flex; align-items: center; gap: 8px; background: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid var(--blue); border-radius: 8px; padding: 10px 14px; font-size: .85rem; color: #334155; margin-bottom: 16px; line-height: 1.6; }
  .type-hint.multi-hint { border-left-color: #9333ea; background: #fdf4ff; color: #7e22ce; }
  .type-hint.fill-hint  { border-left-color: #16a34a; background: #f0fdf4; color: #166534; }
  .type-hint.match-hint { border-left-color: #d97706; background: #fffbeb; color: #92400e; }
  .type-hint.sort-hint  { border-left-color: #0284c7; background: #f0f9ff; color: #075985; }
  
  /* Choice Options (Single & Multi) */
  .opt { display: flex; align-items: center; width: 100%; text-align: left; background: #f8fafc; border: 2px solid var(--border); border-radius: 10px; padding: 13px 16px; margin-bottom: 9px; font-size: .92rem; color: #334155; cursor: pointer; transition: .15s; line-height: 1.6; user-select: none; }
  .opt:hover:not(:disabled) { border-color: var(--sky); background: #f0f9ff; }
  .opt.selected { border-color: var(--blue); background: #dbeafe; font-weight: 600; color: #1e3a8a; }
  .opt.correct { border-color: var(--good); background: #f0fdf4; color: #15803d; font-weight: 600; }
  .opt.wrong { border-color: var(--bad); background: #fef2f2; color: #b91c1c; }
  .opt:disabled { cursor: default; }
  .opt-letter { font-weight: 700; min-width: 26px; }
  .opt-txt { flex: 1; }
  .check-box { display: inline-flex; align-items: center; justify-content: center; width: 22px; height: 22px; border: 2px solid #94a3b8; border-radius: 6px; margin-right: 12px; font-size: .8rem; font-weight: 700; background: #fff; transition: .15s; flex-shrink: 0; }
  .opt.selected .check-box { background: #9333ea; border-color: #9333ea; color: #fff; }
  .opt.correct .check-box { background: var(--good); border-color: var(--good); color: #fff; }
  .opt.wrong .check-box { background: var(--bad); border-color: var(--bad); color: #fff; }
  
  /* Fill in the Blank (填寫空白) */
  .fill-sentence { font-size: 1.05rem; line-height: 2.6; color: #1e293b; background: #f8fafc; padding: 22px 20px; border-radius: 12px; border: 1px solid #e2e8f0; margin-bottom: 20px; }
  .drop-slot { display: inline-flex; align-items: center; justify-content: center; min-width: 130px; min-height: 38px; padding: 4px 14px; margin: 0 4px; border: 2px dashed #93c5fd; border-radius: 8px; background: #ffffff; color: #1d4ed8; font-weight: 600; font-size: .95rem; vertical-align: middle; cursor: pointer; transition: all .2s ease; user-select: none; box-shadow: 0 1px 2px rgba(0,0,0,.04); }
  .drop-slot.empty-slot { color: #94a3b8; font-size: .85rem; font-style: italic; background: #f1f5f9; }
  .drop-slot.drag-over { border-color: #2563eb; background: #dbeafe; transform: scale(1.04); box-shadow: 0 0 10px rgba(37,99,235,.25); }
  .drop-slot.filled { border-style: solid; border-color: #3b82f6; background: #eff6ff; color: #1e40af; }
  .drop-slot .slot-remove { margin-left: 8px; color: #94a3b8; font-size: 1.05rem; font-weight: 700; border-radius: 50%; padding: 0 4px; transition: .15s; }
  .drop-slot .slot-remove:hover { color: #dc2626; background: rgba(220,38,38,.12); }
  .drop-slot.correct { border-color: var(--good); background: #f0fdf4; color: #15803d; }
  .drop-slot.wrong { border-color: var(--bad); background: #fef2f2; color: #b91c1c; }
  .expected-tag { display: inline-block; font-size: .78rem; background: #dcfce7; color: #15803d; padding: 2px 8px; border-radius: 6px; margin-left: 6px; font-weight: 600; }
  
  .word-bank-wrap { margin-top: 16px; }
  .word-bank-title { font-size: .88rem; font-weight: 700; color: #475569; margin-bottom: 10px; display: flex; align-items: center; gap: 6px; }
  .word-bank { display: flex; flex-wrap: wrap; gap: 10px; background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 16px; min-height: 60px; }
  .word-chip { display: inline-flex; align-items: center; background: #f8fafc; color: #1e293b; border: 2px solid #cbd5e1; border-radius: 20px; padding: 8px 18px; font-size: .92rem; font-weight: 600; cursor: grab; user-select: none; transition: all .15s ease; box-shadow: 0 1px 3px rgba(0,0,0,.06); }
  .word-chip:hover:not(.used) { border-color: var(--sky); background: #f0f9ff; color: var(--blue); transform: translateY(-2px); box-shadow: 0 4px 8px rgba(14,165,233,.15); }
  .word-chip:active:not(.used) { cursor: grabbing; }
  .word-chip.active { border-color: #2563eb; background: #dbeafe; color: #1e40af; box-shadow: 0 0 0 3px rgba(37,99,235,.25); animation: pulse 1.5s infinite; }
  .word-chip.used { opacity: .35; background: #f1f5f9; border-color: #e2e8f0; color: #94a3b8; cursor: not-allowed; text-decoration: line-through; }
  
  /* Matching (匹配) */
  .match-list { display: flex; flex-direction: column; gap: 12px; margin-bottom: 22px; }
  .match-row { display: grid; grid-template-columns: 1fr 1.25fr; gap: 14px; align-items: stretch; }
  @media (max-width: 640px) { .match-row { grid-template-columns: 1fr; gap: 6px; } }
  .match-key { background: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid var(--blue); border-radius: 10px; padding: 14px 16px; font-size: .92rem; font-weight: 600; color: #1e293b; display: flex; align-items: center; }
  .match-slot { background: #ffffff; border: 2px dashed #93c5fd; border-radius: 10px; padding: 12px 16px; min-height: 54px; display: flex; align-items: center; justify-content: space-between; cursor: pointer; transition: all .2s ease; user-select: none; font-size: .9rem; color: #1e40af; font-weight: 500; }
  .match-slot.empty-slot { color: #94a3b8; font-style: italic; font-size: .85rem; background: #f8fafc; }
  .match-slot.drag-over { border-color: #2563eb; background: #dbeafe; box-shadow: 0 0 8px rgba(37,99,235,.25); }
  .match-slot.filled { border-style: solid; border-color: #3b82f6; background: #eff6ff; color: #1e3a8a; font-weight: 600; }
  .match-slot .match-remove { color: #94a3b8; font-size: 1.15rem; font-weight: 700; border-radius: 50%; padding: 0 6px; transition: .15s; }
  .match-slot .match-remove:hover { color: #dc2626; background: rgba(220,38,38,.12); }
  .match-slot.correct { border-color: var(--good); background: #f0fdf4; color: #15803d; }
  .match-slot.wrong { border-color: var(--bad); background: #fef2f2; color: #b91c1c; }
  .expected-match { font-size: .8rem; color: #15803d; margin-top: 4px; font-weight: 600; }
  
  .match-bank-wrap { margin-top: 14px; }
  .match-bank-title { font-size: .88rem; font-weight: 700; color: #475569; margin-bottom: 10px; display: flex; align-items: center; gap: 6px; }
  .match-bank { display: flex; flex-direction: column; gap: 8px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 14px; }
  .match-card { background: #fff; border: 2px solid #cbd5e1; border-radius: 10px; padding: 12px 16px; font-size: .9rem; color: #334155; cursor: grab; user-select: none; transition: all .15s ease; box-shadow: 0 1px 3px rgba(0,0,0,.05); }
  .match-card:hover:not(.used) { border-color: var(--sky); background: #f0f9ff; transform: translateX(4px); }
  .match-card.active { border-color: #2563eb; background: #dbeafe; color: #1e40af; box-shadow: 0 0 0 3px rgba(37,99,235,.25); }
  .match-card.used { opacity: .35; background: #f1f5f9; border-color: #e2e8f0; cursor: not-allowed; text-decoration: line-through; }
  
  /* Sorting (排序) */
  .sort-list { display: flex; flex-direction: column; gap: 10px; margin-bottom: 16px; }
  .sort-item { display: flex; align-items: center; gap: 12px; background: #fff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 14px 16px; cursor: grab; user-select: none; transition: all .15s ease; box-shadow: 0 1px 3px rgba(0,0,0,.05); }
  .sort-item:hover { border-color: var(--sky); background: #f8fafc; }
  .sort-item:active { cursor: grabbing; }
  .sort-item.dragging { opacity: .35; border-style: dashed; border-color: #3b82f6; background: #eff6ff; }
  .sort-item.drag-over { border-color: #2563eb; background: #dbeafe; transform: translateY(-2px); }
  .sort-item.correct { border-color: var(--good); background: #f0fdf4; }
  .sort-item.wrong { border-color: var(--bad); background: #fef2f2; }
  .sort-handle { font-size: 1.25rem; color: #94a3b8; cursor: grab; padding: 0 4px; }
  .sort-num { display: flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 50%; background: #dbeafe; color: #1e40af; font-weight: 700; font-size: .85rem; flex-shrink: 0; }
  .sort-item.correct .sort-num { background: #dcfce7; color: #15803d; }
  .sort-item.wrong .sort-num { background: #fee2e2; color: #b91c1c; }
  .sort-text { flex: 1; font-size: .92rem; color: #1e293b; line-height: 1.6; }
  .sort-actions { display: flex; flex-direction: column; gap: 4px; flex-shrink: 0; }
  .sort-btn { background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 6px; width: 30px; height: 26px; display: flex; align-items: center; justify-content: center; cursor: pointer; font-size: .75rem; color: #475569; transition: .15s; }
  .sort-btn:hover:not(:disabled) { background: #dbeafe; color: #1e40af; border-color: #93c5fd; }
  .sort-btn:disabled { opacity: .25; cursor: not-allowed; }
  .sort-expected-badge { display: inline-block; background: #fef3c7; color: #92400e; font-size: .75rem; padding: 2px 8px; border-radius: 6px; margin-left: 8px; font-weight: 600; }
  
  /* Explain Box */
  .explain { display: none; background: #eff6ff; border-left: 4px solid var(--blue); border-radius: 0 10px 10px 0; padding: 16px 20px; margin-top: 14px; font-size: .92rem; color: #1e3a8a; line-height: 1.9; }
  .explain.show { display: block; }
  .verdict { font-weight: 700; margin-bottom: 8px; font-size: 1rem; line-height: 1.7; }
  
  /* Toolbar & Buttons */
  .toolbar { display: flex; justify-content: space-between; gap: 10px; margin-top: 18px; flex-wrap: wrap; }
  .btn { padding: 11px 24px; border: none; border-radius: 10px; font-size: .92rem; font-weight: 600; cursor: pointer; transition: .15s; user-select: none; }
  .btn-primary { background: var(--blue); color: #fff; }
  .btn-primary:hover { background: #1d4ed8; }
  .btn-outline { background: #f1f5f9; color: #475569; }
  .btn-outline:hover { background: #e2e8f0; }
  
  /* Results */
  .result-big { font-size: 3.4rem; font-weight: 700; margin: 12px 0; }
  .result-big.pass { color: var(--good); }
  .result-big.fail { color: var(--bad); }
  .breakdown-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 10px; }
  @media (max-width: 600px) { .breakdown-grid { grid-template-columns: 1fr; } }
  .domain-row { display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid #f1f5f9; font-size: .88rem; color: #334155; gap: 12px; }
  .domain-row:last-child { border-bottom: none; }
  
  /* Animations */
  @keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(37, 99, 235, 0.4); }
    70% { box-shadow: 0 0 0 8px rgba(37, 99, 235, 0); }
    100% { box-shadow: 0 0 0 0 rgba(37, 99, 235, 0); }
  }
  
  footer { text-align: center; padding: 18px; color: #94a3b8; font-size: .8rem; }
</style>
</head>
<body>
<div class="topbar">
  <a href="index.html">🔐 ISO 27001 指南</a><span class="sep">/</span><span>互動模擬試題</span>
</div>

<div class="hero">
  <h1>📝 <span>ISO 27001</span> 互動模擬試題</h1>
  <p>全面升級<b>五大國際認證全真題型</b>：選擇題、多選題、填寫空白、匹配與排序！全題庫共 <b>192 題</b>，涵蓋 Clause 4~10 條款、Annex A 93 項控制措施、<b>CQI/IRCA 主導稽核員考證實戰</b>與<b>中華電信關鍵基礎設施機電維運實戰</b>。支援拖放互動、即時詳解與錯題複習。</p>
</div>

<div class="wrap"><div id="app"></div></div>
<footer>ISO 27001 學習指南 · 成績與錯題儲存於瀏覽器本機</footer>

<script>
const QUESTIONS = ${JSON.stringify(questions, null, 2)};

// ===== 應用程式邏輯 =====
const DOMAINS = {
  1: "主題 1：標準架構與條款（Clause 4~10 考證核心）",
  2: "主題 2：Annex A 控制項（93項控制措施與新版實務）",
  3: "主題 3：風險評估、SOA 與文件（方法論與審查）",
  4: "主題 4：稽核、認證與企業實務（ISO 19011 / 17021）",
  5: "主題 5：CQI / IRCA 證照考試全真模擬（主導稽核員高分檢定）",
  6: "主題 6：中華電信與關鍵基礎設施（CI）資安機電實戰題"
};

const QTYPES = {
  single: { name: "選擇題 (選擇一個正確答案)", icon: "🔘", cls: "qtype-single", hint: "請點選選擇一個最符合題意的正確答案：" },
  multi:  { name: "多選題 (選擇幾個正確答案)", icon: "☑️", cls: "qtype-multi",  hint: "⚠️ 多選題：請選擇幾個正確答案（點選按鈕進行複選勾選）：" },
  fill:   { name: "填寫空白 (拖動並將正確的單詞放入句子中)", icon: "📝", cls: "qtype-fill",   hint: "💡 提示：請將下方單詞拖動放入句子空白處（亦可點選單詞後點選空白填入；點擊空白中已填詞彙可取出）：" },
  match:  { name: "匹配 (拖放回應以正確匹配項目)", icon: "🔀", cls: "qtype-match",  hint: "💡 提示：請將下方回應項目拖放至對應項目旁配對（亦可點選項目後點選目標框配對；點擊已配對卡片可移除）：" },
  sort:   { name: "排序 (拖放回應以形成正確的順序)", icon: "🔢", cls: "qtype-sort",   hint: "💡 提示：請拖曳卡片上下調整順序，或使用右側 ▲ / ▼ 按鈕，形成正確的先後順序：" }
};

const PASS = 70;
let quiz = [], idx = 0, answers = [], submitted = false, mode = "all";
const app = document.getElementById("app");

// Interactive State per question
let selected = new Set();
let fillAnswers = [];
let fillWords = [];
let activeWord = null;
let matchAnswers = {};
let matchOptions = [];
let activeMatchOpt = null;
let sortOrder = [];
let sortDragIdx = null;

function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function getQType(q) {
  return q.type || (q.a && q.a.length > 1 ? 'multi' : 'single');
}

function renderSetup() {
  const wrong = JSON.parse(localStorage.getItem("iso_wrong") || "[]");
  const dKeys = Object.keys(DOMAINS).map(Number);
  
  const countSingle = QUESTIONS.filter(q => getQType(q) === 'single').length;
  const countMulti  = QUESTIONS.filter(q => getQType(q) === 'multi').length;
  const countFill   = QUESTIONS.filter(q => getQType(q) === 'fill').length;
  const countMatch  = QUESTIONS.filter(q => getQType(q) === 'match').length;
  const countSort   = QUESTIONS.filter(q => getQType(q) === 'sort').length;

  app.innerHTML = \`
  <div class="card">
    <h2 style="margin-bottom:8px;">選擇測驗模式</h2>
    <p class="stat" style="margin-bottom:14px;">題庫共 \${QUESTIONS.length} 題 · 依 ISO/IEC 27001:2022（含 Amendment 1:2024）、CQI/IRCA 與中華電信甄試規範出題 · 及格線 \${PASS}%</p>
    
    <div class="setup-opt" onclick="startQuiz('all')" style="border-color:#3b82f6;background:#f0f7ff;">
      <h3>📝 完整全真綜合模擬考（\${QUESTIONS.length} 題）</h3>
      <p>五大考證題型（選擇、多選、填空、匹配、排序）與主題 1~6 隨機混合出題，全方位驗收學習成效</p>
    </div>

    <div class="setup-section-title">🎯 依題型專項特訓</div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:10px;margin-bottom:12px;">
      <div class="setup-opt" onclick="startQuiz('type_single')" style="margin-bottom:0;">
        <h3>🔘 選擇題專區（\${countSingle} 題）</h3>
        <p>選擇一個正確答案，標準客觀觀念驗證</p>
      </div>
      <div class="setup-opt" onclick="startQuiz('type_multi')" style="margin-bottom:0;border-color:#d8b4fe;background:#fdf4ff;">
        <h3>☑️ 多選題專區（\${countMulti} 題）</h3>
        <p>選擇幾個正確答案，精準考驗多重條件判斷</p>
      </div>
      <div class="setup-opt" onclick="startQuiz('type_fill')" style="margin-bottom:0;border-color:#86efac;background:#f0fdf4;">
        <h3>📝 填寫空白專區（\${countFill} 題）</h3>
        <p>拖動並將正確的單詞放入句子中，核心詞彙記憶</p>
      </div>
      <div class="setup-opt" onclick="startQuiz('type_match')" style="margin-bottom:0;border-color:#fde047;background:#fffbeb;">
        <h3>🔀 匹配專區（\${countMatch} 題）</h3>
        <p>拖放回應以正確匹配項目，概念與情境精確對應</p>
      </div>
      <div class="setup-opt" onclick="startQuiz('type_sort')" style="margin-bottom:0;border-color:#7dd3fc;background:#f0f9ff;">
        <h3>🔢 排序專區（\${countSort} 題）</h3>
        <p>拖放回應以形成正確的順序，導入與應變流程梳理</p>
      </div>
    </div>

    <div class="setup-section-title">🎓 依專業模組與考證分類</div>
    <div class="setup-opt" onclick="startQuiz('la_exam')" style="border-color:#8b5cf6;background:#faf5ff;">
      <h3>🎓 CQI / IRCA 主導稽核員考證專區（\${QUESTIONS.filter(q=>q.d===5).length} 題）</h3>
      <p>專門練習 Section 1~4 概念題、稽核情境題、條款歸屬判定與 NCR 不符合報告書判定</p>
    </div>
    <div class="setup-opt" onclick="startQuiz('cht_exam')" style="border-color:#10b981;background:#f0fdf4;">
      <h3>⚡ 中華電信招考資安與機電維運專區（\${QUESTIONS.filter(q=>q.d===6).length} 題）</h3>
      <p>專門練習數據一大樓 2N 供電、UPS 電池室、發電機 ATS、BGP/DDoS 清洗、CI 通報實戰題</p>
    </div>
    <div class="setup-opt" onclick="startQuiz('quick')">
      <h3>⚡ 快速衝刺練習（20 題）</h3>
      <p>隨機抽取 20 題跨題型題目進行高效率測驗</p>
    </div>

    <div class="setup-section-title">📚 依核心主題練習</div>
    \${dKeys.map(d => \`
      <div class="setup-opt" onclick="startQuiz(\${d})">
        <h3>📖 \${DOMAINS[d]}</h3>
        <p>專攻此主題（\${QUESTIONS.filter(q=>q.d===d).length} 題）</p>
      </div>
    \`).join("")}

    \${wrong.length ? \`
      <div class="setup-opt" onclick="startQuiz('wrong')" style="border-color:#ef4444;background:#fef2f2;">
        <h3>🔁 錯題複習專區（\${wrong.length} 題）</h3>
        <p>針對上次答錯的題目進行重點突破</p>
      </div>
    \` : ""}
  </div>
  <div class="card">
    <h3 style="margin-bottom:8px;">📌 考證與測驗說明</h3>
    <p class="stat">本系統已完整整合<b>五大考證題型</b>（選擇題、多選題、填寫空白、匹配、排序），模擬最新國際認證考試（如 CQI/IRCA、CompTIA Security+、CISSP 及國家級關鍵基礎設施招考）之電腦化測驗介面。支援<b>滑鼠拖曳（Drag & Drop）</b>與<b>點選填入/按鈕調整</b>雙重操作模式，完美相容桌面與行動裝置。</p>
  </div>\`;
}

window.startQuiz = function(m) {
  mode = m;
  if (m === "all") quiz = shuffle(QUESTIONS);
  else if (m === "quick") quiz = shuffle(QUESTIONS).slice(0, 20);
  else if (m === "la_exam") quiz = shuffle(QUESTIONS.filter(q => q.d === 5));
  else if (m === "cht_exam") quiz = shuffle(QUESTIONS.filter(q => q.d === 6));
  else if (m === "type_single") quiz = shuffle(QUESTIONS.filter(q => getQType(q) === 'single'));
  else if (m === "type_multi") quiz = shuffle(QUESTIONS.filter(q => getQType(q) === 'multi'));
  else if (m === "type_fill") quiz = shuffle(QUESTIONS.filter(q => getQType(q) === 'fill'));
  else if (m === "type_match") quiz = shuffle(QUESTIONS.filter(q => getQType(q) === 'match'));
  else if (m === "type_sort") quiz = shuffle(QUESTIONS.filter(q => getQType(q) === 'sort'));
  else if (m === "wrong") {
    const w = JSON.parse(localStorage.getItem("iso_wrong") || "[]");
    quiz = shuffle(QUESTIONS.filter((q, i) => w.includes(i)));
  } else {
    quiz = shuffle(QUESTIONS.filter(q => q.d === m));
  }
  
  idx = 0;
  answers = [];
  renderQuestion();
};

function renderQuestion() {
  const q = quiz[idx];
  const type = getQType(q);
  submitted = false;
  selected = new Set();
  activeWord = null;
  activeMatchOpt = null;
  sortDragIdx = null;

  if (type === 'fill') {
    fillAnswers = new Array(q.a.length).fill(null);
    fillWords = shuffle(q.words);
  } else if (type === 'match') {
    matchAnswers = {};
    matchOptions = shuffle(q.options || q.items.map(it => it.target));
  } else if (type === 'sort') {
    let attempts = 0;
    sortOrder = shuffle(q.items);
    while (sortOrder.every((it, i) => it === q.items[i]) && q.items.length > 1 && attempts < 5) {
      sortOrder = shuffle(q.items);
      attempts++;
    }
  }

  renderQuestionUI();
}

function renderQuestionUI() {
  const q = quiz[idx];
  const type = getQType(q);
  const qMeta = QTYPES[type];

  let bodyHtml = "";
  if (type === 'single') {
    bodyHtml = \`
      <div class="type-hint">\${qMeta.hint}</div>
      \${q.o.map((o, i) => \`
        <button class="opt \${selected.has(i)?'selected':''}" id="opt\${i}" onclick="pickSingle(\${i})">
          <span class="opt-letter">\${String.fromCharCode(65+i)}.</span>
          <span class="opt-txt">\${escapeHtml(o)}</span>
        </button>
      \`).join("")}
    \`;
  } else if (type === 'multi') {
    bodyHtml = \`
      <div class="type-hint multi-hint">\${qMeta.hint}</div>
      \${q.o.map((o, i) => \`
        <button class="opt multi-opt \${selected.has(i)?'selected':''}" id="opt\${i}" onclick="pickMulti(\${i})">
          <span class="check-box">\${selected.has(i)?'✓':''}</span>
          <span class="opt-letter">\${String.fromCharCode(65+i)}.</span>
          <span class="opt-txt">\${escapeHtml(o)}</span>
        </button>
      \`).join("")}
    \`;
  } else if (type === 'fill') {
    let sentenceHtml = q.text.replace(/\\{(\\d+)\\}/g, (match, slotIdx) => {
      const sIdx = parseInt(slotIdx);
      const val = fillAnswers[sIdx];
      return \`<span class="drop-slot \${val?'filled':'empty-slot'}" id="slot-\${sIdx}" data-slot="\${sIdx}" onclick="handleSlotClick(\${sIdx})" ondragover="handleFillDragOver(event)" ondragleave="handleFillDragLeave(event)" ondrop="handleFillDrop(event, \${sIdx})">
        \${val ? \`<span>\${escapeHtml(val)}</span>\${!submitted ? \`<span class="slot-remove" onclick="event.stopPropagation(); removeSlotWord(\${sIdx})" title="取回單詞">×</span>\` : ''}\` : \`<span class="empty-hint">〔 空白 \${sIdx+1} 〕</span>\`}
      </span>\`;
    });

    bodyHtml = \`
      <div class="type-hint fill-hint">\${qMeta.hint}</div>
      <div class="fill-sentence">\${sentenceHtml}</div>
      \${!submitted ? \`
        <div class="word-bank-wrap">
          <div class="word-bank-title">🔤 候選單詞庫（拖曳或點選單詞填入）：</div>
          <div class="word-bank">
            \${fillWords.map((w, wIdx) => {
              const isUsed = fillAnswers.includes(w);
              const isActive = activeWord === w;
              return \`<span class="word-chip \${isUsed?'used':''} \${isActive?'active':''}" id="chip-\${wIdx}" draggable="\${!isUsed}" ondragstart="handleFillDragStart(event, '\${encodeURIComponent(w)}')" onclick="handleChipClick('\${encodeURIComponent(w)}')">\${escapeHtml(w)}</span>\`;
            }).join("")}
          </div>
        </div>
      \` : ''}
    \`;
  } else if (type === 'match') {
    bodyHtml = \`
      <div class="type-hint match-hint">\${qMeta.hint}</div>
      <div class="match-list">
        \${q.items.map((it, i) => \`
          <div class="match-row" id="match-row-\${i}">
            <div class="match-key">\${escapeHtml(it.key)}</div>
            <div class="match-slot \${matchAnswers[i]?'filled':'empty-slot'}" id="match-slot-\${i}" data-idx="\${i}" onclick="handleMatchSlotClick(\${i})" ondragover="handleMatchDragOver(event)" ondragleave="handleMatchDragLeave(event)" ondrop="handleMatchDrop(event, \${i})">
              \${matchAnswers[i] ? \`<span>\${escapeHtml(matchAnswers[i])}</span>\${!submitted ? \`<span class="match-remove" onclick="event.stopPropagation(); removeMatchItem(\${i})" title="取消配對">×</span>\` : ''}\` : \`<span class="slot-placeholder">〔 請拖放或點選項目至此 〕</span>\`}
            </div>
          </div>
        \`).join("")}
      </div>
      \${!submitted ? \`
        <div class="match-bank-wrap">
          <div class="match-bank-title">📋 候選回應清單（拖放或點選配對）：</div>
          <div class="match-bank">
            \${matchOptions.map((opt, optIdx) => {
              const isUsed = Object.values(matchAnswers).includes(opt);
              const isActive = activeMatchOpt === opt;
              return \`<div class="match-card \${isUsed?'used':''} \${isActive?'active':''}" draggable="\${!isUsed}" id="mcard-\${optIdx}" ondragstart="handleMatchDragStart(event, '\${encodeURIComponent(opt)}')" onclick="handleMatchCardClick('\${encodeURIComponent(opt)}')">\${escapeHtml(opt)}</div>\`;
            }).join("")}
          </div>
        </div>
      \` : ''}
    \`;
  } else if (type === 'sort') {
    bodyHtml = \`
      <div class="type-hint sort-hint">\${qMeta.hint}</div>
      <div class="sort-list" id="sortList">
        \${sortOrder.map((item, i) => \`
          <div class="sort-item" id="sort-item-\${i}" draggable="\${!submitted}" ondragstart="handleSortDragStart(event, \${i})" ondragover="handleSortDragOver(event, \${i})" ondragleave="handleSortDragLeave(event)" ondrop="handleSortDrop(event, \${i})">
            <span class="sort-handle" title="拖曳排序">☰</span>
            <span class="sort-num">\${i + 1}</span>
            <div class="sort-text">\${escapeHtml(item)}</div>
            \${!submitted ? \`
              <div class="sort-actions">
                <button type="button" class="sort-btn" onclick="moveSortItem(\${i}, -1)" \${i===0?'disabled':''} title="向上移">▲</button>
                <button type="button" class="sort-btn" onclick="moveSortItem(\${i}, 1)" \${i===sortOrder.length-1?'disabled':''} title="向下移">▼</button>
              </div>
            \` : ''}
          </div>
        \`).join("")}
      </div>
    \`;
  }

  app.innerHTML = \`
    <div class="progress-wrap"><div class="progress-bar" style="width:\${idx / quiz.length * 100}%"></div></div>
    <div class="stat" style="margin-bottom:8px;">第 \${idx + 1} / \${quiz.length} 題</div>
    <div class="card">
      <div class="tag-row">
        <span class="qtype-tag \${qMeta.cls}">\${qMeta.icon} \${qMeta.name}</span>
        <span class="domain-tag">\${DOMAINS[q.d]}</span>
      </div>
      <div class="q-text">\${q.q}</div>
      <div id="qBody">\${bodyHtml}</div>
      <div class="explain" id="explain"></div>
      <div class="toolbar">
        <button class="btn btn-outline" onclick="renderSetup()">結束測驗</button>
        <button class="btn btn-primary" id="mainBtn" onclick="submitAnswer()">送出答案</button>
      </div>
    </div>
  \`;
}

// ── Single Choice Handlers ──
window.pickSingle = function(i) {
  if (submitted) return;
  selected.clear();
  selected.add(i);
  document.querySelectorAll(".opt").forEach((b, idx) => {
    b.classList.toggle("selected", idx === i);
  });
};

// ── Multi Choice Handlers ──
window.pickMulti = function(i) {
  if (submitted) return;
  if (selected.has(i)) selected.delete(i);
  else selected.add(i);
  
  document.querySelectorAll(".opt").forEach((b, idx) => {
    const isSel = selected.has(idx);
    b.classList.toggle("selected", isSel);
    const cb = b.querySelector(".check-box");
    if (cb) cb.textContent = isSel ? "✓" : "";
  });
};

// ── Fill in Blank Handlers ──
window.handleFillDragStart = function(e, encodedWord) {
  const word = decodeURIComponent(encodedWord);
  e.dataTransfer.setData("text/plain", word);
};

window.handleFillDragOver = function(e) {
  if (submitted) return;
  e.preventDefault();
  e.currentTarget.classList.add("drag-over");
};

window.handleFillDragLeave = function(e) {
  e.currentTarget.classList.remove("drag-over");
};

window.handleFillDrop = function(e, slotIdx) {
  if (submitted) return;
  e.preventDefault();
  e.currentTarget.classList.remove("drag-over");
  const word = e.dataTransfer.getData("text/plain");
  if (!word) return;
  placeWordInSlot(word, slotIdx);
};

window.handleChipClick = function(encodedWord) {
  if (submitted) return;
  const word = decodeURIComponent(encodedWord);
  if (fillAnswers.includes(word)) return;
  activeWord = (activeWord === word ? null : word);
  renderQuestionUI();
};

window.handleSlotClick = function(slotIdx) {
  if (submitted) return;
  if (activeWord) {
    placeWordInSlot(activeWord, slotIdx);
    activeWord = null;
  } else if (fillAnswers[slotIdx]) {
    removeSlotWord(slotIdx);
  }
};

window.removeSlotWord = function(slotIdx) {
  if (submitted) return;
  fillAnswers[slotIdx] = null;
  renderQuestionUI();
};

function placeWordInSlot(word, slotIdx) {
  const oldIdx = fillAnswers.indexOf(word);
  if (oldIdx !== -1 && oldIdx !== slotIdx) {
    fillAnswers[oldIdx] = null;
  }
  fillAnswers[slotIdx] = word;
  renderQuestionUI();
}

// ── Matching Handlers ──
window.handleMatchDragStart = function(e, encodedOpt) {
  const opt = decodeURIComponent(encodedOpt);
  e.dataTransfer.setData("text/plain", opt);
};

window.handleMatchDragOver = function(e) {
  if (submitted) return;
  e.preventDefault();
  e.currentTarget.classList.add("drag-over");
};

window.handleMatchDragLeave = function(e) {
  e.currentTarget.classList.remove("drag-over");
};

window.handleMatchDrop = function(e, itemIdx) {
  if (submitted) return;
  e.preventDefault();
  e.currentTarget.classList.remove("drag-over");
  const opt = e.dataTransfer.getData("text/plain");
  if (!opt) return;
  placeMatchInSlot(opt, itemIdx);
};

window.handleMatchCardClick = function(encodedOpt) {
  if (submitted) return;
  const opt = decodeURIComponent(encodedOpt);
  if (Object.values(matchAnswers).includes(opt)) return;
  activeMatchOpt = (activeMatchOpt === opt ? null : opt);
  renderQuestionUI();
};

window.handleMatchSlotClick = function(itemIdx) {
  if (submitted) return;
  if (activeMatchOpt) {
    placeMatchInSlot(activeMatchOpt, itemIdx);
    activeMatchOpt = null;
  } else if (matchAnswers[itemIdx]) {
    removeMatchItem(itemIdx);
  }
};

window.removeMatchItem = function(itemIdx) {
  if (submitted) return;
  delete matchAnswers[itemIdx];
  renderQuestionUI();
};

function placeMatchInSlot(opt, itemIdx) {
  for (let k in matchAnswers) {
    if (matchAnswers[k] === opt) delete matchAnswers[k];
  }
  matchAnswers[itemIdx] = opt;
  renderQuestionUI();
}

// ── Sorting Handlers ──
window.handleSortDragStart = function(e, idx) {
  if (submitted) return;
  sortDragIdx = idx;
  e.dataTransfer.setData("text/plain", idx);
  e.currentTarget.classList.add("dragging");
};

window.handleSortDragOver = function(e, idx) {
  if (submitted) return;
  e.preventDefault();
  e.currentTarget.classList.add("drag-over");
};

window.handleSortDragLeave = function(e) {
  e.currentTarget.classList.remove("drag-over");
};

window.handleSortDrop = function(e, targetIdx) {
  if (submitted) return;
  e.preventDefault();
  e.currentTarget.classList.remove("drag-over");
  const fromIdx = sortDragIdx !== null ? sortDragIdx : parseInt(e.dataTransfer.getData("text/plain"));
  if (isNaN(fromIdx) || fromIdx === targetIdx) return;
  
  const moved = sortOrder.splice(fromIdx, 1)[0];
  sortOrder.splice(targetIdx, 0, moved);
  sortDragIdx = null;
  renderQuestionUI();
};

window.moveSortItem = function(idx, dir) {
  if (submitted) return;
  const targetIdx = idx + dir;
  if (targetIdx < 0 || targetIdx >= sortOrder.length) return;
  const temp = sortOrder[idx];
  sortOrder[idx] = sortOrder[targetIdx];
  sortOrder[targetIdx] = temp;
  renderQuestionUI();
};

// ── Submit Answer ──
window.submitAnswer = function() {
  const q = quiz[idx];
  const type = getQType(q);

  if (!submitted) {
    let correct = false;
    let verdictHtml = "";

    if (type === 'single') {
      if (selected.size === 0) { alert("請先選擇一個答案"); return; }
      submitted = true;
      const userChoice = Array.from(selected)[0];
      correct = (userChoice === q.a[0]);
      
      document.querySelectorAll(".opt").forEach((b, i) => {
        b.disabled = true;
        if (i === q.a[0]) b.classList.add("correct");
        else if (selected.has(i)) b.classList.add("wrong");
      });
      
      verdictHtml = correct 
        ? '<div class="verdict" style="color:var(--good)">✅ 答對了！</div>' 
        : \`<div class="verdict" style="color:var(--bad)">❌ 答錯了。正確答案是：<b>\${String.fromCharCode(65 + q.a[0])}. \${escapeHtml(q.o[q.a[0]])}</b></div>\`;
    } 
    else if (type === 'multi') {
      if (selected.size === 0) { alert("請至少選擇一個答案"); return; }
      submitted = true;
      correct = (q.a.length === selected.size && q.a.every(a => selected.has(a)));
      
      document.querySelectorAll(".opt").forEach((b, i) => {
        b.disabled = true;
        if (q.a.includes(i)) b.classList.add("correct");
        else if (selected.has(i)) b.classList.add("wrong");
      });
      
      const correctLetters = q.a.map(a => String.fromCharCode(65 + a)).join(", ");
      verdictHtml = correct
        ? '<div class="verdict" style="color:var(--good)">✅ 答對了！所有正確選項皆已選出。</div>'
        : \`<div class="verdict" style="color:var(--bad)">❌ 答錯了。本題正確答案為：<b>\${correctLetters}</b></div>\`;
    } 
    else if (type === 'fill') {
      if (fillAnswers.some(a => !a)) {
        if (!confirm("尚有空白未填寫，確定要送出答案嗎？")) return;
      }
      submitted = true;
      correct = q.a.every((ans, i) => fillAnswers[i] === ans);
      
      q.a.forEach((ans, i) => {
        const slotEl = document.getElementById(\`slot-\${i}\`);
        if (!slotEl) return;
        if (fillAnswers[i] === ans) {
          slotEl.classList.add("correct");
        } else {
          slotEl.classList.add("wrong");
          slotEl.innerHTML = \`<span>\${escapeHtml(fillAnswers[i] || '未填')}</span><span class="expected-tag">正解: \${escapeHtml(ans)}</span>\`;
        }
      });
      
      const expectedText = q.a.map((ans, i) => \`【空白 \${i+1}】：<b>\${escapeHtml(ans)}</b>\`).join("， ");
      verdictHtml = correct
        ? '<div class="verdict" style="color:var(--good)">✅ 答對了！所有詞彙填入完全正確。</div>'
        : \`<div class="verdict" style="color:var(--bad)">❌ 答錯了。正確填答應為：<br>\${expectedText}</div>\`;
    } 
    else if (type === 'match') {
      if (q.items.some((_, i) => !matchAnswers[i])) {
        if (!confirm("尚有項目未完成配對，確定要送出答案嗎？")) return;
      }
      submitted = true;
      correct = q.items.every((it, i) => matchAnswers[i] === it.target);
      
      q.items.forEach((it, i) => {
        const slotEl = document.getElementById(\`match-slot-\${i}\`);
        if (!slotEl) return;
        if (matchAnswers[i] === it.target) {
          slotEl.classList.add("correct");
        } else {
          slotEl.classList.add("wrong");
          slotEl.innerHTML = \`<span>\${escapeHtml(matchAnswers[i] || '未配對')}</span><div class="expected-match">✅ 正確配對：\${escapeHtml(it.target)}</div>\`;
        }
      });
      
      const matchDetails = q.items.map(it => \`<b>\${escapeHtml(it.key)}</b> ➔ <b>\${escapeHtml(it.target)}</b>\`).join("<br>");
      verdictHtml = correct
        ? '<div class="verdict" style="color:var(--good)">✅ 答對了！所有對應項目配對完全正確。</div>'
        : \`<div class="verdict" style="color:var(--bad)">❌ 配對有誤。標準配對結果如下：<br>\${matchDetails}</div>\`;
    } 
    else if (type === 'sort') {
      submitted = true;
      correct = q.items.every((it, i) => sortOrder[i] === it);
      
      sortOrder.forEach((it, i) => {
        const itemEl = document.getElementById(\`sort-item-\${i}\`);
        if (!itemEl) return;
        if (sortOrder[i] === q.items[i]) {
          itemEl.classList.add("correct");
        } else {
          itemEl.classList.add("wrong");
          const expectedStep = q.items.indexOf(it) + 1;
          const badge = document.createElement("span");
          badge.className = "sort-expected-badge";
          badge.textContent = \`應為第 \${expectedStep} 步\`;
          itemEl.querySelector(".sort-text").appendChild(badge);
        }
      });
      
      // Hide buttons in sort
      document.querySelectorAll(".sort-actions").forEach(el => el.style.display = "none");

      const correctOrderList = q.items.map((it, i) => \`<b>第 \${i+1} 步</b>：\${escapeHtml(it)}\`).join("<br>");
      verdictHtml = correct
        ? '<div class="verdict" style="color:var(--good)">✅ 答對了！排序完全符合標準程序規範。</div>'
        : \`<div class="verdict" style="color:var(--bad)">❌ 順序有誤。標準正確順序如下：<br>\${correctOrderList}</div>\`;
    }

    answers.push({
      d: q.d,
      type: type,
      correct: correct,
      qi: QUESTIONS.indexOf(q)
    });

    const ex = document.getElementById("explain");
    ex.innerHTML = verdictHtml + q.e;
    ex.classList.add("show");
    document.getElementById("mainBtn").textContent = (idx === quiz.length - 1 ? "查看成績" : "下一題");

  } else {
    idx++;
    if (idx < quiz.length) renderQuestion();
    else renderResult();
  }
};

// ── Render Result ──
function renderResult() {
  const total = answers.length;
  const right = answers.filter(a => a.correct).length;
  const pct = Math.round(right / total * 100);
  const pass = pct >= PASS;
  
  const wrongIdx = answers.filter(a => !a.correct).map(a => a.qi);
  localStorage.setItem("iso_wrong", JSON.stringify(wrongIdx));
  
  const hist = JSON.parse(localStorage.getItem("iso_history") || "[]");
  hist.push({ date: new Date().toLocaleDateString("zh-TW"), pct, total, mode });
  localStorage.setItem("iso_history", JSON.stringify(hist.slice(-20)));

  // Domain Breakdown
  let domainRows = "";
  for (const d of Object.keys(DOMAINS).map(Number)) {
    const da = answers.filter(a => a.d === d);
    if (!da.length) continue;
    const dr = da.filter(a => a.correct).length;
    const dpct = Math.round(dr / da.length * 100);
    domainRows += \`<div class="domain-row">
      <span>\${DOMAINS[d]}</span>
      <strong style="color:\${dpct >= PASS ? 'var(--good)' : 'var(--bad)'}">\${dr}/\${da.length}（\${dpct}%）</strong>
    </div>\`;
  }

  // Question Type Breakdown
  let typeRows = "";
  for (const t of Object.keys(QTYPES)) {
    const ta = answers.filter(a => a.type === t);
    if (!ta.length) continue;
    const tr = ta.filter(a => a.correct).length;
    const tpct = Math.round(tr / ta.length * 100);
    typeRows += \`<div class="domain-row">
      <span>\${QTYPES[t].icon} \${QTYPES[t].name}</span>
      <strong style="color:\${tpct >= PASS ? 'var(--good)' : 'var(--bad)'}">\${tr}/\${ta.length}（\${tpct}%）</strong>
    </div>\`;
  }

  app.innerHTML = \`
  <div class="card" style="text-align:center;">
    <h2>測驗結果</h2>
    <div class="result-big \${pass ? 'pass' : 'fail'}">\${pct}%</div>
    <p style="font-size:1.05rem;margin-bottom:6px;color:#334155;">\${right} / \${total} 題正確 · \${pass ? "🎉 恭喜達到及格門檻（" + PASS + "%）！" : "未達及格門檻（" + PASS + "%），建議複習弱項題型再接再厲！"}</p>
  </div>

  <div class="card">
    <h3 style="margin-bottom:8px;">🎯 題型表現分析</h3>
    \${typeRows}
  </div>

  <div class="card">
    <h3 style="margin-bottom:8px;">📚 各主題專業領域表現</h3>
    \${domainRows}
    <p class="stat" style="margin-top:12px;">💡 建議針對正確率低於 \${PASS}% 的主題或題型，使用「題型專項特訓」加強刷題。</p>
  </div>

  <div class="card">
    <h3 style="margin-bottom:8px;">🕒 歷史成績紀錄</h3>
    \${hist.slice(-5).reverse().map(h => \`
      <div class="domain-row">
        <span>\${h.date}（\${h.total} 題 · 模式: \${h.mode || '綜合'}）</span>
        <strong>\${h.pct}%</strong>
      </div>
    \`).join("")}
  </div>

  <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;">
    \${wrongIdx.length ? \`<button class="btn btn-primary" onclick="startQuiz('wrong')">🔁 複習 \${wrongIdx.length} 題錯題</button>\` : ""}
    <button class="btn btn-outline" onclick="renderSetup()">回到模式選擇</button>
  </div>\`;
}

renderSetup();
</script>

<!-- portfolio-analytics:begin -->
<script>window.ANALYTICS_CONFIG={"url": "https://rkotktpmpatojxxnqlpj.supabase.co", "key": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJrb3RrdHBtcGF0b2p4eG5xbHBqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODEyOTgxMTAsImV4cCI6MjA5Njg3NDExMH0.GRs9u9t7pU5ERTtXkMYovCL0d1bqCcQGXvIdNxAtGqk"};</script>
<script data-project="iso27001">
(function () {
  'use strict';
  var CFG = window.ANALYTICS_CONFIG || {};
  var script = document.currentScript;
  var PROJECT = (script && script.getAttribute('data-project')) || 'iso27001';
  var LIVE = !!(CFG.url && CFG.key && typeof fetch === 'function');
  var STORAGE_KEY = 'portfolio_views_' + PROJECT;
  var DEDUP_KEY = 'portfolio_viewed_' + PROJECT;

  function visitorId() {
    var k = 'portfolio_vid';
    var vid = localStorage.getItem(k);
    if (!vid) {
      vid = 'v_' + Math.random().toString(36).slice(2) + Date.now().toString(36);
      localStorage.setItem(k, vid);
    }
    return vid;
  }

  function shouldCount() {
    var last = sessionStorage.getItem(DEDUP_KEY);
    if (last) return false;
    sessionStorage.setItem(DEDUP_KEY, String(Date.now()));
    return true;
  }

  function localBump() {
    try {
      var d = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{"total":0,"days":{}}');
      var today = new Date().toISOString().slice(0, 10);
      d.total = (d.total || 0) + 1;
      d.days[today] = (d.days[today] || 0) + 1;
      localStorage.setItem(STORAGE_KEY, JSON.stringify(d));
    } catch (e) {}
  }

  function localRead() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{"total":0,"days":{}}');
    } catch (e) {
      return { total: 0, days: {} };
    }
  }

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
        page_path: location.pathname + location.search,
        visitor_id: visitorId(),
        referrer: document.referrer ? document.referrer.slice(0, 300) : null
      })
    }).catch(function () { localBump(); });
  }

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
    track: track, summary: summary, paint: paint
  };

  function boot() { track().then(paint); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
</script>
<!-- portfolio-analytics:end -->
<script src="assets/tts.js"></script>
</body>
</html>
`;

fs.writeFileSync(path.join(__dirname, 'quiz.html'), htmlTemplate, 'utf8');
console.log('Successfully wrote updated quiz.html with 5 question types!');
