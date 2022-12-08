from random import randint

def c_to_f(temp_c):
    return round((temp_c * 9 / 5) + 32)

assert c_to_f(0) == 32

reminders = ['Go for a walk', 'Drink water', 'Stretch']

name = input("What's your name? ").strip().title()
weather = input("What's the weather like? ")
temp_hi = randint(3, 20)
temp_lo = randint(temp_hi - 10, temp_hi - 2)

temp_hi_f = c_to_f(temp_hi)
temp_lo_f = c_to_f(temp_lo)

greeting = f"""Good morning, {name}!

Today is going to be {weather}.
High: {round(temp_hi)} °C ({round(temp_hi_f)} °F)
Low: {round(temp_lo)} °C ({round(temp_lo_f)} °F)
"""

greeting += "\nRemember to:\n"
for reminder in reminders:
    greeting += f"- {reminder}\n"

print(greeting)
