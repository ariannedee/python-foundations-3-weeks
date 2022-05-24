class Person(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hello {self.name}'

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Person("{self.name}")'  # Person("Name")


if __name__ == '__main__':
    people = [Person('Jack'), Person('Jill')]

    for person in people:
        print(person)        # Calls __str__
        print(repr(person))  # Calls __repr__

    print(people)  # Calls __repr__ on each item in string
