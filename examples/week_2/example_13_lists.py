# Lists are ordered, mutable and can have duplicates
new_list = [0, 1, 2, 2, 3]

print(len(new_list))  # Get length

# Indexing and slicing
print(new_list[1])
print(new_list[1:3])
print(new_list[:2])
print(new_list[2:])
print()


# Adding, removing, and updating
languages = ['English', 'French', 'Tagalog']

languages[0] = 'Anglais'            # Update an item
languages.append('Mandarin')        # Add item to end of list
languages.insert(1, 'Icelandic')    # Add item to list at index
languages.remove('French')
print(languages)

if 'Tagalog' in languages:
    print('Kumusta')

for language in languages:
    print(f'I can count to 10 in {language}')

for index, lang in enumerate(languages):
    print(f'{index + 1}: {lang}')

# More list methods
new_list.insert(0, -1)      # Insert item at an index
new_list.extend([1, 2, 3])  # Add contents of another list to the end
print(new_list)
new_list.reverse()  # Reverse in-place
print(new_list)
print(new_list.count(1))
print(new_list.index(1))  # Find position of item if in list, else raise ValueError
new_list.sort()
print(new_list)


# Nested lists can be used for matrices
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

matrix[1][0] = 1000  # Replace the 4 with 1000
print(matrix)

# List comprehensions (more advanced)
nums = [1, 2, 3, 4]
squares = [num ** 2 for num in nums]  # Create a new list from an existing one
even_squares = [num ** 2 for num in nums if num % 2 == 0]  # Can filter with if's
