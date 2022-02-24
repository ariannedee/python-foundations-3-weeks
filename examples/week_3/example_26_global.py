x = 1

def a_func():
    global x  # Toggle this line to see how the value of x changes
    x = 2

a_func()
print(x)