import sys
from pprint import pprint

import requests

from weather_codes import weather_from_code

DEBUG = False

base_url = f'https://api.open-meteo.com/v1/forecast'

params = {
    'timezone': 'America/Los_Angeles',
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

temp_high = today['temperature_2m_max'][0]
temp_low = today['temperature_2m_min'][0]
weather_code = today['weathercode'][0]
weather = weather_from_code.get(weather_code)

if weather is None:
    print(f"Weather code {weather_code} doesn't match a known code")
    weather = 'unknown'

def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32


args = sys.argv
if len(args) > 1:
    name = ' '.join(args[1:]).title()
else:
    name = input('Name: ')


temp_high_f = c_to_f(temp_high)
temp_low_f = c_to_f(temp_low)

greeting = f"""Good morning, {name.strip().title()}

Today will be {weather.lower()}.
High of {round(temp_high)} °C ({round(temp_high_f)} °F).
Low of {round(temp_low)} °C ({round(temp_low_f)} °F)

Remember to:
"""

with open('reminders.txt') as file:
    for reminder in file.readlines():
        greeting += f"- {reminder}"

print(greeting)
