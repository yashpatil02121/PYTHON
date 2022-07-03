import random
cards=["T","H"]

def pick_a_card():
    card=random.choices(cards)
    print(f"{card} ")
pick_a_card()
        