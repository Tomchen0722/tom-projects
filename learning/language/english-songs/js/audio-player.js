/**
 * 英文歌學習系統 - 音訊播放引擎 (Audio Engine)
 * 支援：
 * 1. 本地/自選音訊 (HTML5 Audio)，具備變速不變調 (preservesPitch)、微秒級精確跳轉
 * 2. 內建 Web Audio 和弦伴奏合成器 (零外部依賴，離線/開箱即享高品質原創伴奏音樂)
 * 3. A-B 單句循環 (Single Line Loop / Repeat) 專注聽寫訓練
 * 4. 0.5x ~ 2.0x 任意速度調整 (慢速聽細節、常速磨耳朵)
 * 5. Web Audio 頻譜分析儀 (動態 Canvas 視覺化波形)
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

    this.isPlaying = false;
    this.playbackRate = 1.0;
    this.currentTime = 0;
    this.duration = 0;

    // 播放模式
    this.sourceType = "synth"; // "synth" | "audio-file"
    this.loopCurrentLine = false;
    this.currentLineRange = null; // { start, end }

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
        if (this.onTimeUpdate) this.onTimeUpdate(this.currentTime);
      }
    });

    this.audioElement.addEventListener("play", () => {
      this.isPlaying = true;
      if (this.onPlayStateChange) this.onPlayStateChange(true);
    });

    this.audioElement.addEventListener("pause", () => {
      this.isPlaying = false;
      if (this.onPlayStateChange) this.onPlayStateChange(false);
    });

    this.audioElement.addEventListener("loadedmetadata", () => {
      this.duration = this.audioElement.duration || 0;
      if (this.onDurationChange) this.onDurationChange(this.duration);
    });

    this.audioElement.addEventListener("ended", () => {
      this.isPlaying = false;
      if (this.onEnded) this.onEnded();
      if (this.onPlayStateChange) this.onPlayStateChange(false);
    });
  }

  loadCustomAudio(fileOrUrl, totalDurationHint = 100) {
    this._initAudioContext();
    this.sourceType = "audio-file";
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
    if (this.onPlayStateChange) this.onPlayStateChange(true);
  }

  pause() {
    this.isPlaying = false;
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

    if (this.sourceType === "audio-file") {
      this.audioElement.currentTime = clampedTime;
    } else {
      if (this.synthEngine) {
        this.synthEngine.seek(clampedTime, this.isPlaying);
      }
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

    if (this.onRateChange) this.onRateChange(safeRate);
  }

  setLoopRange(start, end) {
    this.currentLineRange = { start, end };
  }

  clearLoopRange() {
    this.currentLineRange = null;
  }

  setLoopMode(enable) {
    this.loopCurrentLine = enable;
  }

  _checkLoopBoundary() {
    if (this.loopCurrentLine && this.currentLineRange) {
      if (this.currentTime >= this.currentLineRange.end) {
        this.seek(this.currentLineRange.start);
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
}

/**
 * 伴奏音樂合成器 (Web Audio API Synthesizer)
 * 利用振盪器 (Oscillator)、濾波器 (BiquadFilter)、增益節點 (GainNode)
 * 在純前端即時生成悅耳的吉他琶音、溫暖鋼琴和弦、貝斯與輕快節奏
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
    this.masterGain.gain.value = 0.45;
    this.masterGain.connect(this.analyser);
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
    // 依據歌曲風格提供動聽的和弦級數
    if (this.pattern === "disney-orchestral-ballad") {
      // D - G - A - Bm - G - A - D (經典迪士尼神級和弦)
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
      // A - F#m - D - E (Stand By Me 經典五零年代摩城名曲輪迴)
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
      // Am7 - Dm7 - G7 - Cmaj7 - Fmaj7 - Bm7b5 - E7 - Am7 (Fly Me to the Moon 經典爵士循環)
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
      // 預設陽光木吉他輪迴 C - Em - F - G (Count On Me / Sunshine / Country Roads)
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

    // 依據子拍挑選音符打造溫柔琶音
    let freq;
    if (subBeat === 0) {
      freq = chord.root; // 根音 Bass
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
    // 白色噪音模擬柔和沙鈴/小鼓
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
