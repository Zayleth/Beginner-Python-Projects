# let's do the Hangman game!
import random
from words import words
import string

def valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # letters that user has guessed
    lives = 10

    # user input

    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'c']) --> 'a b c'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # current word is (for example Z A Y L E - H)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        """
        we create a new variable 'word_list'. 
        Si la letter se encuentra en el conjunto used_letters (lo que significa que se ha adivinado correctamente), la letra en sí se agrega a la lista word_list.
        De lo contrario, se agrega un guión (-) a la lista.
        """

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word. Try again!')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nInvalid character. Try again.')

    #user gets here when len (word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died. The word was', word)
    
    else:
        print('Yayy! You guessed the word', word, '!!')

if __name__ == '__main__':
    hangman()