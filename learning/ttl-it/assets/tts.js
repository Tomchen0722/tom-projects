/**
 * 台灣菸酒招考從業職員（資訊管理）- 智慧英文語音合成引擎 (TTS Engine)
 * 核心功能：
 * 1. 行內點擊朗讀 (Inline Pronunciation): 點擊 .spk-btn 或專有名詞自動朗讀標準英語。
 * 2. 劃詞選取發音 (Selection Bubble): 自由選取頁面中任何英文詞句，浮現「🔊 發音」氣泡按鈕。
 * 3. 語音保護與停頓優化 (Speech Normalization): 自動處理專業術語縮寫 (如 SQL, ACID, DBMS, TCP/IP, RESTful)。
 * 4. 舒適慢速 (0.85x) 與音準調控，支援中途停止與播放中動態脈衝光圈反饋。
 */

(function () {
  'use strict';

  // 1. 動態注入 TTS 專用暖色系樣式
  var style = document.createElement('style');
  style.id = 'tts-engine-styles';
  style.textContent = `
    /* 行內英文發音小按鈕 */
    .spk-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 3px;
      margin: 0 4px;
      padding: 1px 7px;
      font-size: 0.78em;
      font-family: 'JetBrains Mono', monospace;
      line-height: 1.3;
      color: #B87818;
      background: #FDF8F0;
      border: 1px solid rgba(184, 120, 24, 0.35);
      border-radius: 4px;
      cursor: pointer;
      user-select: none;
      vertical-align: middle;
      transition: all 0.22s cubic-bezier(0.22, 1, 0.36, 1);
      box-shadow: 0 1px 2px rgba(184, 120, 24, 0.08);
      text-decoration: none !important;
    }
    .spk-btn:hover {
      background: #C2410C;
      color: #ffffff;
      border-color: #C2410C;
      transform: translateY(-1px) scale(1.05);
      box-shadow: 0 3px 8px rgba(194, 65, 12, 0.3);
    }
    .spk-btn.spk-playing {
      background: #C2410C;
      color: #ffffff;
      border-color: #9A3412;
      animation: spk-pulse-amber 1.2s infinite;
    }
    @keyframes spk-pulse-amber {
      0% { box-shadow: 0 0 0 0 rgba(194, 65, 12, 0.6); }
      70% { box-shadow: 0 0 0 7px rgba(194, 65, 12, 0); }
      100% { box-shadow: 0 0 0 0 rgba(194, 65, 12, 0); }
    }

    /* 劃詞反白浮動朗讀按鈕 */
    #tts-selection-bubble {
      position: absolute;
      display: none;
      background: linear-gradient(135deg, #1F1A17, #38302A);
      color: #FDFBF7;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 500;
      cursor: pointer;
      box-shadow: 0 6px 20px rgba(31, 26, 23, 0.35);
      border: 1px solid rgba(184, 120, 24, 0.4);
      z-index: 999999;
      user-select: none;
      transition: transform 0.15s ease, opacity 0.15s ease;
      white-space: nowrap;
      pointer-events: auto;
    }
    #tts-selection-bubble:hover {
      background: #C2410C;
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(194, 65, 12, 0.45);
    }
    #tts-selection-bubble:active {
      transform: translateY(0);
    }

    /* 英文術語標記卡片 */
    .term-en {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 600;
      color: #1F1A17;
      background: rgba(184, 120, 24, 0.08);
      padding: 1px 5px;
      border-radius: 4px;
      border-bottom: 1.5px solid #B87818;
      display: inline-flex;
      align-items: center;
      gap: 3px;
    }
    .term-zh {
      font-weight: 500;
      color: #6B5F54;
      margin-left: 2px;
    }
    .phonetic-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.82em;
      color: #A99C8E;
      margin-left: 4px;
    }
  `;
  document.head.appendChild(style);

  // 2. 語音合成核心
  var synth = window.speechSynthesis;
  var currentUtterance = null;
  var speakingBtn = null;
  var selectedVoice = null;

  function initVoice() {
    if (!synth) return;
    var voices = synth.getVoices();
    if (!voices || voices.length === 0) return;

    // 優先選取純正美式/英式自然人聲
    var preferred = voices.filter(function (v) {
      return v.lang.indexOf('en') === 0 && (
        v.name.indexOf('Google') >= 0 ||
        v.name.indexOf('Natural') >= 0 ||
        v.name.indexOf('Samantha') >= 0 ||
        v.name.indexOf('Jenny') >= 0 ||
        v.name.indexOf('Guy') >= 0 ||
        v.name.indexOf('Online') >= 0
      );
    });

    if (preferred.length > 0) {
      selectedVoice = preferred[0];
    } else {
      var anyEn = voices.filter(function (v) { return v.lang.indexOf('en') === 0; });
      selectedVoice = anyEn[0] || voices[0];
    }
  }

  initVoice();
  if (synth && synth.onvoiceschanged !== undefined) {
    synth.onvoiceschanged = initVoice;
  }

  // 專有名詞縮寫讀音特化處理
  function cleanForSpeech(raw) {
    if (!raw) return '';
    var t = raw;
    // 移除 LaTeX / MathJax
    t = t.replace(/\$\$.+?\$\$/gs, ' ');
    t = t.replace(/\$[^\$]+?\$/g, ' ');
    // 移除中文字符（只朗讀純英文與音標）
    t = t.replace(/[\u4e00-\u9fa5]+/g, ' ');
    // 專有名詞音標或縮寫自然停頓
    t = t.replace(/[\/|\\]+/g, ', ');
    t = t.replace(/[（）()「」、。，；：？！\-_+=*&^%$#@~`><\[\]{}]/g, ' ');
    t = t.replace(/\s+/g, ' ').trim();
    return t;
  }

  function stopSpeech() {
    if (synth) {
      synth.cancel();
    }
    if (speakingBtn) {
      speakingBtn.classList.remove('spk-playing');
      speakingBtn.innerHTML = '🔊';
      speakingBtn = null;
    }
  }

  function speakEn(text, btn, rate) {
    if (!synth) {
      alert('您的瀏覽器不支援語音合成功能，建議使用最新版 Chrome、Edge 或 Safari。');
      return;
    }

    var cleanText = cleanForSpeech(text);
    if (!cleanText) return;

    // 若同一按鈕正在發音，點擊則停止
    if (speakingBtn === btn && synth.speaking) {
      stopSpeech();
      return;
    }

    stopSpeech();

    var utterance = new SpeechSynthesisUtterance(cleanText);
    if (selectedVoice) utterance.voice = selectedVoice;
    utterance.lang = (selectedVoice && selectedVoice.lang) || 'en-US';
    utterance.rate = rate || 0.85; // 舒適清晰的學習語速
    utterance.pitch = 1.02;

    if (btn) {
      speakingBtn = btn;
      speakingBtn.classList.add('spk-playing');
      speakingBtn.innerHTML = '⏹';
    }

    utterance.onend = function () {
      stopSpeech();
    };

    utterance.onerror = function (e) {
      if (e.error !== 'canceled' && e.error !== 'interrupted') {
        console.warn('TTS 發音中斷:', e.error);
      }
      stopSpeech();
    };

    synth.speak(utterance);
  }

  // 3. 劃詞反白選取朗讀浮動氣泡
  var bubble = document.createElement('div');
  bubble.id = 'tts-selection-bubble';
  bubble.innerHTML = '🔊 朗讀發音';
  document.body.appendChild(bubble);

  var selectedTextCache = '';

  document.addEventListener('mouseup', function (e) {
    if (e.target.closest('#tts-selection-bubble')) return;

    var sel = window.getSelection();
    if (!sel || sel.isCollapsed) {
      bubble.style.display = 'none';
      return;
    }

    var text = sel.toString().trim();
    // 檢查選取內容是否包含至少一個英文字母
    if (/[a-zA-Z]/.test(text) && text.length > 0 && text.length < 500) {
      selectedTextCache = text;
      var range = sel.getRangeAt(0);
      var rect = range.getBoundingClientRect();

      var top = rect.top + window.scrollY - 38;
      var left = rect.left + window.scrollX + (rect.width / 2) - 45;

      bubble.style.top = Math.max(10, top) + 'px';
      bubble.style.left = Math.max(10, left) + 'px';
      bubble.style.display = 'block';
    } else {
      bubble.style.display = 'none';
    }
  });

  bubble.addEventListener('click', function (e) {
    e.stopPropagation();
    if (selectedTextCache) {
      speakEn(selectedTextCache, null, 0.85);
    }
    bubble.style.display = 'none';
  });

  document.addEventListener('mousedown', function (e) {
    if (!e.target.closest('#tts-selection-bubble')) {
      bubble.style.display = 'none';
    }
  });

  // 4. 自動為含 data-speak 或 .spk-btn 的元素綁定事件
  function bindSpeakButtons() {
    document.querySelectorAll('.spk-btn').forEach(function (btn) {
      if (btn._bound) return;
      btn._bound = true;
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        var txt = btn.getAttribute('data-speak') || btn.previousElementSibling?.textContent || btn.parentElement?.textContent;
        speakEn(txt, btn);
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bindSpeakButtons);
  } else {
    bindSpeakButtons();
  }

  // 導出全局介面
  window.speakEn = speakEn;
  window.stopSpeech = stopSpeech;
  window.bindSpeakButtons = bindSpeakButtons;
})();
