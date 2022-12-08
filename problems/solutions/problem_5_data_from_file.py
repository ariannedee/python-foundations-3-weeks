import csv
from collections import defaultdict

def print_by_category(api_list, num_per_page=None):
    apis_by_category = defaultdict(list)

    for api in api_list:
        category = api['Category']
        apis_by_category[category].append(api)

    for category, apis in apis_by_category.items():
        print(category.upper())
        print()
        for i, api in enumerate(apis, start=1):
            print(f"{api['API']}: {api['Link']}")
            if num_per_page and i % num_per_page == 0:
                input()
        input()

while True:
    try:
        num_per_page = int(input("How many results to display at a time? "))
        break
    except ValueError:
        print("Invalid number")

with open('data/apis.csv', 'r') as file:
    reader = csv.DictReader(file)
    print_by_category(reader, num_per_page)
