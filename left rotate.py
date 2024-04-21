x=[10,20,30,40,50,60,70,80,90,100]
element=int(input("Enter an element "))
if element in x:
    output=[]
    idx=x.index(element)
    output.extend(x[idx-1::-1])
    output.extend(x[len(x)-1:idx-1:-1])
    print(output)
