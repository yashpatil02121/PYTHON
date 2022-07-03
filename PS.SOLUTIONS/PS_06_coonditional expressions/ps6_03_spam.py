text=input("enter a text:")

if ("make a lot of money" in text):
   spam=True
elif("click this"):
    spam=True
elif("subscribe this"):
    spam=True
elif("buy now"):
    spam=True
else:
    spam=False

if spam:
    print("text is a spam")
else:
    print("text is not a spam")
