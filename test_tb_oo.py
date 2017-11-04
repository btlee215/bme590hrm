from hrmtb import TachyBrady


def test_tb_check():
    first_test = TachyBrady([50, 50, 50, 75, 110, 110, 110], 60, 100)
    first_test.tb()
    assert first_test.tachy == [False, False, False, False, False,
                                False, True]
    assert first_test.brady == [False, False, True, False, False,
                                False, False]