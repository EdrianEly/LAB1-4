const menuSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.menu');
    const menuLinks = document.querySelectorAll('.menu li');

    burger.addEventListener('click', () => {
        nav.classList.toggle('menu-active');
    });

}

menuSlide();