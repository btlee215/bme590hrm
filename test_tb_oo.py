from hrmtb import TachyBrady

def test_tb_check():
    first_test = TachyBrady([50, 50, 50, 75, 110, 110, 110], 60, 100)
    first_test.tb()
    assert first_test.tachy == [0, 0, 0, 0, 0, 0, 1]
    assert first_test.brady ==[0, 0, 1, 0, 0, 0, 0]