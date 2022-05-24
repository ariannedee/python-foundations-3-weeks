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
    name = input("What's your name? ")
    p = Person(name)
    print(p.greet())
