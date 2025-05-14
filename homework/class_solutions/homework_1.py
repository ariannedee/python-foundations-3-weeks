import random

def c_to_f(temp):
    return round((temp * 9 / 5) + 32)

assert c_to_f(0) == 32
assert c_to_f(36.5) == 98

reminders = [
    "Drink water",
    "Stretch for 10 minutes",
    "Go for a brisk walk",
]

name = input("Name: ").strip().title()
weather_conditions = ["sunny", "cloudy", "rainy", "snowy"]
condition = random.choice(weather_conditions)
temp_hi = random.randint(10, 20)
temp_lo = temp_hi - random.randint(5, 10)

content = f"""Good morning, {name}!

Today will be {condition}.

High: {temp_hi}°C ({c_to_f(temp_hi)}°F)
Low: {temp_lo}°C ({c_to_f(temp_lo)}°F)

Remember to:
"""

for reminder in reminders:
    content += f"- {reminder}\n"

print(content)