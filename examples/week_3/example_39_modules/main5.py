"""
Can import from a package if its __init__.py has:
  - imports (e.g. red_fish)
  - definitions (e.g. n_fish)
"""
from things import red_fish, blue_fish, n_fish

print(red_fish())
print(blue_fish())

print(n_fish(1))
print(n_fish(2))
