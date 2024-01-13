
import random

def guess(x):
    computer = random.randint(1,x)
    user = 0
    while computer != user:
        user = int(input('Enter your Guess: '))
        if computer > user:
            print('Go up')
        elif user > computer :
            print('Go down')

    print(f'Yaa, you guessed {computer} correctly🥰😘')

def computer_guess(x):
    lower = 1
    upper = x
    feedback = ''
    while feedback != 'c':
        # check if the lower and upper are the same since 
        # it will give an error in randint function
        if lower != upper:
            computer = random.randint(lower, upper)
        else :
            computer = upper
        feedback = input('Give a feed back')
        if feedback == 'h':
            upper = upper - 1
        elif feedback == 'l':
            lower += 1
    
    print(f'Yaa, you guessed {computer} correctly🥰😘')



guess(100)