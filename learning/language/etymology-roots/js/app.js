/**
 * 字根字首魔法學院 (EtymoRoots Master)
 * 應用程式核心邏輯控制器
 */

(function () {
  'use strict';

  // 應用程式狀態管理
  const state = {
    currentRootId: "tele", // 預設為使用者指定的首波字首 tele-
    currentTab: "words",   // "words" | "equations" | "grammar" | "article" | "quiz" | "flashcards"
    searchQuery: "",
    bookmarkedWords: JSON.parse(localStorage.getItem("etymo_bookmarks") || "[]"),
    flashcardIndex: 0,
    isFlashcardFlipped: false,
    articleMode: "bilingual", // "bilingual" | "en-only"
    activeSpeakingSentenceIndex: -1,
    // 測驗狀態
    puzzleWordIndex: 0,
    puzzlePlacedMorphemes: [],
    quizScore: { correct: 0, total: 0 }
  };

  // DOM 容器快取
  const dom = {
    rootChipsList: document.getElementById("root-chips-list"),
    searchInput: document.getElementById("search-input"),
    ttsRateSelect: document.getElementById("tts-rate-select"),
    btnFavToggle: document.getElementById("btn-fav-toggle"),
    favCountBadge: document.getElementById("fav-count-badge"),
    viewTabsBar: document.getElementById("view-tabs-bar"),
    tabBtns: document.querySelectorAll(".tab-btn"),
    etymoBannerContainer: document.getElementById("etymo-banner-container"),
    mainTabContent: document.getElementById("main-tab-content")
  };

  /**
   * 初始化入口
   */
  function init() {
    bindGlobalEvents();
    renderNavChips();
    updateFavBadge();
    renderView();
  }

  /**
   * 全域事件綁定
   */
  function bindGlobalEvents() {
    // 標籤頁切換
    if (dom.viewTabsBar) {
      dom.viewTabsBar.addEventListener("click", (e) => {
        const btn = e.target.closest(".tab-btn");
        if (!btn) return;
        state.currentTab = btn.dataset.tab;
        dom.tabBtns.forEach(b => b.classList.toggle("active", b === btn));
        renderView();
      });
    }

    // 搜尋輸入
    if (dom.searchInput) {
      dom.searchInput.addEventListener("input", (e) => {
        state.searchQuery = e.target.value.trim().toLowerCase();
        renderView();
      });
    }

    // 語音播放語速調節
    if (dom.ttsRateSelect) {
      dom.ttsRateSelect.addEventListener("change", (e) => {
        window.etymoTTS.setRate(e.target.value);
      });
    }

    // 收藏過濾切換
    if (dom.btnFavToggle) {
      dom.btnFavToggle.addEventListener("click", () => {
        state.showFavOnly = !state.showFavOnly;
        dom.btnFavToggle.classList.toggle("active", state.showFavOnly);
        renderView();
      });
    }
  }

  /**
   * 取得當前所選字根資料
   */
  function getCurrentRootData() {
    return ETYMO_DATA.find(item => item.id === state.currentRootId) || ETYMO_DATA[0];
  }

  /**
   * 渲染橫向字根字首膠囊列
   */
  function renderNavChips() {
    if (!dom.rootChipsList) return;
    dom.rootChipsList.innerHTML = ETYMO_DATA.map(item => `
      <button class="root-chip ${item.id === state.currentRootId ? 'active' : ''}" data-id="${item.id}" title="${item.etymology}">
        <span>${item.icon}</span>
        <span class="chip-name">${item.name}</span>
        <span class="chip-meaning">${item.originMeaning}</span>
      </button>
    `).join("");

    dom.rootChipsList.querySelectorAll(".root-chip").forEach(btn => {
      btn.addEventListener("click", () => {
        state.currentRootId = btn.dataset.id;
        state.flashcardIndex = 0;
        state.isFlashcardFlipped = false;
        state.puzzleWordIndex = 0;
        state.puzzlePlacedMorphemes = [];
        renderNavChips();
        renderView();
      });
    });
  }

  /**
   * 更新收藏標記數目
   */
  function updateFavBadge() {
    if (dom.favCountBadge) {
      dom.favCountBadge.textContent = state.bookmarkedWords.length;
    }
  }

  /**
   * 切換收藏狀態
   */
  function toggleBookmark(word) {
    const idx = state.bookmarkedWords.indexOf(word);
    if (idx > -1) {
      state.bookmarkedWords.splice(idx, 1);
    } else {
      state.bookmarkedWords.push(word);
    }
    localStorage.setItem("etymo_bookmarks", JSON.stringify(state.bookmarkedWords));
    updateFavBadge();
    renderView();
  }

  /**
   * 主視圖總控渲染
   */
  function renderView() {
    const currentRoot = getCurrentRootData();
    renderBanner(currentRoot);

    switch (state.currentTab) {
      case "words":
        renderWordsTab(currentRoot);
        break;
      case "equations":
        renderEquationsTab(currentRoot);
        break;
      case "grammar":
        renderGrammarTab(currentRoot);
        break;
      case "article":
        renderArticleTab(currentRoot);
        break;
      case "quiz":
        renderQuizTab(currentRoot);
        break;
      case "flashcards":
        renderFlashcardsTab(currentRoot);
        break;
      default:
        renderWordsTab(currentRoot);
    }
  }

  /**
   * 渲染頂部介紹橫幅
   */
  function renderBanner(root) {
    if (!dom.etymoBannerContainer) return;
    dom.etymoBannerContainer.innerHTML = `
      <div class="etymo-banner-card" style="border-left-color: ${root.color};">
        <div class="banner-header">
          <div class="banner-title-area">
            <div class="banner-badge-group">
              <span class="type-pill" style="background: ${root.color}18; color: ${root.color};">${root.typeLabel}</span>
              <span class="phonetic-pill">發音：${root.phonetic}</span>
            </div>
            <h2 class="banner-title">
              <span>${root.icon} ${root.name}</span>
              <span class="zh-meaning">${root.originMeaning}</span>
            </h2>
            <p class="banner-etymology-desc">
              <strong>詞源典故：</strong>${root.etymology}
              <br><strong>核心理念：</strong>${root.summary}
            </p>
          </div>

          <div class="banner-stats">
            <div class="stat-item">
              <div class="stat-number">${root.words.length}</div>
              <div class="stat-label">衍伸核心單字</div>
            </div>
            <div class="stat-item">
              <div class="stat-number">100%</div>
              <div class="stat-label">KK/IPA音標</div>
            </div>
            <div class="stat-item">
              <div class="stat-number">有聲</div>
              <div class="stat-label">TTS 真人發音</div>
            </div>
          </div>
        </div>
      </div>
    `;
  }

  /**
   * 1. 渲染單字庫視圖 (Words Tab)
   */
  function renderWordsTab(root) {
    let words = root.words;

    // 搜尋過濾
    if (state.searchQuery) {
      const q = state.searchQuery;
      words = words.filter(w => 
        w.word.toLowerCase().includes(q) ||
        w.meaning.includes(q) ||
        w.kk.toLowerCase().includes(q) ||
        w.sentence.toLowerCase().includes(q)
      );
    }

    // 收藏過濾
    if (state.showFavOnly) {
      words = words.filter(w => state.bookmarkedWords.includes(w.word));
    }

    if (words.length === 0) {
      dom.mainTabContent.innerHTML = `
        <div style="text-align:center; padding: 60px 20px; color: var(--ink-muted);">
          <div style="font-size: 48px; margin-bottom: 12px;">🔍</div>
          <h3>未找到符合條件的單字</h3>
          <p style="font-size: 14px; margin-top: 6px;">請嘗試更換搜尋關鍵字，或取消收藏篩選。</p>
        </div>
      `;
      return;
    }

    dom.mainTabContent.innerHTML = `
      <div class="words-grid">
        ${words.map(w => renderWordCardHTML(w, root)).join("")}
      </div>
    `;

    bindWordCardEvents();
  }

  /**
   * 單一單字卡片 HTML 生成
   */
  function renderWordCardHTML(w, root) {
    const isBookmarked = state.bookmarkedWords.includes(w.word);

    // 高亮造句中的目標單字
    const regex = new RegExp(`\\b(${w.word}|${w.word}s|${w.word}ed|${w.word}ing|${w.word}es)\\b`, 'gi');
    const highlightedSentence = w.sentence.replace(regex, '<span class="highlight-word">$1</span>');

    return `
      <div class="word-card" data-word="${w.word}">
        <div class="word-card-top">
          <div class="word-heading-wrap">
            <h3 class="word-text">${w.word}</h3>
            <span class="word-pos">${w.pos}</span>
          </div>
          <div class="card-actions">
            <button class="btn-speak btn-speak-word" data-text="${w.word}" title="發音 ${w.word}">
              <span>🔊</span>
            </button>
            <button class="btn-bookmark ${isBookmarked ? 'bookmarked' : ''}" data-word="${w.word}" title="收藏單字">
              <span>${isBookmarked ? '★' : '☆'}</span>
            </button>
          </div>
        </div>

        <!-- 音標列 (KK 與 IPA) -->
        <div class="phonetics-bar">
          <div class="phonetic-tag">
            <span class="phonetic-label">KK</span>
            <span>${w.kk}</span>
          </div>
          <div class="phonetic-tag">
            <span class="phonetic-label">IPA</span>
            <span>${w.ipa}</span>
          </div>
        </div>

        <!-- 繁體中文釋義 -->
        <div class="word-meaning-zh">${w.meaning}</div>

        <!-- 形態拆解公式方塊 -->
        <div class="formula-box">
          <div class="formula-title">
            <span>🧩 詞根構詞公式 (Morphological Equation)</span>
          </div>
          <div class="formula-equation">
            ${w.formula.parts.map((p, idx) => `
              <div class="morpheme-badge ${p.role === 'prefix' || p.role === 'root' ? 'is-root' : ''}">
                <span class="morpheme-text">${p.text}</span>
                <span class="morpheme-meaning">${p.meaning}</span>
              </div>
              ${idx < w.formula.parts.length - 1 ? '<span class="formula-operator">+</span>' : '<span class="formula-operator">➔</span>'}
            `).join("")}
            <div class="morpheme-badge" style="background:#E0F2FE; border-color:#38BDF8;">
              <span class="morpheme-text">${w.word}</span>
              <span class="morpheme-meaning">${w.meaning.split('；')[0]}</span>
            </div>
          </div>
          <div class="formula-result-desc">
            <strong>造詞邏輯：</strong>${w.formula.resultMeaning}
          </div>
        </div>

        <!-- 英文經典例句 -->
        <div class="sentence-box">
          <div class="sentence-header">
            <span class="sentence-label">情境例句 (Authentic Context)</span>
            <button class="btn-speak btn-speak-sentence" data-sentence="${encodeURIComponent(w.sentence)}" title="朗讀整句">
              <span>🔊 聽例句</span>
            </button>
          </div>
          <p class="sentence-en">${highlightedSentence}</p>
          <p class="sentence-zh">${w.sentenceZh}</p>
        </div>

        <!-- 文法解析切換按鈕與抽屜 -->
        <button class="grammar-toggle-btn" data-word="${w.word}">
          <span>🔬 查看此句深度文法解析 (Grammar Breakdown)</span>
          <span class="arrow-icon">▼</span>
        </button>

        <div class="grammar-details-drawer" id="drawer-${w.word}">
          <div class="grammar-pattern-badge">${w.grammar.pattern}</div>

          <div class="grammar-breakdown-list">
            ${w.grammar.breakdown.map(item => `
              <div class="grammar-item">
                <div class="grammar-item-part">${item.part}</div>
                <div class="grammar-item-role">${item.role}</div>
                <div class="grammar-item-note">${item.note}</div>
              </div>
            `).join("")}
          </div>

          <div class="grammar-key-points">
            <h5>💡 關鍵文法要點提煉：</h5>
            <ul>
              ${w.grammar.keyPoints.map(kp => `<li>${kp}</li>`).join("")}
            </ul>
          </div>
        </div>
      </div>
    `;
  }

  /**
   * 綁定單字卡片各項按鈕事件
   */
  function bindWordCardEvents() {
    // 單字發音按鈕
    document.querySelectorAll(".btn-speak-word").forEach(btn => {
      btn.addEventListener("click", () => {
        window.etymoTTS.speak(btn.dataset.text, btn);
      });
    });

    // 例句發音按鈕
    document.querySelectorAll(".btn-speak-sentence").forEach(btn => {
      btn.addEventListener("click", () => {
        const sentence = decodeURIComponent(btn.dataset.sentence);
        window.etymoTTS.speak(sentence, btn);
      });
    });

    // 收藏切換
    document.querySelectorAll(".btn-bookmark").forEach(btn => {
      btn.addEventListener("click", () => {
        toggleBookmark(btn.dataset.word);
      });
    });

    // 文法解析展開/折疊
    document.querySelectorAll(".grammar-toggle-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        const word = btn.dataset.word;
        const drawer = document.getElementById(`drawer-${word}`);
        if (!drawer) return;
        const isShown = drawer.classList.contains("show");
        drawer.classList.toggle("show", !isShown);
        btn.classList.toggle("expanded", !isShown);
        btn.querySelector(".arrow-icon").textContent = isShown ? "▼" : "▲";
      });
    });
  }

  /**
   * 2. 渲染形態拆解矩陣視圖 (Equations Tab)
   */
  function renderEquationsTab(root) {
    dom.mainTabContent.innerHTML = `
      <div style="background:var(--bg-card); border:1px solid var(--border-subtle); border-radius:var(--radius-lg); padding:32px;">
        <div style="margin-bottom:24px;">
          <h2 style="font-family:var(--font-serif); font-size:24px; color:var(--ink-primary);">
            🧩 「${root.name}」形態衍生造字矩陣
          </h2>
          <p style="font-size:14px; color:var(--ink-secondary); margin-top:6px;">
            英語詞彙中 70% 以上的高階字彙皆可透過「字首 (方向/屬性) + 字根 (核心意義) + 字尾 (詞性功能)」直觀拆解組合。掌握形態公式，就能以一當十、成串記憶！
          </p>
        </div>

        <div style="display:flex; flex-direction:column; gap:20px;">
          ${root.words.map(w => `
            <div style="background:var(--bg-sand-warm); border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:20px;">
              <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px; flex-wrap:wrap; gap:10px;">
                <div style="display:flex; align-items:baseline; gap:12px;">
                  <span style="font-family:var(--font-en-serif); font-size:28px; font-weight:700; color:var(--ink-primary);">${w.word}</span>
                  <span style="font-family:var(--font-mono); font-size:13px; color:var(--ink-muted);">${w.kk} | ${w.ipa}</span>
                  <span style="font-size:15px; font-weight:700; color:var(--amber-primary);">${w.meaning}</span>
                </div>
                <button class="btn-speak" onclick="window.etymoTTS.speak('${w.word}', this)" title="發音">🔊</button>
              </div>

              <!-- 大公式列 -->
              <div style="display:flex; align-items:center; flex-wrap:wrap; gap:10px; background:#FFF; padding:16px 20px; border-radius:var(--radius-sm); border:1px dashed rgba(217,119,6,0.3); margin-bottom:12px;">
                ${w.formula.parts.map((p, idx) => `
                  <div style="background:#FFFDF9; border:1px solid var(--border-subtle); border-radius:8px; padding:8px 14px; text-align:center;">
                    <div style="font-family:var(--font-en-serif); font-size:18px; font-weight:700; color:var(--ink-primary);">${p.text}</div>
                    <div style="font-size:12px; color:var(--ink-secondary); margin-top:2px;">${p.meaning}</div>
                  </div>
                  ${idx < w.formula.parts.length - 1 ? '<span style="font-size:18px; font-weight:bold; color:var(--amber-primary);">+</span>' : '<span style="font-size:18px; font-weight:bold; color:var(--amber-primary);">➔</span>'}
                `).join("")}
                <div style="background:#EFF6FF; border:1px solid #93C5FD; border-radius:8px; padding:8px 16px; text-align:center;">
                  <div style="font-family:var(--font-en-serif); font-size:19px; font-weight:700; color:#1D4ED8;">${w.word}</div>
                  <div style="font-size:12px; font-weight:600; color:#1E40AF; margin-top:2px;">${w.meaning.split('；')[0]}</div>
                </div>
              </div>

              <div style="font-size:13px; color:var(--ink-secondary); line-height:1.6;">
                💡 <strong>字義推導過程：</strong>${w.formula.resultMeaning}
              </div>
            </div>
          `).join("")}
        </div>
      </div>
    `;
  }

  /**
   * 3. 渲染文法顯微鏡專區 (Grammar Tab)
   */
  function renderGrammarTab(root) {
    dom.mainTabContent.innerHTML = `
      <div style="background:var(--bg-card); border:1px solid var(--border-subtle); border-radius:var(--radius-lg); padding:32px;">
        <div style="margin-bottom:28px;">
          <h2 style="font-family:var(--font-serif); font-size:24px; color:var(--ink-primary);">
            🔬 「${root.name}」句型結構與深度文法解剖室
          </h2>
          <p style="font-size:14px; color:var(--ink-secondary); margin-top:6px;">
            背誦單字若不能在真實英文句法中靈活運用，只是空中樓閣。本專區為每個衍生單字量身打造權威例句，逐層拆解主詞、及物/不及物謂語動詞、受詞補語、時態語態、分詞構句與進階子句！
          </p>
        </div>

        <div style="display:flex; flex-direction:column; gap:28px;">
          ${root.words.map((w, index) => `
            <div style="background:var(--bg-sand-warm); border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:24px; border-left:6px solid ${root.color};">
              <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
                <div style="display:flex; align-items:baseline; gap:10px;">
                  <span style="font-size:12px; font-family:var(--font-mono); font-weight:bold; background:var(--ink-primary); color:#FFF; padding:2px 8px; border-radius:4px;">#0${index+1}</span>
                  <span style="font-family:var(--font-en-serif); font-size:26px; font-weight:700; color:var(--ink-primary);">${w.word}</span>
                  <span style="font-size:14px; font-weight:600; color:var(--amber-primary);">${w.meaning}</span>
                </div>
                <button class="btn-speak" onclick="window.etymoTTS.speak('${encodeURIComponent(w.sentence)}', this)" title="聽整句朗讀">
                  <span>🔊 聆聽例句</span>
                </button>
              </div>

              <!-- 例句 -->
              <div style="background:#FFF; padding:16px; border-radius:var(--radius-sm); border:1px solid var(--border-subtle); margin-bottom:16px;">
                <p style="font-family:var(--font-en-serif); font-size:19px; font-weight:600; color:var(--ink-primary); line-height:1.45;">
                  ${w.sentence}
                </p>
                <p style="font-size:13px; color:var(--ink-secondary); margin-top:6px;">
                  ${w.sentenceZh}
                </p>
              </div>

              <!-- 句型架構標籤 -->
              <div style="margin-bottom:14px;">
                <span style="font-family:var(--font-mono); font-size:12px; font-weight:600; background:#EFF6FF; color:#1D4ED8; padding:5px 12px; border-radius:4px; border:1px solid #BFDBFE;">
                  句型架構：${w.grammar.pattern}
                </span>
              </div>

              <!-- 句法成分切片表格 -->
              <div style="display:flex; flex-direction:column; gap:8px; margin-bottom:16px;">
                ${w.grammar.breakdown.map(item => `
                  <div style="display:grid; grid-template-columns: 220px 140px 1fr; gap:12px; background:#FFF; padding:8px 14px; border-radius:6px; font-size:13px; align-items:center; border:1px solid var(--border-subtle);">
                    <div style="font-family:var(--font-en-serif); font-weight:700; color:var(--ink-primary);">${item.part}</div>
                    <div style="font-weight:700; color:var(--amber-primary);">${item.role}</div>
                    <div style="color:var(--ink-secondary); line-height:1.4;">${item.note}</div>
                  </div>
                `).join("")}
              </div>

              <!-- 核心文法考點 -->
              <div style="background:#FFFDF9; border:1px dashed rgba(217,119,6,0.3); border-radius:6px; padding:12px 16px;">
                <h5 style="font-size:13px; font-weight:700; color:var(--ink-primary); margin-bottom:6px;">💡 句型精萃與高分考點：</h5>
                <ul style="padding-left:18px; font-size:13px; color:var(--ink-secondary); line-height:1.6;">
                  ${w.grammar.keyPoints.map(kp => `<li>${kp}</li>`).join("")}
                </ul>
              </div>
            </div>
          `).join("")}
        </div>
      </div>
    `;
  }

  /**
   * 4. 渲染主題篇章小短文視圖 (Article Tab)
   */
  function renderArticleTab(root) {
    const art = root.article;
    if (!art) {
      dom.mainTabContent.innerHTML = `<p>此分類暫未生成文章。</p>`;
      return;
    }

    // 將所有英文句子切出，供有聲逐句朗讀使用
    const allSentences = [];
    art.paragraphs.forEach(p => {
      const sArr = p.en.match(/[^.!?]+[.!?]+/g) || [p.en];
      sArr.forEach(s => allSentences.push(s.trim()));
    });

    dom.mainTabContent.innerHTML = `
      <div class="article-reader-container">
        <!-- 篇章頂部資訊 -->
        <div class="article-header">
          <div>
            <h2 class="article-title-en">${art.title}</h2>
            <h3 class="article-title-zh">${art.titleZh}</h3>
            <p class="article-intro">${art.intro}</p>
          </div>

          <div class="article-toolbar">
            <button class="btn-article-play" id="btn-play-whole-article">
              <span id="play-article-icon">▶</span>
              <span id="play-article-text">全文有聲伴讀</span>
            </button>

            <div class="toggle-mode-chips">
              <button class="mode-chip ${state.articleMode === 'bilingual' ? 'active' : ''}" data-mode="bilingual">雙語對照</button>
              <button class="mode-chip ${state.articleMode === 'en-only' ? 'active' : ''}" data-mode="en-only">英文純享</button>
            </div>
          </div>
        </div>

        <!-- 篇章本文段落 -->
        <div class="article-body" id="article-body-content">
          ${art.paragraphs.map((p, pIdx) => {
            // 切割為句子 span
            const sentences = p.en.match(/[^.!?]+[.!?]+/g) || [p.en];
            const sentenceSpans = sentences.map((s, sIdx) => {
              // 高亮當前根詞
              let annotated = s;
              root.words.forEach(w => {
                const reg = new RegExp(`\\b(${w.word}|${w.word}s|${w.word}ed|${w.word}ing|${w.word}es)\\b`, 'gi');
                annotated = annotated.replace(reg, `<span class="article-word-highlight" title="${w.word} (${w.meaning})">$1</span>`);
              });
              return `<span class="sentence-span" data-p="${pIdx}" data-s="${sIdx}" title="點擊朗讀此句">${annotated}</span>`;
            }).join(" ");

            return `
              <div class="article-paragraph">
                <div class="para-en">${sentenceSpans}</div>
                ${state.articleMode === 'bilingual' ? `<div class="para-zh">${p.zh}</div>` : ''}
              </div>
            `;
          }).join("")}
        </div>

        <!-- 篇章閱讀測驗區 -->
        <div class="comprehension-section">
          <h4 class="comprehension-title">
            <span>📝 篇章閱讀理解檢測 (Comprehension Check)</span>
          </h4>
          <div class="quiz-list">
            ${art.comprehensionQuestions.map((qItem, qIdx) => `
              <div class="quiz-card" data-qidx="${qIdx}">
                <p class="quiz-q-en">Q${qIdx+1}: ${qItem.q}</p>
                <p class="quiz-q-zh">${qItem.qZh}</p>
                <div class="quiz-options-list">
                  ${qItem.options.map((opt, optIdx) => `
                    <button class="quiz-opt-btn" data-qidx="${qIdx}" data-optidx="${optIdx}">
                      ${opt}
                    </button>
                  `).join("")}
                </div>
                <div class="quiz-explanation" id="q-explain-${qIdx}">
                  <strong>答案解說：</strong>${qItem.explanation}
                </div>
              </div>
            `).join("")}
          </div>
        </div>
      </div>
    `;

    bindArticleEvents(allSentences, art);
  }

  /**
   * 綁定篇章事件
   */
  function bindArticleEvents(allSentences, art) {
    // 朗讀全文按鈕
    const playBtn = document.getElementById("btn-play-whole-article");
    if (playBtn) {
      playBtn.addEventListener("click", () => {
        if (window.etymoTTS.isPlaying) {
          window.etymoTTS.stop();
          playBtn.classList.remove("speaking");
          document.getElementById("play-article-icon").textContent = "▶";
          document.getElementById("play-article-text").textContent = "全文有聲伴讀";
          document.querySelectorAll(".sentence-span").forEach(el => el.classList.remove("active-speaking"));
          return;
        }

        playBtn.classList.add("speaking");
        document.getElementById("play-article-icon").textContent = "⏸";
        document.getElementById("play-article-text").textContent = "停止播放";

        const allSpans = Array.from(document.querySelectorAll(".sentence-span"));

        window.etymoTTS.speakParagraph(
          allSentences,
          (index) => {
            allSpans.forEach((span, i) => {
              span.classList.toggle("active-speaking", i === index);
              if (i === index) {
                span.scrollIntoView({ behavior: "smooth", block: "center" });
              }
            });
          },
          () => {
            playBtn.classList.remove("speaking");
            document.getElementById("play-article-icon").textContent = "▶";
            document.getElementById("play-article-text").textContent = "全文有聲伴讀";
            allSpans.forEach(span => span.classList.remove("active-speaking"));
          }
        );
      });
    }

    // 點擊任一句子立即單句朗讀
    document.querySelectorAll(".sentence-span").forEach(span => {
      span.addEventListener("click", () => {
        const text = span.textContent.trim();
        document.querySelectorAll(".sentence-span").forEach(s => s.classList.remove("active-speaking"));
        span.classList.add("active-speaking");
        window.etymoTTS.speak(text, null, () => {
          span.classList.remove("active-speaking");
        });
      });
    });

    // 雙語 / 英文純享 切換
    document.querySelectorAll(".mode-chip").forEach(btn => {
      btn.addEventListener("click", () => {
        state.articleMode = btn.dataset.mode;
        renderArticleTab(getCurrentRootData());
      });
    });

    // 篇章閱讀測驗選項點擊
    document.querySelectorAll(".quiz-opt-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        const qIdx = parseInt(btn.dataset.qidx, 10);
        const optIdx = parseInt(btn.dataset.optidx, 10);
        const qData = art.comprehensionQuestions[qIdx];
        const card = btn.closest(".quiz-card");

        const allBtns = card.querySelectorAll(".quiz-opt-btn");
        allBtns.forEach((b, idx) => {
          b.disabled = true;
          if (idx === qData.answer) {
            b.classList.add("correct");
          } else if (idx === optIdx) {
            b.classList.add("wrong");
          }
        });

        const explainBox = document.getElementById(`q-explain-${qIdx}`);
        if (explainBox) explainBox.classList.add("show");
      });
    });
  }

  /**
   * 5. 渲染測驗與拼字遊戲 (Quiz Tab)
   */
  function renderQuizTab(root) {
    const currentWord = root.words[state.puzzleWordIndex % root.words.length];
    const correctParts = currentWord.formula.parts.map(p => p.text);

    // 建立選項池 (包含正確語素 + 隨機干擾語素)
    const distractors = ["anti-", "dis-", "un-", "micro-", "graph", "meter", "logy"];
    const pool = [...correctParts];
    distractors.forEach(d => {
      if (!pool.includes(d) && pool.length < 5) pool.push(d);
    });
    // 洗牌
    pool.sort(() => Math.random() - 0.5);

    dom.mainTabContent.innerHTML = `
      <div class="quiz-arena-container">
        <div class="arena-header">
          <h2 class="arena-title">🎯 字根字首組裝拼圖挑戰</h2>
          <p class="arena-desc">請點選下方語素零件，正確拼組出符合定義的單字！</p>
        </div>

        <div class="puzzle-card">
          <div style="font-size:12px; font-weight:700; color:var(--ink-muted); margin-bottom:4px;">
            題目 ${ (state.puzzleWordIndex % root.words.length) + 1 } / ${root.words.length}
          </div>
          <div class="puzzle-target-meaning">
            目標中文釋義：${currentWord.meaning}
          </div>
          <div style="font-family:var(--font-mono); font-size:13px; color:var(--ink-muted); margin-bottom:16px;">
            提示音標：${currentWord.kk} | ${currentWord.ipa}
          </div>

          <!-- 拼裝放置區 -->
          <div class="puzzle-dropzone" id="puzzle-dropzone">
            ${state.puzzlePlacedMorphemes.length === 0 ? '<span style="color:var(--ink-muted); font-size:13px;">點選下方零件進行組裝...</span>' : ''}
            ${state.puzzlePlacedMorphemes.map((m, idx) => `
              <div class="morpheme-draggable" data-idx="${idx}" style="background:#FEF3C7; border-color:#D97706; color:#92400E;">
                ${m} ✕
              </div>
            `).join("")}
          </div>

          <!-- 零件備選池 -->
          <div class="puzzle-options-pool" id="puzzle-options-pool">
            ${pool.map(m => `
              <button class="morpheme-draggable pool-item" data-text="${m}">
                ${m}
              </button>
            `).join("")}
          </div>

          <div style="display:flex; align-items:center; justify-content:center; gap:12px;">
            <button class="btn-check-puzzle" id="btn-check-puzzle">驗證答案</button>
            <button class="fc-nav-btn" id="btn-reset-puzzle">清空重選</button>
            <button class="fc-nav-btn" id="btn-next-puzzle">下一題 ➔</button>
          </div>

          <div id="puzzle-feedback" style="margin-top:16px; font-size:14px; font-weight:bold;"></div>
        </div>
      </div>
    `;

    bindQuizEvents(currentWord, correctParts);
  }

  /**
   * 綁定測驗拼字事件
   */
  function bindQuizEvents(currentWord, correctParts) {
    // 點選零件加入組裝區
    document.querySelectorAll(".pool-item").forEach(btn => {
      btn.addEventListener("click", () => {
        state.puzzlePlacedMorphemes.push(btn.dataset.text);
        renderQuizTab(getCurrentRootData());
      });
    });

    // 點選放置區零件將其移除
    const dropzone = document.getElementById("puzzle-dropzone");
    if (dropzone) {
      dropzone.querySelectorAll(".morpheme-draggable").forEach(el => {
        el.addEventListener("click", () => {
          const idx = parseInt(el.dataset.idx, 10);
          state.puzzlePlacedMorphemes.splice(idx, 1);
          renderQuizTab(getCurrentRootData());
        });
      });
    }

    // 驗證按鈕
    const checkBtn = document.getElementById("btn-check-puzzle");
    const fb = document.getElementById("puzzle-feedback");
    if (checkBtn) {
      checkBtn.addEventListener("click", () => {
        const isMatch = JSON.stringify(state.puzzlePlacedMorphemes) === JSON.stringify(correctParts);
        if (isMatch) {
          fb.style.color = "#059669";
          fb.innerHTML = `🎉 完全正確！組成單字：<strong>${currentWord.word}</strong> (${currentWord.meaning})。`;
          window.etymoTTS.speak(currentWord.word);
        } else {
          fb.style.color = "#DC2626";
          fb.textContent = `❌ 還差一點點！正確語素應為：${correctParts.join(" + ")}。`;
        }
      });
    }

    // 清空重選
    const resetBtn = document.getElementById("btn-reset-puzzle");
    if (resetBtn) {
      resetBtn.addEventListener("click", () => {
        state.puzzlePlacedMorphemes = [];
        renderQuizTab(getCurrentRootData());
      });
    }

    // 下一題
    const nextBtn = document.getElementById("btn-next-puzzle");
    if (nextBtn) {
      nextBtn.addEventListener("click", () => {
        state.puzzleWordIndex++;
        state.puzzlePlacedMorphemes = [];
        renderQuizTab(getCurrentRootData());
      });
    }
  }

  /**
   * 6. 渲染單字翻卡記憶模式 (Flashcards Tab)
   */
  function renderFlashcardsTab(root) {
    const words = root.words;
    const currentWord = words[state.flashcardIndex % words.length];

    dom.mainTabContent.innerHTML = `
      <div class="flashcards-container">
        <div style="font-size:13px; font-weight:700; color:var(--ink-muted);">
          卡片 ${ (state.flashcardIndex % words.length) + 1 } / ${words.length}（點擊卡片翻面）
        </div>

        <div class="flashcard-wrap ${state.isFlashcardFlipped ? 'flipped' : ''}" id="flashcard-card">
          <div class="flashcard-inner">
            <!-- 正面：英文單字、音標、發音 -->
            <div class="flashcard-front">
              <span class="type-pill" style="margin-bottom:12px;">${currentWord.pos}</span>
              <div class="fc-word">${currentWord.word}</div>
              <div class="fc-phonetics">${currentWord.kk} &nbsp;|&nbsp; ${currentWord.ipa}</div>
              <button class="btn-speak" id="btn-fc-speak" style="margin-bottom:16px;">🔊 發音</button>
              <div class="fc-hint">💡 點擊卡片查看繁中釋義與形態公式</div>
            </div>

            <!-- 背面：繁中釋義、公式、例句 -->
            <div class="flashcard-back">
              <div class="fc-meaning">${currentWord.meaning}</div>
              <div class="fc-formula">
                ${currentWord.formula.parts.map(p => `${p.text} (${p.meaning})`).join(" + ")}
              </div>
              <div style="font-size:13px; color:var(--ink-secondary); line-height:1.5; background:var(--bg-card-sub); padding:10px 14px; border-radius:8px;">
                "${currentWord.sentence}"
              </div>
              <div class="fc-hint" style="margin-top:16px;">點擊翻回正面</div>
            </div>
          </div>
        </div>

        <!-- 導航控制列 -->
        <div class="flashcard-nav">
          <button class="fc-nav-btn" id="btn-fc-prev">◀ 上一張</button>
          <button class="fc-nav-btn" id="btn-fc-flip">🔄 翻轉卡片</button>
          <button class="fc-nav-btn" id="btn-fc-next">下一張 ▶</button>
        </div>
      </div>
    `;

    bindFlashcardEvents(currentWord, words.length);
  }

  /**
   * 綁定翻卡事件
   */
  function bindFlashcardEvents(currentWord, totalWords) {
    const card = document.getElementById("flashcard-card");
    const flipBtn = document.getElementById("btn-fc-flip");
    const prevBtn = document.getElementById("btn-fc-prev");
    const nextBtn = document.getElementById("btn-fc-next");
    const speakBtn = document.getElementById("btn-fc-speak");

    const toggleFlip = () => {
      state.isFlashcardFlipped = !state.isFlashcardFlipped;
      card.classList.toggle("flipped", state.isFlashcardFlipped);
    };

    if (card) card.addEventListener("click", toggleFlip);
    if (flipBtn) flipBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      toggleFlip();
    });

    if (speakBtn) speakBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      window.etymoTTS.speak(currentWord.word, speakBtn);
    });

    if (prevBtn) prevBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      state.flashcardIndex = (state.flashcardIndex - 1 + totalWords) % totalWords;
      state.isFlashcardFlipped = false;
      renderFlashcardsTab(getCurrentRootData());
    });

    if (nextBtn) nextBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      state.flashcardIndex = (state.flashcardIndex + 1) % totalWords;
      state.isFlashcardFlipped = false;
      renderFlashcardsTab(getCurrentRootData());
    });
  }

  // 啟動應用程式
  document.addEventListener("DOMContentLoaded", init);

})();
