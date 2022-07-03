spam=["monkey","donkey","owls","crackpots","crabs"]

with open ("ps9_05_list-file.txt","r") as f:
    content= f.read()

for word in spam:
    content=content.replace(word,"*****")
    with open ("ps9_05_list-file.txt","w") as f:
        f.write(content)
