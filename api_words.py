#!/usr/bin/python3
"""
Gathers data from the word dictionary API
"""


import requests
import random


def get_words():
    """
    Gets the words from a word dictionary API
    """
    api_url = "http://app.linkedin-reach.io/words"

    request = requests.get(api_url)

    word_list = request.text.splitlines()

    random.shuffle(word_list)
    random_word = word_list.pop()

    print(random_word)


if __name__ == "__main__":
    get_words()
