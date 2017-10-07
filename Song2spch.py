from gtts import gTTS
import os 
tts=gTTS(text="Hello Aditya Have a good weekend",lang='en')
tts.save("hello.mp3")
os.system("mpg321 hello.mp3")
