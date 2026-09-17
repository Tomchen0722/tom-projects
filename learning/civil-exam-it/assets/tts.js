/**
 * 智慧英文發音引擎 (TTS) — 公職資訊處理國考教材
 * 1. 提供全局 speakEn(text, btn)：透過瀏覽器 Web Speech API 朗讀標準美式英語（en-US），語速 0.82x 舒適清晰。
 * 2. 劃詞選取發音：滑鼠選取任何含英文文字時，自動浮現「🔊 發音」氣泡按鈕。
 * 3. 專有名詞自動附加按鈕：自動在「中文 (English Term)」、名詞速查表、英文題目/選項旁插入點擊朗讀按鈕。
 * 4. 點擊正在播放之按鈕可即刻停止播放，並具備播放動態回饋。
 */
(function () {
  'use strict';

  // 1. 動態注入 TTS 專屬樣式
  var style = document.createElement('style');
  style.id = 'tts-engine-styles';
  style.textContent = `
    /* 行內英文發音小按鈕 */
    .spk-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      margin-left: 5px;
      margin-right: 3px;
      padding: 1px 5px;
      font-size: 0.78em;
      line-height: 1.2;
      color: #0284c7;
      background: #f0f9ff;
      border: 1px solid #bae6fd;
      border-radius: 4px;
      cursor: pointer;
      user-select: none;
      vertical-align: middle;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      box-shadow: 0 1px 2px rgba(0,0,0,0.05);
      text-decoration: none !important;
    }
    .spk-btn:hover {
      background: #0284c7;
      color: #ffffff;
      border-color: #0284c7;
      transform: scale(1.1);
      box-shadow: 0 2px 5px rgba(2,132,199,0.3);
    }
    .spk-btn.spk-playing {
      background: #0284c7;
      color: #ffffff;
      border-color: #0369a1;
      animation: spk-pulse-glow 1.2s infinite;
    }
    @keyframes spk-pulse-glow {
      0% { box-shadow: 0 0 0 0 rgba(2, 132, 199, 0.6); }
      70% { box-shadow: 0 0 0 6px rgba(2, 132, 199, 0); }
      100% { box-shadow: 0 0 0 0 rgba(2, 132, 199, 0); }
    }

    /* 劃詞反白浮動朗讀按鈕 */
    #tts-selection-bubble {
      position: absolute;
      display: none;
      background: linear-gradient(135deg, #0284c7, #0369a1);
      color: #ffffff;
      padding: 5px 12px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 500;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(2, 132, 199, 0.4);
      z-index: 999999;
      user-select: none;
      transition: transform 0.15s ease, opacity 0.15s ease;
      white-space: nowrap;
      pointer-events: auto;
    }
    #tts-selection-bubble:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(2, 132, 199, 0.5);
    }
    #tts-selection-bubble:active {
      transform: translateY(0);
    }
  `;
  document.head.appendChild(style);

  // 2. 語音合成核心
  var speakingBtn = null;

  function cleanForSpeech(raw) {
    if (!raw) return '';
    var t = raw;
    // 移除 MathJax/LaTeX 標籤與代號
    t = t.replace(/\$\$.+?\$\$/gs, ' ');
    t = t.replace(/\$[^\$]+?\$/g, ' ');
    t = t.replace(/\\\w+(\{[^}]*\})?/g, ' ');
    // 移除中文字符
    t = t.replace(/[\u4e00-\u9fa5]+/g, ' ');
    // 替換特殊分隔符為自然停頓
    t = t.replace(/[\/|\\]+/g, ', ');
    // 移除多餘符號
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
    u.rate = 0.82; // 稍慢而清晰，最適合國考考生聽清發音與音節
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
    btn.title = title || '點擊朗讀英文（再按一次停止）';
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
    // (A) 處理括號內的英文專有名詞，例如：子網路遮罩 (Subnet Mask)、網路位址 (Network ID)
    // 遍歷所有可能含有段落文字的標籤
    var candidateContainers = document.querySelectorAll(
      '.container p, .container li, .container td, .container .step-item, .container h1, .container h2, .container h3, .container h4, .container .frame, .container .easy, .container .hl, .card p, .card li, .card td, .card h2, .card h3'
    );

    var parenRegex = /([\(（]([A-Za-z][A-Za-z0-9\s\-_/\'.]{1,50})[\)）])/g;

    candidateContainers.forEach(function (container) {
      // 避免在 code block, pre, script, 或已標記的容器中操作
      if (container.closest('pre') || container.closest('code') || container.dataset.spkScanned) return;
      container.dataset.spkScanned = '1';

      // 檢查子節點中的純文字節點 (Text Nodes)
      var walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT, null, false);
      var textNodes = [];
      var node;
      while ((node = walker.nextNode())) {
        // 跳過 code, pre 內的文字
        if (node.parentNode && (node.parentNode.nodeName === 'CODE' || node.parentNode.nodeName === 'PRE' || node.parentNode.classList.contains('spk-btn'))) {
          continue;
        }
        textNodes.push(node);
      }

      textNodes.forEach(function (textNode) {
        var text = textNode.nodeValue;
        if (!text) return;
        var match;
        parenRegex.lastIndex = 0;
        
        // 如果有匹配括號英文
        if (parenRegex.test(text)) {
          parenRegex.lastIndex = 0;
          var frag = document.createDocumentFragment();
          var lastIndex = 0;
          var found = false;

          while ((match = parenRegex.exec(text)) !== null) {
            var fullMatch = match[1]; // (Subnet Mask)
            var engTerm = match[2].trim(); // Subnet Mask

            // 確保英文字母至少占 50%
            var letterCount = (engTerm.match(/[A-Za-z]/g) || []).length;
            if (letterCount < 2) continue;

            found = true;
            // 匹配前面的純文字
            var beforeText = text.substring(lastIndex, match.index + fullMatch.length);
            frag.appendChild(document.createTextNode(beforeText));

            // 插入 🔊 按鈕
            var btn = createSpkButton(engTerm, '點擊朗讀 ' + engTerm);
            frag.appendChild(btn);

            lastIndex = match.index + fullMatch.length;
          }

          if (found) {
            // 補上最後的文字
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

    // (B) 處理名詞速查表 (glossary.html) 或術語對照表中的英文欄位
    var tables = document.querySelectorAll('table');
    tables.forEach(function (tbl) {
      if (tbl.dataset.spkAttached) return;
      tbl.dataset.spkAttached = '1';

      var rows = tbl.querySelectorAll('tbody tr, tr');
      rows.forEach(function (row) {
        var firstCell = row.querySelector('td:first-child');
        if (firstCell && !firstCell.querySelector('.spk-btn')) {
          var cellText = (firstCell.textContent || '').trim();
          // 如果第一格包含英文縮寫或專有名詞 (如 ADT, BST, CIDR, Subnet Mask 等)
          var englishLetters = (cellText.match(/[A-Za-z]/g) || []).length;
          if (englishLetters >= 2 && cellText.length < 80) {
            // 提取第一格文字發音
            var btn = createSpkButton(function () {
              return cellText;
            }, '點擊朗讀 ' + cellText);
            firstCell.appendChild(btn);
          }
        }
      });
    });

    // (C) 標有 .en 的元素
    document.querySelectorAll('.en').forEach(function (el) {
      if (el.dataset.spkAttached || el.querySelector('.spk-btn')) return;
      el.dataset.spkAttached = '1';
      var text = el.textContent.trim();
      if (text) {
        el.appendChild(createSpkButton(text, '點擊朗讀 ' + text));
      }
    });

    // (D) 題目與選項中的純英文
    document.querySelectorAll('.q .ch span').forEach(function (el) {
      var t = (el.textContent || '').trim();
      if (/^[A-Za-z][A-Za-z0-9\s\-',.()\/]{1,60}$/.test(t)) {
        var p = el.parentNode;
        if (p && !p.dataset.spkAttached && !p.querySelector('.spk-btn')) {
          p.dataset.spkAttached = '1';
          p.appendChild(createSpkButton(t, '點擊朗讀 ' + t));
        }
      }
    });
  }

  // 5. 劃詞選取發音按鈕 (Selection Floating Bubble)
  function initSelectionBubble() {
    var bubble = document.createElement('div');
    bubble.id = 'tts-selection-bubble';
    bubble.innerHTML = '🔊 朗讀英文';
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
    document.addEventListener('keyup', function (e) {
      if (e.key === 'Shift' || e.key.startsWith('Arrow')) {
        handleSelection();
      }
    });

    document.addEventListener('mousedown', function (e) {
      if (e.target !== bubble) {
        bubble.style.display = 'none';
      }
    });

    bubble.addEventListener('mousedown', function (e) {
      e.preventDefault(); // 防止點擊清空選取範圍
    });

    bubble.addEventListener('click', function (e) {
      e.stopPropagation();
      window.speakEn(selectedText, bubble);
    });
  }

  // 6. 頁面載入與自動初始化
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      initSelectionBubble();
      autoAttachSpeechButtons();
    });
  } else {
    initSelectionBubble();
    autoAttachSpeechButtons();
  }

  // 提供動態加載後的手動重新掃描介面
  window.refreshSpeechButtons = autoAttachSpeechButtons;
})();
