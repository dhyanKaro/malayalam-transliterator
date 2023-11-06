const inputArea = document.getElementById("inputText");
const outputArea = document.getElementById("outputText");
const darkModeButton = document.querySelector('.dark-mode-button');

//copy
function copyFunction() {
    outputArea.select();
    outputArea.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(outputArea.value);
}

//clear
function clearFunction() {
    inputArea.value = "";
    outputArea.value = "";
}


//dark-mode
function toggleDarkMode() {
    const body = document.body;
    const navbar = document.querySelector('.navbar');
    const textAreas = document.querySelectorAll('.texty');
    const tools = document.querySelector('.tools');
    const buttons = document.querySelectorAll('.buttons'); // Add this line

    body.classList.toggle('dark-mode');
    navbar.classList.toggle('dark-mode');
    tools.classList.toggle('dark-mode');

    textAreas.forEach((textarea) => {
        textarea.classList.toggle('dark-mode');
    });

    buttons.forEach((button) => {
        button.classList.toggle('dark-mode');
    });
}


// Listen for changes in the system's color scheme
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
    const newColorScheme = e.matches ? "dark" : "light";
    if (newColorScheme === 'dark') {
        toggleDarkMode();
    }
});


// Check the system's color scheme when the page loads
if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    toggleDarkMode();
}