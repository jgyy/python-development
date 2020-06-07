# The not Operation
name = ""
print(not name)
if not name:
    print("No name given")

# The or Operation
first = ""
last = "Thompson"
if first or last:
    print("The user has a first or last name")

# If both first and last were "falsy" then the print would never happen
first = ""
last = ""
if first or last:
    print("The user has a first or last name")

# set default values for variables
last = ""
last_name = last or "Doe"
print(last_name)

# The or operation will return the first value that is
# "truthy" or the last value in the chain
print(0 or 1)
print(1 or 2)

# The and Operation
first = "Keith"
last = ""
if first and last:
    print(f"Full name: {first} {last}")
elif first:
    print(f"First name: {first}")
elif last:
    print(f"Last name: {last}")

# the same thing with both first and last
first = "Keith"
last = "Thompson"
if first and last:
    print(f"Full name: {first} {last}")
elif first:
    print(f"First name: {first}")
elif last:
    print(f"Last name: {last}")

# The and operation will return the first value that
# is "falsy" or the last value in the chain
print(0 and 1)
print(1 and 2)
print((1 == 1) and print("Something"))
print((1 == 2) and print("Something"))
