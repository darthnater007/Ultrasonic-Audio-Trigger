#install google tts with `pip install gTTS`
from gtts import gTTS

from gtts import gTTS 

import os
    
def play_audio():
    # TODO: have this call text from an API
    my_text = "Reminder: get Nate a cup of coffee."
    #get tts response
    myobj = gTTS(text=my_text, lang='en', slow=False) 
    print(myobj)
    #save it
    myobj.save("./audio/audio.mp3")
    #play it
    os.system("mpg123 ./audio/audio.mp3")