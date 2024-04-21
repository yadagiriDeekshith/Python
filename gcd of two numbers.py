x=int(input("Enter a number "))
y=int(input("Enter a number "))
if x>y:
    small=x
else:
    small =y
for i in range(2,small+1):
    if (x%i==0) & (y%i==0):
        gcd=i
print("GCD if given two numbers is",x,"and",y,"is",gcd)
