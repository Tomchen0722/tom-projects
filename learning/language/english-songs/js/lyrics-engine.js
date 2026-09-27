/**
 * 英文歌學習系統 - 歌詞同步與字詞動作互動引擎 (Lyrics Engine)
 * 支援：
 * 1. 毫秒級雙語字幕即時同步、平滑自動滾動置中、卡拉OK動態發光
 * 2. 歌聲動作同步 (Singing Vocal Subtitle Motion)：
 *    字幕單字跟隨歌聲節奏逐字彈跳、發光與行進（字幕跟著歌聲一起動作）
 * 3. 歌詞單字即點即查 (Interactive Word Lookup) 與生字本收藏
 * 4. 英文原句、KK音標/IPA、繁體中文翻譯、發音連音與語法註解
 * 5. LRC 格式時間戳記解析器 (支援使用者自訂匯入任何英文歌)
 */

class LyricsEngine {
  constructor(containerElement, onWordClickCallback, onLineClickCallback, onWordSungCallback) {
    this.container = containerElement;
    this.onWordClick = onWordClickCallback;
    this.onLineClick = onLineClickCallback;
    this.onWordSung = onWordSungCallback;

    this.lyrics = [];
    this.currentLineIndex = -1;
    this.currentWordIndex = -1;
    this.autoScrollEnabled = true;
    this.displayMode = "bilingual"; // "bilingual" | "en-only" | "zh-only"
    this.showPhonetics = true;

    this.wordbookKey = "tom_song_wordbook_v1";
    this.wordbook = this._loadWordbook();
  }

  setLyrics(lyricsArray) {
    this.lyrics = lyricsArray || [];
    this.currentLineIndex = -1;
    this.currentWordIndex = -1;
    this.render();
  }

  setDisplayMode(mode) {
    this.displayMode = mode;
    this.render();
  }

  togglePhonetics(show) {
    this.showPhonetics = show;
    this.render();
  }

  toggleAutoScroll(enable) {
    this.autoScrollEnabled = enable;
  }

  render() {
    if (!this.container) return;
    this.container.innerHTML = "";

    if (!this.lyrics || this.lyrics.length === 0) {
      this.container.innerHTML = `
        <div class="empty-lyrics-notice">
          <span class="icon">🎵</span>
          <p>請選擇上方歌曲，或匯入自訂 LRC 歌詞檔案開始學習！</p>
        </div>
      `;
      return;
    }

    this.lyrics.forEach((line, index) => {
      const lineEl = document.createElement("div");
      lineEl.className = "lyric-line";
      lineEl.dataset.index = index;
      lineEl.id = `lyric-line-${index}`;

      if (index === this.currentLineIndex) {
        lineEl.classList.add("active");
      }

      // 時間標籤
      const timeStr = this._formatTime(line.start);

      // 單字分詞 HTML (將每個英文單字包覆為可點擊 token 並標註序號)
      const wordsHtml = this._tokenizeEnglishText(line.en, line.keyWords);

      // 繁體中文與註解 HTML
      let zhHtml = "";
      if (this.displayMode !== "en-only" && line.zh) {
        zhHtml = `<div class="lyric-zh">${this._escapeHtml(line.zh)}</div>`;
      }

      // 音標
      let phoneticHtml = "";
      if (this.showPhonetics && line.phonetic) {
        phoneticHtml = `<div class="lyric-phonetic">/${this._escapeHtml(line.phonetic)}/</div>`;
      }

      // 語法與片語提示
      let notesHtml = "";
      if (line.notes && this.displayMode === "bilingual") {
        notesHtml = `<div class="lyric-notes"><span class="badge">解析</span> ${this._escapeHtml(line.notes)}</div>`;
      }

      lineEl.innerHTML = `
        <div class="lyric-meta">
          <span class="lyric-time" title="點擊跳轉至此時間">${timeStr}</span>
          <div class="lyric-actions">
            <button class="btn-line-action btn-speak" title="朗讀此句 (TTS)" data-action="speak" data-text="${this._escapeHtml(line.en)}">
              🔊
            </button>
            <button class="btn-line-action btn-loop-line" title="單句重複循環" data-action="loop" data-index="${index}">
              🔂
            </button>
          </div>
        </div>
        <div class="lyric-content">
          ${phoneticHtml}
          <div class="lyric-en">${wordsHtml}</div>
          ${zhHtml}
          ${notesHtml}
        </div>
        <div class="line-progress-bar"><div class="fill"></div></div>
      `;

      // 綁定行點擊跳轉
      lineEl.addEventListener("click", (e) => {
        const wordToken = e.target.closest(".word-token");
        if (wordToken) {
          e.stopPropagation();
          const rawWord = wordToken.dataset.word;
          if (this.onWordClick) this.onWordClick(rawWord, line);
          return;
        }

        const actionBtn = e.target.closest(".btn-line-action");
        if (actionBtn) {
          const action = actionBtn.dataset.action;
          if (action === "speak") {
            e.stopPropagation();
            this.speakText(actionBtn.dataset.text);
            return;
          } else if (action === "loop") {
            e.stopPropagation();
            if (this.onLineClick) this.onLineClick(index, line, true);
            return;
          }
        }

        if (this.onLineClick) {
          this.onLineClick(index, line, false);
        }
      });

      this.container.appendChild(lineEl);
    });
  }

