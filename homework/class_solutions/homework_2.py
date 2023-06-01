import sys
import requests
from pprint import pprint

from weather_codes import weather_from_code

DEBUG = False

URL = f'https://api.open-meteo.com/v1/forecast'

params = {
    'timezone': 'America/Vancouver',
    'latitude': 49.25235,
    'longitude': -123.0515,
    'daily': ['weathercode', 'temperature_2m_max', 'temperature_2m_min', 'sunrise', 'sunset'],
}
headers = {
    'content-type': 'application/json'
}

response = requests.get(URL, headers=headers, params=params)

data = response.json()

if DEBUG:
    print(response.url)
    pprint(data)


def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32


assert c_to_f(0) == 32, f"got {c_to_f(0)}"
assert round(c_to_f(36.5)) == 98, f"got {round(c_to_f(36.5))}"


args = sys.argv[1:]  # list of string arguments after the filename
if len(args):
    name = ' '.join(args)  # Concatenate list of strings, with spaces in between
else:
    name = input("Name: ")

name = name.strip().title()
today = data['daily']
code = today['weathercode'][0]
weather_condition = weather_from_code.get(code, f"Code {code} not found").lower()

temp_hi = today['temperature_2m_max'][0]
temp_lo = today['temperature_2m_min'][0]


greeting = f"""Hello, {name}!

Today is going to be {weather_condition}.
High: {temp_hi}°C ({c_to_f(temp_hi)})°F.
Low: {temp_lo}°C ({c_to_f(temp_lo)})°F.

Remember to:
"""

with open('reminders.txt', 'r') as file:
    for reminder in file.readlines():
        greeting += f"- {reminder}"

print(greeting)
