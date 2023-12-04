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
}
function scrollToBottom() {
    const chatContainer = document.getElementById("chat-container");
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function openManual(folder) {
    // You can customize this function to open the corresponding folder
    alert('Opening folder: ' + folder);
}