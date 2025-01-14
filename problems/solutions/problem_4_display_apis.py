"""
Display a list of free APIs, sorted by category
Data is hardcoded in file
"""
sample_apis = [
    {'Name': 'Dog facts', 'URL': 'https://dukengn.github.io/Dog-facts-API/', 'Category': 'Animal'},
    {'Name': 'PoetryDB', 'URL': 'https://github.com/thundercomb/poetrydb', 'Category': 'Books'},
    {'Name': 'Colormind', 'URL': 'http://colormind.io/api-access/', 'Category': 'Art & Design'},
    {'Name': 'Pixel Encounter', 'URL': 'https://pixelencounter.com/api', 'Category': 'Art & Design'},
    {'Name': 'Random dog', 'URL': 'https://random.dog/woof.json', 'Category': 'Animal'},
    {'Name': 'Cat facts', 'URL': 'https://alexwohlbruck.github.io/cat-facts/', 'Category': 'Animal'},
    {'Name': 'Bored', 'URL': 'https://www.boredapi.com/', 'Category': 'Development'},
    {'Name': 'Open-Meteo', 'URL': 'https://open-meteo.com/', 'Category': 'Weather'},
]


def sort_by_category(api_dict):
    return api_dict['Category'] + api_dict['Name']


sample_apis.sort(key=sort_by_category)

# sample_apis.sort(key=lambda api_dict: api_dict['Category'] + api_dict['Name'])

# ANIMAL
# Cat facts: https://alexwohlbruck.github.io/cat-facts/
# Dog facts: https://dukengn.github.io/Dog-facts-API/

last_category = None
for api in sample_apis:
    category = api['Category']
    if last_category != category:
        if last_category is not None:
            input()
        print(category.upper())
    last_category = category
    print(f"{api['Name']}: {api['URL']}")
