from player import User, Computer, SmartComputer
import time
import random


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + '|'.join(row) + '|')

    @staticmethod
    def print_board_nums():
        
        # number_board  = []
        # for j in range(3):
        #     row = []
        #     for i in range(j*3, (j +1) * 3 ):
        #         row.append(str(i))
        #     number_board.append(row)

        # the privous snippit by using list comprehensions 
        number_board = [[str(i) for i in range(j * 3, (j+1) * 3)] for j in range(3)]
       
        for row in number_board:
            print('|' + '|'.join(row) + '|')

        


    def available_moves(self):
        return [i for (i, spot) in enumerate(self.board) if spot == ' ']

        # without using list comprehension
        
        # moves= []
        # for (i, spot) in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)
        #     return moves

    def empty_squares(self):
        return ' ' in self.board    # return True if still empty spots on the board
    
    def empty_squares_num(self):    # to know the number of embty squares
        # return self.board.count(' ')
        return len(self.available_moves())  

    def make_move(self, square, letter) :
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    

    def winner(self, square, letter):

        # check the row
        row_ind = square // 3
        row = self.board[row_ind * 3 : ((row_ind + 1) * 3)]
        if all([spot == letter for spot in row]):
            return True
        
        #check the column 
        col_ind = square % 3 
        col = [self.board[col_ind + i * 3 ] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True
        #check for diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                
                return True

def play(game, x_player, o_player, print_game = True):

    if print_game: 
        game.print_board_nums()

    letter = random.choice(['X', 'O'])

    while game.empty_squares():

        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + " make a move to " + str(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + " win!" )
                return letter


        # change letters after move
        letter = 'O' if letter == 'X' else 'X'

        time.sleep(0.8)


    if print_game:
        print("It's a tie! ")


# if __name__ == "__main__":
#     x_player = User('X')
#     o_player = SmartComputer('O')
#     game = TicTacToe()

#     play(game, x_player, o_player, print_game = True)
#     print('')
 
