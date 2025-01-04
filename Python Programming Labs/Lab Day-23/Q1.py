#Importing the matplotlib library
import matplotlib.pyplot as plt
#Input data
days = list(range(1, 32))
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78,
               80, 81, 82, 83, 82, 80, 78, 76, 74, 71]
#Plotting
plt.figure(figsize=(10, 5))
plt.plot(days, temperature, marker='o', color='b')
plt.title('Daily Temperature Changes Over Time')
plt.xlabel('Days')
plt.ylabel('Temperature (°F)')
plt.xticks(days)
plt.grid()
plt.show()


