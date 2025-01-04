#Importing the Pandas library
import pandas as pd
#Input data
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']
expenses = [500, 200, 1200, 300, 150]
#Creating a Pandas Series
expenses_series = pd.Series(expenses, index=categories)
#Output
print("Monthly Household Expenses:")
print(expenses_series)



