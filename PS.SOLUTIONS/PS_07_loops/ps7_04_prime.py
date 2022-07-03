n=int(input("enter a number:"))

for i in range(2,n+1):
    if((n%i)==0):
        prime=False     
    else:
        prime=True

if prime:
    print("prime")
else:
    print("not prime")