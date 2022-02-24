"""
Use a main block to specify code that only runs when running the file as a script.
This code doesn't run when the file is imported as a module
"""
from a_module import Person as Hobbit


if __name__ == '__main__':
    for name in ['Frodo', 'Bilbo', 'Sam']:
        h = Hobbit(name)
        print(h.greet())
