#Importing the matplotlib library
import matplotlib.pyplot as plt
#Input data
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]
#Plotting
plt.figure(figsize=(10, 5))
plt.bar(categories, expenses, color='orange')
plt.title('Monthly Expenses by Category')
plt.xlabel('Categories')
plt.ylabel('Expenses ($)')
plt.grid(axis='y')
plt.show()



