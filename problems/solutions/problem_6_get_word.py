"""
From data/words.txt, retrieve a random word and remove it from the file
Raise a ValueError if there are no words in the file
"""
from random import choice


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


if __name__ == '__main__':
    # Test getting word
    word = retrieve_random_word()
    assert len(word) == 5
    print(word)

    # Expect exception with empty file
    try:
        len(retrieve_random_word('data/empty.txt'))
        assert False, 'ValueError expected'
    except ValueError:
        pass
