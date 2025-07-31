
import streamlit as st
import speech_recognition as sr
import pyttsx3
from openai import OpenAI

# --- OpenAI Client ---
client = OpenAI(api_key="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")  # Replace with your actual key

# --- Voice Engine Setup ---
engine = pyttsx3.init()

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Listening... Speak your medical question.")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand you."
        except sr.RequestError:
            return "Speech service unavailable."

def ask_openai(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

# --- Streamlit App ---
st.set_page_config(page_title="🩺 Medical Chatbot", layout="centered")
st.title("🩺 Medical Chatbot with Voice + Text")

mode = st.radio("Choose input mode:", ["Text", "Voice"])

if mode == "Text":
    user_input = st.text_input("Enter your medical question:")
else:
    if st.button("🎙️ Start Recording"):
        user_input = get_voice_input()
        st.text(f"You said: {user_input}")
    else:
        user_input = ""

if user_input:
    with st.spinner("💬 Chatbot is responding..."):
        response = ask_openai(user_input)
        st.success("🤖 Response:")
        st.write(response)

        if st.checkbox("🔊 Read response aloud"):
            speak_text(response)
