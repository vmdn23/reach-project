# Hangman game


import random
import re
from api_words import get_words
import assets


# Filters inputs to only allow letters
input_filter = re.compile('\w+')

# Filters out special characters
special_filter = re.compile('^.[~!@#$%^&()_+={}[]|:;“’<,>.?๐฿].$')

# Grabs random word using the api_words function from the word dictionary api 
word_list = get_words()
random.shuffle(word_list)
secret_word = word_list.pop().upper()

# Keeps track of correct and incorrect guesses
correct = []
incorrect = []


# Display word to check if underscores are working
print(f"Debugger: {secret_word} ")


def draw_game_board():
    """ Draws the hangman ascii as well as the word display board """
    print(assets.hangman_board[len(incorrect)])
    print("\n\n")

    for i in secret_word:
        if i in correct:
            print(i, end=' ')
        else:
            print('_', end=' ')
    print("\n\n")

    print("********* YOUR GUESSES SO FAR *********")
    for i in incorrect:
        print(i, end=' ')
    print("\n***************************************\n")


def user_guess():
    """ Let's the user take a guess. Appends letter to correct or inncorrect list"""
    while True:
        pre_guess = input("Type in your guess\n: ").upper()
        guess = input_filter.search(pre_guess)
        specials = special_filter.search(pre_guess) 

        # If there is an empty guess or there isn't any specail characters
        if guess is None or specials is not None:
            print("\nPlease enter a proper guess.\n")
            continue
        
        # There is no group() in a none, reassign to fix error
        guess = guess.group()

        if specials is not None:
            specials = specials.group()

        elif guess in correct or guess in incorrect:
            print("\nYou've already guessed that! Try again.\n")

        elif guess.isnumeric():
            print("\nPlease enter letters and not numbers. Try again.\n")
            
        elif guess == secret_word:
            break
        
        else:
            break

        
        """
        Need to account for numbers and letters A2123DO
        Add condition to prevent users from making big string of guess
        """


    if guess == secret_word or guess in secret_word:
        correct.append(guess)
    else:
        incorrect.append(guess)


def win_checker():
    """ Checks to see if the user has won or lost the current game. """  
    if len(incorrect) > 5:
        return 'lose'
    if correct == []:
        return 'not yet'
    for i in secret_word:
        if i not in correct:
            return 'not yet'      
    return 'win'


while True:
    draw_game_board()
    user_guess()
    game_status = win_checker()

    # Losing Message
    if game_status == 'lose':
        print(assets.hangman_board[6])
        print("\n~~~ GAME OVER ~~~")
        print(f"The secret word was ~~~ {secret_word} ~~~")
        break

    # Winning Message
    elif game_status == 'win':
        print("\n~~~~~ YOU WON THE GAME! ~~~~~")
        print(f"The secret word was ~~~ {secret_word} ~~~")
        break
