from client import mic
from client import jasperpath
import os
import random

def getRandomSong(format):
    dir = jasperpath.data('daniel', format)
    return os.path.join(dir, random.choice(os.listdir(dir)))

def run(mic):
    mic.speaker.play(getRandomSong("wav"))


if __name__=="__main__":
    os.system("mpg321 " + getRandomSong("mp3").replace(" ", "\ "))
