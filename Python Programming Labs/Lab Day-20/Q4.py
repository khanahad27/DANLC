#4.Calculate the total cost of items in a shopping cart, considering the quantity and price per item.
#importing the Numpy library
import numpy as np
#Initializing the arr
quantity = np.array([2, 3, 4, 1])
price_per_item = np.array([10.0, 5.0, 8.0, 12.0])
#Using sum() function to find out total cost.
total_cost = np.sum(quantity * price_per_item)
print("Total cost of items in the cart:",total_cost)


