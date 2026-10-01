/**
 * iPAS 資訊安全工程師 - 核心學習平台前端邏輯 (app.js)
 * 涵蓋：Web Speech API 英語語音發音、全真模擬考引擎、情境式章節練習、錯題本、題庫搜尋、名詞辭典與講義研讀
 */

(function () {
  "use strict";

  // 全域狀態管理
  const state = {
    currentTab: "dashboard",
    theme: localStorage.getItem("ipas_theme") || "dark",
    speechRate: 1.0,
    speechLang: "en-US",
    
    // 題庫資料快取
    basicQuestions: window.IPAS_QUESTIONS_BASIC || [],
    midQuestions: window.IPAS_QUESTIONS_MID || [],
    glossary: window.IPAS_GLOSSARY || [],
    notes: window.IPAS_LECTURE_NOTES || {},

    // 模擬考狀態
    exam: {
      active: false,
      level: "初級", // 或 "中級"
      questions: [],
      currentIndex: 0,
      userAnswers: {}, // index -> 'A'/'B'/'C'/'D'
      flagged: {}, // index -> true/false
      timerSeconds: 90 * 60, // 90 分鐘
      timerInterval: null,
      submitted: false,
      score: 0
    },

    // 章節練習狀態
    practice: {
      level: "初級",
      subject: "all",
      domain: "all",
      scenarioOnly: false,
      searchKeyword: "",
      filteredQuestions: [],
      currentIndex: 0,
      selectedAnswer: null,
      showExplanation: false
    },

    // 錯題筆記本 (持久化存於 localStorage)
    errorBook: JSON.parse(localStorage.getItem("ipas_error_book") || "{}"), // id -> question object

    // 收藏題目
    favorites: JSON.parse(localStorage.getItem("ipas_favorites") || "{}"),

    // 講義研讀器狀態
    currentNoteLevel: "basic",
    currentNoteModuleId: "B1-M01"
  };

  // ==========================================================================
  // 1. Web Speech API 語音發音模組 (English Pronunciation Engine)
  // ==========================================================================
  const speech = {
    synth: window.speechSynthesis || null,
    voices: [],

    init() {
      if (!this.synth) {
        console.warn("此瀏覽器不支援 Web Speech API 語音合成功能");
        return;
      }
      this.loadVoices();
      if (this.synth.onvoiceschanged !== undefined) {
        this.synth.onvoiceschanged = () => this.loadVoices();
      }
    },

    loadVoices() {
      if (!this.synth) return;
      this.voices = this.synth.getVoices().filter(v => v.lang.startsWith("en"));
    },

    speak(text, btnElement = null) {
      if (!this.synth) {
        alert("抱歉，您的瀏覽器不支援 Web Speech 語音發音功能。");
        return;
      }

      // 若正在播放則先取消
      this.synth.cancel();

      // 清理文本：只保留英文專有名詞與字母
      const cleanText = text.replace(/[\u4e00-\u9fa5（）()、，。]/g, "").trim();
      if (!cleanText) return;

      const utterance = new SpeechSynthesisUtterance(cleanText);
      utterance.rate = state.speechRate || 1.0;
      utterance.lang = state.speechLang || "en-US";

      // 挑選合適的英語音色
      if (this.voices.length > 0) {
        const preferredVoice = this.voices.find(v => v.name.includes("Google") || v.name.includes("Natural") || v.name.includes("Samantha") || v.lang === "en-US");
        if (preferredVoice) utterance.voice = preferredVoice;
      }

      if (btnElement) {
        btnElement.classList.add("speaking");
        utterance.onend = () => btnElement.classList.remove("speaking");
        utterance.onerror = () => btnElement.classList.remove("speaking");
      }

      this.synth.speak(utterance);
    }
  };

  // 全域發音輔助函式 (提供 HTML onclick 呼叫)
  window.speakEnglish = function (text, btn = null) {
    speech.speak(text, btn);
  };

  // ==========================================================================
  // 2. 佈景主題與導航切換
  // ==========================================================================
  function initTheme() {
    document.documentElement.setAttribute("data-theme", state.theme);
    const themeBtn = document.getElementById("themeToggleBtn");
    if (themeBtn) {
      themeBtn.innerHTML = state.theme === "dark" ? "☀️" : "🌙";
    }
  }

  function toggleTheme() {
    state.theme = state.theme === "dark" ? "light" : "dark";
    localStorage.setItem("ipas_theme", state.theme);
    initTheme();
  }

  function switchTab(tabId) {
    state.currentTab = tabId;

    // 更新導航按鈕狀態
    document.querySelectorAll(".nav-btn").forEach(btn => {
      if (btn.getAttribute("data-tab") === tabId) {
        btn.classList.add("active");
      } else {
        btn.classList.remove("active");
      }
    });

    // 切換視圖區塊
    document.querySelectorAll(".view-section").forEach(sec => {
      if (sec.id === `tab-${tabId}`) {
        sec.classList.add("active");
      } else {
        sec.classList.remove("active");
      }
    });

    window.scrollTo({ top: 0, behavior: "smooth" });

    // 針對各頁面進行專屬初始化
    if (tabId === "dashboard") updateDashboardStats();
    if (tabId === "practice") renderPracticeView();
    if (tabId === "error-book") renderErrorBookView();
    if (tabId === "glossary") renderGlossaryView();
    if (tabId === "notes") renderNotesView();
    if (tabId === "search") executeGlobalSearch();
  }

  window.switchTab = switchTab;

  // ==========================================================================
  // 3. 儀表板總覽 (Dashboard)
  // ==========================================================================
  function updateDashboardStats() {
    const totalQuestions = state.basicQuestions.length + state.midQuestions.length;
    const basicCount = state.basicQuestions.length;
    const midCount = state.midQuestions.length;
    const scenarioCount = [...state.basicQuestions, ...state.midQuestions].filter(q => q.scenario).length;
    const errorCount = Object.keys(state.errorBook).length;
    const glossaryCount = state.glossary.length;

    // 最高分統計
    const bestScore = localStorage.getItem("ipas_best_score") || "尚無紀錄";

    const elTotal = document.getElementById("statTotalQuestions");
    const elBasic = document.getElementById("statBasicQuestions");
    const elMid = document.getElementById("statMidQuestions");
    const elScenario = document.getElementById("statScenarioCount");
    const elBest = document.getElementById("statBestScore");
    const elErrors = document.getElementById("statErrorCount");
    const elGlossary = document.getElementById("statGlossaryCount");

    if (elTotal) elTotal.textContent = totalQuestions.toLocaleString();
    if (elBasic) elBasic.textContent = basicCount.toLocaleString();
    if (elMid) elMid.textContent = midCount.toLocaleString();
    if (elScenario) elScenario.textContent = `${scenarioCount} 題 (90%)`;
    if (elBest) elBest.textContent = bestScore !== "尚無紀錄" ? `${bestScore} 分` : bestScore;
    if (elErrors) elErrors.textContent = errorCount;
    if (elGlossary) elGlossary.textContent = glossaryCount;
  }

  // ==========================================================================
  // 4. 全真模擬考引擎 (Mock Exam Engine)
  // ==========================================================================
  function startMockExam(level = "初級", questionCount = 50) {
    const bank = level === "初級" ? state.basicQuestions : state.midQuestions;
    if (bank.length === 0) {
      alert("題庫載入中，請稍候重試");
      return;
    }

    // 隨機抽取 50 題
    const shuffled = [...bank].sort(() => 0.5 - Math.random());
    const selected = shuffled.slice(0, questionCount);

    state.exam.active = true;
    state.exam.level = level;
    state.exam.questions = selected;
    state.exam.currentIndex = 0;
    state.exam.userAnswers = {};
    state.exam.flagged = {};
    state.exam.submitted = false;
    state.exam.timerSeconds = 90 * 60; // 90 分鐘

    // 切換至模擬考頁面
    switchTab("mock-exam");

    document.getElementById("examSetupBox").style.display = "none";
    document.getElementById("examRunnerBox").style.display = "block";
    document.getElementById("examResultCard").style.display = "none";

    startExamTimer();
    renderCurrentExamQuestion();
    renderExamGrid();
  }

  window.startMockExam = startMockExam;

  function startExamTimer() {
    clearInterval(state.exam.timerInterval);
    const timerEl = document.getElementById("examTimerDisplay");

    state.exam.timerInterval = setInterval(() => {
      if (state.exam.timerSeconds <= 0) {
        clearInterval(state.exam.timerInterval);
        alert("作答時間到！系統即將為您自動交卷計算成績。");
        submitExam();
        return;
      }
      state.exam.timerSeconds--;

      const min = Math.floor(state.exam.timerSeconds / 60);
      const sec = state.exam.timerSeconds % 60;
      if (timerEl) {
        timerEl.textContent = `${String(min).padStart(2, "0")}:${String(sec).padStart(2, "0")}`;
        if (state.exam.timerSeconds < 300) {
          timerEl.parentElement.classList.add("warning");
        } else {
          timerEl.parentElement.classList.remove("warning");
        }
      }
    }, 1000);
  }

  function renderCurrentExamQuestion() {
    const q = state.exam.questions[state.exam.currentIndex];
    if (!q) return;

    const idx = state.exam.currentIndex;
    const total = state.exam.questions.length;
    const userAnswer = state.exam.userAnswers[idx] || null;
    const isFlagged = state.exam.flagged[idx] || false;

    const card = document.getElementById("examQuestionContainer");
    if (!card) return;

    // 英文詞彙發音標籤產生
    let termsHtml = "";
    if (q.terms && q.terms.length > 0) {
      termsHtml = `
        <div class="question-terms-box">
          <div class="terms-header">🔊 關鍵資安英文術語與發音（點擊朗讀）</div>
          <div class="terms-pills">
            ${q.terms.map(t => `
              <div class="term-pill" onclick="speakEnglish('${t.en}', this)">
                <span class="speak-icon">🔊</span>
                <b>${t.en}</b>
                <span>${t.zh}</span>
                <span class="ipa-text">${t.ipa}</span>
              </div>
            `).join("")}
          </div>
        </div>
      `;
    }

    // 選項渲染
    const optionsHtml = q.options.map((opt, optIndex) => {
      const letter = opt.substring(0, 1);
      const isSelected = userAnswer === letter;
      let optionClass = "option-item";
      if (isSelected) optionClass += " selected";

      // 若已交卷則標記對錯
      if (state.exam.submitted) {
        if (letter === q.answer) optionClass += " correct";
        else if (isSelected && letter !== q.answer) optionClass += " wrong";
      }

      return `
        <div class="${optionClass}" onclick="selectExamOption('${letter}')">
          <div class="option-letter">${letter}</div>
          <div class="option-text">${opt.substring(3)}</div>
        </div>
      `;
    }).join("");

    // 解析面板 (僅交卷後顯示)
    let explanationHtml = "";
    if (state.exam.submitted) {
      explanationHtml = `
        <div class="explanation-panel">
          <div class="explanation-title">
            <span>${userAnswer === q.answer ? "✅ 答對！" : "❌ 答錯！"} 正確答案為：【${q.answer}】</span>
          </div>
          <div class="explanation-text">${q.explanation}</div>
          <div class="trap-box">💡 <strong>考點防呆與盲點：</strong>${q.trap}</div>
          <div class="law-tag">📜 標準與規範依據：${q.law}</div>
        </div>
      `;
    }

    card.innerHTML = `
      <div class="question-card">
        <div class="question-meta">
          <span class="badge badge-cyan">${q.level}</span>
          <span class="badge badge-purple">${q.subject}</span>
          <span class="badge badge-gold">${q.domain}</span>
          ${q.scenario ? '<span class="badge badge-green">🎯 實務情境題</span>' : '<span class="badge badge-cyan">核心觀念題</span>'}
          <span style="margin-left:auto;font-family:var(--font-mono);font-size:0.85rem;color:var(--text-muted);">
            第 ${idx + 1} / ${total} 題 (${q.id})
          </span>
        </div>

        <div class="question-title">${q.question}</div>

        <div class="options-list">
          ${optionsHtml}
        </div>

        ${termsHtml}

        ${explanationHtml}

        <div style="display:flex;justify-content:space-between;align-items:center;margin-top:24px;flex-wrap:wrap;gap:10px;">
          <div style="display:flex;gap:10px;">
            <button class="btn btn-outline" onclick="prevExamQuestion()" ${idx === 0 ? "disabled" : ""}>⬅ 上一題</button>
            <button class="btn btn-outline" onclick="nextExamQuestion()" ${idx === total - 1 ? "disabled" : ""}>下一題 ➡</button>
          </div>
          <div style="display:flex;gap:10px;">
            <button class="btn btn-outline" onclick="toggleExamFlag(${idx})" style="color:${isFlagged ? "var(--cyber-gold)" : "inherit"}">
              ${isFlagged ? "🚩 取消標記" : "🏳 標記覆查"}
            </button>
            ${!state.exam.submitted ? '<button class="btn btn-cyan" onclick="confirmSubmitExam()">📝 提早交卷</button>' : ''}
          </div>
        </div>
      </div>
    `;

    renderExamGrid();
  }

  window.selectExamOption = function (letter) {
    if (state.exam.submitted) return;
    const idx = state.exam.currentIndex;
    state.exam.userAnswers[idx] = letter;
    renderCurrentExamQuestion();
  };

  window.prevExamQuestion = function () {
    if (state.exam.currentIndex > 0) {
      state.exam.currentIndex--;
      renderCurrentExamQuestion();
    }
  };

  window.nextExamQuestion = function () {
    if (state.exam.currentIndex < state.exam.questions.length - 1) {
      state.exam.currentIndex++;
      renderCurrentExamQuestion();
    }
  };

  window.toggleExamFlag = function (idx) {
    state.exam.flagged[idx] = !state.exam.flagged[idx];
    renderCurrentExamQuestion();
  };

  window.jumpToExamQuestion = function (idx) {
    state.exam.currentIndex = idx;
    renderCurrentExamQuestion();
  };

  function renderExamGrid() {
    const gridEl = document.getElementById("examAnswerGrid");
    if (!gridEl) return;

    gridEl.innerHTML = state.exam.questions.map((q, idx) => {
      const isAnswered = state.exam.userAnswers[idx] !== undefined;
      const isCurrent = state.exam.currentIndex === idx;
      const isFlagged = state.exam.flagged[idx] === true;

      let cls = "grid-num-btn";
      if (isAnswered) cls += " answered";
      if (isFlagged) cls += " flagged";
      if (isCurrent) cls += " current";

      if (state.exam.submitted) {
        const isCorrect = state.exam.userAnswers[idx] === q.answer;
        cls += isCorrect ? " correct" : " wrong";
      }

      return `<button class="${cls}" onclick="jumpToExamQuestion(${idx})">${idx + 1}</button>`;
    }).join("");
  }

  window.confirmSubmitExam = function () {
    const answeredCount = Object.keys(state.exam.userAnswers).length;
    const total = state.exam.questions.length;
    if (answeredCount < total) {
      if (!confirm(`您尚有 ${total - answeredCount} 題未作答，確定要提早交卷嗎？`)) {
        return;
      }
    } else {
      if (!confirm("確定要交卷評分嗎？")) return;
    }
    submitExam();
  };

  function submitExam() {
    clearInterval(state.exam.timerInterval);
    state.exam.submitted = true;

    // 計算分數
    let correctCount = 0;
    const domainScores = {};

    state.exam.questions.forEach((q, idx) => {
      const userAns = state.exam.userAnswers[idx];
      const isCorrect = userAns === q.answer;

      if (!domainScores[q.domain]) {
        domainScores[q.domain] = { total: 0, correct: 0 };
      }
      domainScores[q.domain].total++;

      if (isCorrect) {
        correctCount++;
        domainScores[q.domain].correct++;
      } else {
        // 自動加入錯題筆記本
        state.errorBook[q.id] = q;
      }
    });

    // 存入 localStorage
    localStorage.setItem("ipas_error_book", JSON.stringify(state.errorBook));

    const total = state.exam.questions.length;
    const finalScore = Math.round((correctCount / total) * 100);
    state.exam.score = finalScore;

    // 紀錄最高分
    const prevBest = parseInt(localStorage.getItem("ipas_best_score") || "0", 10);
    if (finalScore > prevBest) {
      localStorage.setItem("ipas_best_score", finalScore);
    }

    // 顯示結果卡片
    const resultCard = document.getElementById("examResultCard");
    if (resultCard) {
      const passed = finalScore >= 60;
      resultCard.style.display = "block";
      resultCard.innerHTML = `
        <div style="background:var(--bg-card);border:2px solid ${passed ? "var(--cyber-green)" : "var(--cyber-red)"};border-radius:var(--radius-xl);padding:32px;box-shadow:var(--shadow-lg);margin-bottom:24px;text-align:center;">
          <div style="font-size:3.5rem;margin-bottom:12px;">${passed ? "🏆" : "💪"}</div>
          <h2 style="font-size:1.8rem;margin-bottom:8px;">${passed ? "恭喜及格！達到 iPAS 證照能力門檻！" : "仍需努力！距離 60 分及格門檻僅一步之遙"}</h2>
          <div style="font-size:3.2rem;font-weight:900;font-family:var(--font-mono);color:${passed ? "var(--cyber-green)" : "var(--cyber-red)"};margin:12px 0;">
            ${finalScore} <span style="font-size:1.2rem;color:var(--text-muted);">/ 100 分</span>
          </div>
          <p style="color:var(--text-muted);font-size:1rem;margin-bottom:20px;">
            共 ${total} 題，答對 ${correctCount} 題，答錯 ${total - correctCount} 題（答錯題目已自動為您收錄至「錯題筆記本」）。
          </p>

          <div style="max-width:600px;margin:20px auto;text-align:left;background:var(--bg-secondary);border-radius:var(--radius-lg);padding:20px;">
            <h4 style="font-size:1rem;font-weight:800;color:var(--cyber-cyan);margin-bottom:12px;">📊 各領域能力落點分析：</h4>
            ${Object.entries(domainScores).map(([dom, sc]) => {
              const pct = Math.round((sc.correct / sc.total) * 100);
              return `
                <div style="margin-bottom:10px;">
                  <div style="display:flex;justify-content:space-between;font-size:0.85rem;margin-bottom:4px;">
                    <span>${dom}</span>
                    <span style="font-weight:700;color:${pct >= 60 ? "var(--cyber-green)" : "var(--cyber-red)"};">${sc.correct}/${sc.total} (${pct}%)</span>
                  </div>
                  <div style="height:6px;background:rgba(255,255,255,0.1);border-radius:3px;overflow:hidden;">
                    <div style="width:${pct}%;height:100%;background:${pct >= 60 ? "var(--cyber-green)" : "var(--cyber-red)"};"></div>
                  </div>
                </div>
              `;
            }).join("")}
          </div>

          <div style="display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-top:24px;">
            <button class="btn btn-cyan" onclick="startMockExam('${state.exam.level}', 50)">🔄 再次挑戰一回</button>
            <button class="btn btn-gold" onclick="switchTab('error-book')">❌ 查看錯題筆記本</button>
            <button class="btn btn-outline" onclick="jumpToExamQuestion(0)">🔍 逐題檢視解析</button>
          </div>
        </div>
      `;
      resultCard.scrollIntoView({ behavior: "smooth" });
    }

    renderCurrentExamQuestion();
    renderExamGrid();
  }

  // ==========================================================================
  // 5. 循序章節練習 (Practice View)
  // ==========================================================================
  function renderPracticeView() {
    const bank = state.practice.level === "初級" ? state.basicQuestions : state.midQuestions;

    let filtered = bank;
    if (state.practice.domain !== "all") {
      filtered = filtered.filter(q => q.domain === state.practice.domain);
    }
    if (state.practice.scenarioOnly) {
      filtered = filtered.filter(q => q.scenario);
    }
    if (state.practice.searchKeyword.trim() !== "") {
      const kw = state.practice.searchKeyword.trim().toLowerCase();
      filtered = filtered.filter(q =>
        q.question.toLowerCase().includes(kw) ||
        q.explanation.toLowerCase().includes(kw) ||
        (q.terms && q.terms.some(t => t.en.toLowerCase().includes(kw) || t.zh.includes(kw)))
      );
    }

    state.practice.filteredQuestions = filtered;
    if (state.practice.currentIndex >= filtered.length) {
      state.practice.currentIndex = 0;
    }

    renderPracticeQuestion();
  }

  function renderPracticeQuestion() {
    const container = document.getElementById("practiceQuestionContainer");
    if (!container) return;

    const list = state.practice.filteredQuestions;
    if (list.length === 0) {
      container.innerHTML = `
        <div style="background:var(--bg-card);border-radius:var(--radius-xl);padding:60px 20px;text-align:center;">
          <div style="font-size:3rem;margin-bottom:12px;">🔍</div>
          <h3>查無符合篩選條件之題目</h3>
          <p style="color:var(--text-muted);margin-top:8px;">請嘗試更換科目、領域或清除搜尋關鍵字。</p>
        </div>
      `;
      return;
    }

    const q = list[state.practice.currentIndex];
    const idx = state.practice.currentIndex;
    const total = list.length;
    const isFav = !!state.favorites[q.id];

    // 關鍵詞發音
    let termsHtml = "";
    if (q.terms && q.terms.length > 0) {
      termsHtml = `
        <div class="question-terms-box">
          <div class="terms-header">🔊 關鍵資安英文術語與發音（點擊朗讀）</div>
          <div class="terms-pills">
            ${q.terms.map(t => `
              <div class="term-pill" onclick="speakEnglish('${t.en}', this)">
                <span class="speak-icon">🔊</span>
                <b>${t.en}</b>
                <span>${t.zh}</span>
                <span class="ipa-text">${t.ipa}</span>
              </div>
            `).join("")}
          </div>
        </div>
      `;
    }

    // 選項渲染 (練習模式：若已選擇選項立即揭示答案)
    const optionsHtml = q.options.map(opt => {
      const letter = opt.substring(0, 1);
      const isSelected = state.practice.selectedAnswer === letter;
      let optionClass = "option-item";

      if (state.practice.showExplanation) {
        if (letter === q.answer) optionClass += " correct";
        else if (isSelected && letter !== q.answer) optionClass += " wrong";
      } else if (isSelected) {
        optionClass += " selected";
      }

      return `
        <div class="${optionClass}" onclick="answerPracticeOption('${letter}')">
          <div class="option-letter">${letter}</div>
          <div class="option-text">${opt.substring(3)}</div>
        </div>
      `;
    }).join("");

    let explanationHtml = "";
    if (state.practice.showExplanation) {
      const isRight = state.practice.selectedAnswer === q.answer;
      explanationHtml = `
        <div class="explanation-panel">
          <div class="explanation-title">
            <span>${isRight ? "✅ 正確！" : "❌ 回答錯誤！"} 標準解答為：【${q.answer}】</span>
          </div>
          <div class="explanation-text">${q.explanation}</div>
          <div class="trap-box">💡 <strong>實務防呆陷阱提示：</strong>${q.trap}</div>
          <div class="law-tag">📜 標準與規範依據：${q.law}</div>
        </div>
      `;
    }

    container.innerHTML = `
      <div class="question-card">
        <div class="question-meta">
          <span class="badge badge-cyan">${q.level}</span>
          <span class="badge badge-purple">${q.subject}</span>
          <span class="badge badge-gold">${q.domain}</span>
          ${q.scenario ? '<span class="badge badge-green">🎯 90% 實務情境題</span>' : '<span class="badge badge-cyan">核心觀念題</span>'}
          <span style="margin-left:auto;font-family:var(--font-mono);font-size:0.85rem;color:var(--text-muted);">
            第 ${idx + 1} / ${total} 題 (${q.id})
          </span>
          <button class="btn btn-outline" style="padding:4px 10px;font-size:0.75rem;" onclick="toggleFavorite('${q.id}')">
            ${isFav ? "⭐ 已收藏" : "☆ 收藏"}
          </button>
        </div>

        <div class="question-title">${q.question}</div>

        <div class="options-list">
          ${optionsHtml}
        </div>

        ${termsHtml}

        ${explanationHtml}

        <div style="display:flex;justify-content:space-between;align-items:center;margin-top:24px;">
          <button class="btn btn-outline" onclick="prevPracticeQuestion()" ${idx === 0 ? "disabled" : ""}>⬅ 上一題</button>
          <div style="display:flex;gap:10px;">
            ${!state.practice.showExplanation ? `<button class="btn btn-gold" onclick="revealPracticeAnswer()">💡 直接看解答</button>` : ''}
            <button class="btn btn-cyan" onclick="nextPracticeQuestion()" ${idx === total - 1 ? "disabled" : ""}>下一題 ➡</button>
          </div>
        </div>
      </div>
    `;
  }

  window.answerPracticeOption = function (letter) {
    if (state.practice.showExplanation) return;
    state.practice.selectedAnswer = letter;
    state.practice.showExplanation = true;

    const q = state.practice.filteredQuestions[state.practice.currentIndex];
    if (letter !== q.answer) {
      // 加入錯題本
      state.errorBook[q.id] = q;
      localStorage.setItem("ipas_error_book", JSON.stringify(state.errorBook));
    }

    renderPracticeQuestion();
  };

  window.revealPracticeAnswer = function () {
    state.practice.showExplanation = true;
    renderPracticeQuestion();
  };

  window.prevPracticeQuestion = function () {
    if (state.practice.currentIndex > 0) {
      state.practice.currentIndex--;
      state.practice.selectedAnswer = null;
      state.practice.showExplanation = false;
      renderPracticeQuestion();
    }
  };

  window.nextPracticeQuestion = function () {
    if (state.practice.currentIndex < state.practice.filteredQuestions.length - 1) {
      state.practice.currentIndex++;
      state.practice.selectedAnswer = null;
      state.practice.showExplanation = false;
      renderPracticeQuestion();
    }
  };

  window.toggleFavorite = function (qid) {
    if (state.favorites[qid]) {
      delete state.favorites[qid];
    } else {
      const allQ = [...state.basicQuestions, ...state.midQuestions];
      const target = allQ.find(q => q.id === qid);
      if (target) state.favorites[qid] = target;
    }
    localStorage.setItem("ipas_favorites", JSON.stringify(state.favorites));
    renderPracticeQuestion();
  };

  // ==========================================================================
  // 6. 錯題筆記本 (Error Notebook)
  // ==========================================================================
  function renderErrorBookView() {
    const container = document.getElementById("errorBookContainer");
    if (!container) return;

    const errorList = Object.values(state.errorBook);
    const countEl = document.getElementById("errorBookCount");
    if (countEl) countEl.textContent = `${errorList.length} 題`;

    if (errorList.length === 0) {
      container.innerHTML = `
        <div style="background:var(--bg-card);border-radius:var(--radius-xl);padding:60px 20px;text-align:center;">
          <div style="font-size:3.5rem;margin-bottom:12px;">🎉</div>
          <h3>太棒了！錯題筆記本中暫無錯題！</h3>
          <p style="color:var(--text-muted);margin-top:8px;">在模擬考或章節練習中若有答錯的題目，系統將自動為您集中收錄至此處。</p>
        </div>
      `;
      return;
    }

    container.innerHTML = errorList.map((q, idx) => {
      let termsHtml = "";
      if (q.terms && q.terms.length > 0) {
        termsHtml = `
          <div class="terms-pills" style="margin-top:10px;">
            ${q.terms.map(t => `
              <div class="term-pill" onclick="speakEnglish('${t.en}', this)">
                <span class="speak-icon">🔊</span>
                <b>${t.en}</b> (${t.zh})
              </div>
            `).join("")}
          </div>
        `;
      }

      return `
        <div class="question-card" style="margin-bottom:20px;">
          <div class="question-meta">
            <span class="badge badge-red">錯題 #${idx + 1}</span>
            <span class="badge badge-cyan">${q.level}</span>
            <span class="badge badge-gold">${q.domain}</span>
            <button class="btn btn-outline" style="margin-left:auto;padding:4px 10px;font-size:0.75rem;" onclick="removeErrorQuestion('${q.id}')">
              ✅ 標記已掌握並移除
            </button>
          </div>
          <div class="question-title">${q.question}</div>
          <div class="options-list">
            ${q.options.map(opt => `
              <div class="option-item ${opt.startsWith(q.answer) ? "correct" : ""}" style="cursor:default;">
                <div class="option-letter">${opt.substring(0, 1)}</div>
                <div class="option-text">${opt.substring(3)}</div>
              </div>
            `).join("")}
          </div>
          <div class="explanation-panel" style="margin-top:12px;">
            <div class="explanation-title">標準解答：【${q.answer}】</div>
            <div class="explanation-text">${q.explanation}</div>
            <div class="trap-box">💡 <strong>防呆重點：</strong>${q.trap}</div>
          </div>
          ${termsHtml}
        </div>
      `;
    }).join("");
  }

  window.removeErrorQuestion = function (qid) {
    delete state.errorBook[qid];
    localStorage.setItem("ipas_error_book", JSON.stringify(state.errorBook));
    renderErrorBookView();
    updateDashboardStats();
  };

  window.clearAllErrors = function () {
    if (confirm("確定要清空所有的錯題紀錄嗎？")) {
      state.errorBook = {};
      localStorage.setItem("ipas_error_book", JSON.stringify(state.errorBook));
      renderErrorBookView();
      updateDashboardStats();
    }
  };

  // ==========================================================================
  // 7. 資安核心術語與發音辭典 (Glossary & Pronunciation)
  // ==========================================================================
  function renderGlossaryView() {
    const grid = document.getElementById("glossaryGrid");
    if (!grid) return;

    const kwInput = document.getElementById("glossarySearchInput");
    const categorySelect = document.getElementById("glossaryCategorySelect");

    const kw = kwInput ? kwInput.value.trim().toLowerCase() : "";
    const cat = categorySelect ? categorySelect.value : "all";

    let list = state.glossary;
    if (cat !== "all") {
      list = list.filter(item => item.category === cat);
    }
    if (kw) {
      list = list.filter(item =>
        item.term.toLowerCase().includes(kw) ||
        (item.abbr && item.abbr.toLowerCase().includes(kw)) ||
        item.zh.includes(kw) ||
        item.definition.includes(kw)
      );
    }

    grid.innerHTML = list.map(item => `
      <div class="glossary-card">
        <div class="term-top">
          <div>
            <div class="term-name">${item.term}</div>
            ${item.abbr ? `<span class="badge badge-cyan" style="margin-top:4px;">${item.abbr}</span>` : ""}
          </div>
          <button class="term-audio-btn" title="聆聽英語真人發音" onclick="speakEnglish('${item.term}', this)">
            🔊
          </button>
        </div>
        <div class="term-ipa">${item.ipa}</div>
        <div class="term-zh">${item.zh}</div>
        <div class="term-def">${item.definition}</div>
        ${item.scenarioExamTip ? `<div class="term-tip">🎯 <strong>考點情境：</strong>${item.scenarioExamTip}</div>` : ""}
      </div>
    `).join("");
  }

  window.filterGlossary = renderGlossaryView;

  // ==========================================================================
  // 8. 全域題庫智慧搜尋 (Question Bank Search)
  // ==========================================================================
  function executeGlobalSearch() {
    const input = document.getElementById("globalSearchInput");
    const container = document.getElementById("globalSearchResults");
    if (!container) return;

    const kw = input ? input.value.trim().toLowerCase() : "";
    if (!kw) {
      container.innerHTML = `
        <div style="background:var(--bg-card);border-radius:var(--radius-xl);padding:50px 20px;text-align:center;">
          <div style="font-size:2.5rem;margin-bottom:10px;">🔍</div>
          <h4>請在上方搜尋框輸入關鍵字</h4>
          <p style="color:var(--text-muted);font-size:0.9rem;margin-top:6px;">支援搜尋題目、題號、英文專有名詞、法規標準或解題觀念。</p>
        </div>
      `;
      return;
    }

    const allQuestions = [...state.basicQuestions, ...state.midQuestions];
    const results = allQuestions.filter(q =>
      q.id.toLowerCase().includes(kw) ||
      q.question.toLowerCase().includes(kw) ||
      q.explanation.toLowerCase().includes(kw) ||
      q.domain.toLowerCase().includes(kw) ||
      (q.terms && q.terms.some(t => t.en.toLowerCase().includes(kw) || t.zh.includes(kw)))
    );

    const countEl = document.getElementById("searchResultCount");
    if (countEl) countEl.textContent = `${results.length} 筆`;

    if (results.length === 0) {
      container.innerHTML = `
        <div style="background:var(--bg-card);border-radius:var(--radius-xl);padding:50px 20px;text-align:center;">
          <h4>找不到包含「${kw}」的題目</h4>
          <p style="color:var(--text-muted);margin-top:6px;">請嘗試更換關鍵字或縮短詞彙。</p>
        </div>
      `;
      return;
    }

    container.innerHTML = results.map(q => `
      <div class="question-card" style="margin-bottom:18px;">
        <div class="question-meta">
          <span class="badge badge-cyan">${q.level}</span>
          <span class="badge badge-purple">${q.subject}</span>
          <span class="badge badge-gold">${q.domain}</span>
          <span style="margin-left:auto;font-family:var(--font-mono);font-size:0.85rem;color:var(--text-muted);">${q.id}</span>
        </div>
        <div class="question-title">${q.question}</div>
        <div class="options-list">
          ${q.options.map(opt => `
            <div class="option-item ${opt.startsWith(q.answer) ? "correct" : ""}" style="cursor:default;">
              <div class="option-letter">${opt.substring(0, 1)}</div>
              <div class="option-text">${opt.substring(3)}</div>
            </div>
          `).join("")}
        </div>
        <div class="explanation-panel">
          <div class="explanation-title">標準解答：【${q.answer}】</div>
          <div class="explanation-text">${q.explanation}</div>
          <div class="trap-box">💡 <strong>防呆重點：</strong>${q.trap}</div>
          <div class="law-tag">📜 標準依據：${q.law}</div>
        </div>
      </div>
    `).join("");
  }

  window.executeGlobalSearch = executeGlobalSearch;

  // ==========================================================================
  // 9. 考科講義研讀器 (Lecture Notes Reader)
  // ==========================================================================
  function renderNotesView() {
    const level = state.currentNoteLevel;
    const notesData = state.notes[level];
    if (!notesData) return;

    // 側邊欄導航生成
    const navContainer = document.getElementById("notesSidebarNav");
    if (navContainer) {
      navContainer.innerHTML = notesData.subjects.map(sub => `
        <div class="notes-nav-group">
          <div class="notes-group-title">${sub.name}</div>
          <ul class="notes-nav-list">
            ${sub.modules.map(mod => `
              <li class="notes-nav-item ${mod.id === state.currentNoteModuleId ? "active" : ""}" onclick="selectNoteModule('${level}', '${mod.id}')">
                ${mod.title}
              </li>
            `).join("")}
          </ul>
        </div>
      `).join("");
    }

    // 取得當前單元內容
    let currentModule = null;
    for (const sub of notesData.subjects) {
      for (const mod of sub.modules) {
        if (mod.id === state.currentNoteModuleId) {
          currentModule = mod;
          break;
        }
      }
      if (currentModule) break;
    }

    // 若未找到則選第一個
    if (!currentModule && notesData.subjects[0]?.modules[0]) {
      currentModule = notesData.subjects[0].modules[0];
      state.currentNoteModuleId = currentModule.id;
    }

    const contentCard = document.getElementById("notesContentContainer");
    if (!contentCard || !currentModule) return;

    contentCard.innerHTML = `
      <h2>${currentModule.title}</h2>
      <div class="notes-keywords">
        ${currentModule.keywords.map(kw => `
          <span class="keyword-tag" onclick="speakEnglish('${kw}', this)">
            🔊 <b>${kw}</b>
          </span>
        `).join("")}
      </div>
      <div style="background:rgba(6,182,212,0.06);border-left:4px solid var(--cyber-cyan);padding:14px 18px;border-radius:0 var(--radius-md) var(--radius-md) 0;margin-bottom:24px;font-size:0.95rem;color:var(--text-main);">
        <strong>📌 核心架構概述：</strong>${currentModule.summary}
      </div>
      <div class="notes-body">
        ${formatMarkdownContent(currentModule.content)}
      </div>
      <div class="notes-case-box">
        <h4>💡 實務情境案例與考點剖析 (Case Study)：</h4>
        <div style="font-size:0.95rem;line-height:1.75;">${currentModule.caseStudy}</div>
      </div>
    `;
  }

  function formatMarkdownContent(mdText) {
    // 輕量化 Markdown 解析成 HTML
    return mdText
      .replace(/^### (.*$)/gim, "<h3>$1</h3>")
      .replace(/^## (.*$)/gim, "<h2>$1</h2>")
      .replace(/^\- (.*$)/gim, "<li>$1</li>")
      .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
      .replace(/\n\n/g, "<br>");
  }

  window.selectNoteModule = function (level, modId) {
    state.currentNoteLevel = level;
    state.currentNoteModuleId = modId;
    renderNotesView();
  };

  window.switchNotesLevel = function (level) {
    state.currentNoteLevel = level;
    state.currentNoteModuleId = level === "basic" ? "B1-M01" : "M1-M01";
    document.querySelectorAll(".notes-level-btn").forEach(b => {
      if (b.getAttribute("data-level") === level) b.classList.add("active");
      else b.classList.remove("active");
    });
    renderNotesView();
  };

  // ==========================================================================
  // 10. 初始化掛載
  // ==========================================================================
  document.addEventListener("DOMContentLoaded", () => {
    initTheme();
    speech.init();

    // 註冊主題切換按鈕
    const themeBtn = document.getElementById("themeToggleBtn");
    if (themeBtn) themeBtn.addEventListener("click", toggleTheme);

    // 註冊導航按鈕
    document.querySelectorAll(".nav-btn").forEach(btn => {
      btn.addEventListener("click", (e) => {
        const tab = e.currentTarget.getAttribute("data-tab");
        if (tab) switchTab(tab);
      });
    });

    // 註冊練習模式篩選監聽
    const pLevel = document.getElementById("practiceLevelSelect");
    const pDomain = document.getElementById("practiceDomainSelect");
    const pScenario = document.getElementById("practiceScenarioSwitch");
    const pSearch = document.getElementById("practiceSearchInput");

    if (pLevel) pLevel.addEventListener("change", (e) => {
      state.practice.level = e.target.value;
      renderPracticeView();
    });
    if (pDomain) pDomain.addEventListener("change", (e) => {
      state.practice.domain = e.target.value;
      renderPracticeView();
    });
    if (pScenario) pScenario.addEventListener("change", (e) => {
      state.practice.scenarioOnly = e.target.checked;
      renderPracticeView();
    });
    if (pSearch) pSearch.addEventListener("input", (e) => {
      state.practice.searchKeyword = e.target.value;
      renderPracticeView();
    });

    // 預設進入總覽
    switchTab("dashboard");
  });

})();
