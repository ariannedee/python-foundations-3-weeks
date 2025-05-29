"""
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


# Todo: determine next number in sequence
def next_num(n):
    pass


# Todo: get tests to pass
def collatz(num):
    """Return the Collatz sequence for a number (num) as a string"""
    pass


assert_equals(collatz(1), '1')
assert_equals(collatz(2), '2 1')
assert_equals(collatz(3), '3 10 5 16 8 4 2 1')
assert_equals(collatz(4), '4 2 1')

# Todo: print the Collatz sequence for each number from 1 - 100
