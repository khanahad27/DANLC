#2. Suppose you have a dataset containing monthly sales data for a company, and you want to split this data into quarterly reports for analysis and reporting purposes. 
#importing the Numpy library
import numpy as np
#Initializing the arr
monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])
#Reshape into 4 quarters of 3 months each
quarterly_sales = monthly_sales.reshape(4, 3)
print("Quarterly sales data:\n",quarterly_sales)


