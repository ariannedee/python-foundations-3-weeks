import sys
from pprint import pprint

import requests

from weather_codes import weather_from_code

DEBUG = False

def c_to_f(temp_c: int | float) -> float:
    return (temp_c * 9 / 5) + 32

args = sys.argv[1:]
if args:
    name = " ".join(args)
else:
    name = input("Name: ").strip()

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
    pprint(data)

today = data['daily']

temp_c_high = today['temperature_2m_max'][0]
temp_c_low = today['temperature_2m_min'][0]
weathercode = today['weathercode'][0]
weather = weather_from_code.get(weathercode, f"[unknown weather for code {weathercode}]")


content = f"""Good morning, {name.title()}!

Today is going to be {weather.lower()}.
High: {temp_c_high:.0f}°C ({c_to_f(temp_c_high):.0f}°F)
Low: {temp_c_low:.0f}°C ({c_to_f(temp_c_low):.0f}°F)

Remember to:
"""
with open("reminders.txt") as file:
    for reminder in file.readlines():
        content += "- " + reminder

print(content)