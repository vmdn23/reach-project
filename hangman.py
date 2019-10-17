# Hangman - Python command line interface edition
# You have 6 chances to guess the secret word or you lose
# You can guess letters or words 
# You can't guess numbers or special characters


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

# Keeps track of "correct" and "incorrect" guesses
game_stats = {"correct": [], "incorrect": [], "secret_word": "", "lives" : 6, "starting_lives": 6}

# Grabs random a word using the api_words function from the word dictionary api 
word_list = get_words()
random.shuffle(word_list)
game_stats["secret_word"] = word_list.pop().upper()

# Allowed number of guesses
GUESS_LIMIT = 6


def draw_game_board():
    """ Draws the hangman ascii as well as the word display board """
    
    # Prints out the hangman image according to the number lives available
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~ HANGMAN ~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(assets.hangman_board[game_stats["starting_lives"] - game_stats["lives"]])
    print("\n\n")

    # Print out the letter of the secret word if guessed correctly or _ 
    for i in game_stats["secret_word"]:
        if i in game_stats["correct"]:
            print(i, end=' ')
        else:
            print('_', end=' ')
    print("\n\n")

    print("~~~~~~~~~~~~ HERE ARE YOUR GUESSES SO FAR ~~~~~~~~~~~~~")
    # Prints out the "incorrect" letters 
    for i in game_stats["incorrect"]:
        print(i, end=' ')
    print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


def user_guess():
    """ Let's the user take a guess. Appends letter to "correct" or inn"correct" list"""
    # Variable to obtain length of secret word and prevent guesses longer than it
    check_len = len(game_stats["secret_word"])

    print(f"~~~~~ YOU HAVE {game_stats['lives']} CHANCES LEFT! ~~~~~")

    # Filters out the guess input by special characters and numbers
    pre_guess = input("Type in your guess\n: ").upper()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    guess = input_filter.search(pre_guess)
    specials = special_filter.search(pre_guess)
    num_check = num_filter.search(pre_guess)

    # If there is an empty guess or there isn't any special characters
    if guess is None:
        print("\nPlease enter a non-empty guess.\n")
        game_stats["lives"] -= 1
        return 0
        
    elif specials is not None:
        print("\nPlease don't enter special charcters, enter a word or letter.\n")
        game_stats["lives"] -= 1
        return 0
    
    elif num_check is not None:
        print("\nPlease enter a word or letter.\n")
        game_stats["lives"] -= 1
        return 0
    
    # Search and return one or more sub group and prints out the actual match
    else:
        guess = guess.group()

    if len(guess) > check_len:
        print("\nYour guess is too long. Try again!\n")
        return 0

    elif guess in game_stats["correct"] or guess in game_stats["correct"]:
        print("\nYou've already guessed that! Try again.\n")
        return 0
        
    elif guess == game_stats["secret_word"]:
        pass
    
    else:
        pass

    if guess == game_stats["secret_word"] or guess in game_stats["secret_word"]:
        if len(guess) > 1:
            # For every char in the string guess, add it to "correct"
            guess = [char for char in guess]
        game_stats["correct"].extend(guess)
        
    else:
        # Appends guess to incorrect counter
        game_stats["incorrect"].append(guess)
        game_stats["lives"] -= 1
        
    return True

def win_checker():
    """ Checks to see if the user has won or lost the current game. """  
    if len(game_stats["incorrect"]) == GUESS_LIMIT:
        return 'lose'
    if game_stats["correct"] == []:
        return 'alive'
    for i in game_stats["secret_word"]:
        if i not in game_stats["correct"]:
            return 'alive'      
    return 'win'

def play_again():
    replay = input('Do you want to play again? Enter "Y" or "N"\n:').upper()

    # reinitialize the game
    if replay.startswith('Y'):
        game_stats["lives"] = game_stats["starting_lives"]
        game_stats["correct"]=[]
        game_stats["incorrect"]=[]

        # Grabs a new word from api
        random.shuffle(word_list)
        game_stats["secret_word"] = word_list.pop().upper()
        
        return True
        
    elif replay.startswith('N'):
        return False

while True:
    draw_game_board()
    state = user_guess()

    # Checks if loop will continue again or not
    if state is False:
        continue
    elif state is 0:
        pass
    else:
        pass
    
    game_status = win_checker()
    
    # Losing Message
    if game_status == 'lose' or game_stats["lives"] <= 0:
        print(assets.hangman_board[6])
        print("\n~~~ GAME OVER ~~~")
        print(f"The secret word was ~~~ {game_stats['secret_word']} ~~~")
        
        replay = play_again()
        if replay:
            continue 
        else:
            break

    # Winning Message
    elif game_status == 'win':
        print("\n~~~~~ YOU WON THE GAME! ~~~~~")
        print(f"\nThe secret word was ~~~ {game_stats['secret_word']} ~~~")

        replay = play_again()
        if replay:
            continue 
        else:
            break
        break