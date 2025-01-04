#Importing the matplotlib, numpy and pandaslibrary
import numpy as np
import matplotlib.pyplot as plt
#Sample data creation
sales_dates = np.array(['2023-01-31', '2023-02-28', '2023-03-31', '2023-04-30', 
                        '2023-05-31', '2023-06-30', '2023-07-31', '2023-08-31', 
                        '2023-09-30', '2023-10-31', '2023-11-30', '2023-12-31'])
products = np.array(['Electronics', 'Clothing', 'Home & Garden', 'Sports & Outdoors'] * 3)
regions = np.array(['North', 'South', 'East', 'West'] * 3)
sales_quantity = np.random.randint(50, 200, size=12)
price = np.random.randint(20, 500, size=12)
#Calculate total sales for each region
total_sales = sales_quantity * price
regions_unique = np.unique(regions)
sales_by_region = {region: 0 for region in regions_unique}

for i in range(len(regions)):
    sales_by_region[regions[i]] += total_sales[i]
#Plotting Bar Chart for Sales by Region
plt.figure(figsize=(10, 5))
plt.bar(sales_by_region.keys(), sales_by_region.values(), color='skyblue')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
#Plotting Pie Chart for Price Distribution
price_distribution = {}
for p in price:
    if p in price_distribution:
        price_distribution[p] += 1
    else:
        price_distribution[p] = 1
plt.figure(figsize=(8, 8))
plt.pie(price_distribution.values(), labels=price_distribution.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Price Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
plt.show()
#Plotting Line Chart for SalesDate and Prices
plt.figure(figsize=(10, 5))
for product in np.unique(products):
    product_indices = np.where(products == product)[0]
    plt.plot(sales_dates[product_indices], price[product_indices], marker='o', label=product)
plt.title('Price Trends Over Time')
plt.xlabel('Sales Date')
plt.ylabel('Price ($)')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()



