from read_data import read_data
from matplotlib.pyplot import plot


data = read_data("../Experimental Data/Trial 01.dat")

print(data)
print(data.events)
print(data.channel(0))