with open ("ps9_04_spam-file.txt","r") as f:
    content= f.read()
    
content=content.replace("donkey","######")

with open ("ps9_04_spam-file.txt","w") as f:
    content= f.write(content)