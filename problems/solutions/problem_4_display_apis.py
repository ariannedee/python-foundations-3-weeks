"""
Display a list of free APIs, sorted by category
Data is hardcoded in file
"""
sample_apis = [
    {'Name': 'Dog facts', 'URL': 'https://dukengn.github.io/Dog-facts-API/', 'Category': 'Animal'},
    {'Name': 'PoetryDB', 'URL': 'https://github.com/thundercomb/poetrydb', 'Category': 'Books'},
    {'Name': 'Random dog', 'URL': 'https://random.dog/woof.json', 'Category': 'Animal'},
    {'Name': 'Open-Meteo', 'URL': 'https://open-meteo.com/', 'Category': 'Weather'},
    {'Name': 'Colormind', 'URL': 'http://colormind.io/api-access/', 'Category': 'Art & Design'},
    {'Name': 'Cat facts', 'URL': 'https://alexwohlbruck.github.io/cat-facts/', 'Category': 'Animal'},
    {'Name': 'Pixel Encounter', 'URL': 'https://pixelencounter.com/api', 'Category': 'Art & Design'},
    {'Name': 'Bored', 'URL': 'https://www.boredapi.com/', 'Category': 'Development'},
]

# ANIMAL
# Cat facts: https://alexwohlbruck.github.io/cat-facts/
# Dog facts: https://dukengn.github.io/Dog-facts-API/

def category_sort(api_dict):
    return api_dict['Category'] + api_dict['Name']

sample_apis.sort(key=category_sort)

current_category = None
for api in sample_apis:
    category = api['Category']
    if category != current_category:
        if current_category is not None:
            input()
        current_category = category
        print(category.upper())
    print(f"{api['Name']}: {api['URL']}")
