x = 3

while x >= 0:  # Keep looping until condition is met
    print(x)
    x -= 1


y = 0
while True:  # Will keep looping until it encounters a break
    y += 1
    if y % 2 == 1:
        continue  # skip rest of loop and move onto next loop
    print(y)
    if y == 10:
        break
