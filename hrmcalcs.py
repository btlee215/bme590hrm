import hrmread
import numpy as np


def hrminstant(peakvalues):
    instantHR = []
    for i in peakvalues:
        instantHR.append(60/timebeat[i])
    return instantHR


def hrmaverage(timebeat, minutes): 
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

def hrmtb(instantHR):
    tachy = []
    brady = []
    for i in instantHR:
        if i > 1:
            if i < 60 and (i-1)<60 and (i-2)<60:
                brady.append(1)
                tachy.append(0)
            elif i>100 and (i-1)>100 and (i-2)>100:
                brady.append(0)
                tachy.append(1)
            else:
                brady.append(0)
                tachy.append(0)
    return tachy, brady

def maincalcs():
    csv_check, data_type, peakvalues = hrmread.main()
    if data_type == 1:
        if csv_check == 1:
            timebeat = np.diff(peakvalues)
            instantHR = hrminstant(peakvalues)
            averageHR = hrmaverage(timebeat,2)
            tachy, brady = hrmtb(instantHR)
    return instantHR, averageHR, tachy, brady

if __name__ == "main":
    maincalcs()

