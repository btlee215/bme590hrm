import numpy as np

class hrmcalcs:
    def __init__(self, timebeat, peakvalues, start_min, end_min):
        self.timebeat = timebeat
        self.start_min = start_min
        self.end_min = end_min
        self.peakvalues = peakvalues

    def hrminstant(self):
        instantHR = []
        for i in self.timebeat:
            a = round((60/i), 1)
            instantHR.append(a)
        return instantHR

    def hrmaverage(self):
        start_time = 60 * self.start_min
        end_time = 60 * self.end_min
        start_index = np.argmax(self.peakvalues > start_time)
        end_index = np.argmax(self.peakvalues > end_time)-1
        timevals = self.timebeat[start_index:(end_index-1)]
        averageHR = round(60/np.average(timevals), 4)
        return averageHR