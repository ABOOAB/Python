from game import play, TicTacToe
from player import User, Computer, SmartComputer


def main():
    wish = input('What do you want? (play or test): ')
    if wish == 'play':
        game = TicTacToe()
        level = input("Level: (Easy or Hard): ").lower()
        user = input("Choose (X or O): ").capitalize()
        if user == 'X': 
            X_player = User('X')
            O_player = Computer('O') if level == 'easy' else SmartComputer('O')
        else :
            O_player = User('O')
            X_player = Computer('X') if level == 'easy' else SmartComputer('X')  
        play(game, X_player, O_player, print_game=True)
    else:
        result = {'smart_computer' : 0, 'computer' : 0, 'Ties': 0}
        for _ in range(10):
            game = TicTacToe()
            winer = play(game, Computer('X'), SmartComputer('O'), print_game=False)
            if winer== 'O':
                result['smart_computer'] += 1
            elif winer== 'X' :
                result['computer'] += 1
            else :
                result['Ties'] += 1
        print(result)





if __name__ == "__main__":
    main()
