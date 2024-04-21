veg=["Brinjal","Tomato","Potato","Beans"]
quantity=[10,20,15,8]
price=[30,60,22,40]
while True:
    item=input("Wnat do you want? ")

    if item in veg:
        q=float(input("How much amount of quantity do you want? "))
        idx=veg.index(item)
        if q<= quantity[idx]:
            amount=q*price[idx]
            print("Please pay the amount of",amount,"rupees")
            quantity[idx]=quantity[idx]-q
        else:
            print("That much quantity is not available at our shop")

    else:
        print(item,"is not available at our shop")

    loop=input("Do you want to close the shop say (Yes/No)" )
    if loop == "Yes":
        print("Closing the shop")
        print("_"*20,"Report","_"*20)

        for it in zip(veg,quantity):
            print(it)
        break
    
