import random

def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32

reminders = [
    "drink water",
    "stretch for 10 mins",
    "meditate"
]

name = input("Name: ").strip().title()

weather = random.choice(["sunny", "cloudy", "rainy"])
temp_c_high = random.randint(15, 30)
temp_c_low = temp_c_high - random.randint(5, 10)

content = f"""Good morning, {name}!
Today is going to be {weather}.

High: {temp_c_high:.0f}°C ({c_to_f(temp_c_high):.0f}°F)
Low: {temp_c_low:.0f}°C ({c_to_f(temp_c_low):.0f}°F)

Remember to:"""

for reminder in reminders:
    content += "\n- " + reminder.capitalize()

print(content)