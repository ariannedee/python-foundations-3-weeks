class Person(object):
    def __init__(self):
        pass

    def greet(self):
        pass


if __name__ == '__main__':
    person = Person()    # Create instance of class
    person.greet()       # Call method on instance (does nothing)
    print(person)        # <__main__.Person object at memory location>
    print(type(person))  # <class '__main__.Person'>
