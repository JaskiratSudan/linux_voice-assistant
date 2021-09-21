from recog import recog
from say import say
from search_package import searchpac
from install_package import install
import os
import wikipedia
import webbrowser as wb
import subprocess

say("How can i help you sir....")

try:
    
    text = recog()
    print("USER: "+text)

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
        say("{} is installed in your pc sir".format(word)) if(searchpac(word)) else say("can't find {} in your pc sir".format(word))

    elif ("install" in text.lower()):
        word = text.split()[text.split().index("install")+1].lower()
        say("{} has been installed successfully".format(word)) if(install(word)) else None


    else:
        print("Fetching information from Wikipedia.........")
        say("Fetching information from Wikipedia")
        result = wikipedia.summary(text, sentences = 2)
        print(result)
        say(result)

except:
    print("Sorry, i din't understand that")
    say("Sorry, i din't understand that")