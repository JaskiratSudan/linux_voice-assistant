import os
from search_package import searchpac
from say import say


def install(name):

    if not (searchpac(name)):

        print("Installing {}..........".format(name))
        say("Installing {}".format(name))
        say("it may ask you for your password")
        
        try:
            os.system("sudo apt install {}".format(name))
            if (searchpac(name)):
                return True

        except:
            return False

    else:
        print("{} is already installed in your pc sir".format(name))
        say("{} is already installed in your pc sir".format(name))