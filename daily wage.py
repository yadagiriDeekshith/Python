#2.Write a python program to calculate and print the total daily wage of labor.
#Wage means the salary or money that has to be paid to the worker. Labor is the man who worked for you.
#The money that has to be paid to the labor will be paid on a daily basis as per the following wage structure:
#Until the first eight hours	50.00
#For the next four hours	10.00 per hour additional
#For the next four hours	20.00 per hour additional
#For the next four hours	25.00 per hour additional
#For the next four hours	40.00 per hour additional

worker_name=input("Enter the worker name you want to calculate daily wage of hm: ")         #Deekshith
hours_worked = int(input("Enter total hours worked: "))                                     #21  
initial_rate=50 
temp=0
total=0

if hours_worked <= 8:                              #21<=8 ----> "False"
    total=initial_rate
    print(worker_name,"worked for",hours_worked,"Hours and gained the daily wage of",total,"Rupees")
    
elif (hours_worked > 8) & (hours_worked <=12):     #(21>8) and (21<=12) ---->  (True) and (False) ------>"False"
    temp=hours_worked-8
    rate=temp*10
    total=rate+initial_rate
    print(worker_name,"worked for",hours_worked,"Hours and gained the daily wage of",total,"Rupees")
    
elif (hours_worked > 12) & (hours_worked <= 16):   #(21>12) and (21<=16) ---->  (True) and (False) ------>"False"
    temp=hours_worked-12
    rate=temp*20
    total=initial_rate+rate+(4*10)
    print(worker_name,"worked for",hours_worked,"Hours and gained the daily wage of",total,"Rupees")
    
elif (hours_worked > 16) & (hours_worked <= 20):    #(21>16) and (21<=20) ---->  (True) and (False) ------>"False"
    temp=hours_worked-16
    rate=temp*25
    total=initial_rate+(4*10)+(4*20)+rate
    print(worker_name,"worked for",hours_worked,"Hours and gained the daily wage of",total,"Rupees")
    
elif (hours_worked >20) & (hours_worked <=24):      #(21>20) and (21<=24) ---->  (True) and (True) ------>"True"
    temp=hours_worked-20                            #temp=21-20=1hour
    rate=temp*40                                    #rate=1*40=40 rupees
    total=initial_rate+(4*10)+(4*20)+(4*25)+rate    #total= for firsr 8 hrs + next 4hrs + next 4hrs + next 4hrs + next 4 hrs
                                                    #total= 50+(4*10)+(4*20)+(4*25)+(rate=1*40=40 rupees)------>310
    print(worker_name,"worked for",hours_worked,"Hours and gained the daily wage of",total,"Rupees")
    
#           (Deekshith worked for 21 Hours and gained the daily wage of 310 rupees)
    
else:
    print("One day has only 24 hours please enter a valid hours between 1 to 24")
    

#         final result is ------>  (Deekshith worked for 21 Hours and gained the daily wage of 310 rupees)
