# standard comparison operators
print(1 < 2)
print(0 > 2)
print(2 == 1)
print(2 != 1)
print(3.0 >= 3.0)
print(3.1 <= 3.0)

# comparisons of types that don't match up = error
# 3.1 <= "this"
print(3 <= 3.1)
print(1.1 == "1.1")
print(1.1 == float("1.1"))

# compare strings
print("this" == "this")
print("this" == "This")
print("b" > "a")
print("abc" < "b")

# The in Check
print(2 in [1, 2, 3])
print(4 in [1, 2, 3])
print(2 not in [1, 2, 3])
print(4 not in [1, 2, 3])

# if/elif/else
if True:
    print("Was True")
if False:
    print("Was True")
else:
    print("Was False")

# elif CONDITION: statement
name = "Kevin"
if len(name) >= 6:
    print("name is long")
elif len(name) == 5:
    print("name is 5 characters")
elif len(name) >= 4:
    print("name is 4 or more")
else:
    print("name is short")
