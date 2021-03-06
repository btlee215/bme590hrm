class TachyBrady:
    def __init__(self, instant_hr, brady_limit=60, tachy_limit=100):
        """
        :param instant_hr: Takes instant_hr vector from hrmcalcs200, a stored
        vector of instantaneous heart rate values

        :param brady_limit: The threshold value for bradycardia, with the
        default set at 60 bpm

        :param tachy_limit: The threshold value for tachycardia, with the
        default set at 100 bpm

        """
        import numpy as np
        self.instant_hr = instant_hr
        self.brady_limit = brady_limit
        self.tachy_limit = tachy_limit
        self.tachy = []
        self.brady = []

    def tb(self):
        """
        This method determines the occurrence of tachycardia and/or
        bradycardia.

        :return: This method appends the resulting time values associated with
        heart beats onto an array called peak_vector.
        """
        count = 0
        for i in self.instant_hr:
            if count > 1:
                if self.instant_hr[count] < self.brady_limit and \
                        self.instant_hr[count - 1] < self.brady_limit and \
                        self.instant_hr[count - 2] < self.brady_limit:
                    self.brady.append(True)
                    self.tachy.append(False)
                elif self.instant_hr[count] > self.tachy_limit and \
                        self.instant_hr[count - 1] > self.tachy_limit and \
                        self.instant_hr[count - 2] > self.tachy_limit:
                    self.brady.append(False)
                    self.tachy.append(True)
                else:
                    self.brady.append(False)
                    self.tachy.append(False)
            else:
                self.brady.append(False)
                self.tachy.append(False)
            count += 1
        return self.tachy, self.brady
