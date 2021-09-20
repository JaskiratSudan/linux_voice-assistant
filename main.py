from recog import recog
from say import say
import os
import wikipedia
import webbrowser as wb
import subprocess

say("Say something sir....")

text = recog()
print(text)

try:
    if ("youtube" in text.lower()):
        say("Opening youtube")
        wb.open("youtube.com")

    elif ("google" in text.lower()):
        say("Opening google")
        wb.open("google.com")

    elif ("gmail" in text.lower()):
        say("Opening gmail")
        wb.open("gmail.com")

    elif ("search" in text.lower()):
        word = text.split()[text.split().index("search")+1].lower()
        res = os.popen("which {}".format(word)).read()
        if (word.lower() in res.split("/")):
            print(word)
            say("{} is found sir".format(word))

    else:
        result = wikipedia.summary(text, sentences = 2)
        print(result)
        say(result)

except:
    print("Sorry, i din't understand that")
    say("Sorry, i din't understand that")