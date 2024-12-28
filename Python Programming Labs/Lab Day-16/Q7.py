#7.Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.
#importing the Numpy library
import numpy as np
#Initializing the list
list = [1, 2, 3, 4, 5]
#Initializing the arr
numpy_array = np.array(list)
first_index = numpy_array[0]
last_index = numpy_array[-1]
multiplied_array = numpy_array * 2
print("Numpy array:", numpy_array)
print("First index:", first_index)
print("Last index:", last_index)
print("Array with each element multiplied by 2:", multiplied_array)


