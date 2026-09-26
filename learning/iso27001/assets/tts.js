/**
 * ISO 27001 資訊安全完全指南 — 全方位英文發音引擎 (TTS Engine)
 * 1. 深度掃描全站所有標題、卡片、條款、表格、清單、提示盒中的英文單字、縮寫與專有名詞，自動附加 🔊 朗讀按鈕。
 * 2. 支援英文詞彙直接點擊發音 (.en-term) 與專屬發音按鈕 (.spk-btn)。
 * 3. 採用 Web Speech API 標準美式發音 (en-US)，語速 0.85x，音質清晰自然。
 * 4. 內建資安與管理體系專業縮寫朗讀字典（ISMS、CIA、PDCA、SoA、RTO、RPO、MFA、SIEM、SOC 等），精準拼讀。
 * 5. 支援滑鼠劃詞選取任意英文文字即時彈出浮動「🔊 朗讀發音」氣泡。
 * 6. 支援 MutationObserver，測驗頁面 (quiz.html) 切換題目與顯示解析時自動無縫綁定發音。
 * 7. 具備播放中微光呼吸動畫回饋，重複點擊可隨時停止播放。
 * 8. 自動排除代碼區塊 (code, pre)、導航頂欄、頁尾與計數器。
 */
(function () {
  'use strict';

  // 1. 動態注入 ISO 27001 專屬 TTS 樣式
  var style = document.createElement('style');
  style.id = 'iso-tts-engine-styles';
  style.textContent = `
    /* 行內英文詞彙：懸停提示可點擊朗讀 */
    .en-term {
      border-bottom: 1px dotted rgba(30, 64, 175, 0.45);
      cursor: pointer;
      transition: color 0.15s ease, border-color 0.15s ease, background-color 0.15s ease;
      border-radius: 2px;
      padding: 0 1px;
    }
    .en-term:hover {
      color: #1d4ed8;
      background-color: rgba(219, 234, 254, 0.45);
      border-bottom-color: #1d4ed8;
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
      color: #1e40af;
      background: #eff6ff;
      border: 1px solid #93c5fd;
      border-radius: 4px;
      cursor: pointer;
      user-select: none;
      vertical-align: baseline;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      box-shadow: 0 1px 2px rgba(0,0,0,0.04);
      text-decoration: none !important;
    }
    .spk-btn:hover {
      background: #1e40af;
      color: #ffffff;
      border-color: #1e40af;
      transform: scale(1.15);
      box-shadow: 0 2px 6px rgba(30, 64, 175, 0.35);
    }
    .spk-btn.spk-playing {
      background: #0ea5e9;
      color: #ffffff;
      border-color: #0284c7;
      animation: iso-spk-pulse 1.2s infinite;
    }
    @keyframes iso-spk-pulse {
      0% { box-shadow: 0 0 0 0 rgba(14, 165, 233, 0.7); }
      70% { box-shadow: 0 0 0 6px rgba(14, 165, 233, 0); }
      100% { box-shadow: 0 0 0 0 rgba(14, 165, 233, 0); }
    }

    /* 劃詞反白浮動朗讀按鈕 */
    #tts-selection-bubble {
      position: absolute;
      display: none;
      background: linear-gradient(135deg, #1e40af, #0ea5e9);
      color: #ffffff;
      padding: 5px 12px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(14, 165, 233, 0.4);
      z-index: 999999;
      user-select: none;
      transition: transform 0.15s ease, opacity 0.15s ease;
      white-space: nowrap;
      pointer-events: auto;
    }
    #tts-selection-bubble:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(14, 165, 233, 0.55);
    }
    #tts-selection-bubble:active {
      transform: translateY(0);
    }

    /* 右下角輔助提示小貼紙 */
    #iso-tts-badge {
      position: fixed;
      bottom: 16px;
      right: 16px;
      background: rgba(255, 255, 255, 0.95);
      border: 1px solid #93c5fd;
      color: #1e40af;
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
      backdrop-filter: blur(6px);
    }
    #iso-tts-badge:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(30, 64, 175, 0.25);
      background: #eff6ff;
      color: #1d4ed8;
    }
    #iso-tts-badge .tts-close {
      opacity: 0.5;
      font-size: 0.85em;
      margin-left: 4px;
    }
    #iso-tts-badge .tts-close:hover {
      opacity: 1;
    }
  `;
  document.head.appendChild(style);

  // 2. 資安專業縮寫發音優化字典
  var ACRONYM_SPOKEN = {
    'ISMS': 'I S M S',
    'CIA': 'C I A',
    'PDCA': 'P D C A',
    'SOA': 'S O A',
    'SoA': 'S O A',
    'RTO': 'R T O',
    'RPO': 'R P O',
    'BIA': 'B I A',
    'BCP': 'B C P',
    'DRP': 'D R P',
    'MFA': 'M F A',
    '2FA': 'Two F A',
    'SSO': 'S S O',
    'RBAC': 'R BAC',
    'ABAC': 'A BAC',
    'EDR': 'E D R',
    'XDR': 'X D R',
    'MDR': 'M D R',
    'SIEM': 'seem',
    'SOC': 'sock',
    'WAF': 'waf',
    'DLP': 'D L P',
    'IDS': 'I D S',
    'IPS': 'I P S',
    'VPN': 'V P N',
    'TLS': 'T L S',
    'SSL': 'S S L',
    'PKI': 'P K I',
    'CA': 'C A',
    'DNS': 'D N S',
    'URL': 'U R L',
    'IP': 'I P',
    'API': 'A P I',
    'OWASP': 'oh-wasp',
    'CVE': 'C V E',
    'CVSS': 'C V S S',
    'GDPR': 'G D P R',
    'BYOD': 'B Y O D',
    'CEO': 'C E O',
    'CIO': 'C I O',
    'CISO': 'see-so',
    'CTO': 'C T O',
    'CFO': 'C F O',
    'COO': 'C O O',
    'KPI': 'K P I',
    'KRI': 'K R I',
    'SLA': 'S L A',
    'NDA': 'N D A',
    'IT': 'I T',
    'OT': 'O T',
    'IoT': 'I o T',
    'AI': 'A I',
    'HR': 'H R',
    'QA': 'Q A',
    'QC': 'Q C',
    'CB': 'C B',
    'AB': 'A B',
    'IAF': 'I A F',
    'TAF': 'T A F',
    'NCR': 'N C R',
    'CAR': 'C A R',
    'CAPA': 'kay-puh',
    'OFI': 'O F I',
    'IEC': 'I E C',
    'ISO': 'eye-so',
    'HLS': 'H L S',
    'MSS': 'M S S',
    'CSIRT': 'see-sirt',
    'CERT': 'sert',
    'SOC2': 'sock two',
    'SOC 2': 'sock two'
  };

  // 3. 語音合成核心
  var speakingBtn = null;
  var preferredVoice = null;

  function updateVoices() {
    if (!('speechSynthesis' in window)) return;
    var voices = window.speechSynthesis.getVoices();
    preferredVoice = voices.find(function (v) {
      return v.lang === 'en-US' && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Samantha') || v.name.includes('Jenny') || v.name.includes('Guy'));
    }) || voices.find(function (v) {
      return v.lang === 'en-US';
    }) || voices.find(function (v) {
      return v.lang && v.lang.startsWith('en');
    }) || null;
  }

  if ('speechSynthesis' in window) {
    updateVoices();
    window.speechSynthesis.onvoiceschanged = updateVoices;
  }

  function cleanForSpeech(raw) {
    if (!raw) return '';
    var t = raw.trim();

    if (ACRONYM_SPOKEN[t]) return ACRONYM_SPOKEN[t];
    if (ACRONYM_SPOKEN[t.toUpperCase()]) return ACRONYM_SPOKEN[t.toUpperCase()];

    // 移除中文字符
    t = t.replace(/[\u4e00-\u9fa5]+/g, ' ');
    // 替換特定符號
    t = t.replace(/[\/|\\]+/g, ', ');
    t = t.replace(/:/g, ' ');
    t = t.replace(/[（）()「」、。，；：？！\-_+=*&^%$#@~`><\[\]{}【】]/g, ' ');

    var words = t.split(/\s+/);
    var processed = words.map(function (w) {
      var cleanW = w.replace(/[^A-Za-z0-9]/g, '');
      if (ACRONYM_SPOKEN[cleanW]) return w.replace(cleanW, ACRONYM_SPOKEN[cleanW]);
      if (ACRONYM_SPOKEN[cleanW.toUpperCase()]) return w.replace(cleanW, ACRONYM_SPOKEN[cleanW.toUpperCase()]);
      return w;
    });

    return processed.join(' ').replace(/\s+/g, ' ').trim();
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
    if (preferredVoice) {
      u.voice = preferredVoice;
    }

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

  // 4. 建立 🔊 發音按鈕 DOM 元素
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
    if (letters < 2) return false; // 排除單字母選項（如 A, B, C, D）

    // 過濾檔案後綴或網址代碼
    if (/\.(html|js|css|json|py|md|png|jpg|svg|ico)$/i.test(term)) return false;
    if (/^(http|https|file|mailto|ftp):/i.test(term)) return false;

    // 過濾貨幣符號連綴
    if (/^(US|NT|TWD|USD|RMB)\$/i.test(term)) return false;

    // 過濾佔位符
    if (/^(XX|YY|ZZ)$/i.test(term)) return false;

    return true;
  }

  // 5. 全自動掃描文字節點並附加發音按鈕
  function autoAttachSpeechButtons(root) {
    var candidateContainers;
    if (root) {
      candidateContainers = [root];
    } else {
      candidateContainers = document.querySelectorAll(
        '.hero, .container, .wrap, #app, .card, .module, .cert-banner, .path, .tip-box, .highlight, .clause, .pdca, .table-wrap, .ex, main, article'
      );
    }

    var textNodes = [];

    candidateContainers.forEach(function (container) {
      if (!container) return;
      var walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT, null, false);
      var node;
      while ((node = walker.nextNode())) {
        var parent = node.parentNode;
        if (!parent) continue;
        // 排除程式碼區塊、導覽按鈕列、頁首、頁尾、已有按鈕的容器
        if (parent.closest('pre, code, .code-box, .sim-board, .topbar, .nav-btns, footer, script, style, .spk-btn, .en-term, #iso-tts-badge, #tts-selection-bubble, #view-counter, #tom-hub-return')) {
          continue;
        }
        textNodes.push(node);
      }
    });

    // 匹配英文單詞或連續英文片語（支援 ISO 27001、ISO/IEC 27001:2022、Plan-Do-Check-Act、SoA、CIA 等）
    var engRegex = /\b([A-Za-z][A-Za-z0-9]*(?:['’\-_/][A-Za-z0-9]+)*(?::\d+)?(?:\s+[A-Za-z0-9]+(?:['’\-_/][A-Za-z0-9]+)*(?::\d+)?)*)\b/g;

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
        var remainText = text.substring(lastIndex);
        if (remainText) {
          frag.appendChild(document.createTextNode(remainText));
        }
        if (textNode.parentNode) {
          textNode.parentNode.replaceChild(frag, textNode);
        }
      }
    });
  }

  // 6. 劃詞選取即時朗讀氣泡
  function initSelectionBubble() {
    var bubble = document.createElement('div');
    bubble.id = 'tts-selection-bubble';
    bubble.innerHTML = '🔊 朗讀發音';
    document.body.appendChild(bubble);

    var currentSelectedText = '';

    document.addEventListener('mouseup', function (e) {
      if (e.target && (e.target.id === 'tts-selection-bubble' || e.target.closest('#tts-selection-bubble'))) {
        return;
      }

      var sel = window.getSelection();
      var text = sel ? sel.toString().trim() : '';

      if (text && shouldSpeak(text)) {
        currentSelectedText = text;
        var range = sel.getRangeAt(0);
        var rect = range.getBoundingClientRect();
        var top = rect.top + window.scrollY - 38;
        var left = rect.left + window.scrollX + (rect.width / 2) - 45;

        bubble.style.top = Math.max(10, top) + 'px';
        bubble.style.left = Math.max(10, left) + 'px';
        bubble.style.display = 'block';
      } else {
        bubble.style.display = 'none';
        currentSelectedText = '';
      }
    });

    bubble.addEventListener('mousedown', function (e) {
      e.preventDefault();
      e.stopPropagation();
      if (currentSelectedText) {
        window.speakEn(currentSelectedText);
      }
      bubble.style.display = 'none';
    });

    document.addEventListener('mousedown', function (e) {
      if (e.target && e.target.id !== 'tts-selection-bubble' && !e.target.closest('#tts-selection-bubble')) {
        bubble.style.display = 'none';
      }
    });
  }

  // 7. 右下角提示小貼紙
  function initTtsBadge() {
    if (localStorage.getItem('iso_tts_badge_hidden') === '1') return;

    var badge = document.createElement('div');
    badge.id = 'iso-tts-badge';
    badge.innerHTML = '<span>🔊 英文發音已就緒</span><span class="tts-close" title="關閉提示">✕</span>';
    badge.title = '點擊任意英文單字或 🔊 按鈕即可聆聽真人美式發音；反白選取文字也可即時朗讀！';

    badge.querySelector('.tts-close').addEventListener('click', function (e) {
      e.stopPropagation();
      badge.remove();
      localStorage.setItem('iso_tts_badge_hidden', '1');
    });

    badge.addEventListener('click', function () {
      window.speakEn('Welcome to ISO 27001 Information Security Management System Complete Guide.');
    });

    document.body.appendChild(badge);
  }

  // 8. 監聽動態 DOM 變化 (支援 quiz.html 等動態渲染內容)
  var observerTimeout = null;
  function observeDynamicContent() {
    if (!window.MutationObserver) return;
    var observer = new MutationObserver(function (mutations) {
      var shouldScan = false;
      for (var i = 0; i < mutations.length; i++) {
        var m = mutations[i];
        if (m.target && m.target.classList && (m.target.classList.contains('spk-btn') || m.target.classList.contains('en-term'))) {
          continue;
        }
        if (m.addedNodes && m.addedNodes.length > 0) {
          for (var j = 0; j < m.addedNodes.length; j++) {
            var n = m.addedNodes[j];
            if (n.nodeType === 1 && (n.classList.contains('spk-btn') || n.classList.contains('en-term') || n.id === 'tts-selection-bubble')) {
              continue;
            }
            shouldScan = true;
            break;
          }
        }
        if (shouldScan) break;
      }

      if (shouldScan) {
        clearTimeout(observerTimeout);
        observerTimeout = setTimeout(function () {
          autoAttachSpeechButtons();
        }, 120);
      }
    });

    observer.observe(document.body, {
      childList: true,
      subtree: true
    });
  }

  // 9. 啟動入口
  function init() {
    autoAttachSpeechButtons();
    initSelectionBubble();
    initTtsBadge();
    observeDynamicContent();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
