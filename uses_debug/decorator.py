# python -m doctest -v .\uses_debug\decorator.py
"""
>>> import sys
>>> sys.version > "3.5"
True
"""

def inspect(func):
    """
    Inspect acts as a decorator for combine function

    >>> result = inspect(combine(4, b=3))
    Running combine
    Result: 7
    >>> type(result)
    <class 'function'>
    """
    def wrapped_func(*args, **kwargs):
        """
        Wrapper function for combine with arguments

        >>> result = inspect(combine(1, b=2))
        Running combine
        Result: 3
        >>> type(result)
        <class 'function'>
        """
        print(f"Running {func.__name__}")
        val = func(*args, **kwargs)
        print(f"Result: {val}")
        return val

    return wrapped_func

@inspect
def combine(a, b):
    return a + b

combine(1, b=2)

# inspect and combine omitted
class User:
    """
    User class with query url, username and fullname

    >>> user = User('Keith', 'Thompson')
    >>> user.base_url
    'https://example.com/api'
    """
    base_url = 'https://example.com/api'

    def __init__(self, first_name, last_name):
        """
        Get the first and last name of the user

        >>> user = User('Keith', 'Thompson')
        >>> (user.first_name, user.last_name)
        ('Keith', 'Thompson')
        """
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def query(cls, query_string):
        """
        Return query url and query string

        >>> User.query('name=test')
        'https://example.com/api?name=test'
        """
        return cls.base_url + '?' + query_string

    @staticmethod
    def name():
        """
        Return only a certain name without parameters

        >>> User.name()
        'Kevin Bacon'
        """
        return "Kevin Bacon"

    @property
    def full_name(self):
        """
        Get the full name of the user

        >>> user = User('Keith', 'Thompson')
        >>> user.full_name
        'Keith Thompson'
        """
        return f"{self.first_name} {self.last_name}"

print(User.name)
print(User.name())
print(User.query('name=test'))
user = User('Keith', 'Thompson')
print(user.base_url)
print(user.full_name)
