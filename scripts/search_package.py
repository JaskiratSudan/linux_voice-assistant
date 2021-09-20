import subprocess

def searchpac(name):
    
    try:
        res = subprocess.check_output("which {}".format(name), shell=True)
        if (b'/usr/bin' in res):
            return True

    except:
        return False