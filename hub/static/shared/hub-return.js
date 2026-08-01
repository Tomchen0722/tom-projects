/* ══════════════════════════════════════════════════════════════
   回 Hub 浮動按鈕
   由 Project Hub 提供，各專案只需引入一行：
     <script src="http://127.0.0.1:7000/shared/hub-return.js"></script>

   設計上刻意做成「載入失敗就當作不存在」——
   單獨執行專案（沒開 Hub）時不會有任何錯誤或副作用。
   ══════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  var HUB = 'http://127.0.0.1:7000';

  // 自己就是 Hub 頁面時不要重複加
  if (location.port === '7000') return;
  if (document.getElementById('tom-hub-return')) return;

  function mount() {
    if (!document.body) return;

    var css = [
      '#tom-hub-return{',
      '  position:fixed;left:18px;bottom:18px;z-index:2147483000;',
      '  display:inline-flex;align-items:center;gap:8px;',
      '  min-height:44px;padding:11px 18px;',
      '  background:#1C1A18;color:#FEFEF9;',
      '  font-family:"Noto Sans TC","Microsoft JhengHei",sans-serif;',
      '  font-size:13px;font-weight:500;letter-spacing:.03em;line-height:1;',
      '  text-decoration:none;border:none;cursor:pointer;',
      '  box-shadow:0 6px 24px rgba(28,26,24,.22);',
      '  transition:background .25s cubic-bezier(.22,1,.36,1),transform .25s cubic-bezier(.22,1,.36,1);',
      '}',
      '#tom-hub-return::after{',
      '  content:"";position:absolute;bottom:-3px;right:-3px;',
      '  width:100%;height:100%;border:1.5px solid #3A68AD;opacity:.45;',
      '  pointer-events:none;transition:opacity .25s;',
      '}',
      '#tom-hub-return:hover{background:#3A68AD;transform:translateY(-2px);}',
      '#tom-hub-return:hover::after{opacity:0;}',
      '#tom-hub-return:focus-visible{outline:2px solid #3A68AD;outline-offset:3px;}',
      '@media (max-width:600px){#tom-hub-return{left:12px;bottom:12px;padding:11px 15px;font-size:12px;}}',
      '@media (prefers-reduced-motion:reduce){#tom-hub-return{transition:none;}}',
      '@media print{#tom-hub-return{display:none;}}',
    ].join('');

    var style = document.createElement('style');
    style.textContent = css;
    document.head.appendChild(style);

    var a = document.createElement('a');
    a.id = 'tom-hub-return';
    a.href = HUB;
    a.setAttribute('aria-label', '返回 Project Hub 總覽頁');
    a.title = '返回 Project Hub';
    a.innerHTML =
      '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"' +
      ' stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
      '<line x1="19" y1="12" x2="5" y2="12"></line>' +
      '<polyline points="12 19 5 12 12 5"></polyline></svg>' +
      '<span>回 Hub</span>';

    document.body.appendChild(a);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mount);
  } else {
    mount();
  }
})();
