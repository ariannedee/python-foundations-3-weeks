from csv import DictReader

from problem_4_display_apis import display_by_category

while True:
    try:
        num_results = int(input("How many results to show at a time? "))
        break
    except ValueError:
        print("Invalid number")

with open('data/apis.csv', 'r') as file:
    reader = DictReader(file)
    display_by_category(reader, num_results)
