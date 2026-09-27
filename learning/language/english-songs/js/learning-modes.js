/**
 * 英文歌學習系統 - 學習模式與互動測驗模組 (Learning Modes)
 * 支援：
 * 1. 聽力克漏字練習 (Listening Cloze Test): 挖空關鍵字、慢速聽辨、即時反饋
 * 2. 影子跟讀錄音比對 (Shadowing Recording & Compare): 錄下自己聲音與原聲對照
 * 3. 歌曲單字閃卡 (Song Vocabulary Flashcards): 3D 翻牌記憶、發音與例句
 * 4. 個人生字庫管理與匯出 (Wordbook Manager): 隨堂收藏、Anki 匯出
 */

class LearningModesManager {
  constructor(player, lyricsEngine) {
    this.player = player;
    this.lyricsEngine = lyricsEngine;

    // 克漏字狀態
    this.clozeCurrentIndex = 0;
    this.clozeScore = { correct: 0, total: 0, streak: 0 };
    this.clozeCurrentQuestion = null;

    // 錄音狀態
    this.mediaRecorder = null;
    this.audioChunks = [];
    this.userRecordedAudioUrl = null;
    this.isRecording = false;

    // 閃卡狀態
    this.flashcards = [];
    this.currentCardIndex = 0;
    this.cardFlipped = false;
  }

  /* ══════════════════════════════════════════════════════════════
     1. 聽力克漏字練習模式 (Listening Cloze)
     ══════════════════════════════════════════════════════════════ */
  startClozeTest(containerEl, song) {
    if (!song || !song.lyrics || song.lyrics.length === 0) {
      containerEl.innerHTML = `<div class="cloze-empty">當前歌曲沒有歌詞資料。</div>`;
      return;
    }

    this.clozeContainer = containerEl;
    this.currentSong = song;
    this.clozeCurrentIndex = 0;
    this.clozeScore = { correct: 0, total: 0, streak: 0 };

    this.renderClozeQuestion();
  }

