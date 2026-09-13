/**
 * AutoCAD 2024 高中生圖文自學手冊 · 互動式 CAD / PCB 畫布檢視器
 * 原生 HTML5 Canvas 實作 · 支援圖層開關、縮放平移、元件點選與 AutoCAD 指令聯動解說
 */

class CADViewer {
  constructor(canvasId, sidebarId, hudId) {
    this.canvas = document.getElementById(canvasId);
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.sidebar = document.getElementById(sidebarId);
    this.hud = document.getElementById(hudId);

    // 視圖狀態 (以公釐 mm 為邏輯座標，中心原點 (0,0) 置於板中央或左下角)
    this.scale = 8.5; // 螢幕像素 / mm
    this.panX = 0;
    this.panY = 0;
    this.isDragging = false;
    this.startX = 0;
    this.startY = 0;
    this.hoveredElement = null;
    this.selectedElement = null;

    // 顯示模式: 'pcb' (實體電路板) 或 'schematic' (原理圖)
    this.viewMode = 'pcb';

    // 圖層顯示開關
    this.layers = {
      outline: true,   // 01_板框外輪廓 (黃色)
      drill: true,     // 02_螺栓安裝孔 (洋紅)
      pads: true,      // 03_貫孔焊盤 (青色/金黃)
      traces: true,    // 04_銅箔走線 (亮綠色 45度角)
      silk: true,      // 05_頂層絲印 (白色文字外框)
      dim: true        // 06_工程尺寸標註 (橙色)
    };

    // PCB 元件幾何資料 (經典 NE555 雙色閃燈電路板, 50mm x 35mm)
    this.initPCBData();
    this.initEventListeners();
    this.resizeCanvas();
    this.resetView();
    this.render();
  }

