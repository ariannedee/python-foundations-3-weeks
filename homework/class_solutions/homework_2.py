import sys
import requests

args = sys.argv

assert len(args) == 2, "Expected 1 argument of name"

name = args[1].strip().title()

def c_to_f(temp_c):
    return round((temp_c * 9 / 5) + 32)

assert c_to_f(0) == 32

greeting = f"Good morning, {name}!"

weather_url = "https://api.open-meteo.com/v1/forecast"
params = {
    'latitude': 35.67,
    'longitude': 139.65,
    'timezone': 'America/Vancouver',
    'daily': 'temperature_2m_max,temperature_2m_min'
}
response = requests.get(weather_url, params)

if response.status_code == 200:
    data = response.json()
    temp_hi_f = c_to_f(temp_hi)
    temp_lo_f = c_to_f(temp_lo)
    greeting += f"""
Today is going to be {weather}.
High: {round(temp_hi)} °C ({round(temp_hi_f)} °F)
Low: {round(temp_lo)} °C ({round(temp_lo_f)} °F)
"""
else:
    error = f"Got {response.status_code}: {response.reason}"
    print(error)
    try:
        data = response.json()
        print(data)
    except Exception as e:
        print(repr(e))

greeting += "\nRemember to:\n"
with open('reminders.txt', 'r') as file:
    reminders = []
    for reminder in file:
        greeting += f"- {reminder}"

print(greeting)
