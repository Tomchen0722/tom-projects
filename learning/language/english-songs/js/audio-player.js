/**
 * 英文歌學習系統 - 音訊與歌聲演唱播放引擎 (Audio & Vocal Singing Engine)
 * 核心特色：
 * 1. 歌聲伴唱 (Melodic Vocal Singer)：利用 Web Speech API 音樂調校技術，
 *    在和弦伴奏進行時，逐句同步唱出標準純正的英文歌聲！
 * 2. 伴奏音樂合成器 (Web Audio API Synthesizer)：原創吉他、鋼琴、貝斯與爵士和弦，離線開箱即聽。
 * 3. 變速不變調 (Pitch-Preserving Speed Adjustment)：0.5x ~ 2.0x 慢速聽發音細節、高速鍛鍊耳朵。
 * 4. A-B 單句循環 (Single Line Loop / Repeat) 專注影子聽寫。
 * 5. 即時字幕動作同步 (Karaoke Syllable & Word Motion Tracking)。
 * 6. 雙軌音量獨立調控：🎙️ 歌聲音量 + 🎹 伴奏音量。
 */

/**
 * 歌聲導唱引擎 (Vocal Singing Engine)
 */
class VocalSinger {
  constructor() {
    this.synth = window.speechSynthesis;
    this.vocalsEnabled = true;
    this.vocalVolume = 1.0;
    this.vocalPitch = 1.08; // 微微上揚的旋律感音調
    this.selectedVoice = null;
    this.currentUtterance = null;
    this.lastSungLineIndex = -1;

    this.onWordBoundary = null; // (lineIndex, charIndex, wordIndex) => {}

    this._initVoices();
    if (this.synth && this.synth.onvoiceschanged !== undefined) {
      this.synth.onvoiceschanged = () => this._initVoices();
    }
  }

  _initVoices() {
    if (!this.synth) return;
    const voices = this.synth.getVoices();
    if (!voices || voices.length === 0) return;

    // 優先挑選最自然純正的英語人聲 (Natural, Google, Samantha, Jenny, Guy)
    const preferredVoices = voices.filter(v => 
      v.lang.startsWith("en") && 
      (v.name.includes("Natural") || v.name.includes("Google") || v.name.includes("Samantha") || v.name.includes("Jenny") || v.name.includes("Guy") || v.name.includes("Online"))
    );

    if (preferredVoices.length > 0) {
      this.selectedVoice = preferredVoices[0];
    } else {
      // 備選任何英文人聲
      const anyEn = voices.find(v => v.lang.startsWith("en"));
      this.selectedVoice = anyEn || voices[0];
    }
  }

  getAvailableVoices() {
    if (!this.synth) return [];
    return this.synth.getVoices().filter(v => v.lang.startsWith("en"));
  }

  setVoice(voiceUri) {
    if (!this.synth) return;
    const voices = this.synth.getVoices();
    const found = voices.find(v => v.voiceURI === voiceUri || v.name === voiceUri);
    if (found) this.selectedVoice = found;
  }

  setVocalsEnabled(enabled) {
    this.vocalsEnabled = enabled;
    if (!enabled) {
      this.cancel();
    }
  }

  setVolume(vol) {
    this.vocalVolume = Math.max(0, Math.min(1.0, vol));
    if (this.currentUtterance) {
      this.currentUtterance.volume = this.vocalVolume;
    }
  }

  setPitch(pitch) {
    this.vocalPitch = Math.max(0.5, Math.min(2.0, pitch));
  }

  singLine(line, lineIndex, playbackRate = 1.0) {
    if (!this.synth || !this.vocalsEnabled || !line || !line.en) return;
    if (this.lastSungLineIndex === lineIndex) return;

    this.lastSungLineIndex = lineIndex;
    this.cancel();

    const cleanText = line.en.trim();
    if (!cleanText) return;

    const utterance = new SpeechSynthesisUtterance(cleanText);
    if (this.selectedVoice) {
      utterance.voice = this.selectedVoice;
    }
    utterance.lang = (this.selectedVoice && this.selectedVoice.lang) || "en-US";

    // 依據歌詞時長動態匹配語音歌唱節奏
    const durationSec = Math.max(0.8, line.end - line.start);
    const wordCount = cleanText.split(/\s+/).length;
    // 基準英文朗讀速度約 2.4 字/秒
    let targetRate = (wordCount / durationSec) / 2.2;
    // 與播放器總變速結合
    targetRate = targetRate * playbackRate;
    utterance.rate = Math.max(0.65, Math.min(1.75, targetRate));

    utterance.pitch = this.vocalPitch;
    utterance.volume = this.vocalVolume;

    // 單詞邊界即時通知（讓字幕動作與歌聲完全一致）
    utterance.onboundary = (e) => {
      if (e.name === "word" && this.onWordBoundary) {
        this.onWordBoundary(lineIndex, e.charIndex);
      }
    };

    utterance.onerror = (e) => {
      // 忽略因 cancel 引起的被動中止
      if (e.error !== "canceled" && e.error !== "interrupted") {
        console.warn("歌聲引擎輸出提示:", e.error);
      }
    };

    this.currentUtterance = utterance;
    this.synth.speak(utterance);
  }

