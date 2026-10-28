(() => {
  const form = document.getElementById("chat-form");
  const input = document.getElementById("message-input");
  const messages = document.getElementById("chat-messages");
  const sendButton = document.getElementById("send-button");
  const clearButton = document.getElementById("clear-chat");
  const suggestionList = document.getElementById("suggestion-list");

  const initialGreeting = "Hello! 👋 I'm the hospital FAQ assistant. I can help with common questions about appointments, opening hours, facilities, and more. What would you like to know?";

  function timeLabel() {
    return new Intl.DateTimeFormat([], { hour: "numeric", minute: "2-digit" }).format(new Date());
  }

  function addMessage(text, who) {
    const row = document.createElement("div");
    row.className = `message-row ${who === "user" ? "user-row" : "bot-row"}`;

    const avatar = document.createElement("div");
    avatar.className = "message-avatar";
    avatar.setAttribute("aria-hidden", "true");
    avatar.textContent = who === "user" ? "You" : "✚";

    const content = document.createElement("div");
    content.className = "message-content";
    const meta = document.createElement("div");
    meta.className = "message-meta";
    const name = document.createElement("strong");
    name.textContent = who === "user" ? "You" : "CareDesk Assistant";
    const time = document.createElement("span");
    time.textContent = timeLabel();
    meta.append(name, time);

    const bubble = document.createElement("div");
    bubble.className = `bubble ${who === "user" ? "user-bubble" : "bot-bubble"}`;
    // textContent prevents user-supplied HTML from being interpreted as markup.
    bubble.textContent = text;

    content.append(meta, bubble);
    row.append(avatar, content);
    messages.append(row);
    messages.scrollTop = messages.scrollHeight;
    return row;
  }

  function addTyping() {
    const row = document.createElement("div");
    row.className = "message-row bot-row";
    row.id = "typing-indicator";
    const avatar = document.createElement("div");
    avatar.className = "message-avatar";
    avatar.textContent = "✚";
    const bubble = document.createElement("div");
    bubble.className = "bubble bot-bubble typing";
    bubble.setAttribute("aria-label", "Assistant is typing");
    for (let i = 0; i < 3; i++) bubble.append(document.createElement("span"));
    row.append(avatar, bubble);
    messages.append(row);
    messages.scrollTop = messages.scrollHeight;
  }

  async function sendMessage(rawText) {
    const message = rawText.trim();
    if (!message || sendButton.disabled) return;
    addMessage(message, "user");
    input.value = "";
    sendButton.disabled = true;
    input.disabled = true;
    addTyping();
    try {
      const response = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.error || "Something went wrong. Please try again.");
      addMessage(data.reply, "bot");
    } catch (error) {
      addMessage(error.message || "Unable to connect to the assistant. Please try again.", "bot");
    } finally {
      document.getElementById("typing-indicator")?.remove();
      sendButton.disabled = false;
      input.disabled = false;
      input.focus();
    }
  }

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    sendMessage(input.value);
  });

  suggestionList.addEventListener("click", (event) => {
    const button = event.target.closest("[data-question]");
    if (button) sendMessage(button.dataset.question);
  });

  clearButton.addEventListener("click", () => {
    messages.replaceChildren();
    addMessage(initialGreeting, "bot");
    input.focus();
  });
})();