from read_data import read_data
import matplotlib.pyplot as plt
from stats import Stats


data = read_data("../Experimental Data/Trial 01.dat")

print(data)
print(data.events)

plt.figure()
print(data.events[0][0].plot())
print(Stats.moving_avg(data.events[0][0]).plot())
plt.show()