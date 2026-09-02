/* 英文發音 — 公職資訊處理國考教材
   1. 提供全域 speakEn(text)：以瀏覽器內建語音朗讀英文，速度放慢以利聽清楚。
   2. 自動掃描頁面中的英文內容（題幹、選項、例句、標了 class="en" 的元素），
      在其後方加上可點擊的 🔊，不需要逐題修改內容。
   瀏覽器不支援語音合成時，不加任何按鈕，頁面照常使用。 */
(function () {
  'use strict';

  if (!('speechSynthesis' in window)) return;

  var speaking = null;

  window.speakEn = function (text, btn) {
    if (!text) return;
    window.speechSynthesis.cancel();
    if (speaking === btn) { speaking = null; return; }   // 再點一次 = 停止
    var u = new SpeechSynthesisUtterance(text);
    u.lang = 'en-US';
    u.rate = 0.75;                                        // 放慢，考生聽得清楚
    u.onend = u.onerror = function () { speaking = null; };
    speaking = btn || null;
    window.speechSynthesis.speak(u);
  };

  /* ---------- 判斷一段文字是否值得發音 ---------- */
  function isEnglish(t) {
    t = (t || '').trim();
    if (t.length < 8) return false;
    var latin = (t.match(/[A-Za-z]/g) || []).length;
    var cjk = (t.match(/[一-鿿]/g) || []).length;
    if (latin < 6) return false;
    return latin > cjk * 2;                               // 英文為主才發音
  }

  function makeBtn(getText) {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'spk';
    b.setAttribute('aria-label', '朗讀英文');
    b.title = '點擊朗讀（再按一次停止）';
    b.textContent = '🔊';
    b.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();                                // 不要觸發外層的作答或展開
      window.speakEn(getText(), b);
    });
    return b;
  }

  /* 取出元素的英文部分：去掉中括號註解與中文句子後的殘留 */
  function englishOf(el) {
    var t = el.textContent || '';
    t = t.replace(/[一-鿿]+/g, ' ');              // 去中文字
    t = t.replace(/[（）「」、。，；：？！]/g, ' ');
    return t.replace(/\s+/g, ' ').trim();
  }

  function attach(el, getText) {
    if (!el || el.dataset.spk) return;
    el.dataset.spk = '1';
    var snapshot = englishOf(el);                         // 先取文字，避免把 🔊 也念出來
    el.appendChild(document.createTextNode(' '));
    el.appendChild(makeBtn(getText || function () { return snapshot; }));
  }

  document.addEventListener('DOMContentLoaded', function () {
    /* ① 明確標記的元素 */
    [].slice.call(document.querySelectorAll('.en')).forEach(function (el) { attach(el); });

    /* ② 題幹與選項 */
    [].slice.call(document.querySelectorAll('.q .stem')).forEach(function (el) {
      if (isEnglish(el.textContent)) attach(el);
    });
    [].slice.call(document.querySelectorAll('.q .ch span')).forEach(function (el) {
      var t = (el.textContent || '').trim();
      if (/^[A-Za-z][A-Za-z\s\-']{2,}$/.test(t)) {         // 單字或片語選項
        var p = el.parentNode;
        if (p && !p.dataset.spk) {
          p.dataset.spk = '1';
          p.appendChild(makeBtn(function () { return t; }));
        }
      }
    });

    /* ③ 詳解與講義中的英文段落（含中譯的那一段不重複掛） */
    [].slice.call(document.querySelectorAll('.ans p, .frame, .hl, .easy')).forEach(function (el) {
      if (el.querySelector('.spk')) return;
      if (isEnglish(el.textContent)) attach(el);
    });
  });
})();
