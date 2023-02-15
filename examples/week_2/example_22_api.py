from pprint import pprint

import requests

DEBUG = True

base_url = f'https://api.open-meteo.com/v1/forecast'

params = {
    'timezone': 'America/Vancouver',
    'latitude': 49.25235,
    'longitude': -123.0515,
    'daily': ['temperature_2m_max', 'temperature_2m_min', 'sunrise', 'sunset'],
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

temp_hi = today['temperature_2m_max'][0]
temp_lo = today['temperature_2m_min'][0]

print(f'Today will have a high of {temp_hi}°C and low of {temp_lo}°C')
