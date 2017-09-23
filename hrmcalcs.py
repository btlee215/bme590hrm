import hrmread
import numpy as np


def hrminstant(timebeat):
    instantHR = []
    for i in timebeat:
        instantHR.append(60/i)
    return instantHR


def hrmaverage(timebeat, peakvalues, minutes):
    averageHR = []
    seconds = 60*minutes # range of seconds over which to average
    # placeholder = seconds/np.array(peakvalues)
    for i in peakvalues:
        start_index =  np.argmax(peak_values > (i - seconds))
        end_index = np.argmax(peak_values > i) - 1
        timevals = timebeat[start_index:end_index]
        avetimebeat = np.average(timevals)
        averageHR.append(60/avetimebeat)
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

