#!/usr/bin/env python
# this file should read in the csv file, sort into time and voltage
# should also output vector of times of each heartbeat
import csv


def read_ecg(file='Test_ECG.csv'):
    with open (file) as ecg_Data_File:
        ecg_reader = csv.reader(ecg_Data_File)
    return ecg_reader


def find_range(ecg_reader, peakthresh = 0.7, basethresh = 0.1):
    time = []
    voltage = []
    for row in ecg_reader:
        time.append(row[0])
        voltage.append(row[1])
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
    return peak_times


def main():
    ecg_reader = read_ecg(file)
    peak_vector = find_range(ecg_reader)
    return peak_vector


if __name__ == "main":
    main()
