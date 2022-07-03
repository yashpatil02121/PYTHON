f=open("ps9_01.txt","r")
t=f.read()
if 'Night' in t:
    print("Night is present")
else:
    print("Night is not present")
f.close()