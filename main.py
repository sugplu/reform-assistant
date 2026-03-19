<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Ask Reform California</title>
  <style>
    :root {
      --ink-950: #07111d;
      --ink-900: #0d1b2c;
      --ink-800: #132741;
      --blue-700: #1d5fbe;
      --blue-600: #2f76dc;
      --blue-100: #e8f1ff;
      --gold-500: #e7b82f;
      --gold-300: #f6d97c;
      --stone-900: #182230;
      --stone-700: #344054;
      --stone-500: #667085;
      --stone-300: #d0d5dd;
      --stone-200: #eaecf0;
      --stone-100: #f5f7fa;
      --white: #ffffff;
      --danger-bg: #fef3f2;
      --danger-border: #fecdca;
      --danger-text: #b42318;
      --shadow-xl: 0 28px 80px rgba(7, 17, 29, 0.16);
      --shadow-lg: 0 16px 40px rgba(7, 17, 29, 0.09);
      --shadow-md: 0 8px 20px rgba(7, 17, 29, 0.06);
      --radius-2xl: 32px;
      --radius-xl: 24px;
      --radius-lg: 18px;
      --radius-md: 14px;
      --radius-sm: 10px;
    }

    * {
      box-sizing: border-box;
    }

    html, body {
      margin: 0;
      min-height: 100%;
      font-family: Georgia, "Times New Roman", serif;
      background:
        radial-gradient(circle at top left, rgba(246, 217, 124, 0.22), transparent 24%),
        linear-gradient(180deg, #eef3f8 0%, #f8fafc 42%, #edf2f7 100%);
      color: var(--stone-900);
    }

    body {
      padding: 22px;
    }

    .app {
      width: min(100%, 1180px);
      min-height: calc(100vh - 44px);
      margin: 0 auto;
      display: grid;
      grid-template-columns: 320px minmax(0, 1fr);
      background: rgba(255, 255, 255, 0.92);
      border: 1px solid rgba(255, 255, 255, 0.72);
      border-radius: var(--radius-2xl);
      overflow: hidden;
      box-shadow: var(--shadow-xl);
      backdrop-filter: blur(12px);
    }

    .sidebar {
      position: relative;
      padding: 28px 24px;
      background:
        linear-gradient(180deg, rgba(7, 17, 29, 0.98), rgba(19, 39, 65, 0.96)),
        linear-gradient(180deg, var(--ink-950), var(--ink-800));
      color: var(--white);
      display: flex;
      flex-direction: column;
      gap: 24px;
    }

    .sidebar::after {
      content: "";
      position: absolute;
      inset: auto -60px -80px auto;
      width: 220px;
      height: 220px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(246, 217, 124, 0.18), rgba(246, 217, 124, 0));
      pointer-events: none;
    }

    .brand {
      position: relative;
      z-index: 1;
      display: flex;
      gap: 14px;
      align-items: center;
    }

    .brand-mark {
      width: 56px;
      height: 56px;
      border-radius: 18px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: linear-gradient(135deg, var(--gold-300), var(--gold-500));
      color: var(--ink-900);
      font-family: "Segoe UI", sans-serif;
      font-size: 20px;
      font-weight: 800;
      box-shadow: 0 14px 28px rgba(231, 184, 47, 0.28);
      flex: 0 0 auto;
    }

    .brand-copy h1 {
      margin: 0;
      font-family: "Segoe UI", sans-serif;
      font-size: 20px;
      line-height: 1.15;
      letter-spacing: -0.02em;
    }

    .brand-copy p {
      margin: 4px 0 0;
      color: rgba(255, 255, 255, 0.78);
      font-family: "Segoe UI", sans-serif;
      font-size: 13px;
      line-height: 1.45;
    }

    .status-card,
    .sidebar-card {
      position: relative;
      z-index: 1;
      border-radius: var(--radius-xl);
      border: 1px solid rgba(255, 255, 255, 0.12);
      background: rgba(255, 255, 255, 0.06);
      padding: 18px;
      backdrop-filter: blur(8px);
    }

    .status-top {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 10px;
      font-family: "Segoe UI", sans-serif;
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.09em;
      color: rgba(255, 255, 255, 0.72);
    }

    .pulse {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #4ade80;
      box-shadow: 0 0 18px rgba(74, 222, 128, 0.7);
      position: relative;
    }

    .pulse::after {
      content: "";
      position: absolute;
      inset: -7px;
      border-radius: 50%;
      border: 1px solid rgba(74, 222, 128, 0.4);
      animation: ping 1.7s infinite;
    }

    @keyframes ping {
      0% { transform: scale(0.75); opacity: 1; }
      100% { transform: scale(1.7); opacity: 0; }
    }

    .status-card h2,
    .sidebar-card h3 {
      margin: 0;
      font-size: 22px;
      line-height: 1.1;
      letter-spacing: -0.03em;
    }

    .status-card p,
    .sidebar-card p {
      margin: 10px 0 0;
      color: rgba(255, 255, 255, 0.82);
      font-size: 14px;
      line-height: 1.65;
    }

    .sidebar-links {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-top: 14px;
    }

    .sidebar-link {
      display: inline-flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      text-decoration: none;
      color: var(--white);
      font-family: "Segoe UI", sans-serif;
      font-size: 13px;
      font-weight: 700;
      padding: 12px 14px;
      border-radius: 14px;
      border: 1px solid rgba(255, 255, 255, 0.10);
      background: rgba(255, 255, 255, 0.05);
      transition: background 0.18s ease, transform 0.18s ease, border-color 0.18s ease;
    }

    .sidebar-link:hover {
      transform: translateX(2px);
      background: rgba(255, 255, 255, 0.09);
      border-color: rgba(255, 255, 255, 0.18);
    }

    .sidebar-meta {
      margin-top: auto;
      position: relative;
      z-index: 1;
      color: rgba(255, 255, 255, 0.64);
      font-family: "Segoe UI", sans-serif;
      font-size: 12px;
      line-height: 1.6;
    }

    .main {
      min-width: 0;
      display: grid;
      grid-template-rows: auto 1fr auto;
      background:
        linear-gradient(180deg, rgba(248, 250, 252, 0.78), rgba(255, 255, 255, 0.96));
    }

    .main-top {
      padding: 24px 28px 18px;
      border-bottom: 1px solid rgba(208, 213, 221, 0.7);
      background: rgba(255, 255, 255, 0.72);
      backdrop-filter: blur(10px);
    }

    .main-top h2 {
      margin: 0;
      font-family: "Segoe UI", sans-serif;
      font-size: 18px;
      letter-spacing: -0.02em;
      color: var(--stone-900);
    }

    .main-top p {
      margin: 6px 0 0;
      font-family: "Segoe UI", sans-serif;
      font-size: 13px;
      color: var(--stone-500);
      line-height: 1.55;
    }

    .chat-scroll {
      min-height: 0;
      overflow-y: auto;
      padding: 22px 28px 24px;
      scroll-behavior: smooth;
    }

    .chat-scroll::-webkit-scrollbar {
      width: 10px;
    }

    .chat-scroll::-webkit-scrollbar-thumb {
      background: rgba(19, 39, 65, 0.14);
      border-radius: 999px;
      border: 2px solid transparent;
      background-clip: padding-box;
    }

    .welcome {
      margin-bottom: 20px;
      border-radius: var(--radius-xl);
      background:
        radial-gradient(circle at top right, rgba(246, 217, 124, 0.16), transparent 30%),
        linear-gradient(135deg, #ffffff, #edf4fb);
      border: 1px solid #dce8f6;
      box-shadow: var(--shadow-md);
      overflow: hidden;
    }

    .welcome-inner {
      padding: 24px;
    }

    .welcome-kicker {
      margin: 0 0 10px;
      font-family: "Segoe UI", sans-serif;
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--blue-700);
    }

    .welcome h3 {
      margin: 0;
      font-size: 32px;
      line-height: 1.02;
      letter-spacing: -0.04em;
      color: var(--ink-900);
    }

    .welcome p {
      margin: 12px 0 0;
      max-width: 700px;
      font-size: 16px;
      line-height: 1.7;
      color: var(--stone-700);
    }

    .question-row {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 18px;
    }

    .question-chip {
      appearance: none;
      border: 1px solid #d8e4f4;
      background: rgba(255, 255, 255, 0.9);
      color: var(--ink-800);
      padding: 10px 14px;
      border-radius: 999px;
      font-family: "Segoe UI", sans-serif;
      font-size: 12.5px;
      font-weight: 700;
      cursor: pointer;
      transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
    }

    .question-chip:hover {
      transform: translateY(-1px);
      border-color: #b7d1f4;
      box-shadow: 0 8px 18px rgba(16, 24, 40, 0.06);
    }

    .message-list {
      display: flex;
      flex-direction: column;
      gap: 18px;
    }

    .message-row {
      display: flex;
      gap: 12px;
      align-items: flex-end;
      animation: fadeUp 0.25s ease;
    }

    .message-row.user {
      flex-direction: row-reverse;
    }

    @keyframes fadeUp {
      from {
        opacity: 0;
        transform: translateY(10px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .avatar {
      width: 42px;
      height: 42px;
      border-radius: 14px;
      flex: 0 0 auto;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: "Segoe UI", sans-serif;
      font-size: 13px;
      font-weight: 800;
      box-shadow: 0 10px 22px rgba(16, 24, 40, 0.08);
    }

    .avatar.assistant {
      background: linear-gradient(135deg, var(--ink-900), var(--blue-700));
      color: var(--gold-300);
    }

    .avatar.user {
      background: linear-gradient(135deg, #ffffff, #ecf2f8);
      color: var(--stone-700);
      border: 1px solid #dde6ef;
    }

    .message-stack {
      max-width: min(78%, 760px);
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .message-row.user .message-stack {
      align-items: flex-end;
    }

    .message-label {
      padding: 0 4px;
      color: var(--stone-500);
      font-family: "Segoe UI", sans-serif;
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.02em;
    }

    .bubble {
      padding: 15px 17px;
      border-radius: 20px;
      font-family: "Segoe UI", sans-serif;
      font-size: 14px;
      line-height: 1.72;
      word-break: break-word;
    }

    .bubble.assistant {
      background: rgba(255, 255, 255, 0.96);
      border: 1px solid #e4ebf3;
      border-bottom-left-radius: 7px;
      color: var(--stone-900);
      box-shadow: var(--shadow-md);
    }

    .bubble.user {
      background: linear-gradient(135deg, var(--blue-700), var(--blue-600));
      color: var(--white);
      border-bottom-right-radius: 7px;
      box-shadow: 0 14px 28px rgba(31, 95, 191, 0.2);
    }

    .bubble p { margin: 0; }
    .bubble p + p { margin-top: 10px; }
    .bubble ul, .bubble ol { margin: 8px 0 0; padding-left: 20px; }
    .bubble li + li { margin-top: 4px; }

    .bubble a {
      color: var(--blue-700);
      font-weight: 700;
      text-decoration-thickness: 1.5px;
      text-underline-offset: 2px;
    }

    .bubble.user a {
      color: #e8f2ff;
    }

    .typing {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 1px;
    }

    .typing span {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #98a2b3;
      animation: bounce 1s infinite ease-in-out;
    }

    .typing span:nth-child(2) { animation-delay: 0.12s; }
    .typing span:nth-child(3) { animation-delay: 0.24s; }

    @keyframes bounce {
      0%, 80%, 100% { transform: translateY(0); opacity: 0.55; }
      40% { transform: translateY(-6px); opacity: 1; }
    }

    .error-banner {
      padding: 12px 14px;
      border-radius: var(--radius-md);
      border: 1px solid var(--danger-border);
      background: var(--danger-bg);
      color: var(--danger-text);
      font-family: "Segoe UI", sans-serif;
      font-size: 13px;
      line-height: 1.5;
    }

    .composer {
      padding: 20px 24px 24px;
      border-top: 1px solid rgba(208, 213, 221, 0.75);
      background: rgba(255, 255, 255, 0.82);
      backdrop-filter: blur(12px);
    }

    .composer-shell {
      display: flex;
      gap: 12px;
      align-items: flex-end;
    }

    .composer-input {
      flex: 1;
      display: flex;
      align-items: flex-end;
      gap: 10px;
      padding: 12px 14px;
      border-radius: 22px;
      border: 1px solid #d8e3ef;
      background: linear-gradient(180deg, #ffffff, #f9fbfd);
      box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.8);
      transition: border-color 0.18s ease, box-shadow 0.18s ease;
    }

    .composer-input:focus-within {
      border-color: #a2c5fb;
      box-shadow: 0 0 0 4px rgba(47, 118, 220, 0.12);
    }

    .composer-icon {
      width: 36px;
      height: 36px;
      border-radius: 13px;
      flex: 0 0 auto;
      display: flex;
      align-items: center;
      justify-content: center;
      background: linear-gradient(135deg, rgba(29, 95, 190, 0.12), rgba(231, 184, 47, 0.16));
      color: var(--ink-900);
      font-family: "Segoe UI", sans-serif;
      font-size: 16px;
      font-weight: 800;
    }

    textarea {
      width: 100%;
      resize: none;
      border: 0;
      outline: 0;
      background: transparent;
      color: var(--stone-900);
      font: inherit;
      font-family: "Segoe UI", sans-serif;
      font-size: 14px;
      line-height: 1.55;
      max-height: 150px;
      min-height: 24px;
    }

    textarea::placeholder {
      color: #98a2b3;
    }

    .send-btn {
      width: 56px;
      height: 56px;
      border: 0;
      border-radius: 20px;
      flex: 0 0 auto;
      cursor: pointer;
      color: var(--white);
      background: linear-gradient(135deg, var(--ink-900), var(--blue-700));
      box-shadow: 0 18px 30px rgba(31, 95, 191, 0.22);
      transition: transform 0.18s ease, box-shadow 0.18s ease, opacity 0.18s ease;
    }

    .send-btn:hover:not(:disabled) {
      transform: translateY(-2px);
      box-shadow: 0 22px 34px rgba(31, 95, 191, 0.28);
    }

    .send-btn:disabled {
      opacity: 0.55;
      box-shadow: none;
      cursor: not-allowed;
    }

    .send-btn svg {
      width: 20px;
      height: 20px;
    }

    .composer-meta {
      margin-top: 10px;
      display: flex;
      justify-content: space-between;
      gap: 12px;
      color: var(--stone-500);
      font-family: "Segoe UI", sans-serif;
      font-size: 12px;
      line-height: 1.45;
    }

    .composer-meta a {
      color: var(--blue-700);
      font-weight: 700;
      text-decoration: none;
    }

    .composer-meta a:hover {
      text-decoration: underline;
    }

    @media (max-width: 980px) {
      body {
        padding: 0;
      }

      .app {
        width: 100%;
        min-height: 100vh;
        border-radius: 0;
        grid-template-columns: 1fr;
      }

      .sidebar {
        gap: 18px;
      }

      .sidebar-meta {
        margin-top: 0;
      }
    }

    @media (max-width: 680px) {
      .topbar,
      .main-top,
      .chat-scroll,
      .composer {
        padding-left: 16px;
        padding-right: 16px;
      }

      .welcome-inner {
        padding: 18px;
      }

      .welcome h3 {
        font-size: 25px;
      }

      .message-stack {
        max-width: 88%;
      }

      .composer-meta {
        flex-direction: column;
      }
    }
  </style>
</head>
<body>
  <div class="app">
    <aside class="sidebar">
      <div class="brand">
        <div class="brand-mark">RC</div>
        <div class="brand-copy">
          <h1>Ask Reform California</h1>
          <p>Official help, direct answers, and the right next step.</p>
        </div>
      </div>

      <section class="status-card">
        <div class="status-top">
          <span class="pulse"></span>
          <span>Live Assistant</span>
        </div>
        <h2>Public information, without the runaround.</h2>
        <p>
          Ask about petitions, volunteering, events, voter guides, donations,
          office details, or where to go next.
        </p>
      </section>

      <section class="sidebar-card">
        <h3>Useful Links</h3>
        <p>Open official pages directly here anytime.</p>
        <div class="sidebar-links">
          <a class="sidebar-link" href="https://reformcalifornia.org" target="_blank" rel="noopener noreferrer">
            <span>Main Website</span><span>↗</span>
          </a>
          <a class="sidebar-link" href="https://reformcalifornia.org/events" target="_blank" rel="noopener noreferrer">
            <span>Events</span><span>↗</span>
          </a>
          <a class="sidebar-link" href="https://reformcalifornia.org/volunteer" target="_blank" rel="noopener noreferrer">
            <span>Volunteer</span><span>↗</span>
          </a>
          <a class="sidebar-link" href="https://reformcalifornia.org/voter-guides" target="_blank" rel="noopener noreferrer">
            <span>Voter Guides</span><span>↗</span>
          </a>
        </div>
      </section>

      <div class="sidebar-meta">
        Reform California<br />
        Hotline: <a href="tel:6193547257" style="color:#fff;text-decoration:none;font-weight:700;">619-354-7257</a>
      </div>
    </aside>

    <section class="main">
      <div class="main-top">
        <h2>Conversation</h2>
        <p>Ask a straightforward question and the assistant will respond with the clearest answer it can provide.</p>
      </div>

      <div class="chat-scroll" id="chatArea">
        <div class="welcome" id="welcomeCard">
          <div class="welcome-inner">
            <div class="welcome-kicker">Reform California</div>
            <h3>Find the page, process, or answer you actually need.</h3>
            <p>
              Ask naturally. For example: “How do I sign the petition?”, “Where is the voter guide?”,
              “Can I volunteer from home?”, or “What are the office hours?”
            </p>
            <div class="question-row" id="questionRow">
              <button class="question-chip" type="button" onclick="askQuick('How do I sign a petition?')">How do I sign a petition?</button>
              <button class="question-chip" type="button" onclick="askQuick('How can I volunteer with Reform California?')">How can I volunteer?</button>
              <button class="question-chip" type="button" onclick="askQuick('Where are upcoming events?')">Where are upcoming events?</button>
              <button class="question-chip" type="button" onclick="askQuick('Where can I find the voter guide?')">Where is the voter guide?</button>
            </div>
          </div>
        </div>

        <div class="message-list" id="messageList"></div>
      </div>

      <div class="composer">
        <div class="composer-shell">
          <div class="composer-input">
            <div class="composer-icon" id="composerIcon">RC</div>
            <textarea
              id="userInput"
              rows="1"
              placeholder="Ask your question here..."
              oninput="autoResize(this)"
              onkeydown="handleKey(event)"
            ></textarea>
          </div>

          <button class="send-btn" id="sendBtn" type="button" onclick="sendMessage()" aria-label="Send message">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M22 2L11 13"></path>
              <path d="M22 2L15 22L11 13L2 9L22 2Z"></path>
            </svg>
          </button>
        </div>

        <div class="composer-meta">
          <div>Official links and direct next steps are included when relevant.</div>
          <div>
            <a href="https://reformcalifornia.org" target="_blank" rel="noopener noreferrer">reformcalifornia.org</a>
            &nbsp;·&nbsp;
            <a href="tel:6193547257">619-354-7257</a>
          </div>
        </div>
      </div>
    </section>
  </div>

  <script>
    const chatArea = document.getElementById("chatArea");
    const messageList = document.getElementById("messageList");
    const userInput = document.getElementById("userInput");
    const sendBtn = document.getElementById("sendBtn");
    const composerIcon = document.getElementById("composerIcon");

    let conversationHistory = [];
    let isStreaming = false;

    function scrollBottom() {
      chatArea.scrollTop = chatArea.scrollHeight;
    }

    function autoResize(el) {
      el.style.height = "auto";
      el.style.height = Math.min(el.scrollHeight, 150) + "px";
    }

    function handleKey(event) {
      if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
      }
    }

    function askQuick(question) {
      userInput.value = question;
      sendMessage();
    }

    function clearWelcome() {
      document.getElementById("welcomeCard")?.remove();
    }

    function escapeHtml(text) {
      return text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");
    }

    function normalizeUrl(url) {
      if (!url) return url;
      let clean = url.trim().replace(/[),.;!?]+$/g, "");

      if (/^https?:\/\//i.test(clean)) return clean;
      if (/^www\./i.test(clean)) return "https://" + clean;
      if (/^[a-z0-9.-]+\.[a-z]{2,}(\/.*)?$/i.test(clean)) return "https://" + clean;

      return clean;
    }

    function formatText(text) {
      if (!text) return "";

      let safe = escapeHtml(text);

      safe = safe.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");

      safe = safe.replace(
        /\[([^\]]+)\]\((https?:\/\/[^\s)]+|www\.[^\s)]+|[a-z0-9.-]+\.[a-z]{2,}[^\s)]*)\)/gi,
        (_, label, url) => `<a href="${normalizeUrl(url)}" target="_blank" rel="noopener noreferrer">${label}</a>`
      );

      safe = safe.replace(
        /(^|[\s(>])((https?:\/\/[^\s<>"']+|www\.[^\s<>"']+|[a-z0-9.-]+\.[a-z]{2,}(\/[^\s<>"']*)?))/gi,
        (_, prefix, url) => `${prefix}<a href="${normalizeUrl(url)}" target="_blank" rel="noopener noreferrer">${url.replace(/[),.;!?]+$/g, "")}</a>`
      );

      safe = safe.replace(/^\d+\.\s(.+)$/gm, "<li>$1</li>");
      safe = safe.replace(/^[-•]\s(.+)$/gm, "<li>$1</li>");

      return safe
        .split(/\n{2,}/)
        .map((block) => {
          const trimmed = block.trim();
          if (!trimmed) return "";
          if (trimmed.includes("<li>")) return "<ul>" + trimmed + "</ul>";
          return "<p>" + trimmed.replace(/\n/g, "<br>") + "</p>";
        })
        .join("");
    }

    function createMessageRow(role, content = "") {
      const row = document.createElement("div");
      row.className = "message-row " + role;

      const avatar = document.createElement("div");
      avatar.className = "avatar " + (role === "assistant" ? "assistant" : "user");
      avatar.textContent = role === "assistant" ? "RC" : "You";

      const stack = document.createElement("div");
      stack.className = "message-stack";

      const label = document.createElement("div");
      label.className = "message-label";
      label.textContent = role === "assistant" ? "Reform California" : "You";

      const bubble = document.createElement("div");
      bubble.className = "bubble " + (role === "assistant" ? "assistant" : "user");
      bubble.innerHTML = formatText(content);

      stack.appendChild(label);
      stack.appendChild(bubble);
      row.appendChild(avatar);
      row.appendChild(stack);
      messageList.appendChild(row);

      scrollBottom();
      return bubble;
    }

    function addTyping() {
      composerIcon.textContent = "...";

      const row = document.createElement("div");
      row.className = "message-row assistant";
      row.id = "typingRow";

      const avatar = document.createElement("div");
      avatar.className = "avatar assistant";
      avatar.textContent = "RC";

      const stack = document.createElement("div");
      stack.className = "message-stack";

      const label = document.createElement("div");
      label.className = "message-label";
      label.textContent = "Reform California";

      const bubble = document.createElement("div");
      bubble.className = "bubble assistant";
      bubble.innerHTML = '<div class="typing"><span></span><span></span><span></span></div>';

      stack.appendChild(label);
      stack.appendChild(bubble);
      row.appendChild(avatar);
      row.appendChild(stack);
      messageList.appendChild(row);

      scrollBottom();
    }

    function removeTyping() {
      composerIcon.textContent = "RC";
      document.getElementById("typingRow")?.remove();
    }

    function showError(message) {
      const error = document.createElement("div");
      error.className = "error-banner";
      error.textContent = message;
      messageList.appendChild(error);
      scrollBottom();
    }

    async function sendMessage() {
      if (isStreaming) return;

      const text = userInput.value.trim();
      if (!text) return;

      clearWelcome();
      createMessageRow("user", text);
      conversationHistory.push({ role: "user", content: text });

      userInput.value = "";
      userInput.style.height = "auto";
      sendBtn.disabled = true;
      isStreaming = true;

      addTyping();

      let fullResponse = "";
      let responseBubble = null;

      try {
        const response = await fetch("/chat", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ messages: conversationHistory })
        });

        if (!response.ok || !response.body) {
          throw new Error("Server error");
        }

        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let buffer = "";
        let doneReceived = false;

        while (true) {
          const { done, value } = await reader.read();
          if (done) break;

          buffer += decoder.decode(value, { stream: true });
          const lines = buffer.split("\n");
          buffer = lines.pop() || "";

          for (const line of lines) {
            if (!line.startsWith("data: ")) continue;

            const payload = line.slice(6).trim();

            if (payload === "[DONE]") {
              doneReceived = true;
              break;
            }

            try {
              const parsed = JSON.parse(payload);

              if (parsed.error) {
                removeTyping();
                showError(parsed.error);
                doneReceived = true;
                break;
              }

              if (parsed.content) {
                removeTyping();
                if (!responseBubble) {
                  responseBubble = createMessageRow("assistant", "");
                }
                fullResponse += parsed.content;
                responseBubble.innerHTML = formatText(fullResponse);
                scrollBottom();
              }
            } catch (err) {
              console.error("Bad SSE payload", err);
            }
          }

          if (doneReceived) break;
        }

        if (fullResponse) {
          conversationHistory.push({ role: "assistant", content: fullResponse });
        }
      } catch (error) {
        removeTyping();
        showError("Connection issue. Please try again or call 619-354-7257.");
      } finally {
        isStreaming = false;
        sendBtn.disabled = false;
        userInput.focus();
      }
    }

    userInput.focus();
  </script>
