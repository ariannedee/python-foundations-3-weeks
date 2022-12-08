from collections import defaultdict

import click
import requests
from csv import DictReader, DictWriter


def display_api(api):
    print(f"{api['API']}: {api['Link']} (Auth: {api['Auth']})")

@click.command()
@click.option('--load', is_flag=True, help='Load fresh data.')
@click.option('--no-auth', is_flag=True, prompt='No auth required')
def run(load, no_auth):
    if load:
        load_data()

    with open('apis.csv', 'r') as file:
        reader = DictReader(file)
        apis_by_cat = defaultdict(list)
        for api in reader:
            if not no_auth or not api['Auth']:
                category = api['Category']
                apis_by_cat[category].append(api)

    for category, apis in apis_by_cat.items():
        print(category.upper())
        print()
        for api in apis:
            display_api(api)
        input()


def load_data():
    url = "https://api.publicapis.org/entries"
    print(f"Loading data from {url}")
    response = requests.get(url)
    data = response.json()

    fieldnames = data['entries'][0].keys()
    with open('apis.csv', 'w') as file:
        writer = DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data['entries'])


run()
