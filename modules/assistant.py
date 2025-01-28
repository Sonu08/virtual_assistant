import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def greet():
    from datetime import datetime
    hour = datetime.now().hour
    if 0 <= hour < 12:
        print("Good morning!")
    elif 12 <= hour < 18:
        print("Good afternoon!")
    else:
        print("Good evening!")
    print("I am your virtual assistant. How can I help you today?")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("You were silent for too long. Please try again.")
            return "None"
    try:
        command = recognizer.recognize_google(audio, language="en-US")
        print(f"User said: {command}\n")
    except Exception:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return "None"
    return command.lower()
