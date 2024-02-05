from enum import Enum


class TimeOfDay(Enum):
    MORNING = 0
    AFTERNOON = 1
    EVENING = 2
    NIGHT = 3


class Person:
    species = 'Homo Sapien'

    def __init__(self, name):
        self.name = name

    def greet(self, time_of_day=None):
        if not time_of_day or not isinstance(time_of_day, TimeOfDay):
            return f'Hello, {self.name}!'
        return f'Good {time_of_day.name.lower()}, {self.name}!'

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Person("{self.name}")'


if __name__ == '__main__':
    person = Person('Plato')
    print(person.greet(TimeOfDay.AFTERNOON))  # Good afternoon, Plato!
