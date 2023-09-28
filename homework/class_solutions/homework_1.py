import random


def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32


assert c_to_f(0) == 32, f"Got {c_to_f(0)}"
assert round(c_to_f(36.5)) == 98, f"Got {c_to_f(0)}"

reminders = [
    "Go for a walk",
    "Stretch",
]

name = input("What's your name? ").strip().title()

weather = ["sunny", "cloudy", "rainy"]

today_weather = random.choice(weather)
temp_c_high = random.randint(10, 25)
temp_c_low = random.randint(0, 10)


content = f"""Hello {name},

Today is going to be {today_weather}.

High of {temp_c_high}°C ({c_to_f(temp_c_high)}°F) 
Low of {temp_c_low}°C ({c_to_f(temp_c_low)}°F) 

Remember to:
"""

for reminder in reminders:
    content += f"- {reminder}\n"


print(content)
