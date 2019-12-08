from gtts import gTTS 

import os

import requests


def get_phrase():
    response = requests.get("https://uat-server-jsu25stwna-uc.a.run.app/getphrase")
    print(str(response.json()))
    return str(response.json())

def play_audio():
    my_text = get_phrase()
    my_object = gTTS(text=my_text, lang='en', slow=False) 
    my_object.save("./audio/audio.mp3")
    os.system("mpg123 ./audio/audio.mp3")

play_audio()