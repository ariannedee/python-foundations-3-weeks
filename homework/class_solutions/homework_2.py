import datetime
import sys
from pprint import pprint

import requests


url = 'https://api.openweathermap.org/data/2.5/onecall'
params = {
    'appid': 'app id goes here',
    'lat': -34.58352695350743,
    'lon': -58.441551072163925,
    'exclude': 'minutely,hourly,current',
    'units': 'metric'
}

response = requests.get(url, params=params)

response.raise_for_status()

data = response.json()
weather = data['daily'][0]

# print(datetime.datetime.fromtimestamp(weather['dt']))
# pprint(weather)

def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32

assert c_to_f(0) == 32, f"Got {c_to_f(0)}"
assert round(c_to_f(36.5)) == 98, f"Got {round(c_to_f(36.5))}"

assert len(sys.argv) == 2, f'Expects name as script argument'

name = sys.argv[1].capitalize()

temp_hi = weather['temp']['max']
temp_low = weather['temp']['min']

with open('reminders.txt') as file:
    content = file.read()
    reminders = content.split('\n')

reminder_list = "\n".join([f'- {reminder}' for reminder in reminders if reminder])

content = f"""Good morning, {name}!

Today's high: {temp_hi}°C ({round(c_to_f(temp_hi))}°F)
Today's low: {temp_low}°C ({round(c_to_f(temp_low))}°F)

Remember to:
{reminder_list}
"""

print(content)
