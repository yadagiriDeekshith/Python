print("Welcome to the Python Atm Simulator!")
balance=1000
user_pin=2598
enter_pin=int(input("Please enter your PIN: "))
print("_"*50)

if enter_pin == user_pin:
    correct_pin =True
else:
    print("Invalid PIN.")
    correct_pin=False


while correct_pin:
    print("Main Menu")
    print("1.Check Balance")
    print("2.Deposite Money")
    print("3.Withdraw Money")
    print("4.Exit")
    print("_"*50)

    choice=int(input("Enter your choice: "))

    if choice == 1:
        print("Your current balance is",balance)
        print("_"*50)

    elif choice == 2:
        amount=float(input("Enter the amount to deposit: "))
        balance +=amount
        print(amount," deposited successfully.")
        print("_"*50)

    elif choice == 3:
        amount=float(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance!")
            print("_"*50)
        else:
            balance -= amount
            print(amount,"Withdrawn successfully.")
            print("_"*50)
    elif choice ==4:
        print("Thank you for using the ATM. GoodByee!")
        correct_pin=False
        print("_"*50)

    else:
        print("Invalid choice. please try again")
        print("_"*50)
        
