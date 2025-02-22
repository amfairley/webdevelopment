document.addEventListener("DOMContentLoaded", function () {
    const dayButton = document.getElementById("day-mode");
    const nightButton = document.getElementById("night-mode");
    const modeToggleButton = document.getElementById(
        "day-mode-toggle-dropdown"
    );

    // Set initial selected mode
    function setSelectedMode(mode) {
        if (mode === "<i class='fa-solid fa-sun'></i>") {
            dayButton.classList.add("active");
            nightButton.classList.remove("active");
            modeToggleButton.html = "<i class='fa-solid fa-sun'></i>";
        } else {
            nightButton.classList.add("active");
            dayButton.classList.remove("active");
            modeToggleButton.html = "<i class='fa-solid fa-moon'></i>";
        }
    }

    // Event listeners for changing modes
    dayButton.addEventListener("click", function () {
        document.body.classList.remove("night-mode");
        document.body.classList.add("day-mode");
        setSelectedMode("<i class='fa-solid fa-sun'></i>");
    });

    nightButton.addEventListener("click", function () {
        document.body.classList.remove("day-mode");
        document.body.classList.add("night-mode");
        setSelectedMode("<i class='fa-solid fa-moon'></i>");
    });

    // Initialize with the default selected mode
    if (document.body.classList.contains("night-mode")) {
        setSelectedMode("<i class='fa-solid fa-moon'></i>");
    } else {
        setSelectedMode("<i class='fa-solid fa-sun'></i>");
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