import sys
from pprint import pprint

import requests

from weather_codes import weather_from_code

DEBUG = False

args = sys.argv[1:]

base_url = 'https://api.open-meteo.com/v1/forecast'

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

def c_to_f(temp_c: float) -> float:
    return (temp_c * 9 / 5) + 32

assert c_to_f(0) == 32, f"Expected 32 but got {c_to_f(0)}"
assert round(c_to_f(36.5)) == 98, f"Expected 98 but got {round(c_to_f(36.5))}"

if args:
    name = " ".join(args)
else:
    name = input("Name: ")

response = requests.get(base_url, params=params, headers=headers)

data = response.json()

if DEBUG:
    print(response.url)
    pprint(data)

today = data['daily']

temp_high = today['temperature_2m_max'][0]
temp_low = today['temperature_2m_min'][0]

weathercode = today['weathercode'][0]
weather = weather_from_code.get(weathercode, f"Code {weathercode} not found")

content = f"""Good morning, {name.strip().title()}!

Today there will be {weather.lower()}.
High: {temp_high:.0f}°C ({c_to_f(temp_high):.0f}°F)
Low: {temp_low:.0f}°C ({c_to_f(temp_low):.0f}°F)

Daily mantra:
{'Seize the day!'}

Remember to:
"""
with open("reminders.txt", "rt") as file:
    for reminder in file.readlines():
        content += f"- {reminder}"

print(content)
