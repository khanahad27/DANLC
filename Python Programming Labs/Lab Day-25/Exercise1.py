#Importing the Pandas, Numpy and Matplotlib library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Sample data creation
#Generate a date range for January 2023
dates = pd.date_range(start='2023-01-01', end='2023-01-31', freq='B')  # Business days in January
#Generate random opening prices between 100 and 200
opening_prices = np.random.uniform(100, 200, size=len(dates))
#Generate random closing prices based on opening prices
closing_prices = opening_prices + np.random.uniform(-10, 10, size=len(dates))  # Random fluctuation
#Create DataFrame
stock_data = pd.DataFrame({
    'Date': dates,
    'Opening Price': opening_prices,
    'Closing Price': closing_prices
})
#Set Date as index
stock_data.set_index('Date', inplace=True)
#Plotting
plt.figure(figsize=(12, 6))
plt.plot(stock_data.index, stock_data['Opening Price'], label='Opening Price', color='blue', marker='o')
plt.plot(stock_data.index, stock_data['Closing Price'], label='Closing Price', color='orange', marker='o')
plt.title('SBI Stock Prices in January 2023')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()