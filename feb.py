n=int(input("Enter a number"))
x=0
y=1
print(x,y,end=" ")
i=1
while i<=n-2:
    z=x+y
    print(z,end=" ")
    x=y
    y=z
    i+=1