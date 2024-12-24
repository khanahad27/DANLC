#4.Reshape a 1D array into a 2D array of shape 2x5.
#importing the Numpy library
import numpy as np
#Initializing the arr
arr = np.arange(1, 11)
#Using reshape() functionality to rebuild the array from 1D to 2D. 
reshaped_arr = arr.reshape(2, 5)
print("Reshaped 1D array into a 2D array of shape 2x5:")
print(reshaped_arr)


