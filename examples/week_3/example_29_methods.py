class Person(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hello {self.name}'


if __name__ == '__main__':
    person = Person('Eve')  # Calls __init__ with name='Eve'
    print(person.greet())   # Hello Eve
