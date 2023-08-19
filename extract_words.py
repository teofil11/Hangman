import requests
import random

def get_words():
    list_words = []
    url = "https://raw.githubusercontent.com/vaibhavsingh97/random-word/master/random_word/database/words.json"

    response = requests.get(url)

    words = response.json()
    for word in words.keys():
        list_words.append(word)
    return list_words

def random_word(lenght_word):
    r_word = random.choice(get_words())
    while len(r_word) != lenght_word:
        r_word = random.choice(get_words())
    return r_word

