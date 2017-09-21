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
    return time, voltage, csv_check
    # else need to insert error message here for if not a csv file!


def find_range(time, voltage, peakthresh = 0.7, basethresh = 0.1):
    toggle_peak_status = 0
    import statistics
    peak_times = []
    baseline = statistics.median(voltage)
    pos_range = max(voltage)-baseline
    for i in voltage:
        if toggle_peak_status == 0:
            if voltage[i] > (baseline + peakthresh * pos_range):
                peak_times.append(time[i])
                toggle_peak_status = 1
        if toggle_peak_status == 1:
            if voltage[i] < (baseline + basethresh * pos_range):
                toggle_peak_status = 0
        peak_vector = np.array(peak_times)
    return peak_vector


def main():
    time, voltage = read_ecg()
    peak_vector = find_range(time, voltage)
    return peak_vector

if __name__ == "main":
    main()
