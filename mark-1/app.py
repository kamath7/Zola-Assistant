from sqlalchemy import engine
import pyttsx3
from decouple import config 

username = "LordKams"
botname = "Zola"

engine = pyttsx3.init('sapi5')
engine.setProperty('rate',183)
engine.setProperty('volume',1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Welcome {0}! How are you today?".format(username))