from gtts import gTTS
import os 
tts=gTTS(text="Hello Youtube today is rough day",lang='en')
tts.save("hello.mp3")
os.system("mpg321 hello.mp3")