import hrmread
import numpy as np

peakvalues = hrmread.main()


def hrminstant(peakvalues):
    for i in peakvalues:
        timebeat = np.diff(peakvalues)
        instantHR = 0.06/timebeat
    return instantHR


def hrmaverage(minutes):
    
    return averageHR
