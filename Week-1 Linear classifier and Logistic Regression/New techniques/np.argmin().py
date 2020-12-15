import numpy as np
list1=[90,32,89,21]
print(list1[-2:])
print(np.argmin(list1)) # least element(21) present in 3rd index position

list2=[[12,31,23,67],[89,45,21,34],[56,25,78,96]]
print(*np.argmin(list2,axis=1))  # Row-wise
print(*np.argmin(list2,axis=0))  # Column-wise