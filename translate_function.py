import requests
from MotionAI import speak

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

tranlate("master")