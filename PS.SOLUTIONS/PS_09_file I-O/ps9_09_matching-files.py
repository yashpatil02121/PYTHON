with open ("ps9_09_mf1.txt","r") as a:
    x=a.read()

with open ("ps9_09_mf2.txt","r") as b:
    y=b.read()

if x==y:
    print("files are matching")
else:
    print("files are NOT matching")