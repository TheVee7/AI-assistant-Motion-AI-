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
        response = model.generate_content(f"{text} in shortest way possible")
        print(response.text)
        speak (response.text)
    except KeyError as e :
        print('something is wrong')

def main():    
        while True:
            query = listen() 
            if "open" in query and "motion" in query:
                open_website(query)
                
            elif "motion" in query :
                bard(query)          
            
            elif "activate" in query :
                created(query)
                
            elif "chrome" in query and "open" in query:
                open_()
                
            elif "time" in query:
                time_()
                
            elif "shutdown" in query and "system" in query:
                shutdown()
                break
                
            elif "chat" in query and "gpt" in query:
                chatgpt()
                
            elif "music" in query or "song" in query or "gaana" in query:
                music()
            
            elif "notes" in query or "making" in query :
                note()
            
            elif "translate" in query :
                trans(query)
            
            else:
                print("Could you please say it again?")
        
        
if __name__ == "__main__":
    main()
    


            





