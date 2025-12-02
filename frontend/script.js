async function init() {
    await loadChat()
}

const fetchURL = "http://127.0.0.1:8000/chat_app/";

async function loadChat() {
    const chat = await fetch(fetchURL);
    const chatToJson = await chat.json();
    render(chatToJson)
}

function render(chats) {
    const chat_history = document.getElementById("chat-history");
    chat_history.innerHTML = "";
    chats.forEach(item => {
        chat_history.innerHTML += `
        <p>${item.first_name} ${item.last_name}</p> 
        <p>${item.created_at}</p>
        <p>${item.message}</p>
        <button onclick="deleteChat(${item.id})">X</button>
        <br>
        <br>
    `;
    });
}

function getCookie(name) {
    return document.cookie.split('; ')
        .find(row => row.startsWith(name + '='))?.split('=')[1];
}

async function addChat() {
    const first_name = document.getElementById("first-name").value;
    const last_name = document.getElementById("last-name").value;
    const message = document.getElementById("message-input").value;
    const data = { first_name, last_name, message };
    console.log("Sending:", data);

    try {
        const response = await fetch(fetchURL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: JSON.stringify(data),
            credentials: "include",
        });

        document.getElementById("first-name").value = "";
        document.getElementById("last-name").value = "";
        document.getElementById("message-input").value = "";
    } catch (error) {
        console.error("POST failed:", error);
    }
}

async function deleteChat(chatId) {
    console.log("deleted ID", chatId);
    try {
        const response = await fetch(`${fetchURL}${chatId}/`, {
            method: "DELETE",
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            },
            credentials: "include"
        });

        const chats = await fetch(fetchURL).then(r => r.json());
        render(chats);
    } catch (error) {
        console.error("DEL failed:", error);
    }
}