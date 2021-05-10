(function() {
    // Set variables for DOM elements
    const email = document.getElementById('email');
    const flashCollection = document.getElementsByClassName('flash-container');
    const mainHeader = document.getElementById('main-header');
    const coreBannerTitle = document.getElementById('app-name');
    const coreHeading = document.getElementById('core-heading');

    // Focus on the email field of login/registration forms
    if (email) {
        email.focus();
    }

    // Remove flashed messages after timeout
    if (flashCollection) {
        setTimeout(() => {
            for (let el of flashCollection) {
                el.remove();
            }
        }, 4000);
    }

    // First check to see if the width is <= 700 to start with
    if (mainHeader && coreBannerTitle && coreHeading) {
        setBannerStyles(mainHeader, coreBannerTitle, coreHeading);  
    }

    // Allocate the new styles when the window size is reduced on a desktop
    window.addEventListener('resize', () => {
        if (mainHeader && coreBannerTitle && coreHeading) {
            setBannerStyles(mainHeader, coreBannerTitle, coreHeading);  
        }
    });

    // Render correct form fields
    const service = document.getElementById('service');
    renderFields(service, 'service');

    const plaintext = document.getElementById('plaintext');
    renderFields(plaintext, 'plaintext');

    /* Helper functions */

    // Update CSS classes
    function setClasses(el, toGo, toAdd) {
        el.classList.remove(toGo);
        el.classList.add(toAdd);
    }

    function addClass(elList, toAdd) {
        for (let el of elList) {
            el.classList.add(toAdd)
        }
    }

    function removeClass(elList, toGo) {
        for (let el of elList) {
            el.classList.remove(toGo)
        }
    }

    // Set styles for the banner on the core API page based on window width
    function setBannerStyles(mainHeader, coreBannerTitle, coreHeading) {
        const windowWidth = window.innerWidth;
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

    /* Helper functions for showing API options on the Core API page */

    // Get the appropriate DOM elements based on service type
    function getElements(type) {
        const labels = [];
        const options = [];
        const cases = [];
        switch (type) {
            case 'service':
                const encryptionLabel = document.getElementById('encryption-label');
                const encryptionOptions = document.getElementById('encryption');
                const hashLabel = document.getElementById('hashing-label');
                const hashOptions = document.getElementById('hashing');
                labels.push(encryptionLabel, hashLabel);
                options.push(encryptionOptions, hashOptions);
                cases.push('encrypt', 'hash');
                break;
            case 'plaintext':
                const textLabel = document.getElementById('text-label');
                const textOptions = document.getElementById('text');
                const fileLabel = document.getElementById('file-label');
                const fileOptions = document.getElementById('file_upload');
                labels.push(textLabel, fileLabel);
                options.push(textOptions, fileOptions);
                cases.push('text', 'file');
                break;
        }
        return { labels: labels, options: options, cases: cases };
    }

    // Make the unselected options 'invisible'
    function updateClasses(value, labels, options, cases) {
        switch (value) {
            case cases[0]:
                removeClass([labels[0], options[0]], 'invisible');
                addClass([labels[1], options[1]], 'invisible');
                break;
            case cases[1]:
                addClass([labels[0], options[0]], 'invisible');
                removeClass([labels[1], options[1]], 'invisible');
                break;
        }
    }

    // Render the correct form fields based on user choices
    function renderFields(el, type) {
        if (el) {
            el.addEventListener('click', () => {
                const value = el.value;
                const { labels, options, cases } = getElements(type);
                updateClasses(value, labels, options, cases);
            })
        }
    }
})();