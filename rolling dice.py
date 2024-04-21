import random
dice_1=random.randint(1,6)
dice_2=random.randint(1,6)
while True:
    total=dice_1+dice_2
    if total==12:
        print("You won the game")
        print(total)
        break
    elif total==12:
        print("You are having another chance")
    else:
        print("You lost the game")
        print(total)
        break
