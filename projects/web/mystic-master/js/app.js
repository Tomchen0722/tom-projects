// 天機玄學閣主控制器（App Controller）- 和風簡約暖色系增強版
document.addEventListener("DOMContentLoaded", () => {
    initNavigation();
    initZiWeiModule();
    initLiunianModule();
    initPhysiognomyModule();
    initIChingModule();
    initQuizModule();
    initDailyOracle();
    initAudioControls();
    initWarmZenBackground();
});

// 頂部導覽切換
function initNavigation() {
    const navButtons = document.querySelectorAll(".nav-tab-btn");
    const sections = document.querySelectorAll(".mystic-section");

    navButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            const targetId = btn.getAttribute("data-target");
            
            navButtons.forEach(b => b.classList.remove("active"));
            sections.forEach(s => s.classList.remove("active"));

            btn.classList.add("active");
            const targetSec = document.getElementById(targetId);
            if (targetSec) {
                targetSec.classList.add("active");
            }

            if (window.mysticAudio) {
                window.mysticAudio.playChime(520);
            }
        });
    });
}

// 音效控制
function initAudioControls() {
    const audioBtn = document.getElementById("audioToggleBtn");
    if (!audioBtn) return;

    audioBtn.addEventListener("click", () => {
        const isEnabled = window.mysticAudio.toggleSound();
        audioBtn.innerHTML = isEnabled 
            ? `<span class="icon">🔔</span> <span>靈音：開啟</span>` 
            : `<span class="icon">🔕</span> <span>靈音：靜音</span>`;
        audioBtn.classList.toggle("muted", !isEnabled);
    });
}

// ----------------------------------------------------
// 1. 紫微斗數模組
// ----------------------------------------------------
function initZiWeiModule() {
    render14Stars("all");
    renderPalacesOverview();

    // 星曜分類篩選按鈕
    const filterBtns = document.querySelectorAll(".star-filter-btn");
    filterBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            filterBtns.forEach(b => b.classList.remove("active"));
            btn.classList.add("active");
            const filter = btn.getAttribute("data-filter");
            render14Stars(filter);
            window.mysticAudio.playStarGlitter();
        });
    });

    // 排盤按鈕事件
    const calcBtn = document.getElementById("ziweiCalcBtn");
    if (calcBtn) {
        calcBtn.addEventListener("click", () => {
            runZiWeiCalculation();
        });
    }

    // 預設樣板快速排盤（殺破狼、機月同梁、紫府）
    const presetBtns = document.querySelectorAll(".preset-chart-btn");
    presetBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            const year = parseInt(btn.getAttribute("data-year"), 10);
            const month = parseInt(btn.getAttribute("data-month"), 10);
            const day = parseInt(btn.getAttribute("data-day"), 10);
            const hour = parseInt(btn.getAttribute("data-hour"), 10);

            document.getElementById("birthYear").value = year;
            document.getElementById("birthMonth").value = month;
            document.getElementById("birthDay").value = day;
            document.getElementById("birthHour").value = hour;

            runZiWeiCalculation();
        });
    });

    // 預設執行一次排盤以呈現畫面
    runZiWeiCalculation();
}

// 渲染十四主星卡片
function render14Stars(filter) {
    const container = document.getElementById("starsGrid");
    if (!container) return;

    container.innerHTML = "";
    const stars = window.ZiWeiSystem.stars;

    const filterGroups = {
        all: Object.keys(stars),
        emperor: ["ziwei", "tianfu", "taiyang", "taiyin"],
        combat: ["qisha", "pojun", "tanlang", "wuqu"],
        wisdom: ["tianji", "jumen", "tianliang", "tianxiang", "tiantong", "lianzhen"]
    };

    const targetKeys = filterGroups[filter] || filterGroups.all;

    targetKeys.forEach(key => {
        const s = stars[key];
        const card = document.createElement("div");
        card.className = "star-card glass-panel";
        card.innerHTML = `
            <div class="star-header">
                <div class="star-badge">${s.element}</div>
                <h4 class="star-name">${s.name}</h4>
                <span class="star-title">${s.title}</span>
            </div>
            <div class="star-archetype">${s.archetype}</div>
            <p class="star-desc">${s.desc}</p>
            <div class="hs-analogy-box">
                <strong>👑 格局風範與人物原型：</strong>
                <span>${s.proProfile || s.hsAnalogy}</span>
            </div>
            <div class="star-strengths-box">
                <strong>✨ 天賦優勢：</strong>
                <ul>${s.strengths.map(item => `<li>${item}</li>`).join("")}</ul>
            </div>
            <div class="star-study-box">
                <strong>💼 事業拓展與實戰策略：</strong>
                <p>${s.careerStrategy || s.studyGuide}</p>
            </div>
            <div class="star-mindset-box">
                <strong>🛡️ 關鍵決策與風險防禦：</strong>
                <p>${s.riskMindset || s.examMindset}</p>
            </div>
        `;
        container.appendChild(card);
    });
}

// 渲染十二宮位總覽卡
function renderPalacesOverview() {
    const container = document.getElementById("palacesOverviewGrid");
    if (!container) return;

    container.innerHTML = "";
    window.ZiWeiSystem.palaces.forEach(p => {
        const item = document.createElement("div");
        item.className = "palace-summary-card glass-panel";
        item.innerHTML = `
            <div class="p-icon">${p.icon}</div>
            <div class="p-title">${p.name}</div>
            <div class="p-category">${p.category}</div>
            <div class="p-modern">${p.modernDesc}</div>
            <div class="p-hs">${p.proExplain || p.hsExplain}</div>
        `;
        container.appendChild(item);
    });
}

// 執行排盤計算與渲染 12 宮格
function runZiWeiCalculation() {
    const year = parseInt(document.getElementById("birthYear").value, 10) || 1996;
    const month = parseInt(document.getElementById("birthMonth").value, 10) || 6;
    const day = parseInt(document.getElementById("birthDay").value, 10) || 15;
    const hour = parseInt(document.getElementById("birthHour").value, 10) || 6;
    const gender = document.getElementById("birthGender") ? document.getElementById("birthGender").value : "male";

    const result = window.ZiWeiSystem.calculateChart(year, month, day, hour, gender);
    window.currentZiWeiChart = result;

    if (window.mysticAudio) {
        window.mysticAudio.playChime(380);
    }

    renderZiWeiGrid(result);
    updateLiunianAndDecadeUI();
    renderAphorisms();
}

