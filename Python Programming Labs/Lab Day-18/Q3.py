#3. Suppose you have a dataset containing customer data, and you want to split this data into two groups: one group for customers who made a purchase in the last 30 days and another group for customers who haven't made a purchase in the last 30 days.  
#importing the Numpy library
import numpy as np
#Initializing the arr
customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])
#Customers who purchased in the last 30 days
recent_purchases = customer_ids[last_purchase_days_ago <= 30]
#Customers who haven't purchased in the last 30 days
no_recent_purchases = customer_ids[last_purchase_days_ago > 30]
print("Customers who purchased in the last 30 days:", recent_purchases)
print("Customers who haven't purchased in the last 30 days:", no_recent_purchases)


