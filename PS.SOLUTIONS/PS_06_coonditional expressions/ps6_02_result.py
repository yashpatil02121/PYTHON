from typing import Pattern


phy=int(input("enter physics marks:"))
chem=int(input("enter chemistry marks:"))
math=int(input("enter mathematics marks:"))

sum=(phy+chem+math)
avg=sum/3

if(phy<33 or chem<33 or math<33):
    print("one of your subject score is less than 33...\n\tYOU FAILED!!")

elif(avg<40):
    print("your average score is less than 40...\n\tYOU FAILED!!")

else:
    print("congratulations....\n\tYOU PASSED!!! ")
    

print(f"you scored {avg} out of 100")