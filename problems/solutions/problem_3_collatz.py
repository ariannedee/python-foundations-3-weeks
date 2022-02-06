"""
Collatz sequence:
    - Starting at a number, n
    - If n is even, divide it by 2
    - If n is odd, multiply it by 3 and add 1
    - Repeat the process until you reach 1

Print the Collatz sequence for each number from 1 to 100.
"""


def next_num(n):
    if n % 2 == 0:
        return n // 2
    return n * 3 + 1


def collatz(num):
    while True:
        print(num, end=' ')
        if num == 1:
            print()
            return
        num = next_num(num)


for i in range(1, 101):
    collatz(i)
