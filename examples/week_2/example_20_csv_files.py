import csv

with open('data/people.csv', 'r') as file:
    reader = csv.DictReader(file)

    for person in reader:
        print(f'{person["Name"]} is {person["Age"]}')
