# Linkedin Reach Project - Commandline Hangman

!["Linkedin Reach Banner"](https://content.linkedin.com/content/dam/engineering/site-assets/images/blog/posts/2019/08/reach1.png)

This is a commandline hangman game that was created by Victor Nguyen using Python for the Linkedin Reach Apprenticeship application.

## Table of Contents

1. [Getting Started](README.md#getting-started)
    * Prequisites
    * Installation
    * How to run the game
2. [Game Rules](README.md#game-rules)
3. [Reported Bugs](README.md#reported-bugs)
4. [Future Work](README.md#future-work)
    * Refactor code for performance
    * Expand testing suite
    * Online access
    * Reliability and scale
5. [Credits](README.md#credits)

## Getting Started

Please follow these instructions to get a copy of the project up and running on your local machine.

### Prequisites
You will need to install the following:
```
Python 3.7.3
Python requests library 
```

### Installation
Grab a copy of the program by entering the following into your terminal and `cd` into the repository.
```
git clone https://github.com/vmdn23/reach-project.git
```

If you are working on a new `Ubuntu 18.04` environment, please run the `setup_build.sh` script.
```
cd scripts
./setup_build
```

Install Python 3.7.3
```
cd scripts
./install_python3.7.sh
```

Install Pytest so that you can run tests in the future
```
cd scripts
./install_pytest.sh
```

Once you have finished installing everything, you are ready to run the game.

### How to run the game
Move back to the root directory of the repository and execute
```
python3.7 hangman.py
```

If you see a dashboard like the one shown below, you are ready to play!

![Fig 1: Hangman start image](/images/hangman_start.png)


## Game Rules
Here are the rules for the game:
```
You have 6 chances to guess the secret word or you lose
You can guess letters or words 
You can't guess numbers or special characters
You can choose to play again after you win or lose
```

How to make a guess:
* Type in your guess and press enter

If you see a dashboard like the one below, you lose!

![Fig 2: Hangman game over image](/images/hangman_gameover.png)

## Reported Bugs
* One user reported that they had issues entering a guess when using iterm. (Investigation Pending)


## Future Work

## Credits
Created by Victor Nguyen | [@victormdnguyen](https://twitter.com/victormdnguyen)

