"""
Display a list of free APIs, sorted by category
Data is from https://api.publicapis.org/entries
"""
import requests

response = requests.get("https://api.publicapis.org/entries")

response.raise_for_status()

data = response.json()
entries = data['entries']

current_category = None
count = 0
for api in entries:
    category = api['Category']
    if current_category != category:
        count = 0
        current_category = category
        print(category.upper())
    print(f"{api['API']}: {api['Link']}")
    count += 1
    if count == 10:
        input()
        count = 0
