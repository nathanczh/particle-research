#stats file 

import numpy as np

class CallStat(object):
    def __init__(self, params):
        self.data = []
        
##def moving_avg(channel_time(), channel_waveform(N_BINS)):
##    
##    period = 50
##    
##    for (i = 0, i < N_BINS - (period + 2), i ++):
##        
##        for (n = 1, n < period, n ++):
##            
##            channel_waveform(i) += channel_waveform(i + n)
##
##        channel_waveform(i) = channel_waveform(i) / period
##
##
##    pass
##    # doesn't return anything

if i=0 and i<1022, i++:
    if (waveform[b][2][i] > max_):
	    
            max_ = waveform[b][2][i]
	    timemax = time[b][2][i]
	    ampindex = i
	    ampindex2 = i


def rise_time(channel_time(), channel_waveform(N_BINS)):
    
    for i = 0, i < N_BINS - 2, i ++:
            if ((channel_waveform(i) < PEAK_THRESHOLD)
                and channel_waveform(i+1) >= PEAK_THRESHOLD):
                
                return (
                    (PEAK_THRESHOLD - channe_waveform(i))
                    / (channel_waveform(i + 1) - channel_waveform(i))
                    * (channel_time(i+1) -channel_time(i))
                    ) + channel_time(i)
            
        return std global numeric_limits
    
# assumes curve has been smoothed.

def peak_time(wave(N_BINS), time(N_BINS)):
    
    max_dertime = 0
    max_derivative = 0
    
    def derivatives(N_BINS):
        for i in range(0, N_BINS - 1, i ++)
            derivatives(i) = (wave(i + 1) - wave(i)) / (time(i + 1) - time(i))
    
    if ( i >= 9 ):
        
        def avg_derivative = 0
        for (j = 0, j < 10, j++):
            avg_derivative += derivatives(i - j)
        if (max_derivative < avg_derivative):
            max_derivative = avg_derivative
            max_dertime = time(i - 4)

            return max_dertime 


def amplitude(channel_waveform(N_BINS)):

        # find baseline for channel to get amplitude for that channel         sum_ = 0.0
        for i in range(0, i < 10, i++):

            sum_ += channel_waveform(i)
            
        baseline = sum_/10

        # find amplitude for channel

        max_ = -10000.0
        for i in range(0, i < N_BINS - 2, i++):
            if (channel_waveform(i) > max_):
                max_ = channel_waveform(i)


        return max_

def charge(channel_waveform(N_BINS), channel_time(N_BINS)):

    # performs Reimann sum

    sum_ = 0.0
    for i in range(0, i < N_BINS - 2, i++):
        sum_ += (channel_waveform(i) + channel_waveform(i + 1)) * (channel_time(i) + channel_time(i + 1)) / 2

    return sum_ / RESISTANCE 


    
