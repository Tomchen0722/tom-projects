// 地政士（土地登記專業代理人）專技普考全能學習系統核心邏輯
(function() {
  'use strict';

  // 題庫資料（由 assets/questions-data.js 載入）
  const ALL_QUESTIONS = window.QUESTION_BANK || [];

  // 全域狀態
  let state = {
    theme: localStorage.getItem('land_agent_theme') || 'light',
    currentTab: 'dashboard',

    // 練習狀態
    practiceCat: 'ALL',
    practiceFilter: 'all', // all, answered, unanswered
    practiceSearch: '',
    practicePage: 1,
    pageSize: 15,
    practiceAnswers: JSON.parse(localStorage.getItem('land_agent_practice_answers') || '{}'),

    // 錯題本與收藏 (存題號 ID 陣列)
    errors: JSON.parse(localStorage.getItem('land_agent_errors') || '[]'),
    favorites: JSON.parse(localStorage.getItem('land_agent_favorites') || '[]'),

    // 模擬考狀態
    examActive: false,
    examCount: 50, // 50 or 100
    examQuestions: [],
    examAnswers: {},
    examCurrentIdx: 0,
    examTimer: null,
    examSecondsLeft: 3600,
    examHistory: JSON.parse(localStorage.getItem('land_agent_exam_history') || '[]'),

    // 講義當前選取
    currentNote: '00-study-guide'
  };

  // DOM 載入後初始化
  document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initNavigation();
    initDashboard();
    initPractice();
    initErrorBook();
    initSearch();
    initFlashcards();
    initNotes();
  });

  // ══════════════════════════════════════════════════════════
  // 主題切換 (Theme)
  // ══════════════════════════════════════════════════════════
  function initTheme() {
    document.documentElement.setAttribute('data-theme', state.theme);
    const themeBtn = document.getElementById('themeToggleBtn');
    if (themeBtn) {
      themeBtn.textContent = state.theme === 'dark' ? '☀️' : '🌙';
      themeBtn.addEventListener('click', () => {
        state.theme = state.theme === 'dark' ? 'light' : 'dark';
        localStorage.setItem('land_agent_theme', state.theme);
        document.documentElement.setAttribute('data-theme', state.theme);
        themeBtn.textContent = state.theme === 'dark' ? '☀️' : '🌙';
      });
    }
  }

  // ══════════════════════════════════════════════════════════
  // 導航標籤切換 (Navigation)
  // ══════════════════════════════════════════════════════════
  function initNavigation() {
    const navBtns = document.querySelectorAll('.nav-btn');
    navBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const targetTab = btn.getAttribute('data-tab');
        switchTab(targetTab);
      });
    });
  }

  function switchTab(tabId) {
    if (state.examActive && tabId !== 'mock-exam') {
      if (!confirm('全真模擬考正在進行中，確定要離開嗎？（計時器將繼續運行）')) {
        return;
      }
    }

    state.currentTab = tabId;
    document.querySelectorAll('.nav-btn').forEach(b => {
      b.classList.toggle('active', b.getAttribute('data-tab') === tabId);
    });
    document.querySelectorAll('.view-section').forEach(sec => {
      sec.classList.toggle('active', sec.id === `tab-${tabId}`);
    });
    window.scrollTo({ top: 0, behavior: 'smooth' });

    if (tabId === 'dashboard') updateDashboardStats();
    if (tabId === 'practice') renderPracticeQuestions();
    if (tabId === 'error-book') renderErrorBook();
  }
  window.switchTab = switchTab;

  // ══════════════════════════════════════════════════════════
  // 總覽儀表板 (Dashboard)
  // ══════════════════════════════════════════════════════════
  function initDashboard() {
    updateDashboardStats();
  }

  function updateDashboardStats() {
    const totalQEl = document.getElementById('statTotalQuestions');
    const errCountEl = document.getElementById('statErrorCount');
    const bestScoreEl = document.getElementById('statBestScore');
    const examTimesEl = document.getElementById('statExamTimes');

    if (totalQEl) totalQEl.textContent = ALL_QUESTIONS.length.toLocaleString();
    if (errCountEl) errCountEl.textContent = state.errors.length.toLocaleString();
    if (examTimesEl) examTimesEl.textContent = state.examHistory.length.toLocaleString() + ' 次';

    let bestScore = 0;
    if (state.examHistory.length > 0) {
      bestScore = Math.max(...state.examHistory.map(h => h.score));
    }
    if (bestScoreEl) bestScoreEl.textContent = bestScore > 0 ? bestScore + ' 分' : '尚無紀錄';

    // 更新各科練習進度
    const secCounts = {
      '民法概要與信託法概要': 0,
      '土地法規': 0,
      '土地登記規則與地籍測量': 0,
      '土地稅法規': 0
    };
    Object.keys(state.practiceAnswers).forEach(qid => {
      const q = ALL_QUESTIONS.find(item => item.id === qid);
      if (q && secCounts[q.category] !== undefined) {
        secCounts[q.category]++;
      }
    });

    for (let i = 1; i <= 4; i++) {
      const cats = [
        '民法概要與信託法概要',
        '土地法規',
        '土地登記規則與地籍測量',
        '土地稅法規'
      ];
      const cat = cats[i - 1];
      const count = secCounts[cat] || 0;
      const pct = Math.min(100, Math.round((count / 150) * 100));
      const fillEl = document.getElementById(`subProgressFill${i}`);
      const textEl = document.getElementById(`subProgressText${i}`);
      if (fillEl) fillEl.style.width = `${pct}%`;
      if (textEl) textEl.textContent = `${count} / 150 題 (${pct}%)`;
    }

    // 歷次模擬考表格
    const historyTbody = document.getElementById('examHistoryTbody');
    if (historyTbody) {
      if (state.examHistory.length === 0) {
        historyTbody.innerHTML = `<tr><td colspan="5" style="text-align:center;color:var(--ink-muted);padding:24px;">尚無模擬考紀錄，立即點擊上方按鈕開始全真測驗！</td></tr>`;
      } else {
        const sorted = [...state.examHistory].reverse().slice(0, 5);
        historyTbody.innerHTML = sorted.map((h, idx) => {
          const isPass = h.score >= 60;
          return `
            <tr>
              <td><span style="font-family:var(--font-mono);font-weight:600;">${h.date}</span></td>
              <td><strong>${h.title || (h.totalQuestions + '題模擬考')}</strong></td>
              <td><span style="font-family:var(--font-mono);font-weight:800;color:${isPass ? 'var(--green)' : 'var(--red)'};font-size:16px;">${h.score} 分</span></td>
              <td><span style="font-family:var(--font-mono);color:var(--ink-secondary);">${h.timeSpent}</span></td>
              <td><span class="subject-pill ${isPass ? 'pill-sec2' : 'pill-sec4'}">${isPass ? '✓ 及格及格' : '✗ 未達標準'}</span></td>
            </tr>
          `;
        }).join('');
      }
    }
  }

  // ══════════════════════════════════════════════════════════
  // 全真模擬考模組 (Mock Exam)
  // ══════════════════════════════════════════════════════════
  window.startMockExam = function(qCount = 50) {
    if (state.examActive) {
      if (!confirm('目前有正在進行中的模擬考，確定要重新開啟新測驗嗎？')) {
        return;
      }
      clearInterval(state.examTimer);
    }

    state.examCount = qCount;
    state.examActive = true;
    state.examAnswers = {};
    state.examCurrentIdx = 0;
    state.examSecondsLeft = qCount === 50 ? 2700 : 3600; // 50題 45分鐘，100題 60分鐘

    // 四大科目均勻抽題
    const sec1 = ALL_QUESTIONS.filter(q => q.category === '民法概要與信託法概要');
    const sec2 = ALL_QUESTIONS.filter(q => q.category === '土地法規');
    const sec3 = ALL_QUESTIONS.filter(q => q.category === '土地登記規則與地籍測量');
    const sec4 = ALL_QUESTIONS.filter(q => q.category === '土地稅法規');

    const perSec = Math.floor(qCount / 4);
    const shuffle = arr => [...arr].sort(() => 0.5 - Math.random());
    
    state.examQuestions = [
      ...shuffle(sec1).slice(0, perSec),
      ...shuffle(sec2).slice(0, perSec),
      ...shuffle(sec3).slice(0, perSec),
      ...shuffle(sec4).slice(0, qCount - perSec * 3)
    ].sort(() => 0.5 - Math.random());

    // 切換 UI
    switchTab('mock-exam');
    document.getElementById('examSetupCard').style.display = 'none';
    document.getElementById('examOngoingArea').style.display = 'block';
    document.getElementById('examResultCard').style.display = 'none';

    renderExamQuestion();
    renderExamNav();
    startExamTimer();
  };

  function startExamTimer() {
    clearInterval(state.examTimer);
    updateTimerDisplay();
    state.examTimer = setInterval(() => {
      state.examSecondsLeft--;
      updateTimerDisplay();
      if (state.examSecondsLeft <= 0) {
        clearInterval(state.examTimer);
        alert('⏰ 時間到！模擬考試自動交卷。');
        submitExam();
      }
    }, 1000);
  }

  function updateTimerDisplay() {
    const timerEl = document.getElementById('examTimerDigits');
    if (!timerEl) return;
    const m = Math.floor(state.examSecondsLeft / 60).toString().padStart(2, '0');
    const s = (state.examSecondsLeft % 60).toString().padStart(2, '0');
    timerEl.textContent = `${m}:${s}`;
    if (state.examSecondsLeft < 300) {
      timerEl.style.color = '#FC8181';
    } else {
      timerEl.style.color = '#FFFFFF';
    }
  }

  function renderExamQuestion() {
    const q = state.examQuestions[state.examCurrentIdx];
    if (!q) return;

    const area = document.getElementById('examQuestionDisplay');
    const userAns = state.examAnswers[q.id];

    let optHtml = q.options.map((opt, i) => {
      const optLetter = ['A', 'B', 'C', 'D'][i];
      const isSelected = userAns === optLetter;
      return `
        <div class="q-opt ${isSelected ? 'selected' : ''}" onclick="selectExamAnswer('${q.id}', '${optLetter}')">
          <span>${opt}</span>
          <span style="font-family:var(--font-mono);font-size:13px;color:var(--ink-muted);">${isSelected ? '● 已選' : '○'}</span>
        </div>
      `;
    }).join('');

    area.innerHTML = `
      <div class="q-card" style="box-shadow:none;border-color:transparent;padding:0;">
        <div class="q-header">
          <div style="display:flex;align-items:center;gap:10px;">
            <span class="q-id">第 ${state.examCurrentIdx + 1} / ${state.examQuestions.length} 題</span>
            <span class="subject-pill pill-sec1">${q.category}</span>
          </div>
          <span style="font-size:13px;font-family:var(--font-mono);color:var(--ink-muted);">${q.id}</span>
        </div>
        <div class="q-title">${q.question}</div>
        <div class="q-options">${optHtml}</div>
      </div>
    `;

    // 更新底部上一題/下一題按鈕
    const prevBtn = document.getElementById('examPrevBtn');
    const nextBtn = document.getElementById('examNextBtn');
    if (prevBtn) prevBtn.disabled = state.examCurrentIdx === 0;
    if (nextBtn) {
      if (state.examCurrentIdx === state.examQuestions.length - 1) {
        nextBtn.textContent = '完成審查';
      } else {
        nextBtn.textContent = '下一題 ➔';
      }
    }
  }

  window.selectExamAnswer = function(qid, optLetter) {
    state.examAnswers[qid] = optLetter;
    renderExamQuestion();
    renderExamNav();
  };

  function renderExamNav() {
    const grid = document.getElementById('examNavGrid');
    if (!grid) return;

    grid.innerHTML = state.examQuestions.map((q, idx) => {
      const isAnswered = !!state.examAnswers[q.id];
      const isCurrent = idx === state.examCurrentIdx;
      return `
        <button class="q-nav-dot ${isAnswered ? 'answered' : ''} ${isCurrent ? 'current' : ''}" onclick="jumpToExamQuestion(${idx})">
          ${idx + 1}
        </button>
      `;
    }).join('');

    // 更新統計已答 / 未答
    const answeredCount = Object.keys(state.examAnswers).length;
    const countEl = document.getElementById('examAnsweredCount');
    if (countEl) countEl.textContent = `已作答：${answeredCount} / ${state.examQuestions.length}`;
  }

  window.jumpToExamQuestion = function(idx) {
    state.examCurrentIdx = idx;
    renderExamQuestion();
    renderExamNav();
  };

  window.examNavPrev = function() {
    if (state.examCurrentIdx > 0) {
      state.examCurrentIdx--;
      renderExamQuestion();
      renderExamNav();
    }
  };

  window.examNavNext = function() {
    if (state.examCurrentIdx < state.examQuestions.length - 1) {
      state.examCurrentIdx++;
      renderExamQuestion();
      renderExamNav();
    }
  };

  window.confirmSubmitExam = function() {
    const answeredCount = Object.keys(state.examAnswers).length;
    const unanswered = state.examQuestions.length - answeredCount;
    let msg = `您已作答 ${answeredCount} 題，尚有 ${unanswered} 題未作答。\n確定現在繳卷並進行系統計分嗎？`;
    if (confirm(msg)) {
      submitExam();
    }
  };

  function submitExam() {
    clearInterval(state.examTimer);
    state.examActive = false;

    let correctCount = 0;
    const totalCount = state.examQuestions.length;
    const mistakes = [];

    const secStats = {
      '民法概要與信託法概要': { correct: 0, total: 0 },
      '土地法規': { correct: 0, total: 0 },
      '土地登記規則與地籍測量': { correct: 0, total: 0 },
      '土地稅法規': { correct: 0, total: 0 }
    };

    state.examQuestions.forEach(q => {
      const uAns = state.examAnswers[q.id];
      if (secStats[q.category]) secStats[q.category].total++;

      if (uAns === q.answer) {
        correctCount++;
        if (secStats[q.category]) secStats[q.category].correct++;
      } else {
        mistakes.push(q);
        // 自動收錄至錯題本
        if (!state.errors.includes(q.id)) {
          state.errors.push(q.id);
        }
      }
    });

    localStorage.setItem('land_agent_errors', JSON.stringify(state.errors));

    // 計算分數（滿分 100）
    const score = Math.round((correctCount / totalCount) * 100);
    const isPass = score >= 60;
    const timeUsedSec = (state.examCount === 50 ? 2700 : 3600) - state.examSecondsLeft;
    const timeSpent = `${Math.floor(timeUsedSec / 60)}分${timeUsedSec % 60}秒`;

    // 紀錄入歷次模考
    const record = {
      date: new Date().toLocaleDateString('zh-TW', { month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' }),
      title: `${totalCount}題全真模擬考`,
      totalQuestions: totalCount,
      score: score,
      correctCount: correctCount,
      timeSpent: timeSpent,
      secStats: secStats
    };
    state.examHistory.push(record);
    localStorage.setItem('land_agent_exam_history', JSON.stringify(state.examHistory));

    // 切換顯示結果
    document.getElementById('examOngoingArea').style.display = 'none';
    const resultCard = document.getElementById('examResultCard');
    resultCard.style.display = 'block';

    resultCard.innerHTML = `
      <div style="text-align:center;padding:32px 20px;border-bottom:1px solid var(--border);">
        <div style="display:inline-block;padding:8px 24px;border-radius:var(--radius-pill);font-size:15px;font-weight:800;margin-bottom:16px;background:${isPass ? 'var(--green-bg)' : 'var(--red-bg)'};color:${isPass ? 'var(--green)' : 'var(--red)'};">
          ${isPass ? '🎉 恭喜通過！達到國家地政士及格標準（60分）！' : '⚠️ 未達及格標準，建議強化弱點科目並多刷錯題！'}
        </div>
        <div style="font-size:68px;font-family:var(--font-mono);font-weight:900;line-height:1;color:${isPass ? 'var(--emerald)' : 'var(--red)'};margin-bottom:10px;">
          ${score} <span style="font-size:24px;color:var(--ink-muted);">/ 100 分</span>
        </div>
        <p style="font-size:15px;color:var(--ink-secondary);">
          答對 <strong>${correctCount}</strong> 題 / 共 ${totalCount} 題 · 耗時 <strong>${timeSpent}</strong> · 產生錯題 <strong>${mistakes.length}</strong> 題（已自動存入錯題本）
        </p>
        <div style="margin-top:20px;display:flex;gap:12px;justify-content:center;flex-wrap:wrap;">
          <button class="btn btn-gold" onclick="startMockExam(${state.examCount})">🔄 再測一次全新模擬考</button>
          <button class="btn btn-secondary" onclick="switchTab('error-book')">❌ 複習本次與歷史錯題 (${state.errors.length})</button>
          <button class="btn btn-secondary" onclick="switchTab('dashboard')">🏠 回總覽儀表板</button>
        </div>
      </div>

      <!-- 四大科診斷分析 -->
      <div style="padding:28px 20px;">
        <h3 style="font-size:18px;margin-bottom:18px;color:var(--ink-primary);">📊 四大專業科目診斷雷達</h3>
        <div class="grid-2">
          ${Object.entries(secStats).map(([cat, s]) => {
            const secScore = s.total > 0 ? Math.round((s.correct / s.total) * 100) : 0;
            return `
              <div style="background:var(--bg-alt);padding:16px;border-radius:var(--radius-sm);border:1px solid var(--border);">
                <div style="display:flex;justify-content:space-between;font-weight:700;font-size:14px;margin-bottom:8px;">
                  <span>${cat}</span>
                  <span style="font-family:var(--font-mono);color:${secScore >= 60 ? 'var(--emerald)' : 'var(--red)'};">${s.correct} / ${s.total} (${secScore}%)</span>
                </div>
                <div class="progress-bar">
                  <div class="progress-fill" style="width:${secScore}%;background:${secScore >= 60 ? 'var(--emerald)' : 'var(--red)'};"></div>
                </div>
              </div>
            `;
          }).join('')}
        </div>
      </div>

      <!-- 本次試卷全部題目與精闢解析逐題檢視 -->
      <div style="padding:28px 20px;background:var(--bg-alt);border-radius:0 0 var(--radius-md) var(--radius-md);">
        <h3 style="font-size:18px;margin-bottom:18px;color:var(--ink-primary);">📝 本次模擬考逐題解析總覽</h3>
        ${state.examQuestions.map((q, idx) => {
          const uAns = state.examAnswers[q.id];
          const isRight = uAns === q.answer;
          return `
            <div class="q-card" style="margin-bottom:16px;">
              <div class="q-header">
                <div style="display:flex;align-items:center;gap:10px;">
                  <span class="q-id">第 ${idx + 1} 題</span>
                  <span class="subject-pill ${isRight ? 'pill-sec2' : 'pill-sec4'}">${isRight ? '✓ 答對' : '✗ 答錯'}</span>
                  <span class="subject-pill pill-sec1">${q.category}</span>
                </div>
                <span style="font-family:var(--font-mono);font-size:13px;color:var(--ink-muted);">${q.id}</span>
              </div>
              <div class="q-title" style="font-size:15px;margin-bottom:14px;">${q.question}</div>
              <div style="font-size:14px;margin-bottom:12px;display:flex;gap:20px;flex-wrap:wrap;">
                <span>您的作答：<strong style="color:${isRight ? 'var(--green)' : 'var(--red)'};">${uAns || '未作答'}</strong></span>
                <span>正確答案：<strong style="color:var(--green);">${q.answer}</strong></span>
              </div>
              <div class="q-analysis" style="margin-top:10px;padding:12px 16px;">
                <div class="law-badge">${q.law}</div>
                <p style="margin-bottom:6px;">${q.explanation}</p>
                <div class="trap-badge">💡 <strong>考點防呆：</strong>${q.trap}</div>
              </div>
            </div>
          `;
        }).join('')}
      </div>
    `;

    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // ══════════════════════════════════════════════════════════
  // 章節循序練習模組 (Practice)
  // ══════════════════════════════════════════════════════════
  function initPractice() {
    renderPracticeQuestions();
    const catSelect = document.getElementById('practiceCatSelect');
    if (catSelect) {
      catSelect.addEventListener('change', () => {
        state.practiceCat = catSelect.value;
        state.practicePage = 1;
        renderPracticeQuestions();
      });
    }

    const searchInput = document.getElementById('practiceSearchInput');
    if (searchInput) {
      searchInput.addEventListener('input', () => {
        state.practiceSearch = searchInput.value.trim().toLowerCase();
        state.practicePage = 1;
        renderPracticeQuestions();
      });
    }
  }

  function getFilteredPracticeQuestions() {
    return ALL_QUESTIONS.filter(q => {
      if (state.practiceCat !== 'ALL' && q.category !== state.practiceCat) return false;
      if (state.practiceSearch) {
        const text = (q.question + q.options.join(' ') + q.law + q.explanation + q.trap).toLowerCase();
        if (!text.includes(state.practiceSearch)) return false;
      }
      return true;
    });
  }

  function renderPracticeQuestions() {
    const container = document.getElementById('practiceQuestionsContainer');
    if (!container) return;

    const filtered = getFilteredPracticeQuestions();
    const totalCount = filtered.length;
    const totalPages = Math.ceil(totalCount / state.pageSize) || 1;
    if (state.practicePage > totalPages) state.practicePage = totalPages;

    const startIdx = (state.practicePage - 1) * state.pageSize;
    const pageQs = filtered.slice(startIdx, startIdx + state.pageSize);

    document.getElementById('practiceCountDisplay').textContent = `符合條件：${totalCount} 題 (第 ${state.practicePage} / ${totalPages} 頁)`;

    if (pageQs.length === 0) {
      container.innerHTML = `<div style="text-align:center;padding:48px 20px;color:var(--ink-muted);background:var(--bg-card);border-radius:var(--radius-md);">無符合搜尋條件之題目。</div>`;
      renderPracticePagination(0, 1);
      return;
    }

    container.innerHTML = pageQs.map(q => {
      const userAns = state.practiceAnswers[q.id];
      const isFav = state.favorites.includes(q.id);
      const isErr = state.errors.includes(q.id);

      let optionsHtml = q.options.map((opt, i) => {
        const optLetter = ['A', 'B', 'C', 'D'][i];
        let optClass = '';
        if (userAns) {
          if (optLetter === q.answer) {
            optClass = 'correct';
          } else if (userAns === optLetter) {
            optClass = 'incorrect';
          }
        }
        return `
          <div class="q-opt ${optClass}" onclick="answerPracticeQuestion('${q.id}', '${optLetter}')">
            <span>${opt}</span>
            <span style="font-family:var(--font-mono);font-size:13px;">
              ${userAns ? (optLetter === q.answer ? '✓ 正確' : (userAns === optLetter ? '✗ 答錯' : '')) : ''}
            </span>
          </div>
        `;
      }).join('');

      let analysisHtml = '';
      if (userAns) {
        analysisHtml = `
          <div class="q-analysis">
            <h5>💡 官方標準解析與法定依據</h5>
            <div class="law-badge">${q.law}</div>
            <p>${q.explanation}</p>
            <div class="trap-badge">⚠️ <strong>考點防呆提示：</strong>${q.trap}</div>
          </div>
        `;
      }

      return `
        <div class="q-card" id="qcard-${q.id}">
          <div class="q-header">
            <div style="display:flex;align-items:center;gap:10px;">
              <span class="q-id">${q.id}</span>
              <span class="subject-pill pill-sec1">${q.category}</span>
            </div>
            <div style="display:flex;align-items:center;gap:8px;">
              <button class="btn btn-secondary btn-sm" onclick="toggleFavorite('${q.id}')" title="標記收藏">
                ${isFav ? '★ 已收藏' : '☆ 收藏'}
              </button>
              <button class="btn btn-secondary btn-sm" onclick="toggleErrorManual('${q.id}')" title="加入或移出租題本">
                ${isErr ? '❌ 已在錯題本' : '➕ 標為錯題'}
              </button>
            </div>
          </div>
          <div class="q-title">${q.question}</div>
          <div class="q-options">${optionsHtml}</div>
          ${analysisHtml}
        </div>
      `;
    }).join('');

    renderPracticePagination(totalCount, totalPages);
  }

  function renderPracticePagination(totalCount, totalPages) {
    const pagEl = document.getElementById('practicePagination');
    if (!pagEl) return;
    if (totalPages <= 1) {
      pagEl.innerHTML = '';
      return;
    }

    pagEl.innerHTML = `
      <div style="display:flex;align-items:center;justify-content:center;gap:10px;margin-top:24px;">
        <button class="btn btn-secondary btn-sm" onclick="changePracticePage(${state.practicePage - 1})" ${state.practicePage === 1 ? 'disabled' : ''}>◀ 上一頁</button>
        <span style="font-family:var(--font-mono);font-size:14px;font-weight:700;">${state.practicePage} / ${totalPages}</span>
        <button class="btn btn-secondary btn-sm" onclick="changePracticePage(${state.practicePage + 1})" ${state.practicePage === totalPages ? 'disabled' : ''}>下一頁 ▶</button>
      </div>
    `;
  }

  window.changePracticePage = function(p) {
    state.practicePage = p;
    renderPracticeQuestions();
    window.scrollTo({ top: 180, behavior: 'smooth' });
  };

  window.answerPracticeQuestion = function(qid, optLetter) {
    state.practiceAnswers[qid] = optLetter;
    localStorage.setItem('land_agent_practice_answers', JSON.stringify(state.practiceAnswers));

    const q = ALL_QUESTIONS.find(item => item.id === qid);
    if (q) {
      if (optLetter !== q.answer) {
        if (!state.errors.includes(qid)) {
          state.errors.push(qid);
          localStorage.setItem('land_agent_errors', JSON.stringify(state.errors));
        }
      }
    }
    renderPracticeQuestions();
  };

  window.toggleFavorite = function(qid) {
    if (state.favorites.includes(qid)) {
      state.favorites = state.favorites.filter(id => id !== qid);
    } else {
      state.favorites.push(qid);
    }
    localStorage.setItem('land_agent_favorites', JSON.stringify(state.favorites));
    renderPracticeQuestions();
  };

  window.toggleErrorManual = function(qid) {
    if (state.errors.includes(qid)) {
      state.errors = state.errors.filter(id => id !== qid);
    } else {
      state.errors.push(qid);
    }
    localStorage.setItem('land_agent_errors', JSON.stringify(state.errors));
    renderPracticeQuestions();
  };

  // ══════════════════════════════════════════════════════════
  // 錯題筆記本模組 (Error Notebook)
  // ══════════════════════════════════════════════════════════
  function initErrorBook() {}

  function renderErrorBook() {
    const countEl = document.getElementById('errorBookCountBadge');
    const container = document.getElementById('errorBookQuestionsContainer');
    if (!container) return;

    if (countEl) countEl.textContent = `${state.errors.length} 題`;

    if (state.errors.length === 0) {
      container.innerHTML = `
        <div style="text-align:center;padding:56px 20px;background:var(--bg-card);border-radius:var(--radius-md);border:1px solid var(--border);">
          <div style="font-size:48px;margin-bottom:12px;">🏆</div>
          <h3 style="font-size:20px;margin-bottom:8px;color:var(--emerald);">太棒了！目前錯題本空空如也！</h3>
          <p style="color:var(--ink-secondary);max-width:500px;margin:0 auto 20px;">
            在全真模擬考或章節練習中答錯的題目會自動匯集於此。現在就去挑戰模擬考吧！
          </p>
          <button class="btn btn-gold" onclick="startMockExam(50)">🚀 開始 50 題衝刺模擬考</button>
        </div>
      `;
      return;
    }

    const errQuestions = state.errors.map(id => ALL_QUESTIONS.find(q => q.id === id)).filter(Boolean);

    container.innerHTML = errQuestions.map((q, idx) => {
      return `
        <div class="q-card" style="border-left:4px solid var(--red);">
          <div class="q-header">
            <div style="display:flex;align-items:center;gap:10px;">
              <span class="q-id" style="color:var(--red);background:var(--red-bg);">錯題 #${idx + 1} (${q.id})</span>
              <span class="subject-pill pill-sec1">${q.category}</span>
            </div>
            <button class="btn btn-secondary btn-sm" onclick="removeError('${q.id}')">✓ 已熟記，移出租題本</button>
          </div>
          <div class="q-title">${q.question}</div>
          <div class="q-options">
            ${q.options.map((opt, i) => {
              const optLetter = ['A', 'B', 'C', 'D'][i];
              const isCorrect = optLetter === q.answer;
              return `
                <div class="q-opt ${isCorrect ? 'correct' : ''}">
                  <span>${opt}</span>
                  <span style="font-family:var(--font-mono);font-size:12px;">${isCorrect ? '★ 正確答案' : ''}</span>
                </div>
              `;
            }).join('')}
          </div>
          <div class="q-analysis">
            <div class="law-badge">${q.law}</div>
            <p>${q.explanation}</p>
            <div class="trap-badge">💡 <strong>防呆重點：</strong>${q.trap}</div>
          </div>
        </div>
      `;
    }).join('');
  }

  window.removeError = function(qid) {
    state.errors = state.errors.filter(id => id !== qid);
    localStorage.setItem('land_agent_errors', JSON.stringify(state.errors));
    renderErrorBook();
  };

  window.clearAllErrors = function() {
    if (state.errors.length === 0) return;
    if (confirm('確定要清空所有錯題記錄嗎？')) {
      state.errors = [];
      localStorage.setItem('land_agent_errors', JSON.stringify(state.errors));
      renderErrorBook();
    }
  };

  // ══════════════════════════════════════════════════════════
  // 全題庫關鍵字即時檢索 (Search)
  // ══════════════════════════════════════════════════════════
  function initSearch() {
    const input = document.getElementById('globalSearchInput');
    if (!input) return;

    input.addEventListener('input', () => {
      const keyword = input.value.trim().toLowerCase();
      performSearch(keyword);
    });
  }

  function performSearch(keyword) {
    const resultsContainer = document.getElementById('searchResultsContainer');
    const countBadge = document.getElementById('searchResultCount');
    if (!resultsContainer) return;

    if (!keyword) {
      resultsContainer.innerHTML = `<div style="text-align:center;padding:48px 20px;color:var(--ink-muted);background:var(--bg-card);border-radius:var(--radius-md);">請在上方輸入關鍵字（例如：「房地合一」、「34條之1」、「信託」、「抵押權」、「重購退稅」）。</div>`;
      if (countBadge) countBadge.textContent = '0 題';
      return;
    }

    const matches = ALL_QUESTIONS.filter(q => {
      const content = (q.id + ' ' + q.question + ' ' + q.options.join(' ') + ' ' + q.law + ' ' + q.explanation + ' ' + q.trap).toLowerCase();
      return content.includes(keyword);
    });

    if (countBadge) countBadge.textContent = `${matches.length} 題`;

    if (matches.length === 0) {
      resultsContainer.innerHTML = `<div style="text-align:center;padding:48px 20px;color:var(--ink-muted);background:var(--bg-card);border-radius:var(--radius-md);">查無包含「${keyword}」的考題。</div>`;
      return;
    }

    resultsContainer.innerHTML = matches.slice(0, 50).map(q => {
      return `
        <div class="q-card">
          <div class="q-header">
            <div style="display:flex;align-items:center;gap:10px;">
              <span class="q-id">${q.id}</span>
              <span class="subject-pill pill-sec1">${q.category}</span>
            </div>
            <span style="font-family:var(--font-mono);font-size:13px;color:var(--green);font-weight:700;">答案：${q.answer}</span>
          </div>
          <div class="q-title">${highlightKeyword(q.question, keyword)}</div>
          <div class="q-options">
            ${q.options.map((opt, i) => {
              const optLetter = ['A', 'B', 'C', 'D'][i];
              const isCorrect = optLetter === q.answer;
              return `
                <div class="q-opt ${isCorrect ? 'correct' : ''}">
                  <span>${highlightKeyword(opt, keyword)}</span>
                  <span>${isCorrect ? '★ 正確' : ''}</span>
                </div>
              `;
            }).join('')}
          </div>
          <div class="q-analysis">
            <div class="law-badge">${highlightKeyword(q.law, keyword)}</div>
            <p>${highlightKeyword(q.explanation, keyword)}</p>
            <div class="trap-badge">💡 <strong>防呆重點：</strong>${highlightKeyword(q.trap, keyword)}</div>
          </div>
        </div>
      `;
    }).join('');
  }

  function highlightKeyword(text, keyword) {
    if (!keyword) return text;
    const reg = new RegExp(`(${keyword})`, 'gi');
    return text.replace(reg, '<mark style="background:#FFEAA7;padding:1px 4px;border-radius:2px;">$1</mark>');
  }

  // ══════════════════════════════════════════════════════════
  // 高頻數字速記卡模組 (Flashcards)
  // ══════════════════════════════════════════════════════════
  const CARDS_DATA = [
    { num: "3日", title: "稅捐逾期繳納加徵滯納金起算基準", cat: "days", law: "稅捐稽徵法§20", tip: "每逾 3 日加徵 1% 滯納金，最高以 10% 為限。" },
    { num: "3日", title: "契稅逾期申報加徵怠報金起算基準", cat: "days", law: "契稅條例§24", tip: "每逾 3 日加徵 1% 怠報金，最高以 15,000 元為限。" },
    { num: "15日", title: "土地登記申請案件法定補正期間", cat: "days", law: "土地登記規則§56", tip: "開具補正通知書一次通知，申請人應於 15 日內完成補正，逾期駁回。" },
    { num: "15日", title: "建物所有權第一次登記（保存登記）公告期", cat: "days", law: "土地登記規則§72", tip: "地政機關審查無誤後公告 15 日，期滿無人異議即發權狀。" },
    { num: "15日", title: "土地徵收地價補償費發給完竣之期限", cat: "days", law: "土地徵收條例§20", tip: "公告期滿後 15 日內必須發放完竣，逾期未發徵收案失其效力！" },
    { num: "15日", title: "共有土地處分通知他共有人行使優先購買權確答期", cat: "days", law: "土地法§34-1第4項", tip: "收到書面通知後 15 日內未確答表示購買者，視為放棄優先購買權。" },
    { num: "30日", title: "土地移轉現值申報期限（享訂約日現值審核）", cat: "days", law: "土地稅法§30", tip: "訂約日起 30 日內申報者，以訂約日當期公告土地現值為移轉現值。" },
    { num: "30日", title: "契稅法定申報期限", cat: "days", law: "契稅條例§16", tip: "買賣、贈與契約成立之日起 30 日內，向房屋所在地稅捐機關申報。" },
    { num: "30日", title: "房地合一稅交易申報期限", cat: "days", law: "所得稅法§14-5", tip: "房屋土地完成移轉登記日次日起算 30 日內即時申報（虧損亦同）。" },
    { num: "30日", title: "預售屋解約申報實價登錄時限", cat: "days", law: "平均地權條例§47-3", tip: "預售屋買賣解約日起 30 日內申報登錄，違者處 3 萬至 15 萬元罰鍰。" },
    { num: "40日", title: "地價稅自用住宅用地特別稅率申請時限", cat: "days", law: "土地稅法§41", tip: "每年地價稅開徵 40 日前（即 9 月 22 日前）提出申請，逾期次年適用。" },
    { num: "3個月", title: "繼承人向法院聲請「拋棄繼承」除斥期間", cat: "days", law: "民法§1174", tip: "繼承人得拋棄其繼承權，應於知悉其得繼承之時起 3 個月內為之。" },
    { num: "6個月", title: "被繼承人死亡申報遺產稅法定期限", cat: "days", law: "遺贈稅法§23", tip: "被繼承人死亡之日起 6 個月內申報；有正當理由得申請延長 3 個月。" },
    { num: "6個月", title: "向地政事務所申辦繼承登記之法定期限", cat: "days", law: "土地法§73", tip: "自繼承開始起 6 個月內申辦，逾 1 個月加罰規費 1 倍，最高 20 倍。" },
    { num: "1年", title: "土增稅一生一次自用住宅出售前無出租營業限制", cat: "years", law: "土地稅法§34", tip: "出售前 1 年內未曾供營業使用或出租，享 10% 優惠稅率。" },
    { num: "2年", title: "土增稅與房地合一稅自住房地重購退稅先後期限", cat: "years", law: "土地稅法§35/所稅§14-8", tip: "先買後賣或先賣後買均限於 2 年內完成重購與出售！" },
    { num: "2年", title: "不動產評價委員會重評房屋標準價格週期（最新修正）", cat: "years", law: "房屋稅條例§11", tip: "最新修法由 3 年改為每 2 年重評一次房屋標準價格！" },
    { num: "4年", title: "地政士開業執照之有效期限", cat: "years", law: "地政士法§10", tip: "開業執照有效期間為 4 年，期滿換發應檢附 30 小時以上專業訓練證明。" },
    { num: "5年", title: "重購退還土增稅及房地合一稅之主管機關列管年限", cat: "years", law: "土地稅法§37/所稅§14-8", tip: "登記日起 5 年內不得改作其他用途、出租、營業或再行移轉，違者追繳！" },
    { num: "5年", title: "私法人買受住宅用房屋許可制管制年限", cat: "years", law: "平均地權條例§79-1", tip: "私法人經許可取得住宅用房屋，登記後 5 年內不得移轉或預告登記！" },
    { num: "6年", title: "土增稅一生一屋及房地合一自住優惠連續設籍持有年限", cat: "years", law: "土稅§34/所稅§4-5", tip: "連續設籍自住滿 6 年，無出租營業，房地合一享 400 萬免稅與超額 10%！" },
    { num: "2‰", title: "地價稅自用住宅用地特別稅率", cat: "rates", law: "土地稅法§17", tip: "千分之二單一稅率，不累進！都 3 非 7 面積限制，本人配偶未成年限 1 處。" },
    { num: "1.0%", title: "全國單一自住房屋房屋稅優惠稅率（囤房稅2.0）", cat: "rates", law: "房屋稅條例§5", tip: "全國僅 1 戶且房屋現值在一定金額以下，房屋稅率降至 1.0%！" },
    { num: "2.0%~4.8%", title: "非自住住家用房屋全國歸戶差別稅率（囤房稅2.0）", cat: "rates", law: "房屋稅條例§5", tip: "打破縣市藩籬，採全國合併單一歸戶，全數累進課徵重稅！" },
    { num: "10%", title: "土地增值稅自用住宅用地（一生一次/一生一屋）稅率", cat: "rates", law: "土地稅法§34", tip: "自用住宅用地土增稅率一律為單一 10%（一般稅率為 20%、30%、40%）。" },
    { num: "45%", title: "房地合一稅 2.0 持有 2 年以內交易稅率", cat: "rates", law: "所得稅法§14-4", tip: "持有 2 年以內短期交易課 45%；2 至 5 年課 35%；5 至 10 年課 20%；逾 10 年 15%。" },
    { num: "400萬元", title: "房地合一 2.0 自住房地課稅所得免稅額", cat: "amounts", law: "所得稅法§4-5", tip: "設籍自住滿 6 年無出租營業，課稅獲利 400 萬以內全免稅，超額僅課 10%！" },
    { num: "1,333萬元", title: "遺產稅一般免稅額（現行公告標準）", cat: "amounts", law: "遺贈稅法§12-1", tip: "每位被繼承人一般免稅額為 1,333 萬元；軍公教因公殉職加倍為 2,666 萬元。" },
    { num: "244萬元", title: "贈與稅每人每年免稅額", cat: "amounts", law: "遺贈稅法§22", tip: "每位贈與人每年累計贈與他人免稅額度為 244 萬元（1/1 至 12/31 止）。" },
    { num: "5,000萬元", title: "平均地權條例炒作不動產行為之最高罰鍰", cat: "amounts", law: "平均地權條例§47-5", tip: "散布不實訊息、通謀虛偽交易炒作房價，處 100 萬至 5,000 萬元罰鍰並得連續罰！" }
  ];

  function initFlashcards() {
    renderFlashcards('all');
    const filterBtns = document.querySelectorAll('.fc-filter-btn');
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        renderFlashcards(btn.getAttribute('data-fc-cat'));
      });
    });
  }

  function renderFlashcards(category) {
    const grid = document.getElementById('flashcardGrid');
    if (!grid) return;

    const filtered = category === 'all' ? CARDS_DATA : CARDS_DATA.filter(c => c.cat === category);

    grid.innerHTML = filtered.map(c => {
      return `
        <div class="flashcard">
          <div>
            <div class="fc-number">${c.num}</div>
            <div class="fc-title">${c.title}</div>
            <div class="fc-law">${c.law}</div>
          </div>
          <div class="fc-tip">💡 ${c.tip}</div>
        </div>
      `;
    }).join('');
  }

  // ══════════════════════════════════════════════════════════
  // 四大考科深度講義 (Notes Reader)
  // ══════════════════════════════════════════════════════════
  function initNotes() {
    loadNote('00-study-guide');
    const noteBtns = document.querySelectorAll('.note-select-btn');
    noteBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        noteBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        loadNote(btn.getAttribute('data-note'));
      });
    });
  }

  const NOTES_STORE = {
    '00-study-guide': `
      <h1>地政士（土地登記專業代理人）專技普考：通關全戰略指南與讀書計畫</h1>
      <blockquote><strong>目標：一次上榜、穩拿 75+ 高分！</strong> 地政士專技普考兼具高度法律專業度與市場獨佔執業權，是不動產產權移轉、節稅規劃與資產傳承領域含金量最高之國家專業證照。</blockquote>
      <hr style="margin:20px 0;border:0;border-top:1px solid var(--border);">
      <h2>壹、考試制度與及格標準</h2>
      <ul>
        <li><strong>及格標準</strong>：採<strong>總成績滿 60 分及格</strong>（總成績以各應試科目成績平均計算）。</li>
        <li><strong>零分限制</strong>：應試科目中有一科成績為 0 分者，不予及格。</li>
        <li><strong>專業科目限制</strong>：專業科目平均成績未滿 50 分者，不予及格。</li>
      </ul>
      <h2>貳、四大專業科目得分戰略</h2>
      <table>
        <tr><th>專業科目</th><th>目標分數</th><th>核心考點重點</th></tr>
        <tr><td><strong>民法概要與信託法概要</strong></td><td>65 ~ 75 分</td><td>總則意思表示/代理、物權共有物處分/抵押權、債編買賣/租賃/侵權、親屬繼承特留分與夫妻財產制；信託財產獨立性與受託人義務。</td></tr>
        <tr><td><strong>土地法規</strong></td><td>70 ~ 80 分</td><td>土地法第34條之1多數決處分與優先購買權、第73條之1未辦繼承列管代管、平均地權條例打炒房禁轉售罰5000萬、土地徵收協議價購與補償、地政士懲戒罰則。</td></tr>
        <tr><td><strong>土地登記規則與測量</strong></td><td>75 ~ 85 分</td><td>土地登記總則單獨申請24款、繼承登記與代位繼承、抵押權塗銷與次序讓與、預告登記與查封限制登記、建物保存登記、鑑界與地籍圖重測。</td></tr>
        <tr><td><strong>土地稅法規</strong></td><td>80 ~ 90 分</td><td>土增稅一生一次與一生一屋、重購退稅要件與5年列管、地價稅2‰自用、囤房稅2.0全國歸戶單一自住1%/非自住2.0%~4.8%、契稅6大稅率、遺贈稅免稅額與生前2年贈與併計、房地合一2.0四級距與自住400萬免稅。</td></tr>
      </table>
    `,
    '01-civil-and-trust': `
      <h1>第一科：民法概要與信託法概要深度實務講義</h1>
      <blockquote><strong>核心地位</strong>：民法為萬法之母，地政士處理之產權移轉、借貸設定、共有物分割與遺產繼承，全部深植於民法架構。信託法則為高資產規劃之必備工具。</blockquote>
      <hr style="margin:20px 0;border:0;border-top:1px solid var(--border);">
      <h2>一、權利主體與行為能力</h2>
      <ul>
        <li><strong>自然人權利能力</strong>（民法§6）：始於出生，終於死亡。胎兒關於個人利益之保護視為既已出生，但死產者無溯及之效力。</li>
        <li><strong>行為能力分級</strong>：未滿 7 歲為無行為能力人；滿 7 歲未滿 18 歲為限制行為能力人；滿 18 歲為成年完全行為能力人。</li>
        <li><strong>契約行為</strong>：限制行為能力人未得法代允許所為之契約行為，處於<strong>效力未定</strong>狀態。單獨行為未得允許者自始<strong>無效</strong>。</li>
      </ul>
      <h2>二、意思表示瑕疵與消滅時效</h2>
      <ul>
        <li><strong>通謀虛偽意思表示</strong>（§87）：無效，但不得以其無效對抗善意第三人。</li>
        <li><strong>消滅時效</strong>：一般請求權 15 年；定期給付債權（利息、租金）5 年；日常短期債權（地政士代書費）2 年。</li>
      </ul>
      <h2>三、物權共有物處分（民法§819 vs 土地法§34-1）</h2>
      <ul>
        <li><strong>應有部分處分</strong>（§819第1項）：得自由處分，毋須其他共有人同意。</li>
        <li><strong>共有物全筆多數決處分</strong>（土地法§34-1）：人數過半數且持分合計過半數；或持分合計逾三分之二者人數不予計算。須書面通知他共有人，他共有人享有 15 日優先購買權。</li>
      </ul>
      <h2>四、信託法重點</h2>
      <ul>
        <li><strong>信託財產獨立性</strong>（信託法§12）：信託財產原則不得強制執行。信託財產不屬於受託人之遺產或破產財團。</li>
        <li><strong>受託人義務</strong>：負善良管理人之注意義務、忠實義務與分別管理義務。</li>
      </ul>
    `,
    '02-land-laws': `
      <h1>第二科：土地法規與平均地權條例深度講義</h1>
      <blockquote><strong>核心地位</strong>：土地法規為土地行政與地政士執業之準繩，涵蓋產權取得、土地使用分區、打炒房平均地權新制、土地徵收補償及地政士法規範。</blockquote>
      <hr style="margin:20px 0;border:0;border-top:1px solid var(--border);">
      <h2>一、土地分類與地權限制</h2>
      <ul>
        <li><strong>土地四大分類</strong>（土地法§2）：第一類建築用地、第二類直接生產用地、第三類交通水利用地、第四類其他土地。</li>
        <li><strong>未辦繼承登記土地列管</strong>（土地法§73-1）：逾 1 年未辦繼承，公告 3 個月；列冊管理 <strong>15 年</strong>，期滿移送國產署公開標售，價款專戶保管 <strong>10 年</strong>。</li>
      </ul>
      <h2>二、平均地權條例（打炒房與實價登錄 2.0）</h2>
      <ul>
        <li><strong>預售屋禁止轉售換約</strong>：買受人除配偶、直系血親、二親等旁系血親外不得讓與第三人。違者每戶處 <strong>50 萬至 300 萬元罰鍰</strong>。</li>
        <li><strong>重罰不動產炒作行為</strong>：散布不實訊息、造假熱銷炒作，最高處 <strong>100 萬至 5,000 萬元罰鍰</strong>並得連續處罰！</li>
        <li><strong>私法人購屋許可制</strong>：私法人買受住宅用房屋非經許可不得取得，取得後 <strong>5 年內不得移轉</strong>。</li>
      </ul>
      <h2>三、地政士法執業規範</h2>
      <ul>
        <li><strong>執照有效期間</strong>：開業執照有效期間為 <strong>4 年</strong>。換發執照需受訓 <strong>30 小時以上</strong>。</li>
        <li><strong>懲戒處分</strong>：警告、申誡、停止執行業務（2個月至2年）、除名。懲戒權 3 年不行使消滅。</li>
      </ul>
    `,
    '03-land-registration': `
      <h1>第三科：土地登記規則與地籍測量實務講義</h1>
      <blockquote><strong>核心地位</strong>：土地登記規則是地政士的立足之本！土地登記牽涉物權絕對公示與公信力，地政士收件、補正、駁回、審查實務皆以此為標準作業程序。</blockquote>
      <hr style="margin:20px 0;border:0;border-top:1px solid var(--border);">
      <h2>一、土地登記簿三大部別</h2>
      <ul>
        <li><strong>標示部</strong>：記載不動產物理現況（地段、地號、門牌、面積、使用分區）。</li>
        <li><strong>所有權部</strong>：記載產權人姓名、持分範圍、登記原因、原因發生日期。</li>
        <li><strong>他項權利部</strong>：記載抵押權、地上權、不動產役權、典權之負擔與擔保債權金額。</li>
      </ul>
      <h2>二、法定補正與駁回</h2>
      <ul>
        <li><strong>補正期間</strong>（土登§56）：登記機關開立補正通知書，申請人應於接到通知日起 <strong>15 日內</strong> 補正。</li>
        <li><strong>駁回事由</strong>（土登§57）：逾 15 日未補正、補正不完全、不能補正者，以書面敘明理由駁回。</li>
      </ul>
      <h2>三、單獨申請登記（土登§27 核心）</h2>
      <ul>
        <li>土地總登記、建物所有權第一次登記（保存登記）。</li>
        <li><strong>繼承登記</strong>（任何繼承人得為全體繼承人之利益單獨申請）。</li>
        <li>因法院拍賣、判決確定之登記。</li>
        <li>預告登記及其塗銷登記。</li>
      </ul>
      <h2>四、限制登記效力</h2>
      <ul>
        <li><strong>查封、假扣押</strong>：經法院囑託辦竣查封登記後，在法院撤銷前，地政機關絕對<strong>不得受理任何移轉或抵押設定登記</strong>，違者依法駁回！</li>
      </ul>
    `,
    '04-land-tax-laws': `
      <h1>第四科：土地稅法規與房地合一 2.0 節稅講義</h1>
      <blockquote><strong>核心地位</strong>：土地稅法是地政士最具高經濟價值之專業科目！熟稔自用住宅優惠、囤房稅 2.0、遺贈稅節稅與房地合一 2.0 規避重稅，是客戶指名頂尖地政士的關鍵！</blockquote>
      <hr style="margin:20px 0;border:0;border-top:1px solid var(--border);">
      <h2>一、地價稅</h2>
      <ul>
        <li><strong>納稅基準日</strong>：每年 <strong>8 月 31 日</strong>；徵收期間為每年 11 月 1 日至 30 日。</li>
        <li><strong>自用住宅用地特別稅率</strong>：<strong>千分之二（2‰）</strong>。開徵 40 日前（即 <strong>9 月 22 日前</strong>）申請。</li>
      </ul>
      <h2>二、土地增值稅</h2>
      <ul>
        <li><strong>一生一次自用住宅（10%）</strong>：都 3 非 7，出售前 1 年無出租營業。每人一生限一次。</li>
        <li><strong>一生一屋自用住宅（10%）</strong>：都 1.5 非 3.5，持有滿 6 年且設籍連續滿 6 年，出售前 5 年無出租營業。</li>
        <li><strong>重購退稅</strong>（土稅§35）：先買後賣或先賣後買限 <strong>2 年內</strong>。列管管制 <strong>5 年</strong>（不得出租營業或戶籍遷出）。</li>
      </ul>
      <h2>三、房屋稅條例（囤房稅 2.0 最新制）</h2>
      <ul>
        <li><strong>全國單一自住</strong>：降至 <strong>1.0%</strong>（全國僅 1 戶且現值合格）。</li>
        <li><strong>自住住家</strong>：<strong>1.2%</strong>（本人配偶直系設籍自住，全國限 3 戶）。</li>
        <li><strong>非自住住家</strong>：<strong>2.0% ~ 4.8%</strong>（全國單一歸戶、全數累進課徵重稅！）。</li>
      </ul>
      <h2>四、房地合一稅 2.0</h2>
      <ul>
        <li><strong>持有稅率</strong>：2 年以內 <strong>45%</strong>；2 至 5 年 <strong>35%</strong>；5 至 10 年 <strong>20%</strong>；逾 10 年 <strong>15%</strong>。</li>
        <li><strong>自住房地優惠</strong>：設籍自住連續滿 6 年，<strong>課稅所得 400 萬以內免稅</strong>，超額部分僅課 <strong>10%</strong>。</li>
        <li><strong>申報期限</strong>：完成移轉登記日之<strong>次日起算 30 日內</strong>申報繳納（虧損亦同）。</li>
      </ul>
    `
  };

  function loadNote(noteKey) {
    const viewer = document.getElementById('noteContentArea');
    if (viewer && NOTES_STORE[noteKey]) {
      viewer.innerHTML = NOTES_STORE[noteKey];
      window.scrollTo({ top: 180, behavior: 'smooth' });
    }
  }

})();
