import sys
from datetime import datetime

import requests

assert len(sys.argv) > 1, "Expected name as a script argument"
name = sys.argv[1]

def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32

base_url = f'https://api.openweathermap.org/data/2.5/onecall'
params = {
    'appid': 'Your app id',
    'lat': 49.25235,
    'lon': -123.0515,
    'units': 'metric',
    'exclude': 'minutely,hourly,current'
}
headers = {
    'content-type': 'application/json'
}

response = requests.get(base_url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    today = data['daily'][0]
    high_c = today['temp']['max']
    low_c = today['temp']['min']
    condition = today['weather'][0]['description']
    sunrise = datetime.fromtimestamp(today['sunrise'])
    sunset = datetime.fromtimestamp(today['sunset'])
    weather_string = f"""
Today there will be {condition}.
High: {high_c} °C ({c_to_f(high_c)} °F)
Low: {low_c} °C ({c_to_f(low_c)} °F)
Sunrise:️ {datetime.strftime(sunrise, '%-I:%M %p')}
Sunset: {datetime.strftime(sunset, '%-I:%M %p')}
"""
else:
    weather_string = "Could not retrieve weather"

reminder_string = 'Remember to:'

with open('reminders.txt') as file:
    reminders = file.readlines()
    print(len(reminders))
    if not len(reminders):
        reminder_string += '\n  No reminders'
    else:
        for reminder in reminders:
            reminder_string += f'\n- {reminder.strip()}'

email = f"""
Good morning, {name}!
{weather_string}
{reminder_string}"""

print(email)
