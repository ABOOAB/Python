from working import convert
import pytest


def test_A():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:00 AM to 8 AM") == "10:00 to 08:00"


def test_B():
    with pytest.raises(ValueError):
        convert("9AM - 5PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("15:00 AM to 3:00 PM")
