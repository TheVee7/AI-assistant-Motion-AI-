import random
import pyttsx3
import speech_recognition as sr
import time
# import requests
import os
import subprocess
import webbrowser

def created():
    response_dict = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I am perfect ",
        "hey": "hey their"}
    for keyword, response in response_dict.items():
        if keyword in query:
            speak(response)

    # Default response if no keyword matches
    return "I'm not sure how to respond to that."
    

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
        print('Sorry , Could you repeat that')
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
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    time_curr = time.ctime(time.time())
    speak(time_curr[:-7])

def open_():
    try:
        speak("Sure . opening Google chrome")
        subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe")
        # print(1)
    except:
        speak("their is an unknown error")

def insta():
    try:
        speak("Opening Insta")
        webbrowser.open("https://www.instagram.com/?utm_source=pwa_homescreen&__pwa=1")
    except:
        speak("their is an unknown error")
def git():
    try:
        speak("Opening Github")
        webbrowser.open("https://github.com/")
    except:
        speak("their is an unknown error")
def chatgpt():
    try:
        speak("Opening Chatgpt")
        webbrowser.open("https://chat.openai.com/")
    except:
        speak("their is an unknown error")
def youtube():
    try:
        speak("Sure sir")
        webbrowser.open("https://www.youtube.com/")
    except:
        speak("their is an unknown error")
def class_room():
    try:
        speak("Sure sir")
        webbrowser.open("https://classroom.google.com/?lfhs=2")
    except:
        speak("their is an unknown error")

def shutdown():
    shut_ = "shutdown /s"
    try:
        subprocess.run(shut_ , shell=True)
        speak("the system will shutdown shortly")
    except:
        speak("their is an error")

def note():
    with open('notes.txt', 'w') as file:
            a = listen()
            print( a , file=file)

def music():
    files = os.listdir("E:\\MUSIC")   
    # file = os.path.join("E:\\MUSIC", files)
    rf = random.choice(files)
    file_path = os.path.join("E:\\MUSIC" , rf )
    # print(file_path)
    try:
        subprocess.run(["start","wmplayer", file_path],shell=True)
    except:
        print('nonononoon')
        # print(file_path)
def main():    
        while True:
            query = listen() 
            if "insta" in query or "gram" in query:
                insta()
                
            if "youtube" in query or "tube" in query:
                youtube()
                
            elif "chrome" in query or "crome" in query:
                open_()
                
            elif "time" in query:
                time_()
                
            elif "power" in query:
                shutdown()
                break
            elif "github" in query:
                git()
                
            elif "chat" in query or "gpt" in query or "chatgpt" in query:
                chatgpt()
                
            elif "music" in query or "song" in query or "gaana" in query:
                music()
            
            elif "notes" in query or "making" in query :
                note()
            else:
                print("Could you please say it again?")
        
        
if __name__ == "__main__":
    while True:   
        query = listen()
        if "motion" in query.lower() or "hello" in query.lower():
            created()
            break
    main()
    


            





