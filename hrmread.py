#!/usr/bin/env python
# this file should read in the csv file, sort into time and voltage
# should also output vector of times of each heartbeat
import csv
import numpy as np

def read_ecg(file):
    """
    This function takes in ECG data from a CSV file inputted by the user,
    reads it and separates the data into time and voltage.

    :param file: A CSV file being tested by the user

    :return: If the file is not a CSV, the function will raise
    "Error: File is not a .csv". For CSV files, the function will return a
    separate time and voltage array with values extracted from the data file.

    """

    time = []
    voltage = []
    if file.endswith('.csv'):
        with open(file) as ecg_Data_File:
            ecg_reader = csv.reader(ecg_Data_File)
            next(ecg_reader)
            for row in ecg_reader:
                try:
                    u = float(row[0])
                    time.append(u)
                except:
                    time.append(row[0])
                try:
                    v = float(row[1])
                    voltage.append(v)
                except:
                    voltage.append(row[1])
        csv_check = 1
    else:
        csv_check = 0
        time = 0
        voltage = 0
        print("Error: File is not a .csv")
    return csv_check, time, voltage


def check_data_type(time, voltage):
    """
    This function takes in the time and voltage arrays and ensures that the
    data type for every element is a float.

    :param time: Array of time values from .CSV file and returned in an array
    by read_ecg file
    :param voltage: Array of voltage values from .CSV file and returned in an
    array by read_ecg file

    :return: If a particular element in time or voltage is not a float, the
    function will raise "Error: Time vector is wrong data type".

    """

    data_type = 1
    for i in time:
        if type(i) == str:
            data_type = 0
            print("Error: Time vector is wrong data type")
            break
    for j in voltage:
        if type(j) == str:
            data_type = 0
            print("Error: Voltage vector is wrong data type")
            break
    return data_type


def find_range(time, voltage, peakthresh=0.9, basethresh=0.1):
    """
    This function is used to determine the range of what is considered a
    heartbeat. The peak and base thresholds have been set in order to use the
    toggle_peak_status variable to detect the time values where a beat occurs.

    :param time: Time in seconds as output by the read_ecg function
    :param voltage: Voltage in volts as output by the read_ecg function
    :param peakthresh: User-inputted peak threshold value. Default is 0.9
    :param basethresh: User-inputted base threshold value. Default is 0.1

    :return: This function will return an array titled peak_vector with the
    time values at which heart beats were detected.

    """

    toggle_peak_status = 0
    import statistics
    peak_times = []
    baseline = statistics.median(voltage)
    pos_range = max(voltage)-baseline
    count = 0
    for i in voltage:
        if toggle_peak_status == 0:
            if i > (baseline + peakthresh * pos_range):
                peak_times.append(round(time[count], 2))
                toggle_peak_status = 1
                count += 1
        if toggle_peak_status == 1:
            if i < (baseline + basethresh * pos_range):
                toggle_peak_status = 0
                count += 1
        else:
            count += 1
        peak_vector = np.array(peak_times)
    return peak_vector


def main(file):
    """
    This function is run when the hrmread.py file is run and reads the file,
    checks the data type of the time and voltage variables, and finds the
    time values at which a heartbeat occured.

    :return: This function will return the value of the csv_check variable,
    the data_type variable and the peak vector, which shows the time points
    at which a beat was detected

    """
    import csv
    import numpy as np
    csv_check, time, voltage = read_ecg(file)
    if csv_check == 1:
        data_type = check_data_type(time, voltage)
        if data_type == 1:
            peak_vector = find_range(time, voltage)
        if data_type == 0:
            peak_vector = 0
    return csv_check, data_type, peak_vector


if __name__ == "__main__":
    main()
