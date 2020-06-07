# The while Loop
var = 4
while True:
    print("looping")
    var -= 1
    if var <= 0:
        break

# modify something about the condition on each iteration
count = 1
while count <= 4:
    print("looping")
    count += 1

# access to the continue and break keywords
count = 0
while count < 10:
    if count % 2 == 0:
        count += 1
        continue
    print(f"We're counting odd numbers: {count}")
    count += 1

# using the break statement
count = 1
while count < 10:
    if count % 2 == 0:
        break
    print(f"We're counting odd numbers: {count}")
    count += 1
