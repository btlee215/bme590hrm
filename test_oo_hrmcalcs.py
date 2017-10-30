import csv
import numpy as np
from hrmcalcs2oo import hrmcalcs


def test_instant():
    instant = hrmcalcs([45, 85, 95, 110, 140, 185], [10, 10, 10, 10, 10],
                       np.array([45, 85, 95, 110, 140, 185]), 20)
    assert instant.instant_hr == [0, 6, 6, 6, 6, 6]


def test_average():
    instant2 = hrmcalcs([45, 85, 95, 110, 140, 185], [0.65, 0.70, 0.80, 0.80, 0.70],
                        np.array([45, 85, 95, 110, 140, 185]), 86)
    assert instant2.average_hr == [0, 92, 89, 84, 78, 80]
