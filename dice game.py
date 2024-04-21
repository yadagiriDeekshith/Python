import random
while True:
    dice_1=random.randint(1,6)
    dice_2=random.randint(1,6)
    print(dice_1,"firs dice  rolled result",dice_2,"second dice rolled result")
    total=dice_1+dice_2
    print("The total of the dice is ",total)
    if total==12:
        print("You won the game")
        break
    elif total==7:
        print("you have an another chance")
    else:
        print("you lost thr game")
        break
print("Game over")
