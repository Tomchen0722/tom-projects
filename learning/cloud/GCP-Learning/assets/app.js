/* GCP 自學道場 — 進度記錄與互動 */
(function(){
  var KEY = 'gcp_dojo_progress_v1';
  var store = {
    read: function(){
      try { return JSON.parse(localStorage.getItem(KEY) || '{}'); }
      catch(e){ return {}; }
    },
    write: function(o){
      try { localStorage.setItem(KEY, JSON.stringify(o)); } catch(e){}
    }
  };

  var TOTAL = (window.GCP_TOTAL_LESSONS || 1);

  function done(){ return store.read(); }

  function paintProgress(){
    var d = done();
    var n = Object.keys(d).filter(function(k){ return d[k]; }).length;
    var pct = Math.round(n / TOTAL * 100);
    document.querySelectorAll('.progress-pill .bar i').forEach(function(el){ el.style.width = pct + '%'; });
    document.querySelectorAll('[data-progress-text]').forEach(function(el){
      el.textContent = n + ' / ' + TOTAL + ' 課（' + pct + '%）';
    });
    // 側欄與首頁勾記
    document.querySelectorAll('a[data-lid]').forEach(function(a){
      a.classList.toggle('done', !!d[a.getAttribute('data-lid')]);
    });
  }

  // 完成按鈕
  function initDoneBtn(){
    var btn = document.getElementById('doneBtn');
    if(!btn) return;
    var id = btn.getAttribute('data-lid');
    function render(){
      var on = !!done()[id];
      btn.classList.toggle('on', on);
      btn.querySelector('.lbl').textContent = on ? '已完成這一課' : '標記為已完成';
    }
    btn.addEventListener('click', function(){
      var d = done();
      d[id] = !d[id];
      if(!d[id]) delete d[id];
      store.write(d);
      render(); paintProgress();
    });
    render();
  }

  // 複製程式碼
  function initCopy(){
    document.querySelectorAll('.code').forEach(function(box){
      var btn = box.querySelector('.copy-btn');
      var pre = box.querySelector('pre');
      if(!btn || !pre) return;
      btn.addEventListener('click', function(){
        var txt = pre.innerText;
        var ok = function(){
          btn.textContent = '已複製';
          btn.classList.add('ok');
          setTimeout(function(){ btn.textContent = '複製'; btn.classList.remove('ok'); }, 1600);
        };
        if(navigator.clipboard && navigator.clipboard.writeText){
          navigator.clipboard.writeText(txt).then(ok, fallback);
        } else { fallback(); }
        function fallback(){
          var ta = document.createElement('textarea');
          ta.value = txt; ta.style.position='fixed'; ta.style.opacity='0';
          document.body.appendChild(ta); ta.select();
          try{ document.execCommand('copy'); ok(); }catch(e){}
          document.body.removeChild(ta);
        }
      });
    });
  }

  // 手機側欄
  function initMenu(){
    var btn = document.querySelector('.menu-btn');
    var sb  = document.querySelector('.sidebar');
    if(!btn || !sb) return;
    btn.addEventListener('click', function(){ sb.classList.toggle('open'); });
    document.querySelector('.main').addEventListener('click', function(){ sb.classList.remove('open'); });
  }

  // 側欄自動捲到目前課程
  function scrollNav(){
    var cur = document.querySelector('.nav-list a.current');
    if(cur && cur.offsetTop > 260){
      document.querySelector('.sidebar').scrollTop = cur.offsetTop - 200;
    }
  }

  document.addEventListener('DOMContentLoaded', function(){
    initDoneBtn(); initCopy(); initMenu(); paintProgress(); scrollNav();
  });
})();
