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
    word = valid_word(words) # Llama a valid_word para obtener la palabra elegida
    word_letters = set(valid_word(words)) # letters in the word. word_letters llama a la función valid_word, que recupera una palabra aleatoria sin guiones ni espacios como se desea
                                          # mediante la funcion set(...) que toma la cadena devuelta (la palabra) y crea un conjunto que contiene sus letras únicas.
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # letters that user has guessed

    lives = 10


    # user input
    while len(word_letters) > 0 and lives > 0:

    # letters used
    # ' '. join (['a', 'b', 'c']) --> 'a b c'
        print('You have', lives, 'lives and you have used these letters: ', ' '.join(used_letters))

        # current word is (for example Z A Y L E - H)
        word_list = [letter if letter in used_letters else '-' for letter in word]  
        
        """
        we create a new variable 'word_list'. 
        Si la letter se encuentra en el conjunto used_letters (lo que significa que se ha adivinado correctamente), la letra en sí se agrega a la lista word_list.
        De lo contrario, se agrega un guión (-) a la lista.
        """

        print('Current word: ', ' '.join(word_list))


        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters: # if user letter is in the alphabet and the letter has not been used.
            used_letters.add(user_letter) # so, let's add user_letter to used_letters
            
            if user_letter in word_letters: # if user_letter is in word_letters
                word_letters.remove(user_letter) # then, let's remove the user_letter from word_letters
                print('')
            
            
            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word. Try again!')
                

        elif user_letter in used_letters:
            print('\nYou have already used that character. Please try again. ')

        else:
            print('\nInvalid character. Please try again. ')

    #user gets here when len (word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('Oh! You died. The word was', word)

    else:
        print('Yayy!. You guessed the word', word, '!') #nunca sale mensaje de felcitaciones

hangman()
