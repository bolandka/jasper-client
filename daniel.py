from client import mic
from client import jasperpath
import os
import random

def getRandomSong():
    dir = jasperpath.data('daniel')
    return os.path.join(dir, random.choice(os.listdir(dir)))

def run(mic):
    mic.speaker.play(getRandomSong())

    
	
