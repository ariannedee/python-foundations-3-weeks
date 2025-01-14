import random


def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32


assert c_to_f(0) == 32, f'Expected 32 but got {c_to_f(0)}'
assert round(c_to_f(36.7)) == 98, f'Expected 98 but got {round(c_to_f(36.7))}'


reminders = ['Breathe deeply', 'Drink more water', 'Stretch twice a day']
weather_conditions = ['sunny', 'cloudy', 'rainy', 'snowy']

name = input("Name: ").strip().title()
weather = random.choice(weather_conditions)
high_temp_c = random.randint(8, 12)
low_temp_c = random.randint(0, 5)

message = f"""Good morning {name}!

Today will be {weather}.

High: {high_temp_c}C ({c_to_f(high_temp_c)}F)
Low: {low_temp_c}C ({c_to_f(low_temp_c)}F)

Remember to:
"""

for reminder in reminders:
    message += f"- {reminder}\n"

print(message)