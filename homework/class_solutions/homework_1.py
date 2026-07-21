import random

def c_to_f(temp_c: int | float) -> float:
    return (temp_c * 9 / 5) + 32

name = input("Name: ").strip()

weather_conditions = ["sunny", "partly cloudy", "cloudy", "rainy"]
weather = random.choice(weather_conditions)
temp_c_high = random.randint(18, 35)
temp_c_low = temp_c_high - random.randint(5, 15)

reminders = [
    "Send email to Laura",
    "Get groceries",
    "Exercise",
]

content = f"""Good morning, {name.title()}!

Today is going to be {weather.lower()}.
High: {temp_c_high}°C ({c_to_f(temp_c_high):.0f}°F)
Low: {temp_c_low}°C ({c_to_f(temp_c_low):.0f}°F)

Remember to:
"""

for reminder in reminders:
    content += f"- {reminder}\n"

print(content)