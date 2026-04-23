import random
import sys

from weather_codes import weather_from_code

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:]).strip().title()
else:
    name = input("Name: ").strip().title()


def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32

assert c_to_f(0) == 32, f"Expected {32} but got {c_to_f(0)}"
assert round(c_to_f(36.5)) == 98, f"Expected {98} but got {round(c_to_f(36.5))}"

with open("todos.txt") as file:
    todos = list(file.readlines())

from datetime import datetime
from pprint import pprint

import requests

DEBUG = True

base_url = 'https://api.open-meteo.com/v1/forecast'

params = {
    'timezone': 'America/Los_Angeles',
    'latitude': 49.2497,
    'longitude': -123.1193,
    'daily': ['weathercode', 'temperature_2m_max', 'temperature_2m_min', 'sunrise', 'sunset'],
    'forecast_days': 1,
}

headers = {
    'content-type': 'application/json'
}

response = requests.get(base_url, params=params, headers=headers)

data = response.json()

if DEBUG:
    print(response.url)
    pprint(data)

today = data['daily']

temp_c_high = today['temperature_2m_max'][0]
temp_c_low = today['temperature_2m_min'][0]
weather_code = today['weathercode'][0]
try:
    weather = weather_from_code[weather_code]
except KeyError:
    print(f"Weather code {weather_code} not found")
    weather = "unknown"

content = f"""Good morning, {name}!
Today is going to be {weather.lower()}.
High: {temp_c_high}°C ({c_to_f(temp_c_high):.0f}°F)
Low: {temp_c_low}°C ({c_to_f(temp_c_low):.0f}°F)

Remember to:"""

for todo in todos:
    content += "\n- " + todo.strip()

print(content)
