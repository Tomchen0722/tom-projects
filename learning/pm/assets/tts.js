/**
 * PM 專案管理 × 產品管理完全指南 — 智慧英文發音引擎 (TTS)
 * 1. 提供全局 speakEn(text, btn)：透過瀏覽器 Web Speech API 朗讀標準美式英語（en-US），語速 0.85x 舒適清晰。
 * 2. 自動標註發音按鈕：自動掃描頁面所有括號專有名詞、粗體英文術語、標題、表格名詞，插入 🔊 發音按鈕。
 * 3. 劃詞選取即時朗讀：滑鼠選取任何含英文文字時，自動浮現「🔊 朗讀發音」氣泡按鈕。
 * 4. 點擊播放中按鈕即時停止，具備微光動態回饋。
 */
(function () {
  'use strict';

  // 1. 動態注入 TTS 專屬樣式
  var style = document.createElement('style');
  style.id = 'pm-tts-engine-styles';
  style.textContent = `
    /* 行內英文發音小按鈕 */
    .spk-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      margin-left: 4px;
      margin-right: 2px;
      padding: 1px 5px;
      font-size: 0.72em;
      line-height: 1.2;
      color: #ea580c;
      background: #fff7ed;
      border: 1px solid #fdba74;
      border-radius: 4px;
      cursor: pointer;
      user-select: none;
      vertical-align: middle;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      box-shadow: 0 1px 2px rgba(0,0,0,0.05);
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
    // 替換特殊分隔符為自然停頓
    t = t.replace(/[\/|\\]+/g, ', ');
    // 移除括號與特殊標點符號
    t = t.replace(/[（）()「」、。，；：？！\-_+=*&^%$#@~`><\[\]{}]/g, ' ');
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
    var btn = document.createElement('button');
    btn.type = 'button';
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

  // 4. 自動掃描頁面並附加發音按鈕
  function autoAttachSpeechButtons() {
    var candidateContainers = document.querySelectorAll(
      '.container p, .container li, .container td, .container th, .container h1, .container h2, .container h3, .container h4, .card p, .card li, .card td, .card th, .card h2, .card h3, .dual-card, .trophy'
    );

    // 匹配 (English Term)
    var parenRegex = /([\(（]([A-Za-z][A-Za-z0-9\s\-_\/'.&]{1,60})[\)）])/g;

    candidateContainers.forEach(function (container) {
      if (container.closest('pre') || container.closest('code') || container.dataset.spkScanned) return;
      container.dataset.spkScanned = '1';

      var walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT, null, false);
      var textNodes = [];
      var node;
      while ((node = walker.nextNode())) {
        if (node.parentNode && (node.parentNode.nodeName === 'CODE' || node.parentNode.nodeName === 'PRE' || node.parentNode.classList.contains('spk-btn') || node.parentNode.id === 'pm-tts-badge')) {
          continue;
        }
        textNodes.push(node);
      }

      textNodes.forEach(function (textNode) {
        var text = textNode.nodeValue;
        if (!text) return;
        parenRegex.lastIndex = 0;

        if (parenRegex.test(text)) {
          parenRegex.lastIndex = 0;
          var frag = document.createDocumentFragment();
          var lastIndex = 0;
          var match;
          var found = false;

          while ((match = parenRegex.exec(text)) !== null) {
            var fullMatch = match[1];
            var engTerm = match[2].trim();

            var letterCount = (engTerm.match(/[A-Za-z]/g) || []).length;
            if (letterCount < 2) continue;

            found = true;
            var beforeText = text.substring(lastIndex, match.index + fullMatch.length);
            frag.appendChild(document.createTextNode(beforeText));

            var btn = createSpkButton(engTerm, '點擊朗讀 ' + engTerm);
            frag.appendChild(btn);

            lastIndex = match.index + fullMatch.length;
          }

          if (found) {
            if (lastIndex < text.length) {
              frag.appendChild(document.createTextNode(text.substring(lastIndex)));
            }
            if (textNode.parentNode) {
              textNode.parentNode.replaceChild(frag, textNode);
            }
          }
        }
      });
    });

    // (B) 處理 <strong> 或 <b> 或 .tag 中純英文專有名詞（如 Jira, Trello, Scrum, WBS, EVM, PMP, PRD, MVP 等）
    var inlineStrong = document.querySelectorAll('.container strong, .container b, .card strong, .card b, .tag, th');
    inlineStrong.forEach(function (el) {
      if (el.dataset.spkAttached || el.querySelector('.spk-btn')) return;
      var text = el.textContent.trim();
      // 去除可能已有的括號
      var clean = cleanForSpeech(text);
      var letterCount = (clean.match(/[A-Za-z]/g) || []).length;
      var totalCount = clean.length;
      
      // 如果文字中英文字母占 70% 以上，且長度在 2~40 字元之間
      if (letterCount >= 2 && (letterCount / totalCount >= 0.7) && clean.length <= 40) {
        // 檢查後面是否已經緊接著一個按鈕或帶有括號的英文
        var nextSib = el.nextSibling;
        if (nextSib && nextSib.nodeType === 3 && /^\s*[\(（]/.test(nextSib.nodeValue)) {
          // 後面有括號英文，由 Pattern A 處理，此處跳過避免重複按鈕
          return;
        }
        el.dataset.spkAttached = '1';
        var btn = createSpkButton(clean, '點擊朗讀 ' + clean);
        el.parentNode.insertBefore(btn, el.nextSibling);
      }
    });

    // (C) 處理標題包含純英文的卡片（如 h2 中的 Jira, Trello, WBS, PMP, PMO, PRD 等）
    var headings = document.querySelectorAll('.card h2, .hero h1, .feature-box h3');
    headings.forEach(function (h) {
      if (h.dataset.spkAttached) return;
      var engMatches = h.textContent.match(/\b([A-Za-z][A-Za-z0-9\s\-_.]{1,30})\b/g);
      if (engMatches) {
        engMatches.forEach(function (term) {
          term = term.trim();
          if (term.length >= 2 && !h.querySelector('.spk-btn')) {
            var btn = createSpkButton(term, '點擊朗讀 ' + term);
            h.appendChild(btn);
          }
        });
      }
      h.dataset.spkAttached = '1';
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

        // 若選取的文字包含至少 2 個英文字母
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
    badge.innerHTML = '🔊 <span>英文發音已就緒 · 點擊喇叭或反白聽讀</span><span class="tts-close" title="隱藏提示">✕</span>';
    badge.onclick = function (e) {
      if (e.target.classList.contains('tts-close')) {
        badge.style.display = 'none';
        return;
      }
      window.speakEn('Welcome to the complete guide for Project Management and Product Management. Happy learning!', null);
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
