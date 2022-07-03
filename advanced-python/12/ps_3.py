while True:
    print("press x to exit")
    num = int(input("Enter your number:"))
    table = [num*i for i in range(1,11)]
    print(table)
    if(num == "x"):
        break