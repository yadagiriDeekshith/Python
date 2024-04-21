l1=\
[int(x) for x in input("Enter integers: ").split()]
for i in range(1,len(l1)):
    if sum(l1[:i])==sum(l1[i+1:]):
        print(l1[i],"is the equilibrium point")
        break
    else:
        print("no equilibrium point")
