# Work 4: AJAX and Data Fetching

## Overview
Learning asynchronous programming and data fetching.

## Key Features
- AJAX implementation
- API integration
- Data handling
- Asynchronous operations

## Technologies
- AJAX
- Fetch API
- JSON
- Promises

## Code Examples

### Fetch API Example
```javascript
// Function to fetch user data
async function fetchUsers() {
    try {
        const response = await fetch('https://api.example.com/users');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        displayUsers(data);
    } catch (error) {
        console.error('Error fetching users:', error);
        showError('Failed to load users. Please try again later.');
    }
}

// Function to display users
function displayUsers(users) {
    const userList = document.getElementById('userList');
    userList.innerHTML = '';
    
    users.forEach(user => {
        const userElement = document.createElement('div');
        userElement.className = 'user-card';
        userElement.innerHTML = `
            <h3>${user.name}</h3>
            <p>Email: ${user.email}</p>
            <button onclick="loadUserDetails(${user.id})">View Details</button>
        `;
        userList.appendChild(userElement);
    });
}
```

### POST Request Example
```javascript
// Function to create a new user
async function createUser(userData) {
    const loadingSpinner = document.getElementById('loading');
    loadingSpinner.style.display = 'block';
    
    try {
        const response = await fetch('https://api.example.com/users', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + getToken()
            },
            body: JSON.stringify(userData)
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const result = await response.json();
        showSuccess('User created successfully!');
        return result;
        
    } catch (error) {
        console.error('Error creating user:', error);
        showError('Failed to create user. Please try again.');
        throw error;
    } finally {
        loadingSpinner.style.display = 'none';
    }
}

// Example usage with error handling
document.getElementById('createUserForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const userData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        role: document.getElementById('role').value
    };
    
    try {
        const newUser = await createUser(userData);
        console.log('New user created:', newUser);
        // Update UI or redirect
    } catch (error) {
        // Error already handled in createUser function
    }
}); 