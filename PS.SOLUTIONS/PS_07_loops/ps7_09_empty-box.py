# n=int(input("enter a number:"))
# print("* "*n)
# for i in range(n-2):
#     print("*"," "*(n-2),"*")
# print("* "*n)
def is_leap(year):
    if (year%4==0):
        return True
    else:
        return False

year=int(input())
print(is_leap(year))
