import numpy as np

data=np.array([[1,2,3],[4,5,6]])

ones=np.ones((2,3),dtype='int64')

#Operations on the elements of the arrays.
print("Addition of each elements",data+ones)
print("Subtraction of each elements",data-ones)
print("Multiplication of each elements",data*ones)
print("Division of each elements",data/ones)

#Sum of elements of a array.
print("Sum of elements",data.sum(axis=0))  #Axis of rows of elements
print("Sum of elements",data.sum(axis=1))  #Axis of columns of elements


