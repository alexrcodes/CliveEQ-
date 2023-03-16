$(document).ready(function () {
    const chatbox = $("#chatbox");
    const inputForm = $("#input-form");
    const userInput = $("#user-input");
    const micButton = $("#mic-button");

    const synth = window.speechSynthesis;
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();

    function appendMessage(message, className) {
        const newMessage = $("<div>").text(message).addClass(className);
        chatbox.append(newMessage);
        chatbox.scrollTop(chatbox[0].scrollHeight);
    }

    function speak(text) {
        const utterance = new SpeechSynthesisUtterance(text);
        synth.speak(utterance);
    }

    inputForm.on("submit", function (event) {
        event.preventDefault();

        const message = userInput.val();
        userInput.val("");

        sendMessage(message);
    });

    function sendMessage(message) {
        appendMessage("You: " + message, "user-message");

        $.post("/api/conversation", { user_input: message }, function (data) {
            const response = data.response;
            appendMessage("EQ: " + response, "bot-message");
            speak(response);
        });
    }

    recognition.addEventListener('result', (event) => {
        const speech = event.results[0][0].transcript;
        sendMessage(speech);
    });

    micButton.on("click", function () {
        recognition.start();
    });
});
