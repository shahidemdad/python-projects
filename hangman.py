import random
import string
from words import words

def get_valid_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(word)
    print(word)
    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # users used letters

    lives = 6

    #user input
    while len(word_letters) > 0 and lives > 0:
        # used letters
        print('lives left: ', lives, '    Used letters: ', ' '.join(used_letters))

        #current word with - and used letters
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -=1
                print("not in the word")

        elif user_letter in used_letters:
            print("used the character once, try others!")
        
        else:
            print("Invalid characters")
    # when word_letters == 0  or lives == 0
    if lives == 0:
        print("you are dead!")
    else:
        print("\nYou got the word",word,"!")

hangman()