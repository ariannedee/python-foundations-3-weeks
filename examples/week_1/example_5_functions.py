def add(a, b):
    return a + b


def say_hello(name, shout=False):
    greeting = 'Hello ' + name
    if shout:
        return greeting.upper()
    return greeting


print(say_hello('Beyoncé'))
print(say_hello('Shakira', True))
print(say_hello(shout=True, name='Bono'))
