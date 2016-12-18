if __name__=="__main__":
    words = []
    with open("dictionary_all.dic", "r") as f:
        for line in f.readlines():
            if line != "\n":
                words.append(line.split(" ")[0].strip())
        
    print "\n".join(words)
