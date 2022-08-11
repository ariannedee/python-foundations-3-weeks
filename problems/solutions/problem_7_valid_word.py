"""
Check if a word is valid using
https://api.dictionaryapi.dev/api/v2/entries/en/<word>
"""
import requests


def is_valid(word):
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    response = requests.get(url)
    return response.status_code == 200


if __name__ == '__main__':
    assert is_valid('hello')
    assert not is_valid('herblo')
