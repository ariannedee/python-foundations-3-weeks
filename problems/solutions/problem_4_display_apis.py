from collections import defaultdict

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


def display_by_category(api_list, num_per_page=None):
    apis_by_category = defaultdict(list)
    for api in api_list:
        apis_by_category[api['Category']].append(api)

    for category, apis in apis_by_category.items():
        print(f"---- {category.upper()} ----")
        for i, api in enumerate(apis):
            print(f"{api['API']}: {api['Link']}")
            if num_per_page and (i + 1) % num_per_page == 0:
                input()
        input()


if __name__ == '__main__':
    display_by_category(sample_apis)
