def game():
    return 23

score=game()
with open("ps9_02-hiscore.txt") as f:
    hiscore=int(f.read())

if hiscore<score:
    with open("ps9_02-hiscore.txt","w")as f:
        f.write(str(score))



# def game():
#     s=int(input("enter your score:"))
#     return s

# score=game()
# with open("ps9_02-hiscore.txt","r") as f:
#     hiscore=int(f.read())

# if score>hiscore:
#     with open("ps9_02-hiscore.txt","w"):
#         f.write(str(score))
