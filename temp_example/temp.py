import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

temps = np.loadtxt('temps.csv', dtype=int, delimiter=',', skiprows=1)

# Splices to get max, mean, and min array views.
max_temps = temps[:, :1]
mean_temps = temps[:, 1:2]

# Do the splice for min_temps here. It's the third column.


# Mean temperatures of the month
mean_temp = np.mean(mean_temps)
print("The mean is: " + str(mean_temp))

# Find the max temperature for the month using the max_temps array
max_temp = 
print("The max is: " + str(max_temp))

# Find the min temperature for the month using the min_temps array
min_temp = 
print("The min is: " + str(min_temp))

# Print out the standard deviation of the means




# Data is for January 2016
# numpy has datetime data types. The datetime64[D] is the datatype for days.
dates = np.arange('2016-01', '2016-02', dtype='datetime64[D]').astype(datetime)


# Subplots. One for min, max, mean
fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
ax1.plot_date(dates, mean_temps, 'g.-')
ax2.plot_date(dates, max_temps, 'b.-')

# Repeat for min_temps, make the line red


# This sets the title of the figure.
fig.suptitle('Temperatures in Laramie, WY in January 2016')

ax1.set_title('Mean')
ax2.set_title('Max')
ax3.set_title('Min')

# Only setting the y label for the middle plot, and the x label for the bottom plot.
ax2.set_ylabel('Temperature (Degrees Fahrenheit)')
ax3.set_xlabel('Day')
plt.show()


# Plot data on one graph.
plt.plot_date(dates, mean_temps, '.-', label='Mean')
plt.plot_date(dates, max_temps, '.-', label='Max')
plt.plot_date(dates, min_temps, '.-', label='Min')
plt.title('Temparatures in Laramie, WY in January 2016')
plt.ylabel('Temperature (Degrees Fahrenheit)')
plt.xlabel('Day')
# The legend is automatically generated. The labels come from the label parameter
# passed in plt.plot_date above.
plt.legend()
plt.show()

