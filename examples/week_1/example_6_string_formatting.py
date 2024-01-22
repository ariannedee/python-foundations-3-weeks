temp = 30

# String concatenation
print("It will be " + str(temp) + "° today.")

# String interpolation
print("It will be %s° today." % temp)  # C-style (old)
print("It will be {}° today.".format(temp))  # Format method (newer)
print(f"It will be {temp}° today.")  # f-string (newest)

# Formatting numbers in strings
pop = 7868872451
print(f"There are {pop:,} people in the world")   # use comma as thousands separator
print(f"It will be {temp:.2f}° today.")           # format to 2 decimal places
avo_num = 6.0221408e23
print(f"Avogadro's number is {avo_num:.4g}")      # format scientific notation

string = ' Hello world '
string = string.strip()  # Removes whitespace (or input chars) from beginning/end

# Methods
print(string.upper())
print(string.lower())
print(string.title())
print(string.replace('o', '0'))
print(string.find('el'))  # returns index or -1 if not found

# Slicing
print(string[-1])
print(string[0:4])
print(string[5:])
print(string[::2])
print(string[::-1])
print(len(string))

# Splitting and joining
string_list = string.split()
print(string_list)
print('*'.join(string_list))
