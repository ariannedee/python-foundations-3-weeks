from pprint import pprint
import sys

import requests

from weather_codes import weather_from_code


DEBUG = False

def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32


assert c_to_f(0) == 32, f"Got {c_to_f(0)}"
assert round(c_to_f(36.5)) == 98, f"Got {c_to_f(0)}"

assert len(sys.argv) == 2, "Expected file argument for 'name'"
name = sys.argv[1].strip().title()

# GET WEATHER
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

if DEBUG:
    print(response.url)
    pprint(data)

todays_data = data['daily']
today_code = todays_data['weathercode'][0]

today_weather = weather_from_code[today_code].lower()
temp_c_high = todays_data['temperature_2m_max'][0]
temp_c_low = todays_data['temperature_2m_min'][0]

# GET REMINDERS
with open('todos.txt') as file:
    reminders = file.read().split('\n')

# EMAIL CONTENT
content = f"""Hello {name},

Today is going to be {today_weather}.

High of {temp_c_high}°C ({c_to_f(temp_c_high)}°F) 
Low of {temp_c_low}°C ({c_to_f(temp_c_low)}°F) 

Remember to:
"""

for reminder in reminders:
    content += f"- {reminder}\n"


print(content)
