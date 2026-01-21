"""
collatz(1): 1
collatz(2): 2 1
collatz(3): 3 10 5 16 8 4 2 1
collatz(4): 4 2 1
collatz(5): 5 16 8 4 2 1

Collatz sequence:
    - Starting at a number, n
    - If n is even, divide it by 2
    - If n is odd, multiply it by 3 and add 1
    - Repeat the process until you reach 1

Print the Collatz sequence for each number from 1 to 100.
"""
def assert_equals(actual, expected):
    """Helper function for testing"""
    assert actual == expected, f"Expected {expected}, but got {actual}"

def next_num(n: int) -> int | None:
    if n == 1:
        return None
    elif n % 2 == 0:
        return n // 2
    else:
        return n * 3 + 1

assert_equals(next_num(1), None)
assert_equals(next_num(2), 1)
assert_equals(next_num(3), 10)
assert_equals(next_num(4), 2)
assert_equals(type(next_num(2)), int)

def collatz(num):
    """Return the Collatz sequence for a number (num) as a string"""
    sequence = str(num)
    while True:
        num = next_num(num)
        if num is None:
            break
        sequence += f" {num}"
    return sequence

assert_equals(collatz(1), '1')
assert_equals(collatz(2), '2 1')
assert_equals(collatz(3), '3 10 5 16 8 4 2 1')
assert_equals(collatz(4), '4 2 1')

for i in range(1, 101):
    print(collatz(i))