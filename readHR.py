import csv
import numpy as np


class EcgReader:

    def __init__(self, file):
        self.file = file
        self.csv_check = True
        self.data_type = True
        self.time = []
        self.voltage = []
        self.peak_vector = []
        self.filecheck()
        if self.csv_check:
            self.readfile()
            self.datacheck()
        if self.data_type and self.csv_check :
            self.findrange()

    def filecheck(self):
        """
            This method takes in ECG data from a CSV file inputted by the user,
            and checks that it is the correct file format.

            :return: If the file is not a CSV, the function will raise
            "Error: File is not a .csv". For CSV files, the initialization
            will move on to the next step.

        """
        if self.file.endswith('.csv'):
            self.csv_check = True
        else:
            self.csv_check = False
            self.time = None
            self.voltage = None
            print("Error: File is not a .csv")

    def readfile(self):
        """
        This method reads the contents of the csv file and attempts to convert
        numeric strings into floats before adding to time and voltage vectors.

        :return: Time and voltage vectors with each entry from columns in the
        original csv file.
        """
        if self.file.endswith('.csv'):
            with open(self.file) as ecg_Data_File:
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

    def datacheck(self):
        """
            This method takes in the time and voltage arrays and ensures that
            the data type for every element is a float.

            :param self.time: Array of time values from .CSV file assigned to class

            :param self.voltage: Array of voltage values from .CSV file assigned to
            object of class EcgReader

            :return: If a particular element in time or voltage is not a float,
            the function will raise "Error: Time vector is wrong data type".

            :return: self.data_type is a 1 if numeric and 0 if any entries are
            strings. If data_type is 0, some of the remaining initialization
            steps will not be performed.

            """
        for i in self.time:
            if type(i) == str:
                self.data_type = False
                print("Error: Time vector is wrong data type")
                break
        for j in self.voltage:
            if type(j) == str:
                self.data_type = False
                print("Error: Voltage vector is wrong data type")
                break

    def findrange(self, peakthresh=0.9, basethresh=0.1):

        toggle_peak_status = False
        import statistics
        peak_times = []
        baseline = statistics.median(self.voltage)
        pos_range = max(self.voltage)-baseline
        count = 0
        for i in self.voltage:
            if toggle_peak_status == False:
                if i > (baseline + peakthresh * pos_range):
                    peak_times.append(round(self.time[count], 2))
                    toggle_peak_status = True
                    count += 1
            if toggle_peak_status == True:
                if i < (baseline + basethresh * pos_range):
                    toggle_peak_status = False
                    count += 1
            else:
                count += 1
            self.peak_vector = np.array(peak_times)
