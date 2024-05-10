# let's do the Hangman game!

import random
from words import words
import string

def valid_word(words):
    word = random.choice(words) #randomly chooses from the words list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

# we defined the function and add the parameters.
def hangman():
    word = valid_word
    word_letters = set (word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters: set() #letters that user has guessed

    

