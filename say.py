import pyttsx3

sp_rate = 130

def say(txt):  
    engine = pyttsx3.init()
    engine.setProperty('rate', sp_rate)

    engine.say(txt)

    engine.runAndWait()

