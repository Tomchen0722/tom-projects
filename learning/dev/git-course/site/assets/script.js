
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
