import streamlit as st
from chat_utils import get_chatbot_response
from load_data import load_vectorstore

st.set_page_config(page_title="JW.ORG Bible Chatbot")

st.title("📖 JW.ORG Bible Chatbot")
st.write("Ask any question about the Bible, and I'll answer using information from jw.org.")

# Load the vector store once
@st.cache_resource
def load_data():
    return load_vectorstore()

vectorstore = load_data()

# Handle chat input
query = st.chat_input("Ask your Bible question here...")

if query:
    with st.spinner("🔍 Searching jw.org..."):
        try:
            response = get_chatbot_response(query, vectorstore)
            st.write(response)
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
