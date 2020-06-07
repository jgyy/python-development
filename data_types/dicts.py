# Dictionary
ages = { 'kevin': 59, 'alex': 29, 'bob': 40 }
print(ages)

# We can read a value from a dictionary by subscripting using the key
print(ages['kevin'])
# print(ages['billy'])

# Keys can be added or changed using subscripting and assignment
ages['kayla'] = 21
print(ages)

# Items can be removed from a dictionary using the del
# statement or by using the pop
del ages['kevin']
print(ages)
del ages
# print(ages)
ages = { 'kevin': 59, 'alex': 29, 'bob': 40 }
print(ages.pop('alex'))
print(ages)
# {}.pop('billy')

# use the get method
print(ages.get('kevin'))
print(ages.get('billy'))

# values and keys methods
ages = {'kevin': 59, 'bob': 40}
print(ages.keys())
print(list(ages.keys()))
print(ages.values())
print(list(ages.values()))

# using the dict constructor with key/value
# arguments and a list of tuples
weights = dict(kevin=160, bob=240, kayla=135)
print(weights)
colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla', 'red')])
print(colors)
