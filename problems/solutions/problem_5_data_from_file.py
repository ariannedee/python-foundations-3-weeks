"""Print out the API list, sorted by category, from data/apis.csv"""
import csv

with open('data/apis.csv') as file:
    reader = csv.DictReader(file)

    current_category = None
    for api in reader:
        category = api['Category']
        if current_category != category:
            print()
            current_category = category
            print(category.upper())
        print(f"{api['API']}: {api['Link']}")
