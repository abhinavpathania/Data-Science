import numpy as np

data=np.array([1,2,3,3,6,7,8,4,5,9,88,52,4,5])
weights=np.array([1,1,1,1,2,3,5,1,2,3,4,5,2,4])

print(f"The mean of the data is {np.mean(data)}")

print(f"The average of the data without weights is {np.mean(data)}")

print(f"The average of the data with weights {np.average(data,weights=weights)}")