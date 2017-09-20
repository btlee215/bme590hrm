import hrmread
import numpy as np

peakvalues = hrmread.main()
timebeat = np.diff(peakvalues)
instantHR = []


def hrminstant(peakvalues):
    for i in peakvalues:
        instantHR.append(60/timebeat[i])
    return instantHR

def hrmaverage(minutes):
    seconds = 60*minutes
    placeholder = seconds/np.array(peakvalues)
    index = (np.abs(placeholder-1)).argmin()
    timevals = timebeat[:index]
    avetimebeat = np.average(timevals)
    averageHR = 60/avetimebeat
    return averageHR

def maincalcs():
    instantHR = hrminstant(peakvalues)
    averageHR = hrmaverage(minutes)


if __name__ == "main":
    maincalcs()
