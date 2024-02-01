import sys

import requests

from weather_codes import weather_from_code

try:
    name = sys.argv[1]
except IndexError:
    name = input("What's your name? ")


def c_to_f(temp):
    return (temp * 9 / 5) + 32


base_url = f'https://api.open-meteo.com/v1/forecast'

params = {
    'timezone': 'America/Los_Angeles',
    'latitude': 42.2497,
    'longitude': -123.1193,
    'daily': ['weathercode', 'temperature_2m_max', 'temperature_2m_min', 'sunrise', 'sunset'],
    'forecast_days': 1,
}

headers = {
    'content-type': 'application/json'
}

response = requests.get(base_url, headers=headers, params=params)

data = response.json()

# print(data)

today = data['daily']

weather_code = today['weathercode'][0]
weather = weather_from_code[weather_code]
temp_c_hi = today['temperature_2m_max'][0]
temp_c_lo = today['temperature_2m_min'][0]

greeting = f"""Good morning, {name.strip().title()}!
Today is going to be {weather.lower()}.
High: {temp_c_hi}°C ({c_to_f(temp_c_hi)}°F)
Low: {temp_c_lo}°C ({c_to_f(temp_c_lo)}°F)

Remember to:
"""

with open('reminders.txt') as file:
    for reminder in file.readlines():
        greeting += f"- {reminder.capitalize()}"

print(greeting)
