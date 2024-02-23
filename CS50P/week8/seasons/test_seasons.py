from seasons import count, validate


def test_count():
    assert (
        count("1999-01-01")
        == "Twelve million, nine hundred sixty-seven thousand, two hundred minutes"
    )
    assert (
        count("2001-01-01")
        == "Eleven million, nine hundred fourteen thousand, five hundred sixty minutes"
    )
    # assert count('') == ''
    # assert count('') == ''


def test_validate():
    assert validate("1999-01-15") == ("1999", "01", "15")
