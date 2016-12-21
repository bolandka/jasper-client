from client import jasperpath
import os.path

def run(start, end, input, mic=None):
    wpm = computeWpm(start, end, input, mic)
    
    wpm_file = jasperpath.config("wpm.txt")
    if os.path.isfile(wpm_file):
        with open(wpm_file, "r") as f:
            wpms = [float(value) for value in f.readlines()]
    else:
        wpms = []
    
    wpms.append(wpm)
    wilko = sum(wpms) / float(len(wpms))
    message = "The current Wilko is %1.2f words per minute" %wilko
    print message
    if mic:
        mic.say(message)
        
    with open(wpm_file, "a") as f:
        f.write(str(wpm) + "\n")
        
def computeWpm(start, end, input, mic=None):
    num_words = len(input[0].split())
    duration_second = (end - start)
    duration_minute = duration_second / 60
    if num_words == 0:
        wps = wpm = 0.0
    else:
        wps = float(num_words) / duration_second
        wpm = float(num_words) / duration_minute
    
    message = "You spoke %1.2f words per second = %1.2f words per minute!" %(wps, wpm)
    print message
    if mic:
        mic.say(message)
        
    return wpm
