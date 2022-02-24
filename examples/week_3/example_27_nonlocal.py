x = 1

def outer_function(x):
    def inner_function(y):
        global x
        nonlocal z
        x = 6
        y = 7
        z = 8

    y = 2
    z = 3
    inner_function(5)
    print(f'x: {x}, y: {y}, z: {z}')


outer_function(4)
print(f'x: {x}')
