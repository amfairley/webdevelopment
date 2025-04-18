document.addEventListener("DOMContentLoaded", function () {
    const dayButton = document.getElementById("day-mode");
    const nightButton = document.getElementById("night-mode");
    const modeToggleButton = document.getElementById(
        "day-mode-toggle-dropdown"
    );

    // Highlight JS CDN links
    const hightlightJsCDN = document.getElementById('highlightjscdn');

    // Set initial selected mode
    function setSelectedMode(mode) {
        if (mode === "<i class='fa-solid fa-sun'></i>") {
            dayButton.classList.add("active");
            nightButton.classList.remove("active");
            modeToggleButton.html = "<i class='fa-solid fa-sun'></i>";
            hightlightJsCDN.setAttribute('href', 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/default.min.css');
        } else {
            nightButton.classList.add("active");
            dayButton.classList.remove("active");
            modeToggleButton.html = "<i class='fa-solid fa-moon'></i>";
            hightlightJsCDN.setAttribute('href', 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/atom-one-dark.min.css');
        }
    }

    // Event listeners for changing modes
    dayButton.addEventListener("click", function () {
        document.body.classList.remove("night-mode");
        document.body.classList.add("day-mode");
        localStorage.setItem("theme", "day"); // Save preference
        setSelectedMode("<i class='fa-solid fa-sun'></i>");
        hightlightJsCDN.setAttribute('href', 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/default.min.css');
    });

    nightButton.addEventListener("click", function () {
        document.body.classList.remove("day-mode");
        document.body.classList.add("night-mode");
        localStorage.setItem("theme", "night"); // Save preference
        setSelectedMode("<i class='fa-solid fa-moon'></i>");
        hightlightJsCDN.setAttribute('href', 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/atom-one-dark.min.css');
    });

    // Initialize each page with the chosen mode
    const storedTheme = localStorage.getItem("theme");

    if (storedTheme === "night") {
        document.body.classList.add("night-mode");
        document.body.classList.remove("day-mode");
        setSelectedMode("<i class='fa-solid fa-moon'></i>");
        hightlightJsCDN.setAttribute('href', 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/atom-one-dark.min.css');
    } else {
        document.body.classList.add("day-mode");
        document.body.classList.remove("night-mode");
        setSelectedMode("<i class='fa-solid fa-sun'></i>");
        hightlightJsCDN.setAttribute('href', 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/default.min.css');
    }

    // Make navigation bar sticky when scrolled down
    const nav = document.getElementById("site-navigation");
    const footer = document.querySelector("footer");
    // Use height of top bar (6rem)
    const topOffset = 6 * parseFloat(
        getComputedStyle(document.documentElement).fontSize
    );
    const footerHeight = 0.1 * parseFloat(
        getComputedStyle(document.documentElement).fontSize
    );
    
    // Function to add sticky when scroling down
    window.onscroll = function () {
        if (window.scrollY > topOffset) {
            nav.classList.add("sticky");
        } else {
            nav.classList.remove("sticky");
        }
        // Add offset for footer
        if (
            window.innerHeight + window.scrollY >= 
            document.body.offsetHeight - footerHeight
        ) {
            nav.classList.add("footer");
        } else {
            nav.classList.remove("footer");
        }
    };
});