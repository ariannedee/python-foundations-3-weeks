"""
Collatz sequence:
    - Starting at a number, n
    - If n is even, divide it by 2
    - If n is odd, multiply it by 3 and add 1
    - Repeat the process until you reach 1

Print the Collatz sequence for each number from 1 to 100.
"""


def assert_equals(actual, expected):
    """Test helper function"""
    assert actual == expected, f"Expected {expected}, but got {actual}"


def next_num(n):
    if n % 2 == 0:
        return n // 2
    return n * 3 + 1


def collatz(num):
    """Return the Collatz sequence for a number (num) as a string"""
    result = ''
    while True:
        result += f'{num} '
        if num == 1:
            return result.strip()
        num = next_num(num)


assert_equals(collatz(1), '1')
assert_equals(collatz(2), '2 1')
assert_equals(collatz(3), '3 10 5 16 8 4 2 1')
assert_equals(collatz(4), '4 2 1')

for i in range(1, 101):
    print(collatz(i))