// 渲染紫微盤 12 宮格正統排法
function renderZiWeiGrid(result) {
    const gridContainer = document.getElementById("ziweiPanGrid");
    const centerInfo = document.getElementById("ziweiCenterCourt");
    if (!gridContainer || !centerInfo) return;

    gridContainer.innerHTML = "";

    const displayOrder = [
        5, 6, 7, 8,   // 巳 午 未 申
        4,          9,   // 辰     酉
        3,          10,  // 卯     戌
        2, 1, 0, 11   // 寅 丑 子 亥
    ];

    // 計算當前選中流年的地支
    const diZhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"];
    const yZhiIdx = (selectedLiunianYear - 4) % 12;
    const targetZhi = diZhi[yZhiIdx >= 0 ? yZhiIdx : yZhiIdx + 12];

    centerInfo.innerHTML = `
        <div class="court-seal">天機盤印</div>
        <h3>紫微正統星盤中堂</h3>
        <p class="court-meta"><strong>歲次：</strong>${result.yearGan}${result.yearZhi}年 ｜ <strong>造化：</strong>${result.gender === 'male' ? '乾造（男）' : '坤造（女）'}</p>
        <p class="court-meta"><strong>五行局：</strong>${result.bureau}（${result.isForward ? '順行' : '逆行'}大限）</p>
        <p class="court-meta"><strong>命宮坐：</strong>${result.mingZhi}宮 ｜ <strong>身宮坐：</strong>${result.shenZhi}宮（${result.shenPalaceName}）</p>
        <div class="court-tip">💡 點選任一宮位，盤面將即時高亮「三方四正」並呈現合參解析！</div>
    `;

    displayOrder.forEach(zhiIdx => {
        const cellData = result.chart.find(c => c.zhiIndex === zhiIdx);
        if (!cellData) return;

        const cell = document.createElement("div");
        cell.className = `ziwei-cell ${cellData.isMing ? 'is-ming' : ''} ${cellData.isShen ? 'is-shen' : ''}`;
        cell.setAttribute("data-zhi", cellData.zhiIndex);

        // 主星標籤（含廟旺平陷）
        const starNames = cellData.stars.map(s => {
            return `<span class="cell-star-tag">${s.name}<span class="bright-badge bright-${s.brightness}">[${s.brightness}]</span></span>`;
        }).join("");

        // 吉星與煞星標籤
        const auxNames = cellData.auxStars ? cellData.auxStars.map(a => {
            return `<span class="aux-star-tag aux-${a.type}">${a.name}</span>`;
        }).join("") : "";

        // 四化標籤
        const sihuaBadges = cellData.sihua.map(b => `<span class="sihua-badge badge-${b}">${b}</span>`).join("");

        // 是否為流年命宮
        const isLiunianMing = cellData.zhiName === targetZhi;

        cell.innerHTML = `
            <div class="cell-top-bar">
                <span class="cell-palace-name">${cellData.palaceName}</span>
                <div>
                    <span class="decade-badge">${cellData.decadeAgeRange}歲</span>
                    <span class="cell-zhi">${cellData.zhiName}</span>
                </div>
            </div>
            <div class="cell-stars">${starNames}</div>
            ${auxNames ? `<div class="cell-aux-stars">${auxNames}</div>` : ''}
            <div class="cell-sihua-row">${sihuaBadges}</div>
            ${cellData.isMing ? '<span class="marker-tag marker-ming">本命宮</span>' : ''}
            ${cellData.isShen ? '<span class="marker-tag marker-shen">身宮</span>' : ''}
            ${isLiunianMing ? `<span class="marker-tag marker-liunian">${selectedLiunianYear}流年命</span>` : ''}
        `;

        cell.addEventListener("click", () => {
            document.querySelectorAll(".ziwei-cell").forEach(c => {
                c.classList.remove("selected");
                c.classList.remove("is-sanfang-sizheng");
                const oldCorner = c.querySelector(".sanfang-corner-badge");
                if (oldCorner) oldCorner.remove();
            });
            cell.classList.add("selected");

            // 高亮三方四正會照宮位
            if (cellData.sanFangSiZhengIndices) {
                cellData.sanFangSiZhengIndices.forEach(idx => {
                    const targetCell = document.querySelector(`.ziwei-cell[data-zhi="${idx}"]`);
                    if (targetCell && idx !== cellData.zhiIndex) {
                        targetCell.classList.add("is-sanfang-sizheng");
                        let role = "會照";
                        if (idx === (cellData.zhiIndex + 6) % 12) role = "對照";
                        const corner = document.createElement("span");
                        corner.className = "sanfang-corner-badge";
                        corner.textContent = `三方・${role}`;
                        targetCell.appendChild(corner);
                    }
                });
            }

            showPalaceDetail(cellData);
            if (window.mysticAudio) window.mysticAudio.playStarGlitter();
        });

        gridContainer.appendChild(cell);
    });

    const mingCell = result.chart.find(c => c.isMing) || result.chart[0];
    showPalaceDetail(mingCell);
}

// 點擊宮位顯示正統深度詳解
function showPalaceDetail(cellData) {
    const panel = document.getElementById("palaceDetailContent");
    if (!panel) return;

    const palaceInfo = window.ZiWeiSystem.palaces.find(p => p.id === cellData.palaceId) || {
        name: cellData.palaceName,
        modernDesc: "人生關鍵維度",
        hsExplain: "反映你的相應生活領域"
    };

    // 三方四正星曜統整
    const dui = cellData.duiGong;
    const san1 = cellData.sanFang1;
    const san2 = cellData.sanFang2;

    const allAssocAux = [
        ...(cellData.auxStars || []),
        ...(dui && dui.auxStars ? dui.auxStars : []),
        ...(san1 && san1.auxStars ? san1.auxStars : []),
        ...(san2 && san2.auxStars ? san2.auxStars : [])
    ];
    const luckyStars = allAssocAux.filter(a => a.type === "lucky");
    const shaStars = allAssocAux.filter(a => a.type === "sha");

    panel.innerHTML = `
        <div class="detail-header">
            <div>
                <h3 class="detail-title">${cellData.palaceName}（${cellData.zhiName}宮）</h3>
                <span style="font-size: 12px; color: var(--ink-muted);">行運大限：【${cellData.decadeAgeRange} 歲】 ｜ 身宮坐守：${cellData.isShen ? '是（主宰後天修為）' : '否'}</span>
            </div>
            <span class="detail-tag">${palaceInfo.category || "重要領域"}</span>
        </div>

        <div class="detail-meaning">
            <strong>🎯 宮位正統意涵：</strong>${palaceInfo.modernDesc}
        </div>
        <div class="detail-hs-meaning">
            <strong>🏛️ 人生格局與實戰解讀：</strong>${palaceInfo.proExplain || palaceInfo.hsExplain}
        </div>

        <!-- 三方四正會照分析 -->
        <div class="sanfang-summary-box">
            <h4>🌐 三方四正會照合參（對宮：${dui ? dui.palaceName : '對宮'} ｜ 三合：${san1 ? san1.palaceName : ''}、${san2 ? san2.palaceName : ''}）：</h4>
            <div>
                <strong>✨ 匯合六吉星（${luckyStars.length}顆）：</strong>
                ${luckyStars.length > 0 ? luckyStars.map(l => `<span class="sanfang-pill" style="color: #166534;">${l.name}</span>`).join("") : '<span style="color: var(--ink-muted);">本宮及三方吉星平穩</span>'}
            </div>
            <div style="margin-top: 6px;">
                <strong>⚡ 匯合六煞星（${shaStars.length}顆）：</strong>
                ${shaStars.length > 0 ? shaStars.map(s => `<span class="sanfang-pill" style="color: #991b1b;">${s.name}</span>`).join("") : '<span style="color: var(--ink-muted);">無明顯刑煞沖照</span>'}
            </div>
            <div style="margin-top: 8px; color: var(--wood-warm); font-size: 12px; line-height: 1.5;">
                <strong>💡 大師合參斷語：</strong>${luckyStars.length >= 2 ? '三方吉星照會，事業拓展與重大決策如虎添翼，多結盟行業前輩與得力幹將！' : (shaStars.length >= 2 ? '煞曜臨照，乃典型「玉不琢不成器」之攻堅格局！身處逆境越挫越勇，宜以戰略定力破局突圍！' : '本宮氣象清和敦厚，穩健經營、循序漸進，水到渠成。')}
            </div>
        </div>

        ${cellData.isShen ? `
            <div class="hs-analogy-box" style="margin-bottom: 14px;">
                <strong>🥋 身宮後天立命修為：</strong>
                <span>${window.currentZiWeiChart.shenGuidance}</span>
            </div>
        ` : ''}

        <div class="detail-stars-section">
            <h4>🌟 坐守主星與廟旺度分析：</h4>
            ${cellData.stars.length > 0 ? cellData.stars.map(sItem => {
                const s = window.ZiWeiSystem.stars[sItem.key];
                return `
                    <div class="detail-star-block glass-panel">
                        <div class="ds-name">
                            <strong>${s.name}</strong>
                            <span class="bright-badge bright-${sItem.brightness}">[狀態：${sItem.brightness}・${sItem.brightness === '廟' || sItem.brightness === '旺' ? '光芒最熾' : (sItem.brightness === '平' ? '平順中和' : '考驗磨礪')}]</span>
                            <span style="font-size: 12px; color: var(--ink-muted); margin-left: 6px;">（${s.element}・${s.title}）</span>
                        </div>
                        <div class="ds-archetype">${s.archetype}</div>
                        <div class="ds-study"><strong>💼 事業經營與實戰策略：</strong>${s.careerStrategy || s.studyGuide}</div>
                        <div class="ds-mind"><strong>🛡️ 關鍵決策與風險防禦：</strong>${s.riskMindset || s.examMindset}</div>
                    </div>
                `;
            }).join("") : `<div class="detail-star-block"><p>此宮無十四正星（空宮借對宮【${dui ? dui.palaceName : '對宮'}】星曜會照），象徵在該領域適應力極強、可塑性極高，多受外部大環境與合夥人引導影響！</p></div>`}
        </div>

        ${cellData.sihua.length > 0 ? `
            <div class="detail-sihua-section" style="margin-top: 14px;">
                <h4>🔮 宮位四化引動：</h4>
                <div class="sihua-explain">本宮得生年【${cellData.sihua.join("、")}】加持，象徵您在此領域具備格外顯著的命運錨點、重大轉折與突破機遇！</div>
            </div>
        ` : ''}
    `;
}

// 渲染古傳大師賦文精粹
function renderAphorisms() {
    const container = document.getElementById("aphorismsGrid");
    if (!container) return;

    container.innerHTML = "";
    window.ZiWeiSystem.classicalAphorisms.forEach(item => {
        const card = document.createElement("div");
        card.className = "aphorism-card glass-panel";
        card.innerHTML = `
            <div class="aph-origin">${item.origin} 原文精粹</div>
            <div class="aph-quote">「${item.quote}」</div>
            <div class="aph-hs"><strong>📜 大師專業評註與實戰指引：</strong>${item.proAnnotation || item.hsTranslation}</div>
        `;
        container.appendChild(card);
    });
}

