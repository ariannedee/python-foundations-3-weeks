class Person(object):
    species = 'Homo Sapien'

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hello {self.name}'

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Person("{self.name}")'


if __name__ == '__main__':
    people = [Person('Jack'), Person('Jill')]

    # All return 'Homo Sapien'
    print(people[0].species)
    print(people[1].species)
    print(Person.species)