</body>
</html>
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# ---------------------------------------------------------------------------
# Knowledge loading and retrieval
# ---------------------------------------------------------------------------
def load_knowledge_files() -> list[dict]:
    docs = []
    if not KNOWLEDGE_DIR.exists():
        logger.warning("knowledge directory not found at %s", KNOWLEDGE_DIR)
        return docs

    for file_path in sorted(KNOWLEDGE_DIR.iterdir()):
        if file_path.suffix.lower() not in {".txt", ".md"}:
            continue

        try:
            text = file_path.read_text(encoding="utf-8", errors="replace").strip()
            if text:
                docs.append({"name": file_path.name, "text": text})
                logger.info("Loaded knowledge file: %s (%s chars)", file_path.name, len(text))
        except Exception as exc:
            logger.warning("Could not read %s: %s", file_path.name, exc)

    return docs


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zA-Z0-9']+", text.lower())


def chunk_text(text: str, chunk_size: int = 1800, overlap: int = 200) -> list[str]:
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= text_length:
            break
        start += chunk_size - overlap

    return chunks


def build_knowledge_chunks(docs: list[dict]) -> list[dict]:
    chunks = []

    for doc in docs:
        for idx, chunk in enumerate(chunk_text(doc["text"])):
            lines = [line.strip() for line in chunk.splitlines() if line.strip()]
            heading = lines[0][:160] if lines else doc["name"]
            tokens = tokenize(chunk)

            chunks.append(
                {
                    "source": doc["name"],
                    "chunk_id": idx,
                    "heading": heading,
                    "text": chunk,
                    "search_text": chunk.lower(),
                    "tokens": tokens,
                    "token_counts": Counter(tokens),
                }
            )

    logger.info("Built %s knowledge chunks", len(chunks))
    return chunks


