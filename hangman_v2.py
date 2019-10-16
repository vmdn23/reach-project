# Hangman game


import random
import re
from api_words import get_words
import assets


# Filters inputs to only allow letters and no numbers
input_filter = re.compile('[A-Za-z]+')

# Filters out special characters
special_filter = re.compile('[~!@#$%^&()_+={}[]|:;“’<,>.?๐฿]')

# Filters out numbers
num_filter = re.compile('[0-9]+')

# Grabs random a word using the api_words function from the word dictionary api 
word_list = get_words()
random.shuffle(word_list)
secret_word = word_list.pop().upper()

# Keeps track of correct and incorrect guesses
correct = []
incorrect = []

# Starting amount of guesses a user has
lives = 6


# Display word to check if underscores are working
print(f"Debugger: {secret_word} ")


def draw_game_board():
    """ Draws the hangman ascii as well as the word display board """
    
    # Prints out the hangman image according to the number of incorrect guesses
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(assets.hangman_board[len(incorrect)])
    print("\n\n")

    # Print out the letter of the secret word if guessed correctly or _ 
    for i in secret_word:
        if i in correct:
            print(i, end=' ')
        else:
            print('_', end=' ')
    print("\n\n")

    print("~~~~~~~~~ HERE ARE YOUR GUESSES SO FAR  ~~~~~~~~~")
    # Prints out the incorrect letters 
    for i in incorrect:
        print(i, end=' ')
    print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


def user_guess(lives):
    """ Let's the user take a guess. Appends letter to correct or inncorrect list"""

    # Variable to obtain length of secret word and prevent guesses longer than it
    check_len = len(secret_word)
    
    while True:

        print(f"~~~~~ YOU HAVE {lives} LIVES LEFT! ~~~~~")

        # Filters out the guess input by special characters and numbers
        pre_guess = input("Type in your guess\n: ").upper()
        guess = input_filter.search(pre_guess)
        specials = special_filter.search(pre_guess)
        num_check = num_filter.search(pre_guess)

        # If there is an empty guess or there isn't any specail characters
        if guess is None or specials is not None or num_check is not None:
            print("\nPlease enter a non-empty guess with no special characters or numbers.\n")
            lives -= 1
            return lives
        
        # There is no group() in a none, reassign to fix error
        guess = guess.group()

        if len(guess) > check_len:
            print("\nYour guess is too long. Try again!\n")
        elif guess in correct or guess in incorrect:
            print("\nYou've already guessed that! Try again.\n")

        elif guess.isnumeric():
            print("\nPlease enter letters and not numbers. Try again.\n")
            
        elif guess == secret_word:
            break
        
        else:
            break

    if guess == secret_word or guess in secret_word:
        if len(guess) > 1:
            # For every char in the string guess, add it to correct
            guess = [char for char in guess]
        correct.extend(guess)

        lives -= 1
        
    else:
        incorrect.append(guess)
        
        lives -= 1
        
    return lives

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

def play_again():
    while True:
        replay = input('Do you want to play again? Enter "Y" or "N"\n:').upper()

        if replay.startswith('Y'):
            # lives = 6
            correct=[]
            incorrect=[]
            guess=[]

            """ need to reset and redraw game board """

            draw_game_board()
            user_guess(lives=6)

            secret_word = word_list.pop()

            """ Need to reset secret word properly """
            # secret_word = random.shuffle(word_list).pop().upper()

            # secret_word = word_list.shuffle(word_list).pop()
            # word_list = get_words()
            # random.shuffle(word_list)
            # secret_word = word_list.pop().upper()
            return True
        elif replay.startswith('N'):
            return False

        else:
            continue
    

while True:
    draw_game_board()
    lives = user_guess(lives)
    game_status = win_checker()
    
    # Losing Message
    if game_status == 'lose' or lives == 0:
        print(assets.hangman_board[6])
        print("\n~~~ GAME OVER ~~~")
        print(f"The secret word was ~~~ {secret_word} ~~~")
        
        replay = play_again()
        if replay:
            continue 
        else:
            break

    # Winning Message
    elif game_status == 'win':
        print("\n~~~~~ YOU WON THE GAME! ~~~~~")
        print(f"\nThe secret word was ~~~ {secret_word} ~~~")

        replay = play_again()
        if replay:
            continue 
        else:
            break
        break