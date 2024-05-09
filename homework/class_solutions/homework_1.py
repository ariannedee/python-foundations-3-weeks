import random


def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32


reminders = [
    'Stretches',
    'Drink 9 cups of water',
]

name = 'arianne'
weather = input("Weather: ")
temp_high = random.randint(13, 25)
temp_low = random.randint(3, 10)

temp_high_f = c_to_f(temp_high)
temp_low_f = c_to_f(temp_low)

greeting = f"""Good morning, {name.strip().title()}

Today will be {weather}.
High of {round(temp_high)} °C ({round(temp_high_f)} °F).
Low of {round(temp_low)} °C ({round(temp_low_f)} °F)

Remember to:
"""

for reminder in reminders:
    greeting += f"- {reminder}\n"

print(greeting)
