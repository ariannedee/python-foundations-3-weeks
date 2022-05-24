from pprint import pprint

import requests

DEBUG = False

base_url = f'https://api.openweathermap.org/data/2.5/onecall'


params = {
    'appid': '84cc4f09689acb2ab1ac614119a80558',
    'lat': 49.25235,
    'lon': -123.0515,
    'units': 'metric',
}

headers = {
    'content-type': 'application/json'
}

response = requests.get(base_url, headers=headers, params=params)

response.raise_for_status()

data = response.json()

if DEBUG:
    pprint(data)

today = data['daily'][0]

temp_hi = today['temp']['max']
temp_lo = today['temp']['min']

print(f'Today will have a high of {temp_hi}°C and low of {temp_lo}°C')