  initPCBData() {
    // 板尺寸: 50mm x 35mm, 座標系 (0,0) 到 (50,35)
    this.pcb = {
      width: 50,
      height: 35,
      cornerRadius: 3.0,
      mountingHoles: [
        { x: 3.5, y: 3.5, r: 1.6, desc: "左下安裝孔 (M3螺絲, 直徑3.2mm)" },
        { x: 46.5, y: 3.5, r: 1.6, desc: "右下安裝孔 (M3螺絲, 直徑3.2mm)" },
        { x: 46.5, y: 31.5, r: 1.6, desc: "右上安裝孔 (M3螺絲, 直徑3.2mm)" },
        { x: 3.5, y: 31.5, r: 1.6, desc: "左上安裝孔 (M3螺絲, 直徑3.2mm)" }
      ],
      // DIP-8 NE555 IC 腳座 (標準 2.54mm 腳距, 7.62mm 排距)
      ic: {
        id: "U1",
        name: "NE555 雙極性定時器 IC",
        package: "DIP-8",
        cx: 25.0,
        cy: 17.5,
        width: 6.5,
        length: 9.8,
        pads: [
          // 左側 1~4 (Pin 1 在左下)
          { no: 1, x: 21.19, y: 13.69, name: "GND (接地)", net: "GND" },
          { no: 2, x: 21.19, y: 16.23, name: "TRIG (觸發觸發端)", net: "TRIG" },
          { no: 3, x: 21.19, y: 18.77, name: "OUT (訊號輸出端)", net: "OUT" },
          { no: 4, x: 21.19, y: 21.31, name: "RESET (低電位重置端)", net: "VCC" },
          // 右側 5~8 (Pin 8 在右上)
          { no: 8, x: 28.81, y: 21.31, name: "VCC (正電源輸入 +9V)", net: "VCC" },
          { no: 7, x: 28.81, y: 18.77, name: "DISCH (放電接腳)", net: "DISCH" },
          { no: 6, x: 28.81, y: 16.23, name: "THRES (門檻比較端)", net: "TRIG" },
          { no: 5, x: 28.81, y: 13.69, name: "CONT (控制電壓濾波)", net: "CONT" }
        ]
      },
      // 離散被動元件
      components: [
        {
          id: "J1",
          type: "端子台",
          name: "DC 9V 電源端子 (2-Pin 5.08mm)",
          cx: 6.0,
          cy: 17.5,
          box: { w: 6.0, h: 10.0 },
          pads: [
            { x: 6.0, y: 15.0, net: "GND", label: "GND (-)" },
            { x: 6.0, y: 20.0, net: "VCC", label: "VCC (+9V)" }
          ]
        },
        {
          id: "R1",
          type: "電阻",
          name: "充電電阻 1kΩ (1/4W 碳膜)",
          cx: 35.0,
          cy: 26.0,
          box: { w: 8.0, h: 2.8 },
          pads: [
            { x: 31.0, y: 26.0, net: "VCC" },
            { x: 39.0, y: 26.0, net: "DISCH" }
          ]
        },
        {
          id: "R2",
          type: "電阻",
          name: "放電定時電阻 100kΩ (決定閃爍週期)",
          cx: 35.0,
          cy: 17.5,
          box: { w: 8.0, h: 2.8 },
          pads: [
            { x: 31.0, y: 17.5, net: "DISCH" },
            { x: 39.0, y: 17.5, net: "TRIG" }
          ]
        },
        {
          id: "C1",
          type: "電解電容",
          name: "定時電解電容 10μF / 25V",
          cx: 14.0,
          cy: 26.0,
          r: 3.0,
          pads: [
            { x: 12.5, y: 26.0, net: "TRIG", label: "+" },
            { x: 15.5, y: 26.0, net: "GND", label: "-" }
          ]
        },
        {
          id: "C2",
          type: "陶瓷電容",
          name: "高頻濾波電容 0.01μF (103)",
          cx: 14.0,
          cy: 9.0,
          box: { w: 4.5, h: 2.5 },
          pads: [
            { x: 12.0, y: 9.0, net: "CONT" },
            { x: 16.0, y: 9.0, net: "GND" }
          ]
        },
        {
          id: "R3",
          type: "電阻",
          name: "LED1 限流電阻 470Ω",
          cx: 35.0,
          cy: 9.0,
          box: { w: 8.0, h: 2.8 },
          pads: [
            { x: 31.0, y: 9.0, net: "OUT" },
            { x: 39.0, y: 9.0, net: "LED1_A" }
          ]
        },
        {
          id: "LED1",
          type: "發光二極體",
          name: "紅色發光二極體 LED 5mm",
          cx: 44.0,
          cy: 12.0,
          r: 2.5,
          pads: [
            { x: 44.0, y: 10.73, net: "LED1_A", label: "A (陽極)" },
            { x: 44.0, y: 13.27, net: "GND", label: "K (陰極)" }
          ]
        },
        {
          id: "LED2",
          type: "發光二極體",
          name: "綠色發光二極體 LED 5mm (交互閃爍)",
          cx: 44.0,
          cy: 22.0,
          r: 2.5,
          pads: [
            { x: 44.0, y: 20.73, net: "VCC", label: "A (陽極)" },
            { x: 44.0, y: 23.27, net: "OUT", label: "K (陰極)" }
          ]
        }
      ],
      // 銅箔走線清單 (具備嚴格 45 度角導向)
      traces: [
        // VCC 匯流排 (寬度 1.0mm)
        { net: "VCC", width: 1.0, points: [[6.0, 20.0], [9.0, 23.0], [21.19, 21.31]] },
        { net: "VCC", width: 1.0, points: [[21.19, 21.31], [25.0, 24.0], [28.81, 21.31]] },
        { net: "VCC", width: 1.0, points: [[28.81, 21.31], [30.0, 24.0], [31.0, 26.0]] },
        { net: "VCC", width: 1.0, points: [[31.0, 26.0], [38.0, 26.0], [42.0, 22.0], [44.0, 20.73]] },

        // GND 匯流排 (寬度 1.0mm)
        { net: "GND", width: 1.0, points: [[6.0, 15.0], [10.0, 11.0], [16.0, 9.0]] },
        { net: "GND", width: 1.0, points: [[16.0, 9.0], [18.0, 11.0], [21.19, 13.69]] },
        { net: "GND", width: 1.0, points: [[6.0, 15.0], [10.0, 21.0], [15.5, 26.0]] },
        { net: "GND", width: 1.0, points: [[44.0, 13.27], [42.0, 11.27], [35.0, 5.0], [20.0, 5.0], [16.0, 9.0]] },

        // 訊號線 (寬度 0.5mm, 45度斜角)
        // DISCH 接點 (Pin 7 到 R1 與 R2)
        { net: "DISCH", width: 0.5, points: [[28.81, 18.77], [30.5, 18.77], [31.0, 17.5]] },
        { net: "DISCH", width: 0.5, points: [[39.0, 26.0], [37.0, 24.0], [35.0, 20.0], [31.0, 17.5]] },

        // TRIG & THRES 連結 (Pin 2 + Pin 6 + C1 + R2)
        { net: "TRIG", width: 0.5, points: [[21.19, 16.23], [18.0, 19.42], [14.0, 23.42], [12.5, 26.0]] },
        { net: "TRIG", width: 0.5, points: [[28.81, 16.23], [30.0, 15.0], [34.0, 15.0], [39.0, 17.5]] },
        { net: "TRIG", width: 0.5, points: [[21.19, 16.23], [24.0, 13.42], [26.0, 13.42], [28.81, 16.23]] },

        // OUT 訊號輸出 (Pin 3 到 R3 與 LED2 陰極)
        { net: "OUT", width: 0.5, points: [[21.19, 18.77], [23.0, 16.96], [28.0, 11.0], [31.0, 9.0]] },
        { net: "OUT", width: 0.5, points: [[21.19, 18.77], [25.0, 22.58], [30.0, 22.58], [37.0, 22.58], [44.0, 23.27]] },

        // R3 到 LED1 陽極
        { net: "LED1_A", width: 0.5, points: [[39.0, 9.0], [42.0, 9.0], [44.0, 10.73]] },

        // CONT 到 C2 (Pin 5 到 C2)
        { net: "CONT", width: 0.5, points: [[28.81, 13.69], [25.0, 9.88], [15.0, 9.88], [12.0, 9.0]] }
      ]
    };
  }

