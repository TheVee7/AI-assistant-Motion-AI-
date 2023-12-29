import random
import pyttsx3
import speech_recognition as sr
import time
import requests
# import openai
import subprocess
import webbrowser

def created():
    speak("how are you sir. I am Motion Ai . How can I assist you Sir .")

def take_cmd():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print('Recognizing...')
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print('Sorry, I could not understand. Please try again.')
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

def listen():
    while True:
        command = take_cmd()
        if command is not None:
            return command

# speak
engine = pyttsx3.init('sapi5')   
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    time_curr = time.ctime(time.time())
    speak(time_curr[:-7])

def open_():
    try:
        subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe")
        # print(1)
    except:
        speak("their is an unknown error")

def insta():
    try:
        webbrowser.open("https://www.instagram.com/?utm_source=pwa_homescreen&__pwa=1")
    except:
        speak("their is an unknown error")
def git():
    try:
        webbrowser.open("https://github.com/")
    except:
        speak("their is an unknown error")
def chatgpt():
    try:
        webbrowser.open("https://chat.openai.com/")
    except:
        speak("their is an unknown error")

def shutdown():
    shut_ = "shutdown /s"
    try:
        subprocess.run(shut_ , shell=True)
    except:
        speak("their is an error")
        
        
if __name__ == "__main__":
    while True:
        query = listen() 
        if "insta" in query or "gram" in query:
            insta()
        elif "chrome" in query or "crome" in query:
            open_()
        elif "time" in query:
            time_()
        elif "power" in query:
            shutdown()
        elif "github" in query:
            git()
        elif "chat" in query or "gpt" in query or "chatgpt" in query:
            chatgpt()
        else:
            speak("Could you please say it again?")



            





