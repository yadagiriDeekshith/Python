n=int(input("Enter a number to get single digit at the end "))
t=0
while True:
    s=0
    while n>0:
        t=n%10
        s=s+t
        n=n//10
    if s>9:
        n=s
    else:
        print(s)
        break