  updateTime(currentTime) {
    if (!this.lyrics || this.lyrics.length === 0) return;

    // 尋找當前對應的歌詞行
    let activeIndex = -1;
    for (let i = 0; i < this.lyrics.length; i++) {
      const line = this.lyrics[i];
      if (currentTime >= line.start && currentTime <= (line.end + 0.35)) {
        activeIndex = i;
        break;
      } else if (currentTime < line.start) {
        if (i > 0 && currentTime >= this.lyrics[i - 1].start) {
          activeIndex = i - 1;
        }
        break;
      }
    }

    if (activeIndex === -1 && currentTime >= this.lyrics[this.lyrics.length - 1].start) {
      activeIndex = this.lyrics.length - 1;
    }

    // 行切換處理
    if (activeIndex !== this.currentLineIndex) {
      // 清除舊行狀態
      if (this.currentLineIndex >= 0) {
        const oldEl = document.getElementById(`lyric-line-${this.currentLineIndex}`);
        if (oldEl) {
          oldEl.classList.remove("active");
          const oldBar = oldEl.querySelector(".line-progress-bar .fill");
          if (oldBar) oldBar.style.width = "0%";
          oldEl.querySelectorAll(".word-token").forEach(t => {
            t.classList.remove("sung", "singing-now");
          });
        }
      }

      this.currentLineIndex = activeIndex;
      this.currentWordIndex = -1;

      // 設置新 active 行
      if (activeIndex >= 0) {
        const newEl = document.getElementById(`lyric-line-${activeIndex}`);
        if (newEl) {
          newEl.classList.add("active");
          if (this.autoScrollEnabled) {
            this._scrollToActiveLine(newEl);
          }
        }
      }
    }

    // 更新當前行的字幕動作（字詞逐字高亮與進度條）
    if (this.currentLineIndex >= 0 && this.currentLineIndex < this.lyrics.length) {
      const line = this.lyrics[this.currentLineIndex];
      const activeEl = document.getElementById(`lyric-line-${this.currentLineIndex}`);
      if (activeEl) {
        const duration = Math.max(0.1, line.end - line.start);
        const elapsed = Math.max(0, currentTime - line.start);
        const progressRatio = Math.min(1.0, Math.max(0, elapsed / duration));

        // 底線進度
        const fillBar = activeEl.querySelector(".line-progress-bar .fill");
        if (fillBar) fillBar.style.width = `${(progressRatio * 100).toFixed(1)}%`;

        // 🌟 歌聲字幕動作 (Word-by-word dynamic motion tracking vocal singing)
        const wordTokens = activeEl.querySelectorAll(".word-token");
        if (wordTokens && wordTokens.length > 0) {
          const totalWords = wordTokens.length;
          // 計算當前演唱到的單字索引
          const targetWordIdx = Math.min(totalWords - 1, Math.floor(progressRatio * totalWords));

          if (targetWordIdx !== this.currentWordIndex) {
            this.currentWordIndex = targetWordIdx;
            wordTokens.forEach((tok, wIdx) => {
              if (wIdx < targetWordIdx) {
                tok.classList.add("sung");
                tok.classList.remove("singing-now");
              } else if (wIdx === targetWordIdx) {
                tok.classList.add("sung", "singing-now");
              } else {
                tok.classList.remove("sung", "singing-now");
              }
            });

            if (this.onWordSung) {
              const sungWord = wordTokens[targetWordIdx]?.dataset?.word || "";
              this.onWordSung(this.currentLineIndex, targetWordIdx, sungWord, line);
            }
          }
        }
      }
    }
  }

  _scrollToActiveLine(element) {
    if (!element || !this.container) return;
    const containerHeight = this.container.clientHeight;
    const elementTop = element.offsetTop;
    const elementHeight = element.clientHeight;
    const targetScrollTop = elementTop - containerHeight / 2 + elementHeight / 2;

    this.container.scrollTo({
      top: Math.max(0, targetScrollTop),
      behavior: "smooth"
    });
  }

