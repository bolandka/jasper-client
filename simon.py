import random
from client import jasperpath

def getRandomJoke():
    filename = jasperpath.data("chuck.txt")
    with open(filename, "r") as f:
        return random.choice(f.readlines()).strip()
        
def run(mic=None):
    joke = getRandomJoke()
    if mic:
        mic.say(joke, "en-US")
    print joke
    

if __name__=="__main__":
    run()
