
import random
import string
from words import words



def main():
    word = get_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()     # what the user has guessed

    lives = len(word)     # number of tries

    # getting user input
    while len(word_letters) > 0 and lives > 0:

        # show letters used 
        print('You have', lives,  'left and you used this letters: ', ' '.join(used_letters))

        # show progress 
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        # get letterd from user
        user_letter = input('Guess the letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else :
                lives -= 1
                print("Your letter isn't in the word ")

        elif user_letter in  used_letters :
            print("You have already guessed that letter, please try again")

        else:
            print('Invalid character')

    # print either the user win or die
    if lives != 0:
        print('Congratulations! You won!! you guessed', word, 'correctly')
    else:
        print('Sorry, you died the word was', word)



# this function return a valid word from the global list
def get_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word :
        word = random.choice(words)
    return word.upper()



if __name__ == '__main__':
    main()


