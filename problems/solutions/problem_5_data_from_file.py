"""
Display a list of free APIs, sorted by category
Data is from data/apis.csv
"""
import csv


def display_apis(apis):
    current_category = None
    for api in apis:
        category = api['Category']
        if category != current_category:
            print()
            if current_category is not None:
                input("Press Enter for next category")

            current_category = category
            print(category.upper())
        print(f"{api['API']}: {api['Link']}")


with open('data/apis.csv') as file:
    reader = csv.DictReader(file)
    api_list = list(reader)

display_apis(api_list)
