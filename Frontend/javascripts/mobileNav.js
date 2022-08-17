const open_btn = document.querySelector('.open');
const close_btn = document.querySelector('.close');

open_btn.addEventListener('click', () => {
  document.querySelector('.open').style.display = 'none';
  document.querySelector('.close').style.display = 'flex';
  document.querySelector('.mobile__navigations').style.display = 'block';
});

close_btn.addEventListener('click', () => {
  document.querySelector('.open').style.display = 'flex';
  document.querySelector('.close').style.display = 'none';
  document.querySelector('.mobile__navigations').style.display = 'none';
});
