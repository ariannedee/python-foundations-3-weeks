"""
Write a function that takes a word and a guess and produces the following result:
- 💚 if a letter is in the right place
- 💛 if a letter is in the word but in the wrong place
- 🖤 if the letter is not in the word

If the word is "hello" and the guess is "world", it should return "🖤💛🖤💚🖤".

Get the test suite in test_wordle.py to pass.
"""

emoji = {
    'right': '💚',
    'almost': '💛',
    'wrong': '🖤'
}


def wordle_result(word, guess):
    pass


if __name__ == '__main__':
    print(wordle_result(word='hello', guess='world'))
