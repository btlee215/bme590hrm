import hrmread
import numpy as np


def hrminstant(timebeat):
    instantHR = []
    for i in timebeat:
        instantHR.append(60/i)
    return instantHR


def hrmaverage(timebeat, peakvalues, start_min, end_min):
    averageHR = []
    start_time = 60*start_min # range of seconds over which to average
    end_time = 60*end_min
    # placeholder = seconds/np.array(peakvalues)
    start_index =  np.argmax(peak_values > start_time)
    end_index = np.argmax(peak_values > end_time) - 1
    timevals = timebeat[start_index:end_index]
    averageHR = np.average(timevals)
    return averageHR

def hrmtb(instantHR):
    tachy = []
    brady = []
    count = 0
    for i in instantHR:
        if count > 1:
            if instantHR[count] < 60 and instantHR[count-1]<60 and instantHR[count-2]<60:
                brady.append(1)
                tachy.append(0)
            elif instantHR[count]>100 and instantHR[count-1]>100 and instantHR[count-2]>100:
                brady.append(0)
                tachy.append(1)
            else:
                brady.append(0)
                tachy.append(0)
        else:
            brady.append(0)
            tachy.append(0)
        count += 1

    return tachy, brady

def maincalcs():
    csv_check, data_type, peakvalues = hrmread.main()
    if data_type == 1:
        if csv_check == 1:
            timebeat = np.diff(peakvalues)
            instantHR = hrminstant(timebeat, peakvalues)
            averageHR = hrmaverage(timebeat, peakvalues, 2)
            tachy, brady = hrmtb(instantHR)
    return instantHR, averageHR, tachy, brady

if __name__ == "main":
    maincalcs()

