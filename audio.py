import os
# play calls mpg123 at the command line to play the audio.mp3 file stored in the audio folder
def play():
    os.system("mpg123 /home/pi/Ultrasonic_Audio_Trigger/audio/audio.mp3")
