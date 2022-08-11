import random


def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32

assert c_to_f(0) == 32, f"Got {c_to_f(0)}"
assert round(c_to_f(36.5)) == 98, f"Got {round(c_to_f(36.5))}"

reminders = [
    "Go for a walk",
    "Stretch",
    "Drink water"
]

name = input('What is your name? ').capitalize()

temp_hi = random.randint(10, 35)
temp_low = temp_hi - random.randint(5, 15)

reminder_list = "\n".join([f'- {reminder}' for reminder in reminders])
content = f"""Good morning, {name}!

Today's high: {temp_hi}°C ({round(c_to_f(temp_hi))}°F)
Today's low: {temp_low}°C ({round(c_to_f(temp_low))}°F)

Remember to:
{reminder_list}
"""

print(content)
