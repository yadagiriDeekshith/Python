n=int(input("Enter a number"))
t=0
cnt=0
while n>0:
    t=n%10
    cnt=cnt+1
    n=n//10
print(cnt)