  initEventListeners() {
    window.addEventListener('resize', () => {
      this.resizeCanvas();
      this.render();
    });

    // 滑鼠拖曳 (Pan)
    this.canvas.addEventListener('mousedown', (e) => {
      this.isDragging = true;
      this.startX = e.clientX - this.panX;
      this.startY = e.clientY - this.panY;
    });

    window.addEventListener('mousemove', (e) => {
      const rect = this.canvas.getBoundingClientRect();
      const mouseX = e.clientX - rect.left;
      const mouseY = e.clientY - rect.top;

      if (this.isDragging) {
        this.panX = e.clientX - this.startX;
        this.panY = e.clientY - this.startY;
        this.render();
      }

      // 計算滑鼠在邏輯世界座標中的位置 (公釐 mm)
      const worldPos = this.screenToWorld(mouseX, mouseY);
      if (this.hud) {
        this.hud.innerText = `X: ${worldPos.x.toFixed(2)} mm | Y: ${worldPos.y.toFixed(2)} mm | 比例: ${(this.scale * 10).toFixed(0)}%`;
      }

      // 檢查懸停元件
      this.checkHover(worldPos);
    });

    window.addEventListener('mouseup', () => {
      this.isDragging = false;
    });

    // 滑鼠滾輪縮放 (Zoom)
    this.canvas.addEventListener('wheel', (e) => {
      e.preventDefault();
      const rect = this.canvas.getBoundingClientRect();
      const mouseX = e.clientX - rect.left;
      const mouseY = e.clientY - rect.top;

      const zoomFactor = e.deltaY < 0 ? 1.15 : 0.87;
      const newScale = Math.max(3, Math.min(35, this.scale * zoomFactor));

      // 以滑鼠指針為中心進行縮放錨定
      this.panX = mouseX - (mouseX - this.panX) * (newScale / this.scale);
      this.panY = mouseY - (mouseY - this.panY) * (newScale / this.scale);
      this.scale = newScale;

      this.render();
    }, { passive: false });

    // 點選元件以展示 AutoCAD 指令詳解
    this.canvas.addEventListener('click', (e) => {
      const rect = this.canvas.getBoundingClientRect();
      const mouseX = e.clientX - rect.left;
      const mouseY = e.clientY - rect.top;
      const worldPos = this.screenToWorld(mouseX, mouseY);
      this.handleClick(worldPos);
    });
  }

  resizeCanvas() {
    const parent = this.canvas.parentElement;
    this.canvas.width = parent.clientWidth;
    this.canvas.height = Math.max(520, parent.clientHeight || 520);
  }

  resetView() {
    // 置中 PCB 板 (板尺寸 50 x 35)
    this.scale = Math.min(this.canvas.width / 65, this.canvas.height / 50);
    this.panX = (this.canvas.width - this.pcb.width * this.scale) / 2;
    this.panY = (this.canvas.height + this.pcb.height * this.scale) / 2;
    this.render();
  }

  worldToScreen(x, y) {
    // 世界座標原點在左下角，Y 向上；螢幕座標原點在左上角，Y 向下
    return {
      x: this.panX + x * this.scale,
      y: this.panY - y * this.scale
    };
  }

