year = 2000
if (year % 400 == 0) and (year % 100 == 0):#(2000%400==0-->true)and(2000%100==0--->true)
    print(year,"leap year")             # prints 2000 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):#(2000%4==0--->true)and(2000%100!=0---->false)
    print(year,"leap year")               #condition will fails
else:
    print(year,"is not leap year")    #exits out of loop
