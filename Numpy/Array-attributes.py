import numpy as np

#Dimensions of the  array

size=10
#1-dimensional array
a=np.arange(size)
print(a.ndim)

#2-dimensional array
b=np.array([[1,2,3,4,5,6,7,8,9,10],
   [11,12,13,14,15,16,17,18,19,20]])

print(b.ndim)

#Shape of the array

print(a.shape)
print(b.shape)#(1,10) (rows,columns)

#Empty array

a=np.empty(size,dtype="float")
print(a)

#Array filled with zeros

a=np.zeros(size,dtype="bool")
print(a)

#Array filled with ones

a=np.ones(size,dtype="str")
print(a)

#Array range

a=np.arange(1,100,2)
print(a)

#Reshape of the array

b=a.reshape(10,5)
print(b)

#Slice of the array

data = np.array([1,2,3,4,5,6,7,8,9,10])

#same output
print(data[1:])
print(data[-2:])
