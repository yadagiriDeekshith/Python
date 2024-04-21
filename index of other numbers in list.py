x=[1,2,3,4,1,2,6,7,8]
Element=int(input("Enter an element to find in list"))
for i in range(0,len(x)):
    if x[i]==Element:
        print(i)
