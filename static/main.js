(function() {
    
    const flashCollection = document.getElementsByClassName('flash-container');

    // Remove flashed messages after timeout
    if (flashCollection) {
        setTimeout(() => {
            for (let el of flashCollection) {
                el.remove();
            }
        }, 4000);
    }

    updateBanner();
    updateHeading();
    
    window.addEventListener('resize', () => {
        updateBanner();
        updateHeading();
    });

    /* Helper functions */

    // Change the banner on resize
    function updateBanner() {
        const windowWidth = window.innerWidth;
        const appName = document.getElementsByClassName('app-name-container');
        if (appName[0]) {
            if (windowWidth <= 700) {
                appName[0].classList.add('invisible');
            } else {
                appName[0].classList.remove('invisible');
            }
        }
    }

    // Show or remove the page heading on resize
    function updateHeading() {
        const windowWidth = window.innerWidth;
        const coreHeading = document.getElementsByClassName('core-heading');
        if (coreHeading[0]) {
            if (windowWidth <= 700) {
                coreHeading[0].classList.remove('invisible');
            } else {
                coreHeading[0].classList.add('invisible');
            }
        }
    }
})();