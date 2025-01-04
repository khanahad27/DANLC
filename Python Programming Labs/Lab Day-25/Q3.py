#Importing the Pandas library
import pandas as pd
#Input data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']
electricity_usage = [350, 320, 310, 330, 340, 370, 380, 360, 350, 330, 320, 330]
gas_usage = [20, 18, 16, 15, 12, 10, 8, 9, 12, 15, 17, 19]
# Creating Pandas Series
electricity_series = pd.Series(electricity_usage, index=months)
gas_series = pd.Series(gas_usage, index=months)
#Output
print("Monthly Electricity Usage (kWh):")
print(electricity_series)
print("\nMonthly Gas Usage (therms):")
print(gas_series)



