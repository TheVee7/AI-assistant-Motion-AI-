import random
import pyttsx3
import speech_recognition as sr
import time
import requests
import os
import subprocess
import webbrowser
import google.generativeai as genai
import os
import urllib.parse
from Music_player import *
import tkinter as tk
from PIL import Image, ImageTk


def created(query):
    response_dict = {
        "hello motion": "Hi there! How can I help you?",
        "how are you": "I am perfect",
        "activate motion": "Any tasks, sir?"
    }
    for keyword, response in response_dict.items():
        if keyword.lower() in query.lower():
            speak(response)

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
        print(f"VEE: {query}")
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
engine.setProperty('voice', voices[1].id)


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


def chatgpt():
    try:
        speak("Opening Chatgpt")
        webbrowser.open("https://chat.openai.com/")
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

def end():
    # shut_ = "exit"
    # try:
    #     subprocess.run(shut_ , shell=True)
    #     root.destroy()
    # except:
    #     speak("their is an error")
    root.destroy()

def note():
    with open('notes.txt', 'w') as file:
            a = listen()
            print( a , file=file)

def tranlate(x):

    try:
        modified_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{x}"
        res = requests.get(modified_url)
        data = res.json()
        defi = data[0]["meanings"]
        s_data = defi[0]["definitions"][0]["definition"]
        speak(f"meaning of {x} is")
        speak(s_data)
        print(s_data)
    except KeyError as e:
        print("I think their is no word like this", e)
        speak("I think their is no word like this")
    except Exception as e:
        print("Some unknown errors", e)
        speak("Some unknown errors")


def trans(query):
    new_q = query.split()
    a = list(new_q)
    try:
        pos = a.index("translate")
        word = new_q[pos + 1]
        tranlate(word)
    except ValueError:
        print("Sorry whats thats word")

def open_website(query):
    new_query = query.split()
    a = new_query.index("open")
    z = new_query[a + 1]
    web_link = f"https://{z}.com/"
    speak(f"opening {z} ")
    webbrowser.open(web_link)

def bard(query):
    # text = query.remove("hey" , "")
    text = query.replace("motion" , "")
    genai.configure(api_key=os.environ["bard_api"])
    model = genai.GenerativeModel('gemini-pro')
    try:
        response = model.generate_content(f"{text} .in shortest way possible")
        new_text = response.text
        new_text = new_text.replace("*","")
        print(new_text)
        speak(new_text)
    except KeyError as e :
        print('something is wrong')
    except ValueError as e :
        print('something is wrong')

def search_on_google(query):
    # Construct the Google search URL
    new_q = query.split()
    index = new_q.index("google")
    new_q = new_q[index + 1 : ]
    new_q = ' '.join(new_q)

    query = urllib.parse.quote_plus(new_q)
    url = f"https://www.google.com/search?q={query}"

    # Open the URL in a new tab
    webbrowser.open_new_tab(url)



def main():    
        while True:
            query = listen()

            if "open" in query and "motion" in query:
                open_website(query)
                
            elif "activate" in query :
                created(query)
                
            elif "chrome" in query and "open" in query:
                open_()
                
            elif "time" in query:
                time_()
            # elif "compost" or "status" in query:
            #     speak("working on it ")
            #     compost()
                
            elif "shutdown" in query and "system" in query:
                shutdown()
                break
                
            elif "chat" in query and "gpt" in query:
                chatgpt()
                
            elif "music" in query or "gaana" in query:
                directory = "E:\\MUSIC"
                num_songs = 5
                speak("playing local playlist")
                music()
            
            elif "next" in query and "song" in query :
                action = "next"
                control(action)

            elif "stop" in query and "song" in query :
                action = "stop"
                control(action)
            
            elif "notes" in query or "making" in query :
                note()
            
            elif "translate" in query :
                trans(query)
            
            elif "Google" in query or "search" in query: 
                search_on_google(query)
            
            elif "Exit" in query : 
                break
                
            
            elif query :
                bard(query)                               
            
            else:
                print("Could you please say it again?")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Motion")


    image_path = "E:\\GIT PUSH\\AI-assistant-Motion-AI-\\HOMEPAGE.jpg"
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)


    icon_path = "Motion-icon-.ico"
    root.iconbitmap(icon_path)


    label = tk.Label(root, image=photo)
    label.image = photo  # Keep a reference to prevent garbage collection
    label.pack()

# Create and pack the start motion button
    custom_font = ('Helvetica', 10, 'bold')
    button = tk.Button(root, text='Start Motion', command=main , font=custom_font, width=410, bg= "#101018", fg="white")
    button.pack(padx=5)
    button = tk.Button(root, text='Exit Motion', command=end , font=custom_font, width=410, bg= "#101018", fg="white")
    button.pack(padx=5, pady=3 )

# Set window size constraints
    root.geometry("410x460")
    root.maxsize(410, 469)
    root.minsize(410, 469)

# Run the Tkinter event loop
    root.mainloop()