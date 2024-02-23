from twttr import shorten


def test_cap():
    assert shorten("hello") == "hll"
    assert shorten("twitter") == "twttr"


def test_low():
    assert shorten("HellO") == "Hll"
    assert shorten("What's your name?") == "Wht's yr nm?"


def test_num():
    assert shorten("CS50") == "CS50"
