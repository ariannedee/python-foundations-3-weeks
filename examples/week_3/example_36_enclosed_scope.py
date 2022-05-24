x = 1


def outer_function(x):
    def inner_function(y):
        # x, y, z  # Toggle this line to see how locals() changes
        print(locals())
    y = 2
    z = 3
    inner_function(5)


outer_function(4)
