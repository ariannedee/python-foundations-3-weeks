def c_to_f(temp):
    return (temp * 9 / 5) + 32

reminders = [
    'Drink water',
    'Go for a walk',
    'Renew car insurance',
]

name = input("What's your name? ").strip().title()
weather = input("What's the weather like today? ").strip().lower()
temp_c_high = float(input("High temp in °C? "))
temp_c_low = float(input("Low temp in °C? "))

temp_f_high = c_to_f(temp_c_high)
temp_f_low = c_to_f(temp_c_low)

print('------------------------------')

content = f"""
Good morning, {name}

Today is going to be {weather}.
High: {temp_c_high} °C ({temp_f_high} °F)
Low: {temp_c_low} °C ({temp_f_low} °F)

"""

content += 'Remember to:\n'
for reminder in reminders:
    content += f'- {reminder}\n'

# More API content

print(content)
