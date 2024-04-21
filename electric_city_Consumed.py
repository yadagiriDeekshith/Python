#write a python program to input electricity unit charge and calculate the total electricity bill according to the given condition:
#For first 50 units Rs. 0.50/unit
#For next 100 units Rs. 0.75/unit
#For next 100 units Rs. 1.20/unit
#For unit above 250 Rs. 1.50/unit
#An additional surcharge of 20% is added to the bill.

unit_charge =int(input("Enter the electric charge consumed: "))                  #439
consumed_charge_price=0                                                          #0
if unit_charge<50:                                                               #unit_charge < 50 becomes "False"
    consumed_charge_price = unit_charge*0.5
elif unit_charge <150:                                                           #unit_charge < 150 becomes "False"
    consumed_charge_price = 25+(unit_charge-50)*0.75
elif unit_charge < 250:                                                          #unit_charge < 250 becomes "False"
    consumed_charge_price = 100+(unit_charge-150)*1.20
else:
    consumed_charge_price = 220+(unit_charge-250)*1.50                           #consumed_charge_price = 220+(439-250)*1.50 =503.5
surcharge = consumed_charge_price*0.2                                            #surcharge = 503.5*0.2=100.7
total_consumed_charge_price = consumed_charge_price + surcharge                  #total_consumed_charge_price = 503.5 + 100.7=604.2
print("Total consumed electric charge price is ",total_consumed_charge_price)    #Total consumed electric charge price is 604.2
