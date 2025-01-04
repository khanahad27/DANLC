#Importing the matplotlib library
import matplotlib.pyplot as plt
#Input data
product_prices = [24.99, 34.99, 49.99, 64.99, 39.99, 54.99, 79.99, 99.99, 29.99, 44.99, 
                  59.99, 69.99, 84.99, 109.99, 119.99, 89.99, 74.99, 124.99, 69.99, 54.99]
#Plotting
plt.figure(figsize=(10, 5))
plt.hist(product_prices, bins=10, color='purple', edgecolor='black')
plt.title('Distribution of Product Prices')
plt.xlabel('Price ($)')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()


