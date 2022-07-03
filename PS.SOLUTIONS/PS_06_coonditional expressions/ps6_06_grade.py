m=int(input("enter your marks:"))
if (m<=100 and m>=90):
    grade="Ex"
elif(m>=80):
    grade="A"
elif(m>=70):
    grade="B"
elif(m>=60):
    grade="C"
elif(m>=50):
    grade="D"
elif(m<50):
    grade="F"

print("your grade is",grade)

