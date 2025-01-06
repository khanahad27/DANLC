#Importing the Pandas, Numpy and Matplotlib library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Sample sales data
data = {
    'Customer': ['Alice', 'Bob', 'Alice', 'David', 'Bob', 'Alice', 'David'],
    'Product': ['A', 'B', 'A', 'C', 'A', 'C', 'B'],
    'Quantity': [2, 3, 1, 2, 2, 1, 4],
    'Price': [50, 30, 50, 100, 50, 100, 30],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-02', '2023-01-04', '2023-01-01']
}
#Create DataFrame
df = pd.DataFrame(data)
#Add revenue column
df['Revenue'] = df['Quantity'] * df['Price']
#Total revenue
total_revenue = df['Revenue'].sum()
print("Total revenue for the year:", total_revenue)
#Average revenue per sale
average_revenue = df['Revenue'].mean()
print("Average revenue per sale:", average_revenue)
#Best-selling product
best_selling_product = df.groupby('Product')['Quantity'].sum().idxmax()
print("Best-selling product:", best_selling_product)
#Date with highest total revenue
date_highest_revenue = df.groupby('Date')['Revenue'].sum().idxmax()
print("Date with highest total revenue:", date_highest_revenue)
#Bar chart: Product-wise total sales
df.groupby('Product')['Quantity'].sum().plot(kind='bar', title='Total Sales by Product', color='skyblue')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()
#Bar chart: Total revenue per date
df.groupby('Date')['Revenue'].sum().plot(kind='bar', title='Total Revenue by Date', color='green')
plt.xlabel('Date')
plt.ylabel('Total Revenue')
plt.show()