// ----------------------------------------------------
// NEW! 2. 流年精算與未來十年圖譜模組
// ----------------------------------------------------
let selectedLiunianYear = 2026;

function initLiunianModule() {
    renderLiunianYearButtons();
    updateLiunianAndDecadeUI();
}

// 生成 2024~2035 年份快速切換按鈕
function renderLiunianYearButtons() {
    const container = document.getElementById("liunianYearButtons");
    if (!container) return;

    container.innerHTML = "";
    const years = [2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035];

    years.forEach(yr => {
        const btn = document.createElement("button");
        btn.className = `liunian-year-btn ${yr === selectedLiunianYear ? 'active' : ''}`;
        btn.textContent = yr === 2026 ? `${yr}年 (今年)` : `${yr}年`;
        btn.addEventListener("click", () => {
            selectedLiunianYear = yr;
            document.querySelectorAll(".liunian-year-btn").forEach(b => b.classList.remove("active"));
            btn.classList.add("active");
            renderLiunianReport(yr);
            if (window.mysticAudio) window.mysticAudio.playStarGlitter();
        });
        container.appendChild(btn);
    });
}

function updateLiunianAndDecadeUI() {
    if (!window.currentZiWeiChart) return;
    renderLiunianReport(selectedLiunianYear);
    renderDecadeTimeline();
}

// 渲染流年報告
function renderLiunianReport(year) {
    if (!window.currentZiWeiChart) return;
    const report = window.ZiWeiSystem.calculateLiunian(window.currentZiWeiChart, year);

    // 左側概要卡
    const summaryBox = document.getElementById("liunianSummaryBox");
    if (summaryBox) {
        summaryBox.innerHTML = `
            <div class="ln-badge">歲次・${report.targetGan}${report.targetZhi}（${report.zodiac}年）</div>
            <h3 class="ln-year-title">${report.targetYear} 流年運勢</h3>
            <div class="ln-meta">實歲約 ${report.age} 歲 ｜ 流年命宮在【${report.liunianMingZhi}宮】（${report.liunianMingPalace}）</div>
            
            <div class="ln-score-circle">
                <span class="ln-score-num">${report.fortuneScore}</span>
                <span class="ln-score-label">流年運勢指數</span>
            </div>

            <div class="ln-sihua-list">
                <div style="font-weight: bold; margin-bottom: 6px; color: var(--wood-warm);">🌟 本年流年四化飛星：</div>
                <div class="ln-sihua-item">
                    <span>🌱 ${report.sihua.lu.star} 化祿</span>
                    <span style="color: var(--tea-green);">飛入【${report.sihua.lu.palace}】</span>
                </div>
                <div class="ln-sihua-item">
                    <span>🔥 ${report.sihua.quan.star} 化權</span>
                    <span style="color: #b91c1c;">飛入【${report.sihua.quan.palace}】</span>
                </div>
                <div class="ln-sihua-item">
                    <span>📖 ${report.sihua.ke.star} 化科</span>
                    <span style="color: #2563eb;">飛入【${report.sihua.ke.palace}】</span>
                </div>
                <div class="ln-sihua-item">
                    <span>❄️ ${report.sihua.ji.star} 化忌</span>
                    <span style="color: #7c3aed;">飛入【${report.sihua.ji.palace}】</span>
                </div>
            </div>
        `;
    }

    // 右側四維度指引卡
    const guidesGrid = document.getElementById("liunianGuidesGrid");
    if (guidesGrid) {
        guidesGrid.innerHTML = `
            <div class="ln-guide-card ln-gc-study glass-panel">
                <h4 class="ln-guide-title">💼 事業功名與職場進展</h4>
                <p>${report.guides.career || report.guides.study}</p>
            </div>
            <div class="ln-guide-card ln-gc-social glass-panel">
                <h4 class="ln-guide-title">💰 財帛利祿與資產運作</h4>
                <p>${report.guides.wealth || report.guides.social}</p>
            </div>
            <div class="ln-guide-card ln-gc-health glass-panel">
                <h4 class="ln-guide-title">🩺 身心調攝與自律心法</h4>
                <p>${report.guides.health}</p>
            </div>
            <div class="ln-guide-card ln-gc-mind glass-panel">
                <h4 class="ln-guide-title">🎯 年度大師戰略決策心法</h4>
                <p>${report.guides.mindset}</p>
            </div>
        `;
    }
}

// 渲染未來十年運勢時間軸（10-Year Decadal Roadmap）
function renderDecadeTimeline() {
    const container = document.getElementById("decadeTimelineContainer");
    const detailBox = document.getElementById("decadeActiveDetailBox");
    if (!container || !window.currentZiWeiChart) return;

    const decadeData = window.ZiWeiSystem.calculateDecadeFortune(window.currentZiWeiChart, 2026, 10);
    container.innerHTML = "";

    decadeData.forEach((item, idx) => {
        const card = document.createElement("div");
        card.className = `decade-card ${idx === 0 ? 'active' : ''}`;
        card.setAttribute("data-year", item.year);

        card.innerHTML = `
            <div class="dc-head">
                <span class="dc-year">${item.year}</span>
                <span class="dc-age">${item.age}歲</span>
            </div>
            <div class="dc-stage">${item.stageBadge}</div>
            <div class="dc-theme">${item.theme}</div>
            <div class="dc-desc">${item.desc}</div>
            <div class="dc-score-bar-box">
                <div class="dc-score-label">
                    <span>運勢能量</span>
                    <strong>${item.score}分</strong>
                </div>
                <div class="dc-score-bar">
                    <div class="dc-score-fill" style="width: ${item.score}%"></div>
                </div>
            </div>
        `;

        card.addEventListener("click", () => {
            document.querySelectorAll(".decade-card").forEach(c => c.classList.remove("active"));
            card.classList.add("active");
            showDecadeYearDetail(item);
            if (window.mysticAudio) window.mysticAudio.playStarGlitter();
        });

        container.appendChild(card);
    });

    // 預設展示第 1 年詳解
    showDecadeYearDetail(decadeData[0]);
}

function showDecadeYearDetail(item) {
    const detailBox = document.getElementById("decadeActiveDetailBox");
    if (!detailBox) return;

    detailBox.innerHTML = `
        <div class="dad-header">
            <div>
                <h3 class="dad-title">${item.year} 年（${item.ganZhi}年・${item.zodiac}）｜ 歲數：約 ${item.age} 歲</h3>
                <span style="color: var(--wood-warm); font-weight: bold; font-size: 14px;">${item.stageBadge} ｜ 核心主題：【${item.theme}】</span>
            </div>
            <div style="text-align: right;">
                <span style="font-size: 13px; color: var(--ink-muted);">年度運勢指數</span>
                <div style="font-size: 28px; font-weight: 800; color: var(--wood-warm);">${item.score} 分</div>
            </div>
        </div>
        <div class="dad-sihua">
            <strong>🌌 流年四化配置：</strong>${item.sihuaOverview}
        </div>
        <div class="dad-content-row">
            <div class="dad-block">
                <h4>🏛️ 事業發展與資產累積進程</h4>
                <p>${item.careerAdvice || item.studyAdvice}</p>
            </div>
            <div class="dad-block">
                <h4>💡 戰略抉擇與風險防禦指南</h4>
                <p>${item.actionTip}</p>
            </div>
        </div>
    `;
}

// ----------------------------------------------------
// 3. 相術乾坤殿（手相與面相）
// ----------------------------------------------------
function initPhysiognomyModule() {
    initPalmUploadStudio();
    initPalmistryInteractions();
    initFaceInteractions();
}

