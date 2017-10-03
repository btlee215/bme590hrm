import numpy as np


class TachyBrady:
    def __init__(self, instantHR):
        self.instantHR = instantHR

    def tb(self):
        tachy = []
        brady = []
        count = 0
        for i in self.instantHR:
            if count > 1:
                if self.instantHR[count] < 60 and self.instantHR[count - 1] < 60 and self.instantHR[count - 2] < 60:
                    brady.append(1)
                    tachy.append(0)
                elif self.instantHR[count] > 100 and self.instantHR[count - 1] > 100 and self.instantHR[count - 2] > 100:
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
