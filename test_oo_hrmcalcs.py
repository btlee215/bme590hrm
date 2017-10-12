import csv
import numpy as np
from hrmcalcs2oo import hrmcalcs

def test_instant():
    instant = hrmcalcs([10, 10, 10, 10], np.array([45, 85, 95, 110, 140, 185]),1,3)
    assert instant.instant_hr == [6,6,6,6]

def test_average():
    instant2 = hrmcalcs([0.65, 0.70, 0.80, 0.80, 0.70], np.array([45, 85, 95, 110, 140, 185]),1,3)
    assert instant2.instant_hr == [80]

    