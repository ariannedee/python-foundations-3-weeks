import sys

import requests

from weather_codes import weather_from_code


def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32


name = " ".join(sys.argv[1:])

if not name:
    name = input("Name: ")

name = name.strip().title()

# Content greeting
content = f"Good morning, {name}!\n"

WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 49.2497,
    "longitude": -123.1193,
    "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "sunrise", "sunset"],
    "timezone": "America/Los_Angeles",
    "forecast_days": 1,
}
headers = {
    'content-type': 'application/json'
}
response = requests.get(WEATHER_URL, params, headers=headers)

errors = []

if response.status_code != 200:
    errors.append(f"Error getting weather data from {WEATHER_URL} with {params}\n{response.url}")
else:
    data = response.json()
    daily = data["daily"]

    weather_code = data["daily"]["weather_code"][0]
    weather = weather_from_code.get(weather_code, f"unknown ({weather_code})").lower()
    temp_c_high = data["daily"]["temperature_2m_max"][0]
    temp_c_low = data["daily"]["temperature_2m_min"][0]

    # Content weather
    content += f"""\nToday is going to be {weather}.

High: {temp_c_high:.0f}°C ({c_to_f(temp_c_high):.0f}°F)
Low: {temp_c_low:.0f}°C ({c_to_f(temp_c_low):.0f}°F)
\n"""

# Content todos
content += "Remember to:"

with open("reminders.txt") as file:
    for reminder in file.readlines():
        content += "\n- " + reminder.strip().capitalize()

# Content errors
if errors:
    content += "\n\nERRORS -"
    for error in errors:
        content += f"\n[Error]: {error}"

print(content)
