import numpy as np


class TachyBrady:
    def __init__(self, instant_hr):
        self.instant_hr = instant_hr

    def tb(self, brady_limit, tachy_limit):
        tachy = []
        brady = []
        count = 0
        for i in self.instant_hr:
            if count > 1:
                if self.instant_hr[count] < brady_limit and \
                                self.instant_hr[count - 1] < brady_limit and \
                                self.instant_hr[count - 2] < brady_limit:
                    brady.append(1)
                    tachy.append(0)
                elif self.instant_hr[count] > tachy_limit and \
                                self.instant_hr[count - 1] > tachy_limit and \
                                self.instant_hr[count - 2] > tachy_limit:
                    brady.append(0)
                    tachy.append(1)
                else:
                    brady.append(0)
                    tachy.append(0)
            else:
                brady.append(0)
                tachy.append(0)
            count += 1
