from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert str(jar) == ""
    with pytest.raises(ValueError):
        jar = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"
    with pytest.raises(ValueError):
        jar.deposit(15)
    with pytest.raises(ValueError):
        jar = Jar(10)
        jar.deposit(11)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(1)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(11)
    assert str(jar) == ""
    with pytest.raises(ValueError):
        jar.withdraw(1)
