#Importing the matplotlib library
import matplotlib.pyplot as plt
#Sample data
regions = ['North', 'South', 'East', 'West']
sales = [25000, 30000, 15000, 20000]
#Calculate total sales and percentages
total_sales = sum(sales)
percentages = [(sale / total_sales) * 100 for sale in sales]
#Plotting the bar chart
plt.figure(figsize=(10, 5))
bars = plt.bar(regions, sales, color='skyblue')
#Adding percentage labels on top of the bars
for bar, percentage in zip(bars, percentages):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{percentage:.1f}%', ha='center', va='bottom')
plt.title('Sales by Region')
plt.xlabel('Regions')
plt.ylabel('Sales ($)')
plt.grid(axis='y')
plt.show()



