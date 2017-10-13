import numpy as np


class TachyBrady:
    def __init__(self, instant_hr, brady_limit, tachy_limit):
        self.instant_hr = instant_hr
        self.brady_limit = brady_limit
        self.tachy_limit = tachy_limit
        self.tachy = []
        self.brady = []

    def tb(self):
        count = 0
        for i in self.instant_hr:
            if count > 1:
                if self.instant_hr[count] < self.brady_limit and \
                                self.instant_hr[count - 1] < self.brady_limit and \
                                self.instant_hr[count - 2] < self.brady_limit:
                    self.brady.append(1)
                    self.tachy.append(0)
                elif self.instant_hr[count] > self.tachy_limit and \
                                self.instant_hr[count - 1] > self.tachy_limit and \
                                self.instant_hr[count - 2] > self.tachy_limit:
                    self.brady.append(0)
                    self.tachy.append(1)
                else:
                    self.brady.append(0)
                    self.tachy.append(0)
            else:
                self.brady.append(0)
                self.tachy.append(0)
            count += 1
