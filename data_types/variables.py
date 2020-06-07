# Working with Variables
my_str = "This is a simple string"
print(my_str)

my_str += " testing"
print(my_str)

my_str = 1
print(my_str)

# we assign a variable with another variable it will be assigned to the
# result of the variable and not whatever that varible points to later.
my_str = 1
my_int = my_str
my_str = "testing"
print(my_int)
print(my_str)
