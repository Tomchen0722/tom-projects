/**
 * 臺灣證券交易所 (TWSE) 備考系統 - 雙語發音引擎 (Web Speech API TTS)
 * 提供精確之美式/英式英語發音、速度調節與視覺發音狀態反饋
 */

(function () {
  'use strict';

  class SpeechManager {
    constructor() {
      this.synth = window.speechSynthesis || null;
      this.voices = [];
      this.rate = 0.95; // 稍微放慢以聽清金融 IT 專有名詞
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
      // 優先選取 Google, Samantha, Daniel, 或是微軟優質英文語音
      const targetLang = langCode.toLowerCase();
      let match = this.voices.find(v => v.lang.toLowerCase().replace('_', '-').startsWith(targetLang) && (v.name.includes('Natural') || v.name.includes('Premium') || v.name.includes('Google') || v.name.includes('Samantha')));
      if (!match) {
        match = this.voices.find(v => v.lang.toLowerCase().replace('_', '-').startsWith('en'));
      }
      return match || null;
    }

    /**
     * 朗讀文字
     * @param {string} text 要朗讀的英文術語或句子
     * @param {HTMLElement|null} triggerButton 觸發朗讀的按鈕元素 (用於加上動畫效果)
     */
    speak(text, triggerButton = null) {
      if (!this.synth) {
        console.warn('此瀏覽器不支援 Web Speech API 語音合成');
        return;
      }

      // 淨化字串 (去除括號內中文或特殊符號)
      let cleanText = text.trim();
      // 如果包含括號，抽取第一個純英文部分
      const englishMatch = cleanText.match(/[a-zA-Z0-9\s\-_\.\/\+]{2,}/);
      if (englishMatch && englishMatch[0].length >= 2) {
        cleanText = englishMatch[0].trim();
      }

      if (!cleanText) return;

      // 若正在朗讀相同按鈕，則停止
      if (this.isSpeaking && this.currentBtn === triggerButton) {
        this.stop();
        return;
      }

      this.stop();

      const utterance = new SpeechSynthesisUtterance(cleanText);
      const voice = this.getVoice(this.lang);
      if (voice) {
        utterance.voice = voice;
      }
      utterance.lang = this.lang;
      utterance.rate = this.rate;
      utterance.pitch = this.pitch;

      if (triggerButton) {
        this.currentBtn = triggerButton;
        triggerButton.classList.add('speaking');
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
        this.currentBtn.classList.remove('speaking');
        this.currentBtn = null;
      }
    }
  }

  // 註冊全域實例
  window.ttsEngine = new SpeechManager();

  // 事件委派：點擊任何帶有 .btn-speech 或 data-speak 屬性的元素自動播放發音
  document.addEventListener('click', (e) => {
    const btn = e.target.closest('.btn-speech, [data-speak]');
    if (btn) {
      e.preventDefault();
      e.stopPropagation();
      const textToSpeak = btn.getAttribute('data-speak') || btn.getAttribute('data-word') || btn.innerText;
      window.ttsEngine.speak(textToSpeak, btn);
    }
  });
})();
