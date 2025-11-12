from random import choice, randint


def c_to_f(temp: float):
    return (temp * 9 / 5) + 32


todos = [
    'Go for a walk',
    'Drink water',
    'Stretch',
]

weather_options = ['sunny', 'cloudy', 'rainy', 'foggy']

name = input("Name: ").strip().title()

weather = choice(weather_options)
temp_c_high = randint(10, 25)
temp_c_low = randint(0, 10)


content = f"""Good morning, {name}.

Today is going to be {weather}.
High temp: {temp_c_high}°C ({c_to_f(temp_c_high):.1f}°F)
Low temp: {temp_c_low}°C ({c_to_f(temp_c_low):.1f}°F)

Remember to:
"""

for todo in todos:
    content += f"- {todo}\n"

print(content)