KNOWLEDGE_DOCS = load_knowledge_files()
KNOWLEDGE_CHUNKS = build_knowledge_chunks(KNOWLEDGE_DOCS)


def get_relevant_knowledge(query: str, max_chunks: int = 6, max_chars: int = 12000) -> str:
    if not query.strip() or not KNOWLEDGE_CHUNKS:
        return ""

    query_lower = query.lower().strip()
    query_tokens = tokenize(query)
    if not query_tokens:
        return ""

    query_counts = Counter(query_tokens)
    scored = []

    for item in KNOWLEDGE_CHUNKS:
        score = 0

        if query_lower in item["search_text"]:
            score += 200

        if query_lower in item["heading"].lower():
            score += 120

        phrase_parts = [p.strip() for p in re.split(r"[?.!,;:]", query_lower) if len(p.strip()) > 8]
        for phrase in phrase_parts:
            if phrase in item["search_text"]:
                score += 80

        for token, count in query_counts.items():
            if len(token) <= 2:
                continue
            token_hits = item["token_counts"].get(token, 0)
            score += min(token_hits, 5) * (8 + count)

        if score > 0:
            scored.append((score, item))

    scored.sort(key=lambda row: row[0], reverse=True)

    selected = []
    total_chars = 0
    seen = set()

    for score, item in scored:
        key = (item["source"], item["chunk_id"])
        if key in seen:
            continue

        formatted = (
            f"=== SOURCE: {item['source']} | SECTION: {item['heading']} | SCORE: {score} ===\n"
            f"{item['text']}"
        )

        if total_chars + len(formatted) > max_chars:
            break

        selected.append(formatted)
        seen.add(key)
        total_chars += len(formatted)

        if len(selected) >= max_chunks:
            break

    return "\n\n".join(selected)


