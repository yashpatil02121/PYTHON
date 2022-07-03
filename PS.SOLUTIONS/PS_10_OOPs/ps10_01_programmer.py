class programmer:
    company="microsoft"
   
    def __init__(self,name,product):
        self.name=name
        self.product=product

    def getinfo(self):
        print(f"The name of {self.company} programmer is {self.name} and the product is {self.product}")
    
harry=programmer("harry","skype")
yash=programmer("yash","git")

harry.getinfo()
yash.getinfo()
