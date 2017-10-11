import csv
import numpy as np
from readHR import EcgReader


def test_filecheck():
    """
    :return: This function is used as a unit test for the hrmread.py file.
    In this test, the following conditions are tested: whether the file
    input by the user is in .CSV format, whether the time and voltage
    values from the file are floats, and whether the code correctly
    determines the time point a beat occured at.

    """
    read_hr_1 = EcgReader('Test_ECG.txt')
    assert read_hr_1.csv_check == 0


def test_datacheck():
    read_hr_2 = EcgReader('Test_ECG.csv')
    read_hr_2.time = [2, "three", 4]
    read_hr_2.dataCheck()
    assert read_hr_2.data_type == 0


def test_findpeaks():
    read_hr_3 = EcgReader('Test_ECG.csv')
    read_hr_3.time = [0, 0.5, 1, 1.5, 2.0]
    read_hr_3.voltage = [10, 20, 30, 40, 50]
    read_hr_3.findRange()
    assert read_hr_3.peak_vector == [2.0]



