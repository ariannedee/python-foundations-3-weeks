import sys
from datetime import datetime
from pprint import pprint

import requests

from weather_codes import weather_from_code

DEBUG = False


def c_to_f(temp: float):
    return (temp * 9 / 5) + 32


name_args = sys.argv[1:]

if name_args:
    name = " ".join(name_args).title()
else:
    name = input("Name: ").strip().title()

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

response = requests.get(base_url, params=params, headers=headers)

data = response.json()

if DEBUG:
    print(response.url)
    pprint(data)

today = data['daily']

temp_c_high = today['temperature_2m_max'][0]
temp_c_low = today['temperature_2m_min'][0]

weathercode = today['weathercode'][0]
weather = weather_from_code.get(weathercode, f"unknown condition for code {weathercode}")

sunrise = datetime.fromisoformat(today['sunrise'][0]).strftime("%-I:%M %p")
sunset = datetime.fromisoformat(today['sunset'][0]).strftime("%-I:%M %p")

content = f"""Good morning, {name}.

Today is going to be {weather.lower()}.
High temp: {temp_c_high:.0f}°C ({c_to_f(temp_c_high):.0f}°F)
Low temp: {temp_c_low:.0f}°C ({c_to_f(temp_c_low):.0f}°F)

Sunrise: {sunrise}
Sunset: {sunset}

Remember to:
"""

with open('todos.txt') as file:
    for todo in file.readlines():
        content += f"- {todo.strip()}\n"

print(content)
