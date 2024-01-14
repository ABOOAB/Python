import math
import random


class Player:
    def __init__(self, letter):
        self.letter = letter  # chooce (x) or (o)

    def get_move(self, game):
        pass

 
class User(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):

        # val = None
        # valid_square = False
        # while not valid_square:
        #     square = input(self.letter + "'s turn. Input move (0 - 9): ")
        #     try:
        #         val = int(square)
        #         if val not in game.available_moves():
        #             raise ValueError
        #         valid_square = True
        #     except ValueError :
        #         print("Invalid square. Try again")
        #         pass
        # return val

        
        while True:
            try:
                val = int(input(self.letter + "'s turn. Input move (0 - 8): "))
                if val not in game.available_moves():
                    raise ValueError
                break
            except ValueError :
                print("Invalid square. Try again")
                
        return val


class Computer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):

        # get the move randomly from the available spots 
        return random.choice(game.available_moves())   



class SmartComputer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        min_player = 'O' if player == 'X' else 'X'
        if state.current_winner == min_player:
            return {'position': None, 'score': 1 * (state.empty_squares_num() + 1) if min_player == max_player else -1 * (
                        state.empty_squares_num() + 1)}

        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, min_player)

            # Undo the move
            state.board[possible_move] = ' '  # Restore the square to its empty state
            state.current_winner = None

            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best



   


       