"""
From data/words.txt, retrieve a random word and remove it from the file
Raise a ValueError if there are no words in the file
"""


def retrieve_random_word(word_file='data/words.txt'):
    pass


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
