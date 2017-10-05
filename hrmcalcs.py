import hrmread
import numpy as np


def hrminstant(timebeat):
    """
    This function is used to calculate the instantaneous heart rate
    at each heartbeat detected from the CSV file.
    :param timebeat: amount of time between consecutive heart beats.
    Calculated by taking the difference of consecutive data points
    in the peak values vector
    :return: This calculation returns the instantaneous heart rate
    at each time value.

    """

    instant_hr = []
    for i in timebeat:
        a = round((60/i), 1)
        instant_hr.append(a)
    return instant_hr


def hrmaverage(timebeat, peakvalues, start_min=1, end_min=3):
    """
    This function is used to calculate the average heart rate
    over a user-specified time range.
    :param timebeat: amount of time between consecutive heart beats.
    Calculated by taking the difference of consecutive data points
    in the peak values vector
    :param peakvalues: array containing time points at which voltage c
    ondition was met to detect a heart beat. All vals are in terms of time (s)
    :param start_min: User inputs start minute of average HR calculation
    :param end_min: User inputs end minute of average HR calculation
    :return: This calculations returns the average heart rate
    over the user-defined range of minutes.

    """

    start_time = 60 * start_min
    end_time = 60 * end_min
    start_index = np.argmax(peakvalues > start_time)
    end_index = np.argmax(peakvalues > end_time) - 1
    timevals = timebeat[start_index:(end_index-1)]
    average_hr = round(60/np.average(timevals), 4)
    return average_hr


def hrmtb(instant_hr, b_thresh=60, t_thresh=100):
    """
    This function is used to detect whether a patient has bradycardia
     or tachycardia
    :param instant_hr: array of instantaneous heart rate values
    :return: This function returns arrays titled tachy and brady.
    Both arrays are filled with 0s and 1s with a 1
    representing the detection of tachycardia or bradycardia.
    Note: in order for either diagnosis to be recorded, the heart rate
    condition must be met for three consecutive heart beats.
    :param b_thresh: The threshold value for heart rate
    indicating bradycardia (default 60)
    :param t_thresh: The threshold value for heart rate
    indicating tachycardia (default 100)

    """

    tachy = []
    brady = []
    count = 0
    for i in instant_hr:
        if count > 1:
            if instant_hr[count] < b_thresh and \
                instant_hr[count - 1] < b_thresh \
                    and instant_hr[count - 2] < b_thresh:
                brady.append(1)
                tachy.append(0)
            elif instant_hr[count] > t_thresh and \
                instant_hr[count - 1] > t_thresh \
                    and instant_hr[count - 2] > t_thresh:
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
    This function is run when the hrmcalcs.py file is run in the terminal.
    It takes in the peak values vector and makes the calculations needed
    to meet the code criteria specified in the assignment.
    :return: This function returns an array with the time values at which
    heartbeats were recorded, the instant HR at each time point, the average
    heart rate over a user-specified range of minutes, and arrays indicating
    when brady or tachycardia was recorded.

    """

    csv_check, data_type, peakvalues = hrmread.main()
    if data_type == 1:
        if csv_check == 1:
            timebeat = np.diff(peakvalues)
            instant_hr = hrminstant(timebeat)
            average_hr = hrmaverage(timebeat, peakvalues)
            tachy, brady = hrmtb(instantHR)
    return peakvalues, instant_hr, average_hr, tachy, brady


if __name__ == "__main__":
    maincalcs()
