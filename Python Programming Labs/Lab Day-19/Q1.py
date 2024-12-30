#1.How to find the mean of every NumPy array in the given list?
#importing the Numpy library
import numpy as np
#Initializing the arr
list_arr = [
    np.array([3, 2, 8, 9]),
    np.array([4, 12, 34, 25, 78]),
    np.array([23, 12, 67])
]
#Using mean() function to find out Mean.
mean = [np.mean(arr) for arr in list_arr]
print("Mean of each array:",mean)


