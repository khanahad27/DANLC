#Importing the matplotlib library
import matplotlib.pyplot as plt
#Input data
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]
#Plotting
plt.figure(figsize=(8, 8))
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=140)
plt.title('Monthly Income Distribution by Source')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
plt.show()



