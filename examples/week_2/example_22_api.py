from datetime import datetime
from pprint import pprint

import requests

DEBUG = True

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

response = requests.get(base_url, params=params, headers=headers)

data = response.json()

if DEBUG:
    print(response.url)
    pprint(data)

today = data['daily']

temp_hi = today['temperature_2m_max'][0]
temp_lo = today['temperature_2m_min'][0]

# See https://strftime.org/ for datetime format codes
sunrise = datetime.fromisoformat(today['sunrise'][0]).strftime("%-I:%M %p")
sunset = datetime.fromisoformat(today['sunset'][0]).strftime("%-I:%M %p")

print(f'Today will have a high of {temp_hi}°C and low of {temp_lo}°C')
print(f'Sunrise ☀️{sunrise}')
print(f'Sunset 🌙️{sunset}')