# ---------------------------------------------------------------------------
# Live site fetcher
# ---------------------------------------------------------------------------
class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: List[str] = []
        self.skip_depth = 0
        self.skip_tags = {"script", "style", "nav", "footer", "head", "header"}

    def handle_starttag(self, tag, attrs):
        if tag in self.skip_tags:
            self.skip_depth += 1

    def handle_endtag(self, tag):
        if tag in self.skip_tags and self.skip_depth > 0:
            self.skip_depth -= 1

    def handle_data(self, data):
        if self.skip_depth == 0:
            cleaned = " ".join(data.split())
            if cleaned:
                self.parts.append(cleaned)

    def get_text(self) -> str:
        return " ".join(self.parts)


def fetch_page(url: str, max_chars: int = 1800) -> str:
    try:
        response = httpx.get(
            url,
            timeout=15,
            follow_redirects=True,
            headers={"User-Agent": "Mozilla/5.0 ReformCA-Assistant/1.0"},
        )
        response.raise_for_status()
        parser = TextExtractor()
        parser.feed(response.text)
        return parser.get_text()[:max_chars]
    except Exception as exc:
        logger.warning("Could not fetch %s: %s", url, exc)
        return ""


LIVE_PAGES = [
    ("Home", "https://reformcalifornia.org/"),
    ("Events", "https://reformcalifornia.org/events"),
    ("Campaigns", "https://reformcalifornia.org/campaigns"),
    ("Volunteer", "https://reformcalifornia.org/volunteer"),
    ("Voter Guides", "https://reformcalifornia.org/voter-guides"),
]

