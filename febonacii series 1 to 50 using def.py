def febonacci(num):
    if num<=1:
        return num
    return febonacci(num-2)+febonacci(num-1)
for i in range(0,50):
    res=febonacci(i)
    if res>=50:
        break
    else:
        print(res,end=" ")

