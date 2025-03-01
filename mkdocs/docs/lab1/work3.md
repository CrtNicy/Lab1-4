# Work 3: Form Validation

## Overview
Implementing form validation and user interaction.

## Key Features
- Form input validation
- User feedback mechanisms
- Dynamic content updates
- Error handling

## Technologies
- JavaScript Forms API
- Regular Expressions
- Input Validation
- DOM Events

## Code Examples

### Form HTML Structure
```html
<form id="registrationForm" class="registration-form">
    <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <span class="error-message"></span>
    </div>
    
    <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <span class="error-message"></span>
    </div>
    
    <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <span class="error-message"></span>
    </div>
    
    <div class="form-group">
        <label for="confirmPassword">Confirm Password:</label>
        <input type="password" id="confirmPassword" name="confirmPassword" required>
        <span class="error-message"></span>
    </div>
    
    <button type="submit">Register</button>
</form>
```

### Form Validation JavaScript
```javascript
document.getElementById('registrationForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Reset error messages
    clearErrors();
    
    // Get form values
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    
    // Validation flags
    let isValid = true;
    
    // Username validation
    if (username.length < 3) {
        showError('username', 'Username must be at least 3 characters long');
        isValid = false;
    }
    
    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        showError('email', 'Please enter a valid email address');
        isValid = false;
    }
    
    // Password validation
    if (password.length < 8) {
        showError('password', 'Password must be at least 8 characters long');
        isValid = false;
    }
    
    // Confirm password
    if (password !== confirmPassword) {
        showError('confirmPassword', 'Passwords do not match');
        isValid = false;
    }
    
    // If valid, submit the form
    if (isValid) {
        // Show success message
        showSuccess();
        // Here you would typically send the data to a server
    }
});

function showError(fieldId, message) {
    const field = document.getElementById(fieldId);
    const errorSpan = field.nextElementSibling;
    errorSpan.textContent = message;
    field.classList.add('error');
}

function clearErrors() {
    const errorMessages = document.querySelectorAll('.error-message');
    const inputs = document.querySelectorAll('input');
    
    errorMessages.forEach(span => span.textContent = '');
    inputs.forEach(input => input.classList.remove('error'));
}

function showSuccess() {
    const form = document.getElementById('registrationForm');
    form.innerHTML = '<div class="success-message">Registration successful!</div>';
} 