/**
 * 英文歌學習系統 - 歌詞同步與字詞互動引擎 (Lyrics Engine)
 * 支援：
 * 1. 毫秒級雙語字幕即時同步、平滑自動滾動置中、卡拉OK動態發光
 * 2. 歌詞單字即點即查 (Interactive Word Lookup) 與生字本收藏
 * 3. 英文原句、KK音標/IPA、繁體中文翻譯、發音連音與語法註解
 * 4. LRC 格式時間戳記解析器 (支援使用者自訂匯入任何英文歌)
 */

class LyricsEngine {
  constructor(containerElement, onWordClickCallback, onLineClickCallback) {
    this.container = containerElement;
    this.onWordClick = onWordClickCallback;
    this.onLineClick = onLineClickCallback;

    this.lyrics = [];
    this.currentLineIndex = -1;
    this.autoScrollEnabled = true;
    this.displayMode = "bilingual"; // "bilingual" | "en-only" | "zh-only"
    this.showPhonetics = true;

    this.wordbookKey = "tom_song_wordbook_v1";
    this.wordbook = this._loadWordbook();
  }

  setLyrics(lyricsArray) {
    this.lyrics = lyricsArray || [];
    this.currentLineIndex = -1;
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

      // 單字分詞 HTML (將每個英文單字包覆為可點擊 token)
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
        // 如果點擊的是單字或按鈕，不觸發整行跳轉
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
      if (currentTime >= line.start && currentTime <= (line.end + 0.3)) {
        activeIndex = i;
        break;
      } else if (currentTime < line.start) {
        // 尚未到下一行，保持上一行
        if (i > 0 && currentTime >= this.lyrics[i - 1].start) {
          activeIndex = i - 1;
        }
        break;
      }
    }

    if (activeIndex === -1 && currentTime >= this.lyrics[this.lyrics.length - 1].start) {
      activeIndex = this.lyrics.length - 1;
    }

    if (activeIndex !== this.currentLineIndex) {
      // 移除舊的 active
      if (this.currentLineIndex >= 0) {
        const oldEl = document.getElementById(`lyric-line-${this.currentLineIndex}`);
        if (oldEl) {
          oldEl.classList.remove("active");
          const oldBar = oldEl.querySelector(".line-progress-bar .fill");
          if (oldBar) oldBar.style.width = "0%";
        }
      }

      this.currentLineIndex = activeIndex;

      // 設置新的 active
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

    // 更新當前行的卡拉OK進度條
    if (this.currentLineIndex >= 0 && this.currentLineIndex < this.lyrics.length) {
      const line = this.lyrics[this.currentLineIndex];
      const activeEl = document.getElementById(`lyric-line-${this.currentLineIndex}`);
      if (activeEl) {
        const duration = Math.max(0.1, line.end - line.start);
        const elapsed = Math.max(0, currentTime - line.start);
        const percent = Math.min(100, Math.max(0, (elapsed / duration) * 100));
        const fillBar = activeEl.querySelector(".line-progress-bar .fill");
        if (fillBar) fillBar.style.width = `${percent}%`;
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

    // 匹配英文單詞（保留撇號如 I'll, don't, we're）與其他符號
    const regex = /([a-zA-Z'’]+|[^a-zA-Z'’\s]+|\s+)/g;
    const parts = text.match(regex) || [];

    return parts.map(part => {
      // 判斷是否為英文單字
      if (/^[a-zA-Z'’]+$/.test(part)) {
        const cleanWord = part.replace(/['’]/g, "").toLowerCase();
        const isKey = cleanKeyWords.includes(cleanWord) || cleanKeyWords.some(k => k.includes(cleanWord));
        const keyClass = isKey ? "keyword" : "";
        return `<span class="word-token ${keyClass}" data-word="${this._escapeHtml(part)}" title="點擊查單字與音標">${this._escapeHtml(part)}</span>`;
      } else {
        return this._escapeHtml(part);
      }
    }).join("");
  }

  lookupWord(word) {
    const cleanWord = (word || "").replace(/[^a-zA-Z]/g, "").toLowerCase();
    if (!cleanWord) return null;

    // 先在內建單字庫搜尋
    if (SONG_DICTIONARY && SONG_DICTIONARY[cleanWord]) {
      return {
        word: cleanWord,
        original: word,
        ...SONG_DICTIONARY[cleanWord]
      };
    }

    // 簡易詞形還原 (lemmatization) 查找
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

    // 若未在內建庫，回傳基礎結構供線上發音與筆記
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
    utterance.rate = rate; // 略慢一點，適合學習者
    utterance.pitch = 1.0;

    // 優先選取高品質美式/英式英語語音
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
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  /**
   * LRC 格式歌詞解析器
   * 支援標準 [mm:ss.xx] 格式，並自動解析英中雙語或純英文
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
        // 檢查是否包含繁簡中文分離 (例如: "English Text | 中文翻譯" 或 "English Text / 中文")
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
            end: ts + 4.5, // 稍後排序後修正 end
            en: en,
            zh: zh,
            phonetic: "",
            notes: "",
            keyWords: []
          });
        });
      }
    }

    // 依時間排序並校正每句 end 時間
    parsedLines.sort((a, b) => a.start - b.start);
    for (let i = 0; i < parsedLines.length; i++) {
      if (i < parsedLines.length - 1) {
        parsedLines[i].end = Math.max(parsedLines[i].start + 1.0, parsedLines[i + 1].start - 0.2);
      }
    }

    return parsedLines;
  }
}
