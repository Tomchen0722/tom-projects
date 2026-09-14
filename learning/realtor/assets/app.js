// 不動產經紀營業員測驗系統核心邏輯
(function() {
  'use strict';

  // 題庫資料
  const ALL_QUESTIONS = window.QUESTION_BANK || [];
  
  // 狀態管理
  let state = {
    theme: localStorage.getItem('realtor_theme') || 'light',
    currentTab: 'dashboard',
    
    // 練習狀態
    practiceCat: 'ALL',
    practiceIndex: 0,
    practiceAnswers: {},
    
    // 錯題本 (儲存 ID 陣列)
    errors: JSON.parse(localStorage.getItem('realtor_errors') || '[]'),
    favorites: JSON.parse(localStorage.getItem('realtor_favorites') || '[]'),
    
    // 模擬考狀態
    examActive: false,
    examQuestions: [],
    examAnswers: {},
    examTimer: null,
    examSecondsLeft: 3600, // 60 分鐘
    examHistory: JSON.parse(localStorage.getItem('realtor_exam_history') || '[]')
  };

  // 初始化 DOM
  document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initNavigation();
    initDashboard();
    initPractice();
    initErrorBook();
    initSearch();
    initFlashcards();
  });

  // 主題切換
  function initTheme() {
    document.documentElement.setAttribute('data-theme', state.theme);
    const themeBtn = document.getElementById('themeToggleBtn');
    if (themeBtn) {
      themeBtn.textContent = state.theme === 'dark' ? '☀️' : '🌙';
      themeBtn.addEventListener('click', () => {
        state.theme = state.theme === 'dark' ? 'light' : 'dark';
        localStorage.setItem('realtor_theme', state.theme);
        document.documentElement.setAttribute('data-theme', state.theme);
        themeBtn.textContent = state.theme === 'dark' ? '☀️' : '🌙';
      });
    }
  }

  // 導航標籤切換
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
    state.currentTab = tabId;
    document.querySelectorAll('.nav-btn').forEach(b => {
      b.classList.toggle('active', b.getAttribute('data-tab') === tabId);
    });
    document.querySelectorAll('.view-section').forEach(sec => {
      sec.classList.toggle('active', sec.id === `tab-${tabId}`);
    });
    window.scrollTo({ top: 0, behavior: 'smooth' });

    if (tabId === 'dashboard') updateDashboardStats();
    if (tabId === 'error-book') renderErrorBook();
  }
  window.switchTab = switchTab;

  // 儀表板
  function initDashboard() {
    updateDashboardStats();
  }

  function updateDashboardStats() {
    document.getElementById('statTotalQuestions').textContent = ALL_QUESTIONS.length.toLocaleString();
    document.getElementById('statErrorCount').textContent = state.errors.length.toLocaleString();
    
    // 計算歷史最高分
    let bestScore = 0;
    if (state.examHistory.length > 0) {
      bestScore = Math.max(...state.examHistory.map(h => h.score));
    }
    document.getElementById('statBestScore').textContent = bestScore + ' 分';

    // 歷次模擬考紀錄表格
    const historyTbody = document.getElementById('examHistoryTbody');
    if (historyTbody) {
      if (state.examHistory.length === 0) {
        historyTbody.innerHTML = '<tr><td colspan="5" style="text-align:center;padding:20px;color:var(--ink-muted);">尚未進行全真模擬考，立刻開始測驗！</td></tr>';
      } else {
        historyTbody.innerHTML = state.examHistory.slice(-5).reverse().map((h, i) => `
          <tr style="border-bottom:1px solid var(--border);">
            <td style="padding:10px 14px;">${h.date}</td>
            <td style="padding:10px 14px;font-weight:bold;color:${h.score >= 60 ? 'var(--green)' : 'var(--red)'};">${h.score} 分</td>
            <td style="padding:10px 14px;">${h.score >= 60 ? '🎉 及格通過' : '⚠️ 未達標準'}</td>
            <td style="padding:10px 14px;">${h.usedTime}</td>
            <td style="padding:10px 14px;">${h.correctCount} / 100</td>
          </tr>
        `).join('');
      }
    }
  }

  // ══════════════════════════════════════════════════════════════
  // 全真模擬考試模組 (100題, 60分鐘, 隨機抽選)
  // ══════════════════════════════════════════════════════════════
  window.startMockExam = function() {
    if (ALL_QUESTIONS.length < 100) return;
    
    // 隨機抽選 100 題
    const shuffled = [...ALL_QUESTIONS].sort(() => 0.5 - Math.random());
    state.examQuestions = shuffled.slice(0, 100);
    state.examAnswers = {};
    state.examSecondsLeft = 3600; // 60 分鐘
    state.examActive = true;

    document.getElementById('examStartCard').style.display = 'none';
    document.getElementById('examActiveArea').style.display = 'block';

    renderExamQuestions();
    startExamTimer();
    switchTab('mock-exam');
  };

  function startExamTimer() {
    if (state.examTimer) clearInterval(state.examTimer);
    const timerElem = document.getElementById('examTimer');
    
    state.examTimer = setInterval(() => {
      state.examSecondsLeft--;
      const mins = Math.floor(state.examSecondsLeft / 60);
      const secs = state.examSecondsLeft % 60;
      timerElem.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
      
      if (state.examSecondsLeft <= 0) {
        clearInterval(state.examTimer);
        alert('時間到！系統將自動為您交卷評分。');
        submitMockExam();
      }
    }, 1000);
  }

  function renderExamQuestions() {
    const list = document.getElementById('examQuestionsList');
    list.innerHTML = state.examQuestions.map((q, idx) => `
      <div class="question-item" id="exam-q-${idx}">
        <div class="q-header">
          <span class="q-id">第 ${idx + 1} 題 / 100 · ${q.id}</span>
          <span class="q-cat">${q.category}</span>
        </div>
        <div class="q-text">${q.question}</div>
        <div class="options-list">
          ${q.options.map((opt, optIdx) => {
            const letter = ['A', 'B', 'C', 'D'][optIdx];
            return `
              <button class="opt-btn" id="exam-opt-${idx}-${letter}" onclick="selectExamOption(${idx}, '${letter}')">
                ${opt}
              </button>
            `;
          }).join('')}
        </div>
      </div>
    `).join('');
    updateExamProgressTracker();
  }

  window.selectExamOption = function(qIdx, letter) {
    if (!state.examActive) return;
    state.examAnswers[qIdx] = letter;

    ['A', 'B', 'C', 'D'].forEach(l => {
      const btn = document.getElementById(`exam-opt-${qIdx}-${l}`);
      if (btn) {
        btn.classList.toggle('correct', l === letter);
      }
    });
    updateExamProgressTracker();
  };

  function updateExamProgressTracker() {
    const answered = Object.keys(state.examAnswers).length;
    document.getElementById('examAnsweredCount').textContent = `已作答：${answered} / 100 題`;
  }

  window.submitMockExam = function() {
    if (!state.examActive) return;
    
    const answeredCount = Object.keys(state.examAnswers).length;
    if (answeredCount < 100 && state.examSecondsLeft > 0) {
      if (!confirm(`您還有 ${100 - answeredCount} 題尚未作答，確定現在交卷嗎？`)) {
        return;
      }
    }

    clearInterval(state.examTimer);
    state.examActive = false;

    // 計算分數
    let correctCount = 0;
    state.examQuestions.forEach((q, idx) => {
      const userAns = state.examAnswers[idx];
      const isCorrect = userAns === q.answer;
      if (isCorrect) {
        correctCount++;
      } else {
        // 加入錯題本
        if (!state.errors.includes(q.id)) {
          state.errors.push(q.id);
        }
      }

      // 揭示答案與解析
      const card = document.getElementById(`exam-q-${idx}`);
      if (card) {
        ['A', 'B', 'C', 'D'].forEach(l => {
          const btn = document.getElementById(`exam-opt-${idx}-${l}`);
          if (btn) {
            btn.classList.remove('correct', 'wrong');
            if (l === q.answer) btn.classList.add('correct');
            if (l === userAns && userAns !== q.answer) btn.classList.add('wrong');
          }
        });

        // 插入解析區塊
        const expDiv = document.createElement('div');
        expDiv.className = 'exp-box';
        expDiv.innerHTML = `
          <div class="exp-law">⚖️ 法規依據：${q.law}（標準答案：${q.answer}，您答：${userAns || '未作答'}）</div>
          <div>${q.explanation}</div>
          <div class="exp-trap">💡 陷阱提示：${q.trap}</div>
        `;
        card.appendChild(expDiv);
      }
    });

    localStorage.setItem('realtor_errors', JSON.stringify(state.errors));

    const score = correctCount; // 每題 1 分，滿分 100
    const timeUsedSeconds = 3600 - state.examSecondsLeft;
    const timeUsedStr = `${Math.floor(timeUsedSeconds / 60)} 分 ${timeUsedSeconds % 60} 秒`;

    // 儲存至歷史紀錄
    const now = new Date();
    const dateStr = `${now.getMonth() + 1}/${now.getDate()} ${now.getHours()}:${String(now.getMinutes()).padStart(2, '0')}`;
    state.examHistory.push({
      date: dateStr,
      score: score,
      correctCount: correctCount,
      usedTime: timeUsedStr
    });
    localStorage.setItem('realtor_exam_history', JSON.stringify(state.examHistory));

    // 顯示成績結算對話框
    alert(`【測驗結果報告】\n總分：${score} 分 (${score >= 60 ? '🎉 及格通過！' : '⚠️ 未達及格標準(60分)'})\n答對題數：${correctCount} 題\n做錯題目已自動加入【錯題筆記本】！`);
    
    // 滾動回最上方檢視試卷解析
    window.scrollTo({ top: 120, behavior: 'smooth' });
  };

  // ══════════════════════════════════════════════════════════════
  // 章節循序練習模組
  // ══════════════════════════════════════════════════════════════
  function initPractice() {
    renderPracticeQuestions();
  }

  window.filterPractice = function(category, btn) {
    state.practiceCat = category;
    document.querySelectorAll('.cat-filter-btn').forEach(b => b.classList.remove('active'));
    if (btn) btn.classList.add('active');
    renderPracticeQuestions();
  };

  function renderPracticeQuestions() {
    const list = document.getElementById('practiceQuestionsList');
    if (!list) return;

    let filtered = ALL_QUESTIONS;
    if (state.practiceCat !== 'ALL') {
      filtered = ALL_QUESTIONS.filter(q => q.category === state.practiceCat);
    }

    list.innerHTML = filtered.map((q, idx) => `
      <div class="question-item" id="prac-card-${q.id}">
        <div class="q-header">
          <span class="q-id">${q.id}</span>
          <span class="q-cat">${q.category}</span>
        </div>
        <div class="q-text">${q.question}</div>
        <div class="options-list">
          ${q.options.map((opt, optIdx) => {
            const letter = ['A', 'B', 'C', 'D'][optIdx];
            return `
              <button class="opt-btn" id="prac-opt-${q.id}-${letter}" onclick="checkPracticeAnswer('${q.id}', '${letter}')">
                ${opt}
              </button>
            `;
          }).join('')}
        </div>
        <div class="exp-box" id="prac-exp-${q.id}" style="display:none;">
          <div class="exp-law">⚖️ 法規依據：${q.law}（標準答案：${q.answer}）</div>
          <div>${q.explanation}</div>
          <div class="exp-trap">💡 考點防呆：${q.trap}</div>
        </div>
      </div>
    `).join('');
  }

  window.checkPracticeAnswer = function(qId, selectedLetter) {
    const q = ALL_QUESTIONS.find(item => item.id === qId);
    if (!q) return;

    const isCorrect = selectedLetter === q.answer;
    ['A', 'B', 'C', 'D'].forEach(l => {
      const btn = document.getElementById(`prac-opt-${qId}-${l}`);
      if (btn) {
        btn.classList.remove('correct', 'wrong');
        if (l === q.answer) btn.classList.add('correct');
        if (l === selectedLetter && !isCorrect) btn.classList.add('wrong');
      }
    });

    // 顯示解析
    const exp = document.getElementById(`prac-exp-${qId}`);
    if (exp) exp.style.display = 'block';

    // 錯題收集
    if (!isCorrect) {
      if (!state.errors.includes(qId)) {
        state.errors.push(qId);
        localStorage.setItem('realtor_errors', JSON.stringify(state.errors));
      }
    }
  };

  // ══════════════════════════════════════════════════════════════
  // 錯題筆記本模組
  // ══════════════════════════════════════════════════════════════
  function initErrorBook() {
    renderErrorBook();
  }

  function renderErrorBook() {
    const container = document.getElementById('errorBookList');
    if (!container) return;

    if (state.errors.length === 0) {
      container.innerHTML = '<div style="text-align:center;padding:40px;color:var(--ink-muted);background:var(--bg-card);border-radius:var(--radius-md);border:1px solid var(--border);">太棒了！目前沒有任何做錯的題目。</div>';
      return;
    }

    const errorQuestions = ALL_QUESTIONS.filter(q => state.errors.includes(q.id));
    container.innerHTML = `
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
        <span style="font-weight:bold;color:var(--ink-secondary);">目前錯題共 ${errorQuestions.length} 題</span>
        <button class="btn btn-outline" style="border-color:var(--red);color:var(--red);" onclick="clearAllErrors()">🗑️ 清空錯題本</button>
      </div>
    ` + errorQuestions.map(q => `
      <div class="question-item" id="err-card-${q.id}">
        <div class="q-header">
          <span class="q-id" style="color:var(--red);">${q.id}</span>
          <button class="btn btn-outline" style="padding:4px 10px;font-size:0.8rem;border-color:var(--border);color:var(--ink-secondary);" onclick="removeSingleError('${q.id}')">我已學會，移出租題本</button>
        </div>
        <div class="q-text">${q.question}</div>
        <div class="options-list">
          ${q.options.map((opt, optIdx) => {
            const letter = ['A', 'B', 'C', 'D'][optIdx];
            const isAns = letter === q.answer;
            return `<div class="opt-btn ${isAns ? 'correct' : ''}">${opt}</div>`;
          }).join('')}
        </div>
        <div class="exp-box">
          <div class="exp-law">⚖️ ${q.law}（正解：${q.answer}）</div>
          <div>${q.explanation}</div>
          <div class="exp-trap">💡 陷阱提點：${q.trap}</div>
        </div>
      </div>
    `).join('');
  }

  window.removeSingleError = function(qId) {
    state.errors = state.errors.filter(id => id !== qId);
    localStorage.setItem('realtor_errors', JSON.stringify(state.errors));
    renderErrorBook();
    updateDashboardStats();
  };

  window.clearAllErrors = function() {
    if (confirm('確定要清空所有已收集的錯題紀錄嗎？')) {
      state.errors = [];
      localStorage.setItem('realtor_errors', JSON.stringify(state.errors));
      renderErrorBook();
      updateDashboardStats();
    }
  };

  // ══════════════════════════════════════════════════════════════
  // 全題庫即時搜尋引擎
  // ══════════════════════════════════════════════════════════════
  function initSearch() {
    const input = document.getElementById('searchGlobalInput');
    if (input) {
      input.addEventListener('input', (e) => {
        performSearch(e.target.value.trim());
      });
    }
  }

  function performSearch(query) {
    const resultsArea = document.getElementById('searchResultsList');
    if (!resultsArea) return;

    if (!query) {
      resultsArea.innerHTML = '<div style="text-align:center;padding:30px;color:var(--ink-muted);">請在上方輸入關鍵字（例如：「30日」、「定金」、「房地合一」、「借名登記」）</div>';
      return;
    }

    const qLower = query.toLowerCase();
    const matches = ALL_QUESTIONS.filter(q => 
      q.id.toLowerCase().includes(qLower) ||
      q.question.toLowerCase().includes(qLower) ||
      q.options.some(opt => opt.toLowerCase().includes(qLower)) ||
      q.explanation.toLowerCase().includes(qLower) ||
      q.law.toLowerCase().includes(qLower)
    );

    if (matches.length === 0) {
      resultsArea.innerHTML = `<div style="text-align:center;padding:30px;color:var(--ink-muted);">查無符合「${query}」之相關題目。</div>`;
      return;
    }

    resultsArea.innerHTML = `
      <div style="margin-bottom:14px;color:var(--gold);font-weight:bold;">🔍 搜尋「${query}」共找到 ${matches.length} 道相關題目：</div>
    ` + matches.slice(0, 50).map(q => `
      <div class="question-item">
        <div class="q-header">
          <span class="q-id">${q.id}</span>
          <span class="q-cat">${q.category}</span>
        </div>
        <div class="q-text">${highlightMatch(q.question, query)}</div>
        <div class="options-list">
          ${q.options.map((opt, optIdx) => {
            const letter = ['A', 'B', 'C', 'D'][optIdx];
            const isAns = letter === q.answer;
            return `<div class="opt-btn ${isAns ? 'correct' : ''}">${highlightMatch(opt, query)}</div>`;
          }).join('')}
        </div>
        <div class="exp-box">
          <div class="exp-law">⚖️ ${q.law}（標準答案：${q.answer}）</div>
          <div>${highlightMatch(q.explanation, query)}</div>
          <div class="exp-trap">💡 ${q.trap}</div>
        </div>
      </div>
    `).join('');
  }

  function highlightMatch(text, query) {
    if (!query) return text;
    const regex = new RegExp(`(${query})`, 'gi');
    return text.replace(regex, '<mark style="background:#FEF08A;color:#1E293B;padding:1px 4px;border-radius:2px;">$1</mark>');
  }

  // ══════════════════════════════════════════════════════════════
  // 高頻數字速記卡
  // ══════════════════════════════════════════════════════════════
  const FLASHCARDS = [
    { num: "3 日", title: "委託銷售與租賃契約審閱期", desc: "不動產委託銷售契約書至少 3 日；房屋租賃契約至少 3 日。" },
    { num: "5 日", title: "成屋與預售屋買賣契約審閱期", desc: "預售屋買賣契約與成屋買賣定型化契約，審閱期間不得少於 5 日。" },
    { num: "7 日", title: "特種交易解除猶豫期", desc: "訪問或通訊交易，得於收受商品或接受服務後 7 日內無條件解約退費。" },
    { num: "10 日", title: "加盟資訊提供時限", desc: "加盟總部招募加盟前，至少於締約前 10 日提供加盟重要資訊書面說明。" },
    { num: "15 日", title: "增設營業處所保證金繳存", desc: "經紀業增設營業處所達一定規模者，應於 15 日內繳存營業保證金。" },
    { num: "30 日", title: "預售屋實價登錄申報時限", desc: "預售屋簽約日起 30 日內申報登錄；逾期或不實處 3 萬至 15 萬元罰鍰。" },
    { num: "30 日", title: "房地合一稅交易申報", desc: "房地過戶移轉登記日之次日起算 30 日內向戶籍地稽徵機關申報。" },
    { num: "30 日", title: "經紀人出缺補聘時限", desc: "經紀人出缺或人數不符法定員額（每20營業員配1經紀人）時，應於 30 日內補聘。" },
    { num: "1 個月", title: "營業保證金代償補足時限", desc: "營業保證基金代償後，經紀業應於收到通知之日起 1 個月內全額補足。" },
    { num: "40 日", title: "自用地價稅申請截止期限", desc: "每年地價稅開徵 40 日前（即 9 月 22 日前）提出申請，逾期次年適用。" },
    { num: "6 個月", title: "瑕疵通知後請求權除斥期間", desc: "買賣物有瑕疵，買受人自通知後 6 個月不行使或交屋後滿 5 年即消滅。" },
    { num: "4 年", title: "經紀人與營業員證書有效期", desc: "經紀人證書與營業員證明之法定有效期限均為 4 年一換。" },
    { num: "6 年", title: "房地合一自住免稅連續設籍", desc: "個人或配偶、未成年子女設籍居住滿 6 年，享 400 萬課稅所得免稅額。" },
    { num: "6%", title: "買賣服務報酬上限", desc: "經紀業向買賣雙方收取服務報酬總額，合計最高不得超過成交價 6%。" },
    { num: "1.5 個月", title: "租賃服務報酬上限", desc: "經紀業向租賃雙方收取報酬總額，合計最高不得超過 1.5 個月租金。" },
    { num: "2 個月", title: "房屋租賃押金上限", desc: "房屋租賃之擔保金（押金），最高不得超過 2 個月租金總額。" },
    { num: "5,000 萬", title: "打炒房炒作罰鍰天花板", desc: "平均地權條例散布不實炒作者，處 100 萬至 5,000 萬元重罰，並得按次處罰！" }
  ];

  function initFlashcards() {
    const wrap = document.getElementById('flashcardsContainer');
    if (!wrap) return;
    wrap.innerHTML = FLASHCARDS.map(fc => `
      <div class="card" style="border-top:4px solid var(--gold);display:flex;flex-direction:column;justify-content:space-between;">
        <div>
          <div style="font-family:var(--font-mono);font-size:1.8rem;font-weight:900;color:var(--gold);margin-bottom:6px;">${fc.num}</div>
          <h4 style="font-size:1.05rem;color:var(--ink-primary);margin-bottom:8px;">${fc.title}</h4>
          <p style="font-size:0.9rem;color:var(--ink-secondary);line-height:1.6;">${fc.desc}</p>
        </div>
      </div>
    `).join('');
  }

})();
