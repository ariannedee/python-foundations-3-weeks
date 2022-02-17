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
    word = list(word)
    guess = list(guess)
    result = list(emoji['wrong'] * len(word))

    for i, char in enumerate(guess):
        if word[i] == char:
            result[i] = emoji['right']
            word[i] = None
            guess[i] = '-'

    for i, char in enumerate(guess):
        if char in word:
            result[i] = emoji['almost']
            char_i = word.index(char)
            word[char_i] = None
    return ''.join(result)


if __name__ == '__main__':
    print(wordle_result(word='hello', guess='world'))
