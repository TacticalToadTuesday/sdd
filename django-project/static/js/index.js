function scrollToSection1() {
  const section1 = document.querySelector('#features-heading');
  window.scrollTo({
    top: section1.offsetTop,
    behavior: 'smooth'
  });
}