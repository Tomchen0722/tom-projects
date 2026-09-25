/**
 * PM 專案管理 × 產品管理完全指南 — 全方位英文發音引擎 (TTS)
 * 1. 徹底覆蓋全站所有英文單字、縮寫與專有名詞（不限於括號），為每一處英文精準附加 🔊 發音按鈕與點擊朗讀。
 * 2. 採用 Web Speech API 標準美式發音 (en-US)，語速 0.85x，音質清晰自然。
 * 3. 英文詞彙本身亦可點擊朗讀 (.en-term)。
 * 4. 支援滑鼠劃詞選取任意文字即時彈出浮動「🔊 朗讀發音」氣泡按鈕。
 * 5. 正在播放時具備微光動態回饋，再點一次可隨時停止。
 */
(function () {
  'use strict';

  // 1. 動態注入 TTS 專屬樣式
  var style = document.createElement('style');
  style.id = 'pm-tts-engine-styles';
  style.textContent = `
    /* 行內英文詞彙：懸停提示可點擊朗讀 */
    .en-term {
      border-bottom: 1px dotted rgba(234, 88, 12, 0.45);
      cursor: pointer;
      transition: color 0.15s ease, border-color 0.15s ease;
    }
    .en-term:hover {
      color: #c2410c;
      border-bottom-color: #c2410c;
    }

    /* 行內英文發音小按鈕 🔊 */
    .spk-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      margin-left: 2px;
      margin-right: 3px;
      padding: 0 4px;
      font-size: 0.72em;
      line-height: 1.25;
      color: #ea580c;
      background: #fff7ed;
      border: 1px solid #fdba74;
      border-radius: 4px;
      cursor: pointer;
      user-select: none;
      vertical-align: baseline;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      box-shadow: 0 1px 2px rgba(0,0,0,0.04);
      text-decoration: none !important;
    }
    .spk-btn:hover {
      background: #ea580c;
      color: #ffffff;
      border-color: #ea580c;
      transform: scale(1.15);
      box-shadow: 0 2px 6px rgba(234, 88, 12, 0.35);
    }
    .spk-btn.spk-playing {
      background: #ea580c;
      color: #ffffff;
      border-color: #c2410c;
      animation: pm-spk-pulse 1.2s infinite;
    }
    @keyframes pm-spk-pulse {
      0% { box-shadow: 0 0 0 0 rgba(234, 88, 12, 0.6); }
      70% { box-shadow: 0 0 0 6px rgba(234, 88, 12, 0); }
      100% { box-shadow: 0 0 0 0 rgba(234, 88, 12, 0); }
    }

    /* 劃詞反白浮動朗讀按鈕 */
    #tts-selection-bubble {
      position: absolute;
      display: none;
      background: linear-gradient(135deg, #ea580c, #c2410c);
      color: #ffffff;
      padding: 5px 12px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(234, 88, 12, 0.4);
      z-index: 999999;
      user-select: none;
      transition: transform 0.15s ease, opacity 0.15s ease;
      white-space: nowrap;
      pointer-events: auto;
    }
    #tts-selection-bubble:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(234, 88, 12, 0.5);
    }
    #tts-selection-bubble:active {
      transform: translateY(0);
    }

    /* 右下角輔助提示小貼紙 */
    #pm-tts-badge {
      position: fixed;
      bottom: 16px;
      right: 16px;
      background: rgba(255, 255, 255, 0.95);
      border: 1px solid #fdba74;
      color: #9a3412;
      padding: 6px 14px;
      border-radius: 24px;
      font-size: 0.76rem;
      font-weight: 600;
      box-shadow: 0 4px 16px rgba(0,0,0,0.08);
      z-index: 9999;
      display: flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
      transition: all 0.25s ease;
      backdrop-filter: blur(4px);
    }
    #pm-tts-badge:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(234, 88, 12, 0.25);
      background: #fff7ed;
      color: #c2410c;
    }
    #pm-tts-badge .tts-close {
      opacity: 0.5;
      font-size: 0.85em;
      margin-left: 4px;
    }
    #pm-tts-badge .tts-close:hover {
      opacity: 1;
    }
  `;
  document.head.appendChild(style);

  // 2. 語音合成核心
  var speakingBtn = null;

  function cleanForSpeech(raw) {
    if (!raw) return '';
    var t = raw;
    // 移除中文字符
    t = t.replace(/[\u4e00-\u9fa5]+/g, ' ');
    // 替換特定符號
    t = t.replace(/[\/|\\]+/g, ', ');
    t = t.replace(/[（）()「」、。，；：？！\-_+=*&^%$#@~`><\[\]{}【】]/g, ' ');
    t = t.replace(/\s+/g, ' ').trim();
    return t;
  }

  window.speakEn = function (text, btn) {
    if (!('speechSynthesis' in window)) {
      alert('您的瀏覽器不支援 Web Speech API 語音朗讀功能。');
      return;
    }

    var cleanText = cleanForSpeech(text);
    if (!cleanText) return;

    // 若點擊正在朗讀的同一個按鈕，則停止播放
    if (speakingBtn && (speakingBtn === btn || !btn)) {
      window.speechSynthesis.cancel();
      if (speakingBtn) {
        speakingBtn.classList.remove('spk-playing');
        speakingBtn = null;
      }
      return;
    }

    window.speechSynthesis.cancel();
    if (speakingBtn) {
      speakingBtn.classList.remove('spk-playing');
      speakingBtn = null;
    }

    var u = new SpeechSynthesisUtterance(cleanText);
    u.lang = 'en-US';
    u.rate = 0.85; // 清晰自然，最適合專業術語聽音學習
    u.pitch = 1.0;

    if (btn) {
      speakingBtn = btn;
      btn.classList.add('spk-playing');
    }

    u.onend = u.onerror = function () {
      if (speakingBtn) {
        speakingBtn.classList.remove('spk-playing');
        speakingBtn = null;
      }
    };

    window.speechSynthesis.speak(u);
  };

  // 3. 建立 🔊 發音按鈕 DOM 元素
  function createSpkButton(getText, title) {
    var btn = document.createElement('span');
    btn.setAttribute('role', 'button');
    btn.className = 'spk-btn';
    btn.setAttribute('aria-label', '朗讀英文');
    btn.title = title || '點擊朗讀英文發音（再按一次停止）';
    btn.innerHTML = '🔊';
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      var t = typeof getText === 'function' ? getText() : getText;
      window.speakEn(t, btn);
    });
    return btn;
  }

  // 判斷是否為合格英文詞彙
  function shouldSpeak(term) {
    if (!term) return false;
    var letters = (term.match(/[A-Za-z]/g) || []).length;
    if (letters < 2) return false;

    // 過濾檔案後綴或網址代碼
    if (/\.(html|js|css|json|py|md|png|jpg|svg|co)$/i.test(term)) return false;
    if (/^(http|https|file|mailto|ftp):/i.test(term)) return false;

    // 過濾貨幣符號連綴
    if (/^(US|NT|TWD|USD|RMB)\$/i.test(term)) return false;

    // 過濾佔位符
    if (/^(XX|YY|ZZ|ABC)$/i.test(term)) return false;

    return true;
  }

  // 4. 全自動掃描文字節點並附加發音按鈕
  function autoAttachSpeechButtons() {
    var candidateContainers = document.querySelectorAll(
      '.hero, .intro-banner, .dual, .path, .card, .container'
    );

    var textNodes = [];

    candidateContainers.forEach(function (container) {
      if (container.dataset.spkProcessed) return;
      container.dataset.spkProcessed = '1';

      var walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT, null, false);
      var node;
      while ((node = walker.nextNode())) {
        var parent = node.parentNode;
        if (!parent) continue;
        // 排除程式碼區塊、導覽按鈕列、頁首、頁尾、已有按鈕的容器
        if (parent.closest('pre, code, .code-box, .sim-board, .topbar, .nav-btns, footer, script, style, .spk-btn, #pm-tts-badge, #tts-selection-bubble')) {
          continue;
        }
        textNodes.push(node);
      }
    });

    // 匹配英文單詞或連續英文片語
    var engRegex = /\b([A-Za-z][A-Za-z0-9]*(?:['’\-_/][A-Za-z0-9]+)*(?:\s+[A-Za-z][A-Za-z0-9]*(?:['’\-_/][A-Za-z0-9]+)*)*)\b/g;

    textNodes.forEach(function (textNode) {
      var text = textNode.nodeValue;
      if (!text) return;

      engRegex.lastIndex = 0;
      if (!engRegex.test(text)) return;
      engRegex.lastIndex = 0;

      var frag = document.createDocumentFragment();
      var lastIndex = 0;
      var match;
      var found = false;

      while ((match = engRegex.exec(text)) !== null) {
        var term = match[1].trim();
        // 避開 US$555 的情況
        if (text[match.index + match[0].length] === '$' && (term === 'US' || term === 'NT' || term === 'TWD')) {
          continue;
        }
        if (!shouldSpeak(term)) continue;

        found = true;
        // 前置文字
        var beforeText = text.substring(lastIndex, match.index);
        if (beforeText) {
          frag.appendChild(document.createTextNode(beforeText));
        }

        // 英文詞彙本體包裝（點擊亦可朗讀）
        var termSpan = document.createElement('span');
        termSpan.className = 'en-term';
        termSpan.textContent = term;
        termSpan.title = '點擊聽發音: ' + term;
        
        var btn = createSpkButton(term, '點擊朗讀 ' + term);

        (function (t, b) {
          termSpan.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();
            window.speakEn(t, b);
          });
        })(term, btn);

        frag.appendChild(termSpan);
        frag.appendChild(btn);

        lastIndex = match.index + match[0].length;
      }

      if (found) {
        if (lastIndex < text.length) {
          frag.appendChild(document.createTextNode(text.substring(lastIndex)));
        }
        if (textNode.parentNode) {
          textNode.parentNode.replaceChild(frag, textNode);
        }
      }
    });
  }

  // 5. 劃詞選取發音按鈕 (Selection Floating Bubble)
  function initSelectionBubble() {
    var bubble = document.createElement('div');
    bubble.id = 'tts-selection-bubble';
    bubble.innerHTML = '🔊 朗讀發音';
    document.body.appendChild(bubble);

    var selectedText = '';

    function handleSelection() {
      setTimeout(function () {
        var selection = window.getSelection();
        var text = selection.toString().trim();
        var letters = (text.match(/[A-Za-z]/g) || []).length;

        if (text && letters >= 2 && selection.rangeCount > 0) {
          selectedText = text;
          var range = selection.getRangeAt(0);
          var rect = range.getBoundingClientRect();

          if (rect.width > 0 && rect.height > 0) {
            var top = rect.top + window.scrollY - 38;
            var left = rect.left + window.scrollX + (rect.width / 2) - 45;

            bubble.style.top = (top > 0 ? top : 10) + 'px';
            bubble.style.left = (left > 10 ? left : 10) + 'px';
            bubble.style.display = 'block';
            return;
          }
        }
        bubble.style.display = 'none';
      }, 20);
    }

    document.addEventListener('mouseup', handleSelection);
    document.addEventListener('keyup', handleSelection);

    bubble.addEventListener('mousedown', function (e) {
      e.preventDefault();
      e.stopPropagation();
      if (selectedText) {
        window.speakEn(selectedText, null);
      }
    });

    document.addEventListener('mousedown', function (e) {
      if (e.target !== bubble) {
        bubble.style.display = 'none';
      }
    });
  }

  // 6. 右下角快捷提示小標籤
  function initTtsBadge() {
    if (document.getElementById('pm-tts-badge')) return;
    var badge = document.createElement('div');
    badge.id = 'pm-tts-badge';
    badge.innerHTML = '🔊 <span>英文發音已就緒 · 點擊喇叭或詞彙聽讀</span><span class="tts-close" title="隱藏提示">✕</span>';
    badge.onclick = function (e) {
      if (e.target.classList.contains('tts-close')) {
        badge.style.display = 'none';
        return;
      }
      window.speakEn('Welcome to the PM Complete Guide. All English terms now have audio pronunciation.', null);
    };
    document.body.appendChild(badge);
  }

  // 7. 啟動引擎
  function init() {
    autoAttachSpeechButtons();
    initSelectionBubble();
    initTtsBadge();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