// 真人掌相照片上傳與智能辨識中心控制器
function initPalmUploadStudio() {
    const fileInput = document.getElementById("palmFileInput");
    const cameraInput = document.getElementById("palmCameraInput");
    const dropZone = document.getElementById("palmDropZone");
    const btnBrowse = document.getElementById("btnBrowsePalm");
    const btnCamera = document.getElementById("btnCameraPalm");
    const btnPaste = document.getElementById("btnPastePalm");
    const presetBtns = document.querySelectorAll(".btn-preset-palm");
    const canvas = document.getElementById("palmInteractiveCanvas");
    const scannerBar = document.getElementById("palmScannerBar");
    const reportCard = document.getElementById("palmReportCard");
    const layerBtns = document.querySelectorAll(".layer-btn");

    if (!canvas || !reportCard) return;

    let currentMode = "preset"; // "preset" or "custom"
    let currentPresetKey = "leader";
    let customImgElement = null;
    let currentAnalysis = null;
    let activeHighlight = null;
    let isCalibMode = true; // 預設開啟微調錨點，方便隨時拖曳校準
    let preferredHandSide = "auto"; // "auto", "left", "right"
    let draggingAnchor = null;

    const btnToggleCalibPins = document.getElementById("btnToggleCalibPins");
    const btnAutoSnapCreases = document.getElementById("btnAutoSnapCreases");
    const btnToggleHandSide = document.getElementById("btnToggleHandSide");
    const handSideLabel = document.getElementById("handSideLabel");

    let activeLayers = {
        all: true,
        life: false,
        head: false,
        heart: false,
        fate: false,
        sun: false,
        mounts: false,
        ages: false
    };

    function updateHandSideDisplay(isLeft) {
        if (handSideLabel) {
            handSideLabel.textContent = isLeft ? "左手（先天）" : "右手（後天）";
        }
    }

    function refreshCanvasView() {
        if (!currentAnalysis) return;
        if (currentMode === "preset") {
            window.PhysiognomySystem.palmAnalyzer.drawPresetToCanvas(currentPresetKey, canvas);
        } else if (customImgElement) {
            const ctx = canvas.getContext("2d");
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.drawImage(customImgElement, 0, 0, canvas.width, canvas.height);
        }
        window.PhysiognomySystem.palmAnalyzer.renderOverlays(canvas, currentAnalysis, activeLayers, activeHighlight, isCalibMode);
    }

    function triggerScanAnimation(callback) {
        if (scannerBar) {
            scannerBar.classList.add("scanning");
            if (window.mysticAudio) window.mysticAudio.playStarGlitter();
            setTimeout(() => {
                scannerBar.classList.remove("scanning");
                if (callback) callback();
            }, 1200);
        } else {
            if (callback) callback();
        }
    }

    function runPresetAnalysis(presetKey) {
        currentMode = "preset";
        currentPresetKey = presetKey;
        customImgElement = null;

        presetBtns.forEach(b => {
            b.classList.toggle("active", b.getAttribute("data-preset") === presetKey);
        });

        triggerScanAnimation(() => {
            window.PhysiognomySystem.palmAnalyzer.drawPresetToCanvas(presetKey, canvas);
            currentAnalysis = window.PhysiognomySystem.palmAnalyzer.analyzeImage(canvas, null, presetKey, preferredHandSide);
            updateHandSideDisplay(currentAnalysis.geometry.isLeftHand);
            refreshCanvasView();
            renderPalmReport(currentAnalysis.report);
        });
    }

    function runCustomImageAnalysis(file) {
        if (!file || !file.type.startsWith("image/")) {
            alert("請選擇有效的手掌圖片檔案（JPG/PNG/WebP）！");
            return;
        }

        const reader = new FileReader();
        reader.onload = (e) => {
            const img = new Image();
            img.onload = () => {
                currentMode = "custom";
                customImgElement = img;

                // 適配畫布尺寸（維持高解析度）
                const maxW = 540;
                const aspect = img.height / img.width;
                canvas.width = maxW;
                canvas.height = Math.round(maxW * aspect);

                presetBtns.forEach(b => b.classList.remove("active"));

                triggerScanAnimation(() => {
                    const ctx = canvas.getContext("2d");
                    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
                    currentAnalysis = window.PhysiognomySystem.palmAnalyzer.analyzeImage(canvas, img, null, preferredHandSide);
                    updateHandSideDisplay(currentAnalysis.geometry.isLeftHand);
                    refreshCanvasView();
                    renderPalmReport(currentAnalysis.report);
                });
            };
            img.src = e.target.result;
        };
        reader.readAsDataURL(file);
    }

    function renderPalmReport(rep) {
        reportCard.innerHTML = `
            <div class="pr-header">
                <div class="pr-title-group">
                    <span class="pr-badge-tier">${rep.auspiciousTier}</span>
                    <h3>${rep.title}</h3>
                    <div style="font-size: 13px; color: var(--wood-warm); font-weight: 600; margin-top: 4px;">
                        🖐️ 判定掌型：【${rep.handType}】
                    </div>
                </div>
                <div class="pr-score-box">
                    <div class="pr-score-num">${rep.score}</div>
                    <div class="pr-score-sub">相格氣運綜合指數</div>
                </div>
            </div>

            <div class="pr-summary">
                <strong>📜 大師相理總評：</strong>${rep.summary}
            </div>

            <h4 class="pr-section-title">💼 核心功名線吉凶辨析（事業線與太陽線）</h4>
            <div class="pr-detail-grid">
                <div class="pr-line-box pr-lb-career">
                    <h4 style="color: #d97706;">⚡ ${rep.careerLine.name}</h4>
                    <p><strong>起訖走向：</strong>${rep.careerLine.startPoint} ➔ ${rep.careerLine.trend}</p>
                    <p>${rep.careerLine.analysis}</p>
                    <div class="pr-ages-flow">
                        ${rep.careerLine.keyAges.map(ka => `
                            <div class="pr-age-item"><strong>${ka.age}：</strong>${ka.desc}</div>
                        `).join("")}
                    </div>
                </div>

                <div class="pr-line-box pr-lb-sun">
                    <h4 style="color: #ca8a04;">☀️ ${rep.sunLine.name}</h4>
                    <p><strong>紋理形態：</strong>${rep.sunLine.feature}</p>
                    <p>${rep.sunLine.analysis}</p>
                </div>
            </div>

            <h4 class="pr-section-title">🌿 先天三才主線深度診斷（生命・智慧・感情）</h4>
            <div class="pr-detail-grid">
                <div class="pr-line-box pr-lb-life">
                    <h4 style="color: #10b981;">🌿 ${rep.lifeLine.name}</h4>
                    <p><strong>形態辨微：</strong>${rep.lifeLine.feature}</p>
                    <p>${rep.lifeLine.analysis}</p>
                    <p style="font-size: 12px; color: #047857; background: rgba(16, 185, 129, 0.08); padding: 6px 10px; border-radius: 6px;">
                        <strong>🩺 調攝方針：</strong>${rep.lifeLine.healthTip}
                    </p>
                </div>

                <div class="pr-line-box pr-lb-head">
                    <h4 style="color: #2563eb;">🧠 ${rep.headLine.name}</h4>
                    <p><strong>形態辨微：</strong>${rep.headLine.feature}</p>
                    <p>${rep.headLine.analysis}</p>
                </div>

                <div class="pr-line-box pr-lb-heart">
                    <h4 style="color: #db2777;">❤️ ${rep.heartLine.name}</h4>
                    <p><strong>形態辨微：</strong>${rep.heartLine.feature}</p>
                    <p>${rep.heartLine.analysis}</p>
                </div>
            </div>

            <div class="pr-line-box" style="margin-bottom: 16px; border-top-color: var(--wood-warm); background: #fdfbf7;">
                <h4 style="color: var(--wood-warm);">⛰️ 八大掌丘氣場全息盤點</h4>
                <p>${rep.mountsFocus}</p>
            </div>

            <div class="pr-line-box" style="border-top-color: var(--tea-green); background: rgba(91, 112, 82, 0.06);">
                <h4 style="color: var(--tea-green);">⛩️ 大師修身立命戰略箴言</h4>
                <p>《麻衣相法》云：「有心無相，相逐心生；有相無心，相隨心滅。」掌紋本是大腦神經與生活習性在雙掌之生物微刻。吉相者當居安思危、順勢而為以建不世之功；遇考驗者則當沈澱心性、固本培元。修身正念，運隨心轉！</p>
            </div>

            <div class="pr-action-toolbar">
                <button class="btn btn-wood" id="btnPrintPalmReport"><span class="icon">🖨️</span> 列印 / 保存大師診斷書</button>
            </div>
        `;

        const printBtn = document.getElementById("btnPrintPalmReport");
        if (printBtn) {
            printBtn.addEventListener("click", () => {
                window.print();
            });
        }
    }

    // 1. 選擇照片按鈕（直接開啟檔案選擇器）
    if (btnBrowse && fileInput) {
        btnBrowse.addEventListener("click", (e) => {
            e.preventDefault();
            e.stopPropagation();
            fileInput.click();
        });
    }

    // 2. 拍照 / 開啟相機按鈕
    if (btnCamera) {
        btnCamera.addEventListener("click", (e) => {
            e.preventDefault();
            e.stopPropagation();
            if (cameraInput) {
                cameraInput.click();
            } else if (fileInput) {
                fileInput.setAttribute("capture", "environment");
                fileInput.click();
            }
        });
    }

    // 3. 剪貼簿貼上照片按鈕（直接讀取剪貼簿或提示 Ctrl+V）
    if (btnPaste) {
        btnPaste.addEventListener("click", async (e) => {
            e.preventDefault();
            e.stopPropagation();
            try {
                if (navigator.clipboard && navigator.clipboard.read) {
                    const items = await navigator.clipboard.read();
                    let foundImage = false;
                    for (const item of items) {
                        const imgType = item.types.find(t => t.startsWith("image/"));
                        if (imgType) {
                            const blob = await item.getType(imgType);
                            runCustomImageAnalysis(blob);
                            foundImage = true;
                            break;
                        }
                    }
                    if (!foundImage) {
                        alert("📋 剪貼簿內目前沒有圖片資料。\n您可以先在電腦上複製手掌照片，或直接在此頁面按下鍵盤 Ctrl + V 貼上！");
                    }
                } else {
                    alert("請直接在鍵盤上按下 Ctrl + V（或 Mac 的 ⌘ + V）即可貼上手掌截圖！");
                }
            } catch (err) {
                console.warn("Clipboard access warning:", err);
                alert("瀏覽器安全設定限制讀取剪貼簿，請直接按下鍵盤的 Ctrl + V（或 Command + V）貼上照片即可！");
            }
        });
    }

    // 4. 點擊上傳拖曳區（點擊按鈕以外的空白處）
    if (dropZone && fileInput) {
        dropZone.addEventListener("click", (e) => {
            if (e.target.closest("#dropzoneActionButtons")) return;
            fileInput.click();
        });

        dropZone.addEventListener("dragover", (e) => {
            e.preventDefault();
            e.stopPropagation();
            dropZone.classList.add("drag-over");
        });

        dropZone.addEventListener("dragleave", () => {
            dropZone.classList.remove("drag-over");
        });

        dropZone.addEventListener("drop", (e) => {
            e.preventDefault();
            e.stopPropagation();
            dropZone.classList.remove("drag-over");
            if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
                runCustomImageAnalysis(e.dataTransfer.files[0]);
            } else if (e.dataTransfer.items) {
                for (let i = 0; i < e.dataTransfer.items.length; i++) {
                    if (e.dataTransfer.items[i].kind === 'file') {
                        const file = e.dataTransfer.items[i].getAsFile();
                        if (file) {
                            runCustomImageAnalysis(file);
                            break;
                        }
                    }
                }
            }
        });
    }

    // 5. 檔案選擇器選擇後處理
    if (fileInput) {
        fileInput.addEventListener("change", (e) => {
            if (e.target.files && e.target.files.length > 0) {
                runCustomImageAnalysis(e.target.files[0]);
                fileInput.value = "";
            }
        });
    }

    if (cameraInput) {
        cameraInput.addEventListener("change", (e) => {
            if (e.target.files && e.target.files.length > 0) {
                runCustomImageAnalysis(e.target.files[0]);
                cameraInput.value = "";
            }
        });
    }

    // 6. 全域 Ctrl + V 剪貼簿貼上事件（支援任何時刻直接貼上）
    window.addEventListener("paste", (e) => {
        if (e.target.tagName === "INPUT" && (e.target.type === "text" || e.target.type === "number")) return;
        if (e.target.tagName === "TEXTAREA") return;

        if (e.clipboardData && e.clipboardData.items) {
            for (let i = 0; i < e.clipboardData.items.length; i++) {
                const item = e.clipboardData.items[i];
                if (item.type && item.type.startsWith("image/")) {
                    const file = item.getAsFile();
                    if (file) {
                        e.preventDefault();
                        // 若未在手相殿堂，自動切換至手相分頁
                        const physTab = document.querySelector('.nav-tab-btn[data-target="sec-phys"]');
                        if (physTab && !physTab.classList.contains("active")) {
                            physTab.click();
                        }
                        const palmSubBtn = document.getElementById("btnShowPalm");
                        if (palmSubBtn && !palmSubBtn.classList.contains("active")) {
                            palmSubBtn.click();
                        }
                        runCustomImageAnalysis(file);
                        const ws = document.getElementById("palmAnalysisWorkspace");
                        if (ws) ws.scrollIntoView({ behavior: "smooth" });
                        return;
                    }
                }
            }
        }
    });

    presetBtns.forEach(btn => {
        btn.addEventListener("click", (e) => {
            e.stopPropagation();
            const pKey = btn.getAttribute("data-preset");
            runPresetAnalysis(pKey);
        });
    });

    layerBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            const layer = btn.getAttribute("data-layer");
            if (layer === "all") {
                const isAllActive = !activeLayers.all;
                Object.keys(activeLayers).forEach(k => activeLayers[k] = isAllActive);
                layerBtns.forEach(b => b.classList.toggle("active", isAllActive));
            } else {
                activeLayers[layer] = !activeLayers[layer];
                btn.classList.toggle("active", activeLayers[layer]);
                activeLayers.all = Object.keys(activeLayers).filter(k => k !== "all").every(k => activeLayers[k]);
                const allBtn = document.querySelector('.layer-btn[data-layer="all"]');
                if (allBtn) allBtn.classList.toggle("active", activeLayers.all);
            }
            refreshCanvasView();
            if (window.mysticAudio) window.mysticAudio.playWoodTap();
        });
    });

    // ----------------------------------------------------
    // 掌紋微調錨點拖曳互動與校準工具列
    // ----------------------------------------------------
    if (btnToggleCalibPins) {
        btnToggleCalibPins.addEventListener("click", () => {
            isCalibMode = !isCalibMode;
            btnToggleCalibPins.classList.toggle("active", isCalibMode);
            refreshCanvasView();
            if (window.mysticAudio) window.mysticAudio.playWoodTap();
        });
    }

    if (btnAutoSnapCreases) {
        btnAutoSnapCreases.addEventListener("click", () => {
            if (currentMode === "custom" && customImgElement) {
                triggerScanAnimation(() => {
                    const ctx = canvas.getContext("2d");
                    ctx.drawImage(customImgElement, 0, 0, canvas.width, canvas.height);
                    currentAnalysis = window.PhysiognomySystem.palmAnalyzer.analyzeImage(canvas, customImgElement, null, preferredHandSide);
                    updateHandSideDisplay(currentAnalysis.geometry.isLeftHand);
                    refreshCanvasView();
                    renderPalmReport(currentAnalysis.report);
                });
            } else {
                runPresetAnalysis(currentPresetKey);
            }
        });
    }

    if (btnToggleHandSide) {
        btnToggleHandSide.addEventListener("click", () => {
            if (preferredHandSide === "left") {
                preferredHandSide = "right";
            } else if (preferredHandSide === "right") {
                preferredHandSide = "left";
            } else {
                const curIsLeft = currentAnalysis ? currentAnalysis.geometry.isLeftHand : true;
                preferredHandSide = curIsLeft ? "right" : "left";
            }
            if (currentMode === "custom" && customImgElement) {
                const ctx = canvas.getContext("2d");
                ctx.drawImage(customImgElement, 0, 0, canvas.width, canvas.height);
                currentAnalysis = window.PhysiognomySystem.palmAnalyzer.analyzeImage(canvas, customImgElement, null, preferredHandSide);
                updateHandSideDisplay(currentAnalysis.geometry.isLeftHand);
                refreshCanvasView();
                renderPalmReport(currentAnalysis.report);
            } else {
                updateHandSideDisplay(preferredHandSide === "left");
            }
            if (window.mysticAudio) window.mysticAudio.playStarGlitter();
        });
    }

    // 取得畫布實體像素座標（克服 CSS 響應式縮放）
    function getCanvasCoords(e) {
        const rect = canvas.getBoundingClientRect();
        const clientX = e.touches ? e.touches[0].clientX : e.clientX;
        const clientY = e.touches ? e.touches[0].clientY : e.clientY;
        const scaleX = canvas.width / rect.width;
        const scaleY = canvas.height / rect.height;
        return {
            x: (clientX - rect.left) * scaleX,
            y: (clientY - rect.top) * scaleY
        };
    }

    // 搜尋所有可拖曳錨點中距離最近者
    function getNearestAnchor(canvasX, canvasY, threshold = 24) {
        if (!currentAnalysis || !currentAnalysis.geometry || !currentAnalysis.geometry.lines) return null;
        const lines = currentAnalysis.geometry.lines;
        const candidates = [];

        const checkPoint = (pt, lineKey, pointKey) => {
            if (!pt) return;
            const dist = Math.hypot(pt.x - canvasX, pt.y - canvasY);
            if (dist <= threshold) {
                candidates.push({ pt, lineKey, pointKey, dist });
            }
        };

        if (lines.life) {
            checkPoint(lines.life.start, "life", "start");
            checkPoint(lines.life.cp1, "life", "cp1");
            checkPoint(lines.life.cp2, "life", "cp2");
            checkPoint(lines.life.end, "life", "end");
        }
        if (lines.head) {
            checkPoint(lines.head.start, "head", "start");
            checkPoint(lines.head.cp1, "head", "cp1");
            checkPoint(lines.head.end, "head", "end");
        }
        if (lines.heart) {
            checkPoint(lines.heart.start, "heart", "start");
            checkPoint(lines.heart.cp1, "heart", "cp1");
            checkPoint(lines.heart.end, "heart", "end");
        }
        if (lines.fate) {
            checkPoint(lines.fate.start, "fate", "start");
            checkPoint(lines.fate.cp1, "fate", "cp1");
            checkPoint(lines.fate.end, "fate", "end");
        }
        if (lines.sun) {
            checkPoint(lines.sun.start, "sun", "start");
            checkPoint(lines.sun.end, "sun", "end");
        }

        if (candidates.length === 0) return null;
        candidates.sort((a, b) => a.dist - b.dist);
        return candidates[0];
    }

    function onPointerDown(e) {
        if (!isCalibMode) return;
        const coords = getCanvasCoords(e);
        const hit = getNearestAnchor(coords.x, coords.y);
        if (hit) {
            draggingAnchor = hit;
            canvas.style.cursor = "grabbing";
            if (e.cancelable) e.preventDefault();
        }
    }

    function onPointerMove(e) {
        const coords = getCanvasCoords(e);
        if (draggingAnchor) {
            if (e.cancelable) e.preventDefault();
            draggingAnchor.pt.x = Math.round(coords.x);
            draggingAnchor.pt.y = Math.round(coords.y);
            if (draggingAnchor.lineKey === "head" && draggingAnchor.pointKey === "start") {
                if (currentAnalysis.geometry.lines.life) {
                    currentAnalysis.geometry.lines.life.start.x = draggingAnchor.pt.x;
                    currentAnalysis.geometry.lines.life.start.y = draggingAnchor.pt.y;
                }
            } else if (draggingAnchor.lineKey === "life" && draggingAnchor.pointKey === "start") {
                if (currentAnalysis.geometry.lines.head) {
                    currentAnalysis.geometry.lines.head.start.x = draggingAnchor.pt.x;
                    currentAnalysis.geometry.lines.head.start.y = draggingAnchor.pt.y;
                }
            }
            window.PhysiognomySystem.palmAnalyzer.recalculateAges(currentAnalysis.geometry.lines);
            refreshCanvasView();
        } else if (isCalibMode) {
            const hit = getNearestAnchor(coords.x, coords.y);
            canvas.style.cursor = hit ? "grab" : "crosshair";
        }
    }

    function onPointerUp() {
        if (draggingAnchor) {
            draggingAnchor = null;
            canvas.style.cursor = isCalibMode ? "grab" : "crosshair";
        }
    }

    canvas.addEventListener("mousedown", onPointerDown);
    window.addEventListener("mousemove", onPointerMove);
    window.addEventListener("mouseup", onPointerUp);

    canvas.addEventListener("touchstart", onPointerDown, { passive: false });
    window.addEventListener("touchmove", onPointerMove, { passive: false });
    window.addEventListener("touchend", onPointerUp);

    // 預設載入帝王實業型掌相範本
    runPresetAnalysis("leader");
}

