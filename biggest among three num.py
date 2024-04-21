number_1=int(input("Enter a number_1: "))
number_2=int(input("Enter a number_2: "))
number_3=int(input("Enter a number_3: "))

if (number_1 > number_2) & (number_1 >number_3):
    print("Number_1 is the greatest number among 3 numbers")

elif (number_2 > number_1) & (number_2 > number_3):
    print("Number_2 is the greatest number among 3 numbers")

else:
    print("NUmber_3 is the greatest number among 3 numbers")
