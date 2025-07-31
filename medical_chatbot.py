import streamlit as st
import openai
import os

# --- OpenAI API Key (store securely in Streamlit Secrets) ---
openai.api_key = st.secrets["OPENAI_API_KEY"]

# --- Function to query OpenAI ---
def ask_openai(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

# --- Streamlit UI ---
st.set_page_config(page_title="🩺 Medical Chatbot", layout="centered")
st.title("🩺 Medical Chatbot")

st.write("Ask any medical-related question. This chatbot is for informational purposes only and not a substitute for professional medical advice.")

user_input = st.text_input("Enter your medical question:")

if user_input:
    with st.spinner("💬 Chatbot is responding..."):
        response = ask_openai(user_input)
        st.success("🤖 Response:")
        st.write(response)
