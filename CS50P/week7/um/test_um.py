from um import count


def test_A():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album") == 1
    assert count("thank you for album, yummy") == 0
    assert count("Um, thanks, um...") == 2
