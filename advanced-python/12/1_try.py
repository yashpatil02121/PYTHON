while(True):
    print("press x to exit")
    a = input("Enter a number:")
    if a=='x':
        break
    try:
        a = int(a)
        if a>6:
            print("You entered a number greater than 6")

    except Exception as e:
        print(f"Your input resulted in  an error: {e}")
print("Thank you for playing")