  screenToWorld(sx, sy) {
    return {
      x: (sx - this.panX) / this.scale,
      y: (this.panY - sy) / this.scale
    };
  }

  toggleLayer(layerName, state) {
    if (this.layers.hasOwnProperty(layerName)) {
      this.layers[layerName] = state !== undefined ? state : !this.layers[layerName];
      this.render();
    }
  }

  checkHover(worldPos) {
    let found = null;
    const tol = 1.5; // 容許點擊距離 mm

    // 檢查 IC 晶片
    const ic = this.pcb.ic;
    if (Math.abs(worldPos.x - ic.cx) < ic.length / 2 && Math.abs(worldPos.y - ic.cy) < ic.width / 2) {
      found = { type: 'ic', data: ic };
    }

    // 檢查各被動元件
    if (!found) {
      for (const comp of this.pcb.components) {
        if (comp.r) {
          const d = Math.hypot(worldPos.x - comp.cx, worldPos.y - comp.cy);
          if (d <= comp.r + 0.8) {
            found = { type: 'comp', data: comp };
            break;
          }
        } else if (comp.box) {
          if (Math.abs(worldPos.x - comp.cx) < comp.box.w / 2 + 0.8 &&
              Math.abs(worldPos.y - comp.cy) < comp.box.h / 2 + 0.8) {
            found = { type: 'comp', data: comp };
            break;
          }
        }
      }
    }

    // 檢查焊盤
    if (!found) {
      for (const pad of ic.pads) {
        if (Math.hypot(worldPos.x - pad.x, worldPos.y - pad.y) < 1.2) {
          found = { type: 'pad', data: pad, parent: ic };
          break;
        }
      }
    }

    if (this.hoveredElement !== found) {
      this.hoveredElement = found;
      this.canvas.style.cursor = found ? 'pointer' : 'crosshair';
      this.render();
    }
  }

  handleClick(worldPos) {
    if (this.hoveredElement) {
      this.selectedElement = this.hoveredElement;
      this.showElementDetails(this.selectedElement);
      this.render();
    } else {
      // 點在空白處
      this.selectedElement = null;
      this.showDefaultDetails();
      this.render();
    }
  }

  showDefaultDetails() {
    if (!this.sidebar) return;
    this.sidebar.innerHTML = `
      <div class="sidebar-title">
        <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
        <span>AutoCAD 實體屬性檢視</span>
      </div>
      <p style="font-size:0.85rem;color:#94a3b8;line-height:1.7;">
        點擊畫布上的任一電路板元件（例如 <strong>NE555 晶片</strong>、<strong>電阻</strong>、<strong>焊盤</strong> 或 <strong>銅箔走線</strong>），此面板將即時顯示該物件在 AutoCAD 2024 中對應的<strong>繪製指令、座標參數、圖層歸屬與高中程度物理原理解析</strong>！
      </p>
      <div style="margin-top:20px;padding:14px;background:#12151c;border:1px solid #2c3444;border-radius:6px;">
        <div style="font-size:0.82rem;font-weight:bold;color:#38bdf8;margin-bottom:8px;">💡 當前畫布提示</div>
        <ul style="font-size:0.8rem;color:#cbd5e1;padding-left:18px;line-height:1.6;">
          <li>滑鼠滾輪：自由無段縮放 (Zoom)</li>
          <li>滑鼠左鍵按住拖曳：平移視圖 (Pan)</li>
          <li>上方圖層按鈕：即時切換板框/焊盤/銅箔</li>
        </ul>
      </div>
    `;
  }

