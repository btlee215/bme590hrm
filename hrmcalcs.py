import hrmread
import numpy as np


def hrminstant(peakvalues):
    instantHR = []
    for i in peakvalues:
        instantHR.append(60/timebeat[i])
    return instantHR


def hrmaverage(minutes = 2, timebeat):
    averageHR = []
    seconds = 60*minutes # range of seconds over which to average
    # placeholder = seconds/np.array(peakvalues)
    for i in peakvalues:
        start_index =  np.argmax(peak_values > (peakvalues[i] - seconds))
        end_index = np.argmax(peak_values > peak_values[i]) - 1
        timevals = timebeat[start_index:end_index]
        avetimebeat = np.average(timevals)
        averageHR[i] = 60/avetimebeat
    return averageHR


def maincalcs():
    peakvalues = hrmread.main()
    timebeat = np.diff(peakvalues)
    instantHR = hrminstant(peakvalues)
    averageHR = hrmaverage(minutes, timebeat)
    return instantHR, averageHR

if __name__ == "main":
    maincalcs()
