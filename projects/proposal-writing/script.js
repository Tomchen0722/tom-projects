/**
 * 企劃案撰寫指南 — 互動腳本
 * 1. 日式側邊導覽分頁切換
 * 2. 6W2H1E1R 通用企劃範本一鍵複製至剪貼簿
 * 3. 20 項黃金檢核清單互動計數與進度條
 * 4. 浮動 Toast 提示通知
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. 頁籤切換
    const navItems = document.querySelectorAll('.nav-item');
    const sections = document.querySelectorAll('.content-section');
    const contentWrapper = document.querySelector('.content-wrapper');

    navItems.forEach(item => {
        item.addEventListener('click', () => {
            navItems.forEach(nav => nav.classList.remove('active'));
            item.classList.add('active');

            sections.forEach(section => {
                section.classList.remove('active');
            });

            const targetId = item.getAttribute('data-target');
            const targetSection = document.getElementById(targetId);
            if (targetSection) {
                targetSection.classList.add('active');
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            }
        });
    });

    // 2. Toast 提示通知函數
    function showToast(message) {
        const toast = document.getElementById('zen-toast');
        if (!toast) return;
        toast.textContent = message;
        toast.classList.add('show');
        setTimeout(() => {
            toast.classList.remove('show');
        }, 2600);
    }

    // 3. 一鍵複製 6W2H1E1R 通用企劃範本
    const copyBtn = document.getElementById('copy-template-btn');
    if (copyBtn) {
        const templateMarkdown = `# 專案企劃書：[請填寫專案名稱]
**提案單位**：[您的部門/姓名]
**提案日期**：2026 年 [MM] 月 [DD] 日
**版本號**：v1.0

---

## 1. Why (為什麼要做？) - 專案背景與痛點
- **現況問題**：[簡述當前市場或組織面臨的痛點]
- **核心目標**：[本專案要達成的根本目的]
- **不做的代價**：[若維持現狀將造成的潛在損失]

## 2. What (要做什麼？) - 核心主題與交付方案
- **價值主張**：[一句話說明本方案的獨特價值]
- **服務/產品規格**：[方案細部功能與規格描述]
- **具體交付物清單**：[專案結案時提供的產出文件/系統]

## 3. Whom (對象是誰？) - 目標客群畫像
- **主要受眾 (Primary TA)**：[客群特徵、痛點與使用情境]
- **次要受眾/關係人**：[內部主管、協同夥伴、贊助商]

## 4. Where (在哪裡做？) - 執行場域與渠道
- **線上通路**：[官方網站、APP、社群矩陣、通訊軟體]
- **線下場地**：[實體門市、展覽館、戶外活動場地]

## 5. When (何時執行？) - 時程甘特圖與里程碑
- **籌備規劃期 (M1-M2)**：[前期調研、架構設計、供應商招募]
- **執行推廣期 (M3-M4)**：[正式上線、廣告投放、活動引爆]
- **驗收檢討期 (M5)**：[數據回測、結案報告、效益評估]

## 6. Who (誰來負責？) - 團隊組織與分工
- **專案總負責人 (PM)**：[姓名 / 職責]
- **核心執行團隊**：[成員名單 / 具體分工權責 RACI]
- **外部協力夥伴**：[合作廠商 / 顧問群]

## 7. How (具體怎麼做？) - 執行工法與 SOP
- **步驟一**：[標準作業細部步驟]
- **步驟二**：[品質管控與檢驗標準]
- **步驟三**：[跨部門協同與溝通機制]

## 8. How Much (預算多少？) - 經費規劃與單價分析
- **人事工時費用**：$ [金額]
- **外包與軟硬體租賃**：$ [金額]
- **行銷推廣與採購費**：$ [金額]
- **管理費與預備金 (8%)**：$ [金額]
- **預估總經費**：$ [總金額]

## 9. Effect (預期效益？) - 量化指標與投資回報
- **量化指標 (KPI)**：[營收金額、新獲客數、轉換率 CVR]
- **質化效益**：[品牌聲譽提升、客戶滿意度 NPS、組織效率]
- **預估 ROI / ROAS**：[預期投資報酬率說明]

## 10. Risk (風險應對？) - 危機管理與 Plan B
- **潛在風險 1 (如時程落後)**：[預防措施] ➔ [應變備案 Plan B]
- **潛在風險 2 (如成本超支)**：[預防措施] ➔ [應變備案 Plan B]
`;

        copyBtn.addEventListener('click', async () => {
            try {
                await navigator.clipboard.writeText(templateMarkdown);
                copyBtn.classList.add('copied');
                copyBtn.querySelector('span').textContent = '✓ 範本已成功複製至剪貼簿！';
                showToast('📋 6W2H1E1R 企劃範本已複製，可直接貼至 Word 或 Notion！');
                setTimeout(() => {
                    copyBtn.classList.remove('copied');
                    copyBtn.querySelector('span').textContent = '一鍵複製 Markdown 範本格式';
                }, 3000);
            } catch (err) {
                // 降級處理
                const textarea = document.createElement('textarea');
                textarea.value = templateMarkdown;
                document.body.appendChild(textarea);
                textarea.select();
                document.execCommand('copy');
                document.body.removeChild(textarea);
                showToast('📋 範本已複製至剪貼簿！');
            }
        });
    }

    // 4. 20 項黃金檢核清單互動
    const checkItems = document.querySelectorAll('.zen-check-item');
    const progressTitle = document.getElementById('checklist-progress-title');
    const progressBar = document.getElementById('checklist-progress-bar');

    function updateProgress() {
        const total = checkItems.length;
        const checkedCount = document.querySelectorAll('.zen-check-item.checked').length;
        const percentage = Math.round((checkedCount / total) * 100);

        if (progressTitle) {
            progressTitle.textContent = `📝 檢核完成進度：${checkedCount} / ${total} 項 (${percentage}%)`;
        }
        if (progressBar) {
            progressBar.style.width = `${percentage}%`;
            if (percentage === 100) {
                progressBar.style.background = '#C26E28'; // 金橘色達成
            } else {
                progressBar.style.background = '#556B4E'; // 抹茶綠進行中
            }
        }
    }

    checkItems.forEach(item => {
        item.addEventListener('click', () => {
            item.classList.toggle('checked');
            const box = item.querySelector('.zen-check-box');
            if (item.classList.contains('checked')) {
                box.innerHTML = '✓';
            } else {
                box.innerHTML = '';
            }
            updateProgress();
        });
    });

    // 5. 英文專有名詞標準發音播放器 (Web Speech API)
    function speakEnglish(text, element) {
        if (!('speechSynthesis' in window)) {
            showToast('⚠️ 您的瀏覽器暫不支援語音合成功能');
            return;
        }

        window.speechSynthesis.cancel(); // 停止先前的發音

        const cleanText = text.replace(/[^a-zA-Z0-9\s-]/g, ' ').replace(/\s+/g, ' ').trim();
        if (!cleanText) return;

        const utterance = new SpeechSynthesisUtterance(cleanText);
        utterance.lang = 'en-US';
        utterance.rate = 0.92;
        utterance.pitch = 1.0;

        if (element) {
            element.classList.add('playing');
            utterance.onend = () => element.classList.remove('playing');
            utterance.onerror = () => element.classList.remove('playing');
        }

        window.speechSynthesis.speak(utterance);
        showToast(`🔊 播放英文發音：「${cleanText}」`);
    }

    // 綁定所有帶有 .en-term 或 [data-speak] 的元素
    document.querySelectorAll('.en-term, [data-speak]').forEach(el => {
        el.addEventListener('click', (e) => {
            e.stopPropagation();
            const textToSpeak = el.getAttribute('data-speak') || el.textContent;
            speakEnglish(textToSpeak, el);
        });
    });
});
