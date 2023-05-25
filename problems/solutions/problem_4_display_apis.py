"""
Display a list of free APIs, sorted by category
Data is hardcoded in file
"""
sample_apis = [
    {'Name': 'Cat facts', 'URL': 'https://alexwohlbruck.github.io/cat-facts/', 'Category': 'Animal'},
    {'Name': 'Dog facts', 'URL': 'https://dukengn.github.io/Dog-facts-API/', 'Category': 'Animal'},
    {'Name': 'Random dog', 'URL': 'https://random.dog/woof.json', 'Category': 'Animal'},
    {'Name': 'Colormind', 'URL': 'http://colormind.io/api-access/', 'Category': 'Art & Design'},
    {'Name': 'Pixel Encounter', 'URL': 'https://pixelencounter.com/api', 'Category': 'Art & Design'},
    {'Name': 'PoetryDB', 'URL': 'https://github.com/thundercomb/poetrydb', 'Category': 'Books'},
    {'Name': 'Bored', 'URL': 'https://www.boredapi.com/', 'Category': 'Development'},
    {'Name': 'Open-Meteo', 'URL': 'https://open-meteo.com/', 'Category': 'Weather'},
]

# todo: Print the apis, organized by category
# ANIMAL
# Cat facts: https://alexwohlbruck.github.io/cat-facts/
# Dog facts: https://dukengn.github.io/Dog-facts-API/

# Loop over list and print the category if it changes
current_category = None
for api in sample_apis:
    category = api['Category']
    if current_category != category:
        print()
        current_category = category
        print(category.upper())
    print(f"{api['Name']}: {api['URL']}")


# Organize the apis by category
# Loop over all the categories and the apis in them

apis_by_cat = {}  # Key = catgory, value = list of apis in that category

for api in sample_apis:
    category = api['Category']
    if category not in apis_by_cat:  # Set the value to an empty list if it's a new category
        apis_by_cat[category] = []
    apis_by_cat[category].append(api)

for category, apis in apis_by_cat.items():  # Loop over categories and print the apis in them
    print(category.upper())
    for api in apis:
        print(f"{api['Name']}: {api['URL']}")
    print()
