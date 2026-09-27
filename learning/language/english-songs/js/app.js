/**
 * 英文歌學習系統 - 核心應用程式調度器 (Main Application Controller)
 */

document.addEventListener("DOMContentLoaded", () => {
  // 核心模組實例化
  const lyricsContainer = document.getElementById("lyrics-container");
  const player = new EnglishSongPlayer();

  let currentSong = SONGS_DATA[0];
  let customSongs = [];

  // 歌詞引擎實例化
  const lyricsEngine = new LyricsEngine(
    lyricsContainer,
    (word, line) => handleWordClick(word, line),
    (index, line, isLoop) => handleLineClick(index, line, isLoop)
  );

  // 學習模式模組實例化
  const learningModes = new LearningModesManager(player, lyricsEngine);

  // DOM 元素引用
  const playPauseBtn = document.getElementById("btn-play-pause");
  const playPauseIcon = document.getElementById("play-pause-icon");
  const progressBar = document.getElementById("audio-progress-bar");
  const progressFill = document.getElementById("audio-progress-fill");
  const currentTimeLabel = document.getElementById("current-time-label");
  const totalDurationLabel = document.getElementById("total-duration-label");
  const songSelectDropdown = document.getElementById("song-select-dropdown");
  const vinylRecord = document.getElementById("vinyl-record");
  const canvasSpectrum = document.getElementById("canvas-spectrum");
  const loopLineBtn = document.getElementById("btn-loop-line");
  const speedSlider = document.getElementById("speed-slider");
  const speedDisplay = document.getElementById("speed-display-badge");

  // 當前聚焦單句卡片
  const focusedLineCard = document.getElementById("focused-line-card");
  const focusedEn = document.getElementById("focused-en");
  const focusedZh = document.getElementById("focused-zh");
  const focusedPhonetic = document.getElementById("focused-phonetic");
  const focusedNotes = document.getElementById("focused-notes");

  // 單字彈窗 DOM
  const wordModal = document.getElementById("word-modal");
  const modalWord = document.getElementById("modal-word");
  const modalPhonetic = document.getElementById("modal-phonetic");
  const modalPos = document.getElementById("modal-pos");
  const modalZh = document.getElementById("modal-zh");
  const modalDesc = document.getElementById("modal-desc");
  const btnModalSpeak = document.getElementById("btn-modal-speak");
  const btnModalSave = document.getElementById("btn-modal-save");
  const btnModalClose = document.getElementById("btn-modal-close");

  let activeWordObj = null;

  /* ══════════════════════════════════════════════════════════════
     1. 初始化歌曲與介面
     ══════════════════════════════════════════════════════════════ */
  function init() {
    renderSongDropdown();
    loadSong(currentSong);
    bindControls();
    initVisualizer();
    bindKeyboardShortcuts();
  }

  function renderSongDropdown() {
    if (!songSelectDropdown) return;
    songSelectDropdown.innerHTML = "";

    const allSongs = [...SONGS_DATA, ...customSongs];
    allSongs.forEach((song) => {
      const opt = document.createElement("option");
      opt.value = song.id;
      opt.textContent = `${song.cover || "🎵"} ${song.title} — ${song.artist} (${song.level || "推薦"})`;
      songSelectDropdown.appendChild(opt);
    });

    songSelectDropdown.value = currentSong.id;
  }

  function loadSong(song) {
    currentSong = song;
    player.pause();

    // 更新資訊
    document.getElementById("current-song-title").textContent = song.title;
    document.getElementById("current-song-artist").textContent = song.artist;
    document.getElementById("current-song-level").textContent = song.level || "綜合英語";
    document.getElementById("vinyl-cover-emoji").textContent = song.cover || "🎵";

    if (song.color) {
      document.getElementById("vinyl-center-art").style.background = song.color;
    }

    // 載入歌詞
    lyricsEngine.setLyrics(song.lyrics);

    // 載入音樂
    if (song.audioFile) {
      player.loadCustomAudio(song.audioFile);
    } else {
      player.loadSynthSong(song);
    }

    // 更新第一句到聚焦卡片
    if (song.lyrics && song.lyrics.length > 0) {
      updateFocusedCard(song.lyrics[0], 0);
    }

    // 更新各模式標籤內容
    learningModes.renderSongFlashcards(document.getElementById("flashcards-container"), currentSong);
  }

  /* ══════════════════════════════════════════════════════════════
     2. 播放器事件監聽與介面聯動
     ══════════════════════════════════════════════════════════════ */
  player.onTimeUpdate = (currentTime) => {
    lyricsEngine.updateTime(currentTime);

    // 更新進度條
    if (player.duration > 0) {
      const pct = (currentTime / player.duration) * 100;
      progressFill.style.width = `${pct}%`;
      progressBar.setAttribute("aria-valuenow", pct.toFixed(1));
    }
    currentTimeLabel.textContent = formatTime(currentTime);

    // 更新聚焦卡片
    const activeIdx = lyricsEngine.currentLineIndex;
    if (activeIdx >= 0 && currentSong.lyrics && currentSong.lyrics[activeIdx]) {
      updateFocusedCard(currentSong.lyrics[activeIdx], activeIdx);
    }
  };

  player.onPlayStateChange = (isPlaying) => {
    if (isPlaying) {
      playPauseIcon.textContent = "⏸️";
      playPauseBtn.classList.add("playing");
      vinylRecord.classList.add("rotating");
    } else {
      playPauseIcon.textContent = "▶️";
      playPauseBtn.classList.remove("playing");
      vinylRecord.classList.remove("rotating");
    }
  };

  player.onDurationChange = (duration) => {
    totalDurationLabel.textContent = formatTime(duration);
  };

  player.onRateChange = (rate) => {
    speedDisplay.textContent = `${rate.toFixed(2)}x`;
    speedSlider.value = rate;

    // 醒目標示按鈕
    document.querySelectorAll(".btn-speed-pill").forEach((btn) => {
      btn.classList.toggle("active", Math.abs(parseFloat(btn.dataset.rate) - rate) < 0.04);
    });
  };

  /* ══════════════════════════════════════════════════════════════
     3. 歌詞單詞點擊 & 單句點擊處理
     ══════════════════════════════════════════════════════════════ */
  function handleWordClick(word, line) {
    const wordData = lyricsEngine.lookupWord(word);
    if (!wordData) return;

    activeWordObj = wordData;
    modalWord.textContent = wordData.original || wordData.word;
    modalPhonetic.textContent = wordData.kk || "";
    modalPos.textContent = wordData.pos || "";
    modalZh.textContent = wordData.zh || "";
    modalDesc.textContent = wordData.desc || (line ? `歌曲出處例句：${line.en}` : "");

    wordModal.classList.add("open");

    // 自動輕聲發音一次
    lyricsEngine.speakText(wordData.original || wordData.word, 0.9);
  }

  function handleLineClick(index, line, isLoopToggle) {
    if (isLoopToggle) {
      // 切換單句循環
      if (player.loopCurrentLine && player.currentLineRange && player.currentLineRange.start === line.start) {
        player.setLoopMode(false);
        player.clearLoopRange();
        loopLineBtn.classList.remove("active");
        showToast("已關閉單句循環模式");
      } else {
        player.setLoopMode(true);
        player.setLoopRange(line.start, line.end);
        loopLineBtn.classList.add("active");
        player.seek(line.start);
        player.play();
        showToast(`已啟用第 ${index + 1} 句循環播放 🔂`);
      }
    } else {
      player.seek(line.start);
      player.play();
    }
    updateFocusedCard(line, index);
  }

  function updateFocusedCard(line, index) {
    if (!line) return;
    focusedEn.innerHTML = lyricsEngine._tokenizeEnglishText(line.en, line.keyWords);
    focusedZh.textContent = line.zh || "";
    focusedPhonetic.textContent = line.phonetic ? `/${line.phonetic}/` : "";
    focusedNotes.textContent = line.notes || "";
    focusedLineCard.dataset.lineIndex = index;
  }

  // 點擊聚焦卡片中的單字亦可查字典
  focusedEn?.addEventListener("click", (e) => {
    if (e.target.classList.contains("word-token")) {
      const activeIdx = lyricsEngine.currentLineIndex >= 0 ? lyricsEngine.currentLineIndex : 0;
      const line = currentSong.lyrics[activeIdx];
      handleWordClick(e.target.dataset.word, line);
    }
  });

  /* ══════════════════════════════════════════════════════════════
     4. 綁定按鈕與控制項
     ══════════════════════════════════════════════════════════════ */
  function bindControls() {
    // 播放/暫停
    playPauseBtn.addEventListener("click", () => {
      player.togglePlay();
    });

    // 快轉 / 倒帶 5 秒
    document.getElementById("btn-rewind-5")?.addEventListener("click", () => {
      player.seekRelative(-5);
    });

    document.getElementById("btn-forward-5")?.addEventListener("click", () => {
      player.seekRelative(5);
    });

    // 上一句 / 下一句
    document.getElementById("btn-prev-line")?.addEventListener("click", () => {
      jumpToLine(lyricsEngine.currentLineIndex - 1);
    });

    document.getElementById("btn-next-line")?.addEventListener("click", () => {
      jumpToLine(lyricsEngine.currentLineIndex + 1);
    });

    // 單句循環按鈕
    loopLineBtn?.addEventListener("click", () => {
      const activeIdx = lyricsEngine.currentLineIndex >= 0 ? lyricsEngine.currentLineIndex : 0;
      const line = currentSong.lyrics[activeIdx];
      if (line) {
        handleLineClick(activeIdx, line, true);
      }
    });

    // 速度膠囊按鈕
    document.querySelectorAll(".btn-speed-pill").forEach((btn) => {
      btn.addEventListener("click", () => {
        const rate = parseFloat(btn.dataset.rate);
        player.setRate(rate);
      });
    });

    // 速度滑動條
    speedSlider?.addEventListener("input", (e) => {
      player.setRate(e.target.value);
    });

    // 進度條拖曳 / 點擊跳轉
    progressBar?.addEventListener("click", (e) => {
      const rect = progressBar.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const ratio = Math.max(0, Math.min(1, clickX / rect.width));
      player.seek(ratio * player.duration);
    });

    // 歌曲下拉選單切換
    songSelectDropdown?.addEventListener("change", (e) => {
      const allSongs = [...SONGS_DATA, ...customSongs];
      const target = allSongs.find((s) => s.id === e.target.value);
      if (target) {
        loadSong(target);
      }
    });

    // 雙語 / 純英文模式切換
    document.querySelectorAll(".btn-view-mode").forEach((btn) => {
      btn.addEventListener("click", (e) => {
        document.querySelectorAll(".btn-view-mode").forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        lyricsEngine.setDisplayMode(btn.dataset.mode);
      });
    });

    // 音標顯示切換
    const togglePhoneticsCheckbox = document.getElementById("toggle-phonetics");
    togglePhoneticsCheckbox?.addEventListener("change", (e) => {
      lyricsEngine.togglePhonetics(e.target.checked);
    });

    // 自動滾動切換
    const toggleAutoScrollCheckbox = document.getElementById("toggle-autoscroll");
    toggleAutoScrollCheckbox?.addEventListener("change", (e) => {
      lyricsEngine.toggleAutoScroll(e.target.checked);
    });

    // 聚焦卡片操作按鈕
    document.getElementById("btn-focus-speak")?.addEventListener("click", () => {
      const activeIdx = lyricsEngine.currentLineIndex >= 0 ? lyricsEngine.currentLineIndex : 0;
      const line = currentSong.lyrics[activeIdx];
      if (line) lyricsEngine.speakText(line.en, 0.85);
    });

    document.getElementById("btn-focus-loop")?.addEventListener("click", () => {
      const activeIdx = lyricsEngine.currentLineIndex >= 0 ? lyricsEngine.currentLineIndex : 0;
      const line = currentSong.lyrics[activeIdx];
      if (line) handleLineClick(activeIdx, line, true);
    });

    document.getElementById("btn-focus-shadow")?.addEventListener("click", () => {
      const activeIdx = lyricsEngine.currentLineIndex >= 0 ? lyricsEngine.currentLineIndex : 0;
      const line = currentSong.lyrics[activeIdx];
      const tabShadow = document.querySelector('[data-tab="shadowing"]');
      if (tabShadow) tabShadow.click();
      learningModes.renderShadowingStudio(document.getElementById("shadowing-container"), currentSong, line);
    });

    // 單字彈窗按鈕
    btnModalSpeak?.addEventListener("click", () => {
      if (activeWordObj) {
        lyricsEngine.speakText(activeWordObj.original || activeWordObj.word, 0.9);
      }
    });

    btnModalSave?.addEventListener("click", () => {
      if (activeWordObj) {
        const added = lyricsEngine.saveWordToBook(activeWordObj);
        showToast(added ? `已收藏「${activeWordObj.word}」至生字本 ⭐` : `「${activeWordObj.word}」已在生字本中。`);
        wordModal.classList.remove("open");
      }
    });

    btnModalClose?.addEventListener("click", () => {
      wordModal.classList.remove("open");
    });

    wordModal?.addEventListener("click", (e) => {
      if (e.target === wordModal) {
        wordModal.classList.remove("open");
      }
    });

    // 標籤頁 (Tabs) 切換
    document.querySelectorAll(".tab-nav-btn").forEach((tabBtn) => {
      tabBtn.addEventListener("click", () => {
        document.querySelectorAll(".tab-nav-btn").forEach((b) => b.classList.remove("active"));
        document.querySelectorAll(".tab-content-panel").forEach((p) => p.classList.remove("active"));

        tabBtn.classList.add("active");
        const panelId = `panel-${tabBtn.dataset.tab}`;
        const panel = document.getElementById(panelId);
        if (panel) panel.classList.add("active");

        // 依據標籤初始化內容
        const tab = tabBtn.dataset.tab;
        if (tab === "cloze") {
          learningModes.startClozeTest(document.getElementById("cloze-container"), currentSong);
        } else if (tab === "shadowing") {
          const activeIdx = lyricsEngine.currentLineIndex >= 0 ? lyricsEngine.currentLineIndex : 0;
          learningModes.renderShadowingStudio(
            document.getElementById("shadowing-container"),
            currentSong,
            currentSong.lyrics[activeIdx] || currentSong.lyrics[0]
          );
        } else if (tab === "flashcards") {
          learningModes.renderSongFlashcards(document.getElementById("flashcards-container"), currentSong);
        } else if (tab === "wordbook") {
          learningModes.renderWordbookList(document.getElementById("wordbook-container"));
        }
      });
    });

    // 匯入自訂歌曲功能
    bindCustomImporter();
  }

  function jumpToLine(targetIndex) {
    if (!currentSong.lyrics || currentSong.lyrics.length === 0) return;
    const clampedIndex = Math.max(0, Math.min(targetIndex, currentSong.lyrics.length - 1));
    const targetLine = currentSong.lyrics[clampedIndex];
    if (targetLine) {
      player.seek(targetLine.start);
      player.play();
    }
  }

  /* ══════════════════════════════════════════════════════════════
     5. 自訂歌曲與 LRC 匯入器
     ══════════════════════════════════════════════════════════════ */
  function bindCustomImporter() {
    const btnParseImport = document.getElementById("btn-parse-import");
    const inputSongTitle = document.getElementById("import-song-title");
    const inputSongArtist = document.getElementById("import-song-artist");
    const inputAudioFile = document.getElementById("import-audio-file");
    const textareaLrc = document.getElementById("import-lrc-text");

    btnParseImport?.addEventListener("click", () => {
      const title = inputSongTitle.value.trim() || "自訂英文歌";
      const artist = inputSongArtist.value.trim() || "自訂歌手";
      const lrcContent = textareaLrc.value.trim();

      if (!lrcContent) {
        alert("請貼上包含時間戳記的 LRC 歌詞，或點選下方範例貼上！");
        return;
      }

      const parsedLyrics = LyricsEngine.parseLRC(lrcContent);
      if (parsedLyrics.length === 0) {
        alert("無法解析歌詞中的時間戳記，請確保格式為 [00:12.34] 歌詞內容。");
        return;
      }

      const newSong = {
        id: `custom-${Date.now()}`,
        title: title,
        artist: artist,
        genre: "自訂匯入",
        level: "自訂練習",
        cover: "🎧",
        color: "linear-gradient(135deg, #059669, #10b981)",
        audioNotes: "使用者自訂歌曲",
        synthPattern: "acoustic-guitar-ballad",
        bpm: 90,
        lyrics: parsedLyrics,
        audioFile: inputAudioFile.files && inputAudioFile.files[0] ? inputAudioFile.files[0] : null
      };

      customSongs.push(newSong);
      renderSongDropdown();
      songSelectDropdown.value = newSong.id;
      loadSong(newSong);

      showToast(`成功匯入「${title}」，包含 ${parsedLyrics.length} 句歌詞！🎉`);

      // 切換回歌詞分頁
      const tabLyrics = document.querySelector('[data-tab="lyrics"]');
      if (tabLyrics) tabLyrics.click();
    });

    // 快速範例貼上
    document.getElementById("btn-import-sample")?.addEventListener("click", () => {
      textareaLrc.value = `[00:01.00] Yesterday, all my troubles seemed so far away | 昨天，所有的煩惱憂愁似乎都那麼遙遠
[00:08.50] Now it looks as though they're here to stay | 但如今，它們彷彿駐足在此不再離去
[00:15.00] Oh, I believe in yesterday | 噢，我多麼眷戀懷念昨天
[00:22.00] Suddenly, I'm not half the man I used to be | 突然間，我已不再是當初那個完整的自己
[00:29.00] There's a shadow hanging over me | 陰鬱的陰影悄然籠罩著我的心頭
[00:36.00] Oh, yesterday came suddenly | 噢，昨天的一切消逝得如此猝不及防`;
      inputSongTitle.value = "Yesterday";
      inputSongArtist.value = "The Beatles";
    });
  }

  /* ══════════════════════════════════════════════════════════════
     6. 音訊視覺化畫布 (Audio Visualizer Canvas)
     ══════════════════════════════════════════════════════════════ */
  function initVisualizer() {
    if (!canvasSpectrum) return;
    const ctx = canvasSpectrum.getContext("2d");

    function renderFrame() {
      requestAnimationFrame(renderFrame);

      const width = canvasSpectrum.width;
      const height = canvasSpectrum.height;
      ctx.clearRect(0, 0, width, height);

      const freqData = player.getFrequencyData();
      const barCount = 32;
      const barWidth = (width / barCount) * 0.7;
      const gap = (width / barCount) * 0.3;

      for (let i = 0; i < barCount; i++) {
        const val = player.isPlaying ? freqData[i * 2] || 15 : 8;
        const barHeight = Math.max(3, (val / 255) * (height - 6));

        // 漸層色彩 (琥珀金色至霓虹藍紫)
        const gradient = ctx.createLinearGradient(0, height, 0, 0);
        gradient.addColorStop(0, "rgba(245, 158, 11, 0.4)");
        gradient.addColorStop(0.7, "rgba(236, 72, 153, 0.8)");
        gradient.addColorStop(1, "rgba(99, 102, 241, 1)");

        ctx.fillStyle = gradient;
        ctx.beginPath();
        ctx.roundRect(i * (barWidth + gap), height - barHeight, barWidth, barHeight, 3);
        ctx.fill();
      }
    }

    renderFrame();
  }

  /* ══════════════════════════════════════════════════════════════
     7. 鍵盤快捷鍵支援
     ══════════════════════════════════════════════════════════════ */
  function bindKeyboardShortcuts() {
    window.addEventListener("keydown", (e) => {
      // 避免在輸入框打字時誤觸
      if (["INPUT", "TEXTAREA"].includes(document.activeElement.tagName)) return;

      if (e.code === "Space") {
        e.preventDefault();
        player.togglePlay();
      } else if (e.code === "ArrowLeft") {
        e.preventDefault();
        player.seekRelative(-5);
      } else if (e.code === "ArrowRight") {
        e.preventDefault();
        player.seekRelative(5);
      } else if (e.code === "ArrowUp") {
        e.preventDefault();
        player.setRate(Math.min(2.0, player.playbackRate + 0.1));
      } else if (e.code === "ArrowDown") {
        e.preventDefault();
        player.setRate(Math.max(0.5, player.playbackRate - 0.1));
      } else if (e.key === "[") {
        jumpToLine(lyricsEngine.currentLineIndex - 1);
      } else if (e.key === "]") {
        jumpToLine(lyricsEngine.currentLineIndex + 1);
      } else if (e.key === "l" || e.key === "L") {
        loopLineBtn?.click();
      }
    });
  }

  /* ══════════════════════════════════════════════════════════════
     工具函數
     ══════════════════════════════════════════════════════════════ */
  function formatTime(seconds) {
    const s = Math.max(0, Math.floor(seconds || 0));
    const mins = Math.floor(s / 60);
    const secs = s % 60;
    return `${mins}:${secs < 10 ? "0" : ""}${secs}`;
  }

  function showToast(msg) {
    let toast = document.getElementById("app-toast");
    if (!toast) {
      toast = document.createElement("div");
      toast.id = "app-toast";
      toast.className = "app-toast";
      document.body.appendChild(toast);
    }
    toast.textContent = msg;
    toast.classList.add("visible");
    setTimeout(() => {
      toast.classList.remove("visible");
    }, 2500);
  }

  // 啟動
  init();
});
