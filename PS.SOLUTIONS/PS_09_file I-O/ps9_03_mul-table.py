def tables():
    for n in range(2,21):
        for i in range(1,11):
            print(f"{n} x {i} = {n*i}")
    print("\n")
    

with open("ps9_03_2-20.txt","w")as f:
    f.write(str(tables()))
