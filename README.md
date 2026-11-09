# 🤖 AI Chatbot

A multi-turn chatbot that remembers the whole conversation, lets you switch between a fast and a large model, and lets you change the assistant's personality with your own system prompt.

**Live demo:** https://ai-chatbot-afxr5bankg8nzzigdwqkzo.streamlit.app/

## Features
- **Conversation memory** – the full chat history is sent with every message (Streamlit session state)
- **Model switching** – `openai/gpt-oss-20b` (fast) or `openai/gpt-oss-120b` (smarter), served by Groq
- **Custom personality** – edit the system prompt in the sidebar
- **Clear chat** button to start over

## Tech stack
Python · Groq API · GPT-OSS models · Streamlit · Streamlit Community Cloud

## Run it locally

```bash
git clone https://github.com/Harshamaringanti48/ai-chatbot.git
cd ai-chatbot
pip install -r requirements.txt
```

Create `.streamlit/secrets.toml` with your free key from [console.groq.com](https://console.groq.com):

```toml
GROQ_API_KEY = "your-key-here"
```

Then run:

```bash
streamlit run app.py
```

## Maintenance log
- **Nov 2026** – Groq retired Llama 3.1 (8B) and Llama 3.3 (70B). Migrated the app to GPT-OSS-20B and GPT-OSS-120B.
- Fixed 7+ deployment and API errors since launch, including API deprecations.
