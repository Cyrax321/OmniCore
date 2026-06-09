# pyrefly: ignore [missing-import]
import pyttsx3

engine = pyttsx3.init()
engine.say("hi and welcome to my podcast")
engine.runAndWait()