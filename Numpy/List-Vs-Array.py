import time
import numpy as np

size =100000

#list

list1=range(size)
list2=range(size)
start=time.time()
result=[[x+y] for x,y in zip(list1,list2)]
print("List took ",(time.time()-start)*1000)

#array

start=time.time()
arr1=np.arange(size)
arr2=np.arange(size)
result=arr1+arr2
print("Array took" ,(time.time()-start)*1000)