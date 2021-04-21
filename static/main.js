(function() {
    const email = document.getElementById('email');
    if (email) {
        email.focus();
    }

    const flashCollection = document.getElementsByClassName('flash-container');
    if (flashCollection) {
        setTimeout(() => {
            for (let el of flashCollection) {
                el.remove();
            }
        }, 4000);
    }

    const setClasses = (el, toGo, toAdd) => {
        el.classList.remove(toGo);
        el.classList.add(toAdd);
    }

    window.addEventListener('resize', () => {
        const windowWidth = window.innerWidth;
        const mainHeader = document.getElementById('main-header');
        const coreBannerTitle = document.getElementById('app-name');
        const coreHeading = document.getElementById('core-heading');
        
        if (mainHeader && coreBannerTitle && coreHeading) {
            if (windowWidth <= 700) {
                setClasses(mainHeader, 'main-header', 'main-header-resize');
                setClasses(coreBannerTitle, 'app-name-container', 'invisible');
                setClasses(coreHeading, 'invisible', 'form-heading');
            } else {
                setClasses(mainHeader, 'main-header-resize', 'main-header');
                setClasses(coreBannerTitle, 'invisible', 'app-name-container');
                setClasses(coreHeading, 'form-heading', 'invisible');
            }  
        }
    });
})();