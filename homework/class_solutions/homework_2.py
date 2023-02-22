import sys

import requests

from weather_codes import weather_from_code

args = sys.argv

if len(args) == 1:
    raise NameError("You must include an argument for 'name'")

name = args[1]

base_url = f'https://api.open-meteo.com/v1/forecast'

params = {
    'timezone': 'America/Vancouver',
    'latitude': 49.25235,
    'longitude': -123.0515,
    'daily': ['temperature_2m_max', 'temperature_2m_min', 'sunrise', 'sunset', 'weathercode'],
}

def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32


assert c_to_f(0) == 32, f"c_to_f(0) was {c_to_f(0)}, not 32"
assert round(c_to_f(36.5)) == round(98), f"c_to_f(36.5) was {c_to_f(37)}, not 98"


headers = {
    'content-type': 'application/json',
}

response = requests.get(base_url, headers=headers, params=params)

data = response.json()

weather_code = data['daily']['weathercode'][0]

weather = weather_from_code.get(weather_code, 'Unknown').lower()
temp_c_high = data['daily']['temperature_2m_max'][0]
temp_c_low = data['daily']['temperature_2m_min'][0]

sunrise = data['daily']['sunrise'][0]
sunset = data['daily']['sunset'][0]

temp_f_high = c_to_f(temp_c_high)
temp_f_low = c_to_f(temp_c_low)

content = f"""Good morning, {name}

Today's weather: {weather}
High: {temp_c_high} °C ({temp_f_high} °F)
Low: {temp_c_low} °C ({temp_f_low} °F)

"""

content += 'Remember to:\n'
with open('todo.txt') as file:
    for todo in file.readlines():
        content += f'- {todo}'

print(content)
