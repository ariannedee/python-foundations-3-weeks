from random import choice


def c_to_f(temp):
    return (temp * 9 / 5) + 32


def assert_equals(actual, expected):
    assert actual == expected, f"Expected {expected} but got {actual}"


assert_equals(c_to_f(0), 32)
assert_equals(round(c_to_f(36.5)),98)


reminders = ['Go for a walk', 'Drink more water', 'Stretch']
possible_weather = ['Sunny', 'Cloudy', 'Rainy', 'Snowy']

name = 'arianne'
weather = choice(possible_weather)
temp_c_high = float(input("Temp high (in °C): "))
temp_c_low = float(input("Temp low (in °C): "))


greeting = f"""Good morning, {name.title()}!
Today will be {weather.lower()}.

High of {temp_c_high} °C ({c_to_f(temp_c_high)} °F)
Low of {temp_c_low} °C ({c_to_f(temp_c_low)} °F)

Remember to:
"""

for reminder in reminders:
    greeting += f"- {reminder}\n"


print(greeting)