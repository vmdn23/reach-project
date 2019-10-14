# Hangman game


import random


word_list = 'monkey ship ocean computer planet'.upper().split()
random.shuffle(word_list)

hangman_board = ['''
    PLACEHOLDER #0 - Zero''',''' 
    PLACEHOLDER #1 - One''','''
    PLACEHOLDER #2 - Two''','''
    PLACEHOLDER #3 - Three''','''
    PLACEHOLDER #4 - Four''','''
    PLACEHOLDER #5 - Five''','''
    PLACEHOLDER #6 - Six''','''
    '''
]


secret_word = word_list.pop()
correct = []
incorrect = []

# Display word to check if underscores are working
print(f"Debugger: {secret_word} ")


def draw_game_board():
    # Draws the hangman ascii as well as the word display board
    print(hangman_board[len(incorrect)])
    for i in secret_word:
        if i in correct:
            print(i, end=' ')
        else:
            print('_', end=' ')
    print("\n\n\n")
    print("********* MISSED LETTERS *********")
    for i in incorrect:
        print(i, end=' ')
    print("\n**********************************\n")


def user_guess():
    # Let's the user take a guess. Appends the letter to correct or inncorrect
    while True:
        guess = input("Guess a letter\n: ").upper()
        if guess in correct or guess in incorrect:
            print("You've already guessed that! Try again.\n")
        elif guess.isnumeric():
            print("Please enter letters and not numbers. Try again.\n")
        elif len(guess) == 0:
            print("Please enter a guess.\n")
        else:
            break
    if guess in secret_word:
        correct.append(guess)
    else:
        incorrect.append(guess)

while True:
    draw_game_board()
    user_guess()
