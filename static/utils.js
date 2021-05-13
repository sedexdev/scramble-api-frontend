function clearMenu() {
    const menuIcon = document.getElementsByClassName('menu-container');
    const menu = document.getElementsByClassName('menu-options-container');
    menuIcon[0].classList.remove('change');
    if (menu[0]) {
        menu[0].classList.add('invisible');
    }
}

function toggleMenu(el) {
    el.classList.toggle("change");
    const menu = document.getElementsByClassName('menu-options-container');
    if (menu[0]) {
        menu[0].classList.toggle('invisible');
    }
}

function showDeleteModal() {
    const screenBlock = document.getElementById('block-screen');
    const modal = document.getElementById('delete-modal');
    if (modal) {
        screenBlock.classList.add('cover-block');
        modal.classList.remove('invisible');
    }
}

function hideDeleteModal() {
    const screenBlock = document.getElementById('block-screen');
    const modal = document.getElementById('delete-modal');
    if (modal) {
        screenBlock.classList.remove('cover-block');
        modal.classList.add('invisible');
    }
}