  cancel() {
    if (this.synth) {
      this.synth.cancel();
      this.currentUtterance = null;
    }
  }

  resetSungCache() {
    this.lastSungLineIndex = -1;
    this.cancel();
  }
}

/**
 * 英文歌曲主播放器 (English Song Player)
 */
class EnglishSongPlayer {
  constructor() {
    this.audioElement = new Audio();
    this.audioElement.preservesPitch = true;
    this.audioElement.mozPreservesPitch = true;
    this.audioElement.webkitPreservesPitch = true;

    this.audioContext = null;
    this.analyser = null;
    this.sourceNode = null;
    this.synthEngine = null;

    // 歌聲導唱模組
    this.vocalSinger = new VocalSinger();

    this.isPlaying = false;
    this.playbackRate = 1.0;
    this.currentTime = 0;
    this.duration = 0;

    // 播放模式
    this.sourceType = "synth"; // "synth" | "audio-file"
    this.loopCurrentLine = false;
    this.currentLineRange = null; // { start, end, index }
    this.currentSongConfig = null;

    // 回調函數
    this.onTimeUpdate = null;
    this.onPlayStateChange = null;
    this.onRateChange = null;
    this.onDurationChange = null;
    this.onEnded = null;

    this._bindAudioEvents();
  }

  _initAudioContext() {
    if (!this.audioContext) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      this.audioContext = new AudioCtx();
      this.analyser = this.audioContext.createAnalyser();
      this.analyser.fftSize = 128;

      try {
        this.sourceNode = this.audioContext.createMediaElementSource(this.audioElement);
        this.sourceNode.connect(this.analyser);
        this.analyser.connect(this.audioContext.destination);
      } catch (e) {
        console.warn("MediaElementSource 已存在或跨域限制:", e);
      }

      this.synthEngine = new SongSynthesizer(this.audioContext, this.analyser);
    }
    if (this.audioContext.state === "suspended") {
      this.audioContext.resume();
    }
  }

  _bindAudioEvents() {
    this.audioElement.addEventListener("timeupdate", () => {
      if (this.sourceType === "audio-file") {
        this.currentTime = this.audioElement.currentTime;
        this._checkLoopBoundary();
        this._syncVocalSinging();
        if (this.onTimeUpdate) this.onTimeUpdate(this.currentTime);
      }
    });

    this.audioElement.addEventListener("play", () => {
      this.isPlaying = true;
      if (this.onPlayStateChange) this.onPlayStateChange(true);
    });

    this.audioElement.addEventListener("pause", () => {
      this.isPlaying = false;
      this.vocalSinger.cancel();
      if (this.onPlayStateChange) this.onPlayStateChange(false);
    });

    this.audioElement.addEventListener("loadedmetadata", () => {
      this.duration = this.audioElement.duration || 0;
      if (this.onDurationChange) this.onDurationChange(this.duration);
    });

    this.audioElement.addEventListener("ended", () => {
      this.isPlaying = false;
      this.vocalSinger.cancel();
      if (this.onEnded) this.onEnded();
      if (this.onPlayStateChange) this.onPlayStateChange(false);
    });
  }

  loadCustomAudio(fileOrUrl, totalDurationHint = 100) {
    this._initAudioContext();
    this.sourceType = "audio-file";
    this.vocalSinger.resetSungCache();
    if (this.synthEngine) this.synthEngine.stop();

    if (typeof fileOrUrl === "string") {
      this.audioElement.src = fileOrUrl;
    } else {
      this.audioElement.src = URL.createObjectURL(fileOrUrl);
    }
    this.audioElement.playbackRate = this.playbackRate;
    this.audioElement.load();
    this.duration = totalDurationHint;
  }

  loadSynthSong(songConfig) {
    this._initAudioContext();
    this.sourceType = "synth";
    this.currentSongConfig = songConfig;
    this.vocalSinger.resetSungCache();

    this.audioElement.pause();
    this.audioElement.src = "";

    const lastLine = songConfig.lyrics[songConfig.lyrics.length - 1];
    this.duration = lastLine ? lastLine.end + 2.0 : 60;
    this.currentTime = 0;

    if (this.synthEngine) {
      this.synthEngine.setupSong(songConfig);
      this.synthEngine.setRate(this.playbackRate);
    }

    if (this.onDurationChange) this.onDurationChange(this.duration);
    if (this.onTimeUpdate) this.onTimeUpdate(0);
  }

  play() {
    this._initAudioContext();
    this.isPlaying = true;

    if (this.sourceType === "audio-file") {
      this.audioElement.play().catch(e => console.warn("播放受瀏覽器策略限制:", e));
    } else {
      if (this.synthEngine) {
        this.synthEngine.play(this.currentTime);
        this._startSynthTimer();
      }
    }

    // 觸發歌聲同步
    this._syncVocalSinging();

    if (this.onPlayStateChange) this.onPlayStateChange(true);
  }

  pause() {
    this.isPlaying = false;
    this.vocalSinger.cancel();

    if (this.sourceType === "audio-file") {
      this.audioElement.pause();
    } else {
      if (this.synthEngine) {
        this.synthEngine.pause();
        this._stopSynthTimer();
      }
    }
    if (this.onPlayStateChange) this.onPlayStateChange(false);
  }

  togglePlay() {
    if (this.isPlaying) {
      this.pause();
    } else {
      this.play();
    }
  }

  seek(targetSeconds) {
    const clampedTime = Math.max(0, Math.min(targetSeconds, this.duration));
    this.currentTime = clampedTime;
    this.vocalSinger.resetSungCache();

    if (this.sourceType === "audio-file") {
      this.audioElement.currentTime = clampedTime;
    } else {
      if (this.synthEngine) {
        this.synthEngine.seek(clampedTime, this.isPlaying);
      }
    }

    if (this.isPlaying) {
      this._syncVocalSinging();
    }

    if (this.onTimeUpdate) this.onTimeUpdate(this.currentTime);
  }

  seekRelative(deltaSeconds) {
    this.seek(this.currentTime + deltaSeconds);
  }

  setRate(rate) {
    const safeRate = Math.min(2.0, Math.max(0.5, parseFloat(rate)));
    this.playbackRate = safeRate;

    this.audioElement.playbackRate = safeRate;
    if (this.synthEngine) {
      this.synthEngine.setRate(safeRate);
    }

    // 若正在播放，重整當前句歌聲速度
    if (this.isPlaying) {
      this.vocalSinger.cancel();
      this.vocalSinger.lastSungLineIndex = -1;
      this._syncVocalSinging();
    }

    if (this.onRateChange) this.onRateChange(safeRate);
  }

  setLoopRange(start, end, index = -1) {
    this.currentLineRange = { start, end, index };
  }

  clearLoopRange() {
    this.currentLineRange = null;
  }

  setLoopMode(enable) {
    this.loopCurrentLine = enable;
    if (!enable) {
      this.clearLoopRange();
    }
  }

  _checkLoopBoundary() {
    if (this.loopCurrentLine && this.currentLineRange) {
      if (this.currentTime >= this.currentLineRange.end) {
        this.seek(this.currentLineRange.start);
      }
    }
  }

  _syncVocalSinging() {
    if (!this.isPlaying || !this.currentSongConfig || !this.currentSongConfig.lyrics) return;

    const lyrics = this.currentSongConfig.lyrics;
    for (let i = 0; i < lyrics.length; i++) {
      const line = lyrics[i];
      // 當播放時間進入此句範圍，且在該句的前半段啟動歌唱
      if (this.currentTime >= line.start && this.currentTime < line.end) {
        this.vocalSinger.singLine(line, i, this.playbackRate);
        break;
      }
    }
  }

  _startSynthTimer() {
    this._stopSynthTimer();
    let lastStamp = performance.now();

    this._synthTimerId = requestAnimationFrame(function step(now) {
      if (!this.isPlaying || this.sourceType !== "synth") return;

      const delta = (now - lastStamp) / 1000;
      lastStamp = now;

      this.currentTime += delta * this.playbackRate;
      this._checkLoopBoundary();
      this._syncVocalSinging();

      if (this.currentTime >= this.duration) {
        this.currentTime = this.duration;
        this.pause();
        if (this.onEnded) this.onEnded();
        return;
      }

      if (this.onTimeUpdate) this.onTimeUpdate(this.currentTime);
      this._synthTimerId = requestAnimationFrame(step.bind(this));
    }.bind(this));
  }

  _stopSynthTimer() {
    if (this._synthTimerId) {
      cancelAnimationFrame(this._synthTimerId);
      this._synthTimerId = null;
    }
  }

  getFrequencyData() {
    if (!this.analyser) return new Uint8Array(64);
    const dataArray = new Uint8Array(this.analyser.frequencyBinCount);
    this.analyser.getByteFrequencyData(dataArray);
    return dataArray;
  }

  // 伴奏與歌聲音量控制介面
  setBgmVolume(val) {
    if (this.synthEngine) {
      this.synthEngine.setVolume(val);
    }
    this.audioElement.volume = Math.max(0, Math.min(1.0, val));
  }

  setVocalVolume(val) {
    this.vocalSinger.setVolume(val);
  }

  toggleVocals(enabled) {
    this.vocalSinger.setVocalsEnabled(enabled);
    if (enabled && this.isPlaying) {
      this.vocalSinger.lastSungLineIndex = -1;
      this._syncVocalSinging();
    }
  }
}

