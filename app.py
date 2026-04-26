import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ── PAGE SETUP ──────────────────────────────────────────
st.title("My AI Chatbot 🤖")
st.caption("Powered by Groq + Llama 3")

# ── SIDEBAR ─────────────────────────────────────────────
st.sidebar.title("Settings")

# Feature 1 — Model Selector
model = st.sidebar.selectbox(
    "Choose AI Model",
    options=[
        "llama-3.1-8b-instant",
        "llama-3.3-70b-versatile"
    ],
    help="8b is faster. 70b is smarter but slightly slower."
)

# Feature 2 — System Prompt Input
system_prompt = st.sidebar.text_area(
    "Customize AI Personality",
    value="You are a helpful AI assistant.",
    height=120,
    help="Change this to give the AI a different personality."
)

# Feature 3 — Clear Chat Button
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = [
        {"role": "system", "content": system_prompt}
    ]
    st.rerun()

# ── SESSION STATE ────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt}
    ]

# ── DISPLAY CHAT HISTORY ─────────────────────────────────
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# ── CHAT INPUT ───────────────────────────────────────────
if prompt := st.chat_input("Ask me anything..."):

    st.session_state.messages[0] = {
        "role": "system",
        "content": system_prompt
    }

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model=model,
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.write(reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })
