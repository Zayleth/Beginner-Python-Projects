# let's do the Hangman game!

import random
from words import words
import string

def valid_word(words):
    word = random.choice(words) #randomly chooses from the words list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

# we defined the function and add the variables.
def hangman():
    word = valid_word
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #letters that user has guessed
    lives = 10

    #user input
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'and you have used these letters: ', ' '.join(used_letters))

    #letters used
    # ' '. join (['a', 'b', 'c']) --> 'a b c'

    #current word is 
    word_list = [letter if letter in used_letters else '-' for letter in word]      #we create a new variable 'word_list'. 

    print('Current word: ', ' '.join(word_list))

    user_letter = input("Guess a letter: ").upper()

    if user_letter in alphabet - used_letters:    #if user letter is in the alphabet and the letter has not been used.

        used_letters.add(user_letter)               #so, let's add user_letter to used_letters
        if user_letter in word_letters:             #if user_letter is in word_letters
            word_letters.remove(user_letter)        #then, let's remove the user_letter from word_letters

        else:
            lives = lives - 1                       #takes away a life if wrong 
            print('Letter is not in the word')


    elif user_letter in used_letters:
        print('You have already used that character. Please try again. ')

    else:
        print('Invalid character. Please try again. ')

    #user gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('Oh! You died. The word was', word)

    else:
        print('Yayy!. You guessed the world', word, '!')

hangman()