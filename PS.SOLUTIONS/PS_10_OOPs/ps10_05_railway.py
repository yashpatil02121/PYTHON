class train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def getstatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print(f"The fare of the train is {self.fare}")

    def bookticket(self):
        if (self.seats>0):
            print(f"Your ticket is booked! Your ticket number is {self.seats}")
            self.seats=self.seats-1
        else:
            print("Sorry! This train is full...")

interncity= train ("Interncity express 401105",500,10)

interncity.getstatus()
interncity.bookticket()
interncity.bookticket()
interncity.bookticket()
interncity.bookticket()
interncity.getstatus()
