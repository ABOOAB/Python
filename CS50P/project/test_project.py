from project import solve_sudoku, empty_square, is_valid, is_valid_puzzle


game1 = [
        [3, 9, 0,   0, 5, 0,   0, 0, 0],
        [0, 0, 0,   2, 0, 0,   0, 0, 5],
        [0, 0, 0,   7, 1, 9,   0, 8, 0],

        [0, 5, 0,   0, 6, 8,   0, 0, 0],
        [2, 0, 6,   0, 0, 3,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 4],

        [5, 0, 0,   0, 0, 0,   0, 0, 0],
        [6, 7, 0,   1, 0, 5,   0, 4, 0],
        [1, 0, 9,   0, 0, 0,   2, 0, 0]
    ]

game2 = [
        [3, 9, 1,   0, 5, 0,   0, 0, 0],
        [0, 0, 0,   2, 0, 0,   0, 0, 5],
        [0, 0, 0,   7, 1, 9,   0, 8, 0],

        [0, 5, 0,   0, 6, 8,   0, 0, 0],
        [2, 0, 6,   0, 0, 3,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 4],

        [5, 0, 0,   0, 0, 0,   0, 0, 0],
        [6, 7, 0,   1, 0, 5,   0, 4, 0],
        [1, 0, 9,   0, 0, 0,   2, 0, 0]
    ]
game3 = [
        [3, 9, 1,   8, 5, 0,   0, 0, 0],
        [0, 0, 0,   2, 0, 0,   0, 0, 5],
        [0, 0, 0,   7, 1, 9,   0, 8, 0],

        [0, 5, 0,   0, 6, 8,   0, 0, 0],
        [2, 0, 6,   0, 0, 3,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 4],

        [5, 0, 0,   0, 0, 0,   0, 0, 0],
        [6, 7, 0,   1, 0, 5,   0, 4, 0],
        [1, 0, 9,   0, 0, 0,   2, 0, 0]
    ]
game4 = [
        [3, 9, 1,   8, 5, 6,   4, 2, 7],
        [8, 6, 7,   2, 3, 4,   9, 1, 5],
        [4, 2, 5,   7, 1, 9,   6, 8, 3],

        [7, 5, 4,   9, 6, 8,   1, 3, 2],
        [2, 1, 6,   4, 7, 3,   5, 9, 8],
        [9, 3, 8,   5, 2, 1,   7, 6, 4],

        [5, 4, 3,   6, 9, 2,   8, 7, 1],
        [6, 7, 2,   1, 8, 5,   3, 4, 9],
        [1, 8, 9,   3, 4, 7,   2, 5, 6]]

game5 = [
        [3, 9, 0,   0, 5, 0,   0, 0, 8],
        [0, 0, 0,   2, 0, 0,   0, 0, 5],
        [0, 0, 0,   7, 1, 9,   0, 8, 0],

        [0, 5, 0,   0, 6, 8,   0, 0, 0],
        [2, 0, 6,   0, 0, 3,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 4],

        [5, 0, 0,   0, 0, 0,   0, 0, 0],
        [6, 7, 0,   1, 0, 5,   0, 4, 0],
        [1, 0, 9,   0, 0, 0,   2, 0, 0]]

def test_is_valid_puzzle():
    assert is_valid_puzzle(game1) == True
    assert is_valid_puzzle(game5) == False



def test_empty_square():
    assert empty_square(game1) == (0, 2)
    assert empty_square(game2) == (0, 3)
    assert empty_square(game3) == (0, 5)
    assert empty_square(game4) == (None, None)


def test_is_valid():

    assert is_valid(game1, 0, 2, 9) == False
    assert is_valid(game1, 0, 2, 3) == False
    assert is_valid(game1, 0, 2, 1) == True

def test_solve_sudoku():

    assert solve_sudoku(game1) == True
    assert solve_sudoku(game2) == True
    assert solve_sudoku(game3) == True
    assert solve_sudoku(game4) == True
    assert solve_sudoku(game5) == False


