import random
coin=["H","T"]

def tossing():

    for i in range(1,4):
        result=random.choice(coin)
        print(f"{i}-> {result}")

tossing()