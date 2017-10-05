import numpy as np


class TachyBrady:
    def __init__(self, instantHR):
        self.instantHR = instantHR

    def tb(self, brady_limit=60, tachy_limit=100):
        tachy = []
        brady = []
        count = 0
        for i in self.instantHR:
            if count > 1:
                if self.instantHR[count] < brady_limit and \
                                self.instantHR[count - 1] < brady_limit and \
                                self.instantHR[count - 2] < brady_limit:
                    brady.append(1)
                    tachy.append(0)
                elif self.instantHR[count] > tachy_limit and \
                                self.instantHR[count - 1] > tachy_limit and \
                                self.instantHR[count - 2] > tachy_limit:
                    brady.append(0)
                    tachy.append(1)
                else:
                    brady.append(0)
                    tachy.append(0)
            else:
                brady.append(0)
                tachy.append(0)
            count += 1
        return tachy, brady
