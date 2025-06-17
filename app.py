import streamlit as st

st.set_page_config(page_title="JW.ORG Bible Chatbot")

st.title("📖 JW.ORG Bible Chatbot")
st.write("Ask any question about the Bible, and I'll answer using information from jw.org.")

query = st.chat_input("Ask your Bible question here...")

if query:
    st.write(f"You asked: {query}")
    st.info("🔍 I'm searching jw.org content... (chatbot logic coming soon)")
