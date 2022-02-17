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
