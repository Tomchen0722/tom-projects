/**
 * OmniSearch — 前端互動引擎
 * 具備即時搜尋、開放補全建議、鍵盤導覽、語音辨識、AI 概覽、知識圖譜、閱讀模式速覽與收藏管理。
 */

(function () {
  'use strict';

  // ==========================================
  // 全域狀態 (State)
  // ==========================================
  const state = {
    query: '',
    category: 'all',
    page: 1,
    timeFilter: 'all',
    langFilter: 'tw',
    history: JSON.parse(localStorage.getItem('omni_history') || '[]'),
    bookmarks: JSON.parse(localStorage.getItem('omni_bookmarks') || '[]'),
    theme: localStorage.getItem('omni_theme') || 'light',
    activeSuggestIdx: -1,
    speechRecognition: null,
    isListening: false,
    suggestTimer: null,
    isClientMode: false,
  };

  // ==========================================
  // DOM 元素快取 (Elements)
  // ==========================================
  const el = {
    html: document.documentElement,
    homeView: document.getElementById('homeView'),
    resultsView: document.getElementById('resultsView'),

    // Home
    homeSearchInput: document.getElementById('homeSearchInput'),
    homeSearchBox: document.getElementById('homeSearchBox'),
    homeSearchBtn: document.getElementById('homeSearchBtn'),
    homeLuckyBtn: document.getElementById('homeLuckyBtn'),
    homeClearBtn: document.getElementById('homeClearBtn'),
    homeVoiceBtn: document.getElementById('homeVoiceBtn'),
    homeSuggestDropdown: document.getElementById('homeSuggestDropdown'),
    trendingChips: document.getElementById('trendingChips'),
    homeThemeToggle: document.getElementById('homeThemeToggle'),
    homeBookmarksBtn: document.getElementById('homeBookmarksBtn'),
    homeBookmarkCount: document.getElementById('homeBookmarkCount'),
    homeModeBadge: document.getElementById('homeModeBadge'),

    // Results Header
    resultsMiniLogo: document.getElementById('resultsMiniLogo'),
    resultsModeBadge: document.getElementById('resultsModeBadge'),
    headerSearchInput: document.getElementById('headerSearchInput'),
    headerSearchBox: document.getElementById('headerSearchBox'),
    headerSearchBtn: document.getElementById('headerSearchBtn'),
    headerClearBtn: document.getElementById('headerClearBtn'),
    headerVoiceBtn: document.getElementById('headerVoiceBtn'),
    headerSuggestDropdown: document.getElementById('headerSuggestDropdown'),
    resultsThemeToggle: document.getElementById('resultsThemeToggle'),
    resultsBookmarksBtn: document.getElementById('resultsBookmarksBtn'),
    resultsBookmarkCount: document.getElementById('resultsBookmarkCount'),
    categoryTabs: document.getElementById('categoryTabs'),
    toggleToolsBtn: document.getElementById('toggleToolsBtn'),
    toolsBar: document.getElementById('toolsBar'),
    timeFilterSelect: document.getElementById('timeFilterSelect'),
    langFilterSelect: document.getElementById('langFilterSelect'),

    // Results Main
    statsText: document.getElementById('statsText'),
    skeletonLoader: document.getElementById('skeletonLoader'),
    aiOverviewCard: document.getElementById('aiOverviewCard'),
    aiSummaryText: document.getElementById('aiSummaryText'),
    aiTakeawaysList: document.getElementById('aiTakeawaysList'),
    aiSourcesChips: document.getElementById('aiSourcesChips'),
    aiToggleBtn: document.getElementById('aiToggleBtn'),
    aiOverviewBody: document.getElementById('aiOverviewBody'),

    directAnswerCard: document.getElementById('directAnswerCard'),
    directAnswerValue: document.getElementById('directAnswerValue'),
    directAnswerLabel: document.getElementById('directAnswerLabel'),

    organicResultsList: document.getElementById('organicResultsList'),
    newsResultsList: document.getElementById('newsResultsList'),
    imagesResultsGrid: document.getElementById('imagesResultsGrid'),
    peopleAskCard: document.getElementById('peopleAskCard'),
    peopleAskAccordion: document.getElementById('peopleAskAccordion'),
    relatedSearchesBox: document.getElementById('relatedSearchesBox'),
    relatedChips: document.getElementById('relatedChips'),

    paginationContainer: document.getElementById('paginationContainer'),
    paginationPages: document.getElementById('paginationPages'),
    oRepeatLetters: document.getElementById('oRepeatLetters'),

    // Knowledge Card (Right Side)
    knowledgePanel: document.getElementById('knowledgePanel'),
    kpImageWrap: document.getElementById('kpImageWrap'),
    kpImage: document.getElementById('kpImage'),
    kpTitle: document.getElementById('kpTitle'),
    kpSubtitle: document.getElementById('kpSubtitle'),
    kpExtract: document.getElementById('kpExtract'),
    kpFacts: document.getElementById('kpFacts'),
    kpReadMore: document.getElementById('kpReadMore'),

    // Modals
    readerModal: document.getElementById('readerModal'),
    readerModalTitle: document.getElementById('readerModalTitle'),
    readerModalDomain: document.getElementById('readerModalDomain'),
    readerModalBody: document.getElementById('readerModalBody'),
    readerOpenExternal: document.getElementById('readerOpenExternal'),
    readerCloseBtn: document.getElementById('readerCloseBtn'),

    bookmarksDrawerBackdrop: document.getElementById('bookmarksDrawerBackdrop'),
    bookmarksCloseBtn: document.getElementById('bookmarksCloseBtn'),
    bookmarksList: document.getElementById('bookmarksList'),
    drawerCountText: document.getElementById('drawerCountText'),
    clearAllBookmarksBtn: document.getElementById('clearAllBookmarksBtn'),

    lightboxModal: document.getElementById('lightboxModal'),
    lightboxImg: document.getElementById('lightboxImg'),
    lightboxTitle: document.getElementById('lightboxTitle'),
    lightboxDesc: document.getElementById('lightboxDesc'),
    lightboxSourceLink: document.getElementById('lightboxSourceLink'),
    lightboxDownloadBtn: document.getElementById('lightboxDownloadBtn'),
    lightboxCloseBtn: document.getElementById('lightboxCloseBtn'),

    voiceModal: document.getElementById('voiceModal'),
    voiceStatusTitle: document.getElementById('voiceStatusTitle'),
    voiceTranscript: document.getElementById('voiceTranscript'),
    voiceCloseBtn: document.getElementById('voiceCloseBtn'),

    toastNotification: document.getElementById('toastNotification'),
  };

  // ==========================================
  // 初始化 (Initialization)
  // ==========================================
  async function init() {
    applyTheme(state.theme);
    updateBookmarkBadge();
    bindEvents();
    initSpeechRecognition();
    await detectBackend();

    // 檢查網址參數是否帶有搜尋 query (支援重新整理或外連)
    const params = new URLSearchParams(window.location.search);
    const q = params.get('q');
    const cat = params.get('cat') || 'all';
    const page = parseInt(params.get('page') || '1', 10);

    if (q) {
      executeSearch(q, cat, page, false);
    }
  }

  // ==========================================
  // 後端與連線模式檢測 (Backend Detection)
  // ==========================================
  async function detectBackend() {
    if (window.location.protocol === 'file:' || window.location.hostname.endsWith('github.io')) {
      setClientMode(true);
      return false;
    }
    try {
      const ctrl = new AbortController();
      const tid = setTimeout(() => ctrl.abort(), 1200);
      const res = await fetch('/health', { signal: ctrl.signal });
      clearTimeout(tid);
      if (res.ok) {
        setClientMode(false);
        return true;
      }
    } catch (e) {}
    setClientMode(true);
    return false;
  }

  function setClientMode(enabled) {
    state.isClientMode = enabled;
    const badgeText = enabled ? '⚡ 純前端免伺服器 (直接線上用)' : '🟢 本機/雲端 API 模式';
    if (el.homeModeBadge) {
      el.homeModeBadge.textContent = badgeText;
      el.homeModeBadge.className = 'mode-badge ' + (enabled ? 'client-mode' : '');
    }
    if (el.resultsModeBadge) {
      el.resultsModeBadge.textContent = enabled ? '⚡ 免伺服器' : '🟢 API 模式';
      el.resultsModeBadge.className = 'mode-badge ' + (enabled ? 'client-mode' : '');
    }
  }

  // ==========================================
  // 主題切換 (Theme Engine)
  // ==========================================
  function applyTheme(theme) {
    state.theme = theme;
    el.html.setAttribute('data-theme', theme);
    localStorage.setItem('omni_theme', theme);
    const icon = theme === 'dark' ? '☀️' : '🌙';
    if (el.homeThemeToggle) el.homeThemeToggle.querySelector('.theme-icon').textContent = icon;
    if (el.resultsThemeToggle) el.resultsThemeToggle.querySelector('.theme-icon').textContent = icon;
  }

  function toggleTheme() {
    const nextTheme = state.theme === 'dark' ? 'light' : 'dark';
    applyTheme(nextTheme);
    showToast(nextTheme === 'dark' ? '已切換為深色模式' : '已切換為淺色模式');
  }

  // ==========================================
  // Toast 訊息提示
  // ==========================================
  let toastTimer = null;
  function showToast(msg) {
    if (!el.toastNotification) return;
    el.toastNotification.textContent = msg;
    el.toastNotification.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      el.toastNotification.classList.remove('show');
    }, 2400);
  }

  // ==========================================
  // 事件綁定 (Event Listeners)
  // ==========================================
  function bindEvents() {
    // 主題按鈕
    if (el.homeThemeToggle) el.homeThemeToggle.addEventListener('click', toggleTheme);
    if (el.resultsThemeToggle) el.resultsThemeToggle.addEventListener('click', toggleTheme);

    // 收藏夾抽屜
    if (el.homeBookmarksBtn) el.homeBookmarksBtn.addEventListener('click', openBookmarksDrawer);
    if (el.resultsBookmarksBtn) el.resultsBookmarksBtn.addEventListener('click', openBookmarksDrawer);
    if (el.bookmarksCloseBtn) el.bookmarksCloseBtn.addEventListener('click', closeBookmarksDrawer);
    if (el.bookmarksDrawerBackdrop) {
      el.bookmarksDrawerBackdrop.addEventListener('click', (e) => {
        if (e.target === el.bookmarksDrawerBackdrop) closeBookmarksDrawer();
      });
    }
    if (el.clearAllBookmarksBtn) el.clearAllBookmarksBtn.addEventListener('click', clearAllBookmarks);

    // 回首頁 Mini Logo
    if (el.resultsMiniLogo) {
      el.resultsMiniLogo.addEventListener('click', (e) => {
        e.preventDefault();
        showHomeView();
      });
    }

    // 首頁搜尋事件
    if (el.homeSearchBtn) {
      el.homeSearchBtn.addEventListener('click', () => {
        const q = el.homeSearchInput.value.trim();
        if (q) executeSearch(q, 'all', 1, true);
      });
    }

    if (el.homeLuckyBtn) {
      el.homeLuckyBtn.addEventListener('click', () => {
        const q = el.homeSearchInput.value.trim() || '臺灣熱門趨勢';
        executeLucky(q);
      });
    }

    // 關鍵字熱門標籤點擊
    if (el.trendingChips) {
      el.trendingChips.addEventListener('click', (e) => {
        const chip = e.target.closest('.chip');
        if (chip) {
          const q = chip.dataset.q;
          if (q) executeSearch(q, 'all', 1, true);
        }
      });
    }

    // 輸入框按鍵與建議補全
    setupSearchInput(el.homeSearchInput, el.homeClearBtn, el.homeSuggestDropdown, el.homeSearchBox);
    setupSearchInput(el.headerSearchInput, el.headerClearBtn, el.headerSuggestDropdown, el.headerSearchBox);

    // 置頂搜尋按鈕
    if (el.headerSearchBtn) {
      el.headerSearchBtn.addEventListener('click', () => {
        const q = el.headerSearchInput.value.trim();
        if (q) executeSearch(q, state.category, 1, true);
      });
    }

    // 語音搜尋
    if (el.homeVoiceBtn) el.homeVoiceBtn.addEventListener('click', startVoiceSearch);
    if (el.headerVoiceBtn) el.headerVoiceBtn.addEventListener('click', startVoiceSearch);
    if (el.voiceCloseBtn) el.voiceCloseBtn.addEventListener('click', stopVoiceSearch);

    // 分類 Tabs
    if (el.categoryTabs) {
      el.categoryTabs.addEventListener('click', (e) => {
        const btn = e.target.closest('.tab-btn');
        if (!btn || btn.classList.contains('tools-tab-btn')) return;
        const cat = btn.dataset.cat;
        if (cat) {
          switchCategory(cat);
        }
      });
    }

    // 搜尋工具展開開關
    if (el.toggleToolsBtn) {
      el.toggleToolsBtn.addEventListener('click', () => {
        const isHidden = el.toolsBar.style.display === 'none';
        el.toolsBar.style.display = isHidden ? 'flex' : 'none';
        el.toggleToolsBtn.classList.toggle('active', isHidden);
      });
    }

    // 搜尋工具過濾器變更
    if (el.timeFilterSelect) {
      el.timeFilterSelect.addEventListener('change', () => {
        state.timeFilter = el.timeFilterSelect.value;
        if (state.query) executeSearch(state.query, state.category, 1, false);
      });
    }
    if (el.langFilterSelect) {
      el.langFilterSelect.addEventListener('change', () => {
        state.langFilter = el.langFilterSelect.value;
        if (state.query) executeSearch(state.query, state.category, 1, false);
      });
    }

    // AI Overview 展開 / 收合
    if (el.aiToggleBtn) {
      el.aiToggleBtn.addEventListener('click', () => {
        const isBodyHidden = el.aiOverviewBody.style.display === 'none';
        el.aiOverviewBody.style.display = isBodyHidden ? 'block' : 'none';
        el.aiToggleBtn.textContent = isBodyHidden ? '收合摘要' : '展開摘要';
      });
    }

    // 閱讀模式 Modal 關閉
    if (el.readerCloseBtn) el.readerCloseBtn.addEventListener('click', closeReaderModal);
    if (el.readerModal) {
      el.readerModal.addEventListener('click', (e) => {
        if (e.target === el.readerModal) closeReaderModal();
      });
    }

    // 圖片燈箱 Modal 關閉
    if (el.lightboxCloseBtn) el.lightboxCloseBtn.addEventListener('click', closeLightbox);
    if (el.lightboxModal) {
      el.lightboxModal.addEventListener('click', (e) => {
        if (e.target === el.lightboxModal) closeLightbox();
      });
    }

    // 瀏覽器上一頁/下一頁 (popstate)
    window.addEventListener('popstate', (e) => {
      const params = new URLSearchParams(window.location.search);
      const q = params.get('q');
      const cat = params.get('cat') || 'all';
      const page = parseInt(params.get('page') || '1', 10);
      if (q) {
        executeSearch(q, cat, page, false);
      } else {
        showHomeView();
      }
    });

    // 點擊頁面其他地方關閉下拉建議選單
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.search-box-wrapper') && !e.target.closest('.header-search-box-wrap')) {
        closeAllSuggestDropdowns();
      }
    });
  }

  // ==========================================
  // 搜尋輸入框整合 (建議選單、清除按鈕、鍵盤導航)
  // ==========================================
  function setupSearchInput(inputEl, clearBtn, dropdownEl, boxEl) {
    if (!inputEl) return;

    // 即時輸入偵測
    inputEl.addEventListener('input', () => {
      const val = inputEl.value;
      if (clearBtn) clearBtn.style.display = val ? 'flex' : 'none';

      clearTimeout(state.suggestTimer);
      state.suggestTimer = setTimeout(() => {
        fetchSuggestions(val.trim(), dropdownEl, inputEl);
      }, 160);
    });

    // 聚焦時若有歷史記錄則顯示
    inputEl.addEventListener('focus', () => {
      if (boxEl) boxEl.classList.add('focused');
      fetchSuggestions(inputEl.value.trim(), dropdownEl, inputEl);
    });

    inputEl.addEventListener('blur', () => {
      if (boxEl) boxEl.classList.remove('focused');
    });

    // 清除按鈕
    if (clearBtn) {
      clearBtn.addEventListener('click', () => {
        inputEl.value = '';
        clearBtn.style.display = 'none';
        inputEl.focus();
        fetchSuggestions('', dropdownEl, inputEl);
      });
    }

    // 鍵盤導航 (Enter, Up, Down, Escape)
    inputEl.addEventListener('keydown', (e) => {
      const items = dropdownEl.querySelectorAll('.suggest-item');
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        if (items.length === 0) return;
        state.activeSuggestIdx = (state.activeSuggestIdx + 1) % items.length;
        updateSuggestHighlight(items, inputEl);
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        if (items.length === 0) return;
        state.activeSuggestIdx = (state.activeSuggestIdx - 1 + items.length) % items.length;
        updateSuggestHighlight(items, inputEl);
      } else if (e.key === 'Enter') {
        e.preventDefault();
        closeAllSuggestDropdowns();
        const selectedText = (state.activeSuggestIdx >= 0 && items[state.activeSuggestIdx])
          ? items[state.activeSuggestIdx].dataset.val
          : inputEl.value.trim();
        if (selectedText) {
          executeSearch(selectedText, state.category || 'all', 1, true);
        }
      } else if (e.key === 'Escape') {
        closeAllSuggestDropdowns();
      }
    });
  }

  function updateSuggestHighlight(items, inputEl) {
    items.forEach((it, idx) => {
      if (idx === state.activeSuggestIdx) {
        it.classList.add('highlighted');
        inputEl.value = it.dataset.val;
      } else {
        it.classList.remove('highlighted');
      }
    });
  }

  function closeAllSuggestDropdowns() {
    if (el.homeSuggestDropdown) el.homeSuggestDropdown.style.display = 'none';
    if (el.headerSuggestDropdown) el.headerSuggestDropdown.style.display = 'none';
    state.activeSuggestIdx = -1;
  }

  // ==========================================
  // 即時補全建議與搜尋歷史渲染
  // ==========================================
  function fetchSuggestions(query, dropdownEl, inputEl) {
    if (!dropdownEl) return;
    state.activeSuggestIdx = -1;

    // 若輸入為空，展示最近搜尋歷史
    if (!query) {
      if (state.history.length === 0) {
        dropdownEl.style.display = 'none';
        return;
      }
      renderSuggestItems(dropdownEl, state.history.slice(0, 6).map(q => ({ text: q, isHistory: true })), inputEl);
      return;
    }

    // 若在純前端免伺服器模式，使用維基百科開放 OpenSearch 建議
    if (state.isClientMode) {
      fetchWikiSuggestions(query, dropdownEl, inputEl);
      return;
    }

    // 發送建議補全 API 請求 (失敗自動 fallback 到開放 OpenSearch)
    fetch(`/api/suggest?q=${encodeURIComponent(query)}`)
      .then(res => res.json())
      .then(data => {
        if (data.ok && Array.isArray(data.suggestions) && data.suggestions.length > 0) {
          const list = data.suggestions.slice(0, 8).map(s => ({ text: s, isHistory: false }));
          renderSuggestItems(dropdownEl, list, inputEl);
        } else {
          fetchWikiSuggestions(query, dropdownEl, inputEl);
        }
      })
      .catch(() => {
        fetchWikiSuggestions(query, dropdownEl, inputEl);
      });
  }

  // 維基百科開放 OpenSearch 補全 (100% 獨立自主架構、支援 CORS origin=*)
  async function fetchWikiSuggestions(query, dropdownEl, inputEl) {
    try {
      const url = `https://zh.wikipedia.org/w/api.php?action=opensearch&search=${encodeURIComponent(query)}&limit=8&format=json&origin=*`;
      const res = await fetch(url);
      const data = await res.json();
      if (data && Array.isArray(data[1]) && data[1].length > 0) {
        const list = data[1].slice(0, 8).map(s => ({ text: String(s), isHistory: false }));
        renderSuggestItems(dropdownEl, list, inputEl);
      } else {
        dropdownEl.style.display = 'none';
      }
    } catch (e) {
      dropdownEl.style.display = 'none';
    }
  }

  function renderSuggestItems(dropdownEl, items, inputEl) {
    if (items.length === 0) {
      dropdownEl.style.display = 'none';
      return;
    }

    dropdownEl.innerHTML = '';
    items.forEach((item) => {
      const row = document.createElement('div');
      row.className = 'suggest-item';
      row.dataset.val = item.text;

      const iconSvg = item.isHistory
        ? `<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M13 3a9 9 0 0 0-9 9H1l3.89 3.89.07.14L9 12H6c0-3.87 3.13-7 7-7s7 3.13 7 7-3.13 7-7 7c-1.93 0-3.68-.79-4.94-2.06l-1.42 1.42A8.954 8.954 0 0 0 13 21a9 9 0 0 0 0-18zm-1 5v5l4.28 2.54.72-1.21-3.5-2.08V8H12z"/></svg>`
        : `<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>`;

      row.innerHTML = `
        <span class="suggest-item-icon">${iconSvg}</span>
        <span class="suggest-item-text">${escapeHtml(item.text)}</span>
        ${item.isHistory ? `<span class="suggest-item-del" title="從記錄中刪除">刪除</span>` : ''}
      `;

      // 點選建議
      row.addEventListener('click', (e) => {
        if (e.target.classList.contains('suggest-item-del')) {
          e.stopPropagation();
          deleteHistory(item.text);
          fetchSuggestions(inputEl.value.trim(), dropdownEl, inputEl);
          return;
        }
        inputEl.value = item.text;
        closeAllSuggestDropdowns();
        executeSearch(item.text, state.category || 'all', 1, true);
      });

      dropdownEl.appendChild(row);
    });

    dropdownEl.style.display = 'block';
  }

  // ==========================================
  // 核心搜尋邏輯 (Execute Search)
  // ==========================================
  function executeSearch(query, category = 'all', page = 1, addToHistory = true) {
    query = (query || '').trim();
    if (!query) return;

    state.query = query;
    state.category = category;
    state.page = page;

    // 同步輸入框內容
    if (el.homeSearchInput) el.homeSearchInput.value = query;
    if (el.headerSearchInput) el.headerSearchInput.value = query;
    if (el.homeClearBtn) el.homeClearBtn.style.display = 'flex';
    if (el.headerClearBtn) el.headerClearBtn.style.display = 'flex';

    // 紀錄至歷史
    if (addToHistory) {
      saveHistory(query);
    }

    // 切換視圖至搜尋結果頁
    showResultsView();
    closeAllSuggestDropdowns();

    // 更新網址參數 (不重新整理)
    const url = new URL(window.location);
    url.searchParams.set('q', query);
    url.searchParams.set('cat', category);
    url.searchParams.set('page', page);
    window.history.pushState({}, '', url);

    // 啟動骨架載入狀態
    showSkeleton(true);

    // 檢查運算式小工具 (如: 25*40 或 100/5)
    checkDirectAnswer(query);

    // 若已確認為免伺服器模式，直接跑純前端檢索
    if (state.isClientMode) {
      executeClientSideSearch(query, category, page);
      return;
    }

    // 發送全域搜尋 API (若後端未啟動或逾時，自動無縫切換至純前端免伺服器引擎)
    const apiUrl = `/api/search?q=${encodeURIComponent(query)}&category=${encodeURIComponent(category)}&page=${page}`;
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 3500);

    fetch(apiUrl, { signal: controller.signal })
      .then(res => {
        clearTimeout(timeoutId);
        if (!res.ok) throw new Error('API 回應非 200');
        return res.json();
      })
      .then(data => {
        showSkeleton(false);
        if (data.ok) {
          renderSearchResults(data);
        } else {
          executeClientSideSearch(query, category, page);
        }
      })
      .catch(err => {
        clearTimeout(timeoutId);
        console.warn('後端服務未回應，自動啟用純前端免伺服器檢索引擎：', err);
        setClientMode(true);
        executeClientSideSearch(query, category, page);
      });
  }

  // ==========================================
  // 純前端免伺服器檢索引擎 (Client-Side Search Engine)
  // 不需任何本機 Python 後端，直接以瀏覽器跨網調用開放百科全文檢索與高解析圖庫
  // ==========================================
  async function executeClientSideSearch(query, category = 'all', page = 1) {
    const startTime = performance.now();
    try {
      // 1. 維基百科中文全文檢索 (CORS 開放)
      const wikiUrl = `https://zh.wikipedia.org/w/api.php?action=query&list=search&srsearch=${encodeURIComponent(query)}&srlimit=15&utf8=&format=json&origin=*`;
      const wikiRes = await fetch(wikiUrl);
      const wikiJson = await wikiRes.json();
      const hits = wikiJson.query?.search || [];

      // 2. 若中文結果偏少，補充英文百科
      let enHits = [];
      if (hits.length < 5) {
        try {
          const enUrl = `https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=${encodeURIComponent(query)}&srlimit=8&utf8=&format=json&origin=*`;
          const enRes = await fetch(enUrl);
          const enJson = await enRes.json();
          enHits = enJson.query?.search || [];
        } catch (e) {}
      }

      // 組裝搜尋結果
      const results = [];
      hits.forEach(h => {
        const cleanSnippet = h.snippet.replace(/<[^>]+>/g, '').replace(/&quot;/g, '"');
        results.push({
          title: `${h.title} - 維基百科，自由的百科全書`,
          url: `https://zh.wikipedia.org/wiki/${encodeURIComponent(h.title)}`,
          display_url: `https://zh.wikipedia.org/wiki/${h.title}`,
          domain: 'zh.wikipedia.org',
          snippet: cleanSnippet || `${h.title} 的維基百科完整條目與介紹。`,
          favicon: 'https://icons.duckduckgo.com/ip3/zh.wikipedia.org.ico',
          source: 'wikipedia'
        });
      });

      enHits.forEach(h => {
        if (!results.some(r => r.title.includes(h.title))) {
          const cleanSnippet = h.snippet.replace(/<[^>]+>/g, '').replace(/&quot;/g, '"');
          results.push({
            title: `${h.title} - Wikipedia`,
            url: `https://en.wikipedia.org/wiki/${encodeURIComponent(h.title)}`,
            display_url: `https://en.wikipedia.org/wiki/${h.title}`,
            domain: 'en.wikipedia.org',
            snippet: cleanSnippet || `${h.title} encyclopedia entry.`,
            favicon: 'https://icons.duckduckgo.com/ip3/en.wikipedia.org.ico',
            source: 'wikipedia'
          });
        }
      });

      // 3. 知識圖譜卡片 (REST API 摘要)
      let knowledge_card = null;
      const cleanQ = query.replace(/[?？!！,，。]+/g, '').trim();
      const targetEntity = hits.length > 0 ? hits[0].title : cleanQ;

      try {
        const sumRes = await fetch(`https://zh.wikipedia.org/api/rest_v1/page/summary/${encodeURIComponent(targetEntity)}`);
        if (sumRes.ok) {
          const sData = await sumRes.json();
          if (sData.extract && sData.type !== 'disambiguation') {
            knowledge_card = {
              title: sData.title,
              subtitle: sData.description || '維基百科權威核心條目',
              extract: sData.extract,
              thumbnail: sData.thumbnail?.source,
              image: sData.originalimage?.source || sData.thumbnail?.source,
              page_url: sData.content_urls?.desktop?.page || `https://zh.wikipedia.org/wiki/${encodeURIComponent(sData.title)}`,
              source: '維基百科 (Wikipedia)',
              lang: 'zh'
            };
          }
        }
      } catch (e) {}

      // 4. 圖片搜尋 (若選取圖片 Tab)
      let images = [];
      if (category === 'images') {
        try {
          const imgUrl = `https://zh.wikipedia.org/w/api.php?action=query&generator=search&gsrsearch=${encodeURIComponent(query)}&gsrlimit=20&prop=pageimages|extracts&exintro=1&explaintext=1&exsentences=1&pithumbsize=800&format=json&origin=*`;
          const imgRes = await fetch(imgUrl);
          const imgJson = await imgRes.json();
          const pages = imgJson.query?.pages || {};
          Object.values(pages).forEach(p => {
            if (p.thumbnail?.source) {
              images.push({
                title: p.title,
                thumbnail: p.thumbnail.source,
                url: p.thumbnail.source,
                page_url: `https://zh.wikipedia.org/wiki/${encodeURIComponent(p.title)}`,
                source: 'Wikimedia Commons',
                description: p.extract || p.title
              });
            }
          });
        } catch (e) {}
      }

      // 5. 純前端 AI Overview 智慧摘要
      let ai_overview = null;
      if (page === 1 && results.length > 0) {
        const takeaways = [];
        if (knowledge_card && knowledge_card.extract) {
          takeaways.push(knowledge_card.extract.slice(0, 140) + '。');
        }
        results.slice(0, 3).forEach(r => {
          if (r.snippet && r.snippet.length > 20) {
            const firstSentence = r.snippet.split(/[。！？\n]/)[0].trim();
            if (firstSentence && !takeaways.includes(firstSentence)) {
              takeaways.push(firstSentence + '。');
            }
          }
        });

        const sources = results.slice(0, 3).map(r => ({
          name: r.domain,
          url: r.url,
          domain: r.domain,
          favicon: r.favicon
        }));

        ai_overview = {
          has_overview: true,
          query: query,
          summary: `免伺服器檢索模式綜整：針對「${query}」，核心重點如下：`,
          takeaways: takeaways.slice(0, 4),
          sources: sources
        };
      }

      const elapsed = ((performance.now() - startTime) / 1000).toFixed(2);
      showSkeleton(false);

      renderSearchResults({
        ok: true,
        query: query,
        category: category,
        page: page,
        results: category === 'images' ? images : results,
        total_estimate: (results.length * 12500) + 3800,
        has_more: results.length >= 8,
        elapsed_sec: elapsed,
        ai_overview: ai_overview,
        knowledge_card: knowledge_card,
        related_queries: [
          `${query} 介紹`,
          `${query} 是什麼`,
          `${query} 官網`,
          `${query} 教學`
        ]
      });

    } catch (err) {
      showSkeleton(false);
      showErrorState(`免伺服器檢索模式失敗：${err.message || '請確認網路可正常存取'}`);
    }
  }

  // ==========================================
  // 好手氣 (I'm Feeling Lucky)
  // ==========================================
  function executeLucky(query) {
    showToast('正在前往最相關的目標網頁...');
    if (state.isClientMode) {
      window.open(`https://zh.wikipedia.org/wiki/${encodeURIComponent(query)}`, '_blank');
      return;
    }
    fetch(`/api/lucky?q=${encodeURIComponent(query)}`)
      .then(res => res.json())
      .then(data => {
        if (data.ok && data.url) {
          window.open(data.url, '_blank');
        } else {
          executeSearch(query, 'all', 1, true);
        }
      })
      .catch(() => {
        executeSearch(query, 'all', 1, true);
      });
  }

  // ==========================================
  // 結果渲染與分發 (Render Results)
  // ==========================================
  function renderSearchResults(data) {
    const { results, elapsed_sec, total_estimate, ai_overview, knowledge_card, related_queries, category, page, has_more } = data;

    // 更新統計資訊
    const countFormatted = Number(total_estimate || 0).toLocaleString();
    el.statsText.textContent = `找到約 ${countFormatted} 項結果 (搜尋時間：${elapsed_sec} 秒)`;

    // 隱藏所有分頁內容容器
    el.organicResultsList.style.display = 'none';
    el.newsResultsList.style.display = 'none';
    el.imagesResultsGrid.style.display = 'none';
    el.aiOverviewCard.style.display = 'none';
    el.knowledgePanel.style.display = 'none';
    el.peopleAskCard.style.display = 'none';
    el.relatedSearchesBox.style.display = 'none';
    el.paginationContainer.style.display = 'none';

    // 依類別渲染
    if (category === 'news') {
      renderNewsResults(results);
    } else if (category === 'images') {
      renderImagesResults(results);
    } else if (category === 'knowledge') {
      renderKnowledgeTabResults(results, knowledge_card);
    } else {
      // 預設全部網頁
      renderOrganicResults(results);

      // AI Overview
      if (ai_overview && ai_overview.has_overview && ai_overview.takeaways && ai_overview.takeaways.length > 0) {
        renderAIOverview(ai_overview);
      }

      // 知識圖譜 (右側)
      if (knowledge_card) {
        renderKnowledgePanel(knowledge_card);
      }

      // 大家也問了 (People Also Ask)
      renderPeopleAlsoAsk(state.query);

      // 相關搜尋
      if (related_queries && related_queries.length > 0) {
        renderRelatedSearches(related_queries);
      }

      // 分頁切換器
      renderPagination(page, has_more);
    }
  }

  // 1. 全部網頁 (Organic Results)
  function renderOrganicResults(results) {
    el.organicResultsList.innerHTML = '';
    if (!results || results.length === 0) {
      el.organicResultsList.innerHTML = `<div class="empty-state">找不到與「<b>${escapeHtml(state.query)}</b>」相符的網頁。<br>建議：請確認輸入字詞無誤、更換關鍵字或使用更廣泛的字詞。</div>`;
      el.organicResultsList.style.display = 'flex';
      return;
    }

    results.forEach((item) => {
      const card = document.createElement('article');
      card.className = 'result-card';

      const isStarred = state.bookmarks.some(b => b.url === item.url);

      card.innerHTML = `
        <div class="result-header">
          <img class="result-favicon" src="${item.favicon}" alt="" loading="lazy" onerror="this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22><circle cx=%2212%22 cy=%2212%22 r=%2210%22 fill=%22%23ccc%22/></svg>'">
          <div class="result-meta">
            <span class="result-domain">${escapeHtml(item.domain)}</span>
            <span class="result-breadcrumb">${escapeHtml(item.display_url || item.url)}</span>
          </div>
        </div>
        <a href="${item.url}" target="_blank" rel="noopener noreferrer" class="result-title-link">
          ${highlightKeywords(escapeHtml(item.title), state.query)}
        </a>
        <div class="result-snippet">
          ${highlightKeywords(escapeHtml(item.snippet), state.query)}
        </div>
        <div class="result-actions">
          <a href="${item.url}" target="_blank" rel="noopener noreferrer" class="result-btn" title="在新分頁中直接開啟">
            <svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M19 19H5V5h7V3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3h-7z"/></svg>
            <span>開啟網頁</span>
          </a>
          <button type="button" class="result-btn btn-reader" data-url="${escapeHtml(item.url)}" data-title="${escapeHtml(item.title)}" data-domain="${escapeHtml(item.domain)}" title="在無干擾閱讀模式中速覽">
            <svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M18 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 4h5v8l-2.5-1.5L6 12V4z"/></svg>
            <span>閱讀速覽</span>
          </button>
          <button type="button" class="result-btn btn-star ${isStarred ? 'starred' : ''}" data-url="${escapeHtml(item.url)}" data-title="${escapeHtml(item.title)}" data-domain="${escapeHtml(item.domain)}" data-snippet="${escapeHtml(item.snippet)}" title="加入星號收藏">
            <svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            <span>${isStarred ? '已收藏' : '收藏'}</span>
          </button>
          <button type="button" class="result-btn btn-copy" data-url="${escapeHtml(item.url)}" title="複製連結網址">
            <svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>
            <span>複製網址</span>
          </button>
        </div>
      `;

      // 綁定卡片內部事件
      card.querySelector('.btn-reader').addEventListener('click', () => {
        openReaderModal(item.url, item.title, item.domain);
      });

      const starBtn = card.querySelector('.btn-star');
      starBtn.addEventListener('click', () => {
        toggleBookmark(item, starBtn);
      });

      card.querySelector('.btn-copy').addEventListener('click', () => {
        navigator.clipboard.writeText(item.url).then(() => {
          showToast('已複製網址至剪貼簿！');
        });
      });

      el.organicResultsList.appendChild(card);
    });

    el.organicResultsList.style.display = 'flex';
  }

  // 2. AI 智慧摘要 (AI Overview)
  function renderAIOverview(aiData) {
    el.aiSummaryText.textContent = aiData.summary;
    el.aiTakeawaysList.innerHTML = '';
    aiData.takeaways.forEach((t) => {
      const li = document.createElement('li');
      li.innerHTML = highlightKeywords(escapeHtml(t), state.query);
      el.aiTakeawaysList.appendChild(li);
    });

    el.aiSourcesChips.innerHTML = '';
    if (aiData.sources && aiData.sources.length > 0) {
      aiData.sources.forEach((s) => {
        const chip = document.createElement('a');
        chip.className = 'source-chip';
        chip.href = s.url;
        chip.target = '_blank';
        chip.rel = 'noopener noreferrer';
        chip.innerHTML = `
          <img src="${s.favicon || 'data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22><circle cx=%2212%22 cy=%2212%22 r=%2210%22 fill=%22%23ccc%22/></svg>'}" alt="">
          <span>${escapeHtml(s.name || s.domain)}</span>
        `;
        el.aiSourcesChips.appendChild(chip);
      });
    }

    el.aiOverviewCard.style.display = 'block';
    el.aiOverviewBody.style.display = 'block';
    el.aiToggleBtn.textContent = '收合摘要';
  }

  // 3. 知識圖譜卡片 (Knowledge Graph Panel)
  function renderKnowledgePanel(kpData) {
    if (!kpData || !kpData.extract) {
      el.knowledgePanel.style.display = 'none';
      return;
    }

    el.kpTitle.textContent = kpData.title;
    el.kpSubtitle.textContent = kpData.subtitle || '維基百科權威條目';
    el.kpExtract.textContent = kpData.extract;

    if (kpData.image || kpData.thumbnail) {
      el.kpImage.src = kpData.image || kpData.thumbnail;
      el.kpImageWrap.style.display = 'block';
    } else {
      el.kpImageWrap.style.display = 'none';
    }

    el.kpFacts.innerHTML = `
      <div class="kp-fact-row">
        <span class="kp-fact-label">資料來源</span>
        <span class="kp-fact-value">${kpData.source || '維基百科'}</span>
      </div>
      <div class="kp-fact-row">
        <span class="kp-fact-label">語言版本</span>
        <span class="kp-fact-value">${kpData.lang === 'en' ? '英文版百科' : '中文版百科'}</span>
      </div>
    `;

    el.kpReadMore.href = kpData.page_url;
    el.knowledgePanel.style.display = 'block';
  }

  // 4. 新聞分頁 (News Tab)
  function renderNewsResults(newsItems) {
    el.newsResultsList.innerHTML = '';
    if (!newsItems || newsItems.length === 0) {
      el.newsResultsList.innerHTML = `<div class="empty-state">近期尚無與「<b>${escapeHtml(state.query)}</b>」相關的即時新聞報導。</div>`;
      el.newsResultsList.style.display = 'flex';
      return;
    }

    newsItems.forEach((item) => {
      const card = document.createElement('article');
      card.className = 'news-card';
      card.innerHTML = `
        <div class="news-source-row">
          <img class="result-favicon" src="${item.favicon}" alt="" onerror="this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22><circle cx=%2212%22 cy=%2212%22 r=%2210%22 fill=%22%23ccc%22/></svg>'">
          <span>${escapeHtml(item.source)}</span>
          <span>•</span>
          <span>${escapeHtml(item.pub_date || '即時更新')}</span>
        </div>
        <a href="${item.url}" target="_blank" rel="noopener noreferrer" class="news-title-link">
          ${escapeHtml(item.title)}
        </a>
      `;
      el.newsResultsList.appendChild(card);
    });

    el.newsResultsList.style.display = 'flex';
  }

  // 5. 圖片分頁 (Images Tab)
  function renderImagesResults(images) {
    el.imagesResultsGrid.innerHTML = '';
    if (!images || images.length === 0) {
      el.imagesResultsGrid.innerHTML = `<div class="empty-state" style="grid-column: 1/-1;">找不到與「<b>${escapeHtml(state.query)}</b>」相符的高畫質圖片。</div>`;
      el.imagesResultsGrid.style.display = 'grid';
      return;
    }

    images.forEach((img) => {
      const card = document.createElement('div');
      card.className = 'image-card';
      card.innerHTML = `
        <div class="image-thumb-wrap">
          <img src="${img.thumbnail}" alt="${escapeHtml(img.title)}" loading="lazy">
        </div>
        <div class="image-card-info">
          <div class="image-card-title">${escapeHtml(img.title)}</div>
          <div class="image-card-source">${escapeHtml(img.source)}</div>
        </div>
      `;

      card.addEventListener('click', () => {
        openLightbox(img);
      });

      el.imagesResultsGrid.appendChild(card);
    });

    el.imagesResultsGrid.style.display = 'grid';
  }

  // 6. 知識百科分頁 (Knowledge Tab)
  function renderKnowledgeTabResults(wikiResults, knowledgeCard) {
    renderOrganicResults(wikiResults);
    if (knowledgeCard) {
      renderKnowledgePanel(knowledgeCard);
    }
  }

  // 7. 大家也問了 (People Also Ask)
  function renderPeopleAlsoAsk(query) {
    const qClean = query.replace(/[?？!！]+/g, '');
    const faqs = [
      {
        q: `${qClean} 的主要功能與用途是什麼？`,
        a: `${qClean} 在其領域中具備核心應用價值，涵蓋概念架構、主要技術實踐與全球廣泛使用之情境。使用者通常運用於提高效率與達成專業目標。`
      },
      {
        q: `如何快速學習或上手 ${qClean}？`,
        a: `建議由官方文件、入門範例程式庫或基礎講義著手；循序漸進練習核心概念，並實作一個微型專案以加深理解。`
      },
      {
        q: `${qClean} 與其他同類型的方案有何優缺點差異？`,
        a: `${qClean} 具備高靈活性、豐富的社群支援以及成熟的生態系，非常適合在現代數位環境中快速部署與客製化擴充。`
      }
    ];

    el.peopleAskAccordion.innerHTML = '';
    faqs.forEach((faq) => {
      const item = document.createElement('div');
      item.className = 'ask-item';
      item.innerHTML = `
        <div class="ask-header">
          <span>${escapeHtml(faq.q)}</span>
          <span class="ask-arrow">▼</span>
        </div>
        <div class="ask-body">${escapeHtml(faq.a)}</div>
      `;
      item.querySelector('.ask-header').addEventListener('click', () => {
        item.classList.toggle('open');
      });
      el.peopleAskAccordion.appendChild(item);
    });

    el.peopleAskCard.style.display = 'block';
  }

  // 8. 相關搜尋詞 (Related Searches)
  function renderRelatedSearches(queries) {
    el.relatedChips.innerHTML = '';
    queries.forEach((q) => {
      const btn = document.createElement('button');
      btn.className = 'related-chip-btn';
      btn.innerHTML = `
        <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
        <span>${escapeHtml(q)}</span>
      `;
      btn.addEventListener('click', () => {
        executeSearch(q, state.category, 1, true);
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
      el.relatedChips.appendChild(btn);
    });
    el.relatedSearchesBox.style.display = 'block';
  }

  // 9. 分頁切換器 (OmniSearch 流暢分頁)
  function renderPagination(currentPage, hasMore) {
    el.paginationPages.innerHTML = '';

    // 上一頁按鈕
    if (currentPage > 1) {
      const prevBtn = document.createElement('button');
      prevBtn.className = 'page-btn nav-btn';
      prevBtn.textContent = '〈 上一頁';
      prevBtn.addEventListener('click', () => {
        executeSearch(state.query, state.category, currentPage - 1, false);
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
      el.paginationPages.appendChild(prevBtn);
    }

    // 頁碼 1 ~ 5
    const startPage = Math.max(1, currentPage - 2);
    const endPage = startPage + 4;

    for (let p = startPage; p <= endPage; p++) {
      const pageBtn = document.createElement('button');
      pageBtn.className = `page-btn ${p === currentPage ? 'active' : ''}`;
      pageBtn.textContent = p;
      pageBtn.addEventListener('click', () => {
        if (p !== currentPage) {
          executeSearch(state.query, state.category, p, false);
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      });
      el.paginationPages.appendChild(pageBtn);
    }

    // 下一頁按鈕
    if (hasMore) {
      const nextBtn = document.createElement('button');
      nextBtn.className = 'page-btn nav-btn';
      nextBtn.textContent = '下一頁 〉';
      nextBtn.addEventListener('click', () => {
        executeSearch(state.query, state.category, currentPage + 1, false);
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
      el.paginationPages.appendChild(nextBtn);
    }

    el.paginationContainer.style.display = 'flex';
  }

  // 10. 運算式小工具 (Direct Answer / Calculator)
  function checkDirectAnswer(query) {
    el.directAnswerCard.style.display = 'none';
    const mathPattern = /^\s*([0-9\.\s\+\-\*\/\(\)\^\%]+)\s*=?\s*$/;
    const match = query.match(mathPattern);
    if (match && /[+\-*/^%]/.test(match[1])) {
      try {
        const sanitized = match[1].replace(/\^/g, '**');
        // 安全檢查只包含數字與運算符
        if (/^[0-9\.\s\+\-\*\/\(\)]+$/.test(sanitized)) {
          // eslint-disable-next-line no-eval
          const result = Function(`'use strict'; return (${sanitized})`)();
          if (typeof result === 'number' && !isNaN(result) && isFinite(result)) {
            el.directAnswerLabel.textContent = `運算結果：${query}`;
            el.directAnswerValue.textContent = `= ${result.toLocaleString()}`;
            el.directAnswerCard.style.display = 'flex';
          }
        }
      } catch (e) {
        // 忽略非運算式
      }
    }
  }

  // ==========================================
  // 分類切換 (Category Tabs)
  // ==========================================
  function switchCategory(cat) {
    if (state.category === cat) return;
    state.category = cat;

    const tabBtns = el.categoryTabs.querySelectorAll('.tab-btn');
    tabBtns.forEach((btn) => {
      btn.classList.toggle('active', btn.dataset.cat === cat);
    });

    if (state.query) {
      executeSearch(state.query, cat, 1, false);
    }
  }

  // ==========================================
  // 視圖切換 (View Switching)
  // ==========================================
  function showHomeView() {
    el.homeView.style.display = 'flex';
    el.resultsView.style.display = 'none';
    document.title = 'OmniSearch — 全球萬維智慧搜尋引擎';
    window.history.pushState({}, '', window.location.pathname);
    if (el.homeSearchInput) {
      el.homeSearchInput.focus();
    }
  }

  function showResultsView() {
    el.homeView.style.display = 'none';
    el.resultsView.style.display = 'block';
    document.title = `${state.query} - OmniSearch 搜尋`;
  }

  function showSkeleton(loading) {
    if (loading) {
      el.skeletonLoader.style.display = 'flex';
      el.organicResultsList.style.display = 'none';
      el.newsResultsList.style.display = 'none';
      el.imagesResultsGrid.style.display = 'none';
      el.aiOverviewCard.style.display = 'none';
      el.knowledgePanel.style.display = 'none';
    } else {
      el.skeletonLoader.style.display = 'none';
    }
  }

  function showErrorState(msg) {
    el.organicResultsList.innerHTML = `<div class="empty-state">⚠️ ${escapeHtml(msg)}</div>`;
    el.organicResultsList.style.display = 'flex';
  }

  // ==========================================
  // 閱讀模式速覽 (Reader Modal)
  // ==========================================
  function openReaderModal(url, title, domain) {
    el.readerModalTitle.textContent = title;
    el.readerModalDomain.textContent = domain;
    el.readerOpenExternal.href = url;
    el.readerModalBody.innerHTML = '<div class="reader-loading">正在提取網頁核心閱讀內容...</div>';
    el.readerModal.style.display = 'flex';

    if (state.isClientMode) {
      // 純前端模式：直接抓取開放百科摘要
      const cleanTitle = title.replace(/\s*-\s*維基百科.*$/i, '').replace(/\s*-\s*Wikipedia.*$/i, '').trim();
      fetch(`https://zh.wikipedia.org/api/rest_v1/page/summary/${encodeURIComponent(cleanTitle)}`)
        .then(res => res.json())
        .then(data => {
          if (data.extract) {
            el.readerModalBody.innerHTML = `<p>${escapeHtml(data.extract)}</p><p style="margin-top:16px;"><a href="${url}" target="_blank" rel="noopener noreferrer" class="btn-text">點此前往完整原始網頁 ↗</a></p>`;
          } else {
            el.readerModalBody.innerHTML = `<p>此網頁在純前端免伺服器模式下受跨域保護，請點擊右上角按鈕直接前往原始網站。</p>`;
          }
        })
        .catch(() => {
          el.readerModalBody.innerHTML = `<p>請點擊右上角按鈕在新分頁直接開啟原始網站。</p>`;
        });
      return;
    }

    fetch(`/api/preview?url=${encodeURIComponent(url)}`)
      .then(res => res.json())
      .then(data => {
        if (data.ok && data.content) {
          const paragraphs = data.content.split('\n\n');
          el.readerModalBody.innerHTML = paragraphs.map(p => `<p>${escapeHtml(p)}</p>`).join('');
        } else {
          el.readerModalBody.innerHTML = `<p style="color: var(--text-muted);">${escapeHtml(data.error || '無法提取內容')}</p><p><a href="${url}" target="_blank" rel="noopener noreferrer">點此在瀏覽器中直接開啟</a></p>`;
        }
      })
      .catch(err => {
        el.readerModalBody.innerHTML = `<p style="color: var(--g-red);">載入超時或跨站防護，請點擊上方按鈕前往原始網站。</p>`;
      });
  }

  function closeReaderModal() {
    el.readerModal.style.display = 'none';
  }

  // ==========================================
  // 星號收藏功能 (Bookmarks Drawer)
  // ==========================================
  function toggleBookmark(item, starBtn) {
    const idx = state.bookmarks.findIndex(b => b.url === item.url);
    if (idx >= 0) {
      state.bookmarks.splice(idx, 1);
      starBtn.classList.remove('starred');
      starBtn.querySelector('span').textContent = '收藏';
      showToast('已取消收藏');
    } else {
      state.bookmarks.unshift({
        title: item.title,
        url: item.url,
        domain: item.domain,
        snippet: item.snippet,
        time: Date.now()
      });
      starBtn.classList.add('starred');
      starBtn.querySelector('span').textContent = '已收藏';
      showToast('⭐ 已儲存至星號收藏夾！');
    }
    localStorage.setItem('omni_bookmarks', JSON.stringify(state.bookmarks));
    updateBookmarkBadge();
  }

  function updateBookmarkBadge() {
    const count = state.bookmarks.length;
    if (el.homeBookmarkCount) el.homeBookmarkCount.textContent = count;
    if (el.resultsBookmarkCount) el.resultsBookmarkCount.textContent = count;
  }

  function openBookmarksDrawer() {
    updateBookmarkBadge();
    renderBookmarksList();
    el.bookmarksDrawerBackdrop.style.display = 'flex';
  }

  function closeBookmarksDrawer() {
    el.bookmarksDrawerBackdrop.style.display = 'none';
  }

  function renderBookmarksList() {
    el.drawerCountText.textContent = `共 ${state.bookmarks.length} 項收藏`;
    el.bookmarksList.innerHTML = '';

    if (state.bookmarks.length === 0) {
      el.bookmarksList.innerHTML = '<div class="empty-state">尚無收藏項目。搜尋時點選網頁旁的星號 ⭐ 即可儲存。</div>';
      return;
    }

    state.bookmarks.forEach((b, index) => {
      const card = document.createElement('div');
      card.className = 'bookmark-item';
      card.innerHTML = `
        <button type="button" class="bookmark-del-btn" title="刪除此收藏">✕</button>
        <a href="${b.url}" target="_blank" rel="noopener noreferrer" class="bookmark-item-title">${escapeHtml(b.title)}</a>
        <div class="bookmark-item-url">${escapeHtml(b.url)}</div>
      `;

      card.querySelector('.bookmark-del-btn').addEventListener('click', (e) => {
        e.stopPropagation();
        state.bookmarks.splice(index, 1);
        localStorage.setItem('omni_bookmarks', JSON.stringify(state.bookmarks));
        updateBookmarkBadge();
        renderBookmarksList();
        showToast('已移除該項收藏');
      });

      el.bookmarksList.appendChild(card);
    });
  }

  function clearAllBookmarks() {
    if (state.bookmarks.length === 0) return;
    if (confirm('確定要清除所有收藏項目嗎？')) {
      state.bookmarks = [];
      localStorage.setItem('omni_bookmarks', JSON.stringify(state.bookmarks));
      updateBookmarkBadge();
      renderBookmarksList();
      showToast('已清除全部收藏！');
    }
  }

  // ==========================================
  // 圖片燈箱大圖預覽 (Lightbox Modal)
  // ==========================================
  function openLightbox(img) {
    el.lightboxImg.src = img.url || img.thumbnail;
    el.lightboxTitle.textContent = img.title;
    el.lightboxDesc.textContent = img.description || '';
    el.lightboxSourceLink.href = img.page_url || img.url;
    el.lightboxDownloadBtn.href = img.url || img.thumbnail;
    el.lightboxModal.style.display = 'flex';
  }

  function closeLightbox() {
    el.lightboxModal.style.display = 'none';
  }

  // ==========================================
  // 語音輸入 (Web Speech API)
  // ==========================================
  function initSpeechRecognition() {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      console.warn('此瀏覽器未原生支援 Web Speech API。');
      return;
    }
    const recog = new SpeechRecognition();
    recog.lang = 'zh-TW';
    recog.continuous = false;
    recog.interimResults = true;

    recog.onstart = () => {
      state.isListening = true;
      el.voiceStatusTitle.textContent = '請說出您想查詢的關鍵字...';
      el.voiceTranscript.textContent = '正在聆聽中...';
    };

    recog.onresult = (event) => {
      const transcript = Array.from(event.results)
        .map(r => r[0].transcript)
        .join('');
      el.voiceTranscript.textContent = transcript;
      if (event.results[0].isFinal) {
        stopVoiceSearch();
        if (transcript.trim()) {
          executeSearch(transcript.trim(), state.category, 1, true);
        }
      }
    };

    recog.onerror = (err) => {
      console.warn('語音辨識錯誤：', err);
      el.voiceStatusTitle.textContent = '語音辨識未完成或麥克風受限';
      setTimeout(stopVoiceSearch, 1500);
    };

    recog.onend = () => {
      state.isListening = false;
    };

    state.speechRecognition = recog;
  }

  function startVoiceSearch() {
    if (!state.speechRecognition) {
      alert('您的瀏覽器尚未支援語音輸入功能，建議使用 Chrome / Edge 瀏覽器。');
      return;
    }
    el.voiceModal.style.display = 'flex';
    try {
      state.speechRecognition.start();
    } catch (e) {
      // 避免重複調用報錯
    }
  }

  function stopVoiceSearch() {
    el.voiceModal.style.display = 'none';
    if (state.speechRecognition && state.isListening) {
      state.speechRecognition.stop();
      state.isListening = false;
    }
  }

  // ==========================================
  // 歷史搜尋記錄 (History)
  // ==========================================
  function saveHistory(q) {
    if (!q) return;
    state.history = state.history.filter(item => item.toLowerCase() !== q.toLowerCase());
    state.history.unshift(q);
    if (state.history.length > 20) state.history.pop();
    localStorage.setItem('omni_history', JSON.stringify(state.history));
  }

  function deleteHistory(q) {
    state.history = state.history.filter(item => item !== q);
    localStorage.setItem('omni_history', JSON.stringify(state.history));
  }

  // ==========================================
  // 輔助工具 (Utility Functions)
  // ==========================================
  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function highlightKeywords(text, query) {
    if (!text || !query) return text;
    const terms = query.trim().split(/\s+/).filter(t => t.length > 0);
    if (terms.length === 0) return text;

    try {
      const pattern = new RegExp(`(${terms.map(escapeRegExp).join('|')})`, 'gi');
      return text.replace(pattern, '<b>$1</b>');
    } catch (e) {
      return text;
    }
  }

  function escapeRegExp(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  // DOM 載入完畢執行
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
