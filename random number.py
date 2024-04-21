import random

Guessing_number=(random.randint(1,9))
i=1
while i<=3:
    my_num = int(input("Enter a number you want to guess: "))
    if my_num==Guessing_number:
        print("You won the game")
        break
    else:
        print("wrong guess")
    i+=1
else:
    print("You lost the game")
print("Game over")
