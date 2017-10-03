import hrmread
import hrmcalcs
import numpy as np


def test_read():
    """
    :return: This function is used as a unit test for the hrmread.py file. In this test, the following conditions are
    tested: whether the file input by the user is in .CSV format, whether the time and voltage values from the file are
    floats, and whether the code correctly determines the time point a beat occured at.

    """
    assert hrmread.read_ecg(file='Test_ECG.txt')== (0,0,0)  #Checks file type
    assert hrmread.check_data_type([2,"three",4],[2,3,4]) == 0 # Checks that times and voltages are floats
    assert hrmread.find_range([0,0.5,1,1.5,2.0],[10,20,30,40,50],peakthresh = 0.7,basethresh = 0.1 ) == [2.0]


def test_instant():
    """

    :return: This function is used as a unit test to ensure that the instant HR is being calculated correctly in the
    hrmcalcs.py file.

    """
    assert hrmcalcs.hrminstant(np.array([10,10,10,10])) == [6,6,6,6]


def test_average():
    """

    :return: This function is used as a unit test to ensure that the average HR is being calculated correctly in the
    hrmcalcs.py file.

    """
    assert hrmcalcs.hrmaverage([0.65, 0.70, 0.80, 0.80, 0.70],np.array([45,85,95,110,140,185]),1,3) == [80]


def test_tachbrady():
    """

    :return: This function is used as a unit test to ensure that brady and tachycardia are being accurately detected in
    the hrmcalcs.py file.

    """
    assert hrmcalcs.hrmtb([50,50,50,75,110,110,110]) ==([0,0,0,0,0,0,1],[0,0,1,0,0,0,0])
