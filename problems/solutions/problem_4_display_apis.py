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

# ANIMAL
# Cat facts: https://alexwohlbruck.github.io/cat-facts/
# Dog facts: https://dukengn.github.io/Dog-facts-API/


def display_apis(api_list):
    current_category = None

    for api in api_list:
        category = api["Category"]
        if category != current_category:
            if current_category is not None:
                input()
            current_category = category
            print(current_category.upper())
        print(f"{api['Name']}: {api['URL']}")
