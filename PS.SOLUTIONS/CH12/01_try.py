while(True):
    print("Press q to quit")
    a = input("Enter a number:")
    if a == 'q':
        break
    a = int(a)
    if (a>6):
        print("You entered a number greater than 6")
print("Thanks for playing this game")