  showElementDetails(el) {
    if (!this.sidebar) return;
    let html = '';

    if (el.type === 'ic') {
      const ic = el.data;
      html = `
        <div class="sidebar-title" style="color:#00d2ff;">
          <span>🎯 元件詳情：${ic.id} (${ic.name})</span>
        </div>
        <div class="element-details">
          <div class="detail-row"><span class="detail-label">封裝規格</span><span class="detail-val">${ic.package} (標準雙列直插)</span></div>
          <div class="detail-row"><span class="detail-label">板面座標</span><span class="detail-val">X: ${ic.cx}mm, Y: ${ic.cy}mm</span></div>
          <div class="detail-row"><span class="detail-label">本體尺寸</span><span class="detail-val">長 9.8mm × 寬 6.5mm</span></div>
          <div class="detail-row"><span class="detail-label">所屬圖層</span><span class="detail-val" style="color:#fff;">05_Top_Silk (頂層絲印)</span></div>
        </div>
        <div style="margin-top:12px;">
          <div style="font-size:0.85rem;font-weight:bold;color:#10b981;margin-bottom:6px;">🛠️ AutoCAD 2024 繪製指令：</div>
          <div class="cmd-line" style="font-size:0.8rem;"><span class="cmd-prompt">指令:</span> RECTANG ➜ @9.8,6.5</div>
          <div class="cmd-line" style="font-size:0.8rem;"><span class="cmd-prompt">指令:</span> FILLET (圓角 R=0.5)</div>
          <div class="cmd-line" style="font-size:0.8rem;"><span class="cmd-prompt">指令:</span> BLOCK ➜ 命名為 "DIP8_IC"</div>
        </div>
        <div class="memo-card orange" style="padding:12px 16px;margin-top:14px;font-size:0.82rem;">
          <strong>🧑‍🏫 高中生秒懂原理：</strong><br>
          為什麼 IC 腳距剛好是 <strong>2.54 mm</strong>？因為這是早年歐美英制的 <strong>100 mil (0.1 英吋)</strong>！現代麵包板孔距、萬用板都是這個倍數。在 AutoCAD 中善用 <code>ARRAY</code>（矩形陣列）輸入行距 2.54mm，點一下就能瞬間生成 8 個孔！
        </div>
      `;
    } else if (el.type === 'pad') {
      const pad = el.data;
      html = `
        <div class="sidebar-title" style="color:#fbbf24;">
          <span>🔘 貫孔焊盤：Pin ${pad.no} (${pad.name})</span>
        </div>
        <div class="element-details">
          <div class="detail-row"><span class="detail-label">焊盤中心</span><span class="detail-val">X: ${pad.x}mm, Y: ${pad.y}mm</span></div>
          <div class="detail-row"><span class="detail-label">焊盤外徑</span><span class="detail-val">Ø 2.0 mm (銅箔焊環)</span></div>
          <div class="detail-row"><span class="detail-label">內鑽孔徑</span><span class="detail-val">Ø 0.9 mm (穿腳孔)</span></div>
          <div class="detail-row"><span class="detail-label">電路網路</span><span class="detail-val" style="color:#4ade80;">Net: ${pad.net}</span></div>
          <div class="detail-row"><span class="detail-label">所屬圖層</span><span class="detail-val" style="color:#38bdf8;">03_Pads_ThroughHole</span></div>
        </div>
        <div style="margin-top:12px;">
          <div style="font-size:0.85rem;font-weight:bold;color:#10b981;margin-bottom:6px;">🛠️ AutoCAD 2024 繪製指令：</div>
          <div class="cmd-line" style="font-size:0.8rem;"><span class="cmd-prompt">外焊環:</span> CIRCLE ➜ 點選座標 ➜ 半徑 1.0</div>
          <div class="cmd-line" style="font-size:0.8rem;"><span class="cmd-prompt">內鑽孔:</span> CIRCLE ➜ 鎖同心 ➜ 半徑 0.45</div>
          <div class="cmd-line" style="font-size:0.8rem;"><span class="cmd-prompt">焊盤實心:</span> DONUT (環) ➜ 內徑 0.9, 外徑 2.0</div>
        </div>
        <div class="memo-card green" style="padding:12px 16px;margin-top:14px;font-size:0.82rem;">
          <strong>🧑‍🏫 焊接小常識：</strong><br>
          若外徑太小（例如只有 1.2mm），焊槍高溫一燙銅箔容易脫落壞板；若內孔太小（<0.8mm），金屬腳穿不過去！在 AutoCAD 畫 <code>DONUT</code> 可以一鍵填滿實心甜甜圈形狀。
        </div>
      `;
    } else if (el.type === 'comp') {
      const comp = el.data;
      html = `
        <div class="sidebar-title" style="color:#34d399;">
          <span>📦 電路零件：${comp.id} (${comp.name})</span>
        </div>
        <div class="element-details">
          <div class="detail-row"><span class="detail-label">元件類別</span><span class="detail-val">${comp.type}</span></div>
          <div class="detail-row"><span class="detail-label">中心座標</span><span class="detail-val">X: ${comp.cx}mm, Y: ${comp.cy}mm</span></div>
          <div class="detail-row"><span class="detail-label">焊點個數</span><span class="detail-val">${comp.pads ? comp.pads.length : 0} 個</span></div>
          <div class="detail-row"><span class="detail-label">所屬圖層</span><span class="detail-val" style="color:#fff;">05_Top_Silk (外框)</span></div>
        </div>
        <div style="margin-top:12px;">
          <div style="font-size:0.85rem;font-weight:bold;color:#10b981;margin-bottom:6px;">🛠️ AutoCAD 2024 繪製指令：</div>
          <div class="cmd-line" style="font-size:0.8rem;"><span class="cmd-prompt">絲印框:</span> RECTANG 或 CIRCLE</div>
          <div class="cmd-line" style="font-size:0.8rem;"><span class="cmd-prompt">標籤字:</span> MTEXT ➜ 字高 1.5mm ➜ 輸入 "${comp.id}"</div>
          <div class="cmd-line" style="font-size:0.8rem;"><span class="cmd-prompt">旋轉角:</span> ROTATE ➜ 基點 ➜ 角度 90</div>
        </div>
      `;
    }

    this.sidebar.innerHTML = html;
  }

