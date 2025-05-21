import sys

import requests

from weather_codes import weather_from_code


def c_to_f(temp):
    return round((temp * 9 / 5) + 32)

assert c_to_f(0) == 32
assert c_to_f(36.5) == 98

args = sys.argv

if len(args) > 1:
    name = ' '.join(args[1:]).title()
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

response = requests.get(base_url, params, headers=headers)

data = response.json()
today = data['daily']

temp_hi = today['temperature_2m_max'][0]
temp_lo = today['temperature_2m_min'][0]

code = today['weathercode'][0]
condition = weather_from_code[code]

content = f"""Good morning, {name}!

Today's condition: {condition.lower()}.

High: {temp_hi}°C ({c_to_f(temp_hi)}°F)
Low: {temp_lo}°C ({c_to_f(temp_lo)}°F)

Remember to:
"""

with open('reminders.txt') as file:
    for line in file.readlines():
        content += '- ' + line

print(content)