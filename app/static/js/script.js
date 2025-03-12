document.addEventListener('DOMContentLoaded', () => {
    // Get elements
    const messagesContainer = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    
    // Store conversation history
    let messageHistory = [
        { role: "assistant", content: "Hello! I'm your AI assistant. How can I help you today?" }
    ];
    
    // Function to add a message to the UI
    function addMessageToUI(role, content) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', role);
        
        const contentDiv = document.createElement('div');
        contentDiv.classList.add('message-content');
        contentDiv.textContent = content;
        
        messageDiv.appendChild(contentDiv);
        messagesContainer.appendChild(messageDiv);
        
        // Scroll to bottom
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
    
    // Function to show typing indicator
    function showTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.classList.add('message', 'assistant', 'message-typing');
        typingDiv.id = 'typing-indicator';
        
        for (let i = 0; i < 3; i++) {
            const dot = document.createElement('div');
            dot.classList.add('dot');
            typingDiv.appendChild(dot);
        }
        
        messagesContainer.appendChild(typingDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
    
    // Function to hide typing indicator
    function hideTypingIndicator() {
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }
    
    // Function to send message to API
    async function sendMessage(message) {
        try {
            // Add message to history
            messageHistory.push({ role: "user", content: message });
            
            // Show typing indicator
            showTypingIndicator();
            
            // Send request to API
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    messages: messageHistory
                })
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            // Parse response
            const data = await response.json();
            
            // Hide typing indicator
            hideTypingIndicator();
            
            // Add AI response to UI and history
            addMessageToUI('assistant', data.response);
            messageHistory.push({ role: "assistant", content: data.response });
            
        } catch (error) {
            console.error('Error:', error);
            hideTypingIndicator();
            
            // Show error message
            addMessageToUI('assistant', "Sorry, I'm having trouble connecting. Please try again later.");
        }
    }
    
    // Handle send button click
    sendButton.addEventListener('click', () => {
        const message = userInput.value.trim();
        if (message) {
            addMessageToUI('user', message);
            sendMessage(message);
            userInput.value = '';
        }
    });
    
    // Handle Enter key
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            const message = userInput.value.trim();
            if (message) {
                addMessageToUI('user', message);
                sendMessage(message);
                userInput.value = '';
            }
        }
    });
    
    // Focus input on load
    userInput.focus();
});