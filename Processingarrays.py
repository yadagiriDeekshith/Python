import time
import numpy as np
import sys

#1.creating array

#data=np.array([1,2,3,4])
#output=data.reshape(2,2)
#print(data)
#print(output)
#print(output.T)

#2.numpy is faster in excution

#start=time.time()
#list1=[i for i in range(1,100001)]
#list2=[i for i in range(1,100001)]
#output=[]
#for j in range(0,len(list1)):
#    output.append(list1[j]+list2[j])
#print(output)
#end=time.time()
#print("Time taken by list ",end-start)

#start=time.time()
#arr1=np.arange(1,100001)
#arr2=np.arange(1,100001)
#arr=arr1+arr2
#print(arr)
#end=time.time()
#print("Time taken by num py is",end-start)

#3.it takes less memory
#list1=[i for i in range(1,1001)]
#arr1=np.arange(1,1001)
##list_memory=sys.getsizeof(list1)
#print("list memory",list_memory)
#array_memory=sys.getsizeof(arr1)
#print("aray memory",array_memory)

#4.4x4 matrix
arr=np.arange(1,17)
arr=arr.reshape(4,4)
print(arr[0:2,0:2])
print(arr)
res=arr.sum()
print(res)
res2=arr*2
print(res2)
res3=arr.dot(arr)
print(res3)
arr2=np.ones(10,dtype=int)
print(arr2)
    
