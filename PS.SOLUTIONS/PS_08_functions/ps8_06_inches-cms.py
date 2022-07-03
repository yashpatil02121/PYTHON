def cms(inch):
    cen=inch*2.54
    return cen

inch=int(input("enter length in inches-> "))
print(f"{inch} inches = {cms(inch)} centimeters")