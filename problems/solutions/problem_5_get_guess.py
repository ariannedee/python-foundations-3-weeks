"""
Get a word with a given length from the user.

Validate that it:
- only includes letters
- has the correct number of letters
"""


def get_guess(word_length):
    while True:
        guess = input('> ').lower()
        if len(guess) != word_length:
            print(f'Must be {word_length} letters')
        else:
            break
    return guess


if __name__ == '__main__':
    word = get_guess(5)
    print(word)