live_context = {
    "content": "",
    "last_updated": 0.0,
}


def refresh_live_context() -> None:
    logger.info("Refreshing live site content...")
    parts = []

    for label, url in LIVE_PAGES:
        text = fetch_page(url)
        if text:
            parts.append(f"[{label} - {url}]\n{text}")

    live_context["content"] = "\n\n".join(parts)
    live_context["last_updated"] = time.time()
    logger.info("Live content refreshed.")


def background_refresh(interval_seconds: int = 3600) -> None:
    while True:
        time.sleep(interval_seconds)
        refresh_live_context()


refresh_live_context()
threading.Thread(target=background_refresh, daemon=True).start()


# ---------------------------------------------------------------------------
# System prompt
# ---------------------------------------------------------------------------
BASE_SYSTEM_PROMPT = """
You are the official 24/7 public assistant for Reform California and Chairman Carl DeMaio.
Your role is to help supporters, voters, donors, and the public get accurate information
and take immediate action. You are knowledgeable, warm, professional, and action-oriented.
You speak on behalf of Reform California's team. You are not Carl himself.

RESPONSE RULES
1. Give the direct answer first.
2. Add the best link or contact.
3. Offer a clear next step or action.
4. Use numbered steps for multi-step processes.
5. Keep answers concise but complete.
6. Never invent facts, dates, endorsements, office details, petition details, or deadlines.
7. If a detail is uncertain or not verified, say so clearly and direct the user to the official source.

SOURCE PRIORITY
1. Official Reform California website and official public pages.
2. Relevant snippets from uploaded knowledge files.
3. Live fetched website content included in this prompt.
4. General public facts only when necessary and low risk.

ORGANIZATION OVERVIEW
Reform California is a grassroots political organization focused on:
- Taxpayer protection
- Public safety improvement
- Education reform and parental rights
- Election integrity

Three core priorities:
- Make California Affordable Again
- Make California Safe Again
- Make California Dream Again

KEY LINKS
Main website: https://reformcalifornia.org
Events / Town Halls: https://reformcalifornia.org/events
Volunteer signup: https://reformcalifornia.org/volunteer
Volunteer activities: https://reformcalifornia.org/volunteer-activities
Volunteer shifts: https://reformcalifornia.volunteershift.com/shifts?sort=soonest
All campaigns: https://reformcalifornia.org/campaigns
Election Integrity: https://reformcalifornia.org/campaigns/election-integrity-initiative
Block Rate Hikes: https://reformcalifornia.org/campaigns/block-the-rate-hikes
Voter guides: https://reformcalifornia.org/voter-guides
Statewide guide: https://reformcalifornia.org/voter-guides/california
Petition mail form: https://reformcalifornia.org/forms/volunteer-to-stop-the-savings-tax
Signature volunteer form: https://reformcalifornia.org/forms/election-integrity-signature-volunteer-sign-up
Voter registration: https://www.sos.ca.gov/elections/registration-status
Polling place lookup: https://www.sos.ca.gov/elections/polling-place
Ballot tracking: https://www.trackmyballot.org
Campaign finance: https://cal-access.sos.ca.gov/

CONTACT
Volunteer hotline: 619-354-7257
Volunteer email: volunteers@reformcalifornia.org
Walk-in office: 1320 W Valley Pkwy #304, Escondido CA 92029
Mailing address: Reform California, PO Box 27227, San Diego, CA 92198

PETITION RULES
- Always distinguish between an online interest form and an official ballot petition.
- Online form means interest/request only. It is not an official signature.
- Official ballot petitions require a physical wet signature.
- Do not claim petitions can be completed online unless the official site explicitly says so.
- Do not invent downloadable petition options.

ENDORSEMENTS
- Only reference officially published endorsements.
- Never speculate about endorsements.

EVENTS
- Do not invent event dates, venues, or schedules.
- Use official event pages or clearly say when the user should check the events page.

VOTER GUIDES
- If a race or candidate is missing, do not speculate.
- Say Reform California either did not endorse or did not publish guidance.

DONATIONS
- Direct donors to the official website.
- Do not provide tax or legal advice.

GUARDRAILS
- Never provide confidential, internal, or staff-only information.
- Do not speculate.
- Do not argue with users.
- No legal, tax, or campaign finance advice.
- If asked about something not verified, direct the user to the official source.

TONE
Professional, warm, clear, plain-language, and action-oriented.
Express appreciation when users want to volunteer, donate, or help.
""".strip()


