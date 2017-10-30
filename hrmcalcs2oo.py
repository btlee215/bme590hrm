class hrmcalcs:
    def __init__(self, time, timebeat, peak_values, average_window):
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
        self.time = time
        self.timebeat = timebeat
        self.average_window = average_window
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
        count_index = 0
        instant_hr = 0
        for i in self.time:
            if i == self.peak_values[count_index]:
                if count_index != 0:
                    instant_hr = round((60/self.timebeat[count_index - 1]),1)
                count_index += 1
            self.instant_hr.append(round(instant_hr, 1))
        return self.instant_hr

    def hrm_average(self):
        """
        This method is used to calculate the average heart rate
        over a user-specified time range involving start_min and end_min.

        :return: This method returns the average heart rate
        over the user-defined range of minutes.
        """
        import numpy as np
        self.average_hr = []
        toggle_first_heartbeat = False
        average_hr = 0
        for i in self.time:
            if i >= self.peak_values[1]:
                toggle_first_heartbeat = True
            if toggle_first_heartbeat:
                if (i - self.average_window) > 0:
                    start_index = np.argmax(np.array(self.peak_values) >= (i - self.average_window))
                    end_index = np.argmax(np.array(self.peak_values) > i)-1
                else:
                    start_index = 0
                    end_index = np.argmax(np.array(self.peak_values) > i) - 1
                if (end_index < 1):
                    end_index = len(np.array(self.peak_values))
                if (end_index - 1) > start_index:
                    timevals = self.timebeat[(start_index):(end_index)]
                else:
                    if start_index == (len(np.array(self.peak_values)) - 1):
                        start_index = start_index - 1
                    timevals = self.timebeat[start_index]
                average_hr = 60/np.average(timevals)
            self.average_hr.append(round(average_hr, 0))
        return self.average_hr
