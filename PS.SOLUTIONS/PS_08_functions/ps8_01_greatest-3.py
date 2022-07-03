def greatest(x,y,z):
    if(x>y and x>z):
        print(f"x({x}) is greatest")
    elif(y>x and y>z):
        print(f"y({y}) is greatest")
    else:
        print(f"z({z}) is greatest")

x=int(input("enter 1st number:"))
y=int(input("enter 2nd number:"))
z=int(input("enter 3rd number:"))
greatest(x,y,z)