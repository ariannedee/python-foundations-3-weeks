"""
Display a list of free APIs, sorted by category
Data is from data/apis.csv
"""
import csv

with open('data/apis.csv') as file:
    apis = csv.DictReader(file)

    last_category = None
    for api in apis:
        category = api['Category']
        if last_category != category:
            if last_category is not None:
                input('Enter for next category\n')
            print(category.upper())
        last_category = category
        print(f"{api['API']}: {api['Link']}")
