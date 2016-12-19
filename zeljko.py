import random

def run(mic=None):
    vocabulary = ["Mmh.", "Oh, echt?", "Das habe ich jetzt nicht verstanden, kannst du noch mal wiederholen?", "Red mal langsamer!", "Aaaalter!", "Achso.", "Verstehe.", "Sehr interessant.", "Ja, macht schon Sinn", "Das verstehe ich jetzt nicht"]
    answer= random.choice(vocabulary)
    if mic:
        mic.say(answer)
    print answer
    
