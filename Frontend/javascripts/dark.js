const toggle = document.querySelector('.toggle');
const h1 = document.querySelector('h1');
const h2 = document.querySelectorAll('h2');
const h3 = document.querySelectorAll('h3');
const h4 = document.querySelectorAll('h4');
const p = document.querySelectorAll('p');
const a = document.querySelectorAll('a');
const li = document.querySelectorAll('li');
const header = document.querySelector('header');
const btn = document.querySelectorAll('.btn');
const serviceHead = document.querySelectorAll('.service_head');
const servicePara = document.querySelectorAll('.service_para');
const testimonialBox = document.querySelectorAll('.testimonial_box');
const testPara = document.querySelectorAll('.test_para');
const stepList = document.querySelectorAll('.step_list');
const unfilled = document.querySelectorAll('.unfilled');

const light_btn = document.querySelector('.light_mode');
const dark_btn = document.querySelector('.dark_mode');

toggle.addEventListener('click', () => {
  const body = document.querySelector('body');

  if (body.classList.contains('dark')) {
    body.classList.remove('dark');
    header.classList.remove('dark');
    h1.classList.remove('dark');
    h2.forEach((tog) => tog.classList.remove('dark'));
    h3.forEach((tog) => tog.classList.remove('dark'));
    h4.forEach((tog) => tog.classList.remove('dark'));
    p.forEach((tog) => tog.classList.remove('dark'));
    a.forEach((tog) => tog.classList.remove('dark'));
    li.forEach((tog) => tog.classList.remove('dark'));
    btn.forEach((tog) => tog.classList.remove('dark'));
    serviceHead.forEach((tog) => tog.classList.remove('dark'));
    servicePara.forEach((tog) => tog.classList.remove('dark'));
    stepList.forEach((tog) => tog.classList.remove('dark'));
    testimonialBox.forEach((tog) => tog.classList.remove('dark'));
    testPara.forEach((tog) => tog.classList.remove('dark'));
    unfilled.forEach((tog) => tog.classList.remove('dark'));
  } else {
    body.classList.add('dark');
    header.classList.add('dark');
    h1.classList.add('dark');
    h2.forEach((tog) => tog.classList.add('dark'));
    h3.forEach((tog) => tog.classList.add('dark'));
    h4.forEach((tog) => tog.classList.add('dark'));
    p.forEach((tog) => tog.classList.add('dark'));
    a.forEach((tog) => tog.classList.add('dark'));
    li.forEach((tog) => tog.classList.add('dark'));
    btn.forEach((tog) => tog.classList.add('dark'));
    serviceHead.forEach((tog) => tog.classList.add('dark'));
    servicePara.forEach((tog) => tog.classList.add('dark'));
    stepList.forEach((tog) => tog.classList.add('dark'));
    testimonialBox.forEach((tog) => tog.classList.add('dark'));
    testPara.forEach((tog) => tog.classList.add('dark'));
    unfilled.forEach((tog) => tog.classList.add('dark'));
  }
});

light_btn.addEventListener('click', () => {
  document.querySelector('.light_mode').style.display = 'none';
  document.querySelector('.dark_mode').style.display = 'flex';
});

dark_btn.addEventListener('click', () => {
  document.querySelector('.light_mode').style.display = 'flex';
  document.querySelector('.dark_mode').style.display = 'none';
});
