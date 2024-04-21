n=int(input("Enter a n value "))
s=0
for n in range(2,n+1):
    for i in range(2,(n//2)+1):
        if n%i==0:
            break
    else:
        s=s+n
print(s)
