

from plates import is_valid

def test_twoletter():
    assert is_valid("G") == False
    assert is_valid("tg") == True
    assert is_valid("tgie8") == True
    assert is_valid("4") == False
    assert is_valid("44") == False

def test_six():
    assert is_valid("Goodbye") == False
    assert is_valid("HelloWorld") == False
    assert is_valid("HelloW") == True

def test_num():
    assert is_valid("AB122") == True
    assert is_valid("AB122A") == False
    assert is_valid("AB022") == False
    assert is_valid("AB122A") == False

def test_punc():
    assert is_valid("AB 122") == False
    assert is_valid("AB,122") == False
    assert is_valid("AB022!") == False
    assert is_valid("AB122?") == False

