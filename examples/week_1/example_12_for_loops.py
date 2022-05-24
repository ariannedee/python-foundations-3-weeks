# Use range() to loop through a list of numbers
for i in range(10):
    print(i)
print()

for i in range(10, 20):
    print(i)
print()

for i in range(10, 20, 2):
    print(i)
print()


primes = [1, 2, 3, 5, 7, 11, 13]
# Can loop over lists
for number in primes:
    print(number)


# If you need to know the index, use enumerate()
for i, number in enumerate(primes):
    print(f'{i}: {number}')


# Complex example - create list of all primes under 100
primes = []
for i in range(100):
    for n in range(2, i):
        if i % n == 0:  # Check divisibility
            break
    else:               # If for-loop completes without a break, do this
        primes.append(i)

print(primes)
