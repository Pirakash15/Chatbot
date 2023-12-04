const socket = new WebSocket('ws://localhost:8000/chat');

socket.onopen = function (event) {
    console.log('WebSocket connection opened:', event);
};

socket.onmessage = function (event) {
    const botMessage = event.data;
    appendBotMessage(botMessage);
};

socket.onclose = function (event) {
    console.log('WebSocket connection closed:', event);
};


function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendUserMessage(document.getElementById('user-input').value);
    }
}

function sendUserMessage(message) {
    const chatContainer = document.getElementById('chat-container');
    const userMessageElement = document.createElement('div');
    userMessageElement.className = 'chat-message user-message';
    userMessageElement.textContent = 'You: ' + message;
    chatContainer.appendChild(userMessageElement);

    // Send the user message to the server using WebSocket
    socket.send(message);
    scrollToBottom();
    // Clear the input field
    document.getElementById('user-input').value = '';
}

function appendBotMessage(message) {
    const chatContainer = document.getElementById('chat-container');
    const botMessageElement = document.createElement('div');
    botMessageElement.className = 'chat-message bot-message';
    botMessageElement.textContent = message;
    chatContainer.appendChild(botMessageElement);
    scrollToBottom();
}
function scrollToBottom() {
    const chatContainer = document.getElementById("chat-container");
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function openManual(folder) {
    fetch(`/open-manual/${folder}`)
        .then(response => response.json())
        .then(data => {
            const botMessageElement = document.createElement('div');
            botMessageElement.className = 'chat-message bot-message';
            botMessageElement.textContent = data.message;

            const chatContainer = document.getElementById('chat-container');
            chatContainer.appendChild(botMessageElement);
            scrollToBottom();
        })
        .catch(error => {
            console.error(`Error opening manual for ${folder}:`, error);
            alert(`Error opening manual for ${folder}. Check the console for details.`);
        });
}

function clearMessages() {
    fetch('/clear-messages', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            const clearedMessageSpan = document.getElementById('cleared-message');
            clearedMessageSpan.textContent = data.message;
            clearedMessageSpan.classList.add('show');

            // Delay before starting the fade-out animation and reloading the page
            setTimeout(() => {
                clearedMessageSpan.classList.add('fade-out');
                // Reload the page after a delay (adjust the time as needed)
                setTimeout(() => {
                    location.reload();
                }, 1000);
            }, 2000); // Adjust the delay time (in milliseconds) as needed
        })
        .catch(error => {
            console.error('Error clearing messages:', error);
            alert('Error clearing messages. Check the console for details.');
        });
}
