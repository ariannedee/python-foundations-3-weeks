# Sets are unordered, mutable, and cannot have duplicates
new_set = {0, 1, 2, 2, 3}

print(len(new_set))  # Get length

new_set.add(4)  # Add an item
new_set.pop()  # Get and remove an item
print(new_set)  # {1, 2, 3, 4}

# Use set functions/methods to compare with another set
another = {3, 4, 5, 6}

# Combine two sets
print(new_set.union(another))
print(new_set | another)

# Get common items
print(new_set.intersection(another))
print(new_set & another)

# Get items in one that are not in the other
print(new_set.difference(another))
print(new_set - another)
