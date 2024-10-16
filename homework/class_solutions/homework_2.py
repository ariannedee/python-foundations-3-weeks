import sys

import requests

from homework.weather_codes import weather_from_code

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

response = requests.get(base_url, headers=headers, params=params)

data = response.json()

def c_to_f(temp):
    return (temp * 9 / 5) + 32


def assert_equals(actual, expected):
    assert actual == expected, f"Expected {expected} but got {actual}"


assert_equals(c_to_f(0), 32)
assert_equals(round(c_to_f(36.5)),98)

if len(sys.argv) == 1:
    name = 'arianne'
else:
    name = ' '.join(sys.argv[1:])

weathercode = data['daily']['weathercode'][0]
weather = weather_from_code[weathercode]
temp_c_high = data['daily']['temperature_2m_max'][0]
temp_c_low = data['daily']['temperature_2m_min'][0]

sunrise_str = data['daily']['sunrise'][0]
sunset_str = data['daily']['sunset'][0]

sunrise = sunrise_str.split('T')[1]
sunset = sunset_str.split('T')[1]

with open('reminders.txt') as file:
    reminders = file.readlines()

greeting = f"""Good morning, {name.title()}!
Today will be {weather.lower()}.

High of {temp_c_high:.0f} °C ({c_to_f(temp_c_high):.0f} °F)
Low of {temp_c_low:.0f} °C ({c_to_f(temp_c_low):.0f} °F)

Sunrise: {sunrise}
Sunset: {sunset}

Remember to:
{''.join([f"- {reminder}" for reminder in reminders])}

Have a great day!
"""

print(greeting)