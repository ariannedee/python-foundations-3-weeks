print('In __init__.py: __name__ is ' + __name__)

from .thing2 import blue_fish
from .thing1 import red_fish


def n_fish(n):
    if n % 2 == 0:
        return n * red_fish()
    else:
        return n * blue_fish()
