// Google Sign-In
function googleLogin() {
    window.location.href = '/auth/google-login';
}

// Login Form Submission
document.getElementById('login-form')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    try {
        const response = await fetch('/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });
        const data = await response.json();
        if (response.ok) {
            alert('Login successful!');
            window.location.href = '/';
        } else {
            alert(data.error || `Login failed (HTTP ${response.status})`);
        }
    } catch (error) {
        alert('Network error. Check console for details.');
        console.error('Error:', error);
    }
});

// Register Form Submission
document.getElementById('register-form')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    try {
        const response = await fetch('/auth/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });
        const data = await response.json();
        if (response.ok) {
            alert('Registration successful!');
            window.location.href = '/login';
        } else {
            alert(data.error || `Registration failed (HTTP ${response.status})`);
        }
    } catch (error) {
        alert('Network error. Check console for details.');
        console.error('Error:', error);
    }
});

// Send Message Form Submission
document.getElementById('message-form')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const message = document.getElementById('message-input').value;
    try {
        const response = await fetch('/chat/send', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                sender_id: 'user1',  // Replace with actual sender ID
                receiver_id: 'user2',  // Replace with actual receiver ID
                message
            })
        });
        const data = await response.json();
        if (response.ok) {
            document.getElementById('message-input').value = '';  // Clear input
            loadMessages();  // Reload messages
        } else {
            alert(data.error || 'Failed to send message');
        }
    } catch (error) {
        console.error('Error:', error);
    }
});

// Load Messages
async function loadMessages() {
    try {
        const response = await fetch('/chat/messages/user1/user2');  // Replace with actual IDs
        const messages = await response.json();
        const messagesContainer = document.getElementById('messages');
        messagesContainer.innerHTML = '';  // Clear previous messages
        for (const [messageId, messageData] of Object.entries(messages)) {
            const messageElement = document.createElement('div');
            messageElement.textContent = `${messageData.message} (${new Date(messageData.timestamp).toLocaleString()})`;
            messagesContainer.appendChild(messageElement);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

// Load messages on page load
if (window.location.pathname === '/') {
    loadMessages();
}