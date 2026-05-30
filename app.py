import streamlit as st
import anthropic

st.set_page_config(page_title="MakalahAI", page_icon="📄")

st.title("📄 MakalahAI")
st.caption("Chatbot Pembuat Makalah Akademis")

api_key = st.text_input("Anthropic API Key", type="password")

if "chat" not in st.session_state:
    st.session_state.chat = []

for role, msg in st.session_state.chat:
    with st.chat_message(role):
        st.write(msg)

prompt = st.chat_input("Tulis topik atau pertanyaan makalah...")

if prompt:
    st.session_state.chat.append(("user", prompt))

    with st.chat_message("user"):
        st.write(prompt)

    if not api_key:
        with st.chat_message("assistant"):
            st.write("Masukkan API key terlebih dahulu.")
    else:
        client = anthropic.Anthropic(api_key=api_key)

        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1000,
            system="Kamu adalah asisten pembuat makalah akademis berbahasa Indonesia.",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        answer = response.content[0].text
        st.session_state.chat.append(("assistant", answer))

        with st.chat_message("assistant"):
            st.write(answer)
