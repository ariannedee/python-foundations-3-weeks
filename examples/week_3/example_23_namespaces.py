from pprint import pprint  # pretty print function

import example_21_enums
from example_21_enums import Person
from example_21_enums import Person as Robot


def create_person(name):
    return Person(name)

han = create_person("Han")

pprint(vars(__builtins__))  # Dictionary mapping of built-in classes and functions
pprint(vars())              # Dictionary mapping of namespace (minus builtins)
pprint(vars(Person))        # Mapping of methods and class attributes
