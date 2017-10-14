def test_filecheck():
    """
    :return: This function is used as a unit test for the hrmread.py file.
    In this test, the following conditions are tested: whether the file
    input by the user is in .CSV format, whether the time and voltage
    values from the file are floats, and whether the code correctly
    determines the time point a beat occured at.

    """
    from readHR import EcgReader
    read_hr_1 = EcgReader('Test_ECG.txt')
    assert read_hr_1.csv_check is False


def test_datacheck():
    from readHR import EcgReader
    read_hr_2 = EcgReader('Test_ECG.csv')
    read_hr_2.time = [2, "three", 4]
    read_hr_2.datacheck()
    assert read_hr_2.data_type is False


def test_findpeaks():
    from readHR import EcgReader
    read_hr_3 = EcgReader('Test_ECG.csv')
    read_hr_3.time = [0, 0.5, 1, 1.5, 2.0]
    read_hr_3.voltage = [10, 20, 30, 40, 50]
    read_hr_3.findrange()
    assert read_hr_3.peak_vector == [2.0]
