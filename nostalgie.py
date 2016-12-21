from client import jasperpath
import os

def getCommands():
    dir = jasperpath.data('wts-chor')
    cmds = []
    for song in os.listdir(dir):
        cmds.append("mpg321 " + os.path.join(dir, song.replace(" ", "\ ").replace("(", "\(").replace(")", "\)")))
    return cmds

def run():
    for cmdstr in getCommands():
        os.system(cmdstr)


if __name__=="__main__":
    run()
