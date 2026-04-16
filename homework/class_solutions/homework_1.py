import random


def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32

assert c_to_f(0) == 32, f"Expected {32} but got {c_to_f(0)}"
assert round(c_to_f(36.5)) == 98, f"Expected {98} but got {round(c_to_f(36.5))}"

todos = [
    "Get groceries",
    "Drink water",
    "Go to gym",
]

name = input("Name: ").strip().title()
weather_conditions = ["sunny", "cloudy", "rainy"]
weather = random.choice(weather_conditions)
temp_c_high = random.randint(7, 20)
temp_c_low = temp_c_high - random.randint(4, 8)

content = f"""Good morning, {name}!
Today is going to be {weather}.
High: {temp_c_high}°C ({c_to_f(temp_c_high):.0f}°F)
Low: {temp_c_low}°C ({c_to_f(temp_c_low):.0f}°F)

Remember to:"""

for todo in todos:
    content += "\n- " + todo

print(content)