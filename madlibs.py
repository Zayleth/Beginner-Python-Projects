# What is a Mad Lib?
# Mad Libs is a fun word game where you build a silly story together. One player reads a story template with blanks, 
# asking others for random words (nouns, verbs, adjectives) to fill them in, without revealing the story itself. 
# Once all the blanks are filled, the first player reads the complete story aloud – with all the crazy words everyone chose! 
# Mad Libs is a great group activity, perfect for parties or gatherings.

# steps
#1. create the madlib as a variable that contains the history (string).
#2  create variables that will sustitute de blanck space in the history. 

city_name = input("City name: ")
dog_name = input("Dog's name: ")
dog_profession = input("Dog's profession: ") 
place = input("Place: ")
objects = input("Object: ")
second_object= input("Another object: ")
animal = input("Animal: ")


madlib=f"In a small town called {city_name}, there lived a dog named {dog_name}.\
\
Unlike other dogs,{dog_name} wasn't interested in balls or walks in the park.\
\
His biggest dream was to become {dog_profession} and explore the {place}.\
\
Everyone in {city_name} was laughing at {dog_name}'s aspirations.\
\
A dog in the {place}? It was ridiculous! But {dog_name} was not discouraged.\
\
He trained every day, running through the park, climbing trees and jumping over obstacles.\
\
He even built his own {objects} out of cardboard boxes.\
\
One day, while {dog_name} was watching the {place} with his {second_object},\
\
he saw a friendly {animal} who had come to look for him to take him to an unforgettable adventure. {dog_name} couldn't believe it.\
\
His dream was coming true! He said goodbye to his friends in {city_name} and he went with the {animal}.\
\
Together, they created unforgettable experiences.\
\
{dog_name} became the first dog {dog_profession} in history and inspired everyone in {city_name} to follow your dreams, no matter what others said. They learned that with determination and effort, even the strangest dreams can come true. On his return, {dog_name} was welcomed as a hero.\
\
Everyone asked for his autographs and wanted to hear how he had fulfilled his dream.\
\
But {dog_name} never forgot his roots or his small town.\
\
Sometimes he returned to {city_name} to share his adventures with his friends and remind them that with a little imagination, anything is possible!"

print(madlib)