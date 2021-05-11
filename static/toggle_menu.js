function toggleMenu(el) {
    el.classList.toggle("change");
    const menu = document.getElementsByClassName('menu-options-container');
    if (menu[0]) {
        menu[0].classList.toggle('invisible');
    }
}
