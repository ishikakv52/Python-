import os
import speech_recognition as sr
import google.generativeai as genai
import subprocess

# --- CONFIGURE YOUR GEMINI API KEY ---
genai.configure(api_key="AIzaSyC7FKCXR4sBYpB95ajYpp7XXfgZq9mvqOo")

# --- CHOOSE GEMINI MODEL ---
model = genai.GenerativeModel("gemini-2.5-flash")

recognizer = sr.Recognizer()
mic = sr.Microphone()

def listen():
    with mic as source:
        speak("Hello Ishika Rathi How Can I Help you?")
        print("\n🎙️ Hello Ishika Rathi How Can I Help you... (or say 'exit' to quit)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"🧠 You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I couldn’t understand that.")
        print("❌ Sorry, I couldn’t understand that.")
        return None
    except sr.RequestError:
        print("⚠️ Speech recognition service error.")
        return None

def speak(text):
    """Use Mac's built-in 'say' command safely."""
    try:
        subprocess.run(["say", text])
    except Exception as e:
        print("🔇 Speech error:", e)

def chat_with_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        reply = response.text
        print("🤖 AI : ", reply)

        speak(reply)
        return reply
    except Exception as e:
        print("⚠️ Error:", e)
        return None

# --- MAIN CHAT LOOP ---
while True:
    user_input = listen()
    if not user_input:
        continue
    if "exit" in user_input:
        print("👋 Goodbye Ishika Rathi!")
        speak("Goodbye Ishika Rathi")
        break
    chat_with_gemini(user_input)