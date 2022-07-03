try:
    i = int(input("enter a number:"))
    c = 1/i
except Exception as e:
    print(e)
    exit()
finally:
    print("We were done")

print("Thanks for using the program")