state="Stop"
while True:
    print("1. Start")
    print("2. Stop")
    print("3. Exit")
    dec=int(input("Enter an option shown above "))
    if dec==1:
        if state=="Stop":
            print("Car is started")
            state="Start"
        else:
            print("Car is already started")
            
    elif dec==2:
        if state=="Start":
            print("Car is stoped ")
            state="Exited"
        else:
            print("Car is already stoped")
        
    elif dec==3:
        print("Exited")
        break
    else:
        print("Choose correct option from above")
