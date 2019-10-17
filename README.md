# Linkedin Reach Project - Command Line Hangman


!["Linkedin Reach Banner"](https://content.linkedin.com/content/dam/engineering/site-assets/images/blog/posts/2019/08/reach1.png)

This is a command line hangman game that was created by Victor Nguyen using Python for the Linkedin Reach Apprenticeship application.


## Table of Contents


1. [Getting Started](README.md#getting-started)
    * Prerequisites
    * Installation
    * How to run the game
2. [Game Rules](README.md#game-rules)
3. [File Descriptions](README.md#file-descriptions)
4. [Reported Bugs](README.md#reported-bugs)
5. [Future Work](README.md#future-work)
    * Refactor code for performance
    * UX/UI
    * Expand testing suite
    * Online access
    * Reliability and scale
6. [Credits](README.md#credits)


## Getting Started
Please follow these instructions to get a copy of the project up and running on your local machine.


### Prerequisites
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


## File Descriptions
---
File|Task
---|---
images | Hangman start and gameover images
scripts | Prerequisites installation scripts
api_words.py | Function to grab the world list from the provided api
assets.py | ASCII Hangman images
hangman.py | Final version of Hangman game
hangman_v1.py | Prototype version 1 of Hangman game
hangman_v2.py | Prototype version 2 of Hangman game
test_hangman.py | Test file with proposed tests for Hangman game


## Reported Bugs
* One user reported that they had issues entering a guess when using iterm. (Investigation Pending)


## Future Work
Refactor code for performance:
* Improve loading time and speed
* Break up code to make it more modular
* Update installation scripts to use Python setup scripts`setup.py` & `requirements.txt`
* Redesign code using Object Oriented principles

UX/UI:
* Improve command line game dashboard layout
* Center secret word underscores 
* Change `CHANCES` to `CHANCE` when there is only one remaining guess left

Expand testing suite:
* Get testing suite to work
* Break up code to make testing more modular
* Cover more test cases

Online access:
* Create an online in browser terminal that has the game avaiable
* Redesign game to have a front end user interface
* Create user login, score keeping function and leadership scoreboard

Reliability and scale:
* Deploy to a cloud platform with autoscaling groups for resiliency 
* Set up automated testing using services like CircleCi, Jenkins or Travis
* Add monitoring and alerting services to report on the health of the application


## Credits
Created by Victor Nguyen | [@victormdnguyen](https://twitter.com/victormdnguyen)

