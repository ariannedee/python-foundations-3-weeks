import random


def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32


assert c_to_f(0) == 32, f"got {c_to_f(0)}"
assert round(c_to_f(36.5)) == 98, f"got {round(c_to_f(36.5))}"


reminders = [
    "Go for a walk",
    "Drink 3 bottles of water",
    "Meditate",
]

name = input("Name: ").strip().capitalize()
conditions = ['sunny', 'cloudy', 'rainy', 'snowy']
weather_condition = random.choice(conditions)
temp_c = random.randint(18, 28)

greeting = f"""Hello, {name}!
Today is going to be {weather_condition} and {temp_c}°C ({c_to_f(temp_c)})°F.

Remember to:
"""

for reminder in reminders:
    greeting += f"- {reminder}\n"

print(greeting)
