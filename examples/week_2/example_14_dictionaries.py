# Dictionaries are key-value based, unordered, and mutable
a_dict = {'a': 'apple', 'b': 'banana', 'c': 'cantaloupe'}

print(a_dict['b'])             # Retrieve an item
print(a_dict.get('b'))         # Retrieve an item safely
print(a_dict.get('d'))         # If key doesn't exist, return None
print(a_dict.get('d', 'N/A'))  # If key doesn't exist, return a default value

a_dict['d'] = 'dragonfruit'  # Add a new item
a_dict['b'] = 'blueberry'    # Update an item
del a_dict['a']              # Delete an item

# Looping over dictionaries
for letter in a_dict:  # Loops over keys by default
    print(f'{letter}: {a_dict[letter]}')

for fruit in a_dict.values():  # Loop over values
    print(fruit)

for letter, fruit in a_dict.items():  # Loop over (key, value). This is preferred
    print(f'{letter}: {fruit}')

if 'a' in a_dict:
    print('Found key')

# Dictionaries as maps
best_picture_winners = {
    2020: 'Nomadland',
    2019: 'Parasite',
    2018: 'Green Book',
    2017: 'Shape of Water'
}

for year, movie in best_picture_winners.items():
    print(f'{movie} won in {year}')


# Dictionaries as objects
movie_1 = {"title": "Avatar", "year": 2009, "GBO": 2847}
movie_2 = {"title": "Avengers: Endgame", "year": 2019, "GBO": 2797}
movie_3 = {"title": "Titanic", "year": 1997, "GBO": 2187}

highest_grossing_movies = [movie_1, movie_2, movie_3]


def movie_sort_function(movie):
    return movie['year']


highest_grossing_movies.sort(key=movie_sort_function)
highest_grossing_movies.sort(key=lambda movie: movie['year'])  # Lambda functions: one-line, unnamed functions

for movie in highest_grossing_movies:
    print(f"{movie['title']} made ${movie['GBO']/1000} billion in {movie['year']}")
