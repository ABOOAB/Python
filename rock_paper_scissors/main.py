import random


def main():
    user = input('enter R, P, or S: ').lower()
    computer = random.choice(['r', 'p', 's'])
    if user == computer :
        print('TIE')
    else :
        print(f"{winner(computer, user)} WIN")

    
def winner(computer, user):
    if (user=='r' and computer=='s') or (user=='s' and computer=='p') or \
        (user=='p' and computer=='r'):
        return 'user'
    return 'computer'



if __name__ == '__main__':
    main()