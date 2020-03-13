from read_data import read_data
import matplotlib.pyplot as plt
from stats import Stats
from os import path
from scipy.signal import find_peaks, peak_widths

data = None
data = read_data("../Experimental Data/Trial 25.dat")
# if not path.exists('data.pkl'):
#     with open('data.pkl', 'wb') as file:
#         pickle.dump(data, file, pickle.HIGHEST_PROTOCOL)
# else:
#     with open('data.pkl', 'rb') as file:
        # data = pickle.load(file)


# plt.figure()

# print(data)
# print(data.events)
data_stats = data.calc_stats()
def amp_freq(channel):
    # print(data.events[0][1].plot())
    amps = data_stats['single_channel'][channel]['amplitude']
    amps = amps[amps<.15]
    return amps.value_counts(
        normalize= True,
        sort= False,
        bins=250
    )

def time_gaus(chn_1,chn_2):
    return (data_stats['single_channel'][chn_1]['rise_time'] - data_stats['single_channel'][chn_2]['rise_time']).value_counts(
        normalize= True,
        sort= False,
        bins=250
    )


# amp_freq(0).plot()
# amp_freq(1).plot()
# plt.show()

plt.figure()
time_res = time_gaus(0,1)
peaks, _ = find_peaks(time_res, height=.04)
widths = peak_widths(time_res, peaks, rel_height=0.5)
time_res.plot()
plt.plot(peaks, time_res[peaks], 'x')
plt.hlines(*widths[1:], color="C2")
print("Sigma:", widths[0]/2.355) # https://en.wikipedia.org/wiki/Full_width_at_half_maximum
plt.show()