/**
 * 字根字首魔法學院 (EtymoRoots Master)
 * TTS 語音發音與有聲播放控制器 (Web Speech API Engine)
 */

class EtymoTTS {
  constructor() {
    this.synth = window.speechSynthesis || null;
    this.rate = 0.9; // 預設自然稍慢發音，利於單字與音標辨識
    this.pitch = 1.0;
    this.selectedVoice = null;
    this.currentUtterance = null;
    this.isPlaying = false;
    this.activeButton = null;
    this.onSentenceHighlight = null; // 篇章朗讀句子回呼

    this.initVoices();
  }

  initVoices() {
    if (!this.synth) return;

    const loadVoices = () => {
      const voices = this.synth.getVoices();
      if (!voices || voices.length === 0) return;

      // 優先挑選自然優質的美式英語或英式英語聲音
      const preferredVoices = [
        "Google US English",
        "Microsoft Jenny Online (Natural) - English (United States)",
        "Microsoft Aria Online (Natural) - English (United States)",
        "Microsoft Guy Online (Natural) - English (United States)",
        "Microsoft Zira - English (United States)",
        "Samantha",
        "Daniel",
        "Alex"
      ];

      for (const name of preferredVoices) {
        const found = voices.find(v => v.name.includes(name));
        if (found) {
          this.selectedVoice = found;
          break;
        }
      }

      if (!this.selectedVoice) {
        // Fallback: 任何 en-US 或 en 語音
        this.selectedVoice = voices.find(v => v.lang === "en-US") ||
                             voices.find(v => v.lang.startsWith("en")) ||
                             voices[0];
      }
    };

    loadVoices();
    if (this.synth.onvoiceschanged !== undefined) {
      this.synth.onvoiceschanged = loadVoices;
    }
  }

  setRate(rate) {
    this.rate = Math.max(0.5, Math.min(2.0, parseFloat(rate)));
  }

  stop() {
    if (this.synth) {
      this.synth.cancel();
    }
    this.isPlaying = false;
    if (this.activeButton) {
      this.activeButton.classList.remove("speaking");
      this.activeButton = null;
    }
  }

  /**
   * 朗讀單一詞彙或句子
   * @param {string} text 要朗讀的英文文字
   * @param {HTMLElement|null} triggerButton 觸發按鈕，用於波形動畫狀態切換
   * @param {Function|null} onEndCallback 完成時的回呼
   */
  speak(text, triggerButton = null, onEndCallback = null) {
    if (!this.synth) {
      alert("您的瀏覽器暫不支援 Web Speech API 語音發音。請使用 Chrome / Edge / Safari 瀏覽體驗。");
      return;
    }

    if (!text || text.trim() === "") return;

    // 清空現有發音
    this.stop();

    const cleanText = text.replace(/\[.*?\]|\/.*?\/|\(.*?\)/g, "").trim();
    const utterance = new SpeechSynthesisUtterance(cleanText);
    utterance.lang = "en-US";
    utterance.rate = this.rate;
    utterance.pitch = this.pitch;

    if (this.selectedVoice) {
      utterance.voice = this.selectedVoice;
    }

    if (triggerButton) {
      this.activeButton = triggerButton;
      triggerButton.classList.add("speaking");
    }

    this.isPlaying = true;
    this.currentUtterance = utterance;

    utterance.onend = () => {
      this.isPlaying = false;
      if (triggerButton) {
        triggerButton.classList.remove("speaking");
      }
      this.activeButton = null;
      if (typeof onEndCallback === "function") {
        onEndCallback();
      }
    };

    utterance.onerror = (e) => {
      console.warn("TTS speak error:", e);
      this.isPlaying = false;
      if (triggerButton) {
        triggerButton.classList.remove("speaking");
      }
      this.activeButton = null;
      if (typeof onEndCallback === "function") {
        onEndCallback();
      }
    };

    this.synth.speak(utterance);
  }

  /**
   * 篇章逐句有聲朗讀（具備即時句子高亮同步）
   * @param {Array<string>} sentences 英文句子陣列
   * @param {Function} onHighlightCallback (index) => void 句子高亮切換
   * @param {Function} onFinishCallback () => void 全部朗讀完畢
   */
  speakParagraph(sentences, onHighlightCallback, onFinishCallback) {
    if (!this.synth || !sentences || sentences.length === 0) return;

    this.stop();
    let currentIndex = 0;

    const playNext = () => {
      if (currentIndex >= sentences.length) {
        if (typeof onHighlightCallback === "function") onHighlightCallback(-1);
        if (typeof onFinishCallback === "function") onFinishCallback();
        return;
      }

      if (typeof onHighlightCallback === "function") {
        onHighlightCallback(currentIndex);
      }

      const sentence = sentences[currentIndex];
      currentIndex++;

      this.speak(sentence, null, () => {
        // 句與句之間保留自然微停頓 (300ms)
        setTimeout(playNext, 350);
      });
    };

    playNext();
  }
}

// 建立全域單例
window.etymoTTS = new EtymoTTS();