function initPalmistryInteractions() {
    const linesList = window.PhysiognomySystem.palmistry.lines;
    const mountsList = window.PhysiognomySystem.palmistry.mounts;
    const handTypesList = window.PhysiognomySystem.palmistry.handTypes;

    const lineBtnContainer = document.getElementById("palmLinesButtons");
    const infoBox = document.getElementById("palmActiveDetail");
    if (lineBtnContainer) {
        lineBtnContainer.innerHTML = "";
        linesList.forEach((line, idx) => {
            const btn = document.createElement("button");
            btn.className = `btn btn-line-select ${idx === 0 ? 'active' : ''}`;
            btn.textContent = line.name.split("（")[0];
            btn.addEventListener("click", () => {
                document.querySelectorAll(".btn-line-select").forEach(b => b.classList.remove("active"));
                btn.classList.add("active");
                highlightPalmLine(line.id);
                showPalmLineDetail(line);
                window.mysticAudio.playStarGlitter();
            });
            lineBtnContainer.appendChild(btn);
        });

        showPalmLineDetail(linesList[0]);
    }

    const svgLines = document.querySelectorAll(".palm-svg-line");
    svgLines.forEach(lineElem => {
        lineElem.addEventListener("click", () => {
            const lineId = lineElem.getAttribute("data-line");
            const target = linesList.find(l => l.id === lineId);
            if (target) {
                document.querySelectorAll(".btn-line-select").forEach(b => {
                    b.classList.toggle("active", b.textContent === target.name.split("（")[0]);
                });
                highlightPalmLine(lineId);
                showPalmLineDetail(target);
                window.mysticAudio.playStarGlitter();
            }
        });
    });

    const mountsGrid = document.getElementById("mountsGrid");
    if (mountsGrid) {
        mountsGrid.innerHTML = "";
        mountsList.forEach(m => {
            const card = document.createElement("div");
            card.className = "mount-card glass-panel";
            card.innerHTML = `
                <div class="m-head">
                    <span class="m-icon">${m.icon}</span>
                    <h4 class="m-name">${m.name}</h4>
                    <span class="m-pos">（${m.pos}）</span>
                </div>
                <div class="m-meaning"><strong>能量意象：</strong>${m.meaning}</div>
                <div class="m-hs"><strong>⛰️ 大師相理辨微：</strong>${m.proGuide || m.hsGuide}</div>
            `;
            mountsGrid.appendChild(card);
        });
    }

    const handTypesGrid = document.getElementById("handTypesGrid");
    if (handTypesGrid) {
        handTypesGrid.innerHTML = "";
        handTypesList.forEach(ht => {
            const card = document.createElement("div");
            card.className = "hand-type-card glass-panel";
            card.innerHTML = `
                <h4>${ht.type}</h4>
                <p class="ht-traits"><strong>掌型外貌：</strong>${ht.traits}</p>
                <p class="ht-role"><strong>現代角色：</strong>${ht.modernRole}</p>
                <div class="ht-hs"><strong>💼 職場與實戰特質：</strong>${ht.proProfile || ht.hsProfile}</div>
            `;
            handTypesGrid.appendChild(card);
        });
    }
}

