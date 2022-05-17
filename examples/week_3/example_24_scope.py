from pprint import pprint

a = 1
b = 2
c = 3


def a_function(a):
    b = 5
    print(f"a: {a}, b: {b}")
    print(locals())


a_function(4)
pprint(globals())