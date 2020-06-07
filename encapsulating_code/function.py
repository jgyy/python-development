# python -m doctest -v .\encapsulating_code\function.py
def hello_world():
    """
    Prints "Hello, World!"

    >>> hello_world()
    Hello, World!
    """
    print("Hello, World!")

hello_world()

# If we want to define an argument, we will put the
# variable name we want it to have within the parentheses
def print_name(name):
    """
    Prints the name based on argument value.

    >>> print_name("name")
    Name is name
    """
    print(f"Name is {name}")

print_name("Keith")

# assign the value from print_name to a variable
output = print_name("Keith")
print(output)

# We can declare what we're returning from a
# function using the return keyword
def add_two(num):
    """
    Returns original number plus 2

    >>> result = add_two(3)
    >>> result
    5
    """
    return num + 2

result = add_two(2)
print(result)

# Working with Multiple Arguments
def add(num1, num2):
    """
    Returns the sum of 2 numbers

    >>> result = add(1, 3)
    >>> result
    4
    """
    return num1 + num2

result = add(1, 5)
print(result)

# Using Keyword Arguments
def contact_card(name, age, car_model):
    """
    Returns a sentence based on 3 arguments.

    >>> result = contact_card("name", 32, "car_model")
    >>> result
    'name is 32 and drives a car_model'
    """
    return f"{name} is {age} and drives a {car_model}"

print(contact_card("Keith", 29, "Honda Civic"))
print(contact_card(age=29, car_model="Civic", name="Keith"))
print(contact_card("Keith", car_model="Civic", age="29"))
# contact_card(age="29", "Keith", car_model="Civic")

# Defining Default Arguments
def can_drive(age, driving_age=16):
    """
    Returns a sentence based on 3 arguments.

    >>> result = can_drive(21)
    >>> result
    True
    """
    return age >= driving_age

print(can_drive(16))
print(can_drive(16, driving_age=18))
