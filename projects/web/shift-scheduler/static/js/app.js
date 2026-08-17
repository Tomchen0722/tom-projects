// 後台共用的小腳本:刪除 / 發布這類不可逆動作,送出前先確認一次。
document.addEventListener('submit', (event) => {
  const form = event.target.closest('form[data-confirm]');
  if (form && !window.confirm(form.dataset.confirm)) {
    event.preventDefault();
  }
});

// 開始日改了,結束日自動跟上(避免填出結束早於開始的區間)
document.addEventListener('change', (event) => {
  const el = event.target;
  if (el.name !== 'start_date') return;
  const end = el.form && el.form.querySelector('[name=end_date]');
  if (end && (!end.value || end.value < el.value)) end.value = el.value;
});