function highlightPalmLine(lineId) {
    document.querySelectorAll(".palm-svg-line").forEach(l => {
        l.classList.toggle("active-glow", l.getAttribute("data-line") === lineId);
    });
}

function showPalmLineDetail(line) {
    const infoBox = document.getElementById("palmActiveDetail");
    if (!infoBox) return;

    infoBox.innerHTML = `
        <div class="line-detail-card glass-panel" style="border-left: 4px solid ${line.color}">
            <h3 class="line-name" style="color: ${line.color}">${line.name}</h3>
            <p class="line-origin"><strong>📍 起訖位置：</strong>${line.origin}</p>
            <p class="line-classical"><strong>📜 古典正統涵義：</strong>${line.classical}</p>
            <div class="line-hs-box">
                <strong>🖐️ 專業相理解構與意象：</strong>
                <p>${line.proSignificance || line.hsAnalogy}</p>
            </div>
            <div class="line-patterns-box">
                <strong>🔍 常見形態判讀：</strong>
                <ul>
                    ${line.patterns.map(p => `<li><strong>${p.type}：</strong>${p.desc}</li>`).join("")}
                </ul>
            </div>
        </div>
    `;
}

function initFaceInteractions() {
    const zones = window.PhysiognomySystem.physiognomy.threeZones;
    const officials = window.PhysiognomySystem.physiognomy.fiveOfficials;
    const mindset = window.PhysiognomySystem.physiognomy.mindsetPrinciples[0];

    const threeZonesContainer = document.getElementById("threeZonesGrid");
    if (threeZonesContainer) {
        threeZonesContainer.innerHTML = "";
        zones.forEach(z => {
            const card = document.createElement("div");
            card.className = "three-zone-card glass-panel";
            card.innerHTML = `
                <div class="tz-head">
                    <h4>${z.name}</h4>
                    <span class="tz-age">${z.age}</span>
                </div>
                <div class="tz-concept"><strong>心智特徵：</strong>${z.concept}</div>
                <div class="tz-hs"><strong>👤 人生運勢與事業指引：</strong>${z.proGuide || z.hsGuide}</div>
                <div class="tz-tuning"><strong>🌿 調養心法：</strong>${z.tuningTip}</div>
            `;
            threeZonesContainer.appendChild(card);
        });
    }

    const officialsContainer = document.getElementById("fiveOfficialsGrid");
    if (officialsContainer) {
        officialsContainer.innerHTML = "";
        officials.forEach(o => {
            const card = document.createElement("div");
            card.className = "official-card glass-panel";
            card.innerHTML = `
                <div class="off-head">
                    <span class="off-icon">${o.icon}</span>
                    <h4>${o.name}</h4>
                    <span class="off-el">五行屬${o.element}</span>
                </div>
                <div class="off-meaning"><strong>相學司職：</strong>${o.meaning}</div>
                <div class="off-features"><strong>特征辨析：</strong>${o.features}</div>
            `;
            officialsContainer.appendChild(card);
        });
    }

    const mindsetBox = document.getElementById("mindsetScienceBox");
    if (mindsetBox && mindset) {
        mindsetBox.innerHTML = `
            <div class="mindset-card glass-panel">
                <div class="ms-quote">「${mindset.ancient}」</div>
                <div class="ms-science"><strong>🧬 現代神經認知科學解析：</strong>${mindset.modernScience}</div>
                <div class="ms-action"><strong>✨ 大師每日修持指引：</strong>${mindset.actionGuide}</div>
            </div>
        `;
    }
}

