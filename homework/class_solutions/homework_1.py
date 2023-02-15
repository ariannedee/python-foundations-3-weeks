from random import (
    choice,
    randint,
)

NAME = 'Arianne'


def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32


assert c_to_f(0) == 32, f"c_to_f(0) was {c_to_f(0)}, not 32"
assert round(c_to_f(36.5)) == round(98), f"c_to_f(36.5) was {c_to_f(37)}, not 98"

weather_choices = ['sunny', 'cloudy', 'rainy']

weather = choice(weather_choices)
temp_c_high = randint(8, 20)
temp_c_low = randint(-5, 7)

todos = [
    'Get groceries',
    'Fix lightbulb',
    'Run 2k',
]

temp_f_high = c_to_f(temp_c_high)
temp_f_low = c_to_f(temp_c_low)

content = f"""Good morning, {NAME}

Today is going to be {weather}.
High: {temp_c_high} °C ({temp_f_high} °F)
Low: {temp_c_low} °C ({temp_f_low} °F)

"""

content += 'Remember to:\n'
for todo in todos:
    content += f'- {todo}\n'

print(content)
