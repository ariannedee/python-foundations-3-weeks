"""
Make a command-line Wordle clone
https://www.nytimes.com/games/wordle/index.html
"""
from problem_4_wordle import wordle_result


def get_random_word():
    pass


def remove_word_from_file(word):
    pass


def get_guess(word_length):
    pass


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
    answer = get_random_word()
    run_game(answer.lower())
    remove_word_from_file(answer)
