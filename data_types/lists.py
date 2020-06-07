# Reading from Lists
my_list = [1, 2, 3, 4, 5]
print(my_list)
print(my_list[0])
print(my_list[2])

# If we try to access an index that is too high
# (or too low) then we'll receive an error
# print(my_list[5])

print(len(my_list))
print(my_list[0:2])
print(my_list[1:])
print(my_list[:3])
print(my_list[:3])
print(my_list[0::1])
print(my_list[0::2])

# Modifying a List
my_list[0] = "a"
print(my_list)
my_list[0:2] = 'a'
print(my_list)
my_list[0:2] = [1, 2, 3]
print(my_list)
my_list[0:2] = []
print(my_list)

# Attempting to remove an item that isn't in
# the list will result in an error
# my_list.remove(6)

# Items can also be removed from the end of a list using the pop method
print(my_list.pop())
print(my_list)
print(my_list.pop())
print(my_list)
# my_list.pop()

my_list = [1, 2, 3, 4]
print(my_list.pop(0))
print(my_list)

# Adding to the list can be done in a few ways.
# The first of which is by using the append method.
my_list.append(5)
print(my_list)
my_list.insert(1, 3)
print(my_list)
my_list.insert(0, 1)
print(my_list)
