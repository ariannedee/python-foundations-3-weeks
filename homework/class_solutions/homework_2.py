from datetime import datetime
from pprint import pprint
import sys
import requests

# https://openweathermap.org/api/one-call-api
base_url = f'https://api.openweathermap.org/data/2.5/onecall'
coords = (49.25481095208678, -123.06157037494123)

params = {
    'appid': '...',
    'lat': coords[0],
    'lon': coords[1],
    'exclude': 'minutely,hourly,current',
    'units': 'metric',
}

headers = {
    'content-type': 'application/json'
}

response = requests.get(base_url, headers=headers, params=params)

weather = response.json()['daily'][0]
pprint(weather)

def c_to_f(temp):
    return (temp * 9 / 5) + 32

assert len(sys.argv) == 2

name = sys.argv[1].strip().title()
condition = weather['weather'][0]['description']
temp_c_high = weather['temp']['max']
temp_c_low = weather['temp']['min']
sunrise = datetime.fromtimestamp(weather['sunrise'])
sunset = datetime.fromtimestamp(weather['sunset'])
temp_f_high = c_to_f(temp_c_high)
temp_f_low = c_to_f(temp_c_low)

reminders = []
with open('reminders.txt') as file:
    for line in file.readlines():
        reminders.append(line.strip())

print('------------------------------')

content = f"""
Good morning, {name}

Today there will be {condition}.
High: {temp_c_high:.1f} °C ({temp_f_high:.1f} °F)
Low: {temp_c_low:.1f} °C ({temp_f_low:.1f} °F)

Sunrise:️ {datetime.strftime(sunrise, '%-I:%M %p')}
Sunset: {datetime.strftime(sunset, '%-I:%M %p')}

"""

content += 'Remember to:\n'
for reminder in reminders:
    content += f'- {reminder}\n'

# More API content
print(content)
