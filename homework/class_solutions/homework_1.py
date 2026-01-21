import random


def c_to_f(temp_c: float) -> float:
    return (temp_c * 9 / 5) + 32

assert c_to_f(0) == 32, f"Expected 32 but got {c_to_f(0)}"
assert round(c_to_f(36.5)) == 98, f"Expected 98 but got {round(c_to_f(36.5))}"

reminders = ['Drink water', 'Stretch']

name = input("Name: ").strip().title()
weather = random.choice(['sunny', 'cloudy', 'rainy', 'foggy'])
temp_high = random.randint(5, 15)
temp_low = temp_high - random.uniform(5, 10)

content = f"""Good morning, {name}!

Today is going to be {weather}.
High: {temp_high:.0f}°C ({c_to_f(temp_high):.0f}°F)
Low: {temp_low:.0f}°C ({c_to_f(temp_low):.0f}°F)

Daily mantra:
{'Seize the day!'}

Remember to:
"""

for reminder in reminders:
    content += f"- {reminder}\n"

print(content)