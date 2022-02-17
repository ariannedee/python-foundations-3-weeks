"""
Write a Wordle clone

Check if word is valid at https://api.dictionaryapi.dev/api/v2/entries/en/<word>
"""
import requests
from random import choice
from problem_4_wordle import wordle_result


def get_random_word():
    with open('data/words.txt') as file:
        try:
            word = choice(file.readlines()).strip()
        except ValueError:
            print('words.txt is empty')
    return word


def remove_word_from_file(word):
    lines = []
    found = False
    with open('data/words.txt', 'r') as file:
        for line in file.readlines():
            if line.strip() == word:
                found = True
            else:
                lines.append(line)
    if not found:
        raise ValueError(f'{word} not found in words.txt')

    with open('data/words.txt', 'w') as file:
        file.writelines(lines)


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
        print(f"Enter a {word_length} letter word ({num_guesses} guesses)")
        guess = get_guess(word_length)
        print(wordle_result(word, guess))
        num_guesses -= 1
        if word == guess:
            print("Congrats!")
            return
    print(f'The word was: {word}')


if __name__ == '__main__':
    word = get_random_word()
    run_game(word.lower())
    remove_word_from_file(word)

