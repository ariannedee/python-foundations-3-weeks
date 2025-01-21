from pprint import pprint

import requests
from weather_codes import weather_from_code

import sys

DEBUG = False

args = sys.argv[1:]
if len(args) > 0:
    name = ' '.join(args).strip().title()
else:
    name = input("Name: ").strip().title()

base_url = f'https://api.open-meteo.com/v1/forecast'

params = {
    'timezone': 'America/New_York',
    'latitude': 42.997262156214305,
    'longitude': -81.20390128320294,
    'daily': ['weathercode', 'temperature_2m_max', 'temperature_2m_min', 'sunrise', 'sunset'],
    'forecast_days': 1,
}

headers = {
    'content-type': 'application/json'
}

response = requests.get(base_url, headers=headers, params=params)

data = response.json()

if DEBUG:
    print(response.url)
    pprint(data)

today = data['daily']

high_temp_c = today['temperature_2m_max'][0]
low_temp_c = today['temperature_2m_min'][0]
weather_code = today['weathercode'][0]
weather = weather_from_code[weather_code].lower()


def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32


assert c_to_f(0) == 32, f'Expected 32 but got {c_to_f(0)}'
assert round(c_to_f(36.7)) == 98, f'Expected 98 but got {round(c_to_f(36.7))}'

message = f"""Good morning {name}!

Today will be {weather}.

High: {high_temp_c:.1f}°C ({c_to_f(high_temp_c):.1f}°F)
Low: {low_temp_c:.1f}°C ({c_to_f(low_temp_c):.1f}°F)

Remember to:
"""
with open('reminders.txt') as file:
    for reminder in file.readlines():
        message += f"- {reminder}"

print(message)