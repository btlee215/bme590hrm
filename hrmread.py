#!/usr/bin/env python
# this file should read in the csv file, sort into time and voltage
# should also output vector of times of each heartbeat
import csv
import numpy as np


def read_ecg(file='Test_ECG.csv'):
    time = []
    voltage = []
    if file.endswith('.csv'):
        with open (file) as ecg_Data_File:
            ecg_reader = csv.reader(ecg_Data_File)
            next(ecg_reader)
            for row in ecg_reader:
                time.append(row[0])
                voltage.append(row[1])
        csv_check = 1
    else:
        csv_check = 0
        time = 0
        voltage = 0
        print("Error: File is not a .csv")
    return csv_check, time, voltage

    # else need to insert error message here for if not a csv file!


def check_data_type(time, voltage):
    time_type=[]
    voltage_type = []
    for i in time:
        time_type.append(type(i))
        voltage_type.append(type(voltage[time.index(i)])
    if (all(time_type == (float or int))) and (all(voltage_type == (float or int))):
        data_type = 1
    else:
        data_type = 0
        print("Error: Time or voltage vector is wrong data type")
    return data_type


def find_range(time, voltage, peakthresh = 0.7, basethresh = 0.1):
    toggle_peak_status = 0
    import statistics
    peak_times = []
    baseline = statistics.median(voltage)
    pos_range = max(voltage)-baseline
    count = 0
    for i in voltage:
        if toggle_peak_status == 0:
            if i > (baseline + peakthresh * pos_range):
                peak_times.append(time[count])
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
    csv_check, time, voltage = read_ecg()
    if csv_check == 1:
        data_type = check_data_type(time, voltage)
        if data_type == 1 :
            peak_vector = find_range(time, voltage)
        if data_type == 0:
            peak_vector = 0
    return csv_check, data_type, peak_vector

if __name__ == "main":
    main()
