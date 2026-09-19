// 天機玄學閣主控制器（App Controller）
document.addEventListener("DOMContentLoaded", () => {
    initNavigation();
    initZiWeiModule();
    initPhysiognomyModule();
    initIChingModule();
    initQuizModule();
    initDailyOracle();
    initAudioControls();
    initStarBackground();
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
                <strong>🏫 高中生校園畫像：</strong>
                <span>${s.hsAnalogy}</span>
            </div>
            <div class="star-strengths-box">
                <strong>✨ 天賦優勢：</strong>
                <ul>${s.strengths.map(item => `<li>${item}</li>`).join("")}</ul>
            </div>
            <div class="star-study-box">
                <strong>📚 大考升學與學習錦囊：</strong>
                <p>${s.studyGuide}</p>
            </div>
            <div class="star-mindset-box">
                <strong>🛡️ 避坑與心態防禦：</strong>
                <p>${s.examMindset}</p>
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
            <div class="p-hs">${p.hsExplain}</div>
        `;
        container.appendChild(item);
    });
}

// 執行排盤計算與渲染 12 宮格
function runZiWeiCalculation() {
    const year = parseInt(document.getElementById("birthYear").value, 10) || 2008;
    const month = parseInt(document.getElementById("birthMonth").value, 10) || 6;
    const day = parseInt(document.getElementById("birthDay").value, 10) || 15;
    const hour = parseInt(document.getElementById("birthHour").value, 10) || 6;

    const result = window.ZiWeiSystem.calculateChart(year, month, day, hour);
    window.currentZiWeiChart = result;

    if (window.mysticAudio) {
        window.mysticAudio.playChime(380);
    }

    renderZiWeiGrid(result);
}

// 渲染紫微盤 12 宮格傳統排法
function renderZiWeiGrid(result) {
    const gridContainer = document.getElementById("ziweiPanGrid");
    const centerInfo = document.getElementById("ziweiCenterCourt");
    const detailPanel = document.getElementById("palaceDetailContent");
    if (!gridContainer || !centerInfo) return;

    gridContainer.innerHTML = "";

    // 十二地支在九宮格外圈的順序（傳統紫微盤排列）
    // 巳 午 未 申 (上方)
    // 辰 (左)     酉 (右)
    // 卯 (左)     戌 (右)
    // 寅 丑 子 亥 (下方)
    const displayOrder = [
        5, 6, 7, 8,   // 巳 午 未 申
        4,          9,   // 辰     酉
        3,          10,  // 卯     戌
        2, 1, 0, 11   // 寅 丑 子 亥
    ];

    // 更新中堂資訊
    centerInfo.innerHTML = `
        <div class="court-seal">天機盤印</div>
        <h3>紫微天府星盤中堂</h3>
        <p class="court-meta"><strong>歲次：</strong>${result.yearGan}${result.yearZhi}年</p>
        <p class="court-meta"><strong>五行局：</strong>${result.bureau}</p>
        <p class="court-meta"><strong>命宮坐地支：</strong>${result.mingZhi}宮 ｜ <strong>身宮：</strong>${result.shenZhi}宮</p>
        <div class="court-tip">💡 點選周圍任意宮位，即可在右側查看該宮的高中學業與生活解析！</div>
    `;

    displayOrder.forEach(zhiIdx => {
        const cellData = result.chart.find(c => c.zhiIndex === zhiIdx);
        if (!cellData) return;

        const cell = document.createElement("div");
        cell.className = `ziwei-cell ${cellData.isMing ? 'is-ming' : ''} ${cellData.isShen ? 'is-shen' : ''}`;
        cell.setAttribute("data-zhi", cellData.zhiIndex);

        const starNames = cellData.stars.map(sKey => {
            const s = window.ZiWeiSystem.stars[sKey];
            return `<span class="cell-star-tag">${s ? s.name : sKey}</span>`;
        }).join("");

        const sihuaBadges = cellData.sihua.map(b => `<span class="sihua-badge badge-${b}">${b}</span>`).join("");

        cell.innerHTML = `
            <div class="cell-top-bar">
                <span class="cell-palace-name">${cellData.palaceName}</span>
                <span class="cell-zhi">${cellData.zhiName}</span>
            </div>
            <div class="cell-stars">${starNames}</div>
            <div class="cell-sihua-row">${sihuaBadges}</div>
            ${cellData.isMing ? '<span class="marker-tag marker-ming">命宮坐此</span>' : ''}
            ${cellData.isShen ? '<span class="marker-tag marker-shen">身宮</span>' : ''}
        `;

        cell.addEventListener("click", () => {
            document.querySelectorAll(".ziwei-cell").forEach(c => c.classList.remove("selected"));
            cell.classList.add("selected");
            showPalaceDetail(cellData);
            window.mysticAudio.playStarGlitter();
        });

        gridContainer.appendChild(cell);
    });

    // 預設選中命宮
    const mingCell = result.chart.find(c => c.isMing) || result.chart[0];
    showPalaceDetail(mingCell);
}

// 點擊宮位顯示詳解
function showPalaceDetail(cellData) {
    const panel = document.getElementById("palaceDetailContent");
    if (!panel) return;

    const palaceInfo = window.ZiWeiSystem.palaces.find(p => p.id === cellData.palaceId) || {
        name: cellData.palaceName,
        modernDesc: "人生關鍵維度",
        hsExplain: "反映你的相應生活領域"
    };

    const starObjs = cellData.stars.map(k => window.ZiWeiSystem.stars[k]).filter(Boolean);

    panel.innerHTML = `
        <div class="detail-header">
            <h3 class="detail-title">${cellData.palaceName}（${cellData.zhiName}宮）</h3>
            <span class="detail-tag">${palaceInfo.category || "重要領域"}</span>
        </div>
        <div class="detail-meaning">
            <strong>🎯 宮位現代意涵：</strong>${palaceInfo.modernDesc}
        </div>
        <div class="detail-hs-meaning">
            <strong>🏫 高中生生活解讀：</strong>${palaceInfo.hsExplain}
        </div>
        <div class="detail-stars-section">
            <h4>🌟 坐守星曜解析：</h4>
            ${starObjs.length > 0 ? starObjs.map(s => `
                <div class="detail-star-block glass-panel">
                    <div class="ds-name"><strong>${s.name}</strong>（${s.element}・${s.title}）</div>
                    <div class="ds-archetype">${s.archetype}</div>
                    <div class="ds-study"><strong>💡 高中升學讀書策略：</strong>${s.studyGuide}</div>
                    <div class="ds-mind"><strong>⚠️ 避雷防爆心態：</strong>${s.examMindset}</div>
                </div>
            `).join("") : `<div class="detail-star-block"><p>此宮無十四主星（借對宮星曜觀測），象徵該領域靈活變通，受外部環境影響較大。</p></div>`}
        </div>
        ${cellData.sihua.length > 0 ? `
            <div class="detail-sihua-section">
                <h4>🔮 宮位四化引動：</h4>
                <div class="sihua-explain">本宮引動【${cellData.sihua.join("、")}】，代表在此生活維度中將得到格外顯著的能量催化與考驗！</div>
            </div>
        ` : ''}
    `;
}

// ----------------------------------------------------
// 2. 相術乾坤殿（手相與面相）
// ----------------------------------------------------
function initPhysiognomyModule() {
    initPalmistryInteractions();
    initFaceInteractions();
}

function initPalmistryInteractions() {
    const linesList = window.PhysiognomySystem.palmistry.lines;
    const mountsList = window.PhysiognomySystem.palmistry.mounts;
    const handTypesList = window.PhysiognomySystem.palmistry.handTypes;

    // 手相三大主線切換按鈕
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

        // 預設顯示生命線
        showPalmLineDetail(linesList[0]);
    }

    // 點擊 SVG 線路
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

    // 掌丘卡片渲染
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
                <div class="m-hs"><strong>🏫 高中生指引：</strong>${m.hsGuide}</div>
            `;
            mountsGrid.appendChild(card);
        });
    }

    // 五行掌型渲染
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
                <div class="ht-hs"><strong>📚 高中讀書特質：</strong>${ht.hsProfile}</div>
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
                <strong>🏫 高中生體感譬喻：</strong>
                <p>${line.hsAnalogy}</p>
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

    // 三停按鈕與卡片
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
                <div class="tz-hs"><strong>🏫 高中學業指引：</strong>${z.hsGuide}</div>
                <div class="tz-tuning"><strong>🌿 調養心法：</strong>${z.tuningTip}</div>
            `;
            threeZonesContainer.appendChild(card);
        });
    }

    // 五官卡片
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

    // 相由心生科學對照
    const mindsetBox = document.getElementById("mindsetScienceBox");
    if (mindsetBox && mindset) {
        mindsetBox.innerHTML = `
            <div class="mindset-card glass-panel">
                <div class="ms-quote">「${mindset.ancient}」</div>
                <div class="ms-science"><strong>🧬 現代神經認知科學解析：</strong>${mindset.modernScience}</div>
                <div class="ms-action"><strong>✨ 高中生每日實踐清單：</strong>${mindset.actionGuide}</div>
            </div>
        `;
    }
}

// ----------------------------------------------------
// 3. 易道變易殿（易經八卦）
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

// 渲染八卦圓盤與屬性
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
            <div class="tri-hs"><strong>🏫 青年心態：</strong>${t.hsConcept}</div>
        `;
        container.appendChild(item);
    });
}

