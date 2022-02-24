class Person(object):
    def __init__(self):
        self.name = 'Adam'

    def greet(self):
        pass


if __name__ == '__main__':
    person = Person()   # Calls __init__
    print(person.name)  # Adam
