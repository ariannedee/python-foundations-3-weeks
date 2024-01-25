import random


def c_to_f(temp):
    return (temp * 9 / 5) + 32


reminders = [
    'drink water',
    'stretch',
    'move',
]

name = input("What's your name? ").strip().title()
weather = input("What's the weather? ").strip().lower()
temp_c_hi = random.randint(5, 10)
temp_c_lo = random.randint(-2, 4)

greeting = f"""Good morning, {name}!
Today is going to be {weather}.
High: {temp_c_hi}°C ({c_to_f(temp_c_hi)}°F)'
Low: {temp_c_lo}°C ({c_to_f(temp_c_lo)}°F)'

Remember to:
"""

for reminder in reminders:
    greeting += f"- {reminder}\n"

print(greeting)
