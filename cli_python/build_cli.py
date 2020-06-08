# python -m doctest -v .\cli_python\build_cli.py
"""
The argparse Package

>>> import sys
>>> sys.version > "3.5"
True
"""
from argparse import Action, ArgumentParser

class DriverAction(Action):
    """
    DriverAction only provides the __call__ function based on Action

    >>> type(DriverAction)
    <class 'type'>
    """
    def __call__(self, parser, namespace, values, option_string=None):
        """
        provides driver and destination

        >>> parser = create_parser()
        >>> args = parser.parse_args(['https://some_urls', '--driver', 's3', 'bucket_name'])
        >>> (args.url, args.driver, args.destination)
        ('https://some_urls', 's3', 'bucket_name')
        """
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    """
    creates parser based on ArgumentParser

    >>> parser = create_parser()
    >>> args = parser.parse_args(['https://some_url', '--driver', 's3', 's3_bucket_name'])
    >>> (args.url, args.driver, args.destination)
    ('https://some_url', 's3', 's3_bucket_name')
    """
    parser = ArgumentParser(description="""
    Back up PostgreSQL databases locally or to AWS S3.
    """)
    parser.add_argument("url", help="URL of database to backup")
    parser.add_argument("--driver",
            help="how & where to store backup",
            nargs=2,
            action=DriverAction,
            required=True)
    return parser

parser = create_parser()
args = parser.parse_args(['https://some_url', '--driver', 's3', 'bucket_name'])
print(args.url)
print(args.driver)
print(args.destination)
# print(parser.parse_args())