  render() {
    const ctx = this.ctx;
    const w = this.canvas.width;
    const h = this.canvas.height;

    // 清空背景 (AutoCAD 經典炭黑網格)
    ctx.fillStyle = '#0f141d';
    ctx.fillRect(0, 0, w, h);

    // 繪製微弱格線 (Grid F7)
    this.renderGrid(ctx);

    // 依圖層順序繪製 PCB 各層
    if (this.layers.outline) this.renderOutline(ctx);
    if (this.layers.drill) this.renderMountingHoles(ctx);
    if (this.layers.traces) this.renderTraces(ctx);
    if (this.layers.pads) this.renderPads(ctx);
    if (this.layers.silk) this.renderSilkscreen(ctx);
    if (this.layers.dim) this.renderDimensions(ctx);

    // 繪製十字游標輔助與座標原點
    this.renderOrigin(ctx);
  }

  renderGrid(ctx) {
    ctx.save();
    ctx.strokeStyle = '#1a2232';
    ctx.lineWidth = 1;

    const gridSize = 5.0 * this.scale; // 每 5mm 一條主格線
    const startX = this.panX % gridSize;
    const startY = this.panY % gridSize;

    ctx.beginPath();
    for (let x = startX; x < this.canvas.width; x += gridSize) {
      ctx.moveTo(x, 0);
      ctx.lineTo(x, this.canvas.height);
    }
    for (let y = startY; y < this.canvas.height; y += gridSize) {
      ctx.moveTo(0, y);
      ctx.lineTo(this.canvas.width, y);
    }
    ctx.stroke();
    ctx.restore();
  }

  renderOrigin(ctx) {
    const p = this.worldToScreen(0, 0);
    ctx.save();
    // X軸紅線, Y軸綠線 (經典 UCS Icon)
    ctx.lineWidth = 2;
    ctx.strokeStyle = '#ef4444';
    ctx.beginPath();
    ctx.moveTo(p.x, p.y);
    ctx.lineTo(p.x + 30, p.y);
    ctx.stroke();

    ctx.strokeStyle = '#22c55e';
    ctx.beginPath();
    ctx.moveTo(p.x, p.y);
    ctx.lineTo(p.x, p.y - 30);
    ctx.stroke();

    ctx.fillStyle = '#94a3b8';
    ctx.font = '10px monospace';
    ctx.fillText('UCS (0,0)', p.x + 4, p.y - 4);
    ctx.restore();
  }

  renderOutline(ctx) {
    ctx.save();
    const p1 = this.worldToScreen(0, 0);
    const p2 = this.worldToScreen(this.pcb.width, this.pcb.height);
    const pw = (this.pcb.width) * this.scale;
    const ph = (this.pcb.height) * this.scale;
    const r = this.pcb.cornerRadius * this.scale;

    // PCB 基板玻纖綠半透明底色
    ctx.fillStyle = 'rgba(16, 78, 48, 0.45)';
    ctx.strokeStyle = '#fbbf24'; // 板框外輪廓金黃色 (01_Board_Outline)
    ctx.lineWidth = Math.max(2, 0.5 * this.scale);

    // 圓角矩形 (FILLET R=3)
    ctx.beginPath();
    ctx.roundRect(p1.x, p2.y, pw, ph, r);
    ctx.fill();
    ctx.stroke();
    ctx.restore();
  }

