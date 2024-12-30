#3. Determine which products in a store are out of stock (quantity is 0).
#importing the Numpy library
import numpy as np
#Initializing the arr
inventory = np.array([10, 0, 5, 0, 20, 0])
#Using where() function to find out zero quatity of the product
out_of_stock_indices = np.where(inventory == 0)[0]
print("Indices of out-of-stock products:", out_of_stock_indices)


