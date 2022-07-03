import os

oldname="ps9_11_old.txt"
newname="ps9_11_new.txt"

with open("ps9_11_old.txt","r")as f:
    text=f.read()

with open("ps9_11_new.txt","w")as f:
    f.write(text)

os.remove(oldname)