  renderMountingHoles(ctx) {
    ctx.save();
    ctx.fillStyle = '#0f141d'; // 孔透光為底色
    ctx.strokeStyle = '#d946ef'; // 02_Mounting_Holes 洋紅色
    ctx.lineWidth = 2;

    for (const hole of this.pcb.mountingHoles) {
      const p = this.worldToScreen(hole.x, hole.y);
      const pr = hole.r * this.scale;
      ctx.beginPath();
      ctx.arc(p.x, p.y, pr, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();

      // 十字中心定位線
      ctx.strokeStyle = 'rgba(217, 70, 239, 0.5)';
      ctx.beginPath();
      ctx.moveTo(p.x - pr - 4, p.y);
      ctx.lineTo(p.x + pr + 4, p.y);
      ctx.moveTo(p.x, p.y - pr - 4);
      ctx.lineTo(p.x, p.y + pr + 4);
      ctx.stroke();
    }
    ctx.restore();
  }

  renderTraces(ctx) {
    ctx.save();
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';

    for (const trace of this.pcb.traces) {
      // 依網路區分走線顏色 (04_Copper_Traces)
      if (trace.net === 'VCC') {
        ctx.strokeStyle = '#f87171'; // 電源線微紅亮色
      } else if (trace.net === 'GND') {
        ctx.strokeStyle = '#38bdf8'; // 地線淡青
      } else {
        ctx.strokeStyle = '#22c55e'; // 訊號線翠綠色
      }

      ctx.lineWidth = trace.width * this.scale;
      ctx.beginPath();
      for (let i = 0; i < trace.points.length; i++) {
        const pt = this.worldToScreen(trace.points[i][0], trace.points[i][1]);
        if (i === 0) ctx.moveTo(pt.x, pt.y);
        else ctx.lineTo(pt.x, pt.y);
      }
      ctx.stroke();
    }
    ctx.restore();
  }

  renderPads(ctx) {
    ctx.save();
    // 繪製 IC 焊盤
    const ic = this.pcb.ic;
    for (const pad of ic.pads) {
      this.drawSinglePad(ctx, pad.x, pad.y, 2.0, 0.9, pad.no === 1);
    }

    // 繪製端子台與被動元件焊盤
    for (const comp of this.pcb.components) {
      if (comp.pads) {
        for (const pad of comp.pads) {
          this.drawSinglePad(ctx, pad.x, pad.y, 2.0, 0.9, false);
        }
      }
    }
    ctx.restore();
  }

  drawSinglePad(ctx, wx, wy, outerDia, innerDia, isPin1) {
    const p = this.worldToScreen(wx, wy);
    const ro = (outerDia / 2) * this.scale;
    const ri = (innerDia / 2) * this.scale;

    // Pin 1 正方形防呆焊盤或外圍圓形
    ctx.fillStyle = '#fbbf24'; // 銅箔亮金黃
    ctx.strokeStyle = '#d97706';
    ctx.lineWidth = 1;

    ctx.beginPath();
    if (isPin1) {
      // Pin 1 為八角形或正方形以示標記
      ctx.rect(p.x - ro, p.y - ro, ro * 2, ro * 2);
    } else {
      ctx.arc(p.x, p.y, ro, 0, Math.PI * 2);
    }
    ctx.fill();
    ctx.stroke();

    // 內穿孔鑽孔 (空心孔洞)
    ctx.fillStyle = '#0f141d';
    ctx.beginPath();
    ctx.arc(p.x, p.y, ri, 0, Math.PI * 2);
    ctx.fill();
  }

  renderSilkscreen(ctx) {
    ctx.save();
    ctx.strokeStyle = '#ffffff'; // 白色頂層絲印 (05_Top_Silk)
    ctx.fillStyle = '#ffffff';
    ctx.lineWidth = Math.max(1.2, 0.2 * this.scale);
    ctx.font = `${Math.max(10, 1.6 * this.scale)}px sans-serif`;

    // 繪製 IC 本體外框與防呆缺口
    const ic = this.pcb.ic;
    const icPos = this.worldToScreen(ic.cx, ic.cy);
    const halfW = (ic.width / 2) * this.scale;
    const halfL = (ic.length / 2) * this.scale;

    ctx.strokeRect(icPos.x - halfW, icPos.y - halfL, halfW * 2, halfL * 2);
    // Pin 1 側半圓防呆凹槽 (Notch)
    ctx.beginPath();
    ctx.arc(icPos.x, icPos.y + halfL, 1.2 * this.scale, Math.PI, 0);
    ctx.stroke();

    // 晶片文字
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('NE555', icPos.x, icPos.y);

    // 繪製各被動元件絲印外框與編號
    for (const comp of this.pcb.components) {
      const cp = this.worldToScreen(comp.cx, comp.cy);
      if (comp.r) {
        // 圓形元件 (電容/LED)
        const cr = comp.r * this.scale;
        ctx.beginPath();
        ctx.arc(cp.x, cp.y, cr, 0, Math.PI * 2);
        ctx.stroke();

        if (comp.id.startsWith('LED')) {
          // LED 切邊陰極標記
          ctx.beginPath();
          ctx.moveTo(cp.x + cr * 0.7, cp.y - cr);
          ctx.lineTo(cp.x + cr * 0.7, cp.y + cr);
          ctx.stroke();
        }
      } else if (comp.box) {
        // 矩形元件 (電阻/端子台)
        const bw = comp.box.w * this.scale;
        const bh = comp.box.h * this.scale;
        ctx.strokeRect(cp.x - bw / 2, cp.y - bh / 2, bw, bh);
      }

      // 零件編號 (R1, C1, J1...)
      ctx.textAlign = 'center';
      ctx.textBaseline = 'bottom';
      ctx.fillText(comp.id, cp.x, cp.y - (comp.r ? comp.r * this.scale + 2 : (comp.box.h / 2) * this.scale + 2));
    }

    // 板子抬頭絲印標籤
    ctx.font = `bold ${Math.max(11, 2.2 * this.scale)}px sans-serif`;
    ctx.fillStyle = '#38bdf8';
    ctx.textAlign = 'left';
    const titleP = this.worldToScreen(20, 31.5);
    ctx.fillText('555 FLASHER PCB v1.0', titleP.x, titleP.y);

    ctx.restore();
  }

  renderDimensions(ctx) {
    ctx.save();
    ctx.strokeStyle = '#f97316'; // 橙色工程尺寸標註 (06_Dimension)
    ctx.fillStyle = '#f97316';
    ctx.lineWidth = 1.2;
    ctx.font = `${Math.max(9, 1.4 * this.scale)}px monospace`;

    // 頂部水平尺寸 50.00 mm
    const pTopL = this.worldToScreen(0, this.pcb.height + 4);
    const pTopR = this.worldToScreen(this.pcb.width, this.pcb.height + 4);

    ctx.beginPath();
    ctx.moveTo(pTopL.x, pTopL.y);
    ctx.lineTo(pTopR.x, pTopR.y);
    ctx.stroke();

    // 箭頭
    this.drawArrow(ctx, pTopL.x, pTopL.y, 'left');
    this.drawArrow(ctx, pTopR.x, pTopR.y, 'right');

    ctx.textAlign = 'center';
    ctx.fillText('50.00 mm', (pTopL.x + pTopR.x) / 2, pTopL.y - 4);

    // 右側垂直尺寸 35.00 mm
    const pRightB = this.worldToScreen(this.pcb.width + 4, 0);
    const pRightT = this.worldToScreen(this.pcb.width + 4, this.pcb.height);

    ctx.beginPath();
    ctx.moveTo(pRightB.x, pRightB.y);
    ctx.lineTo(pRightT.x, pRightT.y);
    ctx.stroke();

    this.drawArrow(ctx, pRightB.x, pRightB.y, 'down');
    this.drawArrow(ctx, pRightT.x, pRightT.y, 'up');

    ctx.textAlign = 'left';
    ctx.fillText('35.00 mm', pRightB.x + 6, (pRightB.y + pRightT.y) / 2);

    ctx.restore();
  }

  drawArrow(ctx, x, y, dir) {
    const size = 6;
    ctx.beginPath();
    if (dir === 'left') {
      ctx.moveTo(x, y);
      ctx.lineTo(x + size, y - size / 2);
      ctx.lineTo(x + size, y + size / 2);
    } else if (dir === 'right') {
      ctx.moveTo(x, y);
      ctx.lineTo(x - size, y - size / 2);
      ctx.lineTo(x - size, y + size / 2);
    } else if (dir === 'up') {
      ctx.moveTo(x, y);
      ctx.lineTo(x - size / 2, y + size);
      ctx.lineTo(x + size / 2, y + size);
    } else if (dir === 'down') {
      ctx.moveTo(x, y);
      ctx.lineTo(x - size / 2, y - size);
      ctx.lineTo(x + size / 2, y - size);
    }
    ctx.closePath();
    ctx.fill();
  }
}

// 頁面載入時自動初始化檢視器實例
window.addEventListener('DOMContentLoaded', () => {
  if (document.getElementById('cadCanvas')) {
    window.myCADViewer = new CADViewer('cadCanvas', 'cadSidebar', 'cadHud');
  }
});
