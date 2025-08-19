"""
Display a list of free APIs, sorted by category
Data is from data/apis.csv
"""
import csv

from problem_4_display_apis import display_apis

with open('data/apis.csv') as file:
    file.readline()
    fieldnames = ['Name', 'Description', 'Auth', 'HTTPS', 'Cors', 'URL', 'Category']
    reader = csv.DictReader(file, fieldnames)

    display_apis(api_list=list(reader))
