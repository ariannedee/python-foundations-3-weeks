"""
Make a command-line Wordle clone
https://www.nytimes.com/games/wordle/index.html

Check if word is valid at https://api.dictionaryapi.dev/api/v2/entries/en/<word>
"""
import requests
from random import choice
from problem_4_wordle import wordle_result


def retrieve_random_word(word_file='data/words.txt'):
    with open(word_file) as file:
        lines = file.readlines()
    if len(lines) > 0:
        random_line = choice(lines)
        lines.remove(random_line)
    else:
        raise ValueError(f'{word_file} is empty')

    with open(word_file, 'w') as file:
        file.writelines(lines)

    return random_line.strip()


def is_valid(word):
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    response = requests.get(url)
    result = response.json()
    return isinstance(result, list)


def get_guess(word_length):
    while True:
        guess = input('> ').lower()
        if len(guess) != word_length:
            print(f'Must be {word_length} letters')
            continue
        if is_valid(guess):
            break
        else:
            print("Invalid word")
    return guess


def run_game(word):
    num_guesses = 6
    word_length = len(word)
    while num_guesses > 0:
        print(f"Enter a {word_length} letter word ({num_guesses} guesses left)")
        guess = get_guess(word_length)
        print(wordle_result(word, guess))
        num_guesses -= 1
        if word == guess:
            print("Congrats!")
            return
    print(f'The word was: {word}')


if __name__ == '__main__':
    word = retrieve_random_word()
    run_game(word.lower())
