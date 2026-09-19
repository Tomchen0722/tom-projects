// Web Audio API 聲音引擎 - 模擬古銅錢落地清脆聲、青銅編鐘與太極磬音
class MysticAudio {
    constructor() {
        this.ctx = null;
        this.enabled = true;
    }

    init() {
        if (!this.ctx) {
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            this.ctx = new AudioContext();
        }
        if (this.ctx.state === 'suspended') {
            this.ctx.resume();
        }
    }

    toggleSound() {
        this.enabled = !this.enabled;
        return this.enabled;
    }

    // 銅錢翻滾落地聲 (多頻率金屬碰撞微顆粒)
    playCoinDrop() {
        if (!this.enabled) return;
        this.init();
        const now = this.ctx.currentTime;
        
        // 模擬 3 枚銅錢微小時間差連續撞擊
        const delays = [0, 0.05, 0.11];
        delays.forEach((delay, idx) => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            const filter = this.ctx.createBiquadFilter();

            // 金屬高頻敲擊
            const baseFreq = 2400 + Math.random() * 800;
            osc.type = 'sine';
            osc.frequency.setValueAtTime(baseFreq, now + delay);
            osc.frequency.exponentialRampToValueAtTime(baseFreq * 0.4, now + delay + 0.18);

            filter.type = 'bandpass';
            filter.frequency.setValueAtTime(baseFreq, now + delay);
            filter.Q.setValueAtTime(12, now + delay);

            gain.gain.setValueAtTime(0, now + delay);
            gain.gain.linearRampToValueAtTime(0.18 / (idx + 1), now + delay + 0.005);
            gain.gain.exponentialRampToValueAtTime(0.0001, now + delay + 0.22);

            osc.connect(filter);
            filter.connect(gain);
            gain.connect(this.ctx.destination);

            osc.start(now + delay);
            osc.stop(now + delay + 0.25);
        });
    }

    // 太極磬音 / 銅鐘悠遠嗡鳴
    playChime(freq = 440) {
        if (!this.enabled) return;
        this.init();
        const now = this.ctx.currentTime;
        
        const osc1 = this.ctx.createOscillator();
        const osc2 = this.ctx.createOscillator();
        const gain = this.ctx.createGain();

        osc1.type = 'sine';
        osc1.frequency.setValueAtTime(freq, now);

        osc2.type = 'triangle';
        osc2.frequency.setValueAtTime(freq * 1.503, now); // 五度泛音諧振

        gain.gain.setValueAtTime(0, now);
        gain.gain.linearRampToValueAtTime(0.2, now + 0.03);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + 2.5);

        osc1.connect(gain);
        osc2.connect(gain);
        gain.connect(this.ctx.destination);

        osc1.start(now);
        osc2.start(now);
        osc1.stop(now + 2.6);
        osc2.stop(now + 2.6);
    }

    // 星辰指引輕靈音
    playStarGlitter() {
        if (!this.enabled) return;
        this.init();
        const now = this.ctx.currentTime;
        const notes = [523.25, 659.25, 783.99, 1046.50]; // C, E, G, High C
        notes.forEach((freq, idx) => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            const t = now + idx * 0.06;

            osc.type = 'sine';
            osc.frequency.setValueAtTime(freq, t);

            gain.gain.setValueAtTime(0, t);
            gain.gain.linearRampToValueAtTime(0.12, t + 0.01);
            gain.gain.exponentialRampToValueAtTime(0.001, t + 0.4);

            osc.connect(gain);
            gain.connect(this.ctx.destination);

            osc.start(t);
            osc.stop(t + 0.45);
        });
    }
}

window.mysticAudio = new MysticAudio();