def build_system_prompt(user_query: str) -> str:
    prompt = BASE_SYSTEM_PROMPT
    relevant_knowledge = get_relevant_knowledge(user_query)

    if relevant_knowledge:
        prompt += (
            "\n\n━━━ REQUIRED KNOWLEDGE SNIPPETS ━━━\n"
            "Answer from these snippets when they contain the answer. "
            "Do not ignore them. Do not contradict them. "
            "If the snippets answer the question, use them as the primary source.\n\n"
            f"{relevant_knowledge}"
        )
    else:
        prompt += (
            "\n\nNo relevant knowledge snippet was found. "
            "If the answer is not clearly available from official live site content, say you are not certain."
        )

    if live_context["content"]:
        age_minutes = int((time.time() - live_context["last_updated"]) / 60)
        prompt += (
            f"\n\n━━━ LIVE SITE CONTENT (refreshed {age_minutes} min ago) ━━━\n"
            "Use this for current website details only when needed.\n\n"
            f"{live_context['content'][:5000]}"
        )

    prompt += (
        "\n\nFINAL ACCURACY RULES\n"
        "- If the answer appears in the knowledge snippets, use that answer.\n"
        "- Do not replace a specific known answer with a vague summary.\n"
        "- Quote exact operational details like links, phone numbers, addresses, steps, and deadlines when present.\n"
        "- If the sources conflict, say so and send the user to the official page.\n"
    )

    return prompt


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------
class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


