expr=input("Enter an expression: ")
obcount=0
cbcount=0
for x in expr:
    if x == "(":
        obcount +=1
    if x ==")":
        if obcount >0:
            obcount -=1
        else:
            cbcount += 1
if obcount + cbcount ==0:
    print(expr, "is valid")
else:
    print(expr,"contains",obcount+cbcount,"errors")
