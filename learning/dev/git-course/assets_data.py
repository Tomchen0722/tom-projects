# -*- coding: utf-8 -*-
"""網站樣式與互動腳本（供 build.py 匯入）。"""

CSS = r"""
:root{
  --bg:#faf6f0; --panel:#ffffff; --ink:#403a33; --muted:#8c8175;
  --line:#ece3d7; --brand:#c8795e; --brand2:#b08968; --accent:#b0674a;
  --code-bg:#2b2622; --code-ink:#ece3d7; --nav-bg:#f3ece1; --nav-ink:#6b6157;
  --nav-active:#c8795e; --radius:16px; --maxw:860px;
}
[data-theme="dark"]{
  --bg:#211d19; --panel:#2b2622; --ink:#ece3d7; --muted:#a89e90;
  --line:#3a332c; --code-bg:#181513; --nav-bg:#1a1712; --nav-ink:#b3a596;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0; background:var(--bg); color:var(--ink);
  font-family:"Segoe UI","PingFang TC","Microsoft JhengHei",-apple-system,"Noto Sans TC",sans-serif;
  line-height:1.85; font-size:17px; letter-spacing:.01em;
}

/* ---------- 側邊導覽（暖色淺色） ---------- */
#sidebar{
  position:fixed; top:0; left:0; width:300px; height:100vh; background:var(--nav-bg);
  color:var(--nav-ink); display:flex; flex-direction:column; z-index:40;
  border-right:1px solid var(--line);
}
.brand{display:flex; gap:12px; align-items:center; padding:24px 24px; text-decoration:none; color:var(--ink); border-bottom:1px solid rgba(0,0,0,.05)}
.brand-logo{font-size:28px; color:var(--brand); line-height:1}
.brand-text{display:flex; flex-direction:column; line-height:1.3}
.brand-text b{font-size:16px; font-weight:700}
.brand-text small{color:var(--muted); font-size:11.5px; margin-top:2px}
.nav-scroll{flex:1; overflow-y:auto; padding:10px 0}
.nav-scroll::-webkit-scrollbar{width:7px}
.nav-scroll::-webkit-scrollbar-thumb{background:#ddd0bf; border-radius:8px}
.nav-group{margin:4px 0 14px}
.nav-part{padding:14px 24px 6px; font-size:11px; letter-spacing:.16em; text-transform:uppercase; color:#a89b8a; font-weight:700}
#sidebar ul{list-style:none; margin:0; padding:0}
#sidebar li a{
  display:flex; gap:10px; align-items:baseline; padding:9px 24px; color:var(--nav-ink);
  text-decoration:none; font-size:14.5px; border-left:3px solid transparent; transition:background .15s;
}
#sidebar li a:hover{background:rgba(200,121,94,.08); color:var(--ink)}
#sidebar li.active a{background:rgba(200,121,94,.13); color:var(--brand); border-left-color:var(--nav-active); font-weight:600}
.nav-num{color:#b3a695; font-size:12px; min-width:20px; font-variant-numeric:tabular-nums}
.theme-toggle{
  margin:14px; padding:11px; background:transparent; color:var(--muted); border:1px solid var(--line);
  border-radius:12px; cursor:pointer; font-size:13px; transition:background .15s;
}
.theme-toggle:hover{background:rgba(200,121,94,.08); color:var(--brand)}

/* ---------- 主要內容 ---------- */
main{margin-left:300px; min-height:100vh; display:flex; flex-direction:column}
.content{width:100%; max-width:var(--maxw); margin:0 auto; padding:42px 28px 20px}
footer{max-width:var(--maxw); margin:0 auto; padding:30px 28px 60px; color:var(--muted); font-size:13px; text-align:center}

h1{font-size:31px; line-height:1.3; margin:.2em 0 .5em}
h2{font-size:23px; margin:1.8em 0 .6em; padding-top:.4em; border-top:1px solid var(--line)}
h3{font-size:19px; margin:1.4em 0 .5em}
h4{font-size:16.5px; margin:1.2em 0 .4em; color:var(--muted)}
p{margin:.7em 0}
a{color:var(--accent)}
strong{color:var(--ink)}
ul,ol{margin:.6em 0; padding-left:1.5em}
li{margin:.3em 0}
hr{border:none; border-top:1px solid var(--line); margin:2em 0}
blockquote{margin:1em 0; padding:.6em 1.1em; border-left:4px solid var(--brand2); background:rgba(107,77,230,.07); border-radius:0 8px 8px 0; color:var(--muted)}

/* 課程標頭 */
.lesson-head{margin-bottom:1.4em}
.lesson-part{display:inline-block; font-size:12.5px; font-weight:700; letter-spacing:.06em; color:var(--brand); background:rgba(240,81,51,.1); padding:4px 12px; border-radius:999px}
.lesson-sub{color:var(--muted); font-size:18px; margin-top:-.2em}

/* 行內程式碼 */
code{font-family:"Cascadia Code","JetBrains Mono","Fira Code",Consolas,monospace; font-size:.9em;
  background:rgba(107,77,230,.1); color:#7c4dff; padding:.12em .42em; border-radius:6px}
[data-theme="dark"] code{color:#b39dff; background:rgba(124,77,255,.16)}

/* 程式碼區塊 */
.codewrap{position:relative; margin:1.1em 0; border-radius:14px; overflow:hidden; border:1px solid #3a332c}
.codewrap::before{content:attr(data-lang); position:absolute; top:0; left:0; font-size:11px; letter-spacing:.08em;
  text-transform:uppercase; color:#a89e90; background:#211d19; padding:4px 12px; border-bottom-right-radius:8px; font-family:monospace}
.codewrap pre{margin:0; padding:38px 16px 16px; background:var(--code-bg); overflow-x:auto}
.codewrap code{background:none; color:var(--code-ink); padding:0; font-size:14px; line-height:1.75}
.copybtn{position:absolute; top:6px; right:8px; z-index:2; background:#3a332c; color:#d8ccbb; border:1px solid #4a4239;
  border-radius:8px; padding:4px 12px; font-size:12px; cursor:pointer}
.copybtn:hover{background:#4a4239; color:#fff}
.copybtn.done{background:#8a9a5b; color:#fff; border-color:#8a9a5b}

/* 提示框 */
.callout{margin:1.2em 0; border-radius:12px; padding:14px 18px; border:1px solid var(--line); background:var(--panel)}
.callout-head{font-weight:700; margin-bottom:.3em; font-size:15px}
.callout-body>*:first-child{margin-top:0}
.callout-body>*:last-child{margin-bottom:0}
.callout.tip{background:rgba(37,99,235,.07); border-color:rgba(37,99,235,.3)}
.callout.tip .callout-head{color:#2563eb}
.callout.warn{background:rgba(217,119,6,.09); border-color:rgba(217,119,6,.35)}
.callout.warn .callout-head{color:#b45309}
.callout.danger{background:rgba(220,38,38,.08); border-color:rgba(220,38,38,.35)}
.callout.danger .callout-head{color:#dc2626}
.callout.rescue{background:rgba(5,150,105,.09); border-color:rgba(5,150,105,.35)}
.callout.rescue .callout-head{color:#059669}
.callout.story{background:rgba(107,77,230,.08); border-color:rgba(107,77,230,.32)}
.callout.story .callout-head{color:#6b4de6}
.callout.vscode{background:rgba(0,122,204,.08); border-color:rgba(0,122,204,.32)}
.callout.vscode .callout-head{color:#007acc}
.callout.best{background:rgba(15,118,110,.08); border-color:rgba(15,118,110,.3)}
.callout.best .callout-head{color:#0f766e}

/* 表格 */
.tablewrap{overflow-x:auto; margin:1.1em 0}
table{border-collapse:collapse; width:100%; font-size:15px; background:var(--panel); border-radius:10px; overflow:hidden}
th,td{border:1px solid var(--line); padding:9px 13px; text-align:left; vertical-align:top}
th{background:rgba(107,77,230,.08); font-weight:700}
[data-theme="dark"] th{background:rgba(124,77,255,.12)}

/* 上下課導覽 */
.pager{max-width:var(--maxw); margin:20px auto 0; padding:0 28px; display:flex; gap:14px; justify-content:space-between}
.pg{flex:1; display:flex; flex-direction:column; gap:2px; padding:14px 18px; border:1px solid var(--line);
  border-radius:12px; background:var(--panel); text-decoration:none; color:var(--ink)}
.pg:hover{border-color:var(--brand); box-shadow:0 4px 18px rgba(0,0,0,.06)}
.pg small{color:var(--muted); font-size:12.5px}
.pg span{font-weight:600}
.pg-next{text-align:right}
.pg-empty{visibility:hidden}

/* 首頁 */
.hero{background:linear-gradient(135deg,#f5e9db 0%,#efdccb 55%,#e9cdb8 100%); color:var(--ink); border-radius:24px; padding:46px 38px; margin-bottom:22px; border:1px solid #ecdcc9}
.hero-badge{display:inline-block; font-size:13px; font-weight:600; background:rgba(200,121,94,.16); color:#a65a3d; padding:6px 15px; border-radius:999px; margin-bottom:16px}
.hero h1{font-size:34px; margin:.1em 0 .35em; color:#4a4038; letter-spacing:.01em}
.hero-sub{color:#6e6357; font-size:16.5px; max-width:640px}
.hero-facts{display:flex; gap:30px; flex-wrap:wrap; margin:24px 0}
.hero-facts div{display:flex; flex-direction:column}
.hero-facts b{font-size:28px; color:var(--brand)}
.hero-facts small{color:#8c8175; font-size:12.5px}
.hero-cta{display:inline-block; background:var(--brand); color:#fff; text-decoration:none; padding:12px 24px; border-radius:12px; font-weight:700}
.hero-cta:hover{background:#d8412a}
.learn-goals{background:var(--panel); border:1px solid var(--line); border-radius:16px; padding:22px 26px; margin-bottom:30px}
.goal-list{list-style:none; padding:0; display:grid; grid-template-columns:1fr 1fr; gap:6px 20px}
.part-title{margin:30px 0 12px}
.card-grid{display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-bottom:8px}
.lesson-card{display:flex; gap:14px; align-items:center; padding:16px 18px; background:var(--panel); border:1px solid var(--line);
  border-radius:14px; text-decoration:none; color:var(--ink)}
.lesson-card:hover{border-color:var(--brand); transform:translateY(-2px); box-shadow:0 8px 22px rgba(0,0,0,.07)}
.card-num{font-size:20px; font-weight:800; color:var(--brand); min-width:34px; font-variant-numeric:tabular-nums}
.card-body{display:flex; flex-direction:column}
.card-body b{font-size:15.5px; line-height:1.35}
.card-body small{color:var(--muted); font-size:13px; margin-top:2px}

/* 自我檢核 / 練習 */
.quiz{margin-top:2.4em; padding-top:1.4em; border-top:2px dashed var(--line)}
.quiz-title{border-top:none; margin-top:1.2em}
.quiz-hint{color:var(--muted); font-size:14.5px; margin-top:-.2em}
.qa{margin:.6em 0; border:1px solid var(--line); border-radius:12px; background:var(--panel); overflow:hidden}
.qa>summary{cursor:pointer; padding:13px 18px; font-weight:600; list-style:none; display:flex; gap:10px; align-items:baseline}
.qa>summary::-webkit-details-marker{display:none}
.qa>summary::before{content:"▸"; color:var(--brand); transition:transform .15s}
.qa[open]>summary::before{transform:rotate(90deg)}
.qa>summary:hover{background:rgba(200,121,94,.05)}
.qnum{color:var(--brand); font-weight:800; font-size:13.5px; background:rgba(200,121,94,.12); padding:1px 9px; border-radius:999px}
.qa-body{padding:2px 18px 14px 18px; border-top:1px solid var(--line); color:var(--ink)}
.qa-body>*:first-child{margin-top:.6em}
.practice-list{background:var(--panel); border:1px solid var(--line); border-radius:12px; padding:14px 18px 14px 40px}
.practice-list li{margin:.5em 0}

/* 速查表：讓表格更緊湊好掃 */
.lesson-part{margin-bottom:6px}

/* 選單按鈕 / 遮罩（手機） */
#menuToggle{display:none; position:fixed; top:12px; left:12px; z-index:60; background:var(--nav-bg); color:#fff;
  border:none; width:44px; height:44px; border-radius:10px; font-size:20px; cursor:pointer}
#overlay{display:none; position:fixed; inset:0; background:rgba(0,0,0,.5); z-index:35}

@media (max-width:960px){
  body{font-size:16px}
  #sidebar{transform:translateX(-100%); transition:transform .25s ease}
  body.nav-open #sidebar{transform:translateX(0)}
  body.nav-open #overlay{display:block}
  #menuToggle{display:block}
  main{margin-left:0}
  .content{padding-top:64px}
  .goal-list,.card-grid{grid-template-columns:1fr}
  .hero h1{font-size:27px}
}
"""

JS = r"""
function copyCode(btn){
  const code = btn.parentElement.querySelector('code').innerText;
  navigator.clipboard.writeText(code).then(()=>{
    const old = btn.textContent;
    btn.textContent = '已複製 ✓'; btn.classList.add('done');
    setTimeout(()=>{ btn.textContent = old; btn.classList.remove('done'); }, 1400);
  });
}
function toggleNav(){ document.body.classList.toggle('nav-open'); }
function toggleTheme(){
  const cur = document.documentElement.getAttribute('data-theme');
  const next = cur === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  try{ localStorage.setItem('gitcourse-theme', next); }catch(e){}
}
(function(){
  try{
    const saved = localStorage.getItem('gitcourse-theme');
    if(saved){ document.documentElement.setAttribute('data-theme', saved); }
  }catch(e){}
})();
"""