  renderClozeQuestion() {
    if (!this.clozeContainer || !this.currentSong) return;

    const lyrics = this.currentSong.lyrics;
    if (this.clozeCurrentIndex >= lyrics.length) {
      // 測驗完成統計
      const accuracy = this.clozeScore.total > 0 
        ? Math.round((this.clozeScore.correct / this.clozeScore.total) * 100) 
        : 0;
      this.clozeContainer.innerHTML = `
        <div class="cloze-result-card">
          <div class="result-badge">🏆 挑戰完成！</div>
          <h3>${this.currentSong.title} 聽力克漏字測驗結果</h3>
          <div class="score-display">
            <div class="score-item">
              <span class="num">${this.clozeScore.correct} / ${this.clozeScore.total}</span>
              <span class="label">答對題數</span>
            </div>
            <div class="score-item">
              <span class="num">${accuracy}%</span>
              <span class="label">正確率</span>
            </div>
            <div class="score-item">
              <span class="num">${this.clozeScore.streak}</span>
              <span class="label">最高連擊</span>
            </div>
          </div>
          <div class="result-actions">
            <button class="btn btn-primary" id="btn-restart-cloze">🔄 再次挑戰</button>
            <button class="btn btn-secondary" id="btn-back-lyrics">📖 返回歌詞播放</button>
          </div>
        </div>
      `;

      document.getElementById("btn-restart-cloze")?.addEventListener("click", () => {
        this.clozeCurrentIndex = 0;
        this.clozeScore = { correct: 0, total: 0, streak: 0 };
        this.renderClozeQuestion();
      });

      document.getElementById("btn-back-lyrics")?.addEventListener("click", () => {
        const tabLyrics = document.querySelector('[data-tab="lyrics"]');
        if (tabLyrics) tabLyrics.click();
      });
      return;
    }

    const currentLine = lyrics[this.clozeCurrentIndex];
    // 挑選挖空的單字
    const words = currentLine.en.split(/\s+/).map(w => w.replace(/[^a-zA-Z]/g, "")).filter(w => w.length > 2);
    let targetWord = words.length > 0 ? words[Math.floor(Math.random() * words.length)] : "you";

    // 優先挑選重點單字
    if (currentLine.keyWords && currentLine.keyWords.length > 0) {
      const match = words.find(w => currentLine.keyWords.some(kw => kw.toLowerCase().includes(w.toLowerCase())));
      if (match) targetWord = match;
    }

    this.clozeCurrentQuestion = {
      line: currentLine,
      targetWord: targetWord,
      options: this._generateOptions(targetWord)
    };

    // 產生挖空文本
    const regex = new RegExp(`\\b${targetWord}\\b`, "i");
    const maskedEn = currentLine.en.replace(regex, `<span class="blank-spot" id="blank-spot">______</span>`);

    this.clozeContainer.innerHTML = `
      <div class="cloze-quiz-card">
        <div class="quiz-header">
          <div class="quiz-progress">題目 ${this.clozeCurrentIndex + 1} / ${lyrics.length}</div>
          <div class="quiz-stats">
            <span>✨ 得分: ${this.clozeScore.correct}</span>
            <span>🔥 連擊: ${this.clozeScore.streak}</span>
          </div>
        </div>

        <div class="quiz-audio-deck">
          <button class="btn-play-line" id="btn-cloze-play-normal" title="正常速度播放此句">
            ▶️ 播放原句
          </button>
          <button class="btn-play-line slow" id="btn-cloze-play-slow" title="0.75x 慢速聽細節">
            🐢 0.75x 慢速
          </button>
          <button class="btn-play-line" id="btn-cloze-tts" title="TTS 標準發音">
            🗣️ 單句朗讀
          </button>
        </div>

        <div class="quiz-sentence-box">
          <div class="quiz-sentence-en">${maskedEn}</div>
          <div class="quiz-sentence-zh">${currentLine.zh || ""}</div>
          <div class="quiz-phonetic">/${currentLine.phonetic || ""}/</div>
        </div>

        <div class="quiz-answer-zone">
          <div class="quiz-input-group">
            <input type="text" id="cloze-input-box" placeholder="聽寫出挖空的英文單字..." autocomplete="off" autocapitalize="off" />
            <button class="btn btn-primary" id="btn-cloze-submit">送出答案</button>
          </div>

          <div class="quiz-options-divider">或從選項中選擇</div>
          <div class="quiz-options-grid" id="cloze-options-grid">
            ${this.clozeCurrentQuestion.options.map(opt => `
              <button class="btn-option" data-val="${opt}">${opt}</button>
            `).join("")}
          </div>
        </div>

        <div class="quiz-feedback-box" id="quiz-feedback-box" style="display:none;"></div>

        <div class="quiz-footer-actions">
          <button class="btn btn-link" id="btn-cloze-hint">💡 提示字首與釋義</button>
          <button class="btn btn-link" id="btn-cloze-skip">跳過此題 ⏩</button>
        </div>
      </div>
    `;

    // 綁定事件
    const inputEl = document.getElementById("cloze-input-box");
    const submitBtn = document.getElementById("btn-cloze-submit");

    document.getElementById("btn-cloze-play-normal")?.addEventListener("click", () => {
      this.player.setRate(1.0);
      this.player.seek(currentLine.start);
      this.player.play();
    });

    document.getElementById("btn-cloze-play-slow")?.addEventListener("click", () => {
      this.player.setRate(0.75);
      this.player.seek(currentLine.start);
      this.player.play();
    });

    document.getElementById("btn-cloze-tts")?.addEventListener("click", () => {
      this.lyricsEngine.speakText(currentLine.en, 0.85);
    });

    submitBtn?.addEventListener("click", () => {
      this._checkAnswer(inputEl.value.trim());
    });

    inputEl?.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        this._checkAnswer(inputEl.value.trim());
      }
    });

    document.querySelectorAll(".btn-option").forEach(btn => {
      btn.addEventListener("click", (e) => {
        this._checkAnswer(e.target.dataset.val);
      });
    });

    document.getElementById("btn-cloze-hint")?.addEventListener("click", () => {
      const hintChar = targetWord.charAt(0).toUpperCase();
      const wordInfo = this.lyricsEngine.lookupWord(targetWord);
      const meaning = wordInfo ? wordInfo.zh : "歌曲關鍵單字";
      this._showFeedback(`💡 提示：字首為【${hintChar}】，長度為 ${targetWord.length} 個字母；中文意義：${meaning}`, "hint");
    });

    document.getElementById("btn-cloze-skip")?.addEventListener("click", () => {
      this._showFeedback(`答案是：<strong>${targetWord}</strong>`, "info");
      setTimeout(() => {
        this.clozeCurrentIndex++;
        this.renderClozeQuestion();
      }, 1500);
    });

    // 自動聚焦輸入框並自動播放該句
    setTimeout(() => {
      inputEl?.focus();
      this.player.seek(currentLine.start);
      this.player.play();
    }, 200);
  }

  _generateOptions(targetWord) {
    const pool = ["together", "forever", "shining", "remember", "beautiful", "wonder", "castle", "silence", "shoulder", "promise", "beloved", "courage", "whisper", "freedom", "journey"];
    const options = [targetWord.toLowerCase()];
    while (options.length < 4) {
      const candidate = pool[Math.floor(Math.random() * pool.length)];
      if (!options.includes(candidate)) {
        options.push(candidate);
      }
    }
    // 隨機洗牌
    return options.sort(() => Math.random() - 0.5);
  }

  _checkAnswer(userWord) {
    if (!this.clozeCurrentQuestion || !userWord) return;

    const target = this.clozeCurrentQuestion.targetWord.toLowerCase();
    const cleanUser = userWord.toLowerCase().replace(/[^a-zA-Z]/g, "");

    this.clozeScore.total++;

    if (cleanUser === target) {
      this.clozeScore.correct++;
      this.clozeScore.streak++;

      // 替換挖空視覺
      const blankEl = document.getElementById("blank-spot");
      if (blankEl) {
        blankEl.textContent = this.clozeCurrentQuestion.targetWord;
        blankEl.classList.add("correct");
      }

      this._showFeedback(`🎉 太棒了！答對了：<strong>${this.clozeCurrentQuestion.targetWord}</strong>`, "success");

      // 正確音效發音
      this.lyricsEngine.speakText(this.clozeCurrentQuestion.targetWord, 1.0);

      setTimeout(() => {
        this.clozeCurrentIndex++;
        this.renderClozeQuestion();
      }, 1400);
    } else {
      this.clozeScore.streak = 0;
      this._showFeedback(`❌ 再聽一次！正確答案是：<strong>${this.clozeCurrentQuestion.targetWord}</strong>`, "error");

      setTimeout(() => {
        this.clozeCurrentIndex++;
        this.renderClozeQuestion();
      }, 2000);
    }
  }

  _showFeedback(msg, type) {
    const box = document.getElementById("quiz-feedback-box");
    if (!box) return;
    box.style.display = "block";
    box.className = `quiz-feedback-box ${type}`;
    box.innerHTML = msg;
  }

  /* ══════════════════════════════════════════════════════════════
     2. 影子跟讀與錄音比對模式 (Shadowing Mode)
     ══════════════════════════════════════════════════════════════ */
  renderShadowingStudio(containerEl, song, currentLine) {
    this.shadowingContainer = containerEl;
    if (!song || !currentLine) {
      containerEl.innerHTML = `<div class="shadow-empty">請先在歌詞清單點選任意一句進行跟讀練習。</div>`;
      return;
    }

    containerEl.innerHTML = `
      <div class="shadow-studio-card">
        <div class="studio-header">
          <h3>🎙️ 影子跟讀與口音發音比對工作台</h3>
          <p>先聽原唱，再點擊錄音並模仿語調連音，雙軌播放比對細微發音差距！</p>
        </div>

        <div class="shadow-focused-line">
          <div class="line-phonetic">/${currentLine.phonetic || ""}/</div>
          <div class="line-en">${currentLine.en}</div>
          <div class="line-zh">${currentLine.zh}</div>
          ${currentLine.notes ? `<div class="line-notes">${currentLine.notes}</div>` : ""}
        </div>

        <div class="shadow-controls-grid">
          <!-- 原聲對照 -->
          <div class="track-card original-track">
            <h4>🎵 原唱示範</h4>
            <div class="track-actions">
              <button class="btn btn-secondary" id="btn-shadow-play-orig">▶️ 播放原句</button>
              <button class="btn btn-secondary" id="btn-shadow-play-slow">🐢 0.75x 慢速聽音</button>
              <button class="btn btn-secondary" id="btn-shadow-tts">🗣️ 慢速真人朗讀</button>
            </div>
          </div>

          <!-- 我的錄音 -->
          <div class="track-card user-track">
            <h4>🎤 我的跟讀錄音</h4>
            <div class="record-meter" id="record-meter">
              <div class="record-indicator" id="record-indicator">● 未錄音</div>
              <span id="record-timer">00:00</span>
            </div>
            <div class="track-actions">
              <button class="btn btn-danger" id="btn-record-toggle">🎙️ 開始錄音</button>
              <button class="btn btn-primary" id="btn-play-user-record" disabled>▶️ 播放我的發音</button>
            </div>
          </div>
        </div>

        <div class="shadow-tips">
          <h4>💡 英語唱歌跟讀三大秘訣：</h4>
          <ul>
            <li><strong>連音 (Linking)：</strong>注意輔音加母音連讀，例如 "find out" 聽起來像 "fine-dout"。</li>
            <li><strong>弱化 (Weak Forms)：</strong>and, of, to, you 等虛詞在旋律中常被極度弱讀，讓出重音給主詞與動詞。</li>
            <li><strong>放慢模仿 (Slow Practice)：</strong>善用 0.75x 慢速播放，把每個母音飽滿度聽清再發聲！</li>
          </ul>
        </div>
      </div>
    `;

    // 綁定跟讀按鈕
    document.getElementById("btn-shadow-play-orig")?.addEventListener("click", () => {
      this.player.setRate(1.0);
      this.player.seek(currentLine.start);
      this.player.play();
    });

    document.getElementById("btn-shadow-play-slow")?.addEventListener("click", () => {
      this.player.setRate(0.75);
      this.player.seek(currentLine.start);
      this.player.play();
    });

    document.getElementById("btn-shadow-tts")?.addEventListener("click", () => {
      this.lyricsEngine.speakText(currentLine.en, 0.8);
    });

    const recordBtn = document.getElementById("btn-record-toggle");
    const playUserBtn = document.getElementById("btn-play-user-record");

    recordBtn?.addEventListener("click", () => {
      if (this.isRecording) {
        this._stopRecording(recordBtn, playUserBtn);
      } else {
        this._startRecording(recordBtn, playUserBtn);
      }
    });

    playUserBtn?.addEventListener("click", () => {
      if (this.userRecordedAudioUrl) {
        const audio = new Audio(this.userRecordedAudioUrl);
        audio.play();
      }
    });
  }

  async _startRecording(recordBtn, playUserBtn) {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      this.mediaRecorder = new MediaRecorder(stream);
      this.audioChunks = [];

      this.mediaRecorder.ondataavailable = (e) => {
        if (e.data.size > 0) this.audioChunks.push(e.data);
      };

      this.mediaRecorder.onstop = () => {
        const audioBlob = new Blob(this.audioChunks, { type: "audio/webm" });
        this.userRecordedAudioUrl = URL.createObjectURL(audioBlob);
        if (playUserBtn) playUserBtn.disabled = false;
        stream.getTracks().forEach(track => track.stop());
      };

      this.mediaRecorder.start();
      this.isRecording = true;
      recordBtn.innerHTML = "⏹️ 停止錄音";
      recordBtn.classList.add("recording");

      const indicator = document.getElementById("record-indicator");
      if (indicator) {
        indicator.textContent = "🔴 錄音中...";
        indicator.classList.add("recording");
      }

      // 計時器
      let seconds = 0;
      this._recordTimerInterval = setInterval(() => {
        seconds++;
        const timerEl = document.getElementById("record-timer");
        if (timerEl) {
          const m = String(Math.floor(seconds / 60)).padStart(2, "0");
          const s = String(seconds % 60).padStart(2, "0");
          timerEl.textContent = `${m}:${s}`;
        }
      }, 1000);

    } catch (err) {
      alert("無法啟用麥克風，請檢查瀏覽器麥克風權限設定。");
      console.error(err);
    }
  }

  _stopRecording(recordBtn, playUserBtn) {
    if (this.mediaRecorder && this.isRecording) {
      this.mediaRecorder.stop();
      this.isRecording = false;
      clearInterval(this._recordTimerInterval);

      recordBtn.innerHTML = "🎙️ 重新錄音";
      recordBtn.classList.remove("recording");

      const indicator = document.getElementById("record-indicator");
      if (indicator) {
        indicator.textContent = "✅ 錄音完成";
        indicator.classList.remove("recording");
      }
    }
  }

  /* ══════════════════════════════════════════════════════════════
     3. 歌曲單字閃卡記憶 (Flashcards)
     ══════════════════════════════════════════════════════════════ */
  renderSongFlashcards(containerEl, song) {
    if (!song) return;

    // 收集該歌曲的所有關鍵字
    const wordsSet = new Set();
    (song.lyrics || []).forEach(line => {
      (line.keyWords || []).forEach(w => wordsSet.add(w.toLowerCase()));
    });

    this.flashcards = Array.from(wordsSet).map(w => {
      return this.lyricsEngine.lookupWord(w) || {
        word: w,
        kk: "/ipa/",
        pos: "word",
        zh: "歌曲核心單字",
        desc: ""
      };
    });

    this.currentCardIndex = 0;
    this.cardFlipped = false;
    this.flashcardsContainer = containerEl;

    this.renderCurrentFlashcard();
  }

  renderCurrentFlashcard() {
    if (!this.flashcardsContainer) return;

    if (this.flashcards.length === 0) {
      this.flashcardsContainer.innerHTML = `<div class="flashcards-empty">本首歌曲尚未建立精選單字卡。</div>`;
      return;
    }

    const card = this.flashcards[this.currentCardIndex];

    this.flashcardsContainer.innerHTML = `
      <div class="flashcard-studio">
        <div class="flashcard-header">
          <span>單字卡 ${this.currentCardIndex + 1} / ${this.flashcards.length}</span>
          <button class="btn btn-sm" id="btn-save-to-wordbook">⭐ 加入生字筆記</button>
        </div>

        <div class="flashcard-scene" id="flashcard-scene">
          <div class="flashcard ${this.cardFlipped ? "is-flipped" : ""}" id="main-flashcard">
            <div class="flashcard-face flashcard-front">
              <div class="card-tag">English Word</div>
              <div class="card-word">${card.word}</div>
              <div class="card-phonetic">${card.kk || ""}</div>
              <button class="btn-sound" id="btn-card-sound">🔊 聆聽真人發音</button>
              <div class="card-hint">（點擊卡片翻面看中文釋義）</div>
            </div>
            <div class="flashcard-face flashcard-back">
              <div class="card-tag">詞性與釋義</div>
              <div class="card-pos">${card.pos || ""}</div>
              <div class="card-zh">${card.zh}</div>
              <div class="card-desc">${card.desc || ""}</div>
              <div class="card-hint">（再次點擊翻回正面）</div>
            </div>
          </div>
        </div>

        <div class="flashcard-actions">
          <button class="btn btn-secondary" id="btn-card-prev" ${this.currentCardIndex === 0 ? "disabled" : ""}>⬅️ 上一個</button>
          <button class="btn btn-primary" id="btn-card-flip">🔄 翻轉卡片</button>
          <button class="btn btn-secondary" id="btn-card-next" ${this.currentCardIndex === this.flashcards.length - 1 ? "disabled" : ""}>下一個 ➡️</button>
        </div>
      </div>
    `;

    const cardEl = document.getElementById("main-flashcard");
    const flipCard = () => {
      this.cardFlipped = !this.cardFlipped;
      cardEl?.classList.toggle("is-flipped", this.cardFlipped);
    };

    document.getElementById("flashcard-scene")?.addEventListener("click", flipCard);
    document.getElementById("btn-card-flip")?.addEventListener("click", flipCard);

    document.getElementById("btn-card-sound")?.addEventListener("click", (e) => {
      e.stopPropagation();
      this.lyricsEngine.speakText(card.word, 0.9);
    });

    document.getElementById("btn-save-to-wordbook")?.addEventListener("click", () => {
      const added = this.lyricsEngine.saveWordToBook(card);
      alert(added ? `已將「${card.word}」加入個人生字筆記本！` : `「${card.word}」已在筆記本中。`);
    });

    document.getElementById("btn-card-prev")?.addEventListener("click", () => {
      if (this.currentCardIndex > 0) {
        this.currentCardIndex--;
        this.cardFlipped = false;
        this.renderCurrentFlashcard();
      }
    });

    document.getElementById("btn-card-next")?.addEventListener("click", () => {
      if (this.currentCardIndex < this.flashcards.length - 1) {
        this.currentCardIndex++;
        this.cardFlipped = false;
        this.renderCurrentFlashcard();
      }
    });
  }

  /* ══════════════════════════════════════════════════════════════
     4. 個人生字筆記本抽屜 (Wordbook Drawer)
     ══════════════════════════════════════════════════════════════ */
  renderWordbookList(containerEl) {
    const list = this.lyricsEngine.getWordbook();

    if (!list || list.length === 0) {
      containerEl.innerHTML = `
        <div class="wordbook-empty">
          <span class="icon">📖</span>
          <p>生字筆記本目前空空如也。</p>
          <p class="sub">在歌詞中點擊任何不熟的單字，點選「⭐ 收藏至生字本」，隨時複習！</p>
        </div>
      `;
      return;
    }

    containerEl.innerHTML = `
      <div class="wordbook-header-bar">
        <span>共收藏 ${list.length} 個英文單字</span>
        <div class="wb-actions">
          <button class="btn btn-sm btn-secondary" id="btn-export-wordbook">💾 匯出生字卡 (TXT)</button>
          <button class="btn btn-sm btn-danger" id="btn-clear-wordbook">🗑️ 全部清空</button>
        </div>
      </div>
      <div class="wordbook-cards-grid">
        ${list.map(item => `
          <div class="wb-card">
            <div class="wb-top">
              <span class="wb-word">${item.word}</span>
              <span class="wb-pos">${item.pos || ""}</span>
              <button class="btn-icon btn-wb-speak" data-word="${item.word}">🔊</button>
              <button class="btn-icon btn-wb-del" data-word="${item.word}" title="移除">✕</button>
            </div>
            <div class="wb-phonetic">${item.kk || ""}</div>
            <div class="wb-zh">${item.zh}</div>
            ${item.desc ? `<div class="wb-desc">${item.desc}</div>` : ""}
            <div class="wb-date">收藏於：${item.addedAt || "今日"}</div>
          </div>
        `).join("")}
      </div>
    `;

    // 綁定發音與刪除
    containerEl.querySelectorAll(".btn-wb-speak").forEach(btn => {
      btn.addEventListener("click", () => {
        this.lyricsEngine.speakText(btn.dataset.word, 0.9);
      });
    });

    containerEl.querySelectorAll(".btn-wb-del").forEach(btn => {
      btn.addEventListener("click", () => {
        if (confirm(`確定要從生字本移除「${btn.dataset.word}」嗎？`)) {
          this.lyricsEngine.removeWordFromBook(btn.dataset.word);
          this.renderWordbookList(containerEl);
        }
      });
    });

    document.getElementById("btn-clear-wordbook")?.addEventListener("click", () => {
      if (confirm("確定要清空所有收藏的生字嗎？此動作無法復原。")) {
        localStorage.removeItem(this.lyricsEngine.wordbookKey);
        this.lyricsEngine.wordbook = [];
        this.renderWordbookList(containerEl);
      }
    });

    document.getElementById("btn-export-wordbook")?.addEventListener("click", () => {
      let txtContent = "英文單字\t音標\t詞性\t中文釋義\t備註例句\n";
      list.forEach(i => {
        txtContent += `${i.word}\t${i.kk || ""}\t${i.pos || ""}\t${i.zh}\t${i.desc || ""}\n`;
      });
      const blob = new Blob([txtContent], { type: "text/plain;charset=utf-8" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `Tom_English_Songs_Wordbook_${new Date().toISOString().slice(0, 10)}.txt`;
      a.click();
    });
  }
}
