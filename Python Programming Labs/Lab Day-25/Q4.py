#Importing the Pandas library
import pandas as pd
# Input data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']
revenue = [5000, 5200, 4800, 5400, 5600, 5800, 6100, 5900, 6200, 6500, 7000, 6900]
# Creating a Pandas Series
revenue_series = pd.Series(revenue, index=months)
# Output
print("Monthly Advertising Revenue:")
print(revenue_series)



