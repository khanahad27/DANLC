#Importing the matplotlib library
import matplotlib.pyplot as plt
#Input data
segments = ['Product A', 'Product B', 'Services', 'Licensing']
revenue_percentages = [45, 25, 15, 15]
#Plotting
plt.figure(figsize=(8, 8))
plt.pie(revenue_percentages, labels=segments, autopct='%1.1f%%', startangle=140)
plt.title('Company Revenue Distribution by Segment')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
plt.show()



