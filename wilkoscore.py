from client import jasperpath
import os.path

# TODO define functions for each rank -> e.g. play a sound; display something     
   
def sleepingWilko():
    print "Your rank is: sleeping Wilko!"
    
def wilko():
    print "Your rank is: Wilko!"
    
def drunkWilko():
    print "Your rank is: drunk Wilko!"

def computeRank(wpm):
    wilko = getCurrentWilko()
    aQuarterWilko = getNPercent(25, wilko)
    if wpm <= wilko - aQuarterWilko:
        rank = "sleeping-wilko"
    elif wpm >= wilko + aQuarterWilko:
        rank = "drunk-wilko"
    else:
        rank = "wilko"
    return rank
    
def getCurrentWilko():
    wpm_file = jasperpath.config("wpm.txt")
    with open(wpm_file, "r") as f:
        wpms = [float(value) for value in f.readlines()]
        
    return sum(wpms) / float(len(wpms))
    
def getNPercent(n, whole):
  return (n * whole) / 100.0
  
def run(wpm):
    rewards = {"sleeping-wilko": sleepingWilko,
        "wilko": wilko,
        "drunk-wilko": drunkWilko}
    rewards.get(computeRank(wpm)).__call__()
