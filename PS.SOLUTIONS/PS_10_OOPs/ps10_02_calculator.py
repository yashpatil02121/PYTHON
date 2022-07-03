class calculator:
    def __init__(self,x,y):
        self.add=x+y
        self.sub=x-y
        self.mul=x*y
        self.div=x/y
        self.mod=x%y
        self.square=x**2
        self.root=x**0.5

    def ans(self):
        print(f"addition:{self.add}")
        print(f"subtraction:{self.sub}")
        print(f"multiplication:{self.mul}")
        print(f"division:{self.div}")
        print(f"modulas:{self.mod}")
        print(f"square:{self.square}")
        print(f"square root:{self.root}")

x=int(input("enter 1st number:"))
y=int(input("enter 2nd number:"))

result=calculator(x,y)
result.ans()