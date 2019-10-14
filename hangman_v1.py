# Hangman game


import random


word_list = 'monkey ship ocean computer planet'.upper().split()
random.shuffle(word_list)

hangman_board = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

secret_word = word_list.pop()
correct = []
incorrect = []


# Display word to check if underscores are working
print(f"Debugger: {secret_word} ")


def draw_game_board():
    # Draws the hangman ascii as well as the word display board
    print(hangman_board[len(incorrect)])
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
    # Let's the user take a guess. Appends the letter to correct or inncorrect
    while True:
        guess = input("Type in your guess\n: ").upper()
        if guess in correct or guess in incorrect:
            print("\nYou've already guessed that! Try again.\n")
        elif guess.isnumeric():
            print("\nPlease enter letters and not numbers. Try again.\n")
        elif len(guess) == 0:
            print("\nPlease enter a guess.\n")
        elif guess == secret_word:
            print("\n~~~~~ YOU WON THE GAME! ~~~~~")
            print(f"The secret word was ~~~ {secret_word} ~~~")
            break

            ### Doesn't break out yet

        else:
            break
    if guess in secret_word:
        correct.append(guess)
    else:
        incorrect.append(guess)

def win_checker():
    # Checks to see if the user has won or lost the current game.
    if len(incorrect) > 6:
        return 'lose'
    for i in secret_word:
        if i not in correct:
            return 'not yet'
    return 'win'


while True:
    draw_game_board()
    user_guess()
    game_status = win_checker()
    if game_status == 'lose':
        print("\n~~~ GAME OVER ~~~")
        print(f"The secret word was ~~~ {secret_word} ~~~")
        break
    elif game_status == 'win':
        print("\n~~~~~ YOU WON THE GAME! ~~~~~")
        print(f"The secret word was ~~~ {secret_word} ~~~")
        break
