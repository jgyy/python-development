# create strings using either single quotes ('), double quotes ("),
# or triple single or double quotes for a multi-line string.
print("single quoted string'")
print("\"double quoted string\"")
print("""'''
this is a triple
quoted string
'''""")

# combine strings using the + operator and multiply a
# string by a number using the * operator
print("'pass" + "word'")
print("'" + "Ha" * 4 + "'")

# find locates the first instance of a character (or string) in a string
print("double".find('s'))
print("double".find('u'))
print("double".find('bl'))

# lower converts all of the characters in a string to their lowercase versions
print("'TeStInG'".lower()) # "testing"
print("'another'".lower())
print("'PassWord123'".lower())

# use quotes or special characters in a string we can do that
# using the '' character
print("Tab\tDelimited")
print("New\nLine")
print("Slash\\Character")
print("'Single' in Double")
print('"Double" in Single')
print("\"Double\" in Double")