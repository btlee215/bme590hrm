class hrmcalcs:
    def __init__(self, timebeat, peak_values, start_min, end_min):
        """
        :param timebeat: amount of time between consecutive heart beats.
        Calculated by taking the difference of consecutive data points
        in the peak values vector

        :param peakvalues: array containing time points at which voltage
        condition was met to detect a heart beat. All vals are in terms of
        time(s)

        :param start_min: User-inputted value for the "starting minute" of
        average heart rate calculations, in minutes.

        :param end_min: User-inputted value for the "ending minute" of average
        heart rate calculations, in minutes.
        """
        self.timebeat = timebeat
        self.start_min = start_min
        self.end_min = end_min
        self.peak_values = peak_values
        self.instant_hr = None
        self.average_hr = None
        self.hrm_instant()
        self.hrm_average()

    def hrm_instant(self):
        """
        This method calculates the instant heart rate values from timebeat,
        the time occurrence of each heartbeat.

        :return: This method returns a stored vector of instantaneous heart
        rate values.
        """
        import numpy as np
        self.instant_hr = []
        for i in self.timebeat:
            a = round((60/i), 1)
            self.instant_hr.append(a)

    def hrm_average(self):
        """
        This method is used to calculate the average heart rate
        over a user-specified time range involving start_min and end_min.

        :return: This method returns the average heart rate
        over the user-defined range of minutes.
        """
        import numpy as np
        start_time = 60 * self.start_min
        end_time = 60 * self.end_min
        start_index = np.argmax(self.peak_values > start_time)
        end_index = np.argmax(self.peak_values > end_time)-1
        timevals = self.timebeat[start_index:(end_index-1)]
        self.average_hr = round(60/np.average(timevals), 4)
