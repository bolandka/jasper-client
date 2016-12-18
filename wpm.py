

def run(start, end, input, mic=None):
    duration = (end - start) / 100    
    message = "You needed %1.2f seconds to speak %d words" %(duration, len(input[0].split()))
    print message
    if mic:
        mic.say(message)
