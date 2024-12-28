#4.Write a NumPy program to convert a list and tuple into arrays.
#importing the Numpy library
import numpy as np
#Initializing the arr
list = [1, 2, 3, 4, 5, 6, 7, 8]
tuple = ([8, 4, 6], [1, 2, 3])
#Converting list and tuple 
list_arr = np.array(list)
tuple_arr = np.array(tuple)
print("Array from list:", list_arr)
print("Array from tuple:\n",tuple_arr)