def normalize_messages(messages: List[Message]) -> List[dict]:
    allowed_roles = {"user", "assistant"}
    normalized = []

    for message in messages:
        role = message.role if message.role in allowed_roles else "user"
        normalized.append({"role": role, "content": message.content})

    return normalized


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
async def root():
    index_path = STATIC_DIR / "index.html"
    return HTMLResponse(index_path.read_text(encoding="utf-8"))


@app.get("/health")
async def health():
    age_minutes = int((time.time() - live_context["last_updated"]) / 60) if live_context["last_updated"] else None
    return {
        "status": "ok",
        "knowledge_files_loaded": len(KNOWLEDGE_DOCS),
        "knowledge_chunks_loaded": len(KNOWLEDGE_CHUNKS),
        "live_content_loaded": bool(live_context["content"]),
        "live_content_age_mins": age_minutes,
    }


@app.get("/debug-search")
async def debug_search(q: str):
    return {
        "query": q,
        "results": get_relevant_knowledge(q, max_chunks=3, max_chars=6000),
    }


@app.post("/chat")
async def chat(body: ChatRequest):
    messages = normalize_messages(body.messages)
    latest_user_message = next((m.content for m in reversed(body.messages) if m.role == "user"), "")
    system_prompt = build_system_prompt(latest_user_message)

    def generate():
        try:
            stream = client.chat.completions.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4o"),
                messages=[{"role": "system", "content": system_prompt}] + messages,
                stream=True,
                max_completion_tokens=int(os.getenv("MAX_TOKENS", "700")),
                temperature=float(os.getenv("TEMPERATURE", "0.1")),
            )

            for chunk in stream:
                delta = chunk.choices[0].delta
                if getattr(delta, "content", None):
                    yield f"data: {json.dumps({'content': delta.content})}\n\n"

            yield "data: [DONE]\n\n"
        except Exception as exc:
            logger.error("OpenAI error: %s", exc)
            yield f"data: {json.dumps({'error': 'Something went wrong. Please try again or call 619-354-7257.'})}\n\n"
            yield "data: [DONE]\n\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)

"- Always write full absolute links starting with https:// .\n"

