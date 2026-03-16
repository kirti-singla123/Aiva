import { useState, useCallback } from "react";
import PlanetOrb from "./PlanetOrb";
import "../ChatPanel.css";

function ChatPanel() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  /* =========================
     🚀 SEND MESSAGE
  ========================== */
  const sendMessage = useCallback(
    async () => {
      const messageText = input;
      if (!messageText.trim()) return;

      const userMessage = { sender: "user", text: messageText };
      setMessages((prev) => [...prev, userMessage]);
      setInput("");
      setLoading(true);

      try {
        const response = await fetch("http://127.0.0.1:8000/chat/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ message: messageText }),
        });

        const data = await response.json();
        const aiMessage = { sender: "ai", text: data.response };
        setMessages((prev) => [...prev, aiMessage]);
      } catch (error) {
        setMessages((prev) => [
          ...prev,
          { sender: "ai", text: "⚠️ Error connecting to AI." },
        ]);
      }

      setLoading(false);
    },
    [input]
  );

  return (
    <div className="main-container">
      <div className="chat-container">
        {messages.length === 0 && (
          <div className="hero-section">
            <PlanetOrb />
            <h1 className="hero-text">How can I help you today?</h1>
          </div>
        )}

        {messages.length > 0 && (
          <div className="chat-messages">
            {messages.map((msg, index) => (
              <div key={index} className={`message ${msg.sender}`}>
                {msg.text}
              </div>
            ))}
            {loading && <div className="message ai">Thinking...</div>}
          </div>
        )}

        <div className="chat-input">
          <input
            type="text"
            placeholder="Ask me anything..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") sendMessage();
            }}
          />

          <button className="send-btn" onClick={sendMessage}>
            ➤
          </button>
        </div>
      </div>
    </div>
  );
}

export default ChatPanel;