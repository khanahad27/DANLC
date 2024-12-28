#1. Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 
#importing the Numpy library
import numpy as np
#Initializing the arr
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])
#Find hot days (temperature > 35)
hot_days = temperatures > 35
#Find cold days (temperature < 5)
cold_days = temperatures < 5
print("Hot days (temperature > 35):",np.where(hot_days)[0])
print("Cold days (temperature < 5):",np.where(cold_days)[0])


