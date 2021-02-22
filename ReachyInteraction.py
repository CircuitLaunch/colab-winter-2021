import speech_recognition as sr
from gtts import gTTS
import os
import time

#Reachy should detect a person first or program to be initiated 
introtext1 = "Hello l am Reachy your concierge welcome to circuit launch"
language = 'en-us'
speech = gTTS(text = introtext1, lang = language, slow = False)
speech.save("introtext1.mp3")
os.system("open introtext1.mp3")
time.sleep(5) # Sleep for 3 seconds
# Intiate command for gesture
introtext2 = "Due to COVID19 regulations l am going to verify you are wearing a mask "
speech = gTTS(text = introtext2, lang = language, slow = False)
speech.save("introtext2.mp3")
os.system("open introtext2.mp3")
time.sleep(6)
introtext3 = "Please stand still for 10 seconds "
speech = gTTS(text = introtext3, lang = language, slow = False)
speech.save("introtext3.mp3")
os.system("open introtext3.mp3")
time.sleep(4)
#intiate mask detection algoritthm
introtext4 = "Thank you mask is detected where do you want to go to the lab area or to the kitchen"
speech = gTTS(text = introtext4, lang = language, slow = False)
speech.save("introtext4.mp3")
os.system("open introtext4.mp3")
time.sleep(7)
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")
        
#text = "Hi! I am Reachy, the best robot concierge and I am here to help you. What do you need?"
#text1 = "Hello I am Anna, I am learning python"
language = 'en-us'
speech = gTTS(text = text, lang = language, slow = False)
speech.save("text.mp3")
os.system("open text.mp3")