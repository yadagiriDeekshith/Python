print("Enter 10 Numbers ")
sum=0
i=1
while i<=10:
    n=int(input("Enter number %d ="%i))
    if n<0:
        continue
    sum=sum+n
    i+=1
print("Sum of Positive Numbers is =",sum)
