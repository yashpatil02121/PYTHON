def remove_and_strip(text,word):
    new=text.replace(word,"")
    return new.strip()



text="      my name is yash         "
d=remove_and_strip(text,"yash")
print(d)


