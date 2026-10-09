/**
 * 臺灣證券交易所 (TWSE) 備考系統 - 雙語發音引擎 (Web Speech API TTS)
 * 1. 提供全局 speakEn(text, btn) / window.ttsEngine.speak(text, btn)：朗讀標準清晰美式英語（en-US，語速 0.88x）。
 * 2. 劃詞選取發音：滑鼠選取任何含英文的文字時，自動浮現「🔊 朗讀英文」氣泡按鈕。
 * 3. 專有名詞自動附加按鈕：自動在「中文 (English Term)」、名詞速查表、題目與選項、講義標題/內文旁插入 🔊 朗讀按鈕。
 * 4. 點擊 <code> 標籤、.vocab-pill 或任何帶有英文的詞彙立即發音。
 * 5. 點擊正在播放之按鈕可即刻停止播放，並具備波紋動畫回饋。
 */

(function () {
  'use strict';

  class SpeechManager {
    constructor() {
      this.synth = window.speechSynthesis || null;
      this.voices = [];
      this.rate = 0.88; // 稍微放慢以聽清金融 IT 專有名詞與縮寫
      this.pitch = 1.0;
      this.lang = 'en-US';
      this.isSpeaking = false;
      this.currentBtn = null;

      if (this.synth) {
        this.initVoices();
        if (typeof speechSynthesis.onvoiceschanged !== 'undefined') {
          speechSynthesis.onvoiceschanged = () => this.initVoices();
        }
      }
    }

    initVoices() {
      if (!this.synth) return;
      this.voices = this.synth.getVoices();
    }

    getVoice(langCode = 'en-US') {
      if (!this.voices.length) this.initVoices();
      const targetLang = langCode.toLowerCase();
      let match = this.voices.find(v => 
        v.lang.toLowerCase().replace('_', '-').startsWith(targetLang) && 
        (v.name.includes('Natural') || v.name.includes('Premium') || v.name.includes('Google') || v.name.includes('Samantha') || v.name.includes('Jenny'))
      );
      if (!match) {
        match = this.voices.find(v => v.lang.toLowerCase().replace('_', '-').startsWith('en'));
      }
      return match || null;
    }

    cleanText(raw) {
      if (!raw) return '';
      let t = raw;
      // 移除 LaTeX / MathJax
      t = t.replace(/\$\$.+?\$\$/gs, ' ');
      t = t.replace(/\$[^\$]+?\$/g, ' ');
      t = t.replace(/\\\w+(\{[^}]*\})?/g, ' ');
      // 移除中文字元與全形標點
      t = t.replace(/[\u4e00-\u9fa5]+/g, ' ');
      // 特殊符號轉停頓
      t = t.replace(/[\/|\\]+/g, ', ');
      t = t.replace(/[（）()「」、。，；：？！\-_+=*&^%$#@~`><\[\]{}]/g, ' ');
      t = t.replace(/\s+/g, ' ').trim();
      return t;
    }

    speak(text, triggerButton = null) {
      if (!this.synth) {
        console.warn('此瀏覽器不支援 Web Speech API 語音合成');
        return;
      }

      const clean = this.cleanText(text);
      if (!clean) return;

      // 若正在朗讀相同按鈕，則停止播放
      if (this.isSpeaking && this.currentBtn === triggerButton) {
        this.stop();
        return;
      }

      this.stop();

      const utterance = new SpeechSynthesisUtterance(clean);
      const voice = this.getVoice(this.lang);
      if (voice) {
        utterance.voice = voice;
      }
      utterance.lang = this.lang;
      utterance.rate = this.rate;
      utterance.pitch = this.pitch;

      if (triggerButton) {
        this.currentBtn = triggerButton;
        triggerButton.classList.add('speaking', 'spk-playing');
      }

      this.isSpeaking = true;

      utterance.onend = () => {
        this.cleanupState();
      };

      utterance.onerror = (e) => {
        console.debug('TTS playback event:', e);
        this.cleanupState();
      };

      this.synth.speak(utterance);
    }

    stop() {
      if (this.synth) {
        this.synth.cancel();
      }
      this.cleanupState();
    }

    cleanupState() {
      this.isSpeaking = false;
      if (this.currentBtn) {
        this.currentBtn.classList.remove('speaking', 'spk-playing');
        this.currentBtn = null;
      }
    }
  }

  // 註冊全域實例
  const tts = new SpeechManager();
  window.ttsEngine = tts;
  window.speakEn = function (text, btn) {
    tts.speak(text, btn);
  };

  // 建立 🔊 發音按鈕 DOM
  function createSpkButton(getText, title) {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'spk-btn';
    btn.setAttribute('aria-label', '朗讀英文');
    btn.title = title || '點擊朗讀英文（再按一次停止）';
    btn.innerHTML = '🔊';
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      const t = typeof getText === 'function' ? getText() : getText;
      window.speakEn(t, btn);
    });
    return btn;
  }

  // 劃詞選取發音按鈕 (Selection Floating Bubble)
  function initSelectionBubble() {
    let bubble = document.getElementById('tts-selection-bubble');
    if (!bubble) {
      bubble = document.createElement('div');
      bubble.id = 'tts-selection-bubble';
      bubble.innerHTML = '🔊 朗讀英文';
      document.body.appendChild(bubble);
    }

    let selectedText = '';

    function handleSelection() {
      setTimeout(function () {
        const selection = window.getSelection();
        const text = selection.toString().trim();
        const letters = (text.match(/[A-Za-z]/g) || []).length;

        // 若選取的文字包含至少 2 個英文字母
        if (text && letters >= 2 && selection.rangeCount > 0) {
          selectedText = text;
          const range = selection.getRangeAt(0);
          const rect = range.getBoundingClientRect();

          if (rect.width > 0 && rect.height > 0) {
            const top = rect.top + window.scrollY - 38;
            const left = rect.left + window.scrollX + (rect.width / 2) - 45;

            bubble.style.top = (top > 0 ? top : 10) + 'px';
            bubble.style.left = (left > 10 ? left : 10) + 'px';
            bubble.style.display = 'block';
            return;
          }
        }
        bubble.style.display = 'none';
      }, 30);
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

  // 自動掃描並為括號英文、程式碼標籤、表格英文附加發音
  function autoAttachSpeechButtons() {
    // 包含講義主體 (#lectureBody, .notes-body, .notes-content-card)、申論、題庫各容器
    const candidateContainers = document.querySelectorAll(
      '#lectureBody p, #lectureBody li, #lectureBody h2, #lectureBody h3, #lectureBody h4, #lectureBody td, #lectureBody th, #lectureBody .callout-box, ' +
      '.notes-body p, .notes-body li, .notes-body h2, .notes-body h3, .notes-body h4, .notes-body td, .notes-body th, ' +
      '.lecture-content p, .lecture-content li, .lecture-content h2, .lecture-content h3, .lecture-content td, ' +
      '.essay-prompt, .essay-model-answer p, .essay-model-answer li, .essay-model-answer td, .essay-detailed-panel p, .essay-detailed-panel li, .essay-examiner-tips, .exam-prediction-box, ' +
      '.q-stem, .option-text, .option-expl-desc'
    );

    const parenRegex = /([\(（]([A-Za-z][A-Za-z0-9\s\-_/\'.:]{1,60})[\)）])/g;

    candidateContainers.forEach(function (container) {
      if (container.closest('pre') || container.dataset.spkScanned) return;
      container.dataset.spkScanned = '1';

      const walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT, null, false);
      const textNodes = [];
      let node;
      while ((node = walker.nextNode())) {
        if (node.parentNode && (node.parentNode.nodeName === 'PRE' || node.parentNode.classList.contains('spk-btn') || node.parentNode.classList.contains('vocab-pill'))) {
          continue;
        }
        textNodes.push(node);
      }

      textNodes.forEach(function (textNode) {
        const text = textNode.nodeValue;
        if (!text) return;
        parenRegex.lastIndex = 0;

        if (parenRegex.test(text)) {
          parenRegex.lastIndex = 0;
          const frag = document.createDocumentFragment();
          let lastIndex = 0;
          let match;
          let found = false;

          while ((match = parenRegex.exec(text)) !== null) {
            const fullMatch = match[1];
            const engTerm = match[2].trim();
            const letterCount = (engTerm.match(/[A-Za-z]/g) || []).length;
            if (letterCount < 2) continue;

            found = true;
            const beforeText = text.substring(lastIndex, match.index + fullMatch.length);
            frag.appendChild(document.createTextNode(beforeText));

            const btn = createSpkButton(engTerm, '點擊朗讀 ' + engTerm);
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

    // 處理 <code> 標籤中的短英文名詞（如 `DPDK`, `Onload`, `PIM-SSM`, `FIDO2`, `AES-GCM` 等）
    document.querySelectorAll('code').forEach(function (codeEl) {
      if (codeEl.closest('pre') || codeEl.dataset.spkCodeBound) return;
      codeEl.dataset.spkCodeBound = '1';
      const text = (codeEl.textContent || '').trim();
      const letters = (text.match(/[A-Za-z]/g) || []).length;
      if (letters >= 2 && text.length <= 45 && !text.includes('\n')) {
        codeEl.style.cursor = 'pointer';
        codeEl.classList.add('en-code-speakable');
        codeEl.title = '點擊聆聽英文發音：' + text;
        codeEl.addEventListener('click', function (e) {
          e.stopPropagation();
          window.speakEn(text, codeEl);
        });
      }
    });

    // 處理表格欄位中包含英文的單元格
    document.querySelectorAll('table tbody tr td, table tr td, table tr th').forEach(function (td) {
      if (td.dataset.spkAttached || td.querySelector('.spk-btn') || td.querySelector('.vocab-pill')) return;
      const cellText = (td.textContent || '').trim();
      const englishLetters = (cellText.match(/[A-Za-z]/g) || []).length;
      if (englishLetters >= 3 && cellText.length < 50 && !td.querySelector('button') && !cellText.includes('\n')) {
        td.dataset.spkAttached = '1';
        td.appendChild(createSpkButton(cellText, '點擊朗讀 ' + cellText));
      }
    });
  }

  // 委派點擊現有 .btn-speech, [data-speak], .vocab-pill, .en-term
  document.addEventListener('click', (e) => {
    const btn = e.target.closest('.btn-speech, [data-speak], .vocab-pill, .en-term, .en-code');
    if (btn) {
      e.preventDefault();
      e.stopPropagation();
      const textToSpeak = btn.getAttribute('data-speak') || btn.getAttribute('data-word') || btn.innerText;
      window.speakEn(textToSpeak, btn);
    }
  });

  // 初始化
  function init() {
    initSelectionBubble();
    autoAttachSpeechButtons();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // 全域主動重新掃描 API
  window.refreshSpeechButtons = function () {
    setTimeout(autoAttachSpeechButtons, 40);
  };
})();
