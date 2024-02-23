from bank import value


def test_corrLow():
    assert value("hello") == 0
    assert value("hello,") == 0


def test_corrCap():
    assert value("Hello") == 0
    assert value("Hello,") == 0


def test_haCap():
    assert value("Hi") == 20
    assert value("Hey,") == 20
    assert value("Hehe, baby") == 20


def test_haLow():
    assert value("hi") == 20
    assert value("hey,") == 20
    assert value("hehe, baby") == 20


def test_noCap():
    assert value("Welcome") == 100
    assert value("Eee") == 100
    assert value("Come") == 100
    assert value("GEKKl") == 100


def test_nolLow():
    assert value("welcome") == 100
    assert value("eee fdhsoa") == 100
    assert value("come,") == 100
    assert value("gEKKl") == 100
