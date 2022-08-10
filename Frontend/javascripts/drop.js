const liner = document.querySelectorAll('.liner');

liner.forEach((line) => {
  line.addEventListener('click', () => {
    const faq = line.nextElementSibling;
    const icon = line.children[1];

    faq.classList.toggle('on');
    icon.classList.toggle('rotate');
  });
});
