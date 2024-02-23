from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("4/4") == 100
    assert convert("2/5") == 40


def test_gauge():
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(33) == "33%"
    assert gauge(50) == "50%"


def test_Err():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