// ----------------------------------------------------
// 4. 易道變易殿（易經八卦）
// ----------------------------------------------------
let coinTossCount = 0;
let coinTossResults = [];

function initIChingModule() {
    renderBaguaWheel();
    initHexagramLookup();

    const tossBtn = document.getElementById("tossCoinsBtn");
    const resetBtn = document.getElementById("resetCoinsBtn");

    if (tossBtn) {
        tossBtn.addEventListener("click", () => {
            performCoinToss();
        });
    }

    if (resetBtn) {
        resetBtn.addEventListener("click", () => {
            resetCoinToss();
        });
    }
}

function renderBaguaWheel() {
    const container = document.getElementById("baguaTrigramsList");
    if (!container) return;

    container.innerHTML = "";
    window.IChingSystem.trigrams.forEach(t => {
        const item = document.createElement("div");
        item.className = "trigram-card glass-panel";
        item.innerHTML = `
            <div class="tri-symbol">${t.symbol}</div>
            <h4 class="tri-name">${t.name}為${t.nature}</h4>
            <div class="tri-code">二進制碼：<code>${t.code}</code></div>
            <div class="tri-virtue"><strong>卦德：</strong>${t.virtue}</div>
            <div class="tri-hs"><strong>🌀 卦德大局意涵：</strong>${t.proConcept || t.hsConcept}</div>
        `;
        container.appendChild(item);
    });
}

function performCoinToss() {
    if (coinTossCount >= 6) return;

    const tossBtn = document.getElementById("tossCoinsBtn");
    tossBtn.disabled = true;

    if (window.mysticAudio) {
        window.mysticAudio.playCoinDrop();
    }

    const coins = [document.getElementById("coin1"), document.getElementById("coin2"), document.getElementById("coin3")];
    coins.forEach(c => {
        if (c) c.classList.add("spinning");
    });

    setTimeout(() => {
        coins.forEach(c => {
            if (c) c.classList.remove("spinning");
        });

        const tossResult = window.IChingSystem.tossCoins();
        coinTossResults.push(tossResult);
        coinTossCount++;

        coins.forEach((c, idx) => {
            if (c) {
                const isYang = tossResult.coins[idx] === 3;
                c.classList.toggle("is-yang", isYang);
                c.classList.toggle("is-yin", !isYang);
                c.textContent = isYang ? "天" : "地";
            }
        });

        updateYaoHistoryUI();

        if (coinTossCount >= 6) {
            finishHexagramDivination();
            tossBtn.disabled = true;
            tossBtn.textContent = "六爻已成・點擊下方重置";
        } else {
            tossBtn.disabled = false;
            tossBtn.textContent = `繼續搖卦（第 ${coinTossCount + 1} / 6 爻）`;
        }
    }, 600);
}

function updateYaoHistoryUI() {
    const list = document.getElementById("yaoHistoryList");
    if (!list) return;

    list.innerHTML = "";
    const yaoPositions = ["初爻", "二爻", "三爻", "四爻", "五爻", "上爻"];

    for (let i = 5; i >= 0; i--) {
        const item = document.createElement("div");
        item.className = "yao-history-row";

        if (i < coinTossResults.length) {
            const data = coinTossResults[i];
            const yaoVisual = data.originalYao === 1 
                ? '<div class="yao-bar yang-bar"></div>' 
                : '<div class="yao-bar yin-bar"><span></span><span></span></div>';
            item.innerHTML = `
                <span class="yao-index">${yaoPositions[i]}</span>
                <div class="yao-visual-box">${yaoVisual}</div>
                <span class="yao-label ${data.isChanging ? 'is-changing' : ''}">${data.type}（${data.label}）</span>
            `;
        } else {
            item.innerHTML = `
                <span class="yao-index">${yaoPositions[i]}</span>
                <div class="yao-visual-box empty-yao"><div class="yao-bar placeholder-bar"></div></div>
                <span class="yao-label pending">等待起爻...</span>
            `;
        }
        list.appendChild(item);
    }
}

function finishHexagramDivination() {
    const result = window.IChingSystem.resolveHexagram(coinTossResults);
    const displayBox = document.getElementById("hexagramResultBox");
    if (!displayBox) return;

    if (window.mysticAudio) {
        window.mysticAudio.playChime(320);
    }

    displayBox.innerHTML = `
        <div class="divination-card glass-panel">
            <div class="div-top-badge">🌟 易道天機解析結果</div>
            <div class="hexagrams-comparison">
                <div class="hex-block original-hex">
                    <span class="hex-type-tag">本卦（事態現狀）</span>
                    <div class="hex-symbol">${result.originalHex.symbol}</div>
                    <h3 class="hex-title">${result.originalHex.name}</h3>
                    <p class="hex-judgement"><strong>卦辭：</strong>${result.originalHex.judgement}</p>
                    <p class="hex-image"><strong>象曰：</strong>${result.originalHex.image}</p>
                </div>
                ${result.hasChanges ? `
                    <div class="hex-transform-arrow">➡️ 變爻演進</div>
                    <div class="hex-block changed-hex">
                        <span class="hex-type-tag">變卦（未來趨勢）</span>
                        <div class="hex-symbol">${result.changedHex.symbol}</div>
                        <h3 class="hex-title">${result.changedHex.name}</h3>
                        <p class="hex-judgement"><strong>卦辭：</strong>${result.changedHex.judgement}</p>
                        <p class="hex-image"><strong>象曰：</strong>${result.changedHex.image}</p>
                    </div>
                ` : `
                    <div class="hex-block static-hex">
                        <span class="hex-type-tag">靜卦（無變爻）</span>
                        <p>六爻純粹無動爻，代表當前局勢極為穩定，堅守初心、遵循本卦指引即可大展宏圖。</p>
                    </div>
                `}
            </div>

            <div class="hex-inter-block">
                <strong>🌊 互卦暗流（發展過程中的內在機緣）：</strong>
                <span>${result.interHex.name}（${result.interHex.symbol}）——提醒你在執行過程中注意：${result.interHex.image}</span>
            </div>

            <div class="hs-strategy-grand-box">
                <h4>🏛️ 周易大師正統決策與破局指南：</h4>
                <p>${result.originalHex.proStrategy || result.originalHex.hsStrategy}</p>
                ${result.hasChanges ? `
                    <div class="future-advice">
                        <strong>🚀 轉變後的長遠啟示（變卦指引）：</strong>
                        <p>${result.changedHex.proStrategy || result.changedHex.hsStrategy}</p>
                    </div>
                ` : ''}
            </div>
        </div>
    `;
}

function resetCoinToss() {
    coinTossCount = 0;
    coinTossResults = [];
    const tossBtn = document.getElementById("tossCoinsBtn");
    if (tossBtn) {
        tossBtn.disabled = false;
        tossBtn.textContent = "開始拋擲銅錢（第 1 爻）";
    }
    updateYaoHistoryUI();
    const displayBox = document.getElementById("hexagramResultBox");
    if (displayBox) {
        displayBox.innerHTML = `<div class="empty-prompt">請點擊上方按鈕拋擲三枚銅錢，連續 6 次即可演繹出專屬的六爻卦象！</div>`;
    }
}

