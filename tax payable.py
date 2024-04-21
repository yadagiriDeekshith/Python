tax=int(input("Enter the currency to find tax: "))
if tax<=10000:
    total_tax=tax*(0.0)
elif (tax>10000)&(tax<=20000):
    total_tax=10000*0.0+(tax-10000)*0.10
else:
    total_tax=10000*0.0+10000*0.10+(tax-20000)*0.20
print("The income tax payable is",total_tax)
