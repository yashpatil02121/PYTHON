import getpass

data={
    "yash":"2121",
    "patil":"1212"
}
username=input("Enter your username:")
password=getpass.getpass("Enter your password:")

for i in data.keys():
    if username==i:
        while password != data.get(i):
            password=getpass.getpass("Enter your password again:")
        break
print("VERIFIED")        