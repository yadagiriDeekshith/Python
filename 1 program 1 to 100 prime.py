num=1
while num<=100:
    cnt=0
    i=2

    while i<=num//2:
        if num%i==0:
            cnt=cnt+1
            break
        i+=1
    if ((cnt ==0) & (num !=1)):
        print("%d"%num,end=" ")
    num=num+1
