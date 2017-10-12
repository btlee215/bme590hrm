from hrmtb import TachyBrady

def test_tb_check():
    first_test = TachyBrady([50, 50, 50, 75, 110, 110, 110])
    assert first_test == ([0, 0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0])
