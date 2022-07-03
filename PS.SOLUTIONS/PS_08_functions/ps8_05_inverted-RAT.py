def RAT(n):
    j=n
    for i in range(n+1):
        print("* "*j)
        j=j-1

n=int(input("enter a number:"))
RAT(n)
