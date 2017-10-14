import csv
import numpy as np
from readHR import EcgReader
from hrmcalcs2oo import hrmcalcs
from hrmtb import TachyBrady


class HrmOutput:

    def __init__(self, file='Test_ECG.csv', start_min=3, end_min=5,
                 brady_limit=60, tachy_limit=100):
        self.file = file
        self.start_min = start_min
        self.end_min = end_min
        self.brady_limit = brady_limit
        self.tachy_limit = tachy_limit
        self.extract_vals()
        self.print_hrmoutput()

    def extract_vals(self):
        read_ecg = EcgReader(self.file)
        self.peak_vector = read_ecg.peak_vector
        timebeat = np.diff(read_ecg.peak_vector)
        calc_ecg = hrmcalcs(timebeat, read_ecg.peak_vector, self.start_min, self.end_min)
        calc_ecg.hrminstant()
        self.instant_hr = calc_ecg.instant_hr
        calc_ecg.hrmaverage()
        self.average_hr = calc_ecg.average_hr
        tb_ecg = TachyBrady(self.instant_hr, self.brady_limit,self.tachy_limit)
        tb_ecg.tb()
        self.tachy = tb_ecg.tachy
        self.brady = tb_ecg.brady

    def print_hrmoutput(self):
        save_name = self.file.replace(".csv", "_HRoutput.txt")
        with open(save_name, "w") as f:
            f.write("Average HR in Interval: {} \n".format(np.round(self.average_hr)))
            f.write("Time of Heartbeat (s), Instant HR, Bradycardia (0/1), "
                    "Tachycardia (0/1)\n")
            for row in list(zip(self.peak_vector, self.instant_hr, self.brady, self.tachy)):
                f.write("{},{},{},{}\n".format(np.round(row[0], 2),
                                               np.round(row[1], 2),
                                               np.round(row[2], 2),
                                               np.round(row[3], 2)))


test_ecg = HrmOutput('Test_ECG.csv', 3, 5, 60, 100)
