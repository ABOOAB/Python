
from utilities import use_keyboard, use_image, print_game


def is_valid_puzzle(puzzle):
    # Check if the initial puzzle is valid
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                continue
            elif not is_valid(puzzle, i, j, puzzle[i][j]):
                return False
    return True

def solve_sudoku(puzzle):
    row, column = empty_square(puzzle)
    # Check if the puzzle is complete
    if row is None:
        return True  # Puzzle solved

    # Try each possible value
    for value in range(1, 10):
        if is_valid(puzzle, row, column, value):
            puzzle[row][column] = value
            if solve_sudoku(puzzle):
                return True
            # Backtrack if the current value doesn't lead to a solution
            puzzle[row][column] = 0

    # If no valid value leads to a solution, puzzle is unsolvable
    return False


# function to get empty square
def empty_square(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0 :
                return i, j

    return None, None # game done


# check if a spacific square value is valid
def is_valid(puzzle, row , column, value):

    #check row
    for c in range(9):
        if value == puzzle[row][c] and c != column:
            return False

    #check colum
    for k in range(9) :
        if value == puzzle[k][column] and k != row:
            return False

    #check chunck
    first_row_index = (row // 3) * 3
    first_column_index = (column // 3) * 3

    for i in range(first_row_index, first_row_index + 3):
        for j in range(first_column_index, first_column_index + 3):
            if value == puzzle[i][j] and (i != row or j != column):
                return False
    return True

separator = '\033[92m' + '=' * 50 + '\n'  + '=' * 50 + '\033[0m' + '\n'



def main():
    print(separator)
    print("""\nWelcome to Sudoku Solver!

Please choose your input method:

1. Use keyboard
2. Upload image
""")

    while True:
        answer = input("Enter the number corresponding to your chosen method: ")
        if answer == '1':
            puzzle = use_keyboard()
            break

        elif answer =='2':
            puzzle = use_image()
            break

        else:
            print("Please enter a valid choice. Try again.")
    if puzzle is not None:
        if is_valid_puzzle(puzzle):
            solve_sudoku(puzzle)
            print_game(puzzle)
            print("Game done! Congratulations!")
            print(separator)
        else:
            print("Invalid puzzle. Please try again.")
            print(separator)
    else:
        print("Unclear puzzle. Please try again.")
        print(separator)
if __name__ =="__main__":
    main()