/**
 * 伴奏音樂合成器 (Web Audio API Synthesizer)
 */
class SongSynthesizer {
  constructor(audioContext, analyser) {
    this.ctx = audioContext;
    this.analyser = analyser;
    this.songConfig = null;
    this.rate = 1.0;
    this.isPlaying = false;
    this.timer = null;
    this.currentBeatIndex = 0;

    // 主音量總控
    this.masterGain = this.ctx.createGain();
    this.masterGain.gain.value = 0.40;
    this.masterGain.connect(this.analyser);
  }

  setVolume(vol) {
    if (this.masterGain) {
      this.masterGain.gain.value = Math.max(0, Math.min(1.0, vol * 0.45));
    }
  }

  setupSong(songConfig) {
    this.stop();
    this.songConfig = songConfig;
    this.bpm = songConfig.bpm || 90;
    this.pattern = songConfig.synthPattern || "acoustic-guitar-ballad";
  }

  setRate(rate) {
    this.rate = rate;
  }

  play(startTimeSec) {
    this.isPlaying = true;
    this.seek(startTimeSec, true);
  }

  pause() {
    this.isPlaying = false;
    if (this.timer) {
      clearInterval(this.timer);
      this.timer = null;
    }
  }

  stop() {
    this.pause();
    this.currentBeatIndex = 0;
  }