  _tokenizeEnglishText(text, keyWords = []) {
    if (!text) return "";
    const cleanKeyWords = (keyWords || []).map(k => k.toLowerCase().trim());

    // 匹配英文單詞（保留撇號如 I'll, don't, we're）與其他標點符號
    const regex = /([a-zA-Z'’]+|[^a-zA-Z'’\s]+|\s+)/g;
    const parts = text.match(regex) || [];

    let wordIndex = 0;
    return parts.map(part => {
      if (/^[a-zA-Z'’]+$/.test(part)) {
        const cleanWord = part.replace(/['’]/g, "").toLowerCase();
        const isKey = cleanKeyWords.includes(cleanWord) || cleanKeyWords.some(k => k.includes(cleanWord));
        const keyClass = isKey ? "keyword" : "";
        const idx = wordIndex++;
        return `<span class="word-token ${keyClass}" data-word="${this._escapeHtml(part)}" data-word-idx="${idx}" title="點擊查單字與音標">${this._escapeHtml(part)}</span>`;
      } else {
        return this._escapeHtml(part);
      }
    }).join("");
  }

  lookupWord(word) {
    const cleanWord = (word || "").replace(/[^a-zA-Z]/g, "").toLowerCase();
    if (!cleanWord) return null;

    if (SONG_DICTIONARY && SONG_DICTIONARY[cleanWord]) {
      return {
        word: cleanWord,
        original: word,
        ...SONG_DICTIONARY[cleanWord]
      };
    }

    const variations = [
      cleanWord.replace(/ing$/, ""),
      cleanWord.replace(/ed$/, ""),
      cleanWord.replace(/s$/, ""),
      cleanWord.replace(/es$/, ""),
      cleanWord.replace(/ly$/, "")
    ];

    for (const v of variations) {
      if (SONG_DICTIONARY && SONG_DICTIONARY[v]) {
        return {
          word: cleanWord,
          baseWord: v,
          original: word,
          ...SONG_DICTIONARY[v]
        };
      }
    }

    return {
      word: cleanWord,
      original: word,
      kk: "/ipa/",
      pos: "word",
      zh: "點擊發音按鈕聆聽真人發音，或在右側筆記本記錄個人心得。",
      desc: "常用英文詞彙，可透過語意與上下文加深記憶。"
    };
  }

  speakText(text, rate = 0.9) {
    if (!("speechSynthesis" in window)) {
      alert("您的瀏覽器不支援語音合成發音。");
      return;
    }

    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "en-US";
    utterance.rate = rate;
    utterance.pitch = 1.0;

    const voices = window.speechSynthesis.getVoices();
    const preferredVoice = voices.find(v => v.lang.startsWith("en") && (v.name.includes("Google") || v.name.includes("Natural") || v.name.includes("Samantha") || v.name.includes("Zira")));
    if (preferredVoice) {
      utterance.voice = preferredVoice;
    }

    window.speechSynthesis.speak(utterance);
  }

  // 生字本功能 (LocalStorage)
  _loadWordbook() {
    try {
      const data = localStorage.getItem(this.wordbookKey);
      return data ? JSON.parse(data) : [];
    } catch (e) {
      return [];
    }
  }

  saveWordToBook(wordObj) {
    if (!wordObj || !wordObj.word) return false;
    const exists = this.wordbook.some(item => item.word.toLowerCase() === wordObj.word.toLowerCase());
    if (!exists) {
      this.wordbook.unshift({
        ...wordObj,
        addedAt: new Date().toLocaleDateString("zh-TW")
      });
      localStorage.setItem(this.wordbookKey, JSON.stringify(this.wordbook));
      return true;
    }
    return false;
  }

  removeWordFromBook(word) {
    this.wordbook = this.wordbook.filter(item => item.word.toLowerCase() !== word.toLowerCase());
    localStorage.setItem(this.wordbookKey, JSON.stringify(this.wordbook));
  }

  getWordbook() {
    return this.wordbook;
  }

  _formatTime(seconds) {
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins}:${secs < 10 ? "0" : ""}${secs}`;
  }

  _escapeHtml(text) {
    return (text || "")
      .replace(/&/g, "&amp;")
      .replace(/&lt;/g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  /**
   * LRC 格式歌詞解析器
   */
  static parseLRC(lrcText) {
    const lines = lrcText.split(/\r?\n/);
    const parsedLines = [];
    const timeRegex = /\[(\d{2}):(\d{2})(?:\.(\d{2,3}))?\]/g;

    for (let i = 0; i < lines.length; i++) {
      const rawLine = lines[i].trim();
      if (!rawLine) continue;

      let match;
      const timestamps = [];
      while ((match = timeRegex.exec(rawLine)) !== null) {
        const mins = parseInt(match[1], 10);
        const secs = parseInt(match[2], 10);
        const ms = match[3] ? parseInt(match[3].padEnd(3, "0").slice(0, 3), 10) : 0;
        const totalSecs = mins * 60 + secs + ms / 1000;
        timestamps.push(totalSecs);
      }

      const text = rawLine.replace(timeRegex, "").trim();
      if (text && timestamps.length > 0) {
        let en = text;
        let zh = "";
        if (text.includes("|")) {
          const parts = text.split("|");
          en = parts[0].trim();
          zh = parts[1].trim();
        } else if (text.includes(" - ") && /[\u4e00-\u9fa5]/.test(text)) {
          const parts = text.split(" - ");
          en = parts[0].trim();
          zh = parts[1].trim();
        }

        timestamps.forEach(ts => {
          parsedLines.push({
            start: ts,
            end: ts + 4.5,
            en: en,
            zh: zh,
            phonetic: "",
            notes: "",
            keyWords: []
          });
        });
      }
    }

    parsedLines.sort((a, b) => a.start - b.start);
    for (let i = 0; i < parsedLines.length; i++) {
      if (i < parsedLines.length - 1) {
        parsedLines[i].end = Math.max(parsedLines[i].start + 1.0, parsedLines[i + 1].start - 0.2);
      }
    }

    return parsedLines;
  }
}
