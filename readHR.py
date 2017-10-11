#!/usr/bin/env python
# this file should read in the csv file, sort into time and voltage
# should also output vector of times of each heartbeat
import csv
import numpy as np


class EcgReader():
    """
       This function takes in ECG data from a CSV file inputted by the user, reads it and separates the data into time and
       voltage.
       :param file: A CSV file being tested by the user
       :return: If the file is not a CSV, the function will raise "Error: File is not a .csv". For CSV files, the function
       will return a separate time and voltage array with values extracted from the data file.

       """

    def __init__(self, file):
        self.filecheck(file)
        self.readFile()
        self.dataCheck()
        if self.data_type == 1 and self.csv_check == 1:
            self.findRange()


    def filecheck(self, file):
        self.file = file
        if file.endswith('.csv'):
            self.csv_check = 1
        else:
            self.csv_check = 0
            self.time = 0
            self.voltage = 0
            print("Error: File is not a .csv")


    def readFile(self):
        self.time = []
        self.voltage = []
        if self.file.endswith('.csv'):
            with open (self.file) as ecg_Data_File:
                ecg_reader = csv.reader(ecg_Data_File)
                next(ecg_reader)
                for row in ecg_reader:
                    try:
                        u = float(row[0])
                        self.time.append(u)
                    except:
                        self.time.append(row[0])
                    try:
                        v = float(row[1])
                        self.voltage.append(v)
                    except:
                        self.voltage.append(row[1])

    def dataCheck(self):
        """
            This function takes in the time and voltage arrays and ensures that the data type for every element is a float.
            :param time: Array of time values from .CSV file and returned in an array by read_ecg file
            :param voltage: Array of voltage values from .CSV file and returned in an array by read_ecg file
            :return: If a particular element in time or voltage is not a float, the function will raise "Error: Time vector is
            wrong data type".

            """
        self.data_type = 1
        for i in self.time:
            if type(i) == str:
                self.data_type = 0
                print("Error: Time vector is wrong data type")
                break
        for j in self.voltage:
            if type(j) == str:
                self.data_type = 0
                print("Error: Voltage vector is wrong data type")
                break


    def findRange(self, peakthresh = 0.9, basethresh = 0.1):

        toggle_peak_status = 0
        import statistics
        peak_times = []
        baseline = statistics.median(self.voltage)
        pos_range = max(self.voltage)-baseline
        count = 0
        for i in self.voltage:
            if toggle_peak_status == 0:
                if i > (baseline + peakthresh * pos_range):
                    peak_times.append(round(self.time[count],2))
                    toggle_peak_status = 1
                    count += 1
            if toggle_peak_status == 1:
                if i < (baseline + basethresh * pos_range):
                    toggle_peak_status = 0
                    count += 1
            else:
                count += 1
            self.peak_vector = np.array(peak_times)