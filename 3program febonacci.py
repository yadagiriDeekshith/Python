n_term=int(input("Enter the nth number to print "))
x=0
y=1
print(x,y,end=" ")
i=1
while i<=n_term-2:
    z=x+y
    print(z,end=" ")
    x=y
    y=z
    i+=1