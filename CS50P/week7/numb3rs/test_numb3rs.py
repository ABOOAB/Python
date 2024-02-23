from numb3rs import validate


def test_unit():
    assert validate(r"1.233.3.5") == True
    assert validate(r"15.38.5") == False
    assert validate(r"1.25.3.53.6") == False

def test_type():
    assert validate(r"1.253.3.5") == True
    assert validate(r"1kj.23.3.5") == False
    assert validate(r"1.253.3&.5") == False
    assert validate(r"1.25..3.5") == False
    assert validate(r"cat") == False

def test_range():
    assert validate(r"255.255.253.255") == True
    assert validate(r"-1.233.3.5") == False
    assert validate(r"1000.233.3.5") == False
    assert validate(r"1.256.3.5") == False

