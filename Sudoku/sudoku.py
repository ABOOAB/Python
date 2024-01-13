
# THE PUZZLE IS A 9 LISTS OF 9 ELEMENTS IN EACH
# We will impleament empty squares as -1

from pprint import pprint

game = [[2, -1, -1, -1, -1, -1, 3, -1, -1],
        [-1, 7, 4, 6, 8, -1, -1, -1, -1],
        [-1, -1, -1, 2, -1, 7, -1, -1, 8],
        [-1, -1, -1, -1, 6, -1, -1, -1, 7],
        [-1, 2, 3, -1, -1, 9, 8, -1, -1],
        [7, -1, 1, -1, -1, -1, 9, -1, 4],
        [8, -1, 7, 9, 3, 6, -1, 2, 5],
        [-1, -1, -1, -1, 4, -1, -1, 1, 3],
        [4, 3, 5, 7, -1, 1, -1, 8, 9]]

game2 = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

def solve_sudoku(puzzle):
    row, column = empty_square(puzzle)
    if row is None :
        print("Game end successfully :) ")
        return True
    
    for i in range(1, 10):
        if is_valid(puzzle, row, column, i):
            puzzle[row][column] = i
            if solve_sudoku(puzzle):
                return True
        puzzle[row][column] = -1
    return False

    
def empty_square(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == -1 :
                return i, j
           
    return None, None # end of game
    

# check if a spacific square value is valid
def is_valid(puzzle, row , column, value):

    #check row
    # for k in range(9) :
    if value in puzzle[row]:
        return False
        
    #check colum
    for k in range(9) :
        if value == puzzle[k][column]:
            return False
        
    #check chunck
    first_row_index = (row // 3) * 3
    first_column_index = (column // 3) * 3

    for i in range(first_row_index, first_row_index + 3):
        for j in range(first_column_index, first_column_index + 3):
            if value == puzzle[i][j]:
                return False
    return True 


if __name__ == "__main__":
    solve_sudoku(game2)
    pprint(game2)
