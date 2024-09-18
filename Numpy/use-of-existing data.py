import numpy as np

data = np.array([1,2,3,4,5,6,7,8,9,10])

print(data[data<=3])  #Its like print data where data value is <=3.


print(data[data%3==0])  #Its like print data where data value is completely divisble by 3.


#"Concatenation" must have homogeneous shapes.

a1=np.array([[1,2,3],[3,4,5]])
a2=np.array([[5,6,7],[8,9,10]])

result=np.concatenate((a1,a2),axis=1)

print(result)

#Add two arrays in "stack" must ahve the same shape or homogenous shapes.

#horizontal stack

print(np.hstack((a1,a2))) #Same as concatenation.

#vertical stack
print(np.vstack((a1,a2)))


