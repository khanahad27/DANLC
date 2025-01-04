#Importing the matplotlib and numpy library
import numpy as np
import matplotlib.pyplot as plt
#Input data
square_footage = np.array([1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000])
selling_prices = np.array([250, 290, 315, 380, 410, 450, 500, 525, 570, 610])
#Plotting
plt.figure(figsize=(10, 6))
plt.scatter(square_footage, selling_prices, color='blue', marker='o')
plt.title('House Size vs. Selling Price')
plt.xlabel('Square Footage')
plt.ylabel('Selling Price ($1000s)')
plt.grid()
plt.xticks(np.arange(1200, 3100, 200))
plt.yticks(np.arange(250, 620, 50))
plt.show()



