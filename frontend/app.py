import streamlit as st
import requests

st.title("AI Chatbot")

user_input = st.text_input("Type your message:")

if st.button("Send") and user_input:
    try:
        backend_url = "http://127.0.0.1:8000/chat"
        response = requests.post(backend_url, json={"message": user_input})
        data = response.json()
        st.write("AI:", data["reply"])
    except Exception as e:
        st.write("Error connecting to backend:", e)
