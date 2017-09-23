import hrmread
import hrmcalcs
import numpy as np


def test_read():
    assert hrmread.read_ecg(file='Test_ECG.txt')== (0,0,0)  #Checks file type
    assert hrmread.check_data_type([2,"3",4],[2,3,4]) == 0 # Checks that times and voltages are floats
    assert hrmread.find_range([0,0.5,1,1.5,2.0],[10,20,30,40,50],peakthresh = 0.7,basethresh = 0.1 ) == [2.0]


def test_instant():
    assert hrmcalcs.hrminstant(np.array([10,10,10,10])) == [6,6,6,6]


def test_average():
    assert hrmcalcs.hrmaverage([0.65, 0.70, 0.80, 0.80, 0.70],np.array([45,85,95,110,140,185]),1,3) == [80]


def test_tachbrady():
    assert hrmcalcs.hrmtb([50,50,50,75,110,110,110]) ==([0,0,0,0,0,0,1],[0,0,1,0,0,0,0])

