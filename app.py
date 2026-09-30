import streamlit as st
import ollama

st.title("AI Chatbot")

# Store conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display conversation
for message in st.session_state.messages:
    if message["role"] == "user":
        st.write("You:", message["content"])
    else:
        st.write("AI:", message["content"])

# User input
text = st.text_input("Type your message")

if st.button("Send"):

    if text.strip().lower() == "exit":
        st.write("AI: Goodbye!")
        st.session_state.messages = []
        st.stop()

    # Show user's message
    st.session_state.messages.append({
        "role": "user",
        "content": text
    })

    # Send complete conversation to Ollama
    response = ollama.chat(
        model="llama3.2",
        messages=st.session_state.messages
    )

    ai_response = response["message"]["content"]

    # Store AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })

    # Refresh the page
    st.rerun()