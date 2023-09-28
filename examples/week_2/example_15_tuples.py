# Tuples are like lists but cannot be modified
new_tuple = (0, 1, 2, 2, 3)

print(len(new_tuple))  # Get length

# Indexing and slicing
print(new_tuple[1])
print(new_tuple[1:3])
print(new_tuple[:2])
print(new_tuple[2:])

try:
    new_tuple[0] = 'test'  # Tuples are immutable; this will fail
    print(new_tuple)
except TypeError as e:
    print(repr(e))
