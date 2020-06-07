# The for Loop
colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    print(color)

# terminate the loop if we see the string 'red'
colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    if color == 'blue':
        continue
    elif color == 'red':
        break
    print(color)

# tuple example
point = (2.1, 3.2, 7.6)
for value in point:
    print(value)

# dictionary example
ages = {'kevin': 59, 'bob': 40, 'kayla': 21}
for key in ages:
    print(key)

# string example
for letter in "my_string":
    print(letter)

# Unpacking Multiple Items in a for Loop
list_of_points = [(1, 2), (2, 3), (3, 4)]
for x, y in list_of_points:
    print(f"x: {x}, y: {y}")

# use the items method on our ages dictionary
# to list out the names and ages
for name, age in ages.items():
    print(f"Person Named: {name}")
    print(f"Age of: {age}")