// 執行文王金錢課拋擲
function performCoinToss() {
    if (coinTossCount >= 6) {
        return;
    }

    const tossBtn = document.getElementById("tossCoinsBtn");
    tossBtn.disabled = true;

    // 音效
    if (window.mysticAudio) {
        window.mysticAudio.playCoinDrop();
    }

    // 動畫翻轉銅錢
    const coins = [document.getElementById("coin1"), document.getElementById("coin2"), document.getElementById("coin3")];
    coins.forEach(c => {
        if (c) {
            c.classList.add("spinning");
        }
    });

    setTimeout(() => {
        coins.forEach(c => {
            if (c) c.classList.remove("spinning");
        });

        const tossResult = window.IChingSystem.tossCoins();
        coinTossResults.push(tossResult);
        coinTossCount++;

        // 更新銅錢外觀（面=3, 背=2）
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
            // 完成六爻，解析卦象！
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

    // 由上爻至初爻倒序顯示（卦象視覺自下而上構建）
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
                <h4>🎓 高中生人生與大考破局指南：</h4>
                <p>${result.originalHex.hsStrategy}</p>
                ${result.hasChanges ? `
                    <div class="future-advice">
                        <strong>🚀 轉變後的長遠啟示（變卦指引）：</strong>
                        <p>${result.changedHex.hsStrategy}</p>
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

// 64 卦速查選單
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
        const fullCode = lCode + uCode; // 下卦在下，上卦在上

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
                    <strong>🏫 高中決策心法：</strong>
                    <p>${hex.hsStrategy}</p>
                </div>
            </div>
        `;
    }

    upperSelect.addEventListener("change", updateLookup);
    lowerSelect.addEventListener("change", updateLookup);
    updateLookup();
}

// ----------------------------------------------------
// 4. 玄學大考驗（問答闖關）與每日靈光籤
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
        // 完成測驗，顯示總成績評定
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
                <h3>玄學大會考圓滿完成！</h3>
                <div class="qs-score">${userScore} <span class="unit">分</span></div>
                <div class="qs-rank">獲得榮譽封號：<strong>【${rankTitle}】</strong></div>
                <p class="qs-words">你已經成功掌握了紫微斗數、相術微表情與易經決策樹的底層智慧！願這份貫通古今的洞察力，陪伴你在高中的學業與生活中乘風破浪、所向披靡！</p>
                <button class="btn btn-gold" id="retryQuizBtn">重新挑戰測驗</button>
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
// 5. 畫布星宿背景動效 (Canvas Constellation Background)
// ----------------------------------------------------
function initStarBackground() {
    const canvas = document.getElementById("starfieldCanvas");
    if (!canvas) return;

    const ctx = canvas.getContext("2d");
    let width = canvas.width = window.innerWidth;
    let height = canvas.height = window.innerHeight;

    window.addEventListener("resize", () => {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    });

    const stars = [];
    const count = 75;
    for (let i = 0; i < count; i++) {
        stars.push({
            x: Math.random() * width,
            y: Math.random() * height,
            radius: Math.random() * 1.6 + 0.4,
            alpha: Math.random() * 0.8 + 0.2,
            speed: Math.random() * 0.25 + 0.05,
            direction: Math.random() * Math.PI * 2
        });
    }

    function animate() {
        ctx.clearRect(0, 0, width, height);

        // 繪製微弱星連線
        ctx.strokeStyle = "rgba(139, 92, 246, 0.08)";
        ctx.lineWidth = 0.6;
        for (let i = 0; i < stars.length; i++) {
            for (let j = i + 1; j < stars.length; j++) {
                const dx = stars[i].x - stars[j].x;
                const dy = stars[i].y - stars[j].y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < 100) {
                    ctx.beginPath();
                    ctx.moveTo(stars[i].x, stars[i].y);
                    ctx.lineTo(stars[j].x, stars[j].y);
                    ctx.stroke();
                }
            }
        }

        // 繪製星星
        stars.forEach(s => {
            s.x += Math.cos(s.direction) * s.speed;
            s.y += Math.sin(s.direction) * s.speed;

            if (s.x < 0) s.x = width;
            if (s.x > width) s.x = 0;
            if (s.y < 0) s.y = height;
            if (s.y > height) s.y = 0;

            ctx.beginPath();
            ctx.arc(s.x, s.y, s.radius, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(245, 158, 11, ${s.alpha})`;
            ctx.fill();
        });

        requestAnimationFrame(animate);
    }

    animate();
}
