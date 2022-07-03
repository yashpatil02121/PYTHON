import getpass
data={
    "yash":"1234",
    "patil":"4321"
}

email=input("enter your email address:")

print("See password while entering?")
p=input("enter y for yes & n for no::")
if p=="y":
    password=input("password=")

else:
    password=getpass.getpass()

# print("\n\n\nemail is ",email,"\npassword is",password)

for i in data.keys():
    if email==i:
        for j in data.values():
            if password==j:
                print("VERIFIED:")
                break
            else:
                print("wrong password! fill it again...")
                