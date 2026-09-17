/**
 * 相容層：轉發至 assets/tts.js
 * 確保任何引用 speak.js 的頁面均能無縫享受升級後的 TTS 功能
 */
(function () {
  'use strict';
  // 若已由 tts.js 初始化，直接沿用
  if (window.speakEn) return;

  window.speakEn = function (text, btn) {
    if (!('speechSynthesis' in window)) return;
    if (!text) return;
    window.speechSynthesis.cancel();
    var u = new SpeechSynthesisUtterance(text);
    u.lang = 'en-US';
    u.rate = 0.82;
    window.speechSynthesis.speak(u);
  };
})();
