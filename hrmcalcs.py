import hrmread
import numpy as np


def hrminstant(timebeat):
    """
    This function is used to calculate the instantaneous heart rate at each time point in the CSV file.
    :param timebeat: amount of time between consecutive heart beats. Calculated by taking the difference of consecutive
    data points in the peak values vector
    :return: This calculation returns the instantaneous heart rate at each time value.

    """

    instantHR = []
    for i in timebeat:
        a = round((60/i),1)
        instantHR.append(a)
    return instantHR


def hrmaverage(timebeat, peakvalues, start_min=1, end_min=3):
    """
    This function is used to calculate the average heart rate over a user-specified time range.
    :param timebeat: amount of time between consecutive heart beats. Calculated by taking the difference of consecutive
    data points in the peak values vector
    :param peakvalues: array containing time points at which voltage condition was met to detect a heart beat. All vals
    are in terms of time (s)
    :param start_min: User-inputted value for the start minute of average HR calculation
    :param end_min: User-inputted value for the end minute of average HR calculation
    :return: This calculations returns the average heart rate over the user-defined range of minutes.

    """

    start_time = 60 * start_min
    end_time = 60 * end_min
    start_index =  np.argmax(peakvalues > start_time)
    end_index = np.argmax(peakvalues > end_time) - 1
    timevals = timebeat[start_index:(end_index-1)]
    averageHR = round(60/np.average(timevals),4)
    return averageHR

def hrmtb(instantHR):
    """
    This function is used to detect whether a patient has brady (heart rate less than 60) or tachycardia (heart rate
    above 100)
    :param instantHR: array of instantaneous heart rate values
    :return: This function returns arrays titled tachy and brady. Both arrays are filled with 0s and 1s with a 1
    representing the detection of tachycardia or bradychardia. Note: in order for either diagnosis to be recorded, the
    heart rate condition must be met for three consecutive heart beats.

    """

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
    """
    This function is run when the hrmcalcs.py file is run in the terminal. It takes in the peak values vector and makes
    the calculations needed to meet the code criteria specified in the assignment.
    :return: This function returns an array with the time values at which heartbeats were recorded, the instant HR at
    each time point, the average heart rate over a user-specified range of minutes, and arrays indicating when brady or
    tachycardia was recorded.

    """

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

