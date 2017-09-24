import hrmread
import numpy as np


def hrminstant(timebeat):
    instantHR = []
    for i in timebeat:
        a = round((60/i),1)
        instantHR.append(a)
    return instantHR


def hrmaverage(timebeat, peakvalues, start_min=1, end_min=3):
    start_time = 60 * start_min
    end_time = 60 * end_min
    start_index =  np.argmax(peakvalues > start_time)
    end_index = np.argmax(peakvalues > end_time) - 1
    timevals = timebeat[start_index:(end_index-1)]
    averageHR = round(60/np.average(timevals),4)
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
            instantHR = hrminstant(timebeat)
            averageHR = hrmaverage(timebeat, peakvalues)
            tachy, brady = hrmtb(instantHR)
    return peakvalues, instantHR, averageHR, tachy, brady

if __name__ == "__main__":
    maincalcs()

