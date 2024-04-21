n=int(input("Enter a number of rows you need "))
i=1
while i<=n:
    j=n
    while j>i:
        print(" ",end=" ")
        j-=1
    print(i,end=" ")
    k=1
    while k<2 *(i-1):
        print(" ",end=" ")
        k+=1
    if i==1:
        print()
    else:
        print(i)
    i+=1
i=n-1
while i >=1:
    j=n
    while j>i:
        print(" ",end=" ")
        j=j-1
    print(i,end=" ")
    k=1
    while k<2 *(i-1):
        print(" ",end=" ")
        k+=1
    if i==1:
        print()
    else:
        print(i)
    i-=1
