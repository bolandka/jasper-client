import os
import sys
import re

def getGitTip(arg=""):
    f = os.popen('git-tip ' + arg)
    return f.read()
    
def run(arg="", mic=None):
    message = "Matt says:\n" + getGitTip(arg)
    if mic:
        mic.say(message, "en-US")
    print message
    
    
if __name__=="__main__":
    try:
        run(arg=sys.argv[1])
    except IndexError:
        run()
