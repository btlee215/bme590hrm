#!/usr/bin/env python
# this file should read in the csv file, sort into time and voltage
# should also output vector of times of each heartbeat
import csv
import numpy as np


def read_ecg(file='Test_ECG.csv'):
    """
    This function takes in ECG data from a CSV file inputted by the user, reads it and separates the data into time and
    voltage.
    :param file: A CSV file being tested by the user
    :return: If the file is not a CSV, the function will raise "Error: File is not a .csv". For CSV files, the function
    will return a separate time and voltage array with values extracted from the data file.

    """

    time = []
    voltage = []
    if file.endswith('.csv'):
        with open (file) as ecg_Data_File:
            ecg_reader = csv.reader(ecg_Data_File)
            next(ecg_reader)
            for row in ecg_reader:
                time.append(float(row[0]))
                voltage.append(float(row[1]))
        csv_check = 1
    else:
        csv_check = 0
        time = 0
        voltage = 0
        print("Error: File is not a .csv")
    return csv_check, time, voltage


def check_data_type(time, voltage):
    """
    This function takes in the time and voltage arrays and ensures that the data type for every element is a float.
    :param time: Array of time values from .CSV file and returned in an array by read_ecg file
    :param voltage: Array of voltage values from .CSV file and returned in an array by read_ecg file
    :return: If a particular element in time or voltage is not a float, the function will raise "Error: Time vector is
    wrong data type".

    """

    data_type = 1
    for i in time:
        if type(i) != 'float':
            data_type = 1
            print("Error: Time vector is wrong data type")
            break
    for j in voltage:
        if type(j) != 'float':
            data_type = 1
            print("Error: Voltage vector is wrong data type")
            break
    return data_type


def find_range(time, voltage, peakthresh = 0.9, basethresh = 0.1):
    """

    :param time:
    :param voltage:
    :param peakthresh:
    :param basethresh:
    :return:

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
                peak_times.append(round(time[count],2))
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


def main():
    """

    :return:

    """

    csv_check, time, voltage = read_ecg()
    if csv_check == 1:
        data_type = check_data_type(time, voltage)
        if data_type == 1 :
            peak_vector = find_range(time, voltage)
        if data_type == 0:
            peak_vector = 0
    return csv_check, data_type, peak_vector


if __name__ == "__main__":
    main()
