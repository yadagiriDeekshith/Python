list_1=[10,20,25,30,35]
list_2=[40,45,60,75,90]
output=[]
for i in list_1:
    if i % 2 !=0:
        output.append(i)
for i in list_2:
    if i % 2 ==0:
        output.append(i)     
print(output)
