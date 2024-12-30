#2. Calculate the profit made by a company
#importing the Numpy library
import numpy as np
#Initializing the arr
revenue = np.array([10000, 12000, 11000, 10500])
expenses = np.array([4000, 5000, 4500, 4800])
#Subtracting expenses from revenue to find out profit
profit = revenue - expenses
print("Profit for each period:", profit)
print("Total profit:", np.sum(profit))


