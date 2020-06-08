# python -m pdb .\uses_debug\debug_pdb.py
# python -m doctest -v .\uses_debug\debug_pdb.py
"""
Breakpoint Debugging with PDB

>>> import sys
>>> sys.version > "3.5"
True
"""

def map(func, values):
    """
    Map out the final list in function

    >>> map(add_one, list(range(9)))
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    output_values = []
    index = 0
    while index < len(values):
        output_values.append(func(values[index]))
        index += 1
    return output_values

def add_one(val):
    """
    Add the existing value by 1

    >>> add_one(2)
    3
    """
    return val + 1

map(add_one, list(range(10)))
