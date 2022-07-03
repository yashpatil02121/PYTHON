with open("ps9_07_this.txt") as f:
    text=f.read()

with open("ps9_07_this-copy.txt","w") as f:
    f.write(text)
