# Work 2: JavaScript Fundamentals

## Overview
Learning JavaScript basics and DOM manipulation.

## Key Features
- JavaScript core concepts
- DOM manipulation techniques
- Event handling
- Interactive web elements

## Technologies
- JavaScript
- DOM API
- Event Listeners

## Code Examples

### DOM Manipulation
```javascript
// Selecting elements
const header = document.querySelector('header');
const navLinks = document.querySelectorAll('nav a');
const mainContent = document.getElementById('main');

// Creating and adding elements
const newSection = document.createElement('section');
newSection.className = 'new-section';
newSection.innerHTML = `
    <h2>Dynamic Content</h2>
    <p>This section was created using JavaScript.</p>
`;
mainContent.appendChild(newSection);

// Event handling
navLinks.forEach(link => {
    link.addEventListener('click', (event) => {
        event.preventDefault();
        const targetId = link.getAttribute('href').slice(1);
        const targetSection = document.getElementById(targetId);
        targetSection.scrollIntoView({ behavior: 'smooth' });
    });
});
```

### Interactive Features
```javascript
// Counter example
let count = 0;
const counterDisplay = document.getElementById('counter');
const incrementBtn = document.getElementById('increment');
const decrementBtn = document.getElementById('decrement');

function updateCounter() {
    counterDisplay.textContent = count;
    // Add animation class
    counterDisplay.classList.add('updated');
    // Remove animation class after animation completes
    setTimeout(() => {
        counterDisplay.classList.remove('updated');
    }, 500);
}

incrementBtn.addEventListener('click', () => {
    count++;
    updateCounter();
});

decrementBtn.addEventListener('click', () => {
    count--;
    updateCounter();
});

// Toggle dark/light mode
const themeToggle = document.getElementById('theme-toggle');
themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    const isDarkMode = document.body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDarkMode);
}); 