from example_25_clock import Clock

a_clock = Clock()  # Create new instance of Clock class
print(a_clock)
print(type(a_clock))

clock2 = Clock(hours=12, minutes=34)  # Can have multiple instances
print(a_clock)

a_clock.add(hours=6, minutes=30)  # Call methods on an instance
print(a_clock)

print(a_clock.hours)  # Get data attribute from an instance
print(a_clock.minutes)  # Get data attribute from an instance

help(a_clock)  # See documentation for a class
