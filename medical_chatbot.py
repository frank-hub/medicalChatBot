import streamlit as st
import openai
import os

# --- OpenAI API Key (store securely in Streamlit Secrets) ---
openai.api_key = st.secrets["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"]

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
