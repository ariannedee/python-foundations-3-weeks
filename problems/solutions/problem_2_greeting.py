"""
Write a program that takes as input:
    - your name
    - a weather condition
    - high temperature
    - low temperature

And prints a greeting:
    Good morning, {name}!
    Today is going to be {condition}.
    High: {high_c} °C ({high_f} °F)
    Low: {low_c} °C ({low_f} °F)

Scenario 2 practice
"""

name = input("What's your name? ").strip().title()
weather = input("What's the weather like today? ").strip().lower()
temp_c_high = float(input("High temp in °C? "))
temp_c_low = float(input("Low temp in °C? "))

temp_f_high = (temp_c_high * 9 / 5) + 32
temp_f_low = (temp_c_low * 9 / 5) + 32

print('------------------------------')
print(f'Good morning, {name}')
print(f'Today is going to be {weather}.')
print(f'High: {temp_c_high} °C ({temp_f_high} °F)')
print(f'Low: {temp_c_low} °C ({temp_f_low} °F)')