function initHexagramLookup() {
    const upperSelect = document.getElementById("lookupUpperTri");
    const lowerSelect = document.getElementById("lookupLowerTri");
    const resultBox = document.getElementById("lookupResultBox");
    if (!upperSelect || !lowerSelect || !resultBox) return;

    const trigrams = window.IChingSystem.trigrams;
    upperSelect.innerHTML = trigrams.map(t => `<option value="${t.code}">${t.name}（${t.nature}）</option>`).join("");
    lowerSelect.innerHTML = trigrams.map(t => `<option value="${t.code}">${t.name}（${t.nature}）</option>`).join("");

    function updateLookup() {
        const uCode = upperSelect.value;
        const lCode = lowerSelect.value;
        const fullCode = lCode + uCode;

        const hex = window.IChingSystem.hexagrams[fullCode] || window.IChingSystem.getFallbackHexagram(fullCode);
        resultBox.innerHTML = `
            <div class="lookup-card glass-panel">
                <div class="lc-top">
                    <span class="lc-sym">${hex.symbol}</span>
                    <h3 class="lc-title">${hex.name}</h3>
                </div>
                <p class="lc-judge"><strong>卦辭：</strong>${hex.judgement}</p>
                <p class="lc-image"><strong>象曰：</strong>${hex.image}</p>
                <div class="lc-strategy">
                    <strong>📜 大師戰略心法：</strong>
                    <p>${hex.proStrategy || hex.hsStrategy}</p>
                </div>
            </div>
        `;
    }

    upperSelect.addEventListener("change", updateLookup);
    lowerSelect.addEventListener("change", updateLookup);
    updateLookup();
}

// ----------------------------------------------------
// 5. 玄學大考驗與每日靈籤
// ----------------------------------------------------
let currentQuizIndex = 0;
let userScore = 0;

function initQuizModule() {
    renderQuizQuestion(0);

    const restartBtn = document.getElementById("restartQuizBtn");
    if (restartBtn) {
        restartBtn.addEventListener("click", () => {
            currentQuizIndex = 0;
            userScore = 0;
            renderQuizQuestion(0);
        });
    }
}

function renderQuizQuestion(idx) {
    const container = document.getElementById("quizContainer");
    if (!container) return;

    const questions = window.QuizSystem.questions;
    if (idx >= questions.length) {
        let rankTitle = "玄學小秀才";
        let rankBadge = "🥉";
        if (userScore >= 90) {
            rankTitle = "通天曉地・玄門通儒國師";
            rankBadge = "👑";
        } else if (userScore >= 70) {
            rankTitle = "融會貫通・天機傳人";
            rankBadge = "🥇";
        } else if (userScore >= 50) {
            rankTitle = "知書達理・易道學士";
            rankBadge = "🥈";
        }

        container.innerHTML = `
            <div class="quiz-summary-card glass-panel">
                <div class="qs-badge">${rankBadge}</div>
                <h3>玄學大師實戰考核完成！</h3>
                <div class="qs-score">${userScore} <span class="unit">分</span></div>
                <div class="qs-rank">獲得榮譽封號：<strong>【${rankTitle}】</strong></div>
                <p class="qs-words">您已經深刻掌握了紫微斗數星曜格局、相理神態氣色與周易動態決策樹的至高智慧！願這份貫通古今的洞察力，助您在事業開拓、資產運作與人生重大博弈中乘風破浪、立於不敗之地！</p>
                <button class="btn btn-gold" id="retryQuizBtn">重新挑戰考核</button>
            </div>
        `;
        document.getElementById("retryQuizBtn").addEventListener("click", () => {
            currentQuizIndex = 0;
            userScore = 0;
            renderQuizQuestion(0);
        });
        return;
    }

    const q = questions[idx];
    container.innerHTML = `
        <div class="quiz-question-card glass-panel">
            <div class="qq-progress">
                <span>第 ${idx + 1} / ${questions.length} 題</span>
                <span class="qq-cat">分類：${q.category}</span>
                <span class="qq-score-cur">當前得分：${userScore} 分</span>
            </div>
            <h3 class="qq-title">${q.question}</h3>
            <div class="qq-options">
                ${q.options.map((opt, oIdx) => `
                    <button class="quiz-option-btn" data-idx="${oIdx}">
                        <span class="opt-letter">${String.fromCharCode(65 + oIdx)}</span>
                        <span class="opt-text">${opt}</span>
                    </button>
                `).join("")}
            </div>
            <div class="qq-feedback" id="quizFeedbackBox" style="display:none;"></div>
        </div>
    `;

    const optionBtns = container.querySelectorAll(".quiz-option-btn");
    optionBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            const chosen = parseInt(btn.getAttribute("data-idx"), 10);
            const feedbackBox = document.getElementById("quizFeedbackBox");

            optionBtns.forEach(b => b.disabled = true);

            const isCorrect = chosen === q.answerIndex;
            if (isCorrect) {
                userScore += 10;
                btn.classList.add("correct");
                if (window.mysticAudio) window.mysticAudio.playStarGlitter();
            } else {
                btn.classList.add("wrong");
                optionBtns[q.answerIndex].classList.add("correct");
                if (window.mysticAudio) window.mysticAudio.playChime(260);
            }

            feedbackBox.style.display = "block";
            feedbackBox.innerHTML = `
                <div class="fb-result ${isCorrect ? 'fb-correct' : 'fb-wrong'}">
                    ${isCorrect ? '✅ 答對了！妙哉妙哉！' : '❌ 差一點點！不妨細品大師解析：'}
                </div>
                <div class="fb-explain">${q.explanation}</div>
                <button class="btn btn-mystic" id="nextQuestionBtn">下一題 ➔</button>
            `;

            document.getElementById("nextQuestionBtn").addEventListener("click", () => {
                currentQuizIndex++;
                renderQuizQuestion(currentQuizIndex);
            });
        });
    });
}

function initDailyOracle() {
    const drawBtn = document.getElementById("drawOracleBtn");
    const container = document.getElementById("oracleResultContainer");
    if (!drawBtn || !container) return;

    drawBtn.addEventListener("click", () => {
        if (window.mysticAudio) {
            window.mysticAudio.playChime(480);
        }

        drawBtn.disabled = true;
        drawBtn.textContent = "搖動籤筒・天機降臨中...";

        setTimeout(() => {
            const oracles = window.QuizSystem.dailyOracles;
            const pick = oracles[Math.floor(Math.random() * oracles.length)];

            container.innerHTML = `
                <div class="oracle-card glass-panel">
                    <div class="oc-sign">${pick.sign}</div>
                    <h3 class="oc-hex">${pick.hexagram}</h3>
                    <div class="oc-quote">「${pick.quote}」</div>
                    <div class="oc-mentor"><strong>🪷 大師指津：</strong>${pick.mentorAdvice}</div>
                    <div class="oc-action"><strong>🍀 今日開運生活微行動：</strong>${pick.luckyAction}</div>
                    <div class="oc-color"><strong>🎨 今日契合能量色：</strong>${pick.luckyColor}</div>
                </div>
            `;

            drawBtn.disabled = false;
            drawBtn.textContent = "再次抽取靈光籤";
        }, 500);
    });
}

// ----------------------------------------------------
// 6. 和風暖陽金塵浮動背景（Warm Zen Particles）
// ----------------------------------------------------
function initWarmZenBackground() {
    const canvas = document.getElementById("starfieldCanvas");
    if (!canvas) return;

    const ctx = canvas.getContext("2d");
    let width = canvas.width = window.innerWidth;
    let height = canvas.height = window.innerHeight;

    window.addEventListener("resize", () => {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    });

    const particles = [];
    const count = 50;
    for (let i = 0; i < count; i++) {
        particles.push({
            x: Math.random() * width,
            y: Math.random() * height,
            radius: Math.random() * 2.2 + 0.8,
            alpha: Math.random() * 0.45 + 0.15,
            speedY: Math.random() * 0.35 + 0.1,
            driftX: Math.random() * 0.2 - 0.1,
            colorType: Math.random() < 0.6 ? "amber" : "wood"
        });
    }

    function animate() {
        ctx.clearRect(0, 0, width, height);

        particles.forEach(p => {
            p.y -= p.speedY;
            p.x += Math.sin(p.y * 0.01) * 0.3 + p.driftX;

            if (p.y < 0) {
                p.y = height + 10;
                p.x = Math.random() * width;
            }
            if (p.x < 0) p.x = width;
            if (p.x > width) p.x = 0;

            ctx.beginPath();
            ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
            ctx.fillStyle = p.colorType === "amber" 
                ? `rgba(200, 138, 53, ${p.alpha})`
                : `rgba(180, 83, 42, ${p.alpha})`;
            ctx.fill();
        });

        requestAnimationFrame(animate);
    }

    animate();
}
