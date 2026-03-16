import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random
from openai import OpenAI

# Initialize OpenAI client using environment variable
client = OpenAI(api_key="your api key here")

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please repeat.")
            return None
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return None

def ask_openai(prompt):
    try:
        messages = [
            {"role": "system", "content": "You are AIVA, a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Or "gpt-3.5-turbo" if needed
            messages=messages,
            temperature=1,
            max_tokens=2048
        )
        answer = response.choices[0].message.content
        return answer
    except Exception as e:
        print("OpenAI error:", e)
        return "Sorry, I couldn't get a response from OpenAI."

def greet_user():
    speak("Hello, I am Open A.I Assistant. How can I help you today?")

def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

def play_music():
    speak("Playing music for you...")
    songs = [
        "https://www.youtube.com/watch?v=K4DyBUG242c&list=RDQMTgh66LaGkb4&start_radio=1",
        "https://www.youtube.com/watch?v=AKH6ZNSnWOA",
        "https://www.youtube.com/watch?v=F491KFJ7aAw"
    ]
    selected_song = random.choice(songs)
    print(f"Selected song: {selected_song}")
    try:
        webbrowser.open(selected_song)
        speak("Enjoy the song!")
    except Exception as e:
        speak("Sorry, I couldn't play the music. Check your internet connection.")
        print("Error opening song:", e)

def open_website(website_name):
    url_map = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "wikipedia": "https://www.wikipedia.org",
        "openai": "https://platform.openai.com"
    }
    for key, url in url_map.items():
        if key in website_name:
            try:
                webbrowser.open(url)
                speak(f"Opening {key}")
                return
            except Exception as e:
                speak(f"Sorry, I couldn't open {key}.")
                print(f"Error opening {key}: {e}")
                return
    speak(f"Sorry, I don't know how to open {website_name}")

def execute_command(command):
    if 'time' in command:
        tell_time()
    elif 'hello' in command or 'hi' in command:
        greet_user()
    elif 'play music' in command:
        play_music()
    elif 'open' in command:
        open_website(command)
    elif 'quit' in command or 'exit' in command:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        # Anything else goes to OpenAI
        response = ask_openai(command)
        speak(response)

def main():
    greet_user()
    while True:
        command = listen()
        if command:
            execute_command(command)

if __name__ == "__main__":
    main()
