/**
 * MathJax 3 Configuration & Loader for 公職資訊處理國考教材
 * 自動渲染 $...$ 行內公式與 $$...$$ 區塊公式
 * 支援本地離線 (assets/vendor/mathjax/tex-svg.js) 與線上 CDN 備援
 */
(function () {
  'use strict';

  // 1. MathJax 配置 (必須在 MathJax 主程式載入前設定)
  window.MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']],
      displayMath: [['$$', '$$'], ['\\[', '\\]']],
      processEscapes: true,
      processEnvironments: true
    },
    svg: {
      fontCache: 'global'
    },
    options: {
      skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
    }
  };

  // 2. 解析當前 math-config.js 的基礎路徑，以取得 vendor/mathjax/tex-svg.js
  var currentScript = document.currentScript || (function () {
    var scripts = document.getElementsByTagName('script');
    return scripts[scripts.length - 1];
  })();

  var baseUrl = '';
  if (currentScript && currentScript.src) {
    baseUrl = currentScript.src.substring(0, currentScript.src.lastIndexOf('/') + 1);
  }

  var localMathJaxUrl = baseUrl ? baseUrl + 'vendor/mathjax/tex-svg.js' : 'assets/vendor/mathjax/tex-svg.js';
  var cdnMathJaxUrl = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js';

  // 3. 載入 MathJax 主腳本
  var script = document.createElement('script');
  script.id = 'MathJax-script';
  script.async = true;
  script.src = localMathJaxUrl;

  // 萬一本機檔案載入失敗，切換至 CDN
  script.onerror = function () {
    console.warn('[MathJax] 本地 tex-svg.js 載入失敗，切換至 CDN 備援載入。');
    var cdnScript = document.createElement('script');
    cdnScript.id = 'MathJax-script-cdn';
    cdnScript.async = true;
    cdnScript.src = cdnMathJaxUrl;
    document.head.appendChild(cdnScript);
  };

  document.head.appendChild(script);
})();
