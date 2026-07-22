import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# ----------------------------
# Load Environment Variables
# ----------------------------
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("GROQ_API_KEY not found in .env file")
    st.stop()

client = Groq(api_key=api_key)

# ----------------------------
# Streamlit Page Config
# ----------------------------
st.set_page_config(
    page_title="Groq AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Groq AI Chatbot")
st.write("Powered by Groq Llama Models")

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("Settings")

model = st.sidebar.selectbox(
    "Choose Model",
    [
        "llama-3.1-8b-instant",
        "llama-3.1-70b-versatile"
    ]
)

temperature = st.sidebar.slider(
    "Temperature",
    0.0,
    1.0,
    0.7
)

max_tokens = st.sidebar.slider(
    "Max Tokens",
    100,
    2048,
    1024
)

# ----------------------------
# Session State
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        }
    ]

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        }
    ]
    st.rerun()

# ----------------------------
# Display Chat History
# ----------------------------
for message in st.session_state.messages:

    # Don't display the system prompt
    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------
# User Input
# ----------------------------
prompt = st.chat_input("Ask me anything...")

if prompt:

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=st.session_state.messages,
                    temperature=temperature,
                    max_tokens=max_tokens
                )

                reply = response.choices[0].message.content

            except Exception as e:
                st.error(e)
                st.stop()

        st.markdown(reply)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )