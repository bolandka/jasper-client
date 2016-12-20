import random

def run(mic=None):
    vocabulary = ["Mmh.", "Oh, echt?", "Das verstehe ich nicht.", "Red mal langsamer!", "Aaaalter!", "Aaaalter, krass!", "Achso.", "Verstehe.", "Sehr interessant.", "Ja, macht schon Sinn.", "Hahaha.", "ed bruddla - buddla"]
    answer= random.choice(vocabulary)
    if mic:
        mic.say(answer, "de-DE")
    print answer
    
