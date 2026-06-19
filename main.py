import speech_recognition as sr
import pyttsx3
from datetime import datetime

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def log_conversation(user_text, bot_text):
    with open("chat_log.txt", "a") as file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n[{time}]\n")
        file.write(f"User: {user_text}\n")
        file.write(f"InnovX: {bot_text}\n")

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text
    except:
        return "Sorry, I could not understand."

def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! How can I help you?"

    elif "time" in user_input:
        return f"The current time is {datetime.now().strftime('%H:%M')}"

    elif "date" in user_input:
        return f"Today's date is {datetime.now().strftime('%d %B %Y')}"

    elif "your name" in user_input:
        return "I am InnovX, your AI assistant."

    elif "bye" in user_input:
        return "Goodbye! Have a nice day."

    else:
        return "I am still learning. Please try another question."

print("=== InnovX CHATBOT ===")

while True:
    mode = input("\nType T for text or V for voice: ").lower()

    if mode == "t":
        user_text = input("You: ")

    elif mode == "v":
        user_text = listen()

    else:
        print("Invalid option")
        continue

    response = get_response(user_text)

    print("InnovX:", response)
    speak(response)

    log_conversation(user_text, response)

    if "bye" in user_text.lower():
        break