  seek(timeSec, shouldPlay) {
    const secondsPerBeat = (60 / (this.bpm || 90)) / this.rate;
    this.currentBeatIndex = Math.floor(timeSec / secondsPerBeat);

    if (shouldPlay) {
      if (this.timer) clearInterval(this.timer);
      const intervalMs = (secondsPerBeat * 1000) / 2; // 八分音符步進
      this.timer = setInterval(() => {
        this._tick();
      }, intervalMs);
    }
  }

  _tick() {
    if (!this.isPlaying || !this.songConfig) return;

    const chords = this._getChordProgression();
    const chordIdx = Math.floor((this.currentBeatIndex / 8) % chords.length);
    const chord = chords[chordIdx];
    const subBeat = this.currentBeatIndex % 8;

    // 播放和弦分散琶音或伴奏拍點
    this._playArpeggioNote(chord, subBeat);

    // 輕拍節奏 (鼓組/打擊)
    if (subBeat === 0 || subBeat === 4) {
      this._playSoftKick();
    } else if (subBeat === 2 || subBeat === 6) {
      this._playSoftSnare();
    }

    this.currentBeatIndex++;
  }

  _getChordProgression() {
    if (this.pattern === "disney-orchestral-ballad") {
      return [
        { root: 293.66, notes: [293.66, 369.99, 440.00, 587.33] }, // D
        { root: 196.00, notes: [196.00, 246.94, 293.66, 392.00] }, // G
        { root: 220.00, notes: [220.00, 277.18, 329.63, 440.00] }, // A
        { root: 246.94, notes: [246.94, 293.66, 369.99, 493.88] }, // Bm
        { root: 196.00, notes: [196.00, 246.94, 293.66, 392.00] }, // G
        { root: 220.00, notes: [220.00, 277.18, 329.63, 440.00] }, // A
        { root: 293.66, notes: [293.66, 369.99, 440.00, 587.33] }, // D
        { root: 220.00, notes: [220.00, 277.18, 329.63, 440.00] }  // A
      ];
    } else if (this.pattern === "motown-bass-groove") {
      return [
        { root: 110.00, notes: [220.00, 277.18, 329.63, 440.00] }, // A
        { root: 110.00, notes: [220.00, 277.18, 329.63, 440.00] },
        { root: 92.50,  notes: [185.00, 220.00, 277.18, 369.99] }, // F#m
        { root: 92.50,  notes: [185.00, 220.00, 277.18, 369.99] },
        { root: 146.83, notes: [146.83, 220.00, 293.66, 369.99] }, // D
        { root: 164.81, notes: [164.81, 207.65, 246.94, 329.63] }, // E
        { root: 110.00, notes: [220.00, 277.18, 329.63, 440.00] }, // A
        { root: 164.81, notes: [164.81, 207.65, 246.94, 329.63] }  // E
      ];
    } else if (this.pattern === "jazz-swing-piano") {
      return [
        { root: 110.00, notes: [220.00, 261.63, 329.63, 392.00] }, // Am7
        { root: 146.83, notes: [293.66, 349.23, 440.00, 523.25] }, // Dm7
        { root: 98.00,  notes: [196.00, 246.94, 293.66, 349.23] }, // G7
        { root: 130.81, notes: [261.63, 329.63, 392.00, 493.88] }, // Cmaj7
        { root: 87.31,  notes: [174.61, 220.00, 261.63, 329.63] }, // Fmaj7
        { root: 123.47, notes: [246.94, 293.66, 349.23, 440.00] }, // Bm7b5
        { root: 82.41,  notes: [164.81, 207.65, 246.94, 329.63] }, // E7
        { root: 110.00, notes: [220.00, 261.63, 329.63, 392.00] }  // Am
      ];
    } else {
      return [
        { root: 130.81, notes: [261.63, 329.63, 392.00, 523.25] }, // C
        { root: 164.81, notes: [164.81, 196.00, 246.94, 329.63] }, // Em
        { root: 174.61, notes: [174.61, 220.00, 261.63, 349.23] }, // F
        { root: 196.00, notes: [196.00, 246.94, 293.66, 392.00] }, // G
        { root: 220.00, notes: [220.00, 261.63, 329.63, 440.00] }, // Am
        { root: 174.61, notes: [174.61, 220.00, 261.63, 349.23] }, // F
        { root: 196.00, notes: [196.00, 246.94, 293.66, 392.00] }, // G
        { root: 130.81, notes: [261.63, 329.63, 392.00, 523.25] }  // C
      ];
    }
  }

  _playArpeggioNote(chord, subBeat) {
    const t = this.ctx.currentTime;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    const filter = this.ctx.createBiquadFilter();

    let freq;
    if (subBeat === 0) {
      freq = chord.root;
      osc.type = "triangle";
      gain.gain.setValueAtTime(0.55, t);
      gain.gain.exponentialRampToValueAtTime(0.001, t + 0.9);
    } else {
      const noteIdx = (subBeat - 1) % chord.notes.length;
      freq = chord.notes[noteIdx];
      osc.type = "sine";
      gain.gain.setValueAtTime(0.28, t);
      gain.gain.exponentialRampToValueAtTime(0.001, t + 0.6);
    }

    osc.frequency.setValueAtTime(freq, t);
    filter.type = "lowpass";
    filter.frequency.setValueAtTime(1400, t);

    osc.connect(filter);
    filter.connect(gain);
    gain.connect(this.masterGain);

    osc.start(t);
    osc.stop(t + 1.0);
  }

  _playSoftKick() {
    const t = this.ctx.currentTime;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();

    osc.type = "sine";
    osc.frequency.setValueAtTime(110, t);
    osc.frequency.exponentialRampToValueAtTime(35, t + 0.12);

    gain.gain.setValueAtTime(0.35, t);
    gain.gain.exponentialRampToValueAtTime(0.001, t + 0.15);

    osc.connect(gain);
    gain.connect(this.masterGain);

    osc.start(t);
    osc.stop(t + 0.16);
  }

  _playSoftSnare() {
    const t = this.ctx.currentTime;
    const bufferSize = this.ctx.sampleRate * 0.08;
    const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
    const data = buffer.getChannelData(0);
    for (let i = 0; i < bufferSize; i++) {
      data[i] = (Math.random() * 2 - 1) * 0.15;
    }

    const noise = this.ctx.createBufferSource();
    noise.buffer = buffer;

    const filter = this.ctx.createBiquadFilter();
    filter.type = "bandpass";
    filter.frequency.setValueAtTime(1800, t);

    const gain = this.ctx.createGain();
    gain.gain.setValueAtTime(0.25, t);
    gain.gain.exponentialRampToValueAtTime(0.001, t + 0.08);

    noise.connect(filter);
    filter.connect(gain);
    gain.connect(this.masterGain);

    noise.start(t);
  }
}
