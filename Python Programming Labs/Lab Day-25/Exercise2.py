#Importing the Pandas, Numpy and Matplotlib library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Sample data: Daily closing prices for a year
dates = pd.date_range(start='2023-01-01', periods=365, freq='D')
closing_prices = [100 + (x * 0.1) + (5 * np.random.randn()) for x in range(365)]  #Simulated prices
#Creating a DataFrame
stock_data = pd.DataFrame({'Date': dates, 'Closing Price': closing_prices})
stock_data.set_index('Date', inplace=True)
#Calculate average daily return
stock_data['Daily Return'] = stock_data['Closing Price'].pct_change()
average_daily_return = stock_data['Daily Return'].mean()
#Find the date with the highest closing price
max_price_date = stock_data['Closing Price'].idxmax()
max_price_value = stock_data['Closing Price'].max()
#Plotting the closing prices
plt.figure(figsize=(12, 6))
plt.plot(stock_data.index, stock_data['Closing Price'], label='Closing Price', color='blue')
plt.title('Daily Closing Prices Over a Year')
plt.xlabel('Date')
plt.ylabel('Closing Price ($)')
plt.xticks(rotation=45)
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
#Output results
print(f"Average Daily Return: {average_daily_return:.4f}")
print(f"Date with Highest Closing Price: {max_price_date.date()} at ${max_price_value:.2f}")



