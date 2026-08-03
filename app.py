import streamlit as st
from chatbot import chat

st.set_page_config(
    page_title="LangChain Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖  AI Chatbot")




if "messages" not in st.session_state:
    st.session_state.messages = []



with st.sidebar:

    st.header("Settings")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -----------------------
# Show Chat History
# -----------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])



user_input = st.chat_input("Ask me anything...")

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.spinner("Thinking..."):

        result = chat(user_input)

    response = f"""
### ✅ Answer

{result.answer}

---

### 📄 Summary

{result.summary}

---

### 🎯 Category

{result.category}

---

### 📊 Confidence

{result.confidence:.2f}

---

### 🔑 Keywords

{", ".join(result.keywords)}
"""

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    with st.chat_message("assistant"):
        st.markdown(response)