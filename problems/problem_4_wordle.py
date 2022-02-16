"""
Write a function that takes a word and a guess and produces the following result:
- 💚 if a letter is in the right place
- 💛 if a letter is in the word but in the wrong place
- 🖤 if the letter is not in the word
"""

emoji = {
    'right': '💚',
    'almost': '💛',
    'wrong': '🖤'
}


def wordle_result(word, guess):
    # Todo: fill out function
    pass


if __name__ == '__main__':
    print(wordle_result(word='hello', guess='